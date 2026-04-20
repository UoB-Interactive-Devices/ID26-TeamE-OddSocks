# Dreamstream Watch Package

This folder contains the Dreamstream watch files for Bangle.js 2.

## Files

- `dreamstream.js`: Sleep feature extraction and classifier module copied from legacy source.
- `dreamstream.boot.js`: Background sleep service copied from legacy source, with minimal non-detection integration edits.
- `dreamstream.app.js`: One-screen operational app UI (Start/Stop, live metrics, command diagnostics).
- `dreamstream.cmd.boot.js`: Pi command inbox and basic haptic command handling.
- `dreamstream.info`: App metadata.

## Upload to watch

Upload all files in this folder to the watch storage.

## Protocol

Telemetry tag sent by the boot service is `t:"dreamstream"`.
Control packets sent by the app use `{"cmd":"start"}` and `{"cmd":"stop"}`.

## Scientific parity note

Sleep-state detection logic in `dreamstream.js` is kept unchanged from legacy classifier code.
