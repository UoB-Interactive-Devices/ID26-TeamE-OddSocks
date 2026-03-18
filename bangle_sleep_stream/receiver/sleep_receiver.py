"""
BLE receiver daemon for Sleep Stream.
Connects to Bangle.js 2 via UART, decodes JSON sleep updates, persists to SQLite.
Reconnects automatically with backoff.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
from logging.handlers import RotatingFileHandler
import signal
import sqlite3
import time
from pathlib import Path
from typing import Optional

from bleak import BleakClient, BleakScanner

UART_SERVICE_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
UART_TX_CHAR_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"


class ReceiverDaemon:
    """BLE lifecycle, packet handling, and database persistence."""

    def __init__(
        self,
        name_prefix: str,
        db_path: Path,
        scan_timeout: float,
        connect_timeout: float,
    ) -> None:
        self.name_prefix = name_prefix
        self.db_path = db_path
        self.scan_timeout = scan_timeout
        self.connect_timeout = connect_timeout

        self.log = logging.getLogger("sleep_receiver")
        self.stop_event = asyncio.Event()
        self.disconnect_event = asyncio.Event()

        self.backoff_seconds = 2.0
        self.max_backoff_seconds = 30.0
        self.last_sequence: Optional[int] = None
        self.uart_buffer = ""

        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA synchronous=NORMAL")
        self._init_db()

    def _init_db(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sleep_updates (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              recv_ts_ms INTEGER NOT NULL,
              watch_ts_sec INTEGER NOT NULL,
              sequence INTEGER NOT NULL,
              status INTEGER NOT NULL,
              consecutive INTEGER NOT NULL,
              source_mode INTEGER NOT NULL,
              movement INTEGER,
              bpm INTEGER,
              peer TEXT,
              UNIQUE(sequence, watch_ts_sec)
            )
            """
        )
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    def request_stop(self) -> None:
        self.stop_event.set()
        self.disconnect_event.set()

    async def scan_for_device(self):
        self.log.info("scan: looking for name prefix '%s'", self.name_prefix)
        discovered = await BleakScanner.discover(return_adv=True, timeout=self.scan_timeout)

        best = None
        best_rssi = -999
        for dev, adv in discovered.values():
            name = dev.name or adv.local_name or ""
            if not name.startswith(self.name_prefix):
                continue
            rssi = getattr(adv, "rssi", None) or getattr(dev, "rssi", -999) or -999
            if rssi > best_rssi:
                best = dev
                best_rssi = rssi

        if best:
            self.log.info("scan: selected %s (%s) rssi=%s", best.name, best.address, best_rssi)
        else:
            self.log.warning("scan: no matching device found")
        return best

    def on_disconnect(self, _client: BleakClient) -> None:
        self.log.warning("ble: disconnected")
        self.disconnect_event.set()

    def _persist(self, pkt: dict, peer: str) -> None:
        recv_ts_ms = int(time.time() * 1000)
        seq = pkt.get("seq", 0)

        if self.last_sequence is not None and seq != self.last_sequence + 1:
            if seq <= self.last_sequence:
                self.log.warning("sequence regressed/repeated: last=%s current=%s", self.last_sequence, seq)
            else:
                self.log.warning("sequence gap: last=%s current=%s", self.last_sequence, seq)
        self.last_sequence = seq

        try:
            self.conn.execute(
                """
                INSERT INTO sleep_updates (
                  recv_ts_ms, watch_ts_sec, sequence, status, consecutive,
                  source_mode, movement, bpm, peer
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    recv_ts_ms,
                    int(pkt.get("ts", 0)),
                    seq,
                    int(pkt.get("status", 0)),
                    int(pkt.get("consecutive", 0)),
                    int(pkt.get("source_mode", 0)),
                    pkt.get("movement"),
                    pkt.get("bpm"),
                    peer,
                ),
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            self.log.info("db: duplicate packet seq=%s", seq)

    def handle_uart_line(self, line: str, peer: str) -> None:
        line = line.strip()
        if not line:
            return
        try:
            obj = json.loads(line)
        except Exception:
            return
        if obj.get("t") != "sleepstream":
            return

        self.log.info(
            "uart: seq=%d status=%d consecutive=%d source=%d ts=%d bpm=%s movement=%s",
            obj.get("seq", 0), obj.get("status", 0), obj.get("consecutive", 0),
            obj.get("source_mode", 0), obj.get("ts", 0), obj.get("bpm"), obj.get("movement"),
        )
        self._persist(obj, peer)

    def _drain_uart_buffer(self, peer: str) -> None:
        while self.uart_buffer:
            idx_n = self.uart_buffer.find("\n")
            idx_r = self.uart_buffer.find("\r")
            line_endings = [i for i in (idx_n, idx_r) if i >= 0]
            if line_endings:
                split_idx = min(line_endings)
                line = self.uart_buffer[:split_idx]
                self.uart_buffer = self.uart_buffer[split_idx + 1:]
                self.handle_uart_line(line, peer)
                continue

            chunk = self.uart_buffer.lstrip()
            if not chunk.startswith("{"):
                self.uart_buffer = ""
                return
            try:
                _obj, end_idx = json.JSONDecoder().raw_decode(chunk)
            except json.JSONDecodeError:
                return
            self.uart_buffer = chunk[end_idx:]
            self.handle_uart_line(json.dumps(_obj), peer)

    async def connect_and_stream(self, device) -> None:
        self.disconnect_event.clear()
        self.log.info("ble: connecting to %s", device.address)

        async with BleakClient(
            device, timeout=self.connect_timeout, disconnected_callback=self.on_disconnect,
        ) as client:
            await asyncio.sleep(1.0)
            self.uart_buffer = ""

            def uart_callback(_sender: int, data: bytearray) -> None:
                try:
                    self.uart_buffer += bytes(data).decode("utf-8", errors="ignore")
                    self._drain_uart_buffer(device.address)
                except Exception as exc:
                    self.log.exception("uart handling error: %s", exc)

            await client.start_notify(UART_TX_CHAR_UUID, uart_callback)
            self.log.info("ble: subscribed to UART notifications")
            await self.disconnect_event.wait()

            try:
                await client.stop_notify(UART_TX_CHAR_UUID)
            except Exception:
                pass

    async def run_forever(self) -> None:
        while not self.stop_event.is_set():
            try:
                device = await self.scan_for_device()
                if not device:
                    await asyncio.sleep(self.backoff_seconds)
                    self.backoff_seconds = min(self.backoff_seconds * 1.5, self.max_backoff_seconds)
                    continue
                await self.connect_and_stream(device)
                self.backoff_seconds = 2.0
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                self.log.exception("main loop error: %s", exc)
                await asyncio.sleep(self.backoff_seconds)
                self.backoff_seconds = min(self.backoff_seconds * 1.5, self.max_backoff_seconds)


def main() -> None:
    parser = argparse.ArgumentParser(description="Sleep Stream BLE receiver")
    parser.add_argument("--name-prefix", default="Bangle", help="Watch BLE name prefix")
    parser.add_argument("--db-path", default="./sleepstream.db", help="SQLite path")
    parser.add_argument("--log-path", default="./sleepstream.log", help="Log file path")
    parser.add_argument("--scan-timeout", type=float, default=10.0, help="BLE scan timeout seconds")
    parser.add_argument("--connect-timeout", type=float, default=25.0, help="BLE connect timeout seconds")
    parser.add_argument("--debug", action="store_true", help="Enable debug logs")
    args = parser.parse_args()

    handlers = [logging.StreamHandler()]
    if args.log_path:
        Path(args.log_path).parent.mkdir(parents=True, exist_ok=True)
        handlers.append(RotatingFileHandler(args.log_path, maxBytes=1_000_000, backupCount=5))

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        handlers=handlers,
    )

    daemon = ReceiverDaemon(
        name_prefix=args.name_prefix,
        db_path=Path(args.db_path),
        scan_timeout=args.scan_timeout,
        connect_timeout=args.connect_timeout,
    )

    loop = asyncio.new_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, daemon.request_stop)
        except NotImplementedError:
            pass

    try:
        loop.run_until_complete(daemon.run_forever())
    finally:
        daemon.close()


if __name__ == "__main__":
    main()
