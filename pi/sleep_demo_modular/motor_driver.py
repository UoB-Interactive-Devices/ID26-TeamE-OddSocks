from __future__ import annotations

import asyncio

from constants import MOTOR_PIN, MOTOR_PWM_HZ

try:
    import lgpio
except ImportError:  # pragma: no cover
    lgpio = None


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


class MotorDriver:
    def __init__(self):
        self.task: asyncio.Task | None = None
        self.handle = None

        if lgpio is not None:
            try:
                self.handle = lgpio.gpiochip_open(0)
                lgpio.gpio_claim_output(self.handle, MOTOR_PIN)
                self._set(0.0)
            except Exception:
                self.handle = None

    def _set(self, duty: float):
        if self.handle is None or lgpio is None:
            return
        safe = clamp(duty, 0.0, 100.0)
        lgpio.tx_pwm(self.handle, MOTOR_PIN, MOTOR_PWM_HZ, safe)
        if safe <= 0:
            lgpio.gpio_write(self.handle, MOTOR_PIN, 0)

    async def stop(self):
        if self.task and not self.task.done():
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                pass
        self.task = None
        self._set(0.0)

    async def start(self, cfg: dict):
        await self.stop()
        if self.handle is None or cfg.get("mode", "off") == "off":
            return
        self.task = asyncio.create_task(self._loop(cfg), name="motor-loop")

    async def _loop(self, cfg: dict):
        duty = float(cfg.get("duty", 25))
        on_s = max(0.02, float(cfg.get("on_s", 0.3)))
        off_s = max(0.02, float(cfg.get("off_s", 2.0)))
        while True:
            self._set(duty)
            await asyncio.sleep(on_s)
            self._set(0)
            await asyncio.sleep(off_s)

    def close(self):
        if self.handle is not None and lgpio is not None:
            try:
                lgpio.gpiochip_close(self.handle)
            except Exception:
                pass
        self.handle = None
