"""Stage 'rem' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Example intent: play the distinct chime/reality cue used before sleep, synced
with the REM cues. Use the shared audio helper when replacing this example
with real speaker playback.
"""

from __future__ import annotations

import asyncio
import subprocess

from hardware_setup import resolve_speaker_command

SOUND_COMMAND = "speaker-test -t sine -f 660 -l 1"
AUDIO_DEVICE = "auto"


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]
    # Example speaker pattern. Replace this tone with the same callback chime
    # used before sleep, synced with the REM light/haptic/scent cues.
    try:
        command = resolve_speaker_command(SOUND_COMMAND, AUDIO_DEVICE)
        proc = await asyncio.create_subprocess_exec(*command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        await asyncio.wait_for(proc.wait(), timeout=1.2)
    except Exception as exc:
        log.warning("rem/sound example failed: %s", exc)
        return "sound_example_error", f"example sound failed: {exc}", False

    return "sound_example", "Played example REM callback tone", True
