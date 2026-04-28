"""Stage 'awake' + stimulus 'pi_motor'.

This file owns the logic for this exact stage/stimulus combination.

Intent: no below-pillow haptic during awake preparation. The awake haptic
callback cue is handled by the watch, because the user may not be in bed yet.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No awake below-pillow haptic cue before sleep", True
