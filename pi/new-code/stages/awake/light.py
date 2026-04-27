"""Stage 'awake' + stimulus 'light'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no light is best before sleep. Blue/white light suppresses
melatonin, and even red/amber is risky around sleep onset. Keep this off.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No awake light cue; protect sleep onset", True
