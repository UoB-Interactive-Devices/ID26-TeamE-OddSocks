"""Stage 'deep_sleep' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Intent: no sound in deep sleep. Fade out any existing background wave audio so
the restorative stage stays quiet.
"""

from __future__ import annotations

import sys

import pygame


async def run(context: dict) -> tuple[str, str, bool]:
    if pygame.mixer.get_init():
        channel = getattr(sys, "_background_sound_channel", None)
        if channel is not None and channel.get_busy():
            channel.fadeout(2000)
            sys._background_sound_channel = None

    return "none", "No new sound cue in deep sleep (faded out)", True
