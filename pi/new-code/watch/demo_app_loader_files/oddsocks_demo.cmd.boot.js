// Tiny Pi-to-watch command bridge for the demo controller.
// It only handles haptic/buzz commands used by the demo stimuli.

(function () {
  function clamp(v, lo, hi) {
    if (v < lo) return lo;
    if (v > hi) return hi;
    return v;
  }

  function toInt(v, fallback) {
    if (typeof v === "number" && isFinite(v)) return v | 0;
    return fallback;
  }

  function buzzFrom(payload) {
    var haptic = payload.haptic || {};
    var ms = toInt(haptic.ms || haptic.duration || payload.ms || payload.duration || payload.buzz, 120);
    var strength = haptic.strength !== undefined ? haptic.strength : haptic.intensity;

    if (strength === undefined) strength = payload.strength !== undefined ? payload.strength : payload.intensity;
    if (typeof strength !== "number" || !isFinite(strength)) strength = 1;
    if (strength > 1) strength = strength / 100;

    Bangle.buzz(clamp(ms, 20, 2000), clamp(strength, 0, 1));
  }

  function handlePacket(payload) {
    if (!payload || typeof payload !== "object") return;

    var cmd = (payload.cmd || payload.command || "").toString().toLowerCase();
    if (cmd === "buzz" || cmd === "haptic" || payload.haptic || payload.buzz) {
      buzzFrom(payload);
    }
  }

  global.oddsocksDemoCmdBridge = { handlePacket: handlePacket };
})();
