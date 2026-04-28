"""Stage 'awake' + stimulus 'smell'.

Intent: run nebuliser_1 as the awake smell output. Full flow is
5s on / 25s off for 10 minutes; demo mode uses short visible pulses.
"""

from __future__ import annotations

import asyncio
import contextlib
import sys

try:
    import lgpio
except ImportError:
    lgpio = None

SMELL_PINS = (12,)
FULL_DURATION_S = 10 * 60
FULL_ON_S = 5
FULL_OFF_S = 25
DEMO_DURATION_S = 18
DEMO_ON_S = 2
DEMO_OFF_S = 1


def _log(log, level: str, message: str) -> None:
    if log and hasattr(log, level):
        getattr(log, level)(message)


def _open_outputs() -> list[tuple[int, int]]:
    outputs = []
    for pin in SMELL_PINS:
        handle = lgpio.gpiochip_open(0)
        lgpio.gpio_claim_output(handle, pin)
        lgpio.gpio_write(handle, pin, 0)
        outputs.append((handle, pin))
    return outputs


def _set_pins(outputs: list[tuple[int, int]], value: int) -> None:
    for handle, pin in outputs:
        lgpio.gpio_write(handle, pin, value)


def _close_outputs(outputs: list[tuple[int, int]]) -> None:
    for handle, pin in outputs:
        with contextlib.suppress(Exception):
            lgpio.gpio_write(handle, pin, 0)
        with contextlib.suppress(Exception):
            if hasattr(lgpio, "gpio_free"):
                lgpio.gpio_free(handle, pin)
        with contextlib.suppress(Exception):
            lgpio.gpiochip_close(handle)


async def _run_awake_smell(log, duration_s: float, on_s: float, off_s: float) -> None:
    outputs = _open_outputs()
    sys._smell_handle = outputs
    try:
        end_time = asyncio.get_running_loop().time() + duration_s
        while asyncio.get_running_loop().time() < end_time:
            _set_pins(outputs, 1)
            _log(log, "info", "awake/smell nebuliser_1 on")
            await asyncio.sleep(on_s)
            _set_pins(outputs, 0)
            _log(log, "info", "awake/smell nebuliser_1 off")
            await asyncio.sleep(off_s)
    except asyncio.CancelledError:
        raise
    finally:
        _close_outputs(outputs)
        sys._smell_handle = None
        _log(log, "info", "awake/smell nebuliser_1 off")


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]
    if lgpio is None:
        _log(log, "warning", "awake/smell skipped; lgpio unavailable")
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
    sys._smell_mist_task = asyncio.current_task()
    try:
        await _run_awake_smell(log, duration_s, on_s, off_s)
    finally:
        sys._smell_mist_task = None
    return "smell_finished", f"Awake smell cycle ran for {duration_s:g}s", True
