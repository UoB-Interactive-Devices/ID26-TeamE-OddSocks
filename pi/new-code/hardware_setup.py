"""Small shared setup helpers for the Pi demo hardware."""

from __future__ import annotations

import re
import shlex
import shutil
import subprocess
from pathlib import Path


DEFAULT_AUDIO_DEVICE = "auto"
DEFAULT_SPEAKER_VOLUME_PERCENT = 20
SPI_DEVICE = Path("/dev/spidev0.0")


def run_quiet_command(command: list[str], timeout: float = 2.0) -> str:
    try:
        result = subprocess.run(command, check=False, text=True, capture_output=True, timeout=timeout)
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        return str(exc)
    return "\n".join(part for part in (result.stdout.strip(), result.stderr.strip()) if part) or f"exit code {result.returncode}"


def run_setup_command(command: tuple[str, ...], timeout: float = 5.0) -> bool:
    if shutil.which(command[0]) is None:
        return False
    try:
        return subprocess.run(command, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=timeout).returncode == 0
    except subprocess.TimeoutExpired:
        return False


def ensure_bluetooth_ready(auto_setup: bool, log=None) -> bool:
    status = run_quiet_command(["bluetoothctl", "show"])
    if "Powered: yes" in status:
        log_or_print(log, "info", "bluetooth: powered on")
        return True

    if not auto_setup:
        log_or_print(log, "warning", "bluetooth: not powered")
        return False

    for command in (
        ("rfkill", "unblock", "bluetooth"),
        ("systemctl", "start", "bluetooth"),
        ("bluetoothctl", "power", "on"),
    ):
        run_setup_command(command)

    status = run_quiet_command(["bluetoothctl", "show"])
    ok = "Powered: yes" in status
    log_or_print(log, "info" if ok else "warning", "bluetooth: %s", "powered on" if ok else "not powered")
    return ok


def find_usb_audio_device() -> tuple[str, str | None, str] | None:
    """Return (ALSA device, card number, description) for the USB DAC."""
    for line in run_quiet_command(["aplay", "-l"]).splitlines():
        line = line.strip()
        if not line.startswith("card ") or "device 0:" not in line:
            continue
        if "usb" not in line.lower() and "pnp sound" not in line.lower():
            continue
        match = re.match(r"card\s+(\d+):", line)
        if match:
            card = match.group(1)
            return f"plughw:{card},0", card, line
    return None


def resolve_audio_device(audio_device: str = DEFAULT_AUDIO_DEVICE) -> tuple[str, str | None, str]:
    if audio_device != "auto":
        return audio_device, card_from_device(audio_device), f"configured {audio_device}"

    device = find_usb_audio_device()
    if device is None:
        raise RuntimeError(f"no USB audio playback device found; ALSA devices: {run_quiet_command(['aplay', '-l'])}")
    return device


def resolve_speaker_command(command: str, audio_device: str = DEFAULT_AUDIO_DEVICE) -> list[str]:
    parts = shlex.split(command)
    if not parts:
        raise RuntimeError("speaker command is empty")
    if shutil.which(parts[0]) is None:
        raise RuntimeError(f"speaker command not found: {parts[0]}")
    if "-D" in parts or any(part.startswith("--device") for part in parts) or audio_device == "default":
        return parts

    device, _card, _description = resolve_audio_device(audio_device)
    return [parts[0], "-D", device, *parts[1:]]


def set_speaker_volume(audio_device: str, volume_percent: int, log=None) -> bool:
    _device, card, _description = resolve_audio_device(audio_device)
    if card is None:
        log_or_print(log, "warning", "speaker: volume unchanged; no card number for %s", audio_device)
        return False

    controls = run_quiet_command(["amixer", "-c", card, "scontrols"])
    control = first_matching_control(controls, ("Speaker", "PCM", "Master", "Headphone"))
    if control is None:
        log_or_print(log, "warning", "speaker: no mixer volume control found on card %s", card)
        return False

    volume = max(0, min(100, int(volume_percent)))
    ok = run_setup_command(("amixer", "-c", card, "sset", control, f"{volume}%"))
    log_or_print(log, "info" if ok else "warning", "speaker: set %s to %s%%", control, volume)
    return ok


def setup_preflight(
    *,
    enable_ble: bool,
    auto_setup: bool,
    audio_device: str,
    speaker_volume: int | None,
    check_spi: bool,
    log=None,
) -> None:
    if enable_ble:
        ensure_bluetooth_ready(auto_setup, log=log)

    try:
        device, _card, description = resolve_audio_device(audio_device)
    except Exception as exc:
        log_or_print(log, "warning", "speaker: audio device not ready: %s", exc)
    else:
        log_or_print(log, "info", "speaker: using %s (%s)", device, description)
        if speaker_volume is not None:
            set_speaker_volume(audio_device, speaker_volume, log=log)

    if check_spi:
        log_or_print(log, "info" if SPI_DEVICE.exists() else "warning", "leds: SPI device %s %s", SPI_DEVICE, "ready" if SPI_DEVICE.exists() else "not found")


def first_matching_control(controls_output: str, names: tuple[str, ...]) -> str | None:
    controls = re.findall(r"Simple mixer control '([^']+)'", controls_output)
    for name in names:
        if name in controls:
            return name
    return controls[0] if controls else None


def card_from_device(audio_device: str) -> str | None:
    match = re.match(r"(?:plug)?hw:(\d+),", audio_device)
    return match.group(1) if match else None


def log_or_print(log, level: str, message: str, *args) -> None:
    if log is not None and hasattr(log, level):
        getattr(log, level)(message, *args)
    else:
        print(message % args if args else message)


def init_pygame_audio() -> bool:
    import os
    import pygame
    
    if pygame.mixer.get_init():
        return True
        
    try:
        device, _, _ = resolve_audio_device("auto")
        os.environ["SDL_AUDIODRIVER"] = "alsa"
        os.environ["AUDIODEV"] = device
    except Exception:
        pass

    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=2048)
    pygame.mixer.init()
    return True
