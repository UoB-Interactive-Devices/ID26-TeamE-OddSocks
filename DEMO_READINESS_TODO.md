# Demo Readiness Todo

This tracks gaps between the hardware/stimuli test path and the real demo path in `pi/new-code`.

Last lightweight check:

- `python3 -m py_compile pi/new-code/app.py pi/new-code/ble_transport.py pi/new-code/db.py pi/new-code/main.py pi/new-code/test_stimuli.py pi/new-code/stages/*/*.py` passes.
- Hardware behavior still needs to be checked on the Pi; local syntax checks cannot prove GPIO, SPI, ALSA, or BLE behavior.

Legend:

- `P0`: should fix before the live demo.
- `P1`: useful if time allows.
- `P2`: tidy-up after the demo.

## Prerequisite / Setup Gaps

| Priority | Area | Works in `test_stimuli.py`? | Carried into main/demo app? | Todo | Files |
|---|---|---:|---:|---|---|
| P0 | Bluetooth power/setup | Yes. The test script can unblock Bluetooth, start `bluetooth.service`, and run `bluetoothctl power on`. | Partly. The systemd unit wants `bluetooth.service`, but `main.py`/`ble_transport.py` do not actively power on or report adapter state before scanning. | Add a lightweight startup/preflight path for the main app, or document one required terminal command before demo. | `pi/new-code/test_stimuli.py`, `pi/new-code/main.py`, `pi/new-code/ble_transport.py`, `pi/new-code/systemd/sleep-pi-core.service` |
| P0 | Speaker DAC selection | Yes. Default is `--audio-device auto`, which searches `aplay -l` and picks the USB/PnP DAC whether it appears as card 0 or card 1. | No. Stage `sound.py` files are placeholders, so the main app does not currently pick an ALSA device or play anything. | Port the audio-device resolver into a small shared helper, then use it from real stage sound modules. | `pi/new-code/test_stimuli.py`, `pi/new-code/stages/*/sound.py` |
| P0 | Speaker volume safety | No current code sets volume. This was handled manually with `alsamixer`/`amixer`. | No. | Add an explicit safe default volume command for USB DAC before any speaker playback, or document the manual command. For IEMs, default should be low, not 100%. | new helper needed; probably sound helper plus README |
| P0 | SPI LED prerequisite | Partly. Test script assumes `board.SPI()` works and errors clearly if `board/neopixel_spi` is unavailable. README documents GPIO10/MOSI and `/dev/spidev0.0`. | Partly. REM light uses SPI NeoPixel, but the main app has no preflight check for `/dev/spidev0.0` or SPI being enabled. | Add preflight diagnostics or a startup log warning if SPI is unavailable. | `pi/new-code/test_stimuli.py`, `pi/new-code/stages/rem/light.py`, `pi/new-code/README.md` |
| P1 | Requirements / OS packages | Python requirements include `bleak` and `adafruit-circuitpython-neopixel-spi`. | Partly. GPIO code imports `lgpio`, but it is not in `requirements.txt` because it is normally OS-provided on the Pi. | Document/install-check OS prerequisites: `lgpio`, `bluetoothctl`, `rfkill`, `speaker-test`, `aplay`, SPI enabled. | `pi/new-code/requirements.txt`, `pi/new-code/README.md` |

## Logic Gaps Between Test Script And Main App

