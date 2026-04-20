#This has got all the constants you need, need to change any value just go here
from __future__ import annotations

from pathlib import Path


#Explaining most of these seems a lil silly, like yeah the function called APP_NAME is the name of the app, but I'll do it for consistency
APP_NAME = "sleep_pi_core"

# One watch in v1.

#These values for the BLE watch are good probably maybe
BLE_NAME_PREFIX = "Bangle"
BLE_SCAN_TIMEOUT_S = 8.0
BLE_CONNECT_TIMEOUT_S = 20.0
BLE_RETRY_SLEEP_S = 2.0

# Nordic UART Service, gives us unique pathways to communicate with the watch
#The first is watch to this, the other is vice versa
UART_TX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
UART_RX_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e" 

# If disconnected while running, stop the night after this timeout.
DISCONNECT_TIMEOUT_S = 15 * 60

# Protocol values we accept in the program.
VALID_STAGES = ["unknown", "not_worn", "awake", "light_sleep", "deep_sleep", "rem"]
VALID_STIMULI = ["sound", "smell", "light", "pi_motor", "watch_haptic"]

#Kinda vague since detailed use of numbers is in the respective program, but what they actually *do* should be clear
MAX_ON_SECONDS = {
    "sound": 30,
    "smell": 20,
    "light": 60,
    "pi_motor": 10,
    "watch_haptic": 5,
}
#We grab file path location later, so we need a default
DEFAULT_DB_PATH = Path(__file__).resolve().parent / "sleep_core.db"
