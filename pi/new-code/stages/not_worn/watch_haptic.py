"""Stage 'not_worn' + stimulus 'watch_haptic'.

This file owns the logic for this exact stage/stimulus combination.

Safety state: watch is not worn, so do not emit cues.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No wrist haptic cue when watch is not worn", True