| Priority | Area | Test behavior | Main/demo behavior | Todo | Files |
|---|---|---|---|---|---|
| P0 | Speaker stage logic | `speaker` and simultaneous tests use `speaker-test` with USB DAC auto-detection. | All stage sound modules currently return placeholders. No sound will play during the watch-driven demo. | Implement at least one demo-safe sound action, probably REM or stage-specific short tones, using the same DAC selection logic as the test script. | `pi/new-code/test_stimuli.py`, `pi/new-code/stages/rem/sound.py`, `pi/new-code/stages/awake/sound.py`, `pi/new-code/stages/light_sleep/sound.py`, `pi/new-code/stages/deep_sleep/sound.py` |
| P0 | REM Pi haptic demo timing | Test haptic motor uses the requested short duration and always cleans up. | `rem/pi_motor.py` ignores `demo_fast` and can wait 60 seconds between bursts. Watch `RUN DEMO` can look stuck in REM. | Add `demo_fast` behavior matching `rem/watch_haptic.py`: one short burst, tiny/no gap. | `pi/new-code/stages/rem/pi_motor.py`, `pi/new-code/stages/rem/watch_haptic.py` |
| P0 | Stage failure isolation | Test simultaneous mode uses `asyncio.gather(..., return_exceptions=True)` and reports per-output failures. | Main `run_stage()` uses plain `asyncio.gather`; one hardware exception can abort the entire stage. | Make stage execution log per-stimulus failures and keep the other stimuli/stage flow moving. | `pi/new-code/app.py` |
| P0 | Smell task carry-over | Test nebuliser actions are time-bounded and always turn off. | `awake/smell.py` and `rem/smell.py` start long background tasks. `light_sleep/smell.py` and `deep_sleep/smell.py` say "none" but do not cancel an existing smell task. | Add shared smell stop/cleanup behavior, and call it from no-smell stages. | `pi/new-code/stages/awake/smell.py`, `pi/new-code/stages/rem/smell.py`, `pi/new-code/stages/light_sleep/smell.py`, `pi/new-code/stages/deep_sleep/smell.py` |
| P0 | Manual stage command requires a running session | Test script directly runs the chosen hardware action. | The demo watch app's `SEND <stage>` sends a stage packet, but `app.py` only handles stage packets when `self.state == "running"`. If nobody pressed `RUN DEMO` or `START`, manual stage buttons appear to do nothing. | Either make `SEND <stage>` auto-start, add a visible warning/instruction, or make `app.py` optionally auto-start for `demo_fast` stage commands. | `pi/new-code/watch/demo_app_loader_files/oddsocks_demo.app.js`, `pi/new-code/app.py` |
| P0 | Demo run duration is not bounded by `dwell_sec` | Test simultaneous mode uses explicit `--duration`. | `demo_run` uses `dwell_sec` only after each stage finishes; it does not interrupt long stage modules. Long smell tasks are backgrounded, but REM Pi haptic can still block. | Treat every demo-facing stage module as responsible for honoring `demo_fast` and returning quickly. | `pi/new-code/app.py`, `pi/new-code/stages/rem/pi_motor.py`, all stage modules |
| P1 | LED cleanup parity | Test LEDs use `auto_write=False`, explicit `.show()`, fill black, and call `deinit()` if available. | `rem/light.py` creates `NeoPixel_SPI(..., brightness=0.01)` without `auto_write=False` or `deinit()`. It does turn pixels black at the end. | Port the test script's explicit show/deinit cleanup pattern into REM light. | `pi/new-code/test_stimuli.py`, `pi/new-code/stages/rem/light.py` |
| P1 | GPIO cleanup parity | Test haptic motor has signal cleanups, `gpio_free`, `gpiochip_close`, and `pinctrl set 23 dl` fallback. | `rem/pi_motor.py` stops PWM and closes the chip, but does not `gpio_free` or use the `pinctrl` fallback. | Consider porting the safer cleanup class from test script to reusable hardware helper. | `pi/new-code/test_stimuli.py`, `pi/new-code/stages/rem/pi_motor.py` |
| P1 | Hardware constants duplication | Test script centralizes pins: nebulisers 12/16, haptic 23, LEDs 8. | Stage modules repeat constants locally. | Move shared hardware config to one module to avoid wiring drift. | `pi/new-code/test_stimuli.py`, `pi/new-code/stages/*/*.py` |
| P1 | Demo app feedback | Demo watch app buzzes locally when it sends a command. | It does not show whether the Pi received or completed the command. | Optional: have Pi send an acknowledgement packet that the watch displays. Helpful for live demo confidence. | `pi/new-code/watch/demo_app_loader_files/oddsocks_demo.app.js`, `pi/new-code/ble_transport.py`, `pi/new-code/app.py` |

## Stage Implementation Completion

| Stage | Current real behavior | Missing for a convincing demo |
|---|---|---|
| `awake` | Smell on GPIO12, short watch haptic. | Light, Pi haptic, sound are placeholders. Also needs smell cancellation when leaving stage. |
| `light_sleep` | Smell explicitly no-op. | Light, Pi haptic, sound, watch haptic are placeholders. Should probably stop any previous smell task. |
| `deep_sleep` | Smell explicitly no-op. | Light, Pi haptic, sound, watch haptic are placeholders. Should probably stop any previous smell task. |
| `rem` | SPI LEDs, peppermint smell on GPIO16, Pi haptic on GPIO23, watch haptic. | Sound placeholder. Pi haptic needs `demo_fast`. LED cleanup should match test script. |
| `not_worn` | Placeholder only. | Probably okay to ignore for tomorrow unless the regular Dreamstream app may emit it during demo. |
| `unknown` | Placeholder only. | Probably okay to ignore for tomorrow unless the regular Dreamstream app may emit it during demo. |

