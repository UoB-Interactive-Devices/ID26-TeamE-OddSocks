from __future__ import annotations

import asyncio

from constants import LED_COUNT, LED_PIN_NAME

try:
    import board
    import neopixel
except ImportError:  # pragma: no cover
    board = None
    neopixel = None


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def blend(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return (
        int(a[0] + (b[0] - a[0]) * t),
        int(a[1] + (b[1] - a[1]) * t),
        int(a[2] + (b[2] - a[2]) * t),
    )


class LedDriver:
    def __init__(self):
        self.task: asyncio.Task | None = None
        self.pixels = None

        if board is not None and neopixel is not None:
            pin = getattr(board, LED_PIN_NAME, None)
            if pin is not None:
                self.pixels = neopixel.NeoPixel(pin, LED_COUNT, brightness=0.01, auto_write=True)
                self._set((0, 0, 0), 0.0)

    def _set(self, color: tuple[int, int, int], brightness: float):
        if self.pixels is None:
            return
        self.pixels.brightness = clamp(brightness, 0.0, 1.0)
        self.pixels.fill(color)

    async def stop(self):
        if self.task and not self.task.done():
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                pass
        self.task = None
        self._set((0, 0, 0), 0.0)

    async def start(self, cfg: dict):
        await self.stop()
        if self.pixels is None or cfg.get("mode", "off") == "off":
            return
        self.task = asyncio.create_task(self._loop(cfg), name="led-loop")

    async def _loop(self, cfg: dict):
        color_a = cfg.get("color_a", (255, 0, 0))
        color_b = cfg.get("color_b", color_a)
        min_b = float(cfg.get("min_b", 0.01))
        max_b = float(cfg.get("max_b", 0.08))
        step_s = float(cfg.get("step_s", 0.03))
        steps = 60

        while True:
            for i in range(steps):
                t = i / (steps - 1)
                self._set(blend(color_a, color_b, t), min_b + (max_b - min_b) * t)
                await asyncio.sleep(step_s)
            for i in range(steps - 1, -1, -1):
                t = i / (steps - 1)
                self._set(blend(color_a, color_b, t), min_b + (max_b - min_b) * t)
                await asyncio.sleep(step_s)
