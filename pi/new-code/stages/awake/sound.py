"""Stage 'awake' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Example intent: start/keep a quiet masking sound, such as rainfall or waves,
and optionally play one distinct reality-cue chime before the sleep attempt.
Use the shared audio helper when replacing this example with real playback.
"""

from __future__ import annotations

import asyncio
import subprocess
import sys

from hardware_setup import resolve_speaker_command

SOUNDSCAPE_COMMAND = "speaker-test -t pink -l 0"
REALITY_CHIME_COMMAND = "speaker-test -t sine -f 440 -l 1"
AUDIO_DEVICE = "auto"


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]

    # Example background soundscape. Replace speaker-test pink noise with a
    # real rainfall/waves file later, keeping the same start-once structure.
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
            log.info("awake/sound background soundscape started")

        # Example pre-sleep reality cue. Swap this sine tone for the final
        # chime asset when ready.
        chime = resolve_speaker_command(REALITY_CHIME_COMMAND, AUDIO_DEVICE)
        chime_proc = await asyncio.create_subprocess_exec(
            *chime,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        await asyncio.wait_for(chime_proc.wait(), timeout=1.2)
    except Exception as exc:
        log.warning("awake/sound failed: %s", exc)
        return "sound_error", f"sound failed: {exc}", False

    return "soundscape_started", "Background soundscape running; played example pre-sleep chime", True
