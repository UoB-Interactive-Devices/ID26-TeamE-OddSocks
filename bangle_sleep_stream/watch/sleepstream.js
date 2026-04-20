// Shared constants, settings, feature extraction, and classifier for Sleep Stream.
// Used by boot service, settings menu, and debug app.

(function(exports) {
  var SETTINGS_FILE = "sleepstream.json";

  var DEFAULTS = {
    enabled: true,
    preferHRM: false,
    deepTh: 150,
    lightTh: 300,
    hrmDeepTh: 60,
    hrmLightTh: 74,
    wearTemp: 19.5,
    maxAwake: 36E5,
    minConsec: 18E5,
    // REM / epoch settings
    epochLen: 60,         // seconds per epoch
    remLatency: 60,       // minutes before REM allowed
    actWakeTh: 0.15,      // activity MAD threshold for wake
    actDeepMax: 0.02,     // max activity for deep sleep
    actRemMax: 0.04       // max activity for REM
  };

  var STATUS = {
    UNKNOWN: 0,
    NOT_WORN: 1,
    AWAKE: 2,
    LIGHT_SLEEP: 3,
    DEEP_SLEEP: 4,
    REM_SLEEP: 5
  };

  var CONSECUTIVE = {
    UNKNOWN: 0,
    NO: 1,
    YES: 2
  };

  function loadSettings() {
    return Object.assign({}, DEFAULTS, require("Storage").readJSON(SETTINGS_FILE, true) || {});
  }

  function saveSettings(settings) {
    require("Storage").writeJSON(SETTINGS_FILE, settings || {});
  }

  // ── Feature extraction ──

  /**
   * Compute activity score from incremental accel stats.
   * magSum / magCount = mean magnitude.
   * magAbsDevSum / magCount = mean absolute deviation (MAD) of magnitude.
   * Returns activity as the MAD value (lower = less movement).
   */
  function computeActivity(magSum, magAbsDevSum, magCount) {
    if (magCount < 1) return 0;
    return magAbsDevSum / magCount;
  }

  /**
   * Compute HR features from an array of BPM readings collected during the epoch.
   * Returns { meanHR, sdHR, count }.
   */
  function computeHRFeatures(bpmArr) {
    var n = bpmArr.length;
    if (n === 0) return { meanHR: 0, sdHR: 0, count: 0 };
    var sum = 0;
    for (var i = 0; i < n; i++) sum += bpmArr[i];
    var mean = sum / n;
    if (n < 2) return { meanHR: mean, sdHR: 0, count: n };
    var sqSum = 0;
    for (var i = 0; i < n; i++) {
      var d = bpmArr[i] - mean;
      sqSum += d * d;
    }
    return { meanHR: mean, sdHR: Math.sqrt(sqSum / (n - 1)), count: n };
  }

  // ── Night context ──

  function NightContext() {
    this.sleepStart = 0;       // timestamp ms of first sleep epoch
    this.monStart = 0;         // timestamp ms when monitoring started
    this.hrMin = 999;
    this.hrMax = 0;
    this.hrSum = 0;
    this.hrCount = 0;
    // Ring buffer of last 4 epoch stages for temporal smoothing
    this.ring = [];
    this.ringMax = 4;
  }

  NightContext.prototype.reset = function() {
    this.sleepStart = 0;
    this.monStart = 0;
    this.hrMin = 999;
    this.hrMax = 0;
    this.hrSum = 0;
    this.hrCount = 0;
    this.ring = [];
  };

  /** Update HR distribution tracking. */
  NightContext.prototype.addHR = function(meanHR) {
    if (meanHR <= 0) return;
    if (meanHR < this.hrMin) this.hrMin = meanHR;
    if (meanHR > this.hrMax) this.hrMax = meanHR;
    this.hrSum += meanHR;
    this.hrCount++;
  };

  /** Approximate percentile from min/max/mean using linear interpolation. */
  NightContext.prototype.hrPercentile = function(p) {
    if (this.hrCount < 3) return 0;
    // Simple estimate: assume roughly normal distribution around mean
    // P20 ≈ min + 0.2*(max-min), P50 ≈ mean, P80 ≈ min + 0.8*(max-min)
    return this.hrMin + p * (this.hrMax - this.hrMin);
  };

  NightContext.prototype.hrP20 = function() { return this.hrPercentile(0.2); };
  NightContext.prototype.hrP50 = function() {
    return this.hrCount > 0 ? this.hrSum / this.hrCount : 0;
  };

  /** Push a stage to the ring buffer for smoothing. */
  NightContext.prototype.pushStage = function(stage) {
    this.ring.push(stage);
    if (this.ring.length > this.ringMax) this.ring.shift();
  };

  /** Count occurrences of a stage in ring buffer. */
  NightContext.prototype.ringCount = function(stage) {
    var c = 0;
    for (var i = 0; i < this.ring.length; i++)
      if (this.ring[i] === stage) c++;
    return c;
  };

  /** Minutes since monitoring started. */
  NightContext.prototype.minutesSinceStart = function(now) {
    if (!this.monStart) return 0;
    return (now - this.monStart) / 60000;
  };

  /** Minutes since first sleep detected. */
  NightContext.prototype.minutesSinceSleep = function(now) {
    if (!this.sleepStart) return 0;
    return (now - this.sleepStart) / 60000;
  };

  // ── Classifier ──

  /**
   * Classify one epoch given features + night context.
   * features: { activity, meanHR, sdHR, hrCount, ts }
   * ctx: NightContext instance
   * conf: settings object
   * Returns a STATUS code.
   */
  function classifyEpoch(features, ctx, conf) {
    var activity = features.activity;
    var meanHR = features.meanHR;
    var sdHR = features.sdHR;
    var hrCount = features.hrCount;
    var now = features.ts;

    // Not enough HR data — rely on activity only
    var hrValid = hrCount >= 3 && meanHR > 20;

    // ── 1. Wear detection ──
    if (Bangle.isCharging()) return STATUS.NOT_WORN;
    // Very low HR confidence / no HR + no movement likely means not worn
    if (!hrValid && activity < 0.005) return STATUS.NOT_WORN;

    // ── 2. Wake vs sleep ──
    if (activity > conf.actWakeTh) return STATUS.AWAKE;
    if (hrValid && meanHR > (conf.hrmLightTh || 74) + 10) return STATUS.AWAKE;

    // From here, candidate is sleep (low activity)
    // Record sleep onset
    if (!ctx.sleepStart) ctx.sleepStart = now;
    // Accumulate HR stats
    if (hrValid) ctx.addHR(meanHR);

    var hrP20 = ctx.hrP20();
    var hrP50 = ctx.hrP50();
    var minsSleep = ctx.minutesSinceSleep(now);

    // ── 3. Deep sleep ──
    // Very low activity + HR in bottom 20th percentile of night
    if (activity < conf.actDeepMax && hrValid && hrP20 > 0 && meanHR < hrP20) {
      // Require >= 2 consecutive deep candidates (via ring buffer)
      ctx.pushStage(STATUS.DEEP_SLEEP);
      if (ctx.ringCount(STATUS.DEEP_SLEEP) >= 2) return STATUS.DEEP_SLEEP;
      // Not enough consecutive — call it light for now
      return STATUS.LIGHT_SLEEP;
    }

    // ── 4. REM vs light ──
    var remCandidate = (
      activity < conf.actRemMax &&       // still (muscle atonia)
      hrValid &&
      minsSleep >= conf.remLatency &&     // REM latency constraint
      hrP50 > 0 &&
      meanHR > hrP50 &&                   // HR elevated vs median
      sdHR > 2.0                          // autonomic instability (sdHR > 2 bpm)
    );

    if (remCandidate) {
      ctx.pushStage(STATUS.REM_SLEEP);
      // Require >= 2 consecutive REM candidates
      if (ctx.ringCount(STATUS.REM_SLEEP) >= 2) return STATUS.REM_SLEEP;
      return STATUS.LIGHT_SLEEP;
    }

    // ── 5. Default: light sleep ──
    ctx.pushStage(STATUS.LIGHT_SLEEP);
    return STATUS.LIGHT_SLEEP;
  }

  // ── Exports ──

  exports.SETTINGS_FILE = SETTINGS_FILE;
  exports.DEFAULTS = DEFAULTS;
  exports.STATUS = STATUS;
  exports.CONSECUTIVE = CONSECUTIVE;
  exports.loadSettings = loadSettings;
  exports.saveSettings = saveSettings;
  exports.computeActivity = computeActivity;
  exports.computeHRFeatures = computeHRFeatures;
  exports.NightContext = NightContext;
  exports.classifyEpoch = classifyEpoch;
})(exports);
