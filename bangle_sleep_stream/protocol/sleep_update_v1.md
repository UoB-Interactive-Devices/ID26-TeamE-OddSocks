# sleep_update_v1

## Summary

This document defines the version 1 binary payload sent from the watch to the Python receiver.

## Transport

- BLE notify characteristic value.
- Fixed length: 16 bytes.
- Little-endian for multi-byte integers.

## Layout

- byte 0: protocol version (u8), fixed value 1.
- byte 1: status (u8): 0 unknown, 1 not_worn, 2 awake, 3 light_sleep, 4 deep_sleep.
- byte 2: consecutive (u8): 0 unknown, 1 non_consecutive, 2 consecutive.
- byte 3: source mode (u8): 0 movement, 1 hrm.
- bytes 4-7: sequence (u32), incremented on each sent recheck.
- bytes 8-11: watch timestamp seconds UTC (u32).
- bytes 12-13: movement (u16), 0xFFFF means unavailable.
- bytes 14-15: bpm (u16), 0xFFFF means unavailable.

## Characteristic behavior

- Watch notifies once per processed health recheck.
- Characteristic is also readable and returns latest payload snapshot.
- Receiver should handle duplicates, out-of-order delivery, and sequence gaps.

## Compatibility rules

- Receiver must reject unsupported version values.
- Future versions can extend payload by adding a new characteristic UUID or versioned decoder.
