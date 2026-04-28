# OddSocks / Dreamstream Demo Handoff

Last updated: 2026-04-28

This is the quick context file for picking up the Pi/watch demo work in another worktree.

## Project In One Paragraph

OddSocks / Dreamstream is a Raspberry Pi + Bangle.js 2 sleep demo. The watch sends simple BLE control packets to the Pi. The Pi runs stage-specific stimulus files for awake, light sleep, deep sleep, and REM. The demo is not trying to prove full sleep classification live; it is showing the hardware, watch control app, and stage logic working together in a simple, understandable way.

## Important Principle

Keep the codebase simple. Prefer direct, readable code over extra layers. The team needs to be able to open a stage file and quickly change what that stage does. Avoid new frameworks, clever abstractions, or unnecessary edge-case machinery.

## Main Working Area

Only work in:

```text
pi/new-code
```

Key files:

- `main.py` - CLI entry point, startup preflight, starts the app.
- `app.py` - packet parsing, session state, demo runner, stage dispatch.
- `ble_transport.py` - BLE scan/connect/listen/write helper.
- `hardware_setup.py` - small shared setup helpers for Bluetooth, DAC, volume, SPI.
- `test_stimuli.py` - manual hardware test script; confirmed working on device.
- `stages/<stage>/<stimulus>.py` - each stage/stimulus lives in its own file.
- `watch/demo_app_loader_files/` - Bangle demo controller app used for presentation.
- `watch/app_loader_files/` - regular Dreamstream tracking app, not the demo controller.
- `systemd/sleep-pi-core.service` - autostart service template for the Pi.

## Hardware / Wiring Assumptions

- Pi username/path used in the service template:
  `/home/odd/ID26-TeamE-OddSocks/pi/new-code`
- LED strip: SPI NeoPixel on SPI0 MOSI, GPIO10, physical pin 19.
- LED count: 8.
- Pi haptic motor: GPIO23.
- Nebuliser 1 / lavender: GPIO12.
- Nebuliser 2 / peppermint: GPIO16.
- Speaker: USB/PnP DAC, auto-detected from `aplay -l`.
- Audio playback: pygame mixer, initialized through `hardware_setup.init_pygame_audio()`.
- Bluetooth: Pi connects to Bangle.js 2 over Nordic UART.

## Confirmed Working

- `test_stimuli.py` works on the device.
- Watch and command bridge are installed.
- Presentation uses the separate demo controller app.
- Regular Dreamstream app was restored to no demo buttons.
- Demo controller app has `RUN DEMO`, `NEXT`, `SEND`, and `STOP`.

## Pi Commands

Preflight:

```bash
cd /home/odd/ID26-TeamE-OddSocks/pi/new-code
python3 main.py --preflight --debug
```

Manual all-output tests:

```bash
sudo python3 test_stimuli.py all --step
sudo python3 test_stimuli.py all --simultaneous --duration 2 --cycles 2 --gap 5
```

Run app manually:

```bash
python3 main.py --debug
```

Install/start autostart service:

```bash
cd /home/odd/ID26-TeamE-OddSocks/pi/new-code
sudo cp systemd/sleep-pi-core.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable sleep-pi-core.service
sudo systemctl restart sleep-pi-core.service
```

Watch logs from RPi Connect shell:

```bash
sudo journalctl -u sleep-pi-core.service -f
```

Check service:

```bash
sudo systemctl status sleep-pi-core.service
```

When ready, logs should show the Bangle being found and connected, e.g. `BLE found watch` and `BLE connected`.

## Watch Apps

Use this for the demo:

```text
pi/new-code/watch/demo_app_loader_files/metadata.json
```

This app only controls the Pi. It does not run full Dreamstream sleep detection.

Regular Dreamstream app:

```text
pi/new-code/watch/app_loader_files/metadata.json
```

This should stay clean: start/stop tracking, metrics, last Pi command. It should not have demo controls.

## Demo Flow

1. Plug in / boot Pi.
2. Open RPi Connect shell.
3. Watch logs:
   `sudo journalctl -u sleep-pi-core.service -f`
4. Wait for Bangle BLE connection.
5. On the Bangle demo app, press `RUN DEMO`.
6. The Pi runs stages in order:
   `awake`, `light_sleep`, `deep_sleep`, `rem`.

Manual stage testing from watch:

- `NEXT` cycles selected stage.
- `SEND` sends that stage with `demo_fast: true`.
- Manual stage send can auto-start a session.

