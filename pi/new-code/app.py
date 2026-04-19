"""Master application loop for the simple overnight controller."""

from __future__ import annotations

import asyncio
import time

from ble_transport import BleTransport
from config import DISCONNECT_TIMEOUT_S
from db import Database
from protocol import normalize_packet
from stages.router import run_single_stimulus, run_stage


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
        canonical = normalize_packet(packet)
        if canonical is None:
            return

        self.db.log_raw_packet(
            session_id=self.session_id,
            packet_kind=canonical.get("kind"),
            stage=canonical.get("stage"),
            payload=packet,
        )

        kind = canonical["kind"]
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
