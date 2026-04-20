// Background boot service for Bangle.js 2.
// Computes sleep state on each health event and streams updates over BLE UART.
// Includes continuous epoch-based sleep monitoring for REM detection.

(function () {
  var lib = require("sleepstream.js");
  var STATUS = lib.STATUS;
  var CONSECUTIVE = lib.CONSECUTIVE;
  var RUNTIME_FILE = "sleepstream.runtime.json";
  var EPOCH_LOG = "sleepstream.epochs.log";

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

    // ── Monitoring state ──
    monitoring: false,
    nightCtx: null,
    epochInterval: null,
    accelListener: null,
    hrmListener: null,
    // Epoch accumulators
    magSum: 0,
    magAbsDevSum: 0,
    magCount: 0,
    magRunMean: 1,       // running estimate of mean magnitude (init ~1g)
    bpmBuf: [],
    currentStage: STATUS.UNKNOWN,
    lastFeatures: null,

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
      this.stopMonitoring();
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
        info: global.sleepstream.info,
        monitoring: global.sleepstream.monitoring
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

    // ── Sleep monitoring ──

    startMonitoring: function () {
      if (this.monitoring) return;
      this.monitoring = true;
      this.nightCtx = new lib.NightContext();
      this.nightCtx.monStart = Date.now();
      this.currentStage = STATUS.UNKNOWN;
      this.lastFeatures = null;

      // Reset accumulators
      this.magSum = 0;
      this.magAbsDevSum = 0;
      this.magCount = 0;
      this.magRunMean = 1;
      this.bpmBuf = [];

      // Enable HRM
      Bangle.setHRMPower(true, "sleepstream");

      // Accel listener — incremental MAD computation
      var self = this;
      this.accelListener = function (a) {
        var m = a.mag;
        self.magCount++;
        self.magSum += m;
        // Update running mean with exponential moving average
        self.magRunMean = self.magRunMean * 0.99 + m * 0.01;
        // Accumulate absolute deviation from running mean
        var dev = m - self.magRunMean;
        if (dev < 0) dev = -dev;
        self.magAbsDevSum += dev;
      };
      Bangle.on("accel", this.accelListener);

      // HRM listener — collect BPM readings
      this.hrmListener = function (hrm) {
        if (hrm.confidence > 30 && hrm.bpm > 20 && hrm.bpm < 220) {
          self.bpmBuf.push(hrm.bpm);
          // Cap buffer size to prevent memory growth
          if (self.bpmBuf.length > 60) self.bpmBuf.shift();
        }
      };
      Bangle.on("HRM", this.hrmListener);

      // Epoch interval
      this.epochInterval = setInterval(function () {
        self.processEpoch();
      }, (this.conf.epochLen || 60) * 1000);

      Bangle.buzz(80);
    },

    stopMonitoring: function () {
      if (!this.monitoring) return;
      this.monitoring = false;

      // Disable HRM
      Bangle.setHRMPower(false, "sleepstream");

      // Remove listeners
      if (this.accelListener) {
        Bangle.removeListener("accel", this.accelListener);
        this.accelListener = null;
      }
      if (this.hrmListener) {
        Bangle.removeListener("HRM", this.hrmListener);
        this.hrmListener = null;
      }

      // Clear interval
      if (this.epochInterval) {
        clearInterval(this.epochInterval);
        this.epochInterval = null;
      }

      this.nightCtx = null;
      this.currentStage = STATUS.UNKNOWN;
      this.lastFeatures = null;

      Bangle.buzz(80);
    },

    processEpoch: function () {
      if (!this.nightCtx) return;

      var now = Date.now();
      var activity = lib.computeActivity(this.magSum, this.magAbsDevSum, this.magCount);
      var hr = lib.computeHRFeatures(this.bpmBuf);

      var features = {
        activity: activity,
        meanHR: hr.meanHR,
        sdHR: hr.sdHR,
        hrCount: hr.count,
        ts: now
      };

      this.lastFeatures = features;
      this.currentStage = lib.classifyEpoch(features, this.nightCtx, this.conf);

      // Log epoch to on-device storage (survives BLE disconnects)
      this.logEpoch(now, this.currentStage, features);

      // Push BLE update immediately for real-time triggers (e.g. REM actions)
      var data = {
        timestamp: now,
        status: this.currentStage,
        movement: Math.round(activity * 1000), 
        bpm: Math.round(hr.meanHR)
      };
      this.applyState(data);
      this.sendUpdate(data, 1);

      // Reset accumulators for next epoch
      this.magSum = 0;
      this.magAbsDevSum = 0;
      this.magCount = 0;
      this.bpmBuf = [];
    },

    logEpoch: function (ts, stage, features) {
      var line = [
        (ts / 1000) | 0,
        stage,
        features.meanHR ? features.meanHR.toFixed(1) : "0",
        features.sdHR ? features.sdHR.toFixed(1) : "0",
        features.activity ? features.activity.toFixed(4) : "0"
      ].join(",") + "\n";
      try {
        require("Storage").open(EPOCH_LOG, "a").write(line);
      } catch (e) { }
    },

    // ── Original classifier (fallback when not monitoring) ──

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

      // If monitoring, use the epoch classifier's current stage
      if (global.sleepstream.monitoring && global.sleepstream.currentStage !== STATUS.UNKNOWN) {
        data.status = global.sleepstream.currentStage;
        var sourceMode = 1; // HRM-based when monitoring
        global.sleepstream.applyState(data);
        global.sleepstream.sendUpdate(data, sourceMode);
        return;
      }

      // Fallback: original classifier
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

      var pkt = {
        t: "sleepstream",
        v: 1,
        seq: this.sequence,
        ts: (data.timestamp / 1000) | 0,
        status: data.status,
        consecutive: data.consecutive,
        source_mode: sourceMode,
        movement: data.movement === undefined ? null : data.movement,
        bpm: data.bpm === undefined ? null : data.bpm
      };

      // Include HRV features when monitoring
      if (this.monitoring && this.lastFeatures) {
        pkt.sdhr = Math.round(this.lastFeatures.sdHR * 10) / 10;
      }

      try {
        Bluetooth.println(JSON.stringify(pkt));
      } catch (e) { }
    }
  };

  global.sleepstream.start();
})();
