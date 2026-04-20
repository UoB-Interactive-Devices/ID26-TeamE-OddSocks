from __future__ import annotations

import logging

from old.sleep_demo_modular.led_driver import LedDriver
from old.sleep_demo_modular.motor_driver import MotorDriver
from old.sleep_demo_modular.nebuliser_driver import NebuliserDriver
from old.sleep_demo_modular.puredata_client import PureDataClient


class Outputs:
    def __init__(self, dry_run: bool = False, log: logging.Logger | None = None):
        self.dry_run = dry_run
        self.log = log or logging.getLogger("sleep_demo_modular.outputs")

        if self.dry_run:
            self.led = None
            self.motor = None
            self.nebuliser = None
            self.pd = None
            return

        self.led = LedDriver()
        self.motor = MotorDriver()
        self.nebuliser = NebuliserDriver()
        self.pd = PureDataClient(log=self.log.getChild("pd"))

    async def apply_stage(self, stage: dict, bpm: int):
        if self.dry_run:
            self.log.info("[dry-run] apply stage=%s bpm=%s", stage.get("name", ""), bpm)
            return
        await self.led.start(stage.get("led", {}))
        await self.motor.start(stage.get("motor", {}))
        await self.nebuliser.start(stage.get("neb", {}))
        self.pd.send(f"stage {stage.get('name', '')}")
        self.pd.send(f"bpm {bpm}")

    def start_pd(self):
        if self.dry_run:
            self.log.info("[dry-run] start pd")
            return
        self.pd.start()

    def send_bpm(self, bpm: int):
        if self.dry_run:
            self.log.info("[dry-run] send bpm=%s", bpm)
            return
        self.pd.send(f"bpm {bpm}")

    def stop_pd(self):
        if self.dry_run:
            self.log.info("[dry-run] stop pd")
            return
        self.pd.stop()

    async def stop_all(self):
        if self.dry_run:
            self.log.info("[dry-run] stop all outputs")
            return
        await self.led.stop()
        await self.motor.stop()
        await self.nebuliser.stop()

    async def close(self):
        if self.dry_run:
            self.log.info("[dry-run] close outputs")
            return
        await self.stop_all()
        self.pd.stop()
        self.motor.close()
        self.nebuliser.close()
