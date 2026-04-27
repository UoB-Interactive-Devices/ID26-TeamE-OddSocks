"""Stage 'awake' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Example intent: start/keep a quiet masking sound, such as rainfall or waves,
and optionally play one distinct reality-cue chime before the sleep attempt.
Use the shared audio helper when replacing this example with real playback.
"""

from __future__ import annotations

import asyncio
import subprocess

from hardware_setup import resolve_speaker_command

SOUND_COMMAND = "speaker-test -t sine -f 440 -l 1"
AUDIO_DEVICE = "auto"


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]
    # Example speaker pattern. Replace this with rainfall/waves plus a real
    # chime sample when the sound design is ready.
    try:
        command = resolve_speaker_command(SOUND_COMMAND, AUDIO_DEVICE)
        proc = await asyncio.create_subprocess_exec(*command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        await asyncio.wait_for(proc.wait(), timeout=1.2)
    except Exception as exc:
        log.warning("awake/sound example failed: %s", exc)
        return "sound_example_error", f"example sound failed: {exc}", False

    return "sound_example", "Played example pre-sleep tone", True
