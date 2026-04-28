"""Stage 'rem' + stimulus 'smell'.

Intent: pulse both nebulisers together as one REM smell cue. Full flow is
5s on / 25s off for 15 minutes; demo mode uses short visible pulses.
"""

from __future__ import annotations

import asyncio
import sys

try:
    import lgpio
except ImportError:
    lgpio = None

SMELL_PINS = (12, 16)
FULL_DURATION_S = 15 * 60
FULL_ON_S = 5
FULL_OFF_S = 25
DEMO_DURATION_S = 6
DEMO_ON_S = 1
DEMO_OFF_S = 1


def _log(log, level: str, message: str) -> None:
    if log and hasattr(log, level):
        getattr(log, level)(message)


def _set_pins(handle, value: int) -> None:
    for pin in SMELL_PINS:
        lgpio.gpio_write(handle, pin, value)


async def _run_pulsed_smell(log, duration_s: float, on_s: float, off_s: float) -> None:
    handle = lgpio.gpiochip_open(0)
    sys._smell_handle = handle
    try:
        for pin in SMELL_PINS:
            lgpio.gpio_claim_output(handle, pin)

        end_time = asyncio.get_running_loop().time() + duration_s
        while asyncio.get_running_loop().time() < end_time:
            _set_pins(handle, 1)
            _log(log, "info", "rem/smell nebulisers on")
            await asyncio.sleep(on_s)
            _set_pins(handle, 0)
            _log(log, "info", "rem/smell nebulisers off")
            await asyncio.sleep(off_s)
    except asyncio.CancelledError:
        raise
    finally:
        _set_pins(handle, 0)
        lgpio.gpiochip_close(handle)
        sys._smell_handle = None


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]
    if lgpio is None:
        _log(log, "warning", "rem/smell skipped; lgpio unavailable")
        return "smell_skipped", "lgpio unavailable", False

    previous = getattr(sys, "_smell_mist_task", None)
    if previous is not None and not previous.done():
        previous.cancel()
        try:
            await previous
        except asyncio.CancelledError:
            pass

    demo_fast = bool(context.get("demo_fast"))
    duration_s = DEMO_DURATION_S if demo_fast else FULL_DURATION_S
    on_s = DEMO_ON_S if demo_fast else FULL_ON_S
    off_s = DEMO_OFF_S if demo_fast else FULL_OFF_S
    sys._smell_mist_task = asyncio.create_task(_run_pulsed_smell(log, duration_s, on_s, off_s))
    return "smell_started", f"Pulsed smell output started for {duration_s:g}s", True
