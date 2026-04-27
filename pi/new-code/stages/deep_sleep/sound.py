"""Stage 'deep_sleep' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Team decision: no new sound cue in deep sleep. If background masking audio is
already running, do not add sharp stimulation here.
"""

from __future__ import annotations

import asyncio
import sys

import pygame


async def run(context: dict) -> tuple[str, str, bool]:
    if pygame.mixer.get_init():
        channel = getattr(sys, "_background_sound_channel", None)
        if channel is not None and channel.get_busy():
            channel.fadeout(2000)
            sys._background_sound_channel = None

    return "none", "No new sound cue in deep sleep (faded out)", True
