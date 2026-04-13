// Minimal Bangle.js 2 demo controller for sleep_demo_modular.
// Two pages:
// 1) connect/disconnect + status actions
// 2) start/prev/next/stop in a 2x2 button grid

var stages = ["awake", "light", "deep", "rem"];
var stageIndex = 0;
var connected = false;
var bpmTimer = null;
var lastBpm = 60;
var page = 0; // 0 = connect/status, 1 = demo controls
var buttons = [];
var appRect;
var headerH = 18;
var footerH = 16;

function clamp(v, lo, hi) {
  return Math.max(lo, Math.min(hi, v));
}

function send(obj) {
  try {
    Bluetooth.println(JSON.stringify(obj));
  } catch (e) {
    print("send failed", e);
  }
}

function sendBpm() {
  if (!connected) return;
  var bpm = clamp((lastBpm | 0) || 60, 30, 180);
  send({ cmd: "hr", bpm: bpm, ts: Math.floor(Date.now() / 1000) });
}

function onHrm(hrm) {
  if (!hrm) return;
  if (hrm.bpm && hrm.bpm > 0) lastBpm = hrm.bpm;
}

function connect() {
  if (connected) return;
  connected = true;
  Bangle.setHRMPower(1, "sleepstream_demo");
  Bangle.removeListener("HRM", onHrm);
  Bangle.on("HRM", onHrm);
  send({ cmd: "connect", ts: Math.floor(Date.now() / 1000) });
  sendBpm();
  if (!bpmTimer) bpmTimer = setInterval(sendBpm, 1000);
  draw();
}

function disconnect() {
  if (!connected) return;
  connected = false;
  if (bpmTimer) {
    clearInterval(bpmTimer);
    bpmTimer = null;
  }
  Bangle.removeListener("HRM", onHrm);
  Bangle.setHRMPower(0, "sleepstream_demo");
  send({ cmd: "disconnect", ts: Math.floor(Date.now() / 1000) });
  draw();
}

function startDemo() {
  if (!connected) return;
  send({ cmd: "start", ts: Math.floor(Date.now() / 1000) });
}

function stopDemo() {
  if (!connected) return;
  send({ cmd: "stop", ts: Math.floor(Date.now() / 1000) });
}

function nextStage() {
  if (!connected) return;
  stageIndex = clamp(stageIndex + 1, 0, stages.length - 1);
  send({ cmd: "stage", stage: stages[stageIndex], ts: Math.floor(Date.now() / 1000) });
  draw();
}

function prevStage() {
  if (!connected) return;
  stageIndex = clamp(stageIndex - 1, 0, stages.length - 1);
  send({ cmd: "stage", stage: stages[stageIndex], ts: Math.floor(Date.now() / 1000) });
  draw();
}

function currentStatus() {
  return (connected ? "ON" : "OFF") + "  " + stages[stageIndex].toUpperCase() + "  BPM " + ((lastBpm | 0) || 60);
}

function pageTitle() {
  return page === 0 ? "Connect / Status" : "Demo Controls";
}

function makeButtons() {
  var gap = 6;
  var pad = 4;
  var innerW = (appRect.x2 - appRect.x + 1) - pad * 2;
  var innerTop = appRect.y + headerH;
  var innerBottom = appRect.y2 - footerH;
  var innerH = (innerBottom - innerTop + 1) - pad * 2;
  var size = Math.floor(Math.min((innerW - gap) / 2, (innerH - gap) / 2));
  var totalW = size * 2 + gap;
  var totalH = size * 2 + gap;
  var x0 = appRect.x + Math.floor(((appRect.x2 - appRect.x + 1) - totalW) / 2);
  var y0 = innerTop + Math.floor(((innerBottom - innerTop + 1) - totalH) / 2);

  var labels;
  var handlers;
  if (page === 0) {
    labels = [
      ["CONNECT"],
      ["DISCONNECT"],
      [connected ? "STATUS ON" : "STATUS OFF", "BPM " + ((lastBpm | 0) || 60)],
      ["PAGE", "2 ->"],
    ];
    handlers = [connect, disconnect, function() {}, function() { page = 1; draw(); }];
  } else {
    labels = [["START"], ["PREV"], ["NEXT"], ["STOP"]];
    handlers = [startDemo, prevStage, nextStage, stopDemo];
  }

  return [
    { x: x0, y: y0, w: size, h: size, lines: labels[0], onPress: handlers[0] },
    { x: x0 + size + gap, y: y0, w: size, h: size, lines: labels[1], onPress: handlers[1] },
    { x: x0, y: y0 + size + gap, w: size, h: size, lines: labels[2], onPress: handlers[2] },
    { x: x0 + size + gap, y: y0 + size + gap, w: size, h: size, lines: labels[3], onPress: handlers[3] },
  ];
}

