# Troubleshooting guide

## Summary

Common operational issues and quick recovery actions for watch sender and receiver daemon.

## No packets arriving

- Confirm watch is advertising expected name prefix.
- Confirm receiver config uses matching prefix.
- Check receiver logs for scan timeout and reconnect backoff.

## Repeated disconnects

- Reduce BLE interference and keep devices within range.
- Restart receiver service and verify notifications resume.
- Reboot watch if BLE stack appears stuck.

## Database not updating

- Check file permissions on SQLite path.
- Confirm service user can write to receiver directory.
- Inspect logs for sqlite OperationalError messages.
