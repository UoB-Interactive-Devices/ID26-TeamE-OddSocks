// Background boot service for Bangle.js 2.
// Computes sleep state on each health event and streams updates over BLE UART.
// Sleep logic consistent with the original sleeplog app.

(function () {
  var lib = require("sleepstream.js");
  var STATUS = lib.STATUS;
  var CONSECUTIVE = lib.CONSECUTIVE;
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

    onConnect: function () {
      global.sleepstream.connected = true;
    },

    onDisconnect: function () {
      global.sleepstream.connected = false;
    },

    start: function () {
      this.restoreRuntimeState();
      NRF.on("connect", this.onConnect);
      NRF.on("disconnect", this.onDisconnect);
      E.on("kill", this.saveRuntimeState);
      Bangle.prependListener("health", this.health);
    },

    stop: function () {
      Bangle.removeListener("health", this.health);
      NRF.removeListener("connect", this.onConnect);
      NRF.removeListener("disconnect", this.onDisconnect);
      E.removeListener("kill", this.saveRuntimeState);
    },

    saveRuntimeState: function () {
      if (!global.sleepstream) return;
      require("Storage").writeJSON(RUNTIME_FILE, {
        status: global.sleepstream.status,
        consecutive: global.sleepstream.consecutive,
        sequence: global.sleepstream.sequence,
        info: global.sleepstream.info
      });
    },

    restoreRuntimeState: function () {
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
    },

    classifyStatus: function (data, sourceMode) {
      if (Bangle.isCharging()) return STATUS.NOT_WORN;
      if (sourceMode === 1) {
        return data.bpm <= this.conf.hrmDeepTh ? STATUS.DEEP_SLEEP :
          data.bpm <= this.conf.hrmLightTh ? STATUS.LIGHT_SLEEP : STATUS.AWAKE;
      }
      return data.movement <= this.conf.deepTh ? STATUS.DEEP_SLEEP :
        data.movement <= this.conf.lightTh ? STATUS.LIGHT_SLEEP : STATUS.AWAKE;
    },

    health: function (data) {
      if (!global.sleepstream) return;
      if (!data || (data.movement === undefined && data.bpm === undefined)) return;

      data.timestamp = data.timestamp || to10MinStep(Date.now() - 6E5);
      var sourceMode = (global.sleepstream.conf.preferHRM && data.bpm) ? 1 : 0;
      data.status = global.sleepstream.classifyStatus(data, sourceMode);

      // When transitioning to deep sleep from non-sleeping, verify wearing status
      if (data.status === STATUS.DEEP_SLEEP && global.sleepstream.status <= STATUS.AWAKE) {
        global.sleepstream.checkIsWearing(function (isWearing, corrected) {
          if (!isWearing) corrected.status = STATUS.NOT_WORN;
          global.sleepstream.applyState(corrected);
          global.sleepstream.sendUpdate(corrected, sourceMode);
        }, data);
        return;
      }

      global.sleepstream.applyState(data);
      global.sleepstream.sendUpdate(data, sourceMode);
    },

    // Wear detection consistent with original sleeplog boot.js.
    // Uses HRM-raw isWearing check by default, or temperature if wearTemp is changed.
    checkIsWearing: function (returnFn, data) {
      if (this.conf.wearTemp !== 19.5) {
        return returnFn(!Bangle.isCharging() && E.getTemperature() >= this.conf.wearTemp, data);
      }

      var tmp = {
        isWearing: false,
        listener: function (hrm) { tmp.isWearing = !!hrm.isWearing; }
      };

      Bangle.setHRMPower(true, "sleepstream-wearing");
      setTimeout(function () {
        Bangle.on("HRM-raw", tmp.listener);
        setTimeout(function () {
          Bangle.removeListener("HRM-raw", tmp.listener);
          Bangle.setHRMPower(false, "sleepstream-wearing");
          returnFn(tmp.isWearing, data);
        }, 34);
      }, 2500);
    },

    applyState: function (data) {
      data.prevStatus = this.status;
      data.prevConsecutive = this.consecutive;
      this.info.lastCheck = data.timestamp;

      // Correct light sleep to awake if not previously deep sleeping
      // and no sleep session is active (consistent with original sleeplog)
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

    appendStatus: function (timestamp, status, consecutive) {
      var line = [((timestamp / 6E5) | 0), status | 0, consecutive | 0].join(",") + "\n";
      require("Storage").open("sleepstream.log", "a").write(line);
    },

    sendUpdate: function (data, sourceMode) {
      this.sequence += 1;

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
      } catch (e) { }
    }
  };

  global.sleepstream.start();
})();
