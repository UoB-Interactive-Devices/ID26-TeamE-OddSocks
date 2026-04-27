"""Stage 'light_sleep' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Example intent: quiet masking sound can continue through light sleep to cover
disruptive noise, but should not introduce a new sharp cue.
"""

from __future__ import annotations

import asyncio
import subprocess
import sys

from hardware_setup import resolve_speaker_command

SOUNDSCAPE_COMMAND = "speaker-test -t pink -l 0"
AUDIO_DEVICE = "auto"


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]

    # Keep the awake background soundscape running through light sleep. If it
    # is not already running, start it here.
    try:
        proc = getattr(sys, "_background_sound_proc", None)
        if proc is None or proc.returncode is not None:
            command = resolve_speaker_command(SOUNDSCAPE_COMMAND, AUDIO_DEVICE)
            proc = await asyncio.create_subprocess_exec(
                *command,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            sys._background_sound_proc = proc
            log.info("light_sleep/sound background soundscape started")
    except Exception as exc:
        log.warning("light_sleep/sound failed: %s", exc)
        return "sound_error", f"sound failed: {exc}", False

    return "soundscape_running", "Background soundscape running through light sleep", True
