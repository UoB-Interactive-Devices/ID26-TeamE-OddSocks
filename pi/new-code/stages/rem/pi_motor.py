"""Stage 'rem' + stimulus 'pi_motor'.

Intent: use the below-pillow motor as a REM tactile cue after the same
3-minute offset as the light and sound cues. The pattern is short, irregular,
and gently ramping so it can become a dream cue without being a long buzz.
Demo mode shortens the delay, burst count, and gaps.
"""

from __future__ import annotations

import asyncio
import random

try:
    import lgpio
except ImportError:
    lgpio = None

CHIP = 0
PIN = 23
REM_DELAY_S = 3 * 60
DEMO_DELAY_S = 0.5
GAP_BETWEEN_BURSTS_S = 60
FULL_BURSTS = 2
DEMO_BURSTS = 3
DEMO_BURST_SECONDS = 1.8


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]
    demo_fast = bool(context.get("demo_fast"))
    if lgpio is None:
        log.warning("rem/pi_motor skipped; lgpio unavailable")
        return "pi_motor_skipped", "lgpio unavailable", False

    await asyncio.sleep(DEMO_DELAY_S if demo_fast else REM_DELAY_S)

    handle = lgpio.gpiochip_open(CHIP)
    lgpio.gpio_claim_output(handle, PIN)

    async def buzz(intensity: int, duration_s: float) -> None:
        lgpio.tx_pwm(handle, PIN, 100, intensity)
        await asyncio.sleep(duration_s)
        lgpio.tx_pwm(handle, PIN, 100, 0)

    async def burst() -> None:
        burst_duration = DEMO_BURST_SECONDS if demo_fast else random.uniform(1.0, 2.0)
        elapsed = 0.0
        intensity = 20

        while elapsed < burst_duration:
            intensity = min(intensity + random.randint(8, 18), 80)
            on_s = random.choice([0.08, 0.12]) if demo_fast else random.choice([0.2, 0.3])
            off_s = random.uniform(0.05, 0.08) if demo_fast else random.uniform(0.2, 0.3)
            await buzz(intensity, on_s)
            await asyncio.sleep(off_s)
            elapsed += on_s + off_s

    bursts = DEMO_BURSTS if demo_fast else FULL_BURSTS
    gap_s = 0.3 if demo_fast else GAP_BETWEEN_BURSTS_S

    try:
        for index in range(bursts):
            await burst()
            if index < bursts - 1:
                await asyncio.sleep(gap_s)
    finally:
        lgpio.tx_pwm(handle, PIN, 100, 0)
        lgpio.gpiochip_close(handle)

    details = f"{bursts} below-pillow REM haptic burst(s)"
    return "pi_motor_buzzed", details, True
