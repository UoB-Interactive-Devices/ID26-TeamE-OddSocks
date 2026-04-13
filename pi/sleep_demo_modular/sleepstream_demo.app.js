// Minimal Bangle.js 2 demo controller for sleep_demo_modular.
// Sends control commands + continuous BPM packets over BLE UART JSON.

var stages = ["awake", "light", "deep", "rem"];
var stageIndex = 0;
var connected = false;
var bpmTimer = null;
var lastBpm = 60;

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
  var bpm = clamp((lastBpm | 0) || 60, 30, 180);
  send({ cmd: "hr", bpm: bpm, ts: Math.floor(Date.now() / 1000) });
}

function startBpmStreaming() {
  if (bpmTimer) return;

  Bangle.setHRMPower(1, "sleepstream_demo");
  Bangle.removeListener("HRM", onHrm);
  Bangle.on("HRM", onHrm);

  // Send immediately, then every second.
  sendBpm();
  bpmTimer = setInterval(sendBpm, 1000);
}

function stopBpmStreaming() {
  if (bpmTimer) {
    clearInterval(bpmTimer);
    bpmTimer = null;
  }
  Bangle.removeListener("HRM", onHrm);
  Bangle.setHRMPower(0, "sleepstream_demo");
}

function onHrm(hrm) {
  if (!hrm) return;
  if (hrm.bpm && hrm.bpm > 0) {
    lastBpm = hrm.bpm;
  }
}

function connectToggle() {
  connected = !connected;
  if (connected) {
    startBpmStreaming();
    send({ cmd: "connect", ts: Math.floor(Date.now() / 1000) });
  } else {
    stopBpmStreaming();
    send({ cmd: "disconnect", ts: Math.floor(Date.now() / 1000) });
  }
  showMenu();
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
  showMenu();
}

function prevStage() {
  if (!connected) return;
  stageIndex = clamp(stageIndex - 1, 0, stages.length - 1);
  send({ cmd: "stage", stage: stages[stageIndex], ts: Math.floor(Date.now() / 1000) });
  showMenu();
}

function showMenu() {
  E.showMenu({
    "": { title: "Demo Control" },
    "Status": {
      value: connected ? ("ON / " + stages[stageIndex].toUpperCase()) : "OFF",
      format: function(v) { return v; }
    },
    "Connect/Disconnect": function() { connectToggle(); },
    "Start Demo": function() { startDemo(); },
    "Prev Stage": function() { prevStage(); },
    "Next Stage": function() { nextStage(); },
    "Stop Demo": function() { stopDemo(); },
    "Exit": function() {
      stopBpmStreaming();
      E.showMenu();
      load();
    }
  });
}

Bangle.loadWidgets();
Bangle.drawWidgets();
showMenu();
