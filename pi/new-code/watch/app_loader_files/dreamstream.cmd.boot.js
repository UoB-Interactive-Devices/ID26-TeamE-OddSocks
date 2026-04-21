// Command inbox companion for Dreamstream.
// Keeps Pi->watch command handling separate from sleep detection logic.

(function () {
  var Storage = require("Storage");
  var STORE_FILE = "dreamstream.cmd.json";

  function clamp(v, lo, hi) {
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
  }

  function toInt(v) {
    if (typeof v === "number" && isFinite(v)) return v | 0;
    return 0;
  }

  function remember(payload) {
    var rec = {
      ts: Date.now(),
      payload: payload
    };
    global.dreamstreamLastCmd = rec;
    if (global.sleepstream) global.sleepstream.lastCommand = rec;
    try {
      Storage.writeJSON(STORE_FILE, rec);
    } catch (e) {
    }
  }

  function buzzFrom(payload) {
    var ms = 120;
    if (payload && typeof payload === "object") {
      if (payload.haptic && typeof payload.haptic === "object") {
        ms = toInt(payload.haptic.ms || payload.haptic.duration || ms);
      }
      ms = toInt(payload.ms || payload.duration || payload.buzz || ms) || ms;
    }
    ms = clamp(ms, 20, 2000);
    Bangle.buzz(ms);
  }

  function handlePacket(payload) {
    if (!payload || typeof payload !== "object") return;
    remember(payload);

    var cmd = (payload.cmd || payload.command || "").toString().toLowerCase();
    if (cmd === "buzz" || cmd === "haptic" || payload.haptic || payload.buzz) {
      buzzFrom(payload);
    }
  }

  var state = global.dreamstreamCmdBridge || {};
  if (state.listener) Bluetooth.removeListener("data", state.listener);
  state.buffer = "";

  state.listener = function (chunk) {
    state.buffer += chunk;

    var idx = state.buffer.indexOf("\n");
    while (idx >= 0) {
      var line = state.buffer.slice(0, idx).trim();
      state.buffer = state.buffer.slice(idx + 1);
      if (line) {
        try {
          handlePacket(JSON.parse(line));
        } catch (e) {
        }
      }
      idx = state.buffer.indexOf("\n");
    }

    if (state.buffer.length > 1024) {
      state.buffer = state.buffer.slice(-512);
    }
  };

  global.dreamstreamCmdBridge = state;
  Bluetooth.on("data", state.listener);
})();
