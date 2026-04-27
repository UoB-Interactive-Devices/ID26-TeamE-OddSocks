"""Stage 'unknown' + stimulus 'watch_haptic'.

This file owns the logic for this exact stage/stimulus combination.

Safety state: stage is unknown, so do not emit cues.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No wrist haptic cue for unknown stage", True
