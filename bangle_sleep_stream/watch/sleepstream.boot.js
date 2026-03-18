// File summary:
// Background boot service for Bangle.js 2 that:
// - computes sleep and consecutive state on each health recheck
// - exposes a custom BLE GATT service for state streaming
// - sends one notify payload per processed recheck
// - auto-recovers advertising/listeners across disconnects and reloads

(function() {
  var lib = require("sleepstream.js");
  var STATUS = lib.STATUS;
  var CONSECUTIVE = lib.CONSECUTIVE;

  var SERVICE_UUID = "12345678-1234-5678-1234-56789abc0000";
  var UPDATE_CHAR_UUID = "12345678-1234-5678-1234-56789abc0001";
  var RUNTIME_FILE = "sleepstream.runtime.json";

  var conf = lib.loadSettings();
  if (!conf.enabled) {
    delete global.sleepstream;
    return;
  }

  function to10MinStep(ms) {
    return ((ms / 6E5) | 0) * 6E5;
  }

  global.sleepstream = {
    conf: conf,
    status: STATUS.UNKNOWN,
    consecutive: CONSECUTIVE.UNKNOWN,
    sequence: 0,
    connected: false,
    info: {
      lastCheck: 0,
      lastChange: 0,
      asleepSince: 0,
      awakeSince: 0
    },
    lastPayload: lib.packUpdate({
      status: STATUS.UNKNOWN,
      consecutive: CONSECUTIVE.UNKNOWN,
      sourceMode: 0,
      sequence: 0,
      timestampSec: (Date.now() / 1000) | 0,
      movement: 0xFFFF,
      bpm: 0xFFFF
    }),

    logEvent: function(kind, message, detail) {
      if (!this.conf.eventLogEnabled) return;
      var now = Date.now();
      var row = [now, kind || "info", message || "", detail || ""].join("|") + "\n";
      require("Storage").open("sleepstream.events.log", "a").write(row);
    },

    logMeasurement: function(data, sourceMode, changed, prevStatus, prevConsecutive) {
      if (!this.conf.measurementLogEnabled) return;

      var file = require("Storage").open("sleepstream.measure.csv", "a");
      if (!file.getLength()) {
        file.write(
          "processed_at_ms,sample_ts_ms,movement,bpm,source_mode,charging,temp_c,status,consecutive," +
          "changed,prev_status,prev_consecutive,asleep_since_ms,awake_since_ms,next_sequence,connected\n"
        );
      }

      var movement = data.movement;
      if (movement === undefined) movement = "";
      var bpm = data.bpm;
      if (bpm === undefined) bpm = "";

      var row = [
        Date.now(),
        data.timestamp || "",
        movement,
        bpm,
        sourceMode,
        Bangle.isCharging() ? 1 : 0,
        E.getTemperature(),
        data.status,
        data.consecutive,
        changed ? 1 : 0,
        prevStatus,
        prevConsecutive,
        this.info.asleepSince || 0,
        this.info.awakeSince || 0,
        (this.sequence + 1) >>> 0,
        this.connected ? 1 : 0
      ].join(",") + "\n";

      file.write(row);
    },

    initBle: function() {
      var service = {};
      service[SERVICE_UUID] = {};
      service[SERVICE_UUID][UPDATE_CHAR_UUID] = {
        readable: true,
        notify: true,
        value: this.lastPayload
      };

      NRF.setServices(service, {
        uart: false
      });

      this.startAdvertising();
    },

    startAdvertising: function() {
      if (!this.conf.advertiseWhenDisconnected) return;
      try {
        // Keep advertising payload minimal to avoid DATA_SIZE errors.
        NRF.setAdvertising([SERVICE_UUID], {
          discoverable: true,
          connectable: true,
          interval: 375
        });
        this.logEvent("ble", "advertising_started", "service_uuid_only");
      } catch (e) {
        // Last-resort fallback for platform-specific BLE stack quirks.
        this.logEvent("warn", "advertising_primary_failed", String(e));
        try {
          NRF.setAdvertising({}, {
            discoverable: true,
            connectable: true,
            interval: 375
          });
          this.logEvent("ble", "advertising_started", "fallback_empty_payload");
        } catch (e2) {
          this.logEvent("error", "advertising_failed", String(e2));
        }
      }
    },

    onConnect: function() {
      global.sleepstream.connected = true;
      global.sleepstream.logEvent("ble", "connected", "central_connected");
    },

    onDisconnect: function() {
      global.sleepstream.connected = false;
      global.sleepstream.logEvent("ble", "disconnected", "central_disconnected");
      setTimeout(function() {
        if (global.sleepstream) global.sleepstream.startAdvertising();
      }, 300);
    },

    start: function() {
      this.restoreRuntimeState();
      this.logEvent("service", "start", "initializing");
      this.initBle();
      E.on("kill", this.saveRuntimeState);
      NRF.on("connect", this.onConnect);
      NRF.on("disconnect", this.onDisconnect);
      Bangle.prependListener("health", this.health);
      this.logEvent("service", "start_complete", "health_listener_attached");
    },

    stop: function() {
      Bangle.removeListener("health", this.health);
      NRF.removeListener("connect", this.onConnect);
      NRF.removeListener("disconnect", this.onDisconnect);
      E.removeListener("kill", this.saveRuntimeState);
      this.logEvent("service", "stop", "listeners_removed");
    },

    saveRuntimeState: function() {
      if (!global.sleepstream) return;
      require("Storage").writeJSON(RUNTIME_FILE, {
        status: global.sleepstream.status,
        consecutive: global.sleepstream.consecutive,
        sequence: global.sleepstream.sequence,
        info: global.sleepstream.info
      });
      global.sleepstream.logEvent("service", "runtime_saved", "kill_or_manual_save");
    },

    restoreRuntimeState: function() {
      var saved = require("Storage").readJSON(RUNTIME_FILE, true) || {};
      if (typeof saved.status === "number") this.status = saved.status | 0;
      if (typeof saved.consecutive === "number") this.consecutive = saved.consecutive | 0;
      if (typeof saved.sequence === "number") this.sequence = saved.sequence >>> 0;

      if (saved.info && typeof saved.info === "object") {
        this.info.lastCheck = saved.info.lastCheck | 0;
        this.info.lastChange = saved.info.lastChange | 0;
        this.info.asleepSince = saved.info.asleepSince | 0;
        this.info.awakeSince = saved.info.awakeSince | 0;
      }

      this.lastPayload = lib.packUpdate({
        status: this.status,
        consecutive: this.consecutive,
        sourceMode: 0,
        sequence: this.sequence,
        timestampSec: ((this.info.lastCheck || Date.now()) / 1000) | 0,
        movement: 0xFFFF,
        bpm: 0xFFFF
      });

      this.logEvent("service", "runtime_restored", "seq=" + this.sequence);
    },

    classifyStatus: function(data, sourceMode) {
      if (Bangle.isCharging()) return STATUS.NOT_WORN;
      if (sourceMode === 1) {
        return data.bpm <= this.conf.hrmDeepTh ? STATUS.DEEP_SLEEP :
          data.bpm <= this.conf.hrmLightTh ? STATUS.LIGHT_SLEEP : STATUS.AWAKE;
      }
      return data.movement <= this.conf.deepTh ? STATUS.DEEP_SLEEP :
        data.movement <= this.conf.lightTh ? STATUS.LIGHT_SLEEP : STATUS.AWAKE;
    },

    health: function(data) {
      if (!global.sleepstream) return;
      if (!data || (data.movement === undefined && data.bpm === undefined)) return;

      data.timestamp = data.timestamp || to10MinStep(Date.now() - 6E5);
      var sourceMode = (global.sleepstream.conf.preferHRM && data.bpm) ? 1 : 0;
      data.status = global.sleepstream.classifyStatus(data, sourceMode);

      if (data.status === STATUS.DEEP_SLEEP && global.sleepstream.status <= STATUS.AWAKE) {
        global.sleepstream.checkIsWearing(function(isWearing, corrected) {
          if (!isWearing) corrected.status = STATUS.NOT_WORN;
          var changed = global.sleepstream.applyState(corrected);
          global.sleepstream.logMeasurement(
            corrected,
            sourceMode,
            changed,
            corrected.prevStatus,
            corrected.prevConsecutive
          );
          global.sleepstream.sendUpdate(corrected, sourceMode);
        }, data);
        return;
      }

      var changed = global.sleepstream.applyState(data);
      global.sleepstream.logMeasurement(
        data,
        sourceMode,
        changed,
        data.prevStatus,
        data.prevConsecutive
      );
      global.sleepstream.sendUpdate(data, sourceMode);
    },

    checkIsWearing: function(returnFn, data) {
      if (this.conf.wearTemp !== 19.5) {
        return returnFn(!Bangle.isCharging() && E.getTemperature() >= this.conf.wearTemp, data);
      }

      var tmp = {
        isWearing: false,
        listener: function(hrm) { tmp.isWearing = !!hrm.isWearing; }
      };

      Bangle.setHRMPower(true, "sleepstream-wearing");
      setTimeout(function() {
        Bangle.on("HRM-raw", tmp.listener);
        setTimeout(function() {
          Bangle.removeListener("HRM-raw", tmp.listener);
          Bangle.setHRMPower(false, "sleepstream-wearing");
          returnFn(tmp.isWearing, data);
        }, 34);
      }, 2500);
    },

    applyState: function(data) {
      data.prevStatus = this.status;
      data.prevConsecutive = this.consecutive;
      this.info.lastCheck = data.timestamp;

      if (data.status === STATUS.LIGHT_SLEEP && this.status !== STATUS.DEEP_SLEEP && !this.info.asleepSince) {
        data.status = STATUS.AWAKE;
      }

      data.consecutive = this.consecutive;

      if (data.status === STATUS.DEEP_SLEEP && this.status <= STATUS.AWAKE) {
        this.info.asleepSince = this.info.asleepSince || data.timestamp;
        data.consecutive = CONSECUTIVE.UNKNOWN;
      } else if (data.status === STATUS.AWAKE && this.status > STATUS.AWAKE) {
        this.info.awakeSince = this.info.awakeSince || data.timestamp;
        data.consecutive = CONSECUTIVE.UNKNOWN;
      }

      if (data.status === STATUS.NOT_WORN) this.consecutive = CONSECUTIVE.NO;

      if (!this.consecutive) {
        if (data.status === STATUS.DEEP_SLEEP && this.info.asleepSince &&
          this.info.asleepSince + this.conf.minConsec <= data.timestamp) {
          data.consecutive = CONSECUTIVE.YES;
          this.info.awakeSince = 0;
        } else if (data.status <= STATUS.AWAKE && this.info.awakeSince &&
          this.info.awakeSince + this.conf.maxAwake <= data.timestamp) {
          data.consecutive = CONSECUTIVE.NO;
          this.info.asleepSince = 0;
        }
      }

      var changed = data.status !== this.status || data.consecutive !== this.consecutive;
      if (changed) {
        this.status = data.status;
        this.consecutive = data.consecutive;
        this.info.lastChange = data.timestamp;
        this.appendStatus(data.timestamp, data.status, data.consecutive);
      }

      return changed;
    },

    appendStatus: function(timestamp, status, consecutive) {
      var line = [((timestamp / 6E5) | 0), status | 0, consecutive | 0].join(",") + "\n";
      require("Storage").open("sleepstream.log", "a").write(line);
    },

    sendUpdate: function(data, sourceMode) {
      this.sequence += 1;
      this.lastPayload = lib.packUpdate({
        status: data.status,
        consecutive: data.consecutive,
        sourceMode: sourceMode,
        sequence: this.sequence,
        timestampSec: (data.timestamp / 1000) | 0,
        movement: data.movement,
        bpm: data.bpm
      });

      // Also publish a JSON line over UART-compatible BLE for environments
      // where only Nordic UART service is visible to centrals.
      try {
        Bluetooth.println(JSON.stringify({
          t: "sleepstream",
          v: 1,
          seq: this.sequence,
          ts: (data.timestamp / 1000) | 0,
          status: data.status,
          consecutive: data.consecutive,
          source_mode: sourceMode,
          movement: data.movement === undefined ? null : data.movement,
          bpm: data.bpm === undefined ? null : data.bpm
        }));
      } catch (e0) {
        this.logEvent("warn", "uart_json_send_failed", String(e0));
      }

      var update = {};
      update[SERVICE_UUID] = {};
      update[SERVICE_UUID][UPDATE_CHAR_UUID] = { value: this.lastPayload };

      try {
        NRF.updateServices(update);
      } catch (e) {
        // Keep best-effort semantics: we do not queue or throw on notify failure.
        this.logEvent("warn", "notify_failed", String(e));
      }

      // Persist after each update so sequence remains monotonic even if the
      // service is reloaded without a full power-cycle.
      require("Storage").writeJSON(RUNTIME_FILE, {
        status: this.status,
        consecutive: this.consecutive,
        sequence: this.sequence,
        info: this.info
      });
    }
  };

  global.sleepstream.start();
})();
