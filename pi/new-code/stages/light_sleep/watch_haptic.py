"""Stage 'light_sleep' + stimulus 'watch_haptic'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no wrist haptic in light sleep. External tactile cues are more
likely to wake the user here than become useful dream cues.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No wrist haptic cue in light sleep", True
