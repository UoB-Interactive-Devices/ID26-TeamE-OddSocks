"""Stage 'deep_sleep' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no new sound cue in deep sleep. If background masking audio is
already running, do not add sharp stimulation here.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No new sound cue in deep sleep", True
