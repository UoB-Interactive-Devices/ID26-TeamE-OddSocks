from __future__ import annotations
import lgpio
import random
import asyncio

# REM below-pillow haptic intent: tactile dream cue after REM detection, using
# short irregular/ramping bursts. This mirrors the watch haptic idea but uses
# the pillow motor for a stronger physical cue.

CHIP = 0
PIN = 23
delayAfterRem = 3 * 60 #3mins
GAP_BETWEEN_BURSTS = 60
remCycleNo = 2

async def run(context: dict) -> tuple[str, str, bool]:
    #await asyncio.sleep(delayAfterRem)
    #Using await means the other stage files can run during the gaps
    h = lgpio.gpiochip_open(CHIP)
    lgpio.gpio_claim_output(h, PIN)

    async def buzz(intensity, duration):
        lgpio.tx_pwm(h, PIN, 100, intensity)
        await asyncio.sleep(duration)
        lgpio.tx_pwm(h, PIN, 100, 0)

    async def burst():
        burst_duration = random.uniform(1.0, 2.0)
        elapsed = 0
        intensity = 20 

        while elapsed < burst_duration:
            intensity = min(intensity + random.randint(8, 18), 80)

            on_time = random.choice([0.2, 0.3])

            gap_time = random.uniform(0.2, 0.3)

            await buzz(intensity, on_time)
            await asyncio.sleep(gap_time)

            elapsed += on_time + gap_time

    async def rem_cycle(bursts=remCycleNo, gap=GAP_BETWEEN_BURSTS):
        for i in range(bursts):
            print(f"Burst {i + 1} of {bursts}")
            await burst()

            if i < bursts - 1:
                print(f"Waiting {gap}s until next burst...")
                await asyncio.sleep(gap)

    try:
        await rem_cycle()
    finally:
        lgpio.tx_pwm(h, PIN, 100, 0)
        lgpio.gpiochip_close(h)

    return "pi-motor-buzz started", "NremCycle buzz bursts with minute gaps", True
