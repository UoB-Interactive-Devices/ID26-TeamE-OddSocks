# Deployment guide

## Summary

Install watch files on Bangle.js 2, then run the Python receiver on Raspberry Pi as a systemd service.

## Watch deployment

1. Copy files in watch directory into an App Loader package or install manually:
   - sleepstream.boot.js
   - sleepstream.lib.js
   - sleepstream.settings.js
   - metadata.json
2. Ensure the service is enabled in sleepstream settings.

## Receiver deployment

1. Create Python environment and install receiver requirements.
2. Configure the receiver name prefix to match watch advertise name.
3. Install systemd service from receiver/systemd/sleepstream-receiver.service.
4. Enable and start service:
   - sudo systemctl daemon-reload
   - sudo systemctl enable sleepstream-receiver
   - sudo systemctl start sleepstream-receiver

## Validation

- Verify BLE connection logs show subscribe success.
- Verify SQLite receives rows every watch recheck period.
