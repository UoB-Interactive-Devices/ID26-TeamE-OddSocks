"""Stage 'awake' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Intent: start/keep a quiet masking wave sound and optionally play one distinct
reality-cue chime before the sleep attempt.
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
        from hardware_setup import init_pygame_audio
        await asyncio.wait_for(asyncio.to_thread(init_pygame_audio), timeout=3.0)

        channel = getattr(sys, "_background_sound_channel", None)
        if channel is None or not channel.get_busy():
            if os.path.exists(WAVE_FILE):
                sound = pygame.mixer.Sound(WAVE_FILE)
                channel = pygame.mixer.find_channel()
                if channel:
                    channel.play(sound, loops=-1, fade_ms=2000)
                    sys._background_sound_channel = channel
                    sys._background_sound = sound
                    log.info("awake/sound wave soundscape started")
            else:
                log.warning("awake/sound wave_noise.wav not found at %s", WAVE_FILE)

        # Table: "waits 5 minutes into the sleep attempt, then plays a distinct chime."
        wait_time = 2.0 if demo_fast else 300.0
        await asyncio.sleep(wait_time)

        if os.path.exists(CHIME_FILE):
            chime = pygame.mixer.Sound(CHIME_FILE)
            sys._chime_sound = chime
            chime.play()
            log.info("awake/sound wind chimes played")
        else:
            log.warning("awake/sound wind_chimes.wav not found at %s", CHIME_FILE)

    except Exception as exc:
        log.warning("awake/sound failed: %s", exc)
        return "sound_error", f"sound failed: {exc}", False

    return "soundscape_started", "Background wave running and played reality chime", True
