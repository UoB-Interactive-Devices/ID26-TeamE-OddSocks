"""Stage 'deep_sleep' + stimulus 'pi_motor'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no below-pillow haptic in deep sleep. Avoid stimulation during
the most restorative part of the sleep cycle.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No below-pillow haptic cue in deep sleep", True
