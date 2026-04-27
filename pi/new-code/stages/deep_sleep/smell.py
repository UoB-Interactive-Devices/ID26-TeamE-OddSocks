"""Stage 'deep_sleep' + stimulus 'smell'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no scent in deep sleep. Keep stimulation low during N3 and
preserve scent sensitivity for the later REM cue.
"""

from __future__ import annotations

import asyncio
import sys


async def run(context: dict) -> tuple[str, str, bool]:
    task = getattr(sys, "_smell_mist_task", None)
    if task is not None and not task.done():
        task.cancel()
        try:
            await asyncio.wait_for(task, timeout=1.0)
        except (asyncio.CancelledError, asyncio.TimeoutError):
            pass
    sys._smell_mist_task = None
    sys._smell_handle = None
    return "none", "Smell stopped; no scent active for deep sleep", True
