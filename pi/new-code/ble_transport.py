"""Minimal BLE transport.

This class handles scanning, connecting, reading newline JSON packets, and
writing JSON commands back to the watch (for haptic triggers).
"""

from __future__ import annotations

import asyncio
import json
import time
from typing import Any, Awaitable, Callable

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

#Many environments don't need or straight up cant install bleak, if it can't this lets the program still run
try:
    from bleak import BleakClient, BleakScanner
except ImportError:  # pragma: no cover
    BleakClient = None
    BleakScanner = None

#async stuff, we need to check if this stuff actually can be called
#Got it from here stackoverflow.com/questions/49360480/python-type-hinting-for-async-function-as-function-argument
PacketCallback = Callable[[dict[str, Any]], Awaitable[None]]
SignalCallback = Callable[[], Awaitable[None]]


class BleTransport:
    #There's a lot that needs to be defined here as our packets have a lot of detail on them, and we initialise with any known values
    def __init__(
        self,
        on_packet: PacketCallback,
        on_connected: SignalCallback,
        on_disconnected: SignalCallback,
        log,
    ):
        self.on_packet = on_packet
        self.on_connected = on_connected
        self.on_disconnected = on_disconnected
        self.log = log

        self.stop_event = asyncio.Event()
        self.connected = False
        self.last_disconnect_monotonic: float | None = None

        self._client = None
        self._write_lock = asyncio.Lock()

    #If running this from most IDE's, this message will come up. This lets us know the program actually works without having to set up bleak
    #Otherwise as long as we haven't recieved a command to stop
    async def run_forever(self) -> None:
        if BleakClient is None or BleakScanner is None:
            self.log.warning("Bleak is not installed; BLE mode disabled")
            await self.stop_event.wait()
            return

        #These functions are defined below
        while not self.stop_event.is_set():
            device = await self._scan_one()
            if device is None:
                await asyncio.sleep(BLE_RETRY_SLEEP_S)
                continue

            await self._connect_and_listen(device)
            if not self.stop_event.is_set():
                await asyncio.sleep(BLE_RETRY_SLEEP_S)

    async def _scan_one(self):
        #Scan for the device, just a connection algo basically
        found = await BleakScanner.discover(return_adv=True, timeout=BLE_SCAN_TIMEOUT_S)
        for device, adv in found.values():
            name = device.name or adv.local_name or ""
            if name.startswith(BLE_NAME_PREFIX):
                self.log.info("BLE found watch: %s", name)
                return device
        return None

    async def _connect_and_listen(self, device) -> None:
        #Has the functions to disconnect and timeout from the watch connection
        disconnected = asyncio.Event()
        buffer = ""

        def on_disconnect(_client):
            disconnected.set()

        async with BleakClient(device, timeout=BLE_CONNECT_TIMEOUT_S, disconnected_callback=on_disconnect) as client:
            self._client = client
            self.connected = True
            await self.on_connected()
            self.log.info("BLE connected: %s", getattr(device, "address", "unknown"))

            def on_notify(_sender, data):
                #This is all dealing with packets, the buffer is here because the json data isn't always in a consistent format
                nonlocal buffer
                buffer += bytes(data).decode("utf-8", errors="ignore")

                # We only support newline-delimited JSON for simplicity.
                while "\n" in buffer:
                    #This all processes each individual json, cuz the data can come in seperate lines and the like

                    line, buffer = buffer.split("\n", 1)
                    line = line.strip()
                    if not line:
                        #So we skip empty lines
                        continue
                    if line.startswith(">"):  # Watch REPL prompt prefix.
                        line = line[1:].strip()
                    if not line or not line.startswith("{"):
                        continue
                    try:
                        #This is try so that noise in the json can be discarded
                        payload = json.loads(line)
                    except json.JSONDecodeError:
                        self.log.debug("BLE rx malformed JSON line ignored: %s", line)
                        continue
                    if isinstance(payload, dict):
                        self.log.debug("BLE rx packet: %s", payload)
                        #This is set as a background task, async and all that
                        asyncio.create_task(self.on_packet(payload))

            await client.start_notify(UART_TX_UUID, on_notify)

            #Just a stopping function that can communicate with the running tasks.
            #There's two here cuz there's two seperate functions that are waiting to stop, so once one activates both need to be stopped
            stop_wait = asyncio.create_task(self.stop_event.wait())
            disc_wait = asyncio.create_task(disconnected.wait())
            done, pending = await asyncio.wait({stop_wait, disc_wait}, return_when=asyncio.FIRST_COMPLETED)
            for task in pending:
                task.cancel()

            await client.stop_notify(UART_TX_UUID)


            #This is for updating the internal state of the device
            self.connected = False
            self.last_disconnect_monotonic = time.monotonic()
            self._client = None
            await self.on_disconnected()

            if disc_wait in done:
                self.log.info("BLE disconnected")

    async def send_json(self, payload: dict[str, Any]) -> bool:
        if not self.connected or self._client is None:
            self.log.debug("BLE tx skipped (not connected): %s", payload)
            return False
        #As long as the connection is secure it writes the to the BLE data and locks it so it doesn't concurrently write things by mistake
        payload_json = json.dumps(payload, separators=(",", ":"))
        command = (
            "if(global.dreamstreamCmdBridge&&global.dreamstreamCmdBridge.handlePacket)"
            f"global.dreamstreamCmdBridge.handlePacket({payload_json})\n"
        )
        packet = command.encode("utf-8")
        async with self._write_lock:
            await self._client.write_gatt_char(UART_RX_UUID, packet, response=False)
        self.log.debug("BLE tx packet: %s", payload)
        return True

    #Obvious, stops the event, breaks the while loop
    def request_stop(self) -> None:
        self.stop_event.set()
