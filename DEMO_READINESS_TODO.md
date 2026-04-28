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
- [x] Stage files now include team intent notes from the research table.
- [x] Old placeholder stage files now return either explicit no-op or safe example scaffold behavior.
- [x] Systemd service template updated for `/home/odd/...` and root GPIO/SPI access.
- [x] README explains autostart and viewing service logs with `journalctl`.
- [x] Smell output stops when entering light sleep, deep sleep, not-worn, or unknown.
- [x] REM LED code now checks SPI, uses explicit `show()`, turns off, and deinitializes.
- [x] Awake/light sleep sound now starts or keeps looping `wave_noise.wav`.
- [x] Deep sleep sound fades out the background wave loop.
- [x] REM sound plays `wind_chimes.wav` as the callback cue.
- [x] Demo script plays stage announcement MP3s and a final thank-you MP3.
- [x] Demo stage runs now isolate stimulus failures and apply a demo timeout.
- [x] Manual demo `SEND <stage>` can auto-start a session.
- [x] REM below-pillow haptic now honors `demo_fast`.
- [x] Syntax check passes:
  `python3 -m py_compile pi/new-code/app.py pi/new-code/ble_transport.py pi/new-code/db.py pi/new-code/main.py pi/new-code/test_stimuli.py pi/new-code/hardware_setup.py pi/new-code/stages/*/*.py`

## Before Demo: Must Do

- [ ] Run on the Pi:
  `cd pi/new-code && python3 main.py --preflight --debug`
- [ ] Run on the Pi:
  `sudo python3 test_stimuli.py all --step`
- [ ] Run on the Pi:
  `sudo python3 test_stimuli.py all --simultaneous --duration 2 --cycles 2 --gap 5`
- [x] Confirm the watch app and its command bridge are both installed.
- [x] Confirm whether we are presenting with the demo controller app or the regular Dreamstream app.
- [ ] Confirm the real app starts and the watch can trigger `RUN DEMO`.

## Stage Files

### Filled / Existing Hardware Behavior

- [x] `stages/awake/watch_haptic.py`
- [x] `stages/rem/watch_haptic.py`
- [x] `stages/awake/smell.py`
- [ ] `stages/rem/smell.py` - works, but long background behavior needs demo review.
- [x] `stages/rem/light.py`
- [x] `stages/rem/pi_motor.py`

### Safe Example Scaffold

- [x] `stages/awake/sound.py` - starts looping `wave_noise.wav` and plays `wind_chimes.wav`.
- [x] `stages/light_sleep/sound.py` - keeps/restarts looping `wave_noise.wav`.
- [x] `stages/rem/sound.py` - plays `wind_chimes.wav` as the REM callback cue.

### Intentional No-op / Keep Off

- [x] `stages/awake/light.py`
- [x] `stages/awake/pi_motor.py`
- [x] `stages/light_sleep/light.py`
- [x] `stages/light_sleep/pi_motor.py`
- [x] `stages/light_sleep/watch_haptic.py`
- [x] `stages/light_sleep/smell.py`
- [x] `stages/deep_sleep/light.py`
- [x] `stages/deep_sleep/pi_motor.py`
- [x] `stages/deep_sleep/sound.py`
- [x] `stages/deep_sleep/watch_haptic.py`
- [x] `stages/deep_sleep/smell.py`
- [x] `stages/not_worn/*.py`
- [x] `stages/unknown/*.py`

## If Time Allows

- [ ] Implement one clear visible/tactile cue for `light_sleep`.
- [ ] Implement one clear visible/tactile cue for `deep_sleep`.
- [x] Implement demo speaker behavior using the shared DAC helper.
- [ ] Decide whether watch `STOP` should stop the whole session or only cancel the demo script.
- [x] Mark unused placeholder/no-op stage files clearly so logs do not imply unfinished behavior succeeded.
- [ ] Document Pi OS prerequisites in one place: `lgpio`, `bluetoothctl`, `rfkill`, `aplay`, `speaker-test`, `amixer`, SPI enabled.
- [ ] Optional: show a Pi acknowledgement on the watch after commands are received.
- [ ] Centralize hardware constants for pins, LED count, haptic pin, and audio defaults.
- [ ] Clean generated local files from git tracking consideration: DB/WAL/SHM, `.venv`, `.DS_Store`, `__pycache__`.
