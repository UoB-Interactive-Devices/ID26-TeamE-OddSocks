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

Sleepstream telemetry from the watch is also accepted:

- `{"t":"sleepstream","seq":1,"ts":1773846600,"status":3,...}`

For sleepstream packets, the app:

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

CLI test mode without BLE:

```bash
python main.py --cli-test --no-ble --debug
```

## Next implementation step

Replace placeholder modules in `stages/` with real stage logic for each stimulus.
Each file can directly implement the hardware/BLE action for that stage+stimulus.
