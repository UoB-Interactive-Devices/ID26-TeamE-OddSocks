# watch directory overview

## Purpose

Bangle.js 2 runtime files for sleep-state detection and BLE publishing.

## Files and fit

- sleepstream.boot.js: Background service started at boot. Owns state machine, BLE service, health listeners.
- sleepstream.lib.js: Shared helper functions for settings and payload packing.
- sleepstream.settings.js: On-watch settings menu for thresholds and BLE behavior.
- sleepstream.app.js: Interactive debug screen with live runtime, packet decode, config snapshot, and log tail views.
- metadata.json: App metadata for packaging/loader integration.

## Control flow

1. boot script loads settings and initializes BLE service.
2. health listener runs every recheck and updates sleep/consecutive state.
3. service encodes the latest state and sends notify to connected central.
4. service tracks connection events and remains reconnect-friendly.

## Data flow

Inputs: health movement/bpm, charging state, temperature/HRM wear checks, settings JSON.
Outputs: BLE notifications, optional local status persistence.
