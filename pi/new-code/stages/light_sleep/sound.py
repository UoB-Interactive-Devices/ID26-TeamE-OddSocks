"""Stage 'light_sleep' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Example intent: quiet masking sound can continue through light sleep to cover
disruptive noise, but should not introduce a new sharp cue.
"""

from __future__ import annotations

import asyncio
import subprocess

from hardware_setup import resolve_speaker_command

SOUND_COMMAND = "speaker-test -t sine -f 330 -l 1"
AUDIO_DEVICE = "auto"


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]
    # Example speaker pattern. Replace this with continuous low masking audio
    # if the team chooses to keep sound running through light sleep.
    try:
        command = resolve_speaker_command(SOUND_COMMAND, AUDIO_DEVICE)
        proc = await asyncio.create_subprocess_exec(*command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        await asyncio.wait_for(proc.wait(), timeout=1.2)
    except Exception as exc:
        log.warning("light_sleep/sound example failed: %s", exc)
        return "sound_example_error", f"example sound failed: {exc}", False

    return "sound_example", "Played example quiet masking tone", True
