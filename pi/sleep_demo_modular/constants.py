"""Single place to edit pins, BLE settings, and stage behavior."""

from __future__ import annotations


# -------------------- Hardware pins (edit here when wiring is final) --------------------
# Motor output pin and PWM frequency for vibration intensity control.
MOTOR_PIN = 23
MOTOR_PWM_HZ = 100

# Nebuliser relay/transistor control pin. If wiring is inverted, set active high False.
NEBULISER_PIN = 16
NEB_ACTIVE_HIGH = True

# NeoPixel data pin and number of LEDs in the ring/strip.
LED_PIN_NAME = "D18"
LED_COUNT = 3


# -------------------- BLE settings --------------------
# Nordic UART TX characteristic used by Bangle -> Pi notifications.
UART_TX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
# Scan/connect behavior for finding the watch.
BLE_NAME_PREFIX = "Bangle"
BLE_SCAN_TIMEOUT_S = 8.0
BLE_CONNECT_TIMEOUT_S = 20.0


# -------------------- BPM defaults --------------------
# Incoming BPM values are clamped to this range before being sent to Pure Data.
DEFAULT_BPM = 60
MIN_BPM = 30
MAX_BPM = 180


# -------------------- Pure Data settings --------------------
# Launch command and UDP target for soundscape control messages.
PUREDATA_ENABLED = True
# Open the patch created in this module folder.
# GUI mode is more reliable on some Pd builds than -nogui for initial audio setup.
PUREDATA_COMMAND = ["pd", "-open", "pi/sleep_demo_modular/windscape.pd"]
PUREDATA_WORKDIR = ""
# Force PD audio to ALSA device index 1 (speaker) on Raspberry Pi.
# Set False to let PD choose the system default backend/device.
PUREDATA_FORCE_ALSA = False
# Set to None to avoid brittle numeric device mapping across reboots.
PUREDATA_AUDIO_OUT_DEVICE = None
# Disable audio input device open (not needed for this patch and often missing on Pi).
PUREDATA_DISABLE_AUDIO_IN = True
# If forced output device fails, retry once with system default output.
PUREDATA_FALLBACK_TO_DEFAULT_OUTPUT = True
# Prefer a stable ALSA card name from "aplay -L" / "aplay -l".
# Example from your Pi output: "Device" (USB PnP Sound Device).
PUREDATA_ALSA_CARD = "Device"
# Capture PD stdout/stderr to a file so audio/startup errors are visible.
PUREDATA_CAPTURE_LOG = True
PUREDATA_LOG_FILE = "sleepstream_pd.log"
PUREDATA_UDP_HOST = "127.0.0.1"
PUREDATA_UDP_PORT = 9000


# -------------------- Fixed stage sequence --------------------
# Each stage runs in order for duration_s seconds.
# LED: pulse from color_a -> color_b while brightness sweeps between min_b and max_b.
# Motor: off or pulse (duty percent, on_s/off_s seconds).
# Neb: off or pulse (on_s/off_s seconds).
STAGES = [
    {
        # Awake: warm gentle light only, no physical stimulation.
        "name": "Awake",
        "duration_s": 20,
        "led": {
            "mode": "pulse",
            "color_a": (255, 90, 20),
            "color_b": (255, 40, 0),
            "min_b": 0.01,
            "max_b": 0.08,
            "step_s": 0.03,
        },
        "motor": {"mode": "off"},
        "neb": {"mode": "off"},
    },
    {
        # Light sleep: soft pulses with gentle motor and sparse nebuliser.
        "name": "Light",
        "duration_s": 20,
        "led": {
            "mode": "pulse",
            "color_a": (255, 70, 0),
            "color_b": (220, 25, 0),
            "min_b": 0.01,
            "max_b": 0.09,
            "step_s": 0.03,
        },
        "motor": {"mode": "pulse", "duty": 28, "on_s": 0.25, "off_s": 2.0},
        "neb": {"mode": "pulse", "on_s": 12.0, "off_s": 4.0, "warmup_s": 12.0},
    },
    {
        # Deep sleep: dim slower light, low motor activity, very occasional nebuliser.
        "name": "Deep",
        "duration_s": 20,
        "led": {
            "mode": "pulse",
            "color_a": (200, 12, 0),
            "color_b": (120, 0, 0),
            "min_b": 0.005,
            "max_b": 0.04,
            "step_s": 0.045,
        },
        "motor": {"mode": "pulse", "duty": 18, "on_s": 0.2, "off_s": 4.0},
        "neb": {"mode": "pulse", "on_s": 10.0, "off_s": 5.0, "warmup_s": 10.0},
    },
    {
        # REM: brighter/faster visual changes with stronger, more frequent stimulation.
        "name": "REM",
        "duration_s": 20,
        "led": {
            "mode": "pulse",
            "color_a": (255, 0, 0),
            "color_b": (255, 75, 0),
            "min_b": 0.02,
            "max_b": 0.16,
            "step_s": 0.01,
        },
        "motor": {"mode": "pulse", "duty": 65, "on_s": 0.35, "off_s": 0.9},
        "neb": {"mode": "pulse", "on_s": 16.0, "off_s": 2.0, "warmup_s": 16.0},
    },
]
