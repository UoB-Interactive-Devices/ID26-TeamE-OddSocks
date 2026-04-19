"""Central configuration for the simple overnight Pi controller.

Keep constants here so teammates can tune behavior without searching many files.
"""

from __future__ import annotations

from pathlib import Path


APP_NAME = "sleep_pi_core"

# One watch in v1.
BLE_NAME_PREFIX = "Bangle"
BLE_SCAN_TIMEOUT_S = 8.0
BLE_CONNECT_TIMEOUT_S = 20.0
BLE_RETRY_SLEEP_S = 2.0

# Nordic UART Service characteristics used by many watch apps.
UART_TX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"  # watch -> pi notify
UART_RX_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"  # pi -> watch write

# If disconnected while running, stop the night after this timeout.
DISCONNECT_TIMEOUT_S = 15 * 60

# Protocol values we currently accept.
VALID_STAGES = ["unknown", "not_worn", "awake", "light_sleep", "deep_sleep", "rem"]
VALID_STIMULI = ["sound", "smell", "light", "pi_motor", "watch_haptic"]

# Conservative safety values for future real hardware logic.
MAX_ON_SECONDS = {
    "sound": 30,
    "smell": 20,
    "light": 60,
    "pi_motor": 10,
    "watch_haptic": 5,
}

DEFAULT_DB_PATH = Path(__file__).resolve().parent / "sleep_core.db"
