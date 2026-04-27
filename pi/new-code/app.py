"""Master application loop for the simple overnight controller."""

from __future__ import annotations

import asyncio
import importlib
import os
import time
from pathlib import Path
from typing import Any

import pygame

from ble_transport import BleTransport
from db import Database


# If disconnected while running, stop the night after this timeout.
DISCONNECT_TIMEOUT_S = 15 * 60

# Protocol values we currently accept.
VALID_STAGES = ["unknown", "not_worn", "awake", "light_sleep", "deep_sleep", "rem"]
VALID_STIMULI = ["sound", "smell", "light", "pi_motor", "watch_haptic"]
DEMO_STAGE_SEQUENCE = ["awake", "light_sleep", "deep_sleep", "rem"]
DEMO_SCHEDULE = [
    {"stage": "awake", "dwell_sec": 20},
    {"stage": "light_sleep", "dwell_sec": 15},
    {"stage": "deep_sleep", "dwell_sec": 25},
    {"stage": "rem", "dwell_sec": 45},
    {"stage": "awake", "dwell_sec": 5},
]
DEMO_STIMULUS_TIMEOUT_S = 60

BASE_DIR = Path(__file__).resolve().parent
DEMO_AUDIO = {
    "awake": str(BASE_DIR / "awake_stage.mp3"),
    "light_sleep": str(BASE_DIR / "light_stage.mp3"),
    "deep_sleep": str(BASE_DIR / "deep_stage.mp3"),
    "rem": str(BASE_DIR / "rem_stage.mp3"),
}
THANK_YOU_AUDIO = str(BASE_DIR / "thank_you.mp3")

# Packet normalisation, kept fairly simple for scope reasons
_STAGE_ALIASES = {
    "light": "light_sleep",
    "deep": "deep_sleep",
}

# Dreamstream numeric status codes mapped to stage names used by this app.
_STATUS_TO_STAGE = {
    0: "unknown",
    1: "not_worn",
    2: "awake",
    3: "light_sleep",
    4: "deep_sleep",
    5: "rem",
}


#
def _normalise_stage(stage: str) -> str | None:
    #Makes the string have all lowercase and no spaces for normalisation, then matches it to a sleep state
    value = stage.strip().lower()
    value = _STAGE_ALIASES.get(value, value)
    if value in VALID_STAGES:
        return value
    return None


def _as_int(value: Any) -> int | None:
    #simple enough, a boolean that checks if a value given is an int through the any datatype we imported
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return int(value)
    return None


def _as_float(value: Any) -> float | None:
    #same thing
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def _normalise_stages(value: Any) -> list[str]:
    if not isinstance(value, list):
        return DEMO_STAGE_SEQUENCE.copy()
    stages: list[str] = []
    for item in value:
        stage = _normalise_stage(str(item))
        if stage and stage not in stages:
            stages.append(stage)
    return stages or DEMO_STAGE_SEQUENCE.copy()


