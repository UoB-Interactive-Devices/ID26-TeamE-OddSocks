// Background boot service for Bangle.js 2.
// Runs manual start/stop sleep monitoring and streams each classified epoch
// over BLE UART for the Raspberry Pi receiver.

(function () {
  var lib = require("dreamstream.js");
  var STATUS = lib.STATUS;
  var RUNTIME_FILE = "sleepstream.runtime.json";
  var EPOCH_LOG = "sleepstream.epochs.log";
  var AUTO_RESUME_DELAY_MS = 3000;
  var WATCHDOG_MS = 120000;

  var conf = lib.loadSettings();
  if (!conf.enabled) {
    delete global.sleepstream;
    return;
  }

  global.sleepstream = {
    conf: conf,
    status: STATUS.UNKNOWN,
    sequence: 0,
    connected: false,
    trackingWanted: false,
    trackingStartedAt: 0,
    savedSleepStart: 0,
    info: {
      lastEpoch: 0,
      lastChange: 0
    },

    // Monitoring state for the current manual session.
    monitoring: false,
    nightCtx: null,
    epochInterval: null,
    watchdogInterval: null,
    accelListener: null,
    hrmListener: null,

    // Epoch accumulators. These are reset after every classification window.
    magSum: 0,
    magAbsDevSum: 0,
    magCount: 0,
    magRunMean: 1,       // running estimate of mean magnitude (init ~1g)
    bpmBuf: [],
    currentStage: STATUS.UNKNOWN,
    lastFeatures: null,

    onConnect: function () {
      var rt = global.sleepstream;
      rt.connected = true;
      if (rt.trackingWanted) rt.sendStartControl(true);
    },

    onDisconnect: function () {
      global.sleepstream.connected = false;
    },

    start: function () {
      this.restoreRuntimeState();
      NRF.on("connect", this.onConnect);
      NRF.on("disconnect", this.onDisconnect);
      E.on("kill", this.saveRuntimeState);
      this.startWatchdog();
      if (this.trackingWanted) {
        setTimeout(function () {
          if (global.sleepstream) global.sleepstream.ensureMonitoring();
        }, AUTO_RESUME_DELAY_MS);
      }
    },

    stop: function () {
      this.stopMonitoring();
      if (this.watchdogInterval) {
        clearInterval(this.watchdogInterval);
        this.watchdogInterval = null;
      }
      NRF.removeListener("connect", this.onConnect);
      NRF.removeListener("disconnect", this.onDisconnect);
      E.removeListener("kill", this.saveRuntimeState);
    },

    saveRuntimeState: function () {
      if (!global.sleepstream) return;
      var rt = global.sleepstream;
      var sleepStart = rt.savedSleepStart;
      if (rt.nightCtx && rt.nightCtx.sleepStart) sleepStart = rt.nightCtx.sleepStart;
      try {
        require("Storage").writeJSON(RUNTIME_FILE, {
          status: rt.status,
          sequence: rt.sequence,
          info: rt.info,
          trackingWanted: rt.trackingWanted,
          trackingStartedAt: rt.trackingStartedAt,
          sleepStart: sleepStart
        });
      } catch (e) { }
    },

    restoreRuntimeState: function () {
      var saved = require("Storage").readJSON(RUNTIME_FILE, true) || {};
      if (typeof saved.status === "number") this.status = saved.status | 0;
      if (typeof saved.sequence === "number") this.sequence = saved.sequence >>> 0;
      this.trackingWanted = saved.trackingWanted === true;
      this.trackingStartedAt = typeof saved.trackingStartedAt === "number" ? saved.trackingStartedAt : 0;
      this.savedSleepStart = typeof saved.sleepStart === "number" ? saved.sleepStart : 0;

      if (saved.info && typeof saved.info === "object") {
        this.info.lastEpoch = typeof saved.info.lastEpoch === "number" ? saved.info.lastEpoch : 0;
        this.info.lastChange = typeof saved.info.lastChange === "number" ? saved.info.lastChange : 0;
      }
    },

    // Sleep monitoring

    startWatchdog: function () {
      if (this.watchdogInterval) return;
      var self = this;
      this.watchdogInterval = setInterval(function () {
        self.ensureMonitoring();
      }, WATCHDOG_MS);
    },

    ensureMonitoring: function () {
      if (this.trackingWanted && !this.monitoring) this.startMonitoring(true);
    },

    startMonitoring: function (autoResume) {
      var resume = autoResume === true;
      if (this.monitoring) {
        if (!this.trackingWanted) {
          this.trackingWanted = true;
          this.saveRuntimeState();
        }
        return;
      }

      var now = Date.now();
      this.trackingWanted = true;
      if (!resume || !this.trackingStartedAt) this.trackingStartedAt = now;
      if (!resume) this.savedSleepStart = 0;
      this.saveRuntimeState();

      this.monitoring = true;
      this.nightCtx = new lib.NightContext();
      this.nightCtx.monStart = this.trackingStartedAt || now;
      if (resume && this.savedSleepStart) this.nightCtx.sleepStart = this.savedSleepStart;
      this.status = STATUS.UNKNOWN;
      this.currentStage = STATUS.UNKNOWN;
      this.lastFeatures = null;
      if (!resume) {
        this.info.lastEpoch = 0;
        this.info.lastChange = 0;
      }

      // Start every manual session with empty sensor accumulators.
      this.magSum = 0;
      this.magAbsDevSum = 0;
      this.magCount = 0;
      this.magRunMean = 1;
      this.bpmBuf = [];

      // Keep the HRM powered only during an active session to save battery.
      Bangle.setHRMPower(true, "sleepstream");

      // Accelerometer samples are reduced online into mean absolute deviation
      // of magnitude. This gives a cheap movement score without storing samples.
      var self = this;
      this.accelListener = function (a) {
        var m = a.mag;
        self.magCount++;
        self.magSum += m;
        self.magRunMean = self.magRunMean * 0.99 + m * 0.01;
        var dev = m - self.magRunMean;
        if (dev < 0) dev = -dev;
        self.magAbsDevSum += dev;
      };
      Bangle.on("accel", this.accelListener);

      // PPG BPM readings are filtered by confidence and physiological range
      // before they contribute to mean HR and BPM variability for the epoch.
      this.hrmListener = function (hrm) {
        if (hrm.confidence > 30 && hrm.bpm > 20 && hrm.bpm < 220) {
          self.bpmBuf.push(hrm.bpm);
          if (self.bpmBuf.length > 60) self.bpmBuf.shift();
        }
      };
      Bangle.on("HRM", this.hrmListener);

      // The classifier runs once per epoch; all raw sensor sampling happens in
      // the listeners above between interval ticks.
      this.epochInterval = setInterval(function () {
        self.processEpoch();
      }, (this.conf.epochLen || 60) * 1000);

      if (resume) this.sendStartControl(true);
      else Bangle.buzz(80);
    },

    stopMonitoring: function () {
      var wasMonitoring = this.monitoring;
      this.trackingWanted = false;
      this.trackingStartedAt = 0;
      this.savedSleepStart = 0;
      this.status = STATUS.UNKNOWN;
      this.currentStage = STATUS.UNKNOWN;
      this.lastFeatures = null;
      this.info.lastChange = Date.now();

      if (!wasMonitoring) {
        this.saveRuntimeState();
        return;
      }
      this.monitoring = false;

      Bangle.setHRMPower(false, "sleepstream");

      // Remove active session listeners so the watch returns to idle behaviour.
      if (this.accelListener) {
        Bangle.removeListener("accel", this.accelListener);
        this.accelListener = null;
      }
      if (this.hrmListener) {
        Bangle.removeListener("HRM", this.hrmListener);
        this.hrmListener = null;
      }

      if (this.epochInterval) {
        clearInterval(this.epochInterval);
        this.epochInterval = null;
      }

      this.nightCtx = null;
      this.saveRuntimeState();

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
      var previousSleepStart = this.nightCtx.sleepStart;
      this.currentStage = lib.classifyEpoch(features, this.nightCtx, this.conf);
      if (this.nightCtx.sleepStart && this.nightCtx.sleepStart !== previousSleepStart) {
        this.savedSleepStart = this.nightCtx.sleepStart;
        this.saveRuntimeState();
      }
      this.info.lastEpoch = now;
      if (this.status !== this.currentStage) this.info.lastChange = now;
      this.status = this.currentStage;

      // Keep a compact on-watch CSV-style epoch log so BLE disconnects do not
      // lose the evidence used for later debugging/report plots.
      this.logEpoch(now, this.currentStage, features);

      // Push the latest stage immediately for real-time triggers, especially
      // REM-based stimulation on the Pi side.
      var data = {
        timestamp: now,
        status: this.currentStage,
        movement: Math.round(activity * 1000),
        bpm: Math.round(hr.meanHR)
      };
      this.sendUpdate(data);

      // Start the next epoch with fresh accumulators while retaining the
      // classifier's rolling night context.
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

    sendStartControl: function (autoResume) {
      var pkt = {
        cmd: "start",
        src: "dreamstream",
        ts: (Date.now() / 1000) | 0
      };
      if (autoResume) pkt.auto = true;
      try {
        Bluetooth.println(JSON.stringify(pkt));
      } catch (e) { }
    },

    sendUpdate: function (data) {
      this.sequence += 1;

      // The packet intentionally contains only the live epoch result and the
      // features the receiver/reporting code needs. Session state is controlled
      // by the explicit start/stop commands sent by the watch UI.
      var pkt = {
        t: "dreamstream",
        v: 1,
        seq: this.sequence,
        ts: (data.timestamp / 1000) | 0,
        status: data.status,
        movement: data.movement === undefined ? null : data.movement,
        bpm: data.bpm === undefined ? null : data.bpm
      };

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
