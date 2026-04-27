"""Stage 'light_sleep' + stimulus 'smell'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no scent in light sleep. Keep air clear here to reduce
habituation/nose blindness before the REM peppermint cue.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No smell active for this stage", True
