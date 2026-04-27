"""Stage 'deep_sleep' + stimulus 'smell'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no scent in deep sleep. Keep stimulation low during N3 and
preserve scent sensitivity for the later REM cue.
"""

from __future__ import annotations


async def run(context: dict) -> tuple[str, str, bool]:
    return "none", "No smell active for this stage", True
