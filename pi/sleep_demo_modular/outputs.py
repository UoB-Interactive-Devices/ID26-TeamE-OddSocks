from __future__ import annotations

from led_driver import LedDriver
from motor_driver import MotorDriver
from nebuliser_driver import NebuliserDriver
from puredata_client import PureDataClient


class Outputs:
    def __init__(self):
        self.led = LedDriver()
        self.motor = MotorDriver()
        self.nebuliser = NebuliserDriver()
        self.pd = PureDataClient()

    async def apply_stage(self, stage: dict, bpm: int):
        await self.led.start(stage.get("led", {}))
        await self.motor.start(stage.get("motor", {}))
        await self.nebuliser.start(stage.get("neb", {}))
        self.pd.send(f"stage {stage.get('name', '')}")
        self.pd.send(f"bpm {bpm}")

    def start_pd(self):
        self.pd.start()

    def send_bpm(self, bpm: int):
        self.pd.send(f"bpm {bpm}")

    async def stop_all(self):
        await self.led.stop()
        await self.motor.stop()
        await self.nebuliser.stop()

    async def close(self):
        await self.stop_all()
        self.pd.stop()
        self.motor.close()
        self.nebuliser.close()
