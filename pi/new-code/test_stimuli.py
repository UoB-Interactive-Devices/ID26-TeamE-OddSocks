"""Manual hardware checks for OddSocks Pi demo stimuli.

Run this before a demo to confirm each connected output works.
"""

from __future__ import annotations

import argparse
import asyncio
import contextlib
import logging
import os
import shlex
import shutil
import signal
import subprocess
import sys
from collections.abc import Awaitable, Callable
from typing import Any

from ble_transport import BleTransport

# Hardware config lives here so demo wiring changes are easy to update.
GPIO_CHIP = 0
NEBULISERS = {
    "nebuliser_1": 12,
    "nebuliser_2": 16,
}
HAPTIC_MOTOR_PIN = 23
HAPTIC_PWM_HZ = 100
LED_COUNT = 8
LED_BRIGHTNESS = 0.15
SPEAKER_COMMAND = "speaker-test -t sine -f 440 -l 1"
SPEAKER_TIMEOUT_S = 8.0
DEFAULT_AUDIO_DEVICE = "plughw:0,0"
BLUETOOTH_SETUP_COMMANDS = (
    ("rfkill", "unblock", "bluetooth"),
    ("systemctl", "start", "bluetooth"),
    ("bluetoothctl", "power", "on"),
)
USB_AUDIO_SETUP_COMMANDS = (
    ("modprobe", "snd-usb-audio"),
    ("alsactl", "init"),
)
_CLEANUPS: list[Callable[[], None]] = []

try:
    import lgpio
except ImportError:
    lgpio = None

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

try:
    import board
    import neopixel
except Exception:
    board = None
    neopixel = None


class GpioOutput:
    def __init__(self, pin: int):
        self.pin = pin
        self.handle = None
        self.use_rpi_gpio = False

    def __enter__(self):
        if lgpio is not None:
            self.handle = lgpio.gpiochip_open(GPIO_CHIP)
            lgpio.gpio_claim_output(self.handle, self.pin)
            self.write(0)
            return self

        if GPIO is not None:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin, GPIO.OUT)
            self.use_rpi_gpio = True
            self.write(0)
            return self

        raise RuntimeError("No GPIO library available; run this on the Pi")

    def __exit__(self, _exc_type, _exc, _tb):
        try:
            self.write(0)
        finally:
            if self.handle is not None:
                with contextlib.suppress(Exception):
                    if hasattr(lgpio, "gpio_free"):
                        lgpio.gpio_free(self.handle, self.pin)
                lgpio.gpiochip_close(self.handle)
            elif self.use_rpi_gpio:
                GPIO.cleanup(self.pin)

    def write(self, value: int) -> None:
        if self.handle is not None:
            lgpio.gpio_write(self.handle, self.pin, value)
        elif self.use_rpi_gpio:
            GPIO.output(self.pin, GPIO.HIGH if value else GPIO.LOW)


def register_cleanup(cleanup: Callable[[], None]) -> Callable[[], None]:
    _CLEANUPS.append(cleanup)
    return cleanup


def unregister_cleanup(cleanup: Callable[[], None]) -> None:
    with contextlib.suppress(ValueError):
        _CLEANUPS.remove(cleanup)


def run_cleanups() -> None:
    while _CLEANUPS:
        cleanup = _CLEANUPS.pop()
        with contextlib.suppress(Exception):
            cleanup()


def install_signal_cleanup() -> None:
    previous_handlers = {
        signal.SIGINT: signal.getsignal(signal.SIGINT),
        signal.SIGTERM: signal.getsignal(signal.SIGTERM),
    }

    def handle_signal(signum, _frame):
        run_cleanups()
        previous = previous_handlers.get(signum)
        if callable(previous):
            previous(signum, _frame)
        raise KeyboardInterrupt

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)


