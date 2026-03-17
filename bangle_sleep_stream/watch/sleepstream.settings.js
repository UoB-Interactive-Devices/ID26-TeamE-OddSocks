// File summary:
// On-watch settings menu for sleepstream.
// This file edits thresholds and runtime behavior persisted in sleepstream.json.
// It can be launched manually or from an app menu and writes values used by sleepstream.boot.js.

(function(back) {
  var lib = require("sleepstream");
  var settings = lib.loadSettings();

  function save() {
    lib.saveSettings(settings);
  }

  function show() {
    E.showMenu({
      "": { title: "Sleep Stream", back: back || load },
      "Enabled": {
        value: !!settings.enabled,
        onchange: function(v) { settings.enabled = v; save(); }
      },
      "Prefer HRM": {
        value: !!settings.preferHRM,
        onchange: function(v) { settings.preferHRM = v; save(); }
      },
      "Deep Th": {
        value: settings.deepTh | 0,
        min: 20, max: 400, step: 5,
        onchange: function(v) { settings.deepTh = v | 0; save(); }
      },
      "Light Th": {
        value: settings.lightTh | 0,
        min: 50, max: 600, step: 5,
        onchange: function(v) { settings.lightTh = v | 0; save(); }
      },
      "HRM Deep": {
        value: settings.hrmDeepTh | 0,
        min: 35, max: 100, step: 1,
        onchange: function(v) { settings.hrmDeepTh = v | 0; save(); }
      },
      "HRM Light": {
        value: settings.hrmLightTh | 0,
        min: 40, max: 120, step: 1,
        onchange: function(v) { settings.hrmLightTh = v | 0; save(); }
      },
      "Wear Temp": {
        value: Math.round(settings.wearTemp * 2),
        min: 20, max: 90, step: 1,
        format: function(v) { return (v / 2).toFixed(1) + "C"; },
        onchange: function(v) { settings.wearTemp = v / 2; save(); }
      },
      "Max Awake": {
        value: (settings.maxAwake / 6E4) | 0,
        min: 10, max: 180, step: 10,
        format: function(v) { return v + "m"; },
        onchange: function(v) { settings.maxAwake = v * 6E4; save(); }
      },
      "Min Consec": {
        value: (settings.minConsec / 6E4) | 0,
        min: 10, max: 120, step: 10,
        format: function(v) { return v + "m"; },
        onchange: function(v) { settings.minConsec = v * 6E4; save(); }
      }
    });
  }

  show();
})
