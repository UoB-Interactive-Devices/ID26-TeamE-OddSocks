"""Stage 'light_sleep' + stimulus 'pi_motor'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no below-pillow haptic in light sleep. These cues are more
likely to wake the user in N1/N2 than help lucid dreaming.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No below-pillow haptic cue in light sleep", True
