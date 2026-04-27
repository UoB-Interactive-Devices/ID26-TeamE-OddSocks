"""Stage 'deep_sleep' + stimulus 'light'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no light in deep sleep. N3 is restorative and should be
protected from stimulation that could fragment sleep.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No light cue in deep sleep", True
