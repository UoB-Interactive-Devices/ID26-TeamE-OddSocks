# bangle_sleep_stream

## Directory overview

This directory contains a production implementation of the Bangle.js 2 sleep-state sender and a Linux Bleak receiver.

- watch: Bangle.js 2 code that runs sleep detection and publishes BLE updates at each health recheck.
- protocol: Wire-level message format and compatibility/version notes.
- receiver: Python daemon that connects, subscribes, reconnects automatically, and persists updates.
- docs: Deployment and operational runbooks.

## End-to-end flow

1. Bangle.js health event fires (nominally every 10 minutes).
2. Watch classifies sleep state using movement/HRM thresholds and consecutive logic.
3. Watch publishes a BLE notification with a compact, versioned payload.
4. Receiver daemon subscribes, decodes payload, logs it, and stores it in SQLite.
5. On disconnect, receiver reconnects automatically and resumes subscription.

## Reliability model

- Sleep inference is on-watch.
- Transport is best-effort live streaming (no persistent resend queue on watch).
- Receiver is designed for unattended operation with restart and reconnect loops.
