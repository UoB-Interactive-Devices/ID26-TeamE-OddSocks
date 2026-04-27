"""Stage 'awake' + stimulus 'pi_motor'.

This file owns the logic for this exact stage/stimulus combination.

Team note: any awake haptic cue should follow the same macro pattern as light
and should not disturb the hours before sleep. Keep below-pillow haptics off
here unless the team chooses a daytime-only callback routine later.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No awake below-pillow haptic cue before sleep", True
