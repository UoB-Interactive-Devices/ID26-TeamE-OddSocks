from __future__ import annotations

import logging
import shlex
import socket
import subprocess
from pathlib import Path

from old.sleep_demo_modular.constants import (
    PUREDATA_COMMAND,
    PUREDATA_ENABLED,
    PUREDATA_UDP_HOST,
    PUREDATA_UDP_PORT,
    PUREDATA_WORKDIR,
)


class PureDataClient:
    def __init__(self, log: logging.Logger | None = None):
        self.process: subprocess.Popen | None = None
        self.sock: socket.socket | None = None
        self.log = log or logging.getLogger("sleep_demo_modular.pd")

    def start(self):
        if not PUREDATA_ENABLED:
            return
        if self.process and self.process.poll() is None:
            return

        cmd = PUREDATA_COMMAND
        if isinstance(cmd, str):
            cmd = shlex.split(cmd)
        if not cmd:
            return

        repo_root = Path(__file__).resolve().parents[2]
        if PUREDATA_WORKDIR:
            workdir_path = Path(PUREDATA_WORKDIR).expanduser()
            if not workdir_path.is_absolute():
                workdir_path = repo_root / workdir_path
            cwd = str(workdir_path)
        else:
            cwd = str(repo_root)

        try:
            self.process = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            self.process = None

        if self.sock is None:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            except OSError:
                self.sock = None

    def stop(self):
        if self.process and self.process.poll() is None:
            try:
                self.process.terminate()
                self.process.wait(timeout=2.0)
            except Exception:
                try:
                    self.process.kill()
                except Exception:
                    pass
        self.process = None

        if self.sock is not None:
            try:
                self.sock.close()
            except OSError:
                pass
        self.sock = None

    def send(self, msg: str):
        if self.sock is None or not PUREDATA_ENABLED:
            return
        payload = msg.strip()
        if not payload:
            return
        if not payload.endswith(";"):
            payload += ";"
        try:
            self.sock.sendto(payload.encode("utf-8"), (PUREDATA_UDP_HOST, PUREDATA_UDP_PORT))
        except OSError:
            pass