## Stage File Fill-Out Matrix

Status key:

- `Filled`: has real behavior that should visibly/tactually affect hardware/watch, though it may still need cleanup hardening.
- `Partial`: has real behavior but has a known demo-risk gap.
- `Intentional no-op`: explicitly does nothing for that stage/stimulus.
- `Placeholder`: still scaffold code returning placeholder success.

| Stage | Sound | Smell | Light | Pi motor | Watch haptic |
|---|---|---|---|---|---|
| `awake` | Placeholder: `stages/awake/sound.py` | Partial: `stages/awake/smell.py` starts GPIO12 mist, but carry-over cleanup needs work | Placeholder: `stages/awake/light.py` | Placeholder: `stages/awake/pi_motor.py` | Filled: `stages/awake/watch_haptic.py` sends short watch buzz |
| `light_sleep` | Placeholder: `stages/light_sleep/sound.py` | Intentional no-op: `stages/light_sleep/smell.py`, but should stop previous smell task | Placeholder: `stages/light_sleep/light.py` | Placeholder: `stages/light_sleep/pi_motor.py` | Placeholder: `stages/light_sleep/watch_haptic.py` |
| `deep_sleep` | Placeholder: `stages/deep_sleep/sound.py` | Intentional no-op: `stages/deep_sleep/smell.py`, but should stop previous smell task | Placeholder: `stages/deep_sleep/light.py` | Placeholder: `stages/deep_sleep/pi_motor.py` | Placeholder: `stages/deep_sleep/watch_haptic.py` |
| `rem` | Placeholder: `stages/rem/sound.py` | Partial: `stages/rem/smell.py` starts GPIO16 peppermint mist, but long background behavior needs demo review | Partial: `stages/rem/light.py` uses SPI NeoPixel, but cleanup/preflight should match test script | Partial: `stages/rem/pi_motor.py` drives GPIO23 haptic, but lacks `demo_fast` and safer cleanup | Filled: `stages/rem/watch_haptic.py` supports `demo_fast` watch buzzes |
| `not_worn` | Placeholder: `stages/not_worn/sound.py` | Placeholder: `stages/not_worn/smell.py` | Placeholder: `stages/not_worn/light.py` | Placeholder: `stages/not_worn/pi_motor.py` | Placeholder: `stages/not_worn/watch_haptic.py` |
| `unknown` | Placeholder: `stages/unknown/sound.py` | Placeholder: `stages/unknown/smell.py` | Placeholder: `stages/unknown/light.py` | Placeholder: `stages/unknown/pi_motor.py` | Placeholder: `stages/unknown/watch_haptic.py` |

### Stage File Counts

| Status | Count | Files |
|---|---:|---|
| Filled | 2 | `stages/awake/watch_haptic.py`, `stages/rem/watch_haptic.py` |
| Partial | 4 | `stages/awake/smell.py`, `stages/rem/smell.py`, `stages/rem/light.py`, `stages/rem/pi_motor.py` |
| Intentional no-op | 2 | `stages/light_sleep/smell.py`, `stages/deep_sleep/smell.py` |
| Placeholder | 22 | all remaining stage stimulus files |

## Earlier Discussion Items To Carry Forward

