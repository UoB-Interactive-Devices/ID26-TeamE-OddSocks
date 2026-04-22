import lgpio
import time
import random
from __future__ import annotations
import asyncio

CHIP = 0
PIN = 23
delayAftrRem = 3 * 60 #3mins
GAP_BETWEEN_BURSTS = 60
remCycleNo = 2

async def buzz(intensity, duration):
        lgpio.tx_pwm(h, PIN, 100, intensity)
        time.sleep(duration)
        lgpio.tx_pwm(h, PIN, 100, 0)

async def burst():
    burst_duration = random.uniform(1.0, 2.0)
    elapsed = 0
    intensity = 20 

    while elapsed < burst_duration:
        intensity = min(intensity + random.randint(8, 18), 80)

        on_time = random.choice([0.2, 0.3])

        gap_time = random.uniform(0.2, 0.3)

        buzz(intensity, on_time)
        time.sleep(gap_time)

        elapsed += on_time + gap_time

async def rem_cycle(bursts=remCycle, gap=GAP_BETWEEN_BURSTS):
    for i in range(bursts):
        print(f"Burst {i + 1} of {bursts}")
        burst()

        if i < bursts - 1:
            print(f"Waiting {gap}s until next burst...")
            time.sleep(gap)

async def run(context: dict) -> tuple[str, str, bool]:
    #commented out for testing
    #time.sleep(delayAftrRem)
    h = lgpio.gpiochip_open(CHIP)
    lgpio.gpio_claim_output(h, PIN)

    try:
        rem_cycle()
    finally:
        lgpio.tx_pwm(h, PIN, 100, 0)
        lgpio.gpiochip_close(h)

    return "haptic-buzz started", "NremCycle buzz bursts with minute gaps", True

run(1)
time.sleep(10)
run(3)
time.sleep(10)
run(5)