function fitTextScale(text, maxWidth, preferred) {
  var size = preferred;
  while (size > 10) {
    g.setFont("Vector", size);
    if (g.stringWidth(text) <= maxWidth) return size;
    size -= 2;
  }
  return 10;
}

function cropText(text, maxWidth) {
  var out = text;
  g.setFont("Vector", 14);
  if (g.stringWidth(out) <= maxWidth) return out;
  while (out.length > 1 && g.stringWidth(out + "...") > maxWidth) {
    out = out.slice(0, -1);
  }
  return out + "...";
}

function drawButton(b) {
  g.setColor(0.12, 0.12, 0.12);
  g.fillRect(b.x, b.y, b.x + b.w, b.y + b.h);
  g.setColor(0.7, 0.7, 0.7);
  g.drawRect(b.x, b.y, b.x + b.w, b.y + b.h);
  g.setColor(1, 1, 1);
  g.drawRect(b.x + 1, b.y + 1, b.x + b.w - 1, b.y + b.h - 1);

  var maxTextW = b.w - 12;
  var cx = b.x + (b.w >> 1);
  var cy = b.y + (b.h >> 1);

  if (b.lines.length <= 1) {
    var s1 = fitTextScale(b.lines[0], maxTextW, 24);
    g.setFont("Vector", s1);
    g.setFontAlign(0, 0);
    g.drawString(b.lines[0], cx, cy);
  } else if (b.lines.length === 2) {
    var l0 = b.lines[0];
    var l1 = b.lines[1];
    var s2 = fitTextScale((l0.length > l1.length ? l0 : l1), maxTextW, 20);
    g.setFont("Vector", s2);
    var dy = Math.max(10, Math.floor(s2 * 0.9));
    g.setFontAlign(0, 0);
    g.drawString(l0, cx, cy - dy / 2);
    g.drawString(l1, cx, cy + dy / 2);
  } else {
    g.setFont("Vector", 12);
    g.setFontAlign(0, 0);
    g.drawString(b.lines[0], cx, cy - 16);
    g.drawString(b.lines[1], cx, cy);
    g.drawString(b.lines[2], cx, cy + 16);
  }
}

function draw() {
  g.clearRect(appRect.x, appRect.y, appRect.x2, appRect.y2);
  buttons = makeButtons();
  buttons.forEach(drawButton);

  // Dedicated header and footer bands (no overlap with buttons).
  g.setColor(0, 0, 0);
  g.fillRect(appRect.x, appRect.y, appRect.x2, appRect.y + headerH - 1);
  g.fillRect(appRect.x, appRect.y2 - footerH + 1, appRect.x2, appRect.y2);

  g.setColor(1, 1, 1);
  g.setFont("Vector", 13);
  g.setFontAlign(0, 0);
  g.drawString(pageTitle(), (appRect.x + appRect.x2) >> 1, appRect.y + (headerH >> 1));

  g.setFontAlign(-1, 0);
  g.setFont("Vector", 12);
  g.drawString(cropText(currentStatus(), appRect.x2 - appRect.x - 4), appRect.x + 2, appRect.y2 - (footerH >> 1));
}

function hitTest(x, y) {
  for (var i = 0; i < buttons.length; i++) {
    var b = buttons[i];
    if (x >= b.x && x <= (b.x + b.w) && y >= b.y && y <= (b.y + b.h)) return b;
  }
  return null;
}

function onTouch(_button, xy) {
  var b = hitTest(xy.x, xy.y);
  if (b && b.onPress) b.onPress();
}

function onSwipe(dir) {
  if (dir < 0) page = 1;
  if (dir > 0) page = 0;
  draw();
}

function onExit() {
  disconnect();
  Bangle.setUI();
  load();
}

// Use the app drawing region provided by Espruino/Bangle APIs.
appRect = Bangle.appRect || { x: 0, y: 0, x2: g.getWidth() - 1, y2: g.getHeight() - 1 };
Bangle.setUI({ mode: "custom", touch: onTouch, swipe: onSwipe, btn: onExit });
draw();
