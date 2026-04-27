"""Stage 'light_sleep' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Example intent: quiet masking sound can continue through light sleep to cover
disruptive noise, but should not introduce a new sharp cue.
"""

from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

import pygame

WAVE_FILE = str(Path(__file__).resolve().parent.parent.parent / "wave_noise.wav")


async def run(context: dict) -> tuple[str, str, bool]:
    log = context["log"]

    try:
        from hardware_setup import init_pygame_audio
        init_pygame_audio()

        channel = getattr(sys, "_background_sound_channel", None)
        if channel is None or not channel.get_busy():
            if os.path.exists(WAVE_FILE):
                sound = pygame.mixer.Sound(WAVE_FILE)
                channel = sound.play(loops=-1, fade_ms=2000)
                sys._background_sound_channel = channel
                log.info("light_sleep/sound wave soundscape started")
            else:
                log.warning("light_sleep/sound wave_noise.wav not found at %s", WAVE_FILE)

    except Exception as exc:
        log.warning("light_sleep/sound failed: %s", exc)
        return "sound_error", f"sound failed: {exc}", False

    return "soundscape_running", "Background wave soundscape running through light sleep", True
