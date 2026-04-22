from __future__ import annotations
import time
import board
import neopixel
import asyncio

delayAftrRem = 3 * 60 #3mins
NoLEDs = 10
remCycleNo = 3

async def run(context: dict) -> tuple[str, str, bool]:
    #commented out for testing
    #time.sleep(delayAftrRem)
    print("running")
    if remCycleNo <= 2:
        earlyRem()
    else:
        midNlateRem()

    return "light cues started", "5 or 10s brust, colour depndent on NremCycle", True

async def earlyRem():
    print("executing earlyRem")
    pixels = neopixel.NeoPixel(board.D18, NoLEDs, brightness=0.01)

    for cycle in range(5):
        print(cycle)
        for b in range(0, 100):
            pixels.brightness = b / 100
            pixels.fill((255, 0, 0))
            time.sleep(0.002)
        for b in range(100, 0, -1):
            pixels.brightness = b / 100
            pixels.fill((255, 0, 0))
            time.sleep(0.002)
        pixels.fill((0, 0, 0))
        time.sleep(0.5)

    pixels.fill((0, 0, 0))

async def midNlateRem():
    print("executing midRem")
    pixels = neopixel.NeoPixel(board.D18, NoLEDs, brightness=0.01)

    for cycle in range(5):
            for b in range(0, 100):
                pixels.brightness = b / 100
                pixels.fill((255, 0, 0))
                time.sleep(0.002)
            for b in range(100, 0, -1):
                pixels.brightness = b / 100
                pixels.fill((255, 0, 0))
                time.sleep(0.002)
            for b in range(0, 100):
                pixels.brightness = b / 100
                pixels.fill((255, 60, 0))
                time.sleep(0.002)
            for b in range(100, 0, -1):
                pixels.brightness = b / 100
                pixels.fill((255, 60, 0))
                time.sleep(0.002)

    pixels.fill((0, 0, 0))