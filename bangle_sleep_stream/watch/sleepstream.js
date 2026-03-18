// Shared constants and settings for Sleep Stream.
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
    minConsec: 18E5
  };

  var STATUS = {
    UNKNOWN: 0,
    NOT_WORN: 1,
    AWAKE: 2,
    LIGHT_SLEEP: 3,
    DEEP_SLEEP: 4
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

  exports.SETTINGS_FILE = SETTINGS_FILE;
  exports.DEFAULTS = DEFAULTS;
  exports.STATUS = STATUS;
  exports.CONSECUTIVE = CONSECUTIVE;
  exports.loadSettings = loadSettings;
  exports.saveSettings = saveSettings;
})(exports);
