from __future__ import annotations

import asyncio
import json

from old.sleep_demo_modular.constants import BLE_CONNECT_TIMEOUT_S, BLE_NAME_PREFIX, BLE_SCAN_TIMEOUT_S, UART_TX_UUID

try:
    from bleak import BleakClient, BleakScanner
except ImportError:  # pragma: no cover
    BleakClient = None
    BleakScanner = None


def _extract_json_objects(buffer: str) -> tuple[list[dict], str]:
    """Parse newline JSON and concatenated JSON objects from a stream buffer."""
    out: list[dict] = []

    while buffer:
        buffer = buffer.lstrip()
        if not buffer:
            break

        newline_idx = min((i for i in (buffer.find("\n"), buffer.find("\r")) if i >= 0), default=-1)

        if buffer.startswith("{"):
            try:
                obj, end = json.JSONDecoder().raw_decode(buffer)
                if isinstance(obj, dict):
                    out.append(obj)
                buffer = buffer[end:]
                continue
            except json.JSONDecodeError:
                pass

        if newline_idx >= 0:
            line = buffer[:newline_idx].strip()
            buffer = buffer[newline_idx + 1 :]
            if not line:
                continue
            try:
                obj = json.loads(line)
                if isinstance(obj, dict):
                    out.append(obj)
            except Exception:
                continue
            continue

        break

    return out, buffer


class BleListener:
    def __init__(self, on_packet, log):
        self.on_packet = on_packet
        self.log = log
        self.stop_event = asyncio.Event()

    async def run(self):
        if BleakClient is None or BleakScanner is None:
            self.log.warning("Bleak not installed; BLE disabled")
            await self.stop_event.wait()
            return

        while not self.stop_event.is_set():
            try:
                dev = await self._scan_for_bangle()
                if dev is None:
                    await asyncio.sleep(2.0)
                    continue
                await self._connect_and_listen(dev)
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                self.log.warning("BLE loop error: %s", exc)
                await asyncio.sleep(2.0)

    async def _scan_for_bangle(self):
        found = await BleakScanner.discover(return_adv=True, timeout=BLE_SCAN_TIMEOUT_S)
        best = None
        best_rssi = -999

        for dev, adv in found.values():
            name = dev.name or adv.local_name or ""
            if not name.startswith(BLE_NAME_PREFIX):
                continue
            rssi = getattr(adv, "rssi", None) or getattr(dev, "rssi", -999) or -999
            if rssi > best_rssi:
                best = dev
                best_rssi = rssi

        if best:
            self.log.info("Found BLE device: %s", best.name)
        return best

    async def _connect_and_listen(self, dev):
        disconnected = asyncio.Event()
        buffer = ""

        def on_disconnect(_client):
            disconnected.set()

        async with BleakClient(dev, timeout=BLE_CONNECT_TIMEOUT_S, disconnected_callback=on_disconnect) as client:
            self.log.info("Connected to %s", dev.name)

            def on_notify(_sender, data):
                nonlocal buffer
                buffer += bytes(data).decode("utf-8", errors="ignore")
                packets, buffer = _extract_json_objects(buffer)
                for pkt in packets:
                    asyncio.create_task(self.on_packet(pkt))

            await client.start_notify(UART_TX_UUID, on_notify)

            stop_wait = asyncio.create_task(self.stop_event.wait())
            disc_wait = asyncio.create_task(disconnected.wait())
            done, pending = await asyncio.wait({stop_wait, disc_wait}, return_when=asyncio.FIRST_COMPLETED)
            for p in pending:
                p.cancel()

            try:
                await client.stop_notify(UART_TX_UUID)
            except Exception:
                pass

            if disc_wait in done:
                self.log.info("BLE disconnected")
