# bangle_sleep_stream

## Project context

This project turns Bangle.js 2 sleep inference into a live BLE telemetry stream that a nearby computer can ingest continuously.

It was built from the existing sleeplog algorithm and adapted into a two-part system:

- Watch side: infer sleep state on-device from health data and publish updates.
- Receiver side: keep a persistent BLE connection, decode updates, and persist them.

The current deployment target is an always-on receiver (Linux preferred for production), with active testing done on macOS.

## Problem this solves

The original sleeplog logic is valuable, but it lives on-watch. This project makes those state transitions observable off-watch in real time so downstream systems can consume them without pulling full logs manually.

Goals:

1. Keep sleep inference close to sensors (on-watch) for consistency and lower host complexity.
2. Stream compact state updates over BLE with no manual reconnect steps.
3. Persist received updates in a queryable local database.
4. Provide enough diagnostics to debug failures in the field.

## High-level architecture

### 1) Watch runtime

Directory: watch

Responsibilities:

- Load settings and initialize runtime state.
- Listen for Bangle health events.
- Classify sleep status and consecutive status.
- Publish updates over BLE.
- Keep local logs for debugging and audit.

Key files:

- sleepstream.boot.js: background service and state machine.
- sleepstream.js: shared constants/settings/payload packing.
- sleepstream.settings.js: on-watch settings menu.
- sleepstream.app.js: debug UI and self-test controls.

### 2) Protocol definition

Directory: protocol

Responsibilities:

- Define canonical packet format and versioning.
- Keep receiver/watch encoding aligned.

Key file:

- sleep_update_v1.md: binary packet layout and semantics.

### 3) Receiver daemon

Directory: receiver

Responsibilities:

- Scan and connect to watch.
- Subscribe to notifications.
- Decode updates and log structured events.
- Persist rows in SQLite.
- Reconnect on disconnect/error with backoff.

Key file:

- sleep_receiver.py: full BLE lifecycle, decoding, persistence.

## Data flow (end-to-end)

1. Watch health event arrives (nominally every 10 minutes).
2. Service computes source mode (movement or HRM when configured and available).
3. Service computes status and consecutive state.
4. Service publishes:
	- custom characteristic packet (preferred path), and
	- UART JSON fallback packet (compatibility path).
5. Receiver consumes whichever notify path is available.
6. Receiver stores packet fields in sleep_updates table.

## Why these architecture decisions were made

### On-watch inference (not host-side inference)

Reason:

- The watch has direct access to health cadence, charging state, temperature, and optional HRM checks used by the original logic.
- Re-implementing inference host-side would duplicate logic and introduce drift.

Tradeoff:

- Host gets classified state, not raw high-rate sensor streams.

### Best-effort live transport

Reason:

- Simpler and lower-risk for an embedded watch runtime.
- Avoids queue management and flash wear from guaranteed delivery buffering.

Tradeoff:

- No resend of missed packets after disconnect.

### Dual transport path (custom GATT + UART fallback)

Reason:

- In some environments only Nordic UART is visible even when custom service is configured.
- Fallback keeps the pipeline working across BLE stack differences.

Tradeoff:

- Receiver complexity increases due to dual decoding paths.

### Receiver auto-reconnect loop

Reason:

- Intended unattended operation.
- BLE links can drop; recovery must be automatic.

Tradeoff:

- More state handling in daemon lifecycle.

## Current validated behavior

From real run output (macOS test):

- Scan and connect succeed.
- Custom characteristic not found in active GATT map.
- Receiver falls back to UART notify.
- Receiver successfully ingests non-manual packet:
  - uart-notify: seq=1 status=2 consecutive=0 source=0 ts=1773846600 bpm=56 movement=595

Interpretation:

- End-to-end path is operational with real watch-generated updates.
- At least one natural health-cycle packet has been observed.

## What works

1. Watch service startup, classification, and packet emission.
2. Debug app rendering, self-test controls, and log views.
3. Receiver scan/connect/reconnect lifecycle.
4. UART fallback subscription and decoding.
5. SQLite persistence with sequence-gap warning behavior.
6. Structured logging for BLE and packet diagnostics.

## What does not work or is intentionally limited

1. Guaranteed delivery is not implemented.
	- If disconnected at send time, packets are not queued and replayed.

2. Manual forcing of a new official health-cycle movement sample is not available.
	- Real movement values come on firmware health cadence.

3. Custom GATT characteristic discovery is not currently reliable in this test environment.
	- System currently relies on UART fallback path.

4. Measurement fields can appear static between natural health events.
	- Self-test can resend latest known values while sequence increments.

5. Single-central BLE reality still applies.
	- Competing tools (IDE/AppLoader/other clients) can disrupt connection.

## Operational expectations

1. Keep receiver running continuously.
2. Expect packets roughly every 10 minutes from natural health cadence.
3. First packet after connect can arrive sooner or later depending on current point in health interval.
4. If no packet after ~12-15 minutes, inspect connection/subscription logs first.

## Repository structure

- watch
  - Runtime service, settings, and debug UI.
- protocol
  - Message format contract.
- receiver
  - Python BLE daemon and persistence.
- docs
  - Deployment and troubleshooting procedures.

## Success criteria for this phase

This phase is successful when:

1. Receiver stays connected unattended.
2. Natural watch packets continue to arrive over time.
3. Packets are persisted with increasing sequence values.
4. System recovers automatically after transient BLE disconnects.

## Next hardening steps

1. Verify multi-interval stability (several consecutive natural packets).
2. Optionally add startup heartbeat packet on connect for quicker liveness confirmation.
3. Optionally expose receiver health metrics (last packet age, reconnect count).
4. Revisit custom GATT visibility issue to reduce dependence on fallback path.