| Priority | Todo | Why it matters | Files |
|---|---|---|---|
| P0 | Implement minimal visible behavior for `light_sleep` and `deep_sleep`. | In the current watch-driven demo, these stages mostly complete silently. A short LED color/pattern or haptic signature would prove the stage logic is firing. | `pi/new-code/stages/light_sleep/*.py`, `pi/new-code/stages/deep_sleep/*.py` |
| P0 | Decide and implement what `sound` means for the demo. | The speaker works in `test_stimuli.py`, but the main app does not play audio in any stage yet. | `pi/new-code/stages/*/sound.py` |
| P0 | Make REM demo quick and deterministic. | REM is currently the richest stage, but it also has the highest risk of over-running because of Pi haptic gaps and long-running smell background behavior. | `pi/new-code/stages/rem/*.py` |
| P0 | Verify watch command bridge is installed with whichever watch app is used. | Pi-to-watch haptics require either `global.dreamstreamCmdBridge` or `global.oddsocksDemoCmdBridge`; if only the app UI is installed without the boot bridge, watch haptics will not fire. | `pi/new-code/watch/app_loader_files/`, `pi/new-code/watch/demo_app_loader_files/`, `pi/new-code/ble_transport.py` |
| P0 | Choose demo watch app vs regular Dreamstream app before presenting. | The demo app is a simple controller and does not run sleep detection; the regular app runs detection and also includes demo controls. The presenter script should match the installed app. | `pi/new-code/watch/README.md`, `pi/new-code/watch/app_loader_files/`, `pi/new-code/watch/demo_app_loader_files/` |
| P0 | Confirm the app is launched with enough privileges for GPIO/SPI. | `test_stimuli.py` is usually run with `sudo`; the systemd service runs as root by default. Running `python main.py` as a normal user may fail on GPIO/SPI depending on Pi permissions. | `pi/new-code/main.py`, `pi/new-code/systemd/sleep-pi-core.service`, stage modules |
| P1 | Add a main-app preflight command or mode. | `test_stimuli.py preflight` checks Bluetooth and ALSA, but the main app has no equivalent startup summary for demo operators. | `pi/new-code/main.py`, `pi/new-code/test_stimuli.py` |
| P1 | Make no-op stages intentionally no-op, not placeholder-success. | Placeholder modules return success, which can make logs look healthier than the demo really is. Better to mark intentionally unused stimuli as `"none"` and unfinished work as failure/skipped. | `pi/new-code/stages/*/*.py` |
| P1 | Add one command-line demo rehearsal path in README. | The team needs one known-good sequence for tomorrow: preflight, step test, start main app, trigger watch demo. | `pi/new-code/README.md`, root README if wanted |
| P2 | Clean generated local artifacts from git consideration. | `sleep_core.db`, WAL/SHM files, `.venv`, `.DS_Store`, and `__pycache__` exist under `pi/new-code`; they should not accidentally become part of demo commits. | `.gitignore`, `pi/new-code/` |

## Found During This Check

| Priority | Finding | Impact | Todo |
|---|---|---|---|
| P0 | Python syntax check passes for main app, BLE, DB, test script, and all stage modules. | Good baseline; no immediate syntax blocker found. | Keep running this after edits. |
| P0 | Many placeholder modules still report `success=True`. | The database/logs may say a stage succeeded even when nothing real happened. | Decide which placeholders are acceptable for demo, then mark the rest as explicit skipped/unfinished or implement them. |
| P0 | `app.py` currently has no per-stimulus timeout. | A hung hardware call can hold a stage indefinitely. | Add per-stimulus timeout around module `run()` calls, especially for demo mode. |
| P1 | `demo_stop` exists in parser, but demo watch app `STOP` sends `cmd:"stop"`. | It stops the whole session, which may be okay, but it is different from just cancelling the scripted demo. | Decide whether the red watch button should stop only the demo script or the whole session. |
| P1 | `test_stimuli.py` has the most reliable hardware cleanup code, but it is not shared. | Fixes may diverge as wiring changes. | Extract shared hardware helpers only if there is time; otherwise copy the safest pieces into the stage modules. |

## Suggested Before-Demo Order

- [ ] P0: Add `demo_fast` short path to `rem/pi_motor.py`.
- [ ] P0: Add smell stop/cleanup for `light_sleep` and `deep_sleep`.
- [ ] P0: Implement a minimal speaker/sound helper using USB DAC auto-detection.
- [ ] P0: Add safe speaker volume handling before sound playback.
- [ ] P0: Make `app.py` stage execution tolerate one stimulus failing.
- [ ] P0: Add a per-stimulus timeout in `app.py`, at least for `demo_fast` stage runs.
- [ ] P0: Make manual `SEND <stage>` from the watch either auto-start or visibly require an active session.
- [ ] P0: Give `light_sleep` and `deep_sleep` at least one visible/tactile demo cue.
- [ ] P0: Confirm the watch app and its command bridge are both installed.
- [ ] P0: Run `sudo python3 pi/new-code/test_stimuli.py preflight` on the Pi.
- [ ] P0: Run `sudo python3 pi/new-code/test_stimuli.py all --step` on the Pi.
- [ ] P0: Run the actual app and trigger `RUN DEMO` from the watch.
- [ ] P1: Port LED explicit cleanup/deinit into `rem/light.py`.
- [ ] P1: Port safer GPIO cleanup into `rem/pi_motor.py`.
- [ ] P1: Centralize hardware constants.
- [ ] P1: Add a concise demo rehearsal command sequence to `pi/new-code/README.md`.
- [ ] P1: Decide whether watch `STOP` should cancel demo only or stop the whole session.
- [ ] P2: Implement or intentionally remove placeholders for `unknown` and `not_worn`.
