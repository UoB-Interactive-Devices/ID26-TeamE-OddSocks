from __future__ import annotations

import asyncio

from constants import NEBULISER_PIN, NEB_ACTIVE_HIGH

try:
    import lgpio
except ImportError:  # pragma: no cover
    lgpio = None


class NebuliserDriver:
    def __init__(self):
        self.task: asyncio.Task | None = None
        self.handle = None

        if lgpio is not None:
            try:
                self.handle = lgpio.gpiochip_open(0)
                lgpio.gpio_claim_output(self.handle, NEBULISER_PIN)
                self._set(False)
            except Exception:
                self.handle = None

    def _set(self, on: bool):
        if self.handle is None or lgpio is None:
            return
        level = 1 if on else 0
        if not NEB_ACTIVE_HIGH:
            level = 0 if on else 1
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
        if self.handle is None or cfg.get("mode", "off") == "off":
            return
        self.task = asyncio.create_task(self._loop(cfg), name="neb-loop")

    async def _loop(self, cfg: dict):
        on_s = max(0.05, float(cfg.get("on_s", 0.6)))
        off_s = max(0.05, float(cfg.get("off_s", 6.0)))
        while True:
            self._set(True)
            await asyncio.sleep(on_s)
            self._set(False)
            await asyncio.sleep(off_s)

    def close(self):
        if self.handle is not None and lgpio is not None:
            try:
                lgpio.gpiochip_close(self.handle)
            except Exception:
                pass
        self.handle = None
