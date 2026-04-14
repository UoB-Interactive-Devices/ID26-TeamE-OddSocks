import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 3, brightness=0.01)

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
