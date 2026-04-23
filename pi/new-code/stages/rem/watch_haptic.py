#figure out how to buzz watch
from __future__ import annotations
import asyncio
import random

CHIP = 0
GAP_BETWEEN_BURSTS = 60
remCycleNo = 2   

async def run(context: dict) -> tuple[str, str, bool]:
    #commented out for testing
    #await asyncio.sleep(delayAftrRem)
    send_watch_json = context["send_watch_json"]
    log = context["log"]
    demo_fast = bool(context.get("demo_fast"))

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
        burst_duration = random.uniform(0.5, 0.8) if demo_fast else random.uniform(1.0, 2.0)
        elapsed = 0
        intensity = 20
        success = True

        while elapsed < burst_duration:
            intensity = min(intensity + random.randint(8, 18), 80)

            on_time = random.choice([0.08, 0.12]) if demo_fast else random.choice([0.2, 0.3])

            gap_time = random.uniform(0.05, 0.08) if demo_fast else random.uniform(0.2, 0.3)

            success = await buzz(intensity, on_time) and success
            await asyncio.sleep(gap_time)

            elapsed += on_time + gap_time

        return success

    async def rem_cycle(bursts=remCycleNo, gap=GAP_BETWEEN_BURSTS):
        if demo_fast:
            bursts = 1
            gap = 0.1
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

    details = "demo fast buzz cycle" if demo_fast else "NremCycle buzz bursts with minute gaps"
    return "haptic-buzz started", details, True
