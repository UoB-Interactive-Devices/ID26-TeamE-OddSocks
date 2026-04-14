from __future__ import annotations

import asyncio

from constants import NEBULISER_PIN, NEB_ACTIVE_HIGH

try:
    import RPi.GPIO as GPIO
except ImportError:  # pragma: no cover
    GPIO = None

try:
    import lgpio
except ImportError:  # pragma: no cover
    lgpio = None


class NebuliserDriver:
    def __init__(self):
        self.task: asyncio.Task | None = None
        self.backend: str | None = None
        self.handle = None
        self._gpio_ready = False

        # Prefer RPi.GPIO to match the known-good standalone demo script.
        if GPIO is not None:
            try:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(NEBULISER_PIN, GPIO.OUT)
                self.backend = "rpi_gpio"
                self._gpio_ready = True
                self._set(False)
                return
            except Exception:
                self.backend = None
                self._gpio_ready = False

        if lgpio is not None:
            try:
                self.handle = lgpio.gpiochip_open(0)
                lgpio.gpio_claim_output(self.handle, NEBULISER_PIN)
                self.backend = "lgpio"
                self._gpio_ready = True
                self._set(False)
            except Exception:
                self.backend = None
                self._gpio_ready = False
                self.handle = None

    def _set(self, on: bool):
        if not self._gpio_ready:
            return

        level = 1 if on else 0
        if not NEB_ACTIVE_HIGH:
            level = 0 if on else 1

        if self.backend == "rpi_gpio" and GPIO is not None:
            GPIO.output(NEBULISER_PIN, GPIO.HIGH if level else GPIO.LOW)
            return

        if self.backend == "lgpio" and self.handle is not None and lgpio is not None:
            lgpio.gpio_write(self.handle, NEBULISER_PIN, level)

    async def stop(self):
        if self.task and not self.task.done():
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                pass
        self.task = None
        self._set(False)

    async def start(self, cfg: dict):
        await self.stop()
        if not self._gpio_ready or cfg.get("mode", "off") == "off":
            return
        self.task = asyncio.create_task(self._loop(cfg), name="neb-loop")

    async def _loop(self, cfg: dict):
        # Most atomisers need a longer startup pulse than LEDs/motor effects.
        on_s = max(0.3, float(cfg.get("on_s", 0.6)))
        off_s = max(0.05, float(cfg.get("off_s", 6.0)))
        warmup_s = max(on_s, float(cfg.get("warmup_s", 2.0)))

        self._set(True)
        await asyncio.sleep(warmup_s)
        self._set(False)
        await asyncio.sleep(off_s)

        while True:
            self._set(True)
            await asyncio.sleep(on_s)
            self._set(False)
            await asyncio.sleep(off_s)

    def close(self):
        self._set(False)

        if self.backend == "rpi_gpio" and GPIO is not None:
            try:
                GPIO.cleanup(NEBULISER_PIN)
            except Exception:
                pass

        if self.handle is not None and lgpio is not None:
            try:
                lgpio.gpiochip_close(self.handle)
            except Exception:
                pass

        self.backend = None
        self._gpio_ready = False
        self.handle = None