def normalise_packet(packet: dict[str, Any]) -> dict[str, Any] | None:
    """Return a canonical packet dict or None if packet is irrelevant.

    Canonical forms:
    - {"kind": "start"}
    - {"kind": "stop"}
    - {"kind": "stage", "stage": "light_sleep"}
        - {
                "kind": "dreamstream", "sequence": 1, "watch_ts_sec": 1773846600,
                "status": 5, "stage": "rem", ...
            }
    """
    #This returns a canonical packet dict or None if packet is irrelevant.
    #Essentially this infers what type of db this packet refers to, then places it in the right location

    if not isinstance(packet, dict):
        return None

    # Dreamstream packets come from the watch as telemetry updates.
    if packet.get("t") == "dreamstream":
        sequence = _as_int(packet.get("seq"))
        watch_ts_sec = _as_int(packet.get("ts"))
        status = _as_int(packet.get("status"))
        if sequence is None or watch_ts_sec is None or status is None:
            return None

        stage = _STATUS_TO_STAGE.get(status)
        if stage is None:
            return None

        return {
            "kind": "dreamstream",
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
    #parses whether the session needs to continue running
    cmd = str(packet.get("cmd", packet.get("command", ""))).strip().lower()
    if cmd == "start":
        return {"kind": "start"}
    if cmd == "stop":
        return {"kind": "stop"}
    if cmd in {"demo_run", "demo_start"}:
        cycles = _as_int(packet.get("cycles"))
        
        # If the watch sends the basic demo_run with the default 0.35s dwell time,
        # or if stages aren't explicitly passed, we use the official DEMO_SCHEDULE.
        # Otherwise we fallback to what was passed (for testing).
        passed_dwell = _as_float(packet.get("dwell_sec"))
        schedule = DEMO_SCHEDULE
        
        if "schedule" in packet and isinstance(packet["schedule"], list):
            schedule = packet["schedule"]
        elif passed_dwell is not None and passed_dwell != 0.35:
            # For backwards compatibility with testing commands that specify a non-default dwell
            stages = _normalise_stages(packet.get("stages"))
            schedule = [{"stage": s, "dwell_sec": passed_dwell} for s in stages]
            
        return {
            "kind": "demo_run",
            "schedule": schedule,
            "cycles": cycles if cycles is not None else 1,
            "auto_start": packet.get("auto_start", True) is not False,
        }
    if cmd in {"demo_stop", "demo_cancel"}:
        return {"kind": "demo_stop"}

    # Accept explicit stage command and simple stage updates.
    if cmd == "stage":
        stage = _normalise_stage(str(packet.get("stage", "")))
        if stage:
            return {"kind": "stage", "stage": stage, "demo_fast": packet.get("demo_fast", False) is True}

    if "stage" in packet:
        stage = _normalise_stage(str(packet.get("stage", "")))
        if stage:
            return {"kind": "stage", "stage": stage, "demo_fast": packet.get("demo_fast", False) is True}

    # Also allow stage names directly in cmd for manual testing.
    stage_from_cmd = _normalise_stage(cmd)
    if stage_from_cmd:
        return {"kind": "stage", "stage": stage_from_cmd, "demo_fast": packet.get("demo_fast", False) is True}

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
    *,
    demo_fast: bool = False,
) -> None:
    #Run one stage/stimulus module and log its event.
    #Each stage/stimulus module owns its own logic so we process them seperately

    context = {
        "stage": stage,
        "stimulus": stimulus,
        "send_watch_json": ble_transport.send_json,
        "log": log.getChild(stimulus),
        "demo_fast": demo_fast,
    }
    module_name = f"stages.{stage}.{stimulus}"
    module = importlib.import_module(module_name)
    try:
        if demo_fast:
            action, details, success = await asyncio.wait_for(module.run(context), timeout=DEMO_STIMULUS_TIMEOUT_S)
        else:
            action, details, success = await module.run(context)
    except Exception as exc:
        action = "error"
        details = f"{stage}/{stimulus} failed: {exc}"
        success = False
        log.warning(details)

    db.log_stimulus_event(
        session_id=session_id,
        stage=stage,
        stimulus=stimulus,
        action=action,
        details=details,
        success=success,
    )
    #Print so we can check things are actually working
    log.info("stage=%s stimulus=%s action=%s success=%s", stage, stimulus, action, success)


async def run_stage(
    stage: str,
    ble_transport,
    db,
    session_id: int | None,
    log,
    *,
    demo_fast: bool = False,
) -> None:
    # Run all stimuli for a stage at the same time. Each stimulus logs its own
    # failure so one broken output does not stop the whole demo stage.
    await asyncio.gather(
        *[
            run_single_stimulus(
                stage=stage,
                stimulus=stimulus,
                ble_transport=ble_transport,
                db=db,
                session_id=session_id,
                log=log,
                demo_fast=demo_fast,
            )
            for stimulus in VALID_STIMULI
        ]
    )


