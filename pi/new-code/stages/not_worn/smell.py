"""Stage 'not_worn' + stimulus 'smell'.

This file owns the logic for this exact stage/stimulus combination.

Safety state: watch is not worn, so do not emit cues.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No smell cue when watch is not worn", True
