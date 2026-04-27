# Simple Pi Overnight Controller (new-code)

This folder contains a deliberately simple implementation for overnight running.

## Design goals

- Easy to read for multiple contributors.
- Minimal abstraction and minimal async (BLE loop only).
- Clear placeholders for stage-specific logic.
- Minimal tests/error-handling overhead to keep code approachable.

## File layout

- `main.py` - CLI entry point and startup.
- `app.py` - main session flow, packet normalisation, and stage dispatch.
- `ble_transport.py` - BLE scan/connect/listen + write-back helper.
- `db.py` - SQLite schema and inserts.
- `stages/<stage>/<stimulus>.py` - per-stage, per-stimulus logic modules.
- `systemd/sleep-pi-core.service` - startup-on-boot unit template.

## Accepted commands and packets

The parser currently accepts simple JSON forms:

- `{"cmd":"start"}`
- `{"cmd":"stop"}`
- `{"cmd":"stage","stage":"light_sleep"}`
- `{"stage":"deep_sleep"}`
- `{"cmd":"demo_run","stages":["awake","light_sleep","deep_sleep","rem"],"dwell_sec":0.35,"cycles":1}`
- `{"cmd":"demo_stop"}`

Also accepted for convenience in test mode:

- `{"cmd":"light"}` -> treated as `light_sleep`
- `{"cmd":"deep"}` -> treated as `deep_sleep`

Dreamstream telemetry from the regular watch app is accepted:

- `{"t":"dreamstream","seq":1,"ts":1773846600,"status":3,...}`

For dreamstream packets, the app:

- stores rows in `sleep_updates`
- maps numeric `status` to stage names used by this codebase
- updates `current_stage` each packet
- runs stage actions only on stage change while the session is running

The separate demo control watch app in `watch/demo_app_loader_files/` does not run sleep detection or send telemetry. It only sends the simple control packets listed above.

## Run

```bash
cd pi/new-code
pip install -r requirements.txt
python main.py --debug
```

Debug flags:

- `--debug`: app-level debug logs (received/sent packets, packet parsing, stage transitions).
- `--bleak-debug`: full verbose Bleak/backend logs (very noisy, use only when needed).

Example with full backend BLE debug:

```bash
python main.py --debug --bleak-debug
```

CLI test mode without BLE:

```bash
python main.py --cli-test --no-ble --debug
```

CLI test mode with BLE (connect first, then interactive prompt):

```bash
python main.py --cli-test --cli-test-ble --debug
```

In CLI mode:

- `status` shows app state plus `ble_connected=True/False`
- `haptic 120` sends a direct 120ms watch haptic command
- `start` then `stage rem` runs the REM stage stimuli using the active BLE link
- `demo_run` starts a fast scripted demo pass of all major stages
- `demo_stop` cancels an active scripted demo

## Hardware test script

`test_stimuli.py` is intended for one-output-at-a-time checks before running the full app:

```bash
sudo python3 test_stimuli.py haptic_motor
sudo python3 test_stimuli.py leds
python3 test_stimuli.py speaker
python3 test_stimuli.py watch_buzz
```

The script now registers cleanup handlers for GPIO/PWM outputs, so Ctrl-C should turn the Pi haptic motor off. When run as root, haptic cleanup also tries the same low-level fallback as `pinctrl set 23 dl`.

It also has a quick setup check:

```bash
sudo python3 test_stimuli.py preflight
```

For Bluetooth tests, the script tries to unblock Bluetooth, start `bluetooth.service`, and run `bluetoothctl power on` before scanning. Use `--no-auto-setup` to only report state without changing it.

To run all outputs at the same time, use the explicit simultaneous mode. It connects to the watch first, waits until BLE is connected, then runs all outputs together for `--duration` seconds. Use `--cycles` and `--gap` for repeated passes:

```bash
sudo python3 test_stimuli.py all --simultaneous --duration 2 --cycles 3 --gap 10
```

To step through the normal sequential checks manually, use `--step`. Press Enter for the next test, `r` to repeat the current test, or `q` to quit:

```bash
sudo python3 test_stimuli.py all --step
```

For speaker tests, `--audio-device auto` is the default. It picks the USB/PnP sound card from `aplay -l`, which handles the DAC appearing as card 0 after hotplug or card 1 after boot. You can override it when needed:

```bash
python3 test_stimuli.py speaker --audio-device plughw:1,0
python3 test_stimuli.py speaker --audio-device plughw:0,0
python3 test_stimuli.py speaker --audio-device default
```

If `watch_buzz` reports no powered Bluetooth adapters, check the Pi adapter state:

```bash
bluetoothctl show
sudo systemctl status bluetooth
sudo rfkill list bluetooth
```

If `speaker` fails with `Playback open error`, the Pi does not currently have a default ALSA output. Check devices with:

```bash
aplay -l
speaker-test -D plughw:1,0 -t sine -f 440 -l 1
speaker-test -D plughw:0,0 -t sine -f 440 -l 1
```

If the USB DAC is plugged in but `preflight` still says there are no ALSA playback devices, check the diagnostics it prints. `lsusb` seeing the DAC but `aplay -l` not listing it usually means the kernel audio driver is not loaded or the device was not enumerated as an ALSA sound card.

If `leds` reports `GPIO18 is busy` or makes the shell unresponsive, run it by itself rather than through `all` and stop any other script/service using LEDs or audio PWM first. The script now skips the NeoPixel test by default if GPIO18 is already claimed or if `/boot/firmware/config.txt`/`/boot/config.txt` has `dtparam=audio=on`, because GPIO18 NeoPixels use PWM and that conflict can leave the pin stuck until reboot. The LED hardware call runs in a short-lived worker process so the main script can time out if the NeoPixel backend hangs, but it cannot kill a worker stuck in uninterruptible kernel state. Once the Pi config is known-good, force a run with `sudo python3 test_stimuli.py leds --force-leds`. The demo strip is configured as 8 pixels.

## Demo mode notes

`demo_run` is intended for live demos where you want one tap to run all stages without waiting for real sleep detection.

- It auto-starts a session when needed.
- It runs stimuli for each requested stage in order (`awake`, `light_sleep`, `deep_sleep`, `rem` by default).
- It uses a `demo_fast` context so stage modules can shorten internal waits.

You can also trigger individual stage runs manually with:

```json
{"cmd":"stage","stage":"rem","demo_fast":true}
```

## Run on boot on the Pi

The repo already includes a simple systemd unit template at `systemd/sleep-pi-core.service`.

Systemd services run as root by default unless you add a `User=` line, so this is the clean way to have it run with sudo-style privileges on startup.

On the Pi:

```bash
cd /home/pi/ID26-TeamE-OddSocks/pi/new-code
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
sudo cp systemd/sleep-pi-core.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable sleep-pi-core.service
sudo systemctl start sleep-pi-core.service
```

Useful checks:

```bash
sudo systemctl status sleep-pi-core.service
sudo journalctl -u sleep-pi-core.service -f
```

If the repo lives somewhere other than `/home/pi/ID26-TeamE-OddSocks`, update the paths in `systemd/sleep-pi-core.service` before copying it into `/etc/systemd/system/`.

## Next implementation step

Replace placeholder modules in `stages/` with real stage logic for each stimulus.
Each file can directly implement the hardware/BLE action for that stage+stimulus.
