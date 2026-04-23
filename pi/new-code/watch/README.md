# Dreamstream Watch Package

This folder contains the Dreamstream watch files for Bangle.js 2.

## Files

- `dreamstream.js`: Sleep feature extraction and classifier module copied from legacy source.
- `dreamstream.boot.js`: Background sleep service copied from legacy source, with minimal non-detection integration edits.
- `dreamstream.app.js`: One-screen operational/control app UI (Start/Stop, fast demo trigger, stage selector + manual stage fire via button).
- `dreamstream.cmd.boot.js`: Pi command inbox and basic haptic command handling.
- `dreamstream.info`: App metadata.

## Upload to watch

Upload all files in this folder to the watch storage.

## Protocol

Telemetry tag sent by the boot service is `t:"dreamstream"`.
Control packets sent by the app use `{"cmd":"start"}` and `{"cmd":"stop"}`.
Demo/control packets include:

- `{"cmd":"demo_run","stages":[...],"dwell_sec":0.35,"cycles":1}`
- `{"cmd":"stage","stage":"rem","demo_fast":true}`

## Scientific parity note

Sleep-state detection logic in `dreamstream.js` is kept unchanged from legacy classifier code.
