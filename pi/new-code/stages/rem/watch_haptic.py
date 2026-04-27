#figure out how to buzz watch
from __future__ import annotations
import asyncio
import random

CHIP = 0
GAP_BETWEEN_BURSTS = 60
remCycleNo = 2 
delayAfterRem = 3 * 60 #3mins 

async def run(context: dict) -> tuple[str, str, bool]:
    await asyncio.sleep(delayAfterRem)
    send_watch_json = context["send_watch_json"]
    log = context["log"]

    async def buzz(intensity, duration):
        #start buzz at intensity
        payload = {
            "cmd": "buzz",
            "event": "rem_detected",
            "buzz": int(duration * 1000),
            "intensity": intensity,
        }
        sent = await send_watch_json(payload)
        await asyncio.sleep(duration)
        #stop buzz is handled by the watch after the duration
        return sent

    async def burst():
        burst_duration = random.uniform(1.0, 2.0)
        elapsed = 0
        intensity = 20 
        success = True

        while elapsed < burst_duration:
            intensity = min(intensity + random.randint(8, 18), 80)

            on_time = random.choice([0.2, 0.3])

            gap_time = random.uniform(0.2, 0.3)

            success = await buzz(intensity, on_time) and success
            await asyncio.sleep(gap_time)

            elapsed += on_time + gap_time

        return success

    async def rem_cycle(bursts=remCycleNo, gap=GAP_BETWEEN_BURSTS):
        success = True
        for i in range(bursts):
            print(f"Burst {i + 1} of {bursts}")
            success = await burst() and success

            if i < bursts - 1:
                print(f"Waiting {gap}s until next burst...")
                await asyncio.sleep(gap)

        return success

    try:
        success = await rem_cycle()
    except Exception as exc:
        log.warning("rem/watch_haptic send failed: %s", exc)
        return "haptic-buzz error", f"watch buzz failed: {exc}", False
    finally:
        #stop buzzing
        #The watch stops itself after each buzz duration
        pass

    if not success:
        return "haptic-buzz skipped", "watch not connected for one or more buzzes", False

    return "haptic-buzz started", "NremCycle buzz bursts with minute gaps", True
