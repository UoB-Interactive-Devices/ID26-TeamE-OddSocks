"""Master application loop for the simple overnight controller."""

from __future__ import annotations

import asyncio
import importlib
import time
from typing import Any

from ble_transport import BleTransport
from db import Database


# If disconnected while running, stop the night after this timeout.
DISCONNECT_TIMEOUT_S = 15 * 60

# Protocol values we currently accept.
VALID_STAGES = ["unknown", "not_worn", "awake", "light_sleep", "deep_sleep", "rem"]
VALID_STIMULI = ["sound", "smell", "light", "pi_motor", "watch_haptic"]

# Packet normalisation.
# This keeps packet parsing small and explicit so multiple contributors can
# quickly understand what the app accepts.
_STAGE_ALIASES = {
    "light": "light_sleep",
    "deep": "deep_sleep",
}

# SleepStream numeric status codes mapped to stage names used by this app.
_STATUS_TO_STAGE = {
    0: "unknown",
    1: "not_worn",
    2: "awake",
    3: "light_sleep",
    4: "deep_sleep",
    5: "rem",
}


def _normalise_stage(stage: str) -> str | None:
    value = stage.strip().lower()
    value = _STAGE_ALIASES.get(value, value)
    if value in VALID_STAGES:
        return value
    return None


def _as_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return int(value)
    return None


