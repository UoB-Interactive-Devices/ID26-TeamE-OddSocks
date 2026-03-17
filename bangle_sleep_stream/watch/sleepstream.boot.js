// File summary:
// Background boot service for Bangle.js 2 that:
// - computes sleep and consecutive state on each health recheck
// - exposes a custom BLE GATT service for state streaming
// - sends one notify payload per processed recheck
// - auto-recovers advertising/listeners across disconnects and reloads

(function() {
  var lib = require("sleepstream");
  var STATUS = lib.STATUS;
  var CONSECUTIVE = lib.CONSECUTIVE;

  var SERVICE_UUID = "12345678-1234-5678-1234-56789abc0000";
  var UPDATE_CHAR_UUID = "12345678-1234-5678-1234-56789abc0001";

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

    initBle: function() {
      var service = {};
      service[SERVICE_UUID] = {};
      service[SERVICE_UUID][UPDATE_CHAR_UUID] = {
        readable: true,
        notify: true,
        value: this.lastPayload
      };

      NRF.setServices(service, {
        advertise: [SERVICE_UUID],
        uart: false
      });

      this.startAdvertising();
    },

    startAdvertising: function() {
      if (!this.conf.advertiseWhenDisconnected) return;
      NRF.setAdvertising({}, {
        discoverable: true,
        connectable: true,
        scannable: true,
        showName: true,
        name: this.conf.deviceNamePrefix,
        interval: 375
      });
    },

    onConnect: function() {
      global.sleepstream.connected = true;
    },

    onDisconnect: function() {
      global.sleepstream.connected = false;
      setTimeout(function() {
        if (global.sleepstream) global.sleepstream.startAdvertising();
      }, 300);
    },

    start: function() {
      this.initBle();
      E.on("kill", this.saveRuntimeState);
      NRF.on("connect", this.onConnect);
      NRF.on("disconnect", this.onDisconnect);
      Bangle.prependListener("health", this.health);
    },

    stop: function() {
      Bangle.removeListener("health", this.health);
      NRF.removeListener("connect", this.onConnect);
      NRF.removeListener("disconnect", this.onDisconnect);
      E.removeListener("kill", this.saveRuntimeState);
    },

    saveRuntimeState: function() {
      if (!global.sleepstream) return;
      require("Storage").writeJSON("sleepstream.runtime.json", {
        status: global.sleepstream.status,
        consecutive: global.sleepstream.consecutive,
        sequence: global.sleepstream.sequence,
        info: global.sleepstream.info
      });
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
          global.sleepstream.applyState(corrected);
          global.sleepstream.sendUpdate(corrected, sourceMode);
        }, data);
        return;
      }

      global.sleepstream.applyState(data);
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

      var update = {};
      update[SERVICE_UUID] = {};
      update[SERVICE_UUID][UPDATE_CHAR_UUID] = { value: this.lastPayload };

      try {
        NRF.updateServices(update);
      } catch (e) {
        // Keep best-effort semantics: we do not queue or throw on notify failure.
      }
    }
  };

  global.sleepstream.start();
})();
