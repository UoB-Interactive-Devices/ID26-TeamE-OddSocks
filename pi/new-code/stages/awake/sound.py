"""Stage 'awake' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Intent: start/keep the wave masking sound and play the chime as a callback
cue once immediately, then once again 5 minutes into the sleep attempt. Demo
mode shortens the 5 minute wait.
"""

from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

import pygame

WAVE_FILE = str(Path(__file__).resolve().parent.parent.parent / "wave_noise.wav")
CHIME_FILE = str(Path(__file__).resolve().parent.parent.parent / "wind_chimes.wav")


def _play_chime(log) -> bool:
    if not os.path.exists(CHIME_FILE):
        log.warning("awake/sound wind_chimes.wav not found at %s", CHIME_FILE)
        return False

    chime = pygame.mixer.Sound(CHIME_FILE)
    sys._chime_sound = chime
    chime.play()
    return True


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

        first_chime = _play_chime(log)
        if first_chime:
            log.info("awake/sound first wind chime played")

        wait_time = 2.0 if demo_fast else 300.0
        await asyncio.sleep(wait_time)

        second_chime = _play_chime(log)
        if second_chime:
            log.info("awake/sound second wind chime played")

    except Exception as exc:
        log.warning("awake/sound failed: %s", exc)
        return "sound_error", f"sound failed: {exc}", False

    return "soundscape_started", "Background wave running; played awake reality chimes", True
