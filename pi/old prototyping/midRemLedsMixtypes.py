import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 3, brightness=0.01)

MODE = "pulse_crossfade"
# Options:
#   "pulse_solid"      — pulses a single solid colour
#   "pulse_crossfade"  — pulses while crossfading red <-> amber
#   "pulse_split"      — each LED a different colour, all pulse together
#   "pulse_chase"      — chase pattern that pulses in and out

RED   = (255, 0,   0)
AMBER = (255, 75,  0)
OFF   = (0,   0,   0)

PULSES      = 10
FADE_SLEEP  = 0.002
GAP         = 0.5

def set_brightness(b):
    pixels.brightness = b / 100

def fade_in():
    for b in range(0, 101):
        set_brightness(b)
        time.sleep(FADE_SLEEP)

def fade_out():
    for b in range(100, -1, -1):
        set_brightness(b)
        time.sleep(FADE_SLEEP)

def blend(colour_a, colour_b, t):
    return tuple(int(colour_a[i] + (colour_b[i] - colour_a[i]) * t) for i in range(3))


if MODE == "pulse_solid":
    for cycle in range(PULSES):
        pixels.fill(RED)
        fade_in()
        fade_out()
        pixels.fill(OFF)
        time.sleep(GAP)

elif MODE == "pulse_crossfade":
    for cycle in range(PULSES):
        for step in range(101):
            t = step / 100
            colour = blend(RED, AMBER, t)
            pixels.fill(colour)
            set_brightness(step)
            time.sleep(FADE_SLEEP)
        for step in range(100, -1, -1):
            t = step / 100
            colour = blend(AMBER, RED, 1 - t)
            pixels.fill(colour)
            set_brightness(step)
            time.sleep(FADE_SLEEP)
        pixels.fill(OFF)
        time.sleep(GAP)

elif MODE == "pulse_split":
    for cycle in range(PULSES):
        pixels[0] = RED
        pixels[1] = AMBER
        pixels[2] = RED
        fade_in()
        fade_out()
        pixels.fill(OFF)
        time.sleep(GAP)

elif MODE == "pulse_chase":
    colours = [RED, AMBER, RED]
    for cycle in range(PULSES):
        for offset in range(3):
            for i in range(3):
                pixels[i] = colours[(i + offset) % 3]
            fade_in()
            fade_out()
        pixels.fill(OFF)
        time.sleep(GAP)

pixels.fill(OFF)