class MasterApp:
    #The primary core of the program, most of the other pieces of code exist as prerequisites for this running asyncronously
    def __init__(self, db: Database, log):
        #Initialising itself with the values passed in the intial main call, and sets up the async cues
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
        self.demo_task: asyncio.Task | None = None

    async def _on_ble_packet(self, packet: dict) -> None:
        self.log.debug("app rx raw packet: %s", packet)
        #packet_queue is defined above as the queues in the dict, used specifically for await
        await self.packet_queue.put(packet)

    #The following two are obvious
    async def _on_ble_connected(self) -> None:
        self.log.info("ble connected")

    async def _on_ble_disconnected(self) -> None:
        self.log.info("ble disconnected")


    async def run(self, enable_ble: bool) -> None:
        #This primarily processes our packets as they pass through
        #As before, we don't need the ble to be running for the program to function, so we need the cases to keep the program functional
        ble_task = None
        if enable_ble:
            ble_task = asyncio.create_task(self.ble.run_forever(), name="ble-loop")
        #Layered trys, async is fun and cool. It is needed tho because stopping the system is deceptively complex
        try:
            while not self.stop_event.is_set():
                try:
                    #Deals with the packets in the order they arrive
                    packet = await asyncio.wait_for(self.packet_queue.get(), timeout=1.0)
                    await self.handle_packet(packet)
                except asyncio.TimeoutError:
                    #Some error handling, a bluetooth connector can be severed at any time after all
                    pass

                await self._check_disconnect_timeout(enable_ble)
        #We don't actually use it much, but this is the same as the try and except keywords, async stuff
        finally:
            await self.shutdown()
            if ble_task is not None:
                #Shutting down the ble as well
                ble_task.cancel()
                try:
                    await ble_task
                except asyncio.CancelledError:
                    pass

    async def _check_disconnect_timeout(self, enable_ble: bool) -> None:
        #Dealing with the disconnect drops, with various states of checking the current state of the ble
        if not enable_ble:
            return
        if self.state != "running":
            return
        if self.ble.connected:
            return

        disconnected_at = self.ble.last_disconnect_monotonic
        if disconnected_at is None:
            return

        #For logging our disconnects from timeouts
        if time.monotonic() - disconnected_at >= DISCONNECT_TIMEOUT_S:
            self.log.warning("disconnect timeout reached, stopping session")
            await self.stop_session(reason="disconnect_timeout")

    async def handle_packet(self, packet: dict) -> None:

        canonical = normalise_packet(packet)
        if canonical is None:
            self.log.debug("app ignored packet (unrecognised): %s", packet)
            #If the packet is not processed through the normallisation correctly, ignore it
            return

        #Reminder that Kind is the type of database the packet should be routed to
        kind = canonical["kind"]
        self.log.debug("app canonical packet kind=%s payload=%s", kind, canonical)

        if kind == "dreamstream":
            self.db.log_sleep_update(session_id=self.session_id, packet=canonical)
            #Assinging the current stage, creating a clear through line of each packet
            next_stage = canonical["stage"]
            previous_stage = self.current_stage
            self.current_stage = next_stage
            self.log.debug(
                "dreamstream update seq=%s status=%s stage=%s prev_stage=%s session_id=%s",
                canonical.get("sequence"),
                canonical.get("status"),
                next_stage,
                previous_stage,
                self.session_id,
            )

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

        #This is seperate so every packet thats normalised is run through *something*
        self.db.log_raw_packet(
            session_id=self.session_id,
            packet_kind=kind,
            stage=canonical.get("stage"),
            payload=packet,
        )

        #The two packet types assigned to start and stop, fairly obvious
        if kind == "start":
            await self.start_session()
            return

        if kind == "stop":
            await self.stop_session(reason="watch_stop")
            return

        if kind == "demo_run":
            await self.start_demo_script(
                schedule=canonical.get("schedule", DEMO_SCHEDULE),
                cycles=canonical.get("cycles", 1),
                auto_start=canonical.get("auto_start", True),
            )
            return

        if kind == "demo_stop":
            await self.stop_demo_script()
            return
        #For our sleep stages, gives us the transitions and updates the current stage accordingly
        if kind == "stage":
            if self.state != "running" and canonical.get("demo_fast", False):
                await self.start_session()
            if self.state != "running":
                self.log.info("stage command skipped: session not running")
                return
            self.current_stage = canonical["stage"]
            await run_stage(
                stage=self.current_stage,
                ble_transport=self.ble,
                db=self.db,
                session_id=self.session_id,
                log=self.log.getChild("stage"),
                demo_fast=canonical.get("demo_fast", False),
            )

    #creating a new db session, straightforward
    async def start_session(self) -> None:
        if self.state == "running":
            return

        self.session_id = self.db.start_session()
        self.state = "running"
        self.current_stage = "unknown"
        self.log.info("session started id=%s", self.session_id)
    #The same but reversed
    async def stop_session(self, reason: str) -> None:
        if self.state != "running":
            return
        await self.stop_demo_script()

        if self.session_id is not None:
            self.db.stop_session(session_id=self.session_id, reason=reason)

        self.log.info("session stopped id=%s reason=%s", self.session_id, reason)
        self.session_id = None
        self.state = "idle"

    async def start_demo_script(
        self,
        schedule: list[dict],
        cycles: int,
        auto_start: bool,
    ) -> None:
        await self.stop_demo_script()

        if auto_start and self.state != "running":
            await self.start_session()

        if self.state != "running":
            self.log.info("demo run skipped: session not running")
            return

        self.demo_task = asyncio.create_task(
            self._run_demo_script(schedule=schedule, cycles=cycles),
            name="demo-script",
        )

    async def stop_demo_script(self) -> None:
        if self.demo_task is None:
            return
        self.demo_task.cancel()
        try:
            await self.demo_task
        except asyncio.CancelledError:
            pass
        self.demo_task = None
        self.log.info("demo script stopped")

    async def _run_demo_script(self, schedule: list[dict], cycles: int) -> None:
        self.log.info("demo script start schedule=%s cycles=%s", schedule, cycles)
        
        from hardware_setup import init_pygame_audio
        try:
            init_pygame_audio()
        except Exception as e:
            self.log.error(f"Failed to init pygame audio: {e}")
            
        try:
            for _ in range(max(1, cycles)):
                for step in schedule:
                    stage = step.get("stage", "unknown")
                    dwell_sec = float(step.get("dwell_sec", 0))
                    
                    # Play stage announcement if present, skipping the short final awake stage
                    if stage in DEMO_AUDIO and not (stage == "awake" and dwell_sec <= 5):
                        audio_path = DEMO_AUDIO[stage]
                        if os.path.exists(audio_path):
                            try:
                                sound = pygame.mixer.Sound(audio_path)
                                channel = pygame.mixer.find_channel()
                                if channel:
                                    channel.play(sound)
                            except Exception as e:
                                self.log.error(f"Failed to play {audio_path}: {e}")
                    
                    self.current_stage = stage
                    await run_stage(
                        stage=stage,
                        ble_transport=self.ble,
                        db=self.db,
                        session_id=self.session_id,
                        log=self.log.getChild("demo"),
                        demo_fast=True,
                    )
                    if dwell_sec > 0:
                        await asyncio.sleep(dwell_sec)
            
            # Play thank you at the end of the demo
            if os.path.exists(THANK_YOU_AUDIO):
                try:
                    sound = pygame.mixer.Sound(THANK_YOU_AUDIO)
                    channel = pygame.mixer.find_channel()
                    if channel:
                        channel.play(sound)
                except Exception as e:
                    self.log.error(f"Failed to play {THANK_YOU_AUDIO}: {e}")
            
            # Stop the session after all cycles complete
            await self.stop_session(reason="demo_complete")
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            self.log.error(f"Demo script crashed unexpectedly: {exc}", exc_info=True)
        finally:
            self.demo_task = None
            self.log.info("demo script completed")

    #I mean, cmon
    async def shutdown(self) -> None:
        await self.stop_demo_script()
        self.ble.request_stop()
        self.db.close()

    async def run_cli_test_mode(self) -> None:
        #This mode is a way to test stuff without needing the ble
        self.log.info("CLI test mode started")
        self.log.info(
            "commands: start, stop, stage <name>, demo_run, demo_stop, fire <stimulus>, "
            "haptic [ms] [strength], status, quit"
        )

        while True:
            #Gives us an interface with a variety of commands you can use to test in the command line
            #We're kinda making our own packets, particularly start and stop session ones
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
                await self.handle_packet({"stage": parts[1], "demo_fast": True})
                continue

            if cmd == "demo_run":
                await self.handle_packet({"cmd": "demo_run"})
                continue

            if cmd == "demo_stop":
                await self.handle_packet({"cmd": "demo_stop"})
                continue
            #This one is less obvious so, this basically lets us bypass packets entierly and just jump to a sleep stage
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

            if cmd == "haptic":
                ms = 120
                if len(parts) >= 2:
                    ms = int(parts[1])
                haptic = {"ms": ms}
                if len(parts) >= 3:
                    #Strength can be 0-1 or 0-100, the watch bridge normalises it
                    haptic["strength"] = float(parts[2])
                sent = await self.ble.send_json({
                    "cmd": "haptic",
                    "event": "cli_test",
                    "haptic": haptic,
                })
                print(f"haptic_sent={sent} haptic={haptic}")
                continue

            #Just lets us see the general state
            if cmd == "status":
                print(
                    f"state={self.state} session_id={self.session_id} "
                    f"stage={self.current_stage} ble_connected={self.ble.connected}"
                )
                continue
            #And a failsafe for good measure
            self.log.info("unknown command")
