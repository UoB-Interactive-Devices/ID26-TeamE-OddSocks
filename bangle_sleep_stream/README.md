# bangle_sleep_stream

Streams sleep state from a Bangle.js 2 watch over BLE to a Python receiver that persists updates in SQLite.

Sleep classification runs on-watch using the same algorithm as the [sleeplog](https://banglejs.com/apps/#sleeplog) app — movement/HRM thresholds, consecutive sleep tracking, and HRM-based wear detection. When sleep monitoring mode is activated, a continuous epoch-based classifier adds **REM sleep detection** using accelerometer activity and HRV (heart rate variability) features.

## How it works

1. Watch health event fires every ~10 minutes.
2. Boot service classifies sleep state (unknown / not_worn / awake / light / deep / **rem**).
3. JSON update is sent over BLE UART: `{"t":"sleepstream","v":1,"seq":1,"ts":1773846600,"status":5,"consecutive":0,"source_mode":1,"movement":595,"bpm":56,"sdhr":4.2}`
4. Receiver decodes and stores in SQLite.

### Sleep monitoring mode

For REM detection, the watch runs a continuous monitoring mode that must be **manually activated** from the debug app (bottom-right touch on page 1):

- Enables HRM sensor and accelerometer listeners.
- Processes 60-second epochs computing: activity (accel MAD), mean HR, HR standard deviation (sdHR).
- Classifies each epoch using a rule-based state machine considering HR percentiles, REM latency (~60 min), and temporal smoothing.
- Logs all epochs to on-device storage (`sleepstream.epochs.log`) for post-hoc analysis — this data persists even if BLE disconnects or the receiver crashes.
- When the 10-minute health event fires, it uses the classifier's current stage instead of the simple threshold classifier.

**Battery note:** Continuous HRM increases battery drain. The watch should last an 8-hour sleep session, but expect reduced daytime battery compared to the non-monitoring mode.

## Watch files (upload via Espruino Web IDE)

| File | Purpose |
|------|---------|
| `sleepstream.boot.js` | Background service — health listener, sleep state machine, monitoring pipeline, BLE send |
| `sleepstream.js` | Shared module — constants, settings, feature extraction, classifier, night context |
| `sleepstream.settings.js` | On-watch settings menu for thresholds, epoch length, REM latency |
| `sleepstream.app.js` | Debug app — live status, epoch features, monitoring toggle, log tail (3 pages) |

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
| `status` | int | 0=unknown, 1=not_worn, 2=awake, 3=light_sleep, 4=deep_sleep, **5=rem_sleep** |
| `consecutive` | int | 0=unknown, 1=no, 2=yes |
| `source_mode` | int | 0=movement, 1=hrm |
| `movement` | int/null | Movement value or null |
| `bpm` | int/null | Heart rate or null |
| `sdhr` | float/null | HR standard deviation (when monitoring active) or absent |

## On-device epoch log

When monitoring is active, each epoch is logged to `sleepstream.epochs.log` on the Bangle's storage as CSV:

```
unix_ts,status,meanHR,sdHR,activity
1773846660,3,58.2,2.1,0.0180
1773846720,5,64.7,5.3,0.0120
```

Retrieve via the Espruino Web IDE Storage panel.
