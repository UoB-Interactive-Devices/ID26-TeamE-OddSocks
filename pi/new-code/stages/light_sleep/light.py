"""Stage 'light_sleep' + stimulus 'light'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no light in light sleep. N1/N2 have a low arousal threshold
or filter external cues, so light is more likely to wake the user or be wasted.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No light cue in light sleep", True
