"""Stage 'rem' + stimulus 'light'.

Intent: keep LEDs off until REM has been detected for 3 minutes, then pulse
with brightness ramps as a dream cue. Early REM uses red only; later REM ramps
between red and amber. Demo mode shortens the delay and keeps the pattern going.
"""

from __future__ import annotations

import asyncio

from hardware_setup import SPI_DEVICE

try:
    import board
    import neopixel_spi
except Exception as exc:
    board = None
    neopixel_spi = None
    HARDWARE_IMPORT_ERROR = exc
else:
    HARDWARE_IMPORT_ERROR = None

LED_COUNT = 9
BRIGHTNESS = 0.12
RAMP_STEPS = 30
RAMP_STEP_S = 0.01
REM_DELAY_S = 3 * 60
DEMO_DELAY_S = 0.5
EARLY_REM_SECONDS = 5
LATE_REM_SECONDS = 10
DEMO_PULSE_SECONDS = 40
DEFAULT_REM_CYCLE = 3


def make_pixels():
    if board is None or neopixel_spi is None or not SPI_DEVICE.exists():
        return None
    return neopixel_spi.NeoPixel_SPI(board.SPI(), LED_COUNT, brightness=BRIGHTNESS, auto_write=False)


async def _pulse(pixels, duration_s: float, late_rem: bool) -> None:
    colors = [(255, 0, 0), (255, 60, 0)] if late_rem else [(255, 0, 0)]
    end_time = asyncio.get_running_loop().time() + duration_s
    step = 0

    while asyncio.get_running_loop().time() < end_time:
        color = colors[step % len(colors)]
        for brightness in range(RAMP_STEPS + 1):
            pixels.brightness = BRIGHTNESS * (brightness / RAMP_STEPS)
            pixels.fill(color)
            pixels.show()
            await asyncio.sleep(RAMP_STEP_S)
        for brightness in range(RAMP_STEPS, -1, -1):
            pixels.brightness = BRIGHTNESS * (brightness / RAMP_STEPS)
            pixels.fill(color)
            pixels.show()
            await asyncio.sleep(RAMP_STEP_S)
        pixels.brightness = BRIGHTNESS
        pixels.fill((0, 0, 0))
        pixels.show()
        await asyncio.sleep(0.2)
        step += 1


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]
    demo_fast = bool(context.get("demo_fast"))
    rem_cycle = int(context.get("rem_cycle", DEFAULT_REM_CYCLE))
    late_rem = rem_cycle > 2

    pixels = make_pixels()
    if pixels is None:
        log.info("rem/light skipped; LED hardware unavailable: %s", HARDWARE_IMPORT_ERROR)
        return "light_skipped", "LED hardware unavailable on this machine", False

    await asyncio.sleep(DEMO_DELAY_S if demo_fast else REM_DELAY_S)
    pulse_seconds = DEMO_PULSE_SECONDS if demo_fast else (LATE_REM_SECONDS if late_rem else EARLY_REM_SECONDS)

    try:
        await _pulse(pixels, pulse_seconds, late_rem)
    finally:
        pixels.fill((0, 0, 0))
        pixels.show()
        if hasattr(pixels, "deinit"):
            pixels.deinit()

    cue = "red/amber" if late_rem else "red"
    return "light_pulsed", f"{cue} REM light pulse for {pulse_seconds:g}s", True
