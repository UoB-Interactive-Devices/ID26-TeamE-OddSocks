// File summary:
// Canonical Espruino module entry for Sleep Stream.
// The service/app require("sleepstream"), so this file must exist in Storage.
// It mirrors helpers/constants from sleepstream.lib.js for compatibility.

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
    advertiseWhenDisconnected: true,
    deviceNamePrefix: "BangleSleep",
    measurementLogEnabled: true,
    eventLogEnabled: true
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

  function packUpdate(packet) {
    var movement = packet.movement;
    if (movement === undefined || movement === null) movement = 0xFFFF;
    var bpm = packet.bpm;
    if (bpm === undefined || bpm === null) bpm = 0xFFFF;

    var bytes = new Uint8Array(16);
    var view = new DataView(bytes.buffer);

    view.setUint8(0, 1);
    view.setUint8(1, packet.status | 0);
    view.setUint8(2, packet.consecutive | 0);
    view.setUint8(3, packet.sourceMode | 0);
    view.setUint32(4, packet.sequence >>> 0, true);
    view.setUint32(8, packet.timestampSec >>> 0, true);
    view.setUint16(12, movement & 0xFFFF, true);
    view.setUint16(14, bpm & 0xFFFF, true);

    return bytes;
  }

  exports.SETTINGS_FILE = SETTINGS_FILE;
  exports.DEFAULTS = DEFAULTS;
  exports.STATUS = STATUS;
  exports.CONSECUTIVE = CONSECUTIVE;
  exports.loadSettings = loadSettings;
  exports.saveSettings = saveSettings;
  exports.packUpdate = packUpdate;
})(exports);
