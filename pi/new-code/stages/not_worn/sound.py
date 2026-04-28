"""Stage 'not_worn' + stimulus 'sound'.

This file owns the logic for this exact stage/stimulus combination.

Safety state: watch is not worn, so stop any background sound and do not emit
new cues.
"""

from __future__ import annotations

import sys

import pygame


async def run(context: dict) -> tuple[str, str, bool]:
    if pygame.mixer.get_init():
        channel = getattr(sys, "_background_sound_channel", None)
        if channel is not None and channel.get_busy():
            channel.fadeout(1000)
            sys._background_sound_channel = None
    return "none", "No sound cue when watch is not worn", True
