from __future__ import annotations
import asyncio

from hardware_setup import SPI_DEVICE

# REM light intent: cue only after REM has been detected, with a delay offset.
# Use short red/amber pulses; keep LEDs off otherwise. Later REM cycles can
# tolerate slightly more stimulation than early REM.

try:
    import board
    import neopixel_spi
except Exception as exc:  # board can fail during import on non-Pi machines.
    board = None
    neopixel_spi = None
    HARDWARE_IMPORT_ERROR = exc
else:
    HARDWARE_IMPORT_ERROR = None

delayAfterRem = 3 * 60 #3mins
NoLEDs = 8
remCycleNo = 3

def make_pixels():
    if board is None or neopixel_spi is None:
        return None
    if not SPI_DEVICE.exists():
        return None
    return neopixel_spi.NeoPixel_SPI(board.SPI(), NoLEDs, brightness=0.01, auto_write=False)

async def run(context: dict) -> tuple[str, str, bool]:
    #await asyncio.sleep(delayAfterRem)
    #Using await means the other stage files can run during the gaps
    log = context["log"]
    pixels = make_pixels()
    if pixels is None:
        log.info("rem/light skipped; LED hardware unavailable: %s", HARDWARE_IMPORT_ERROR)
        return "light_skipped", "LED hardware unavailable on this machine", False

    async def earlyRem():
        for cycle in range(5):
            for b in range(0, 100):
                pixels.brightness = b / 100
                pixels.fill((255, 0, 0))
                pixels.show()
                await asyncio.sleep(0.002)
            for b in range(100, 0, -1):
                pixels.brightness = b / 100
                pixels.fill((255, 0, 0))
                pixels.show()
                await asyncio.sleep(0.002)
            pixels.fill((0, 0, 0))
            pixels.show()
            await asyncio.sleep(0.5)

        pixels.fill((0, 0, 0))
        pixels.show()

    async def midNlateRem():
        for cycle in range(5):
                for b in range(0, 100):
                    pixels.brightness = b / 100
                    pixels.fill((255, 0, 0))
                    pixels.show()
                    await asyncio.sleep(0.002)
                for b in range(100, 0, -1):
                    pixels.brightness = b / 100
                    pixels.fill((255, 0, 0))
                    pixels.show()
                    await asyncio.sleep(0.002)
                for b in range(0, 100):
                    pixels.brightness = b / 100
                    pixels.fill((255, 60, 0))
                    pixels.show()
                    await asyncio.sleep(0.002)
                for b in range(100, 0, -1):
                    pixels.brightness = b / 100
                    pixels.fill((255, 60, 0))
                    pixels.show()
                    await asyncio.sleep(0.002)

        pixels.fill((0, 0, 0))
        pixels.show()

    try:
        if remCycleNo <= 2:
            await earlyRem()
        else:
            await midNlateRem()
    finally:
        pixels.fill((0, 0, 0))
        pixels.show()
        if hasattr(pixels, "deinit"):
            pixels.deinit()

    return "light cues started", "5 or 10s burst, colour dependent on NremCycle", True
