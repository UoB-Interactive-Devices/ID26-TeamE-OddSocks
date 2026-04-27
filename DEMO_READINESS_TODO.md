# Demo Readiness Todo

Status key: `[x]` done, `[ ]` still needed.

## Done Now

- [x] Shared prerequisite helpers added in `pi/new-code/hardware_setup.py`.
- [x] `hardware_setup.py` kept deliberately small: plain functions, no extra framework.
- [x] Main app now runs startup prerequisite checks before launching.
- [x] Main app can run preflight only: `python main.py --preflight --debug`.
- [x] Bluetooth auto-setup moved into shared code: unblock, start service, power on.
- [x] USB/PnP DAC auto-detection moved into shared code.
- [x] Safe speaker volume startup setting added, default `--speaker-volume 20`.
- [x] SPI LED prerequisite check added for `/dev/spidev0.0`.
- [x] `test_stimuli.py` now uses the same shared Bluetooth/audio/preflight helpers.
- [x] README updated with the new main-app setup flags.
- [x] Syntax check passes:
  `python3 -m py_compile pi/new-code/app.py pi/new-code/ble_transport.py pi/new-code/db.py pi/new-code/main.py pi/new-code/test_stimuli.py pi/new-code/hardware_setup.py pi/new-code/stages/*/*.py`

## Before Demo: Must Do

- [ ] Run on the Pi:
  `cd pi/new-code && python3 main.py --preflight --debug`
- [ ] Run on the Pi:
  `sudo python3 test_stimuli.py all --step`
- [ ] Run on the Pi:
  `sudo python3 test_stimuli.py all --simultaneous --duration 2 --cycles 2 --gap 5`
- [ ] Confirm the watch app and its command bridge are both installed.
- [ ] Confirm whether we are presenting with the demo controller app or the regular Dreamstream app.
- [ ] Confirm the main app is launched with GPIO/SPI permissions, ideally via sudo or systemd root service.
- [ ] Confirm the real app starts and the watch can trigger `RUN DEMO`.
- [ ] Add `demo_fast` short timing to `stages/rem/pi_motor.py`.
- [ ] Stop/cancel smell output when entering no-smell stages.
- [ ] Add per-stimulus timeout/failure isolation in `app.py`.
- [ ] Make manual watch `SEND <stage>` auto-start or clearly require an active session.

## Stage Files

### Filled

- [x] `stages/awake/watch_haptic.py`
- [x] `stages/rem/watch_haptic.py`

### Partial

- [ ] `stages/awake/smell.py` - works, but smell carry-over cleanup needs fixing.
- [ ] `stages/rem/smell.py` - works, but long background behavior needs demo review.
- [ ] `stages/rem/light.py` - SPI LEDs implemented, but cleanup/preflight should match `test_stimuli.py`.
- [ ] `stages/rem/pi_motor.py` - haptic implemented, but lacks `demo_fast` and safer cleanup.

### Intentional No-op

- [ ] `stages/light_sleep/smell.py` - should also stop previous smell task.
- [ ] `stages/deep_sleep/smell.py` - should also stop previous smell task.

### Still Placeholder

- [ ] `stages/awake/light.py`
- [ ] `stages/awake/pi_motor.py`
- [ ] `stages/awake/sound.py`
- [ ] `stages/light_sleep/light.py`
- [ ] `stages/light_sleep/pi_motor.py`
- [ ] `stages/light_sleep/sound.py`
- [ ] `stages/light_sleep/watch_haptic.py`
- [ ] `stages/deep_sleep/light.py`
- [ ] `stages/deep_sleep/pi_motor.py`
- [ ] `stages/deep_sleep/sound.py`
- [ ] `stages/deep_sleep/watch_haptic.py`
- [ ] `stages/rem/sound.py`
- [ ] `stages/not_worn/light.py`
- [ ] `stages/not_worn/pi_motor.py`
- [ ] `stages/not_worn/smell.py`
- [ ] `stages/not_worn/sound.py`
- [ ] `stages/not_worn/watch_haptic.py`
- [ ] `stages/unknown/light.py`
- [ ] `stages/unknown/pi_motor.py`
- [ ] `stages/unknown/smell.py`
- [ ] `stages/unknown/sound.py`
- [ ] `stages/unknown/watch_haptic.py`

## If Time Allows

- [ ] Implement one clear visible/tactile cue for `light_sleep`.
- [ ] Implement one clear visible/tactile cue for `deep_sleep`.
- [ ] Implement demo speaker behavior using the shared DAC helper.
- [ ] Decide whether watch `STOP` should stop the whole session or only cancel the demo script.
- [ ] Mark unused placeholder/no-op stage files clearly so logs do not imply unfinished behavior succeeded.
- [ ] Document Pi OS prerequisites in one place: `lgpio`, `bluetoothctl`, `rfkill`, `aplay`, `speaker-test`, `amixer`, SPI enabled.
- [ ] Optional: show a Pi acknowledgement on the watch after commands are received.
- [ ] Centralize hardware constants for pins, LED count, haptic pin, and audio defaults.
- [ ] Clean generated local files from git tracking consideration: DB/WAL/SHM, `.venv`, `.DS_Store`, `__pycache__`.
