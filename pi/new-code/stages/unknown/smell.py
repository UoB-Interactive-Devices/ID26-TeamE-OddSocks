"""Stage 'unknown' + stimulus 'smell'.

This file owns the logic for this exact stage/stimulus combination.

Safety state: stage is unknown, so do not emit cues.
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
    return "none", "Smell stopped; no smell cue for unknown stage", True
