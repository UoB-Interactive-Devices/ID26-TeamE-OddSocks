#figure out how to buzz watch
from __future__ import annotations
import time
import random
import asyncio

CHIP = 0
PIN = 17
GAP_BETWEEN_BURSTS = 60
remCycleNo = 2

async def buzz(intensity, duration):
        #start buzz at intensity
        time.sleep(duration)
        #stop buzz

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

async def rem_cycle(bursts=remCycleNo, gap=GAP_BETWEEN_BURSTS):
        for i in range(bursts):
            print(f"Burst {i + 1} of {bursts}")
            burst()

            if i < bursts - 1:
                print(f"Waiting {gap}s until next burst...")
                time.sleep(gap)

async def run(context: dict) -> tuple[str, str, bool]:
    #commented out for testing
    #time.sleep(delayAftrRem)

    try:
        rem_cycle()
    finally:
        #stop buzzing
        1==1

    return "watch-haptic started", "NremCycle buzz bursts with minute gaps", True

