# receiver directory overview

## Purpose

Linux Python receiver daemon for automatic BLE ingest from Bangle.js 2.

## Files and fit

- sleep_receiver.py: Main daemon, BLE lifecycle management, decoding, persistence.
- requirements.txt: Python dependencies.
- systemd/sleepstream-receiver.service: Service unit for boot-time start and restart policy.

## Control flow

1. daemon scans for configured watch name.
2. connects and subscribes to notify characteristic.
3. decodes each update, logs structured output, persists to SQLite.
4. on disconnect/error, backoff and reconnect loop runs continuously.

## Data flow

Input: BLE notify packets from watch.
Output: console logs + SQLite records for audit/analysis.
