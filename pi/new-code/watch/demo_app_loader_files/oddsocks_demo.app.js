// OddSocks demo controller for Bangle.js 2.
// Sends only Pi control commands; sleep detection stays in the regular app.

(function () {
  var SRC = "oddsocks_demo";
  var STAGES = ["awake", "light_sleep", "deep_sleep", "rem"];
  var LABELS = ["AWAKE", "LIGHT", "DEEP", "REM"];
  var GAP = 4;
  var stageIndex = 0;
  var buttons = [];

  function nowSec() {
    return (Date.now() / 1000) | 0;
  }

  function selectedStage() {
    return STAGES[stageIndex] || STAGES[0];
  }

  function selectedLabel() {
    return LABELS[stageIndex] || LABELS[0];
  }

  function send(payload) {
    payload.src = SRC;
    payload.ts = nowSec();
    try {
      Bluetooth.println(JSON.stringify(payload));
      Bangle.buzz(40);
    } catch (e) {
      Bangle.buzz(160);
    }
    draw();
  }

  function runDemo() {
    send({
      cmd: "demo_run",
      stages: STAGES,
      dwell_sec: 0.35,
      cycles: 1,
      auto_start: true
    });
  }

  function sendStage() {
    var stage = selectedStage();
    send({ cmd: "stage", stage: stage, demo_fast: true });
  }

  function stopDemo() {
    send({ cmd: "stop" });
  }

  function nextStage() {
    stageIndex = (stageIndex + 1) % STAGES.length;
    draw();
    Bangle.buzz(60);
  }

  function makeButton(index, lines, action, color) {
    var app = Bangle.appRect || { x: 0, y: 24, x2: g.getWidth() - 1, y2: g.getHeight() - 1 };
    var areaH = app.y2 - app.y + 1;
    var height = ((areaH - GAP * 3) / 4) | 0;
    return {
      x: app.x,
      y: app.y + index * (height + GAP),
      w: app.x2 - app.x + 1,
      h: height,
      lines: lines,
      action: action,
      color: color
    };
  }

  function rebuildButtons() {
    buttons = [
      makeButton(0, ["RUN DEMO"], runDemo, "#1f8b4c"),
      makeButton(1, ["NEXT", selectedLabel()], nextStage, "#5146a6"),
      makeButton(2, ["SEND", selectedLabel()], sendStage, "#795548"),
      makeButton(3, ["STOP"], stopDemo, "#a22522")
    ];
  }

  function fitScale(text, maxWidth, preferred) {
    var size = preferred;
    while (size > 10) {
      g.setFont("Vector", size);
      if (g.stringWidth(text) <= maxWidth) return size;
      size -= 2;
    }
    return 10;
  }

  function drawButton(button) {
    var lines = button.lines;
    g.setColor(button.color);
    g.fillRect(button.x, button.y, button.x + button.w - 1, button.y + button.h - 1);

    var cx = button.x + (button.w >> 1);
    var cy = button.y + (button.h >> 1);
    var maxTextW = button.w - 14;
    g.setColor("#ffffff").setFontAlign(0, 0);

    if (lines.length === 1) {
      g.setFont("Vector", fitScale(lines[0], maxTextW, 20));
      g.drawString(lines[0], cx, cy);
    } else {
      var size = fitScale(lines[0].length > lines[1].length ? lines[0] : lines[1], maxTextW, 16);
      var dy = Math.max(10, (size * 0.75) | 0);
      g.setFont("Vector", size);
      g.drawString(lines[0], cx, cy - (dy >> 1));
      g.drawString(lines[1], cx, cy + (dy >> 1));
    }
  }

  function draw() {
    var app = Bangle.appRect || { x: 0, y: 24, x2: g.getWidth() - 1, y2: g.getHeight() - 1 };
    rebuildButtons();
    g.reset().clearRect(app.x, app.y, app.x2, app.y2);
    buttons.forEach(drawButton);
  }

  function hitTest(x, y) {
    for (var i = 0; i < buttons.length; i++) {
      var b = buttons[i];
      if (x >= b.x && x < b.x + b.w && y >= b.y && y < b.y + b.h) return b;
    }
    return null;
  }

  function onTouch(_button, xy) {
    if (!xy) return;
    rebuildButtons();
    var b = hitTest(xy.x, xy.y);
    if (b) b.action();
  }

  Bangle.loadWidgets();
  g.clear(true);
  Bangle.drawWidgets();
  Bangle.setUI({ mode: "custom", touch: onTouch, back: load });
  draw();
})();
