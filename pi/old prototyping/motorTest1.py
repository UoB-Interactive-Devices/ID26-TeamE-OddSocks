import lgpio
import time

CHIP = 0
PIN = 17

h = lgpio.gpiochip_open(CHIP)
lgpio.gpio_claim_output(h, PIN)

try:
    # gentle buzz (30% duty cycle)
    lgpio.tx_pwm(h, PIN, 100, 30)
    time.sleep(0.5)

    # stronger buzz (70% duty cycle)
    lgpio.tx_pwm(h, PIN, 100, 70)
    time.sleep(0.5)

    # full buzz (100% duty cycle)
    lgpio.tx_pwm(h, PIN, 100, 100)
    time.sleep(0.5)

finally:
    lgpio.tx_pwm(h, PIN, 100, 0)
    lgpio.gpiochip_close(h)
