"""Stage 'rem' + stimulus 'smell'.

Intent: pulse both nebulisers together as one REM smell cue. Full flow is
5s on / 25s off for 15 minutes; demo mode uses short visible pulses.
"""

from __future__ import annotations

import asyncio
import contextlib
import sys

try:
    import lgpio
except ImportError:
    lgpio = None

SMELL_PINS = (12, 16)
FULL_DURATION_S = 15 * 60
FULL_ON_S = 5
FULL_OFF_S = 25
DEMO_DURATION_S = 40
DEMO_ON_S = 1
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


def _log_task_result(task: asyncio.Task, log) -> None:
    with contextlib.suppress(asyncio.CancelledError):
        exc = task.exception()
        if exc is not None:
            _log(log, "warning", f"rem/smell task failed: {exc}")


async def _run_pulsed_smell(log, duration_s: float, on_s: float, off_s: float) -> None:
    outputs = _open_outputs()
    sys._smell_handle = outputs
    try:
        end_time = asyncio.get_running_loop().time() + duration_s
        while asyncio.get_running_loop().time() < end_time:
            _set_pins(outputs, 1)
            _log(log, "info", "rem/smell nebulisers on")
            await asyncio.sleep(on_s)
            _set_pins(outputs, 0)
            _log(log, "info", "rem/smell nebulisers off")
            await asyncio.sleep(off_s)
    except asyncio.CancelledError:
        raise
    finally:
        _close_outputs(outputs)
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
    task = asyncio.create_task(_run_pulsed_smell(log, duration_s, on_s, off_s))
    task.add_done_callback(lambda done: _log_task_result(done, log))
    sys._smell_mist_task = task
    await asyncio.sleep(0)
    if task.done():
        task.result()
    return "smell_started", f"Pulsed smell output started for {duration_s:g}s", True
