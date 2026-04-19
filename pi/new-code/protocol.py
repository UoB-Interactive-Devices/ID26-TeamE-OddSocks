"""Packet normalization.

This file intentionally keeps packet parsing small and explicit so multiple
contributors can quickly understand what the app accepts.
"""

from __future__ import annotations

from typing import Any

from config import VALID_STAGES


_STAGE_ALIASES = {
    "light": "light_sleep",
    "deep": "deep_sleep",
}


def _normalize_stage(stage: str) -> str | None:
    value = stage.strip().lower()
    value = _STAGE_ALIASES.get(value, value)
    if value in VALID_STAGES:
        return value
    return None


def normalize_packet(packet: dict[str, Any]) -> dict[str, Any] | None:
    """Return a canonical packet dict or None if packet is irrelevant.

    Canonical forms:
    - {"kind": "start"}
    - {"kind": "stop"}
    - {"kind": "stage", "stage": "light_sleep"}
    """
    if not isinstance(packet, dict):
        return None

    cmd = str(packet.get("cmd", packet.get("command", ""))).strip().lower()
    if cmd == "start":
        return {"kind": "start"}
    if cmd == "stop":
        return {"kind": "stop"}

    # Accept explicit stage command and simple stage updates.
    if cmd == "stage":
        stage = _normalize_stage(str(packet.get("stage", "")))
        if stage:
            return {"kind": "stage", "stage": stage}

    if "stage" in packet:
        stage = _normalize_stage(str(packet.get("stage", "")))
        if stage:
            return {"kind": "stage", "stage": stage}

    # Also allow stage names directly in cmd for manual testing.
    stage_from_cmd = _normalize_stage(cmd)
    if stage_from_cmd:
        return {"kind": "stage", "stage": stage_from_cmd}

    return None
