// Dreamstream operational app for Bangle.js 2.
// One-screen UX: Start/Stop tracking, live metrics, and last Pi command.

(function () {
  var Storage = require("Storage");
  var locale = require("locale");
  var CMD_STORE = "dreamstream.cmd.json";
  var BTN_TOP = 126;
  var BTN_BOTTOM = 172;

  function statusLabel(v) {
    return ["unknown", "not_worn", "awake", "light", "deep", "rem"][v | 0] || "?";
  }

  function stageChar(v) {
    return ["?", "-", "W", "L", "D", "R"][v | 0] || "?";
  }

  function fit(s, w) {
    var t = s === undefined || s === null ? "" : "" + s;
    if (g.stringWidth(t) <= w) return t;
    while (t.length > 1 && g.stringWidth(t + "...") > w) t = t.slice(0, -1);
    return t + "...";
  }

  function shortClock(ms) {
    if (!ms) return "-";
    return locale.time(new Date(ms), 1);
  }

  function sendControl(cmd) {
    var pkt = {
      cmd: cmd,
      src: "dreamstream",
      ts: (Date.now() / 1000) | 0
    };
    try {
      Bluetooth.println(JSON.stringify(pkt));
    } catch (e) {
      return false;
    }
    return true;
  }

  function getRuntime() {
    return global.sleepstream;
  }

  function ensureCmdBridge() {
    if (global.dreamstreamCmdBridge && global.dreamstreamCmdBridge.listener) return;
    try {
      var src = Storage.read("dreamstream.cmd.boot.js");
      if (src) eval(src);
    } catch (e) {
    }
  }

  var cachedLastCmd = Storage.readJSON(CMD_STORE, true) || null;

  function getLastCmd(rt) {
    return global.dreamstreamLastCmd || (rt && rt.lastCommand) || cachedLastCmd || null;
  }

  function startTracking() {
    var rt = getRuntime();
    if (!rt) {
      Bangle.buzz(120);
      return;
    }
    sendControl("start");
    if (!rt.monitoring) rt.startMonitoring();
    Bangle.buzz(50);
    draw();
  }

  function stopTracking() {
    var rt = getRuntime();
    if (!rt) {
      Bangle.buzz(120);
      return;
    }
    sendControl("stop");
    if (rt.monitoring) rt.stopMonitoring();
    Bangle.buzz(50);
    draw();
  }

  function toggleTracking() {
    var rt = getRuntime();
    if (!rt) {
      Bangle.buzz(120);
      return;
    }
    if (rt.monitoring) stopTracking();
    else startTracking();
  }

  function drawButton(active) {
    g.setColor(active ? "#a22522" : "#1f8b4c");
    g.fillRect(8, BTN_TOP, 167, BTN_BOTTOM);
    g.setColor("#ffffff").setFont("6x8", 2).setFontAlign(0, 0);
    g.drawString(active ? "STOP TRACKING" : "START TRACKING", 88, (BTN_TOP + BTN_BOTTOM) >> 1);
  }

  function draw() {
    var rt = getRuntime();
    var f = rt && rt.lastFeatures ? rt.lastFeatures : {};
    var cmd = getLastCmd(rt);

    g.reset().clearRect(0, 24, 175, 175);
    g.setFont("6x8", 2).setFontAlign(-1, -1);
    g.drawString("Dreamstream", 4, 28);
    g.setFont("6x8").setFontAlign(-1, -1);
    g.drawLine(0, 48, 175, 48);

    if (!rt) {
      g.drawString("service: not running", 4, 56);
      g.drawString("check dreamstream.boot.js", 4, 68);
      drawButton(false);
      return;
    }

    var y = 56;
    g.drawString("conn " + (!!rt.connected) + "  monitor " + (rt.monitoring ? "ON" : "off"), 4, y); y += 10;
    g.drawString("stage " + statusLabel(rt.status) + " (" + stageChar(rt.currentStage) + ")", 4, y); y += 10;
    g.drawString("seq " + (rt.sequence | 0) + "  consec " + (rt.consecutive | 0), 4, y); y += 10;
    g.drawString("move " + (f.activity !== undefined ? f.activity.toFixed(4) : "-") + "  bpm " + (f.meanHR ? f.meanHR.toFixed(1) : "-"), 4, y); y += 10;
    g.drawString("sdhr " + (f.sdHR ? f.sdHR.toFixed(1) : "-") + "  hrN " + (f.hrCount | 0), 4, y); y += 10;

    if (cmd) {
      var payload = cmd.payload ? JSON.stringify(cmd.payload) : JSON.stringify(cmd);
      g.drawString("pi cmd @ " + shortClock(cmd.ts), 4, y); y += 10;
      g.drawString(fit(payload, 168), 4, y);
    } else {
      g.drawString("pi cmd: none yet", 4, y);
    }

    drawButton(!!rt.monitoring);
  }

  var tick;
  function startRefresh() {
    if (!tick) tick = setInterval(draw, 2000);
    draw();
  }
  function stopRefresh() {
    if (tick) {
      clearInterval(tick);
      tick = undefined;
    }
  }

  function onLcdPower(on) {
    if (on) startRefresh();
    else stopRefresh();
  }

  function onTouch(_btn, xy) {
    if (xy && xy.y >= BTN_TOP && xy.y <= BTN_BOTTOM) {
      toggleTracking();
      return;
    }
    draw();
  }

  Bangle.loadWidgets();
  g.clear(true);
  Bangle.drawWidgets();
  ensureCmdBridge();

  Bangle.setUI({
    mode: "custom",
    back: load,
    touch: onTouch,
    btn: function () {
      toggleTracking();
    },
    remove: function () {
      stopRefresh();
      Bangle.removeListener("lcdPower", onLcdPower);
      E.removeListener("kill", stopRefresh);
    }
  });

  Bangle.on("lcdPower", onLcdPower);
  E.on("kill", stopRefresh);
  startRefresh();
})();
