# OddSocks Demo Control Manifest

Purpose: a small demo-only Bangle.js 2 controller for the Pi demo flow.

This is not the regular Dreamstream app. It does not include sleep detection, telemetry, epoch logs, settings, or classifier code.

Identity:

- App id: `oddsocks_demo`
- App name: `OddSocks Demo Control`
- Short name: `Demo`
- Command source: `oddsocks_demo`
- Command bridge: `global.oddsocksDemoCmdBridge`

Files:

- `metadata.json`: Bangle App Loader metadata.
- `oddsocks_demo.app.js`: Touch UI for demo commands.
- `oddsocks_demo.cmd.boot.js`: Minimal haptic command bridge for Pi-triggered watch buzzes.

Dependencies:

- External app dependencies: none.
- Built-in platform APIs used: `Bangle`, `Bluetooth`, `Date`, and graphics globals.
