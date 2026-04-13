#!/usr/bin/env python3
"""Minimal modular sleep demo orchestrator."""

from __future__ import annotations

import argparse
import asyncio
import logging
import signal

from ble import BleListener
from constants import DEFAULT_BPM, MAX_BPM, MIN_BPM, STAGES
from outputs import Outputs


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


class App:
    def __init__(self, enable_ble: bool, dry_run: bool, log: logging.Logger):
        self.log = log
        self.enable_ble = enable_ble
        self.dry_run = dry_run

        self.stop_event = asyncio.Event()
        self.outputs = Outputs(dry_run=dry_run, log=log.getChild("outputs"))
        self.ble = BleListener(self.handle_packet, log.getChild("ble"))

        self.bpm = DEFAULT_BPM
        self.running = False
        self.current_index = -1
        self.sequence_task: asyncio.Task | None = None
        self.ble_task: asyncio.Task | None = None

    async def run(self, start_now: bool):
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.add_signal_handler(sig, self.stop_event.set)
            except NotImplementedError:
                pass

        if self.enable_ble:
            self.ble_task = asyncio.create_task(self.ble.run(), name="ble-listener")

        if start_now:
            await self.start_demo()

        await self.stop_event.wait()
        await self.shutdown()

    async def start_demo(self, from_index: int = 0):
        if self.running:
            return
        self.running = True
        self.current_index = from_index
        self.outputs.start_pd()
        self.outputs.send_bpm(self.bpm)
        self.sequence_task = asyncio.create_task(self._run_sequence(), name="stage-sequence")
        self.log.info("Demo started")

    async def stop_demo(self):
        self.running = False

        task = self.sequence_task
        self.sequence_task = None
        if task and not task.done() and task is not asyncio.current_task():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

        await self.outputs.stop_all()
        self.outputs.stop_pd()
        self.current_index = -1
        self.log.info("Demo stopped")

    async def _run_sequence(self):
        try:
            i = self.current_index if self.current_index >= 0 else 0
            while self.running and i < len(STAGES):
                self.current_index = i
                stage = STAGES[i]
                self.log.info("Stage -> %s", stage["name"])
                await self.outputs.apply_stage(stage, self.bpm)
                await asyncio.sleep(float(stage["duration_s"]))
                i += 1
        except asyncio.CancelledError:
            pass
        finally:
            if self.running:
                self.running = False
                await self.outputs.stop_all()
                self.outputs.stop_pd()
                self.current_index = -1
                self.log.info("Demo complete")

    async def set_bpm(self, value):
        try:
            bpm = int(value)
        except Exception:
            return
        bpm = int(clamp(bpm, MIN_BPM, MAX_BPM))
        if bpm == self.bpm:
            return
        self.bpm = bpm
        self.outputs.send_bpm(self.bpm)
        self.log.info("BPM -> %s", self.bpm)

    async def jump_to_stage(self, stage_name: str):
        name = stage_name.strip().lower().replace(" ", "")
        idx = None
        for i, stage in enumerate(STAGES):
            stage_norm = str(stage.get("name", "")).lower().replace(" ", "")
            if stage_norm == name:
                idx = i
                break
        if idx is None:
            return

        if self.running:
            await self.stop_demo()
        await self.start_demo(from_index=idx)

    async def handle_packet(self, pkt: dict):
        cmd = str(pkt.get("cmd", "")).strip().lower()

        if "bpm" in pkt:
            await self.set_bpm(pkt.get("bpm"))

        if cmd in {"start", "run", "trigger"}:
            await self.start_demo()
            return

        if cmd in {"stop", "abort"}:
            await self.stop_demo()
            return

        if cmd in {"set_stage", "stage", "jump"}:
            value = pkt.get("stage", pkt.get("value", ""))
            if isinstance(value, str) and value.strip():
                await self.jump_to_stage(value)
            return

        if cmd in {"awake", "light", "deep", "rem"}:
            await self.jump_to_stage(cmd)

    async def shutdown(self):
        self.ble.stop_event.set()

        if self.ble_task and not self.ble_task.done():
            self.ble_task.cancel()
            try:
                await self.ble_task
            except asyncio.CancelledError:
                pass

        await self.stop_demo()
        await self.outputs.close()


def parse_args():
    parser = argparse.ArgumentParser(description="Minimal modular sleep demo")
    parser.add_argument("--start", action="store_true", help="Start demo immediately")
    parser.add_argument("--no-ble", action="store_true", help="Disable BLE listener")
    parser.add_argument("--dry-run", action="store_true", help="Skip GPIO and Pure Data actions")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    return parser.parse_args()


async def async_main():
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    app = App(enable_ble=not args.no_ble, dry_run=args.dry_run, log=logging.getLogger("sleep_demo_modular"))
    await app.run(start_now=args.start)


def main():
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