def force_pin_low(pin: int) -> None:
    """Last-ditch cleanup for Pi GPIO pins after PWM/backends misbehave."""
    pinctrl = shutil.which("pinctrl")
    if pinctrl and os.geteuid() == 0:
        subprocess.run(
            [pinctrl, "set", str(pin), "dl"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=1,
        )


def run_quiet_command(command: list[str], timeout: float = 2.0) -> str:
    try:
        result = subprocess.run(command, check=False, text=True, capture_output=True, timeout=timeout)
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        return str(exc)
    output = "\n".join(part for part in (result.stdout.strip(), result.stderr.strip()) if part)
    return output or f"exit code {result.returncode}"


def read_quiet_file(path: str) -> str:
    try:
        with open(path) as file:
            return file.read().strip() or "(empty)"
    except OSError as exc:
        return str(exc)


def run_setup_command(command: tuple[str, ...], timeout: float = 5.0) -> tuple[bool, str]:
    if shutil.which(command[0]) is None:
        return False, f"{command[0]} not installed"
    try:
        result = subprocess.run(command, check=False, text=True, capture_output=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return False, "timed out"
    output = "\n".join(part for part in (result.stdout.strip(), result.stderr.strip()) if part)
    return result.returncode == 0, output or f"exit code {result.returncode}"


def bluetooth_status() -> str:
    return run_quiet_command(["bluetoothctl", "show"])


def bluetooth_is_powered(status: str | None = None) -> bool:
    status = bluetooth_status() if status is None else status
    return "Powered: yes" in status


def ensure_bluetooth_ready(auto_setup: bool) -> None:
    status = bluetooth_status()
    if bluetooth_is_powered(status):
        print("bluetooth: powered on")
        return

    if not auto_setup:
        raise RuntimeError(f"Bluetooth is not powered; Bluetooth adapter status: {status}")

    print("bluetooth: not powered; trying to unblock/start/power on")
    for command in BLUETOOTH_SETUP_COMMANDS:
        ok, output = run_setup_command(command)
        if ok:
            print(f"bluetooth: {' '.join(command)} OK")
        else:
            print(f"bluetooth: {' '.join(command)} failed - {output}")

    status = bluetooth_status()
    if not bluetooth_is_powered(status):
        raise RuntimeError(f"Bluetooth is still not powered; Bluetooth adapter status: {status}")


def command_has_audio_device(parts: list[str]) -> bool:
    return "-D" in parts or any(part.startswith("--device") for part in parts)


def audio_diagnostics() -> str:
    return "\n".join(
        (
            "aplay -l:",
            run_quiet_command(["aplay", "-l"]),
            "",
            "/proc/asound/cards:",
            read_quiet_file("/proc/asound/cards"),
            "",
            "/proc/asound/modules:",
            read_quiet_file("/proc/asound/modules"),
            "",
            "lsusb:",
            run_quiet_command(["lsusb"]),
        )
    )


def ensure_usb_audio_ready(auto_setup: bool) -> None:
    if parse_aplay_cards(run_quiet_command(["aplay", "-l"])):
        return

    if not auto_setup:
        return

    print("speaker: no ALSA playback cards yet; trying USB audio setup")
    for command in USB_AUDIO_SETUP_COMMANDS:
        ok, output = run_setup_command(command)
        if ok:
            print(f"speaker: {' '.join(command)} OK")
        else:
            print(f"speaker: {' '.join(command)} failed - {output}")


def parse_aplay_cards(output: str) -> list[tuple[str, str, str, str]]:
    devices = []
    for line in output.splitlines():
        line = line.strip()
        if not line.startswith("card ") or " device " not in line:
            continue
        try:
            left, description = line.split(":", 1)
            card_part, device_part = left.split(",", 1)
            card = card_part.removeprefix("card ").strip().split()[0]
            device = device_part.strip().removeprefix("device ").strip().split()[0]
            label = description.strip()
            score_text = line.lower()
        except (IndexError, ValueError):
            continue
        devices.append((card, device, label, score_text))
    return devices


def preferred_audio_device(auto_setup: bool = False) -> str | None:
    ensure_usb_audio_ready(auto_setup)
    listing = run_quiet_command(["aplay", "-l"])
    devices = parse_aplay_cards(listing)
    if not devices:
        return None

    preferred_words = ("dac", "usb", "audio", "headphones", "bcm2835")

    def score(device: tuple[str, str, str, str]) -> int:
        return sum(1 for word in preferred_words if word in device[3])

    card, device, label, _score_text = max(devices, key=score)
    selected = f"plughw:{card},{device}"
    print(f"speaker: selected ALSA device {selected} ({label})")
    return selected


def resolve_speaker_command(command: str, audio_device: str, auto_setup: bool) -> list[str]:
    parts = shlex.split(command)
    if not parts:
        raise RuntimeError("speaker command is empty")
    if shutil.which(parts[0]) is None:
        raise RuntimeError(f"speaker command not found: {parts[0]}")
    if command_has_audio_device(parts):
        return parts
    if audio_device == "default":
        return parts

    selected_device = preferred_audio_device(auto_setup) if audio_device == "auto" else audio_device
    if selected_device is None:
        print("speaker: no ALSA playback device found by aplay -l; diagnostics:")
        print(audio_diagnostics())
        print("speaker: trying command unchanged")
        return parts
    return [parts[0], "-D", selected_device, *parts[1:]]


async def run_with_timeout(name: str, action: Callable[[], Awaitable[None]], timeout: float) -> None:
    try:
        await asyncio.wait_for(action(), timeout=timeout)
    except asyncio.TimeoutError as exc:
        raise RuntimeError(f"{name} timed out after {timeout:.1f}s; cleanup was requested") from exc


async def test_nebuliser(name: str, pin: int, duration: float) -> None:
    print(f"{name}: GPIO {pin} on for {duration:.1f}s")
    with GpioOutput(pin) as output:
        cleanup = register_cleanup(lambda: output.write(0))
        try:
            output.write(1)
            await asyncio.sleep(duration)
        finally:
            unregister_cleanup(cleanup)
            output.write(0)
    print(f"{name}: off")


class HapticMotor:
    def __init__(self):
        if lgpio is None:
            raise RuntimeError("lgpio is required for PWM haptic motor test")
        self.handle = lgpio.gpiochip_open(GPIO_CHIP)
        self.closed = False
        lgpio.gpio_claim_output(self.handle, HAPTIC_MOTOR_PIN)
        lgpio.gpio_write(self.handle, HAPTIC_MOTOR_PIN, 0)

    def pwm(self, duty_percent: int) -> None:
        lgpio.tx_pwm(self.handle, HAPTIC_MOTOR_PIN, HAPTIC_PWM_HZ, duty_percent)

    def stop(self) -> None:
        if self.closed:
            return
        with contextlib.suppress(Exception):
            lgpio.tx_pwm(self.handle, HAPTIC_MOTOR_PIN, HAPTIC_PWM_HZ, 0)
        with contextlib.suppress(Exception):
            lgpio.gpio_write(self.handle, HAPTIC_MOTOR_PIN, 0)
        with contextlib.suppress(Exception):
            if hasattr(lgpio, "gpio_free"):
                lgpio.gpio_free(self.handle, HAPTIC_MOTOR_PIN)
        with contextlib.suppress(Exception):
            lgpio.gpiochip_close(self.handle)
        self.closed = True
        force_pin_low(HAPTIC_MOTOR_PIN)


async def test_haptic_motor(duration: float, intensity: int) -> None:
    print(f"haptic motor: GPIO {HAPTIC_MOTOR_PIN} PWM {intensity}% for {duration:.1f}s")
    motor = HapticMotor()
    cleanup = register_cleanup(motor.stop)
    try:
        motor.pwm(intensity)
        await asyncio.sleep(duration)
    finally:
        unregister_cleanup(cleanup)
        motor.stop()
    print("haptic motor: off")


async def test_leds(duration: float) -> None:
    if board is None or neopixel is None:
        raise RuntimeError("board/neopixel unavailable; run this on the Pi")

    print(f"leds: D18, {LED_COUNT} pixels")
    try:
        pixels = neopixel.NeoPixel(board.D18, LED_COUNT, brightness=LED_BRIGHTNESS, auto_write=False)
    except RuntimeError as exc:
        if "GPIO busy" in str(exc):
            raise RuntimeError(
                "GPIO18 is busy. Stop any other script/service using LEDs or audio PWM, then retry leds by itself."
            ) from exc
        raise
    cleanup = register_cleanup(lambda: pixels.fill((0, 0, 0)) or pixels.show())
    try:
        for color in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
            pixels.fill(color)
            pixels.show()
            await asyncio.sleep(duration)
    finally:
        unregister_cleanup(cleanup)
        pixels.fill((0, 0, 0))
        pixels.show()
        if hasattr(pixels, "deinit"):
            pixels.deinit()
    print("leds: off")


async def test_speaker(command: str, audio_device: str, auto_setup: bool) -> None:
    parts = resolve_speaker_command(command, audio_device, auto_setup)
    print(f"speaker: {shlex.join(parts)}")
    try:
        proc = await asyncio.to_thread(
            subprocess.run,
            parts,
            check=False,
            timeout=SPEAKER_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"speaker command timed out after {SPEAKER_TIMEOUT_S:.1f}s") from exc
    if proc.returncode:
        cards = run_quiet_command(["aplay", "-l"])
        raise RuntimeError(
            f"speaker command failed with exit code {proc.returncode}; ALSA devices: {cards}"
        )


async def test_watch_buzz(timeout: float, auto_setup: bool) -> None:
    async def noop() -> None:
        return None

    async def on_packet(_packet: dict[str, Any]) -> None:
        return None

    log = logging.getLogger("stimuli_test.ble")
    ensure_bluetooth_ready(auto_setup)
    ble = BleTransport(on_packet=on_packet, on_connected=noop, on_disconnected=noop, log=log)
    task = asyncio.create_task(ble.run_forever())
    cleanup = register_cleanup(ble.request_stop)
    try:
        print("watch buzz: waiting for Bangle BLE connection")
        start = asyncio.get_running_loop().time()
        while not ble.connected:
            if task.done():
                exc = task.exception()
                adapter = run_quiet_command(["bluetoothctl", "show"])
                detail = f"{exc}" if exc else "BLE worker stopped before connecting"
                raise RuntimeError(f"{detail}; Bluetooth adapter status: {adapter}")
            if asyncio.get_running_loop().time() - start > timeout:
                adapter = run_quiet_command(["bluetoothctl", "show"])
                raise RuntimeError(f"timed out waiting for watch BLE connection; Bluetooth adapter status: {adapter}")
            await asyncio.sleep(0.2)

        sent = await ble.send_json({"cmd": "buzz", "buzz": 500, "intensity": 80})
        if not sent:
            raise RuntimeError("watch buzz command was not sent")
        await asyncio.sleep(0.7)
        print("watch buzz: sent")
    finally:
        unregister_cleanup(cleanup)
        ble.request_stop()
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass


async def test_preflight(args: argparse.Namespace) -> None:
    ensure_bluetooth_ready(args.auto_setup)
    device = preferred_audio_device(args.auto_setup) if args.audio_device == "auto" else args.audio_device
    if device:
        print(f"speaker: usable ALSA device candidate: {device}")
    else:
        print("speaker: no ALSA playback devices found; diagnostics:")
        print(audio_diagnostics())


async def run_selected(args: argparse.Namespace) -> None:
    tests: dict[str, Callable[[], Awaitable[None]]] = {
        "preflight": lambda: test_preflight(args),
        "nebuliser_1": lambda: test_nebuliser("nebuliser_1", NEBULISERS["nebuliser_1"], args.duration),
        "nebuliser_2": lambda: test_nebuliser("nebuliser_2", NEBULISERS["nebuliser_2"], args.duration),
        "speaker": lambda: test_speaker(args.speaker_command, args.audio_device, args.auto_setup),
        "haptic_motor": lambda: test_haptic_motor(args.duration, args.intensity),
        "watch_buzz": lambda: test_watch_buzz(args.ble_timeout, args.auto_setup),
        "leds": lambda: test_leds(args.duration),
    }

    names = list(tests) if args.stimulus == "all" else [args.stimulus]
    for name in names:
        print(f"\n== {name} ==")
        try:
            await run_with_timeout(name, tests[name], args.test_timeout)
        except Exception as exc:
            print(f"{name}: FAILED - {exc}")
        else:
            print(f"{name}: OK")
        finally:
            run_cleanups()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Test connected OddSocks demo stimuli")
    parser.add_argument(
        "stimulus",
        choices=["all", "preflight", "nebuliser_1", "nebuliser_2", "speaker", "haptic_motor", "watch_buzz", "leds"],
        nargs="?",
        default="all",
    )
    parser.add_argument("--duration", type=float, default=2.0, help="On-time for GPIO/LED/motor tests")
    parser.add_argument("--intensity", type=int, default=70, help="PWM duty percent for haptic motor")
    parser.add_argument("--ble-timeout", type=float, default=20.0, help="Seconds to wait for Bangle BLE")
    parser.add_argument("--speaker-command", default=SPEAKER_COMMAND, help="Command used for speaker test")
    parser.add_argument(
        "--audio-device",
        default=DEFAULT_AUDIO_DEVICE,
        help="ALSA device for speaker-test: auto, default, or e.g. plughw:1,0",
    )
    parser.add_argument(
        "--no-auto-setup",
        action="store_false",
        dest="auto_setup",
        help="Do not try to unblock/start/power Bluetooth automatically",
    )
    parser.add_argument("--test-timeout", type=float, default=30.0, help="Max seconds before forcing cleanup")
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    install_signal_cleanup()
    try:
        asyncio.run(run_selected(parse_args()))
    except KeyboardInterrupt:
        print("\ninterrupted; cleanup requested", file=sys.stderr)
    finally:
        run_cleanups()


if __name__ == "__main__":
    main()
