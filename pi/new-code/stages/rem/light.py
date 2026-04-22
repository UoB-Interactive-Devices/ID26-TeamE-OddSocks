import time
import board
import neopixel

delayAftrRem = 3 * 60 #3mins
NoLEDs = 10

def run(remCycleNo):
    time.sleep(delayAftrRem)
    if remCycleNo <= 2:
        earlyRem()
    else:
        midNlateRem()

def earlyRem():
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
        pixels.fill((0, 0, 0))
        time.sleep(0.5)

    pixels.fill((0, 0, 0))

def midNlateRem():
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