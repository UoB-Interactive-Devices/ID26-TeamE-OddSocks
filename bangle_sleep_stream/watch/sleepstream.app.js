// File summary:
// Interactive debug app screen for Sleep Stream on Bangle.js 2.
// Provides multiple pages with useful diagnostics:
// - live service state and BLE link details
// - latest protocol packet decode
// - active configuration values
// - tail of the local status log

(function() {
  var lib = require("sleepstream.js");
  var CONTENT_TOP_Y = 64;
  var CONTENT_BOTTOM_Y = 157;
  var FOOTER_SPLIT_Y = 160;
  var LEFT_X = 4;
  var RIGHT_X = 173;
  var CONTENT_WIDTH = 168;
  var ROW_HEIGHT = 10;
  var SELF_TEST_MIN_INTERVAL_MS = 500;

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

  function shortDateTime(ms) {
    if (!ms) return "-";
    var d = new Date(ms);
    return require("locale").date(d, 1) + " " + require("locale").time(d, 1);
  }

  function formatMaybe(v) {
    return v === undefined || v === null || v === 0xFFFF ? "-" : "" + v;
  }

  function readTailLines(fileName, maxChars, maxLines, separator) {
    var file = require("Storage").open(fileName, "r");
    var len = file.getLength();
    if (!len) return [];

    var skip = len > maxChars ? len - maxChars : 0;
    if (skip) file.read(skip);

    var chunk = file.read(maxChars) || "";
    var lines = chunk.trim().split("\n");
    if (separator && lines[0] && !lines[0].includes(separator)) lines.shift();
    if (lines.length > maxLines) lines = lines.slice(lines.length - maxLines);
    return lines;
  }

  function parseStatusLogLine(line) {
    var p = (line || "").split(",");
    if (p.length < 3) return line;
    var step = parseInt(p[0], 10);
    var s = parseInt(p[1], 10);
    var c = parseInt(p[2], 10);
    if (isNaN(step)) return line;
    return shortTime(step * 6E5) + " " + statusLabel(s) + " / " + consecutiveLabel(c);
  }

  function parseMeasureLogLine(line) {
    var p = (line || "").split(",");
    if (p.length < 9 || p[0] === "processed_at_ms") return undefined;
    var sampleTs = parseInt(p[1], 10) || 0;
    var movement = p[2] || "-";
    var bpm = p[3] || "-";
    var sourceMode = parseInt(p[4], 10) || 0;
    var status = parseInt(p[7], 10) || 0;
    var consecutive = parseInt(p[8], 10) || 0;
    return shortTime(sampleTs) + " mv=" + movement + " bpm=" + bpm + " " + sourceLabel(sourceMode) + " " + statusLabel(status) + "/" + consecutiveLabel(consecutive);
  }

  function parseEventLogLine(line) {
    var p = (line || "").split("|");
    if (p.length < 3) return line;
    var ts = parseInt(p[0], 10) || 0;
    var kind = p[1] || "info";
    var msg = p[2] || "";
    return shortTime(ts) + " " + kind + " " + msg;
  }

  function fitText(text, maxWidth) {
    var s = text === undefined || text === null ? "" : "" + text;
    if (g.stringWidth(s) <= maxWidth) return s;

    while (s.length > 1 && g.stringWidth(s + "...") > maxWidth) {
      s = s.substr(0, s.length - 1);
    }
    return s + "...";
  }

  function drawLines(lines, startY, maxRows) {
    var y = startY;
    g.setFont("6x8").setFontAlign(-1, -1);

    for (var i = 0; i < lines.length && i < maxRows; i++) {
      g.drawString(fitText(lines[i], CONTENT_WIDTH), LEFT_X, y);
      y += ROW_HEIGHT;
    }
  }

  var page = 0;
  var pageCount = 6;
  var tick;
  var lastSelfTestAt = 0;
  var lastSelfTestStatus = "none";

  function drawHeader(title) {
    g.reset().clearRect(0, 24, 175, 175)
      .setFont("6x8", 2)
      .setFontAlign(-1, -1)
      .drawString("Sleep Stream Debug", LEFT_X, 28)
      .setFont("6x8")
      .drawString(fitText(title, CONTENT_WIDTH), LEFT_X, 46)
      .drawLine(0, 58, 175, 58);
  }

  function drawFooter(hint) {
    g.reset().setFont("6x8").setFontAlign(-1, -1)
      .drawLine(0, FOOTER_SPLIT_Y, 175, FOOTER_SPLIT_Y);

    if (hint) {
      g.drawString(fitText(hint, CONTENT_WIDTH), LEFT_X, 162);
    }

    g.setFontAlign(1, 1)
      .drawString("tap/swipe " + (page + 1) + "/" + pageCount, RIGHT_X, 173);
  }

  function drawRuntime() {
    drawHeader("Runtime / BLE");

    var rt = global.sleepstream || {};

    if (!global.sleepstream) {
      drawLines([
        "Service object missing",
        "sleepstream.boot.js not active",
        "Check Enabled in settings",
        "or reload watch service"
      ], CONTENT_TOP_Y, 9);
      return;
    }

    drawLines([
      "enabled: " + (!!rt.conf),
      "connected: " + (!!rt.connected),
      "status: " + statusLabel(rt.status | 0),
      "consecutive: " + consecutiveLabel(rt.consecutive | 0),
      "sequence: " + (rt.sequence | 0),
      "last check: " + shortDateTime((rt.info || {}).lastCheck),
      "last change: " + shortDateTime((rt.info || {}).lastChange),
      "asleep since: " + shortTime((rt.info || {}).asleepSince),
      "awake since: " + shortTime((rt.info || {}).awakeSince),
      "self-test: " + lastSelfTestStatus
    ], CONTENT_TOP_Y, 9);
  }

  function runSelfTest() {
    if (!global.sleepstream || typeof global.sleepstream.sendUpdate !== "function") {
      lastSelfTestStatus = "service missing";
      Bangle.buzz(120);
      return;
    }

    var now = Date.now();
    var sinceLast = now - lastSelfTestAt;
    if (lastSelfTestAt && sinceLast < SELF_TEST_MIN_INTERVAL_MS) {
      lastSelfTestStatus = "rate limited " + (SELF_TEST_MIN_INTERVAL_MS - sinceLast) + "ms";
      if (global.sleepstream.logEvent)
        global.sleepstream.logEvent("app", "self_test_rate_limited", String(SELF_TEST_MIN_INTERVAL_MS - sinceLast));
      Bangle.buzz(30);
      return;
    }

    var rt = global.sleepstream || {};
    var pkt = parsePayload(rt.lastPayload);

    var status = (pkt && pkt.status) || (rt.status | 0) || 2;
    var consecutive = (pkt && pkt.consecutive) || (rt.consecutive | 0) || 1;
    var movement = (pkt && pkt.movement !== 0xFFFF) ? pkt.movement : 111;
    var bpm = (pkt && pkt.bpm !== 0xFFFF) ? pkt.bpm : 72;
    var sourceMode = pkt ? pkt.sourceMode : 0;

    var sample = {
      timestamp: now,
      status: status,
      consecutive: consecutive,
      movement: movement,
      bpm: bpm
    };

    try {
      global.sleepstream.sendUpdate(sample, sourceMode);
      if (global.sleepstream.logEvent)
        global.sleepstream.logEvent("app", "self_test_sent", "debug_app_button");
      lastSelfTestAt = now;
      lastSelfTestStatus = "sent seq " + ((global.sleepstream.sequence | 0) || "?") + " @ " + require("locale").time(new Date(now), 1);
      Bangle.buzz(60);
    } catch (e) {
      lastSelfTestStatus = "error";
      if (global.sleepstream && global.sleepstream.logEvent)
        global.sleepstream.logEvent("error", "self_test_failed", String(e));
      Bangle.buzz(150);
    }
  }

  function drawPacket() {
    drawHeader("Latest packet");

    var rt = global.sleepstream;
    var pkt = parsePayload(rt && rt.lastPayload);

    if (!rt) {
      drawLines(["Service not running"], CONTENT_TOP_Y, 1);
      return;
    }

    if (!pkt || !pkt.sequence) {
      drawLines(["No payload yet"], CONTENT_TOP_Y, 1);
      return;
    }

    drawLines([
      "ver: " + pkt.version,
      "status: " + statusLabel(pkt.status),
      "consec: " + consecutiveLabel(pkt.consecutive),
      "source: " + sourceLabel(pkt.sourceMode),
      "seq: " + pkt.sequence,
      "ts: " + require("locale").date(new Date(pkt.timestampSec * 1000), 1) + " " + shortTime(pkt.timestampSec * 1000),
      "movement: " + formatMaybe(pkt.movement),
      "bpm: " + formatMaybe(pkt.bpm)
    ], CONTENT_TOP_Y, 9);
  }

  function drawConfig() {
    drawHeader("Config snapshot");

    var conf = (global.sleepstream && global.sleepstream.conf) || lib.loadSettings();

    drawLines([
      "preferHRM: " + !!conf.preferHRM,
      "deep/light: " + conf.deepTh + "/" + conf.lightTh,
      "hrm D/L: " + conf.hrmDeepTh + "/" + conf.hrmLightTh,
      "wearTemp: " + conf.wearTemp,
      "maxAwake m: " + ((conf.maxAwake / 6E4) | 0),
      "minConsec m: " + ((conf.minConsec / 6E4) | 0),
      "advWhenDisc: " + !!conf.advertiseWhenDisconnected,
      "namePrefix: " + conf.deviceNamePrefix
    ], CONTENT_TOP_Y, 9);
  }

  function drawLogTail() {
    drawHeader("Status log tail");

    var lines = readTailLines("sleepstream.log", 360, 9, ",");
    if (!lines.length) {
      drawLines(["No log lines"], CONTENT_TOP_Y, 1);
      return;
    }
    drawLines(lines.map(parseStatusLogLine), CONTENT_TOP_Y, 9);
  }

  function drawMeasurementTail() {
    drawHeader("Measurement log tail");

    var lines = readTailLines("sleepstream.measure.csv", 450, 9, ",");
    var parsed = lines.map(parseMeasureLogLine).filter(function(v) { return !!v; });
    if (parsed.length > 9) parsed = parsed.slice(parsed.length - 9);
    if (!parsed.length) {
      drawLines(["No measurement rows"], CONTENT_TOP_Y, 1);
      return;
    }
    drawLines(parsed, CONTENT_TOP_Y, 9);
  }

  function drawEventTail() {
    drawHeader("Event log tail");

    var lines = readTailLines("sleepstream.events.log", 420, 9, "|");
    if (!lines.length) {
      drawLines(["No event lines"], CONTENT_TOP_Y, 1);
      return;
    }
    drawLines(lines.map(parseEventLogLine), CONTENT_TOP_Y, 9);
  }

  function drawPage() {
    if (page === 0) drawRuntime();
    else if (page === 1) drawPacket();
    else if (page === 2) drawConfig();
    else if (page === 3) drawLogTail();
    else if (page === 4) drawMeasurementTail();
    else drawEventTail();

    drawFooter(page === 0 ? "BL touch: self-test" : "");
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
    touch: function(_b, xy) {
      // Bottom-left corner on runtime page triggers self-test packet send.
      if (page === 0 && xy && xy.x < 90 && xy.y > FOOTER_SPLIT_Y) {
        runSelfTest();
        drawPage();
        return;
      }
      nextPage();
    },
    swipe: function(h) {
      if (h < 0) page = (page + 1) % pageCount;
      else if (h > 0) page = (page + pageCount - 1) % pageCount;
      drawPage();
    }
  });

  // Optional hardware-button shortcut for targets exposing BTN2.
  if (typeof BTN2 !== "undefined") {
    setWatch(function() {
      if (page === 0) {
        runSelfTest();
        drawPage();
      }
    }, BTN2, { repeat: true, edge: "rising", debounce: 50 });
  }

  tick = setInterval(drawPage, 1000);
  E.on("kill", function() {
    if (tick) tick = clearInterval(tick);
  });

  drawPage();
})();
