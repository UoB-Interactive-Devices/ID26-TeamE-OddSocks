from __future__ import annotations

import logging
import os
import shutil
import shlex
import socket
import subprocess
import time
from pathlib import Path

from constants import (
    PUREDATA_ALSA_CARD,
    PUREDATA_AUDIO_OUT_DEVICE,
    PUREDATA_CAPTURE_LOG,
    PUREDATA_COMMAND,
    PUREDATA_DISABLE_AUDIO_IN,
    PUREDATA_ENABLED,
    PUREDATA_FALLBACK_TO_DEFAULT_OUTPUT,
    PUREDATA_FORCE_ALSA,
    PUREDATA_LOG_FILE,
    PUREDATA_UDP_HOST,
    PUREDATA_UDP_PORT,
    PUREDATA_WORKDIR,
)


class PureDataClient:
    def __init__(self, log: logging.Logger | None = None):
        self.process: subprocess.Popen | None = None
        self.sock: socket.socket | None = None
        self.log = log or logging.getLogger("sleep_demo_modular.pd")
        self._proc_log_handle = None

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
            self.log.warning("Pure Data command is empty; skipping launch")
            return

        exe = cmd[0]
        if shutil.which(exe) is None:
            self.log.error("Pure Data executable not found in PATH: %s", exe)
            return

        has_audiooutdev = any(part == "-audiooutdev" for part in cmd)
        has_alsa = any(part == "-alsa" for part in cmd)
        has_noadc = any(part == "-noadc" for part in cmd)
        extra_args: list[str] = []
        if PUREDATA_FORCE_ALSA and not has_alsa:
            extra_args.append("-alsa")
        added_audiooutdev = False
        if PUREDATA_AUDIO_OUT_DEVICE is not None and not has_audiooutdev:
            extra_args.extend(["-audiooutdev", str(PUREDATA_AUDIO_OUT_DEVICE)])
            added_audiooutdev = True
        if PUREDATA_DISABLE_AUDIO_IN and not has_noadc:
            extra_args.append("-noadc")

        if extra_args:
            try:
                open_idx = cmd.index("-open")
            except ValueError:
                open_idx = -1
            if open_idx >= 0:
                cmd[open_idx:open_idx] = extra_args
            else:
                cmd.extend(extra_args)

        repo_root = Path(__file__).resolve().parents[2]
        if PUREDATA_WORKDIR:
            workdir_path = Path(PUREDATA_WORKDIR).expanduser()
            if not workdir_path.is_absolute():
                workdir_path = repo_root / workdir_path
            cwd = str(workdir_path)
        else:
            cwd = str(repo_root)

        try:
            self.log.info("Launching Pure Data: %s (cwd=%s)", " ".join(cmd), cwd)
            stdout_target = subprocess.DEVNULL
            stderr_target = subprocess.DEVNULL
            proc_env = None
            if PUREDATA_ALSA_CARD:
                proc_env = dict(os.environ)
                proc_env["ALSA_CARD"] = PUREDATA_ALSA_CARD
                proc_env["ALSA_PCM_CARD"] = PUREDATA_ALSA_CARD
                self.log.info("Setting ALSA card preference for PD: %s", PUREDATA_ALSA_CARD)
            if PUREDATA_CAPTURE_LOG:
                log_path = Path(cwd) / PUREDATA_LOG_FILE
                self._proc_log_handle = open(log_path, "a", encoding="utf-8")
                stdout_target = self._proc_log_handle
                stderr_target = self._proc_log_handle
                self.log.info("Pure Data logs -> %s", log_path)
            attempts: list[tuple[str, list[str]]] = [("configured", cmd)]

            if PUREDATA_FALLBACK_TO_DEFAULT_OUTPUT and added_audiooutdev:
                no_outdev: list[str] = []
                i = 0
                while i < len(cmd):
                    if cmd[i] == "-audiooutdev" and i + 1 < len(cmd):
                        i += 2
                        continue
                    no_outdev.append(cmd[i])
                    i += 1
                attempts.append(("without-audiooutdev", no_outdev))

                # Some Pi setups fail specifically when forcing ALSA; retry with default backend.
                no_outdev_no_alsa = [part for part in no_outdev if part != "-alsa"]
                attempts.append(("without-audiooutdev-and-alsa", no_outdev_no_alsa))

            launched = False
            for label, attempt_cmd in attempts:
                self.log.info("Launching Pure Data attempt=%s cmd=%s", label, " ".join(attempt_cmd))
                self.process = subprocess.Popen(
                    attempt_cmd,
                    cwd=cwd,
                    stdout=stdout_target,
                    stderr=stderr_target,
                    env=proc_env,
                )
                time.sleep(0.25)
                if self.process.poll() is None:
                    self.log.info("Pure Data started (attempt=%s)", label)
                    launched = True
                    break
                self.log.error(
                    "Pure Data exited immediately on attempt=%s with code %s",
                    label,
                    self.process.returncode,
                )

            if not launched:
                self.process = None
        except Exception:
            self.log.exception("Failed to launch Pure Data")
            self.process = None
            if self._proc_log_handle is not None:
                try:
                    self._proc_log_handle.close()
                except OSError:
                    pass
                self._proc_log_handle = None

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

        if self._proc_log_handle is not None:
            try:
                self._proc_log_handle.close()
            except OSError:
                pass
            self._proc_log_handle = None

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
