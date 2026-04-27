"""Stage 'awake' + stimulus 'watch_haptic'.

This file owns the logic for this exact stage/stimulus combination.
"""

from __future__ import annotations


def _awake_haptic_payload(duration_ms: int = 80) -> dict:
    """Build a short haptic command understood by the installed watch bridge."""
    return {
        "cmd": "haptic",
        "event": "awake_detected",
        "haptic": {"ms": duration_ms},
    }


async def run(context: dict) -> tuple[str, str, bool]:
    """Send a short buzz to signal awake detection.

    context keys: stage, stimulus, send_watch_json, log
    """
    send_watch_json = context["send_watch_json"]
    log = context["log"]

    payload = _awake_haptic_payload(duration_ms=80)

    try:
        sent = await send_watch_json(payload)
    except Exception as exc:  # pragma: no cover
        log.warning("awake/watch_haptic send failed: %s", exc)
        return "awake_haptic_error", f"failed to send haptic command: {exc}", False

    if sent:
        return "awake_haptic_short_buzz", "sent 80ms haptic buzz for awake detection", True

    return "awake_haptic_skipped", "watch not connected; awake haptic not sent", False
