"""Stage 'rem' + stimulus 'watch_haptic'.

Intent: use the watch motor as the wrist REM tactile cue after the same
3-minute offset as light, pillow haptic, and sound. Bursts are short,
irregular, and gently ramping; demo mode makes the cue fire almost at once.
"""

from __future__ import annotations

import asyncio
import random

REM_DELAY_S = 3 * 60
DEMO_DELAY_S = 0.5
GAP_BETWEEN_BURSTS_S = 60
FULL_BURSTS = 2
DEMO_BURSTS = 3


async def run(context: dict) -> tuple[str, str, bool]:
    send_watch_json = context["send_watch_json"]
    log = context["log"]
    demo_fast = bool(context.get("demo_fast"))

    await asyncio.sleep(DEMO_DELAY_S if demo_fast else REM_DELAY_S)

    async def buzz(intensity: int, duration_s: float) -> bool:
        payload = {
            "cmd": "buzz",
            "event": "rem_detected",
            "buzz": int(duration_s * 1000),
            "intensity": intensity,
        }
        sent = await send_watch_json(payload)
        await asyncio.sleep(duration_s)
        return sent

    async def burst() -> bool:
        burst_duration = 0.8 if demo_fast else random.uniform(1.0, 2.0)
        elapsed = 0.0
        intensity = 20
        success = True

        while elapsed < burst_duration:
            intensity = min(intensity + random.randint(8, 18), 80)
            on_s = random.choice([0.08, 0.12]) if demo_fast else random.choice([0.2, 0.3])
            off_s = random.uniform(0.05, 0.08) if demo_fast else random.uniform(0.2, 0.3)
            success = await buzz(intensity, on_s) and success
            await asyncio.sleep(off_s)
            elapsed += on_s + off_s

        return success

    bursts = DEMO_BURSTS if demo_fast else FULL_BURSTS
    gap_s = 0.3 if demo_fast else GAP_BETWEEN_BURSTS_S

    try:
        success = True
        for index in range(bursts):
            success = await burst() and success
            if index < bursts - 1:
                await asyncio.sleep(gap_s)
    except Exception as exc:
        log.warning("rem/watch_haptic send failed: %s", exc)
        return "watch_haptic_error", f"watch buzz failed: {exc}", False

    if not success:
        return "watch_haptic_skipped", "watch not connected for one or more buzzes", False

    return "watch_haptic_buzzed", f"{bursts} wrist REM haptic burst(s)", True
