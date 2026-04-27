"""Stage 'rem' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Example intent: play the distinct chime/reality cue used before sleep, synced
with the REM cues. Use the shared audio helper when replacing this example
with real speaker playback.
"""

from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

import pygame

CHIME_FILE = str(Path(__file__).resolve().parent.parent.parent / "wind_chimes.wav")


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]
    demo_fast = context.get("demo_fast", False)

    try:
        from hardware_setup import init_pygame_audio
        init_pygame_audio()

        # In REM, play the chime synchronized with the other cues.
        # Wait 3 minutes normally (synced with light), or very short in demo mode.
        wait_time = 0.5 if demo_fast else 180.0
        await asyncio.sleep(wait_time)

        if os.path.exists(CHIME_FILE):
            chime = pygame.mixer.Sound(CHIME_FILE)
            chime_channel = pygame.mixer.find_channel()
            if chime_channel:
                chime_channel.play(chime)
                log.info("rem/sound reality cue callback chime played")
        else:
            log.warning("rem/sound wind_chimes.wav not found at %s", CHIME_FILE)

    except Exception as exc:
        log.warning("rem/sound failed: %s", exc)
        return "sound_error", f"sound failed: {exc}", False

    return "rem_chime_played", "Played callback reality chime for REM", True
