import drv2605
import time

d = drv2605.DRV2605()
d.set_sequence(0, 1)   # effect 1 in slot 0
d.set_sequence(1, 0)   # end marker
d.go()
time.sleep(1)
d.stop()
