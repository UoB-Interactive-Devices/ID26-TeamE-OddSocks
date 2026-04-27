"""Stage 'awake' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Example intent: start/keep a quiet masking sound, such as rainfall or waves,
and optionally play one distinct reality-cue chime before the sleep attempt.
Use the shared audio helper when replacing this example with real playback.
"""

from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

import pygame

WAVE_FILE = str(Path(__file__).resolve().parent.parent.parent / "wave_noise.wav")
CHIME_FILE = str(Path(__file__).resolve().parent.parent.parent / "wind_chimes.wav")


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]
    demo_fast = context.get("demo_fast", False)

    try:
        if not pygame.mixer.get_init():
            pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=2048)
            pygame.mixer.init()

        # 1. Background masking wave noise
        channel = getattr(sys, "_background_sound_channel", None)
        if channel is None or not channel.get_busy():
            if os.path.exists(WAVE_FILE):
                sound = pygame.mixer.Sound(WAVE_FILE)
                # Play on an available channel, loop infinitely, fade in 2 seconds
                channel = pygame.mixer.find_channel()
                if channel:
                    channel.play(sound, loops=-1, fade_ms=2000)
                    sys._background_sound_channel = channel
                    log.info("awake/sound wave soundscape started")
            else:
                log.warning("awake/sound wave_noise.wav not found at %s", WAVE_FILE)

        # 2. Reality cue chime
        # Table: "waits 5 minutes into the sleep attempt, then plays a distinct chime."
        # In fast demo mode, we just wait a short moment (e.g. 2s) so it fits in the 20s awake block
        wait_time = 2.0 if demo_fast else 300.0
        await asyncio.sleep(wait_time)

        if os.path.exists(CHIME_FILE):
            chime = pygame.mixer.Sound(CHIME_FILE)
            chime_channel = pygame.mixer.find_channel()
            if chime_channel:
                chime_channel.play(chime)
                log.info("awake/sound wind chimes played")
        else:
            log.warning("awake/sound wind_chimes.wav not found at %s", CHIME_FILE)

    except Exception as exc:
        log.warning("awake/sound failed: %s", exc)
        return "sound_error", f"sound failed: {exc}", False

    return "soundscape_started", "Background wave running and played reality chime", True
