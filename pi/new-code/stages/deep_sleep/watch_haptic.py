"""Stage 'deep_sleep' + stimulus 'watch_haptic'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no wrist haptic in deep sleep. Avoid sleep fragmentation in N3.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No wrist haptic cue in deep sleep", True
