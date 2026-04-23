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

Also accepted for convenience in test mode:

- `{"cmd":"light"}` -> treated as `light_sleep`
- `{"cmd":"deep"}` -> treated as `deep_sleep`

Dreamstream telemetry from the watch is accepted:

- `{"t":"dreamstream","seq":1,"ts":1773846600,"status":3,...}`

For dreamstream packets, the app:

- stores rows in `sleep_updates`
- maps numeric `status` to stage names used by this codebase
- updates `current_stage` each packet
- runs stage actions only on stage change while the session is running

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
