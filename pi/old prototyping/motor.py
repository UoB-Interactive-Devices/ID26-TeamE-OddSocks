#works for og 3 pin haptic breakout board, no motor attached to 5pin yet
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

GPIO.output(17, GPIO.HIGH)
time.sleep(0.5)
GPIO.output(17, GPIO.LOW)

GPIO.cleanup()
