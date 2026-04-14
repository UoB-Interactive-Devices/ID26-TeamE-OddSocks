import lgpio

h = lgpio.gpiochip_open(0)
lgpio.tx_pwm(h, 17, 100, 0)
lgpio.gpio_write(h, 17, 0)
lgpio.gpiochip_close(h)
