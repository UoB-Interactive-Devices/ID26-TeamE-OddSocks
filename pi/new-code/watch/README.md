# Watch Apps

This folder keeps the two Bangle.js 2 apps separate:

- `app_loader_files/` is the regular Dreamstream watch app from the main branch.
- `demo_app_loader_files/` is the small OddSocks demo control app.

The demo app is intentionally just a controller. It sends start, stop, scripted demo, and manual stage commands to the Pi. It does not include the Dreamstream classifier, background telemetry service, epoch logging, or regular-use storage files.

## Regular App

Use `app_loader_files/metadata.json` when you want the normal Dreamstream sleep tracking app.

## Demo Control App

Use `demo_app_loader_files/metadata.json` when you want the demo-only controller.

Demo commands sent to the Pi:

- `{"cmd":"start","src":"oddsocks_demo"}`
- `{"cmd":"stop","src":"oddsocks_demo"}`
- `{"cmd":"demo_run","stages":["awake","light_sleep","deep_sleep","rem"],"dwell_sec":0.35,"cycles":1,"auto_start":true,"src":"oddsocks_demo"}`
- `{"cmd":"stage","stage":"rem","demo_fast":true,"src":"oddsocks_demo"}`

The demo package also includes a tiny command bridge so Pi-triggered watch haptics still work during demos.
