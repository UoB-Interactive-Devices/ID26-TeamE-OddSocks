// File summary:
// Interactive debug app screen for Sleep Stream on Bangle.js 2.
// Provides multiple pages with useful diagnostics:
// - live service state and BLE link details
// - latest protocol packet decode
// - active configuration values
// - tail of the local status log

(function() {
  var lib = require("sleepstream.js");

  function statusLabel(v) {
    return ["unknown", "not_worn", "awake", "light", "deep"][v] || "?";
  }

  function consecutiveLabel(v) {
    return ["unknown", "no", "yes"][v] || "?";
  }

  function sourceLabel(v) {
    return v === 1 ? "hrm" : "movement";
  }

  function parsePayload(bytes) {
    if (!bytes || bytes.length !== 16) return undefined;
    var view = new DataView(bytes.buffer);
    return {
      version: view.getUint8(0),
      status: view.getUint8(1),
      consecutive: view.getUint8(2),
      sourceMode: view.getUint8(3),
      sequence: view.getUint32(4, true),
      timestampSec: view.getUint32(8, true),
      movement: view.getUint16(12, true),
      bpm: view.getUint16(14, true)
    };
  }

  function shortTime(ms) {
    if (!ms) return "-";
    return require("locale").time(new Date(ms), 1);
  }

  function formatMaybe(v) {
    return v === undefined || v === null || v === 0xFFFF ? "-" : "" + v;
  }

  function readTailLines(fileName, maxChars, maxLines) {
    var file = require("Storage").open(fileName, "r");
    var len = file.getLength();
    if (!len) return [];

    var skip = len > maxChars ? len - maxChars : 0;
    if (skip) file.read(skip);

    var chunk = file.read(maxChars) || "";
    var lines = chunk.trim().split("\n");
    if (!lines[0].includes(",")) lines.shift();
    if (lines.length > maxLines) lines = lines.slice(lines.length - maxLines);
    return lines;
  }

  var page = 0;
  var pageCount = 4;
  var tick;

  function drawHeader(title) {
    g.reset().clearRect(0, 24, 175, 175)
      .setFont("6x8", 2)
      .setFontAlign(-1, -1)
      .drawString("Sleep Stream Debug", 4, 28)
      .setFont("6x8")
      .drawString(title, 4, 46)
      .drawLine(0, 58, 175, 58);
  }

  function drawRuntime() {
    drawHeader("Runtime / BLE");

    var rt = global.sleepstream || {};
    var y = 64;
    g.setFont("6x8").setFontAlign(-1, -1);

    [
      "enabled: " + (!!rt.conf),
      "connected: " + (!!rt.connected),
      "status: " + statusLabel(rt.status | 0),
      "consecutive: " + consecutiveLabel(rt.consecutive | 0),
      "sequence: " + (rt.sequence | 0),
      "last check: " + shortTime((rt.info || {}).lastCheck),
      "last change: " + shortTime((rt.info || {}).lastChange),
      "asleep since: " + shortTime((rt.info || {}).asleepSince),
      "awake since: " + shortTime((rt.info || {}).awakeSince)
    ].forEach(function(line) {
      g.drawString(line, 4, y);
      y += 11;
    });
  }

  function drawPacket() {
    drawHeader("Latest packet");

    var rt = global.sleepstream;
    var pkt = parsePayload(rt && rt.lastPayload);
    var y = 64;

    g.setFont("6x8").setFontAlign(-1, -1);

    if (!pkt) {
      g.drawString("No payload yet", 4, y);
      return;
    }

    [
      "ver: " + pkt.version,
      "status: " + statusLabel(pkt.status),
      "consec: " + consecutiveLabel(pkt.consecutive),
      "source: " + sourceLabel(pkt.sourceMode),
      "seq: " + pkt.sequence,
      "ts: " + require("locale").date(new Date(pkt.timestampSec * 1000), 1) + " " + shortTime(pkt.timestampSec * 1000),
      "movement: " + formatMaybe(pkt.movement),
      "bpm: " + formatMaybe(pkt.bpm)
    ].forEach(function(line) {
      g.drawString(line, 4, y);
      y += 11;
    });
  }

  function drawConfig() {
    drawHeader("Config snapshot");

    var conf = (global.sleepstream && global.sleepstream.conf) || lib.loadSettings();
    var y = 64;

    g.setFont("6x8").setFontAlign(-1, -1);

    [
      "preferHRM: " + !!conf.preferHRM,
      "deepTh/lightTh: " + conf.deepTh + "/" + conf.lightTh,
      "hrmDeep/hrmLight: " + conf.hrmDeepTh + "/" + conf.hrmLightTh,
      "wearTemp: " + conf.wearTemp,
      "maxAwake(min): " + ((conf.maxAwake / 6E4) | 0),
      "minConsec(min): " + ((conf.minConsec / 6E4) | 0),
      "advWhenDisc: " + !!conf.advertiseWhenDisconnected,
      "namePrefix: " + conf.deviceNamePrefix
    ].forEach(function(line) {
      g.drawString(line, 4, y);
      y += 11;
    });
  }

  function drawLogTail() {
    drawHeader("Log tail (sleepstream.log)");
    var y = 64;
    g.setFont("6x8").setFontAlign(-1, -1);

    var lines = readTailLines("sleepstream.log", 400, 9);
    if (!lines.length) {
      g.drawString("No log lines", 4, y);
      return;
    }

    lines.forEach(function(line) {
      g.drawString(line, 4, y);
      y += 11;
    });
  }

  function drawPage() {
    if (page === 0) drawRuntime();
    else if (page === 1) drawPacket();
    else if (page === 2) drawConfig();
    else drawLogTail();

    g.reset().setFont("6x8").setFontAlign(1, 1)
      .drawString("tap/swipe  " + (page + 1) + "/" + pageCount, 173, 173);
  }

  function nextPage() {
    page = (page + 1) % pageCount;
    drawPage();
  }

  Bangle.loadWidgets();
  g.clear(true);
  Bangle.drawWidgets();

  Bangle.setUI({
    mode: "custom",
    back: load,
    touch: function() { nextPage(); },
    swipe: function(h) {
      if (h < 0) page = (page + 1) % pageCount;
      else if (h > 0) page = (page + pageCount - 1) % pageCount;
      drawPage();
    }
  });

  tick = setInterval(drawPage, 1000);
  E.on("kill", function() {
    if (tick) tick = clearInterval(tick);
  });

  drawPage();
})();
