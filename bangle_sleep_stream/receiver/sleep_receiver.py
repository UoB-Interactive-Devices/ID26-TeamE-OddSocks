"""
File summary:
Linux asyncio BLE receiver daemon for Sleep Stream.
- Discovers and connects to the Bangle.js 2 watch.
- Subscribes to sleep update notifications.
- Decodes protocol v1 packets and persists rows to SQLite.
- Reconnects automatically with backoff and no manual intervention.
"""

from __future__ import annotations

import argparse
import asyncio
import logging
from logging.handlers import RotatingFileHandler
import signal
import sqlite3
import struct
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from bleak import BleakClient, BleakScanner

SERVICE_UUID = "12345678-1234-5678-1234-56789abc0000"
UPDATE_CHAR_UUID = "12345678-1234-5678-1234-56789abc0001"


@dataclass
class SleepPacket:
    version: int
    status: int
    consecutive: int
    source_mode: int
    sequence: int
    watch_ts_sec: int
    movement: Optional[int]
    bpm: Optional[int]


def decode_packet(data: bytearray) -> SleepPacket:
    if len(data) != 16:
        raise ValueError(f"invalid packet length {len(data)} (expected 16)")

    version, status, consecutive, source_mode, sequence, watch_ts, movement, bpm = struct.unpack(
        "<BBBBIIHH", data
    )
    if version != 1:
        raise ValueError(f"unsupported protocol version {version}")

    movement_val = None if movement == 0xFFFF else movement
    bpm_val = None if bpm == 0xFFFF else bpm

    return SleepPacket(
        version=version,
        status=status,
        consecutive=consecutive,
        source_mode=source_mode,
        sequence=sequence,
        watch_ts_sec=watch_ts,
        movement=movement_val,
        bpm=bpm_val,
    )


class ReceiverDaemon:
    """Owns BLE lifecycle, packet handling, and database persistence."""

    def __init__(
        self,
        name_prefix: str,
        db_path: Path,
        scan_timeout: float,
        connect_timeout: float,
        settle_seconds: float,
    ) -> None:
        self.name_prefix = name_prefix
        self.db_path = db_path
        self.scan_timeout = scan_timeout
        self.connect_timeout = connect_timeout
        self.settle_seconds = settle_seconds

        self.log = logging.getLogger("sleep_receiver")
        self.stop_event = asyncio.Event()
        self.disconnect_event = asyncio.Event()

        self.backoff_seconds = 2.0
        self.max_backoff_seconds = 30.0
        self.last_sequence: Optional[int] = None

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
            rssi = getattr(adv, "rssi", None)
            if rssi is None:
                rssi = getattr(dev, "rssi", -999)
            if rssi is None:
                rssi = -999
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

    def _persist_packet(self, pkt: SleepPacket, peer: str) -> None:
        recv_ts_ms = int(time.time() * 1000)

        if self.last_sequence is not None and pkt.sequence != self.last_sequence + 1:
            self.log.warning(
                "sequence gap: last=%s current=%s",
                self.last_sequence,
                pkt.sequence,
            )
        self.last_sequence = pkt.sequence

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
                    pkt.watch_ts_sec,
                    pkt.sequence,
                    pkt.status,
                    pkt.consecutive,
                    pkt.source_mode,
                    pkt.movement,
                    pkt.bpm,
                    peer,
                ),
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            self.log.info("db: duplicate packet seq=%s ts=%s", pkt.sequence, pkt.watch_ts_sec)

    def handle_packet(self, data: bytearray, peer: str, from_read: bool = False) -> None:
        pkt = decode_packet(data)
        source = "read" if from_read else "notify"
        self.log.info(
            "%s: seq=%d status=%d consecutive=%d source=%d ts=%d bpm=%s movement=%s",
            source,
            pkt.sequence,
            pkt.status,
            pkt.consecutive,
            pkt.source_mode,
            pkt.watch_ts_sec,
            pkt.bpm,
            pkt.movement,
        )
        self._persist_packet(pkt, peer)

    async def connect_and_stream(self, device) -> None:
        self.disconnect_event.clear()
        self.log.info("ble: connecting to %s", device.address)

        async with BleakClient(
            device,
            timeout=self.connect_timeout,
            disconnected_callback=self.on_disconnect,
        ) as client:
            await asyncio.sleep(self.settle_seconds)

            initial = await client.read_gatt_char(UPDATE_CHAR_UUID)
            self.handle_packet(initial, device.address, from_read=True)

            def notify_callback(_sender: int, data: bytearray) -> None:
                try:
                    self.handle_packet(data, device.address, from_read=False)
                except Exception as exc:  # keep stream alive on decode/db errors
                    self.log.exception("notify handling error: %s", exc)

            await client.start_notify(UPDATE_CHAR_UUID, notify_callback)
            self.log.info("ble: subscribed to notifications")

            await self.disconnect_event.wait()

            try:
                await client.stop_notify(UPDATE_CHAR_UUID)
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


def configure_logging(log_path: Optional[Path], debug: bool) -> None:
    handlers = [logging.StreamHandler()]

    if log_path:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=5))

    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        handlers=handlers,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sleep Stream BLE receiver")
    parser.add_argument("--name-prefix", default="BangleSleep", help="Watch BLE name prefix")
    parser.add_argument("--db-path", default="./sleepstream.db", help="SQLite path")
    parser.add_argument("--log-path", default="./sleepstream.log", help="Log file path")
    parser.add_argument("--scan-timeout", type=float, default=10.0, help="BLE scan timeout seconds")
    parser.add_argument("--connect-timeout", type=float, default=25.0, help="BLE connect timeout seconds")
    parser.add_argument("--settle-seconds", type=float, default=1.0, help="Delay after connect before IO")
    parser.add_argument("--debug", action="store_true", help="Enable debug logs")
    return parser.parse_args()


async def async_main(args: argparse.Namespace) -> None:
    daemon = ReceiverDaemon(
        name_prefix=args.name_prefix,
        db_path=Path(args.db_path),
        scan_timeout=args.scan_timeout,
        connect_timeout=args.connect_timeout,
        settle_seconds=args.settle_seconds,
    )

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, daemon.request_stop)
        except NotImplementedError:
            pass

    try:
        await daemon.run_forever()
    finally:
        daemon.close()


def main() -> None:
    args = parse_args()
    configure_logging(Path(args.log_path) if args.log_path else None, args.debug)
    asyncio.run(async_main(args))


if __name__ == "__main__":
    main()
