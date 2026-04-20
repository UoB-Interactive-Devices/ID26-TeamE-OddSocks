"""Minimal SQLite helper.

The database is intentionally simple:
- sessions: one row per night session
- raw_packets: every accepted inbound packet
- sleep_updates: structured sleepstream packets from the watch
- stimulus_events: every output action attempt
"""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class Database:
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA journal_mode=WAL")
        self._init_schema()

    def _init_schema(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_ts_utc TEXT NOT NULL,
                end_ts_utc TEXT,
                stop_reason TEXT
            )
            """
        )
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS raw_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER,
                recv_ts_utc TEXT NOT NULL,
                packet_kind TEXT,
                stage TEXT,
                payload_json TEXT NOT NULL,
                FOREIGN KEY(session_id) REFERENCES sessions(id)
            )
            """
        )
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS stimulus_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER,
                event_ts_utc TEXT NOT NULL,
                stage TEXT,
                stimulus TEXT NOT NULL,
                action TEXT NOT NULL,
                details TEXT,
                success INTEGER NOT NULL,
                FOREIGN KEY(session_id) REFERENCES sessions(id)
            )
            """
        )
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sleep_updates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER,
                recv_ts_utc TEXT NOT NULL,
                watch_ts_sec INTEGER NOT NULL,
                sequence INTEGER NOT NULL,
                status INTEGER NOT NULL,
                consecutive INTEGER,
                source_mode INTEGER,
                movement INTEGER,
                bpm INTEGER,
                sdhr REAL,
                UNIQUE(sequence, watch_ts_sec),
                FOREIGN KEY(session_id) REFERENCES sessions(id)
            )
            """
        )
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_raw_packets_session ON raw_packets(session_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_stimulus_events_session ON stimulus_events(session_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_sleep_updates_session ON sleep_updates(session_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_sleep_updates_watch_ts ON sleep_updates(watch_ts_sec)")
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    @staticmethod
    def _now_utc() -> str:
        return datetime.now(timezone.utc).isoformat()

    def start_session(self) -> int:
        cursor = self.conn.execute(
            "INSERT INTO sessions (start_ts_utc) VALUES (?)",
            (self._now_utc(),),
        )
        self.conn.commit()
        return int(cursor.lastrowid)

    def stop_session(self, session_id: int, reason: str) -> None:
        self.conn.execute(
            "UPDATE sessions SET end_ts_utc = ?, stop_reason = ? WHERE id = ?",
            (self._now_utc(), reason, session_id),
        )
        self.conn.commit()

    def log_raw_packet(self, session_id: int | None, packet_kind: str | None, stage: str | None, payload: dict[str, Any]) -> None:
        self.conn.execute(
            """
            INSERT INTO raw_packets (session_id, recv_ts_utc, packet_kind, stage, payload_json)
            VALUES (?, ?, ?, ?, ?)
            """,
            (session_id, self._now_utc(), packet_kind, stage, json.dumps(payload, separators=(",", ":"))),
        )
        self.conn.commit()

    def log_sleep_update(self, session_id: int | None, packet: dict[str, Any]) -> None:
        self.conn.execute(
            """
            INSERT OR IGNORE INTO sleep_updates (
                session_id, recv_ts_utc, watch_ts_sec, sequence, status,
                consecutive, source_mode, movement, bpm, sdhr
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                session_id,
                self._now_utc(),
                packet["watch_ts_sec"],
                packet["sequence"],
                packet["status"],
                packet.get("consecutive"),
                packet.get("source_mode"),
                packet.get("movement"),
                packet.get("bpm"),
                packet.get("sdhr"),
            ),
        )
        self.conn.commit()

    def log_stimulus_event(
        self,
        session_id: int | None,
        stage: str,
        stimulus: str,
        action: str,
        details: str,
        success: bool,
    ) -> None:
        self.conn.execute(
            """
            INSERT INTO stimulus_events (session_id, event_ts_utc, stage, stimulus, action, details, success)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (session_id, self._now_utc(), stage, stimulus, action, details, 1 if success else 0),
        )
        self.conn.commit()
