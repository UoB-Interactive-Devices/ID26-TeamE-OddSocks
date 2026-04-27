"""Stage 'deep_sleep' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no new sound cue in deep sleep. If background masking audio is
already running, do not add sharp stimulation here.
"""

from __future__ import annotations

import asyncio
import sys


async def run(context: dict) -> tuple[str, str, bool]:
    proc = getattr(sys, "_background_sound_proc", None)
    if proc is not None and proc.returncode is None:
        proc.terminate()
        try:
            await asyncio.wait_for(proc.wait(), timeout=1.0)
        except asyncio.TimeoutError:
            proc.kill()
            await proc.wait()
        sys._background_sound_proc = None

    return "none", "No new sound cue in deep sleep", True
