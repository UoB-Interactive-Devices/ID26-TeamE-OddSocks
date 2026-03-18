# bangle_sleep_stream

Streams sleep state from a Bangle.js 2 watch over BLE to a Python receiver that persists updates in SQLite.

Sleep classification runs on-watch using the same algorithm as the [sleeplog](https://banglejs.com/apps/#sleeplog) app — movement/HRM thresholds, consecutive sleep tracking, and HRM-based wear detection.

## How it works

1. Watch health event fires every ~10 minutes.
2. Boot service classifies sleep state (unknown / not_worn / awake / light / deep).
3. JSON update is sent over BLE UART: `{"t":"sleepstream","v":1,"seq":1,"ts":1773846600,"status":2,"consecutive":0,"source_mode":0,"movement":595,"bpm":56}`
4. Receiver decodes and stores in SQLite.

## Watch files (upload via Espruino Web IDE)

| File | Purpose |
|------|---------|
| `sleepstream.boot.js` | Background service — health listener, sleep state machine, BLE send |
| `sleepstream.js` | Shared module — constants, settings load/save |
| `sleepstream.settings.js` | On-watch settings menu for thresholds |
| `sleepstream.app.js` | Debug app — live status + log tail (2 pages) |

## Receiver

```bash
cd receiver
pip install -r requirements.txt
python sleep_receiver.py --debug
```

The receiver scans for any device whose name starts with `Bangle` (override with `--name-prefix`), subscribes to UART notifications, and persists packets to `sleepstream.db`.

Run `python sleep_receiver.py --help` for all options. For production, use the systemd unit in `receiver/systemd/`.

## UART JSON packet format

| Field | Type | Description |
|-------|------|-------------|
| `t` | string | Always `"sleepstream"` |
| `v` | int | Protocol version (1) |
| `seq` | int | Monotonic sequence number |
| `ts` | int | Watch timestamp (seconds UTC) |
| `status` | int | 0=unknown, 1=not_worn, 2=awake, 3=light_sleep, 4=deep_sleep |
| `consecutive` | int | 0=unknown, 1=no, 2=yes |
| `source_mode` | int | 0=movement, 1=hrm |
| `movement` | int/null | Movement value or null |
| `bpm` | int/null | Heart rate or null |
