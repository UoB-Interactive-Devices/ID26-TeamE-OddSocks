"""Manual hardware checks for OddSocks Pi demo stimuli.

Run this before a demo to confirm each connected output works.
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import shlex
import subprocess
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
LED_COUNT = 10
LED_BRIGHTNESS = 0.15
SPEAKER_COMMAND = "speaker-test -t sine -f 440 -l 1"

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
                lgpio.gpiochip_close(self.handle)
            elif self.use_rpi_gpio:
                GPIO.cleanup(self.pin)

    def write(self, value: int) -> None:
        if self.handle is not None:
            lgpio.gpio_write(self.handle, self.pin, value)
        elif self.use_rpi_gpio:
            GPIO.output(self.pin, GPIO.HIGH if value else GPIO.LOW)


async def test_nebuliser(name: str, pin: int, duration: float) -> None:
    print(f"{name}: GPIO {pin} on for {duration:.1f}s")
    with GpioOutput(pin) as output:
        output.write(1)
        await asyncio.sleep(duration)
    print(f"{name}: off")


async def test_haptic_motor(duration: float, intensity: int) -> None:
    if lgpio is None:
        raise RuntimeError("lgpio is required for PWM haptic motor test")

    print(f"haptic motor: GPIO {HAPTIC_MOTOR_PIN} PWM {intensity}% for {duration:.1f}s")
    handle = lgpio.gpiochip_open(GPIO_CHIP)
    try:
        lgpio.gpio_claim_output(handle, HAPTIC_MOTOR_PIN)
        lgpio.tx_pwm(handle, HAPTIC_MOTOR_PIN, HAPTIC_PWM_HZ, intensity)
        await asyncio.sleep(duration)
    finally:
        lgpio.tx_pwm(handle, HAPTIC_MOTOR_PIN, HAPTIC_PWM_HZ, 0)
        lgpio.gpiochip_close(handle)
    print("haptic motor: off")


async def test_leds(duration: float) -> None:
    if board is None or neopixel is None:
        raise RuntimeError("board/neopixel unavailable; run this on the Pi")

    print(f"leds: D18, {LED_COUNT} pixels")
    pixels = neopixel.NeoPixel(board.D18, LED_COUNT, brightness=LED_BRIGHTNESS)
    try:
        for color in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
            pixels.fill(color)
            await asyncio.sleep(duration)
    finally:
        pixels.fill((0, 0, 0))
    print("leds: off")


async def test_speaker(command: str) -> None:
    print(f"speaker: {command}")
    proc = await asyncio.to_thread(subprocess.run, shlex.split(command), check=False)
    if proc.returncode:
        raise RuntimeError(f"speaker command failed with exit code {proc.returncode}")


async def test_watch_buzz(timeout: float) -> None:
    async def noop() -> None:
        return None

    async def on_packet(_packet: dict[str, Any]) -> None:
        return None

    log = logging.getLogger("stimuli_test.ble")
    ble = BleTransport(on_packet=on_packet, on_connected=noop, on_disconnected=noop, log=log)
    task = asyncio.create_task(ble.run_forever())
    try:
        print("watch buzz: waiting for Bangle BLE connection")
        start = asyncio.get_running_loop().time()
        while not ble.connected:
            if asyncio.get_running_loop().time() - start > timeout:
                raise RuntimeError("timed out waiting for watch BLE connection")
            await asyncio.sleep(0.2)

        sent = await ble.send_json({"cmd": "buzz", "buzz": 500, "intensity": 80})
        if not sent:
            raise RuntimeError("watch buzz command was not sent")
        await asyncio.sleep(0.7)
        print("watch buzz: sent")
    finally:
        ble.request_stop()
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass


async def run_selected(args: argparse.Namespace) -> None:
    tests: dict[str, Callable[[], Awaitable[None]]] = {
        "nebuliser_1": lambda: test_nebuliser("nebuliser_1", NEBULISERS["nebuliser_1"], args.duration),
        "nebuliser_2": lambda: test_nebuliser("nebuliser_2", NEBULISERS["nebuliser_2"], args.duration),
        "speaker": lambda: test_speaker(args.speaker_command),
        "haptic_motor": lambda: test_haptic_motor(args.duration, args.intensity),
        "watch_buzz": lambda: test_watch_buzz(args.ble_timeout),
        "leds": lambda: test_leds(args.duration),
    }

    names = list(tests) if args.stimulus == "all" else [args.stimulus]
    for name in names:
        print(f"\n== {name} ==")
        try:
            await tests[name]()
        except Exception as exc:
            print(f"{name}: FAILED - {exc}")
        else:
            print(f"{name}: OK")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Test connected OddSocks demo stimuli")
    parser.add_argument(
        "stimulus",
        choices=["all", "nebuliser_1", "nebuliser_2", "speaker", "haptic_motor", "watch_buzz", "leds"],
        nargs="?",
        default="all",
    )
    parser.add_argument("--duration", type=float, default=2.0, help="On-time for GPIO/LED/motor tests")
    parser.add_argument("--intensity", type=int, default=70, help="PWM duty percent for haptic motor")
    parser.add_argument("--ble-timeout", type=float, default=20.0, help="Seconds to wait for Bangle BLE")
    parser.add_argument("--speaker-command", default=SPEAKER_COMMAND, help="Command used for speaker test")
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    asyncio.run(run_selected(parse_args()))


if __name__ == "__main__":
    main()
