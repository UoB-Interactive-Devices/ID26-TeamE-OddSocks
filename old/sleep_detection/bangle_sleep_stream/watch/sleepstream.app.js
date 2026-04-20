// Debug app for Sleep Stream on Bangle.js 2.
// Three pages: live runtime state, monitoring features, and status log tail.
// Tap or swipe to switch pages.
// Page 1: bottom-left = self-test, bottom-right = toggle monitoring.
// Page 2: live epoch features (only when monitoring).
// Page 3: status log tail.

(function () {
  var lib = require("sleepstream.js");
  var LEFT_X = 4;
  var RIGHT_X = 173;
  var CONTENT_WIDTH = 168;
  var ROW_HEIGHT = 10;
  var CONTENT_TOP_Y = 64;
  var FOOTER_Y = 160;

  function statusLabel(v) {
    return ["unknown", "not_worn", "awake", "light", "deep", "rem"][v] || "?";
  }

  function stageChar(v) {
    return ["?", "-", "W", "L", "D", "R"][v] || "?";
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
      .drawString("tap/swipe " + (page + 1) + "/3", RIGHT_X, 173);
  }

  var page = 0;
  var PAGE_COUNT = 4;

  function drawRuntime() {
    drawHeader("Runtime / BLE");
    var rt = global.sleepstream;
    if (!rt) {
      drawLines(["Service not running", "Check Enabled in settings"], CONTENT_TOP_Y);
      drawFooter("");
      return;
    }
    var monStr = rt.monitoring ? "ON" : "off";
    drawLines([
      "conn: " + (!!rt.connected),
      "status: " + statusLabel(rt.status | 0),
      "consec: " + consecutiveLabel(rt.consecutive | 0),
      "seq: " + (rt.sequence | 0),
      "monitor: " + monStr,
      "lastchk: " + shortDateTime((rt.info || {}).lastCheck),
      "lastchg: " + shortDateTime((rt.info || {}).lastChange),
      "asleep: " + shortTime((rt.info || {}).asleepSince)
    ], CONTENT_TOP_Y);
    drawFooter("Swipe to pg 4 for Controls");
  }

  function drawFeatures() {
    drawHeader("Epoch Features");
    var rt = global.sleepstream;
    if (!rt || !rt.monitoring) {
      drawLines(["Monitoring not active", "Start from page 1 (BR)"], CONTENT_TOP_Y);
      drawFooter("");
      return;
    }
    var f = rt.lastFeatures || {};
    var ctx = rt.nightCtx;
    var lines = [
      "stage: " + stageChar(rt.currentStage),
      "meanHR: " + (f.meanHR ? f.meanHR.toFixed(1) : "-"),
      "sdHR: " + (f.sdHR ? f.sdHR.toFixed(1) : "-"),
      "activity: " + (f.activity !== undefined ? f.activity.toFixed(4) : "-"),
      "hrCount: " + (f.hrCount || 0)
    ];
    if (ctx) {
      lines.push("hrP20: " + (ctx.hrP20() ? ctx.hrP20().toFixed(0) : "-"));
      lines.push("hrP50: " + (ctx.hrP50() ? ctx.hrP50().toFixed(0) : "-"));
      lines.push("minsSleep: " + (ctx.minutesSinceSleep(Date.now()) | 0));
    }
    drawLines(lines, CONTENT_TOP_Y);
    drawFooter("");
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

  function drawControls() {
    var rt = global.sleepstream;
    g.reset().clearRect(0, 24, 175, 175);
    g.setFont("6x8", 2).setFontAlign(0,0);
    
    // Top Half: Toggle Monitor (Blue if active, Green if inactive)
    var isMon = rt && rt.monitoring;
    g.setColor(isMon ? "#0000ff" : "#00ff00");
    g.fillRect(0, 24, 175, 96);
    g.setColor(isMon ? "#ffffff" : "#000000");
    g.drawString(isMon ? "STOP MONITOR" : "START MONITOR", 88, 60);

    // Bottom Half: Run Test (Red)
    g.setColor("#ff0000");
    g.fillRect(0, 98, 175, 175);
    g.setColor("#ffffff");
    g.drawString("SEND TEST", 88, 136);

    // Header overlap cleanup
    g.reset().setColor((g.theme && g.theme.bg) ? g.theme.bg : "#000000").fillRect(0,0,175,23);
    g.setColor((g.theme && g.theme.fg) ? g.theme.fg : "#ffffff").setFont("6x8", 1).setFontAlign(-1,-1);
    g.drawString("Controls (Swipe to exit)", 4, 8);
  }

  function drawPage() {
    if (page === 0) drawRuntime();
    else if (page === 1) drawFeatures();
    else if (page === 2) drawLogTail();
    else drawControls();
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

  function toggleMonitoring() {
    if (!global.sleepstream) {
      Bangle.buzz(120);
      return;
    }
    if (global.sleepstream.monitoring) {
      global.sleepstream.stopMonitoring();
    } else {
      global.sleepstream.startMonitoring();
    }
    drawPage();
  }

  Bangle.loadWidgets();
  g.clear(true);
  Bangle.drawWidgets();

  Bangle.setUI({
    mode: "custom",
    back: load,
    touch: function (btn, xy) {
      if (page === 3 && xy) {
        // Toggle if touched top half
        if (xy.y >= 24 && xy.y < 98) {
          toggleMonitoring();
          return;
        }
        // Test if touched bottom half
        if (xy.y >= 98) {
          runSelfTest();
          drawPage();
          return;
        }
      }
      page = (page + 1) % PAGE_COUNT;
      drawPage();
    },
    swipe: function (h) {
      if (h < 0) page = (page + 1) % PAGE_COUNT;
      else if (h > 0) page = (page + PAGE_COUNT - 1) % PAGE_COUNT;
      drawPage();
    }
  });

  // Auto-refresh every 5s, but only while the screen is on.
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