## Current Stage Logic

Awake:

- `light.py`: intentional no light.
- `pi_motor.py`: intentional no pillow haptic.
- `smell.py`: steady lavender release on GPIO12 for 10 minutes, shortened in demo mode.
- `sound.py`: starts looping `wave_noise.wav`, plays `wind_chimes.wav`, waits, then plays it again.
- `watch_haptic.py`: short watch callback cue.

Light sleep:

- `light.py`: intentional no light.
- `pi_motor.py`: intentional no pillow haptic.
- `smell.py`: stops any smell task.
- `sound.py`: keeps/restarts looping `wave_noise.wav`.
- `watch_haptic.py`: intentional no wrist haptic.

Deep sleep:

- `light.py`: intentional no light.
- `pi_motor.py`: intentional no pillow haptic.
- `smell.py`: stops any smell task.
- `sound.py`: fades out background sound; no new sound cue.
- `watch_haptic.py`: intentional no wrist haptic.

REM:

- `light.py`: waits 3 minutes, then pulses red or red/amber LEDs; demo mode shortens the wait and pulse window.
- `pi_motor.py`: waits 3 minutes, then plays below-pillow irregular haptic bursts; demo mode shortens wait, bursts, and gaps.
- `smell.py`: pulses peppermint on GPIO16 for 15 minutes, shortened in demo mode.
- `sound.py`: waits 3 minutes, then plays `wind_chimes.wav` as the callback cue.
- `watch_haptic.py`: waits 3 minutes, then plays wrist haptic bursts; demo mode shortens wait, bursts, and gaps.

Unknown / not worn:

- All stimuli are explicit no-ops/safety states.

## Audio State

The main app and stage files now use pygame audio.

Shared setup:

- `hardware_setup.init_pygame_audio()` auto-detects the USB/PnP DAC, sets SDL/ALSA env vars, and initializes `pygame.mixer`.
- `requirements.txt` includes `pygame>=2.6.0`.
- Startup preflight still sets safe mixer volume using `amixer` through `hardware_setup.set_speaker_volume()`.

Demo narration assets:

- `awake_stage.mp3`
- `light_stage.mp3`
- `deep_stage.mp3`
- `rem_stage.mp3`
- `thank_you.mp3`

Stage stimulus assets:

- `wave_noise.wav`
- `wind_chimes.wav`

Behavior:

- Demo runner plays the stage MP3 announcements before each stage, and `thank_you.mp3` at the end.
- Awake sound starts looping `wave_noise.wav`, plays `wind_chimes.wav`, waits 2 seconds in demo mode or 5 minutes normally, then plays `wind_chimes.wav` again.
- Light sleep sound keeps or restarts the same wave loop.
- Deep sleep sound fades out the wave loop.
- REM sound waits 0.5 seconds in demo mode or 3 minutes normally, then plays `wind_chimes.wav`.

## Current Todo

See `DEMO_READINESS_TODO.md` for the checklist.

Most important remaining items:

- Test actual demo controller app against the systemd-running main app.
- Confirm `RUN DEMO` works end to end from the watch.
- Decide whether `STOP` on the watch should stop the whole session or only cancel the demo script.
- Optional: show a Pi acknowledgement on the watch after commands are received.

## Common Gotchas

- If watch buzz fails at connection time but logs show `BLE found watch`, the Pi saw the watch but BlueZ/Bleak did not finish connecting. Close app loader/browser/phone connections and try again. Restart Bluetooth if needed:
  `sudo systemctl restart bluetooth`.
- `test_stimuli.py watch_buzz` now waits longer by default, because BLE scan + connect can take more than 20 seconds.
- The systemd service must point to the actual Pi checkout path. Current template assumes `/home/odd/ID26-TeamE-OddSocks`.
- Regular Dreamstream app should not show demo buttons. If it does, check `watch/app_loader_files/dreamstream.app.js`.
- Demo controller is separate and lives in `watch/demo_app_loader_files`.

## Verification Commands

Syntax check:

```bash
python3 -m py_compile pi/new-code/app.py pi/new-code/ble_transport.py pi/new-code/db.py pi/new-code/main.py pi/new-code/test_stimuli.py pi/new-code/hardware_setup.py pi/new-code/stages/*/*.py
```

Search for accidental old scaffolding:

```bash
rg "TODO: replace|action = \"scaffold\"|Scaffold modules" pi/new-code/stages
```
