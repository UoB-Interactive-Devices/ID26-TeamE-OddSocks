
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class Database:
    # We grab file path location later, so we need a default
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        # Creating a database, there's a lot of sleep data we need to store
        self.conn = sqlite3.connect(self.db_path, timeout=30)
        # I'll be so fr I just found this line online, it's an efficiency thing
        # More details here harlesleifer.com/blog/going-fast-with-sqlite-and-python/
        self.conn.execute("PRAGMA journal_mode=WAL")
        # Overnight logging is low volume, so favour durability over speed.
        self.conn.execute("PRAGMA synchronous=FULL")
        # schema is validation in SQL formats
        self._init_schema()

    def _init_schema(self) -> None:
        # SQL format moment
        # Creates the table only if one doesn't already exist
        # This one is for the dedicated sleep sessions
        # Makes our columns not repeat their ID
        # Start and end times, we need those for obvious sleep reasons
        # stop_reason tells you why the code executed correctly, whether naturally or from us ending it (which we can do)
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
        #This one is for the packets we recieve from the ble
        #We get the time, the type of packet and the data from the json
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
        #This one for stimulus, hopefully it's all self explanatory
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
        #The actual readings, prob the most important one
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
        #makin the database
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_raw_packets_session ON raw_packets(session_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_stimulus_events_session ON stimulus_events(session_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_sleep_updates_session ON sleep_updates(session_id)")
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_sleep_updates_watch_ts ON sleep_updates(watch_ts_sec)")
        self.conn.commit()


    #The close function closes the connection it turns out
    def close(self) -> None:
        self.conn.close()

    @staticmethod
    #For getting the current time
    def _now_utc() -> str:
        return datetime.now(timezone.utc).isoformat()

    #Adds a new row within the session table
    def start_session(self) -> int:
        cursor = self.conn.execute(
            "INSERT INTO sessions (start_ts_utc) VALUES (?)",
            (self._now_utc(),),
        )
        self.conn.commit()
        return int(cursor.lastrowid)

    #And then this ends the session and sends the time back
    def stop_session(self, session_id: int, reason: str) -> None:
        self.conn.execute(
            "UPDATE sessions SET end_ts_utc = ?, stop_reason = ? WHERE id = ?",
            (self._now_utc(), reason, session_id),
        )
        self.conn.commit()


   #This one is for the raw packet data obv, it's a lil ugly but its a very simple function that just has a lot of preset types
    def log_raw_packet(self, session_id: int | None, packet_kind: str | None, stage: str | None, payload: dict[str, Any]) -> None:
        self.conn.execute(
            """
            INSERT INTO raw_packets (session_id, recv_ts_utc, packet_kind, stage, payload_json)
            VALUES (?, ?, ?, ?, ?)
            """,
            (session_id, self._now_utc(), packet_kind, stage, json.dumps(payload, separators=(",", ":"))),
        )
        self.conn.commit()

    #I mean these have a few lines but they're all kinda just, getting the data and put it in the database, it's just SQL being ugly
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


    #The final one for stimulus, more data types, more commits, more SQL
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
