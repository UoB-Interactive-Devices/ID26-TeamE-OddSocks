from __future__ import annotations

import shlex
import socket
import subprocess
from pathlib import Path

from constants import (
    PUREDATA_AUDIO_OUT_DEVICE,
    PUREDATA_COMMAND,
    PUREDATA_ENABLED,
    PUREDATA_FORCE_ALSA,
    PUREDATA_UDP_HOST,
    PUREDATA_UDP_PORT,
    PUREDATA_WORKDIR,
)


class PureDataClient:
    def __init__(self):
        self.process: subprocess.Popen | None = None
        self.sock: socket.socket | None = None

    def start(self):
        if not PUREDATA_ENABLED:
            return
        if self.process and self.process.poll() is None:
            return

        cmd = PUREDATA_COMMAND
        if isinstance(cmd, str):
            cmd = shlex.split(cmd)
        cmd = list(cmd) if cmd else []
        if not cmd:
            return

        has_audiooutdev = any(part == "-audiooutdev" for part in cmd)
        has_alsa = any(part == "-alsa" for part in cmd)
        extra_args: list[str] = []
        if PUREDATA_FORCE_ALSA and not has_alsa:
            extra_args.append("-alsa")
        if not has_audiooutdev:
            extra_args.extend(["-audiooutdev", str(PUREDATA_AUDIO_OUT_DEVICE)])

        if extra_args:
            try:
                open_idx = cmd.index("-open")
            except ValueError:
                open_idx = -1
            if open_idx >= 0:
                cmd[open_idx:open_idx] = extra_args
            else:
                cmd.extend(extra_args)

        cwd = str(Path(PUREDATA_WORKDIR).expanduser()) if PUREDATA_WORKDIR else None

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
