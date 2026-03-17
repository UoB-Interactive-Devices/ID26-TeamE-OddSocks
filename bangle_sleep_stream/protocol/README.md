# protocol directory overview

## Purpose

Defines the BLE payload contract used between watch and receiver.

## Files and fit

- sleep_update_v1.md: Binary payload layout, field semantics, and compatibility rules.

## Control and data flow

- Producer: watch/sleepstream.boot.js emits payloads that conform to this contract.
- Consumer: receiver/sleep_receiver.py decodes and validates payloads with this contract.
- Versioning: payload includes a version byte so future revisions can remain backward-compatible.