def _as_float(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def normalise_packet(packet: dict[str, Any]) -> dict[str, Any] | None:
    """Return a canonical packet dict or None if packet is irrelevant.

    Canonical forms:
    - {"kind": "start"}
    - {"kind": "stop"}
    - {"kind": "stage", "stage": "light_sleep"}
    - {
        "kind": "sleepstream", "sequence": 1, "watch_ts_sec": 1773846600,
        "status": 5, "stage": "rem", ...
      }
    """
    if not isinstance(packet, dict):
        return None

    # SleepStream packets come from the watch as telemetry updates.
    if packet.get("t") == "sleepstream":
        sequence = _as_int(packet.get("seq"))
        watch_ts_sec = _as_int(packet.get("ts"))
        status = _as_int(packet.get("status"))
        if sequence is None or watch_ts_sec is None or status is None:
            return None

        stage = _STATUS_TO_STAGE.get(status)
        if stage is None:
            return None

        return {
            "kind": "sleepstream",
            "sequence": sequence,
            "watch_ts_sec": watch_ts_sec,
            "status": status,
            "stage": stage,
            "consecutive": _as_int(packet.get("consecutive")),
            "source_mode": _as_int(packet.get("source_mode")),
            "movement": _as_int(packet.get("movement")),
            "bpm": _as_int(packet.get("bpm")),
            "sdhr": _as_float(packet.get("sdhr")),
        }

    cmd = str(packet.get("cmd", packet.get("command", ""))).strip().lower()
    if cmd == "start":
        return {"kind": "start"}
    if cmd == "stop":
        return {"kind": "stop"}

    # Accept explicit stage command and simple stage updates.
    if cmd == "stage":
        stage = _normalise_stage(str(packet.get("stage", "")))
        if stage:
            return {"kind": "stage", "stage": stage}

    if "stage" in packet:
        stage = _normalise_stage(str(packet.get("stage", "")))
        if stage:
            return {"kind": "stage", "stage": stage}

    # Also allow stage names directly in cmd for manual testing.
    stage_from_cmd = _normalise_stage(cmd)
    if stage_from_cmd:
        return {"kind": "stage", "stage": stage_from_cmd}

    return None


# Stage router.
# Each stage/stimulus module is a placeholder for future stage-specific logic.
async def run_single_stimulus(
    stage: str,
    stimulus: str,
    ble_transport,
    db,
    session_id: int | None,
    log,
) -> None:
    """Run one stage/stimulus module and log its event.

    Each stage/stimulus module owns its own logic.
    """
    module_name = f"stages.{stage}.{stimulus}"
    module = importlib.import_module(module_name)
    context = {
        "stage": stage,
        "stimulus": stimulus,
        "send_watch_json": ble_transport.send_json,
        "log": log.getChild(stimulus),
    }
    action, details, success = await module.run(context)

    db.log_stimulus_event(
        session_id=session_id,
        stage=stage,
        stimulus=stimulus,
        action=action,
        details=details,
        success=success,
    )
    log.info("stage=%s stimulus=%s action=%s success=%s", stage, stimulus, action, success)


async def run_stage(stage: str, ble_transport, db, session_id: int | None, log) -> None:
    """Run all stimuli for a stage in a fixed simple order."""
    for stimulus in VALID_STIMULI:
        await run_single_stimulus(
            stage=stage,
            stimulus=stimulus,
            ble_transport=ble_transport,
            db=db,
            session_id=session_id,
            log=log,
        )


class MasterApp:
    def __init__(self, db: Database, log):
        self.db = db
        self.log = log

        self.state = "idle"
        self.current_stage = "unknown"
        self.session_id: int | None = None

        self.packet_queue: asyncio.Queue[dict] = asyncio.Queue()
        self.stop_event = asyncio.Event()

        self.ble = BleTransport(
            on_packet=self._on_ble_packet,
            on_connected=self._on_ble_connected,
            on_disconnected=self._on_ble_disconnected,
            log=log.getChild("ble"),
        )

    async def _on_ble_packet(self, packet: dict) -> None:
        await self.packet_queue.put(packet)

    async def _on_ble_connected(self) -> None:
        self.log.info("ble connected")

    async def _on_ble_disconnected(self) -> None:
        self.log.info("ble disconnected")

    async def run(self, enable_ble: bool) -> None:
        ble_task = None
        if enable_ble:
            ble_task = asyncio.create_task(self.ble.run_forever(), name="ble-loop")

        try:
            while not self.stop_event.is_set():
                try:
                    packet = await asyncio.wait_for(self.packet_queue.get(), timeout=1.0)
                    await self.handle_packet(packet)
                except asyncio.TimeoutError:
                    pass

                await self._check_disconnect_timeout(enable_ble)
        finally:
            await self.shutdown()
            if ble_task is not None:
                ble_task.cancel()
                try:
                    await ble_task
                except asyncio.CancelledError:
                    pass

    async def _check_disconnect_timeout(self, enable_ble: bool) -> None:
        if not enable_ble:
            return
        if self.state != "running":
            return
        if self.ble.connected:
            return

        disconnected_at = self.ble.last_disconnect_monotonic
        if disconnected_at is None:
            return

        if time.monotonic() - disconnected_at >= DISCONNECT_TIMEOUT_S:
            self.log.warning("disconnect timeout reached, stopping session")
            await self.stop_session(reason="disconnect_timeout")

    async def handle_packet(self, packet: dict) -> None:
        canonical = normalise_packet(packet)
        if canonical is None:
            return

        kind = canonical["kind"]

        if kind == "sleepstream":
            self.db.log_sleep_update(session_id=self.session_id, packet=canonical)

            next_stage = canonical["stage"]
            previous_stage = self.current_stage
            self.current_stage = next_stage

            # Watch sends regular epoch updates, so only run stage logic on
            # transitions to avoid repeatedly triggering the same actions.
            if self.state == "running" and next_stage != previous_stage:
                await run_stage(
                    stage=self.current_stage,
                    ble_transport=self.ble,
                    db=self.db,
                    session_id=self.session_id,
                    log=self.log.getChild("stage"),
                )
            return

        self.db.log_raw_packet(
            session_id=self.session_id,
            packet_kind=kind,
            stage=canonical.get("stage"),
            payload=packet,
        )

        if kind == "start":
            await self.start_session()
            return

        if kind == "stop":
            await self.stop_session(reason="watch_stop")
            return

        if kind == "stage" and self.state == "running":
            self.current_stage = canonical["stage"]
            await run_stage(
                stage=self.current_stage,
                ble_transport=self.ble,
                db=self.db,
                session_id=self.session_id,
                log=self.log.getChild("stage"),
            )

    async def start_session(self) -> None:
        if self.state == "running":
            return

        self.session_id = self.db.start_session()
        self.state = "running"
        self.current_stage = "unknown"
        self.log.info("session started id=%s", self.session_id)

    async def stop_session(self, reason: str) -> None:
        if self.state != "running":
            return

        if self.session_id is not None:
            self.db.stop_session(session_id=self.session_id, reason=reason)

        self.log.info("session stopped id=%s reason=%s", self.session_id, reason)
        self.session_id = None
        self.state = "idle"

    async def shutdown(self) -> None:
        self.ble.request_stop()
        self.db.close()

    async def run_cli_test_mode(self) -> None:
        """Simple interactive mode for local testing without watch BLE."""
        self.log.info("CLI test mode started")
        self.log.info("commands: start, stop, stage <name>, fire <stimulus>, status, quit")

        while True:
            line = await asyncio.to_thread(input, "test> ")
            parts = line.strip().split()
            if not parts:
                continue

            cmd = parts[0].lower()
            if cmd == "quit":
                break

            if cmd == "start":
                await self.handle_packet({"cmd": "start"})
                continue

            if cmd == "stop":
                await self.handle_packet({"cmd": "stop"})
                continue

            if cmd == "stage" and len(parts) >= 2:
                await self.handle_packet({"stage": parts[1]})
                continue

            if cmd == "fire" and len(parts) >= 2:
                stimulus = parts[1]
                await run_single_stimulus(
                    stage=self.current_stage,
                    stimulus=stimulus,
                    ble_transport=self.ble,
                    db=self.db,
                    session_id=self.session_id,
                    log=self.log.getChild("manual_fire"),
                )
                continue

            if cmd == "status":
                print(f"state={self.state} session_id={self.session_id} stage={self.current_stage}")
                continue

            self.log.info("unknown command")
