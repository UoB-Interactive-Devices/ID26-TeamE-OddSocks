// Debug app for Sleep Stream on Bangle.js 2.
// Two pages: live runtime state and status log tail.
// Tap or swipe to switch pages. Touch bottom-left on page 1 for self-test.

(function () {
  var lib = require("sleepstream.js");
  var LEFT_X = 4;
  var RIGHT_X = 173;
  var CONTENT_WIDTH = 168;
  var ROW_HEIGHT = 10;
  var CONTENT_TOP_Y = 64;
  var FOOTER_Y = 160;

  function statusLabel(v) {
    return ["unknown", "not_worn", "awake", "light", "deep"][v] || "?";
  }

  function consecutiveLabel(v) {
    return ["unknown", "no", "yes"][v] || "?";
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

  function fitText(text, maxWidth) {
    var s = text === undefined || text === null ? "" : "" + text;
    if (g.stringWidth(s) <= maxWidth) return s;
    while (s.length > 1 && g.stringWidth(s + "...") > maxWidth) {
      s = s.substr(0, s.length - 1);
    }
    return s + "...";
  }

  function drawLines(lines, startY) {
    var y = startY;
    g.setFont("6x8").setFontAlign(-1, -1);
    for (var i = 0; i < lines.length && i < 9; i++) {
      g.drawString(fitText(lines[i], CONTENT_WIDTH), LEFT_X, y);
      y += ROW_HEIGHT;
    }
  }

  function drawHeader(title) {
    g.reset().clearRect(0, 24, 175, 175)
      .setFont("6x8", 2).setFontAlign(-1, -1)
      .drawString("Sleep Stream", LEFT_X, 28)
      .setFont("6x8")
      .drawString(fitText(title, CONTENT_WIDTH), LEFT_X, 46)
      .drawLine(0, 58, 175, 58);
  }

  function drawFooter(hint) {
    g.reset().setFont("6x8").setFontAlign(-1, -1)
      .drawLine(0, FOOTER_Y, 175, FOOTER_Y);
    if (hint) g.drawString(fitText(hint, CONTENT_WIDTH), LEFT_X, 162);
    g.setFontAlign(1, 1)
      .drawString("tap/swipe " + (page + 1) + "/2", RIGHT_X, 173);
  }

  var page = 0;

  function drawRuntime() {
    drawHeader("Runtime / BLE");
    var rt = global.sleepstream;
    if (!rt) {
      drawLines(["Service not running", "Check Enabled in settings"], CONTENT_TOP_Y);
      drawFooter("");
      return;
    }
    drawLines([
      "conn: " + (!!rt.connected),
      "status: " + statusLabel(rt.status | 0),
      "consec: " + consecutiveLabel(rt.consecutive | 0),
      "seq: " + (rt.sequence | 0),
      "lastchk: " + shortDateTime((rt.info || {}).lastCheck),
      "lastchg: " + shortDateTime((rt.info || {}).lastChange),
      "asleep: " + shortTime((rt.info || {}).asleepSince),
      "awake: " + shortTime((rt.info || {}).awakeSince)
    ], CONTENT_TOP_Y);
    drawFooter("BL touch: self-test");
  }

  function drawLogTail() {
    drawHeader("Status log tail");
    var file = require("Storage").open("sleepstream.log", "r");
    var len = file.getLength();
    if (!len) {
      drawLines(["No log lines"], CONTENT_TOP_Y);
      drawFooter("");
      return;
    }
    var skip = len > 360 ? len - 360 : 0;
    if (skip) file.read(skip);
    var chunk = file.read(360) || "";
    var lines = chunk.trim().split("\n");
    if (lines[0] && !lines[0].includes(",")) lines.shift();
    if (lines.length > 9) lines = lines.slice(lines.length - 9);
    drawLines(lines.map(function (line) {
      var p = (line || "").split(",");
      if (p.length < 3) return line;
      var step = parseInt(p[0], 10);
      if (isNaN(step)) return line;
      return shortTime(step * 6E5) + " " + statusLabel(parseInt(p[1], 10)) + " / " + consecutiveLabel(parseInt(p[2], 10));
    }), CONTENT_TOP_Y);
    drawFooter("");
  }

  function drawPage() {
    if (page === 0) drawRuntime();
    else drawLogTail();
  }

  function runSelfTest() {
    if (!global.sleepstream || typeof global.sleepstream.sendUpdate !== "function") {
      Bangle.buzz(120);
      return;
    }
    global.sleepstream.sendUpdate({
      timestamp: Date.now(),
      status: global.sleepstream.status || 2,
      consecutive: global.sleepstream.consecutive || 1,
      movement: 111,
      bpm: 72
    }, 0);
    Bangle.buzz(60);
  }

  Bangle.loadWidgets();
  g.clear(true);
  Bangle.drawWidgets();

  Bangle.setUI({
    mode: "custom",
    back: load,
    touch: function (_b, xy) {
      if (page === 0 && xy && xy.x < 90 && xy.y > FOOTER_Y) {
        runSelfTest();
        drawPage();
        return;
      }
      page = (page + 1) % 2;
      drawPage();
    },
    swipe: function (h) {
      if (h < 0) page = (page + 1) % 2;
      else if (h > 0) page = (page + 2 - 1) % 2;
      drawPage();
    }
  });

  // Auto-refresh every 5s, but only while the screen is on.
  // When LCD is off (e.g. during sleep) the interval is cleared — zero battery cost.
  var tick;
  function startRefresh() {
    if (!tick) tick = setInterval(drawPage, 5000);
    drawPage();
  }
  function stopRefresh() {
    if (tick) { clearInterval(tick); tick = undefined; }
  }
  Bangle.on("lcdPower", function(on) {
    if (on) startRefresh(); else stopRefresh();
  });
  E.on("kill", stopRefresh);

  startRefresh();
})();
