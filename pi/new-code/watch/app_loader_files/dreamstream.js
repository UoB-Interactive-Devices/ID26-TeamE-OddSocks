// Shared constants, settings, feature extraction, and classifier for Sleep Stream.
// Used by boot service, settings menu, and debug app.

(function(exports) {
  var SETTINGS_FILE = "sleepstream.json";

  var DEFAULTS = {
    enabled: true,
    // Continuous monitoring settings. Activity values are acceleration MAD
    // scores, not proprietary actigraphy counts, so these thresholds are tuned
    // to Bangle.js 2 sensor behaviour rather than copied from papers.
    epochLen: 60,         // seconds per epoch; lower battery cost than 30s PSG epochs
    remLatency: 70,       // minutes before REM allowed, following Yoon's heuristic

    // Movement gates. Normal wake is smoothed, but a very large movement should
    // break through immediately so the device does not cue during obvious wake.
    actWakeTh: 0.15,      // movement high enough to be a wake candidate
    strongWakeTh: 0.22,   // movement high enough for immediate wake
    actDeepMax: 0.04,     // deep can tolerate quiet Bangle movement/noise
    actRemMax: 0.04,      // REM should be still because of muscle atonia

    // Cardiac gates. sdHR is a coarse PPG BPM-variability proxy, not clinical
    // R-R interval HRV; it is still useful for stable deep vs unstable REM.
    wakeHrTh: 84,         // HR this high supports wake only with movement/very high sdHR
    deepSdhrMax: 1.8,     // deep sleep should have stable HR
    deepHrMargin: 6,      // bpm above rolling median still allowed for deep
    remSdhrMin: 3.0,      // REM requires elevated HR variability
    remHrMargin: 2,       // bpm above rolling median required for REM

    // Adaptive REM score. This approximates Yoon's adaptive threshold idea with
    // cheap z-scored watch features instead of PCA over ECG HRV parameters.
    remScoreOffset: 0.6,  // adaptive REM score must exceed rolling baseline
    historyMax: 120,      // rolling feature history, in epochs

    // Temporal smoothing. Deep and REM need repeated recent candidates; this is
    // the low-compute substitute for sequence models / smoothed features.
    stageWindow: 8,       // smoothing window, in epochs
    deepVotes: 5,
    remVotes: 4,
    wakeWindow: 3,
    wakeVotes: 2
  };

  var STATUS = {
    UNKNOWN: 0,
    NOT_WORN: 1,
    AWAKE: 2,
    LIGHT_SLEEP: 3,
    DEEP_SLEEP: 4,
    REM_SLEEP: 5
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

    // Rolling feature histories for user-specific adaptation. These let the
    // watch compare the current epoch with this night's recent baseline.
    this.hrValues = [];
    this.sdhrValues = [];
    this.activityValues = [];
    this.remScoreValues = [];

    // Ring buffer of raw epoch stages for temporal smoothing
    this.ring = [];
    this.ringMax = 8;
    this.lastStableStage = STATUS.UNKNOWN;
  }

  NightContext.prototype.reset = function() {
    this.sleepStart = 0;
    this.monStart = 0;
    this.hrValues = [];
    this.sdhrValues = [];
    this.activityValues = [];
    this.remScoreValues = [];
    this.ring = [];
    this.lastStableStage = STATUS.UNKNOWN;
  };

  NightContext.prototype.pushLimited = function(arr, value, maxLen) {
    if (value === undefined || value === null || !isFinite(value)) return;
    arr.push(value);
    while (arr.length > maxLen) arr.shift();
  };

  /**
   * Update rolling feature distributions after a sleep-like epoch.
   * Wake/not-worn epochs are deliberately excluded so personal sleep baselines
   * are not pulled upward by getting out of bed or noisy sensor readings.
   */
  NightContext.prototype.addFeatures = function(meanHR, sdHR, activity, remScore, conf) {
    var maxLen = (conf && conf.historyMax) || 120;
    if (maxLen < 10) maxLen = 10;
    if (meanHR <= 0) return;
    this.pushLimited(this.hrValues, meanHR, maxLen);
    this.pushLimited(this.sdhrValues, sdHR, maxLen);
    this.pushLimited(this.activityValues, activity, maxLen);
    this.pushLimited(this.remScoreValues, remScore, maxLen);
  };

  NightContext.prototype.quantile = function(arr, p) {
    var n = arr.length;
    if (n < 3) return 0;
    var a = arr.slice().sort(function(x, y) { return x - y; });
    var idx = (n - 1) * p;
    var lo = Math.floor(idx);
    var hi = Math.ceil(idx);
    if (lo === hi) return a[lo];
    return a[lo] + (a[hi] - a[lo]) * (idx - lo);
  };

  NightContext.prototype.mean = function(arr) {
    var n = arr.length;
    if (!n) return 0;
    var s = 0;
    for (var i = 0; i < n; i++) s += arr[i];
    return s / n;
  };

  NightContext.prototype.std = function(arr) {
    var n = arr.length;
    if (n < 3) return 0;
    var m = this.mean(arr);
    var s = 0;
    for (var i = 0; i < n; i++) {
      var d = arr[i] - m;
      s += d * d;
    }
    return Math.sqrt(s / (n - 1));
  };

  NightContext.prototype.zScore = function(value, arr) {
    var sd = this.std(arr);
    if (!sd) return 0;
    var z = (value - this.mean(arr)) / sd;
    // Clamp extreme z-scores so one very flat history does not create a huge
    // REM score when the first variable epoch arrives.
    if (z > 4) return 4;
    if (z < -4) return -4;
    return z;
  };

  /** Rolling percentile over recent sleep-like epochs. */
  NightContext.prototype.hrPercentile = function(p) {
    return this.quantile(this.hrValues, p);
  };

  NightContext.prototype.hrP50 = function() { return this.hrPercentile(0.5); };

  NightContext.prototype.remScore = function(activity, meanHR, sdHR) {
    // REM-like physiology is: HR above personal baseline, HR variability above
    // personal baseline, and movement below personal baseline.
    return this.zScore(meanHR, this.hrValues) +
      this.zScore(sdHR, this.sdhrValues) -
      this.zScore(activity, this.activityValues);
  };

  NightContext.prototype.remScoreBaseline = function() {
    return this.quantile(this.remScoreValues, 0.5);
  };

  /** Push a stage to the ring buffer for smoothing. */
  NightContext.prototype.pushStage = function(stage) {
    this.ring.push(stage);
    if (this.ring.length > this.ringMax) this.ring.shift();
  };

  NightContext.prototype.ringCountRecent = function(stage, window) {
    var c = 0;
    var start = this.ring.length - window;
    if (start < 0) start = 0;
    for (var i = start; i < this.ring.length; i++)
      if (this.ring[i] === stage) c++;
    return c;
  };

  /**
   * Convert a raw one-minute decision into a stable reported stage.
   * The raw rules are intentionally responsive, but the reported stage needs
   * hysteresis so one noisy minute does not trigger a stimulus or fragment logs.
   */
  NightContext.prototype.smoothStage = function(rawStage, conf, immediateWake) {
    this.ringMax = conf.stageWindow || this.ringMax || 8;
    this.pushStage(rawStage);

    var out = STATUS.LIGHT_SLEEP;
    if (rawStage === STATUS.AWAKE) {
      // High movement means wake now; weaker wake candidates need repeated
      // support so REM-like HR spikes are not treated as awake too easily.
      if (immediateWake ||
        this.ringCountRecent(STATUS.AWAKE, conf.wakeWindow || 3) >= (conf.wakeVotes || 2)) {
        out = STATUS.AWAKE;
      } else {
        out = this.lastStableStage > STATUS.AWAKE ? this.lastStableStage : STATUS.LIGHT_SLEEP;
      }
    } else if (rawStage === STATUS.DEEP_SLEEP) {
      // Deep and REM are only exposed after enough recent candidates. Until
      // then, light sleep is the safest sleep-like default.
      out = this.ringCountRecent(STATUS.DEEP_SLEEP, conf.stageWindow || 8) >= (conf.deepVotes || 5) ?
        STATUS.DEEP_SLEEP : STATUS.LIGHT_SLEEP;
    } else if (rawStage === STATUS.REM_SLEEP) {
      out = this.ringCountRecent(STATUS.REM_SLEEP, conf.stageWindow || 8) >= (conf.remVotes || 5) ?
        STATUS.REM_SLEEP : STATUS.LIGHT_SLEEP;
    }

    this.lastStableStage = out;
    return out;
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

    // Not enough HR data: use movement-only decisions for wake/not-worn and
    // default sleep-like stillness to light rather than inventing HR stages.
    var hrValid = hrCount >= 3 && meanHR > 20;

    // ── 1. Wear detection ──
    if (Bangle.isCharging()) return STATUS.NOT_WORN;
    // Very low HR confidence / no HR + no movement likely means not worn
    if (!hrValid && activity < 0.005) return STATUS.NOT_WORN;

    // ── 2. Wake vs sleep ──
    // HR alone is not enough to call wake because REM can also raise HR.
    var immediateWake = activity > (conf.strongWakeTh || 0.22);
    var wakeCandidate = activity > conf.actWakeTh;
    if (hrValid && meanHR > (conf.wakeHrTh || 84) &&
      (activity > (conf.actRemMax || 0.04) || sdHR > ((conf.remSdhrMin || 3) + 2))) {
      wakeCandidate = true;
    }
    if (wakeCandidate) return ctx.smoothStage(STATUS.AWAKE, conf, immediateWake);

    // From here, the epoch is sleep-like: low movement and not obviously off
    // wrist. The first sleep-like epoch starts the REM-latency clock.
    if (!ctx.sleepStart) ctx.sleepStart = now;

    var hrP50 = ctx.hrP50();
    var minsSleep = ctx.minutesSinceSleep(now);
    var remScore = hrValid ? ctx.remScore(activity, meanHR, sdHR) : 0;
    features.remScore = remScore;
    var rawStage = STATUS.LIGHT_SLEEP;

    // ── 3. Deep sleep ──
    // Deep is quiet and autonomically stable. The HR margin is deliberately
    // loose because Bangle PPG is noisy and Withings comparison showed that a
    // too-strict HR/actigraphy gate under-called deep sleep.
    if (activity < conf.actDeepMax && hrValid && hrP50 > 0 &&
      sdHR <= (conf.deepSdhrMax || 1.5) &&
      meanHR <= hrP50 + (conf.deepHrMargin || 2)) {
      rawStage = STATUS.DEEP_SLEEP;
    }

    // ── 4. REM vs light ──
    // Yoon-style adaptive idea: cardiac activation must exceed a rolling
    // personal baseline, occur while movement remains low, and happen after
    // normal first-cycle REM latency.
    var remCandidate = (
      activity < conf.actRemMax &&       // still (muscle atonia)
      hrValid &&
      minsSleep >= conf.remLatency &&     // REM latency constraint
      hrP50 > 0 &&
      meanHR >= hrP50 + (conf.remHrMargin || 2) &&
      sdHR >= (conf.remSdhrMin || 3) &&
      ctx.remScoreValues.length >= 10 &&
      remScore > ctx.remScoreBaseline() + (conf.remScoreOffset || 0.8)
    );

    if (remCandidate) rawStage = STATUS.REM_SLEEP;

    if (hrValid) ctx.addFeatures(meanHR, sdHR, activity, remScore, conf);

    // ── 5. Stable reported stage ──
    // Report the smoothed stage, not the raw candidate, so downstream cueing
    // reacts to sleep episodes rather than individual noisy epochs.
    return ctx.smoothStage(rawStage, conf, false);
  }

  // ── Exports ──

  exports.SETTINGS_FILE = SETTINGS_FILE;
  exports.DEFAULTS = DEFAULTS;
  exports.STATUS = STATUS;
  exports.loadSettings = loadSettings;
  exports.saveSettings = saveSettings;
  exports.computeActivity = computeActivity;
  exports.computeHRFeatures = computeHRFeatures;
  exports.NightContext = NightContext;
  exports.classifyEpoch = classifyEpoch;
})(exports);
