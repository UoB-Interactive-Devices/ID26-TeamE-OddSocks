#!/usr/bin/env python3
"""Simple first prototype demo controller.

What it does:
- Waits for BLE JSON packets from a Bangle (UART TX notify characteristic)
- Starts a fixed stage demo: Awake -> Light -> Deep -> REM
- Runs LED, motor, and nebuliser patterns per stage
- Sends stage and BPM updates to Pure Data over UDP

Expected BLE packets (examples):
- {"cmd":"start"}
- {"cmd":"stop"}
- {"bpm":72}
- {"cmd":"hr","bpm":72}
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import shlex
import signal
import socket
import subprocess
from pathlib import Path

try:
    from bleak import BleakClient, BleakScanner
except ImportError:  # pragma: no cover
    BleakClient = None
    BleakScanner = None

try:
    import board
    import neopixel
except ImportError:  # pragma: no cover
    board = None
    neopixel = None

try:
    import lgpio
except ImportError:  # pragma: no cover
    lgpio = None


# BLE UART notify characteristic (Bangle TX -> Pi RX)
UART_TX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

# Change these values directly to tune the demo.
BLE_NAME_PREFIX = "Bangle"
BLE_SCAN_TIMEOUT_S = 8.0
BLE_CONNECT_TIMEOUT_S = 20.0

MOTOR_PIN = 17
MOTOR_PWM_HZ = 100
NEBULISER_PIN = 27
NEB_ACTIVE_HIGH = True

LED_PIN_NAME = "D18"
LED_COUNT = 3

PUREDATA_ENABLED = True
PUREDATA_COMMAND = ["pd", "-nogui", "-open", "/home/pi/windscape.pd"]
PUREDATA_WORKDIR = ""
PUREDATA_UDP_HOST = "127.0.0.1"
PUREDATA_UDP_PORT = 9000

DEFAULT_BPM = 60
MIN_BPM = 30
MAX_BPM = 180

STAGES = [
    {
        "name": "Awake",
        "duration_s": 20,
        "led": {"mode": "pulse", "color_a": (255, 90, 20), "color_b": (255, 40, 0), "min_b": 0.01, "max_b": 0.08, "step_s": 0.03},
        "motor": {"mode": "off"},
        "neb": {"mode": "off"},
    },
    {
        "name": "Light",
        "duration_s": 20,
        "led": {"mode": "pulse", "color_a": (255, 70, 0), "color_b": (220, 25, 0), "min_b": 0.01, "max_b": 0.09, "step_s": 0.03},
        "motor": {"mode": "pulse", "duty": 28, "on_s": 0.25, "off_s": 2.0},
        "neb": {"mode": "pulse", "on_s": 0.4, "off_s": 9.0},
    },
    {
        "name": "Deep",
        "duration_s": 20,
        "led": {"mode": "pulse", "color_a": (200, 12, 0), "color_b": (120, 0, 0), "min_b": 0.005, "max_b": 0.04, "step_s": 0.045},
        "motor": {"mode": "pulse", "duty": 18, "on_s": 0.2, "off_s": 4.0},
        "neb": {"mode": "pulse", "on_s": 0.3, "off_s": 12.0},
    },
    {
        "name": "REM",
        "duration_s": 20,
        "led": {"mode": "pulse", "color_a": (255, 0, 0), "color_b": (255, 75, 0), "min_b": 0.02, "max_b": 0.16, "step_s": 0.01},
        "motor": {"mode": "pulse", "duty": 65, "on_s": 0.35, "off_s": 0.9},
        "neb": {"mode": "pulse", "on_s": 0.8, "off_s": 5.0},
    },
]


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


def blend(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return (
        int(a[0] + (b[0] - a[0]) * t),
        int(a[1] + (b[1] - a[1]) * t),
        int(a[2] + (b[2] - a[2]) * t),
    )


class Outputs:
    """Very small wrapper around hardware outputs and Pure Data."""

    def __init__(self, log: logging.Logger):
        self.log = log

        self.led_task: asyncio.Task | None = None
        self.motor_task: asyncio.Task | None = None
        self.neb_task: asyncio.Task | None = None

        self.pixels = None
        if board is not None and neopixel is not None:
            pin = getattr(board, LED_PIN_NAME, None)
            if pin is not None:
                self.pixels = neopixel.NeoPixel(pin, LED_COUNT, brightness=0.01, auto_write=True)
                self._set_led((0, 0, 0), 0.0)

        self.gpio_handle = None
        if lgpio is not None:
            try:
                self.gpio_handle = lgpio.gpiochip_open(0)
                lgpio.gpio_claim_output(self.gpio_handle, MOTOR_PIN)
                lgpio.gpio_claim_output(self.gpio_handle, NEBULISER_PIN)
                self._set_motor(0)
                self._set_neb(False)
            except Exception as exc:
                self.log.warning("GPIO init failed: %s", exc)
                self.gpio_handle = None

        self.pd_process: subprocess.Popen | None = None
        self.pd_sock: socket.socket | None = None

    async def close(self):
        await self.stop_all()
        self.stop_pd()
        if self.gpio_handle is not None and lgpio is not None:
            try:
                lgpio.gpiochip_close(self.gpio_handle)
            except Exception:
                pass

    async def stop_all(self):
        await self.stop_led()
        await self.stop_motor()
        await self.stop_neb()

    async def apply_stage(self, stage: dict, bpm: int):
        await self.start_led(stage["led"])
        await self.start_motor(stage["motor"])
        await self.start_neb(stage["neb"])
        self.send_pd(f"stage {stage['name']}")
        self.send_pd(f"bpm {bpm}")

    # Pure Data
    def start_pd(self):
        if not PUREDATA_ENABLED:
            return
        if self.pd_process and self.pd_process.poll() is None:
            return

        cmd = PUREDATA_COMMAND
        if isinstance(cmd, str):
            cmd = shlex.split(cmd)
        if not cmd:
            return

        cwd = str(Path(PUREDATA_WORKDIR).expanduser()) if PUREDATA_WORKDIR else None

        try:
            self.pd_process = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as exc:
            self.log.warning("Could not start Pure Data: %s", exc)
            self.pd_process = None

        if self.pd_sock is None:
            try:
                self.pd_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            except OSError:
                self.pd_sock = None

    def stop_pd(self):
        if self.pd_process and self.pd_process.poll() is None:
            try:
                self.pd_process.terminate()
                self.pd_process.wait(timeout=2.0)
            except Exception:
                try:
                    self.pd_process.kill()
                except Exception:
                    pass
        self.pd_process = None

        if self.pd_sock is not None:
            try:
                self.pd_sock.close()
            except OSError:
                pass
        self.pd_sock = None

    def send_pd(self, msg: str):
        if not PUREDATA_ENABLED or self.pd_sock is None:
            return
        payload = msg.strip()
        if not payload:
            return
        if not payload.endswith(";"):
            payload += ";"
        try:
            self.pd_sock.sendto(payload.encode("utf-8"), (PUREDATA_UDP_HOST, PUREDATA_UDP_PORT))
        except OSError:
            pass

    # LED
    def _set_led(self, color: tuple[int, int, int], brightness: float):
        if self.pixels is None:
            return
        self.pixels.brightness = clamp(brightness, 0.0, 1.0)
        self.pixels.fill(color)

    async def stop_led(self):
        if self.led_task and not self.led_task.done():
            self.led_task.cancel()
            try:
                await self.led_task
            except asyncio.CancelledError:
                pass
        self.led_task = None
        self._set_led((0, 0, 0), 0.0)

    async def start_led(self, cfg: dict):
        await self.stop_led()
        if self.pixels is None or cfg.get("mode", "off") == "off":
            return
        self.led_task = asyncio.create_task(self._led_loop(cfg), name="led-loop")

    async def _led_loop(self, cfg: dict):
        color_a = cfg.get("color_a", (255, 0, 0))
        color_b = cfg.get("color_b", color_a)
        min_b = float(cfg.get("min_b", 0.01))
        max_b = float(cfg.get("max_b", 0.08))
        step_s = float(cfg.get("step_s", 0.03))
        steps = 60

        while True:
            for i in range(steps):
                t = i / (steps - 1)
                self._set_led(blend(color_a, color_b, t), min_b + (max_b - min_b) * t)
                await asyncio.sleep(step_s)
            for i in range(steps - 1, -1, -1):
                t = i / (steps - 1)
                self._set_led(blend(color_a, color_b, t), min_b + (max_b - min_b) * t)
                await asyncio.sleep(step_s)

    # Motor
    def _set_motor(self, duty: float):
        if self.gpio_handle is None or lgpio is None:
            return
        safe = clamp(duty, 0.0, 100.0)
        lgpio.tx_pwm(self.gpio_handle, MOTOR_PIN, MOTOR_PWM_HZ, safe)
        if safe <= 0:
            lgpio.gpio_write(self.gpio_handle, MOTOR_PIN, 0)

    async def stop_motor(self):
        if self.motor_task and not self.motor_task.done():
            self.motor_task.cancel()
            try:
                await self.motor_task
            except asyncio.CancelledError:
                pass
        self.motor_task = None
        self._set_motor(0)

    async def start_motor(self, cfg: dict):
        await self.stop_motor()
        if self.gpio_handle is None or cfg.get("mode", "off") == "off":
            return
        self.motor_task = asyncio.create_task(self._motor_loop(cfg), name="motor-loop")

    async def _motor_loop(self, cfg: dict):
        duty = float(cfg.get("duty", 25))
        on_s = max(0.02, float(cfg.get("on_s", 0.3)))
        off_s = max(0.02, float(cfg.get("off_s", 2.0)))
        while True:
            self._set_motor(duty)
            await asyncio.sleep(on_s)
            self._set_motor(0)
            await asyncio.sleep(off_s)

    # Nebuliser
    def _set_neb(self, on: bool):
        if self.gpio_handle is None or lgpio is None:
            return
        level = 1 if on else 0
        if not NEB_ACTIVE_HIGH:
            level = 0 if on else 1
        lgpio.gpio_write(self.gpio_handle, NEBULISER_PIN, level)

    async def stop_neb(self):
        if self.neb_task and not self.neb_task.done():
            self.neb_task.cancel()
            try:
                await self.neb_task
            except asyncio.CancelledError:
                pass
        self.neb_task = None
        self._set_neb(False)

    async def start_neb(self, cfg: dict):
        await self.stop_neb()
        if self.gpio_handle is None or cfg.get("mode", "off") == "off":
            return
        self.neb_task = asyncio.create_task(self._neb_loop(cfg), name="neb-loop")

    async def _neb_loop(self, cfg: dict):
        on_s = max(0.05, float(cfg.get("on_s", 0.6)))
        off_s = max(0.05, float(cfg.get("off_s", 6.0)))
        while True:
            self._set_neb(True)
            await asyncio.sleep(on_s)
            self._set_neb(False)
            await asyncio.sleep(off_s)


class DemoController:
    """Runs the fixed stage sequence and handles BPM updates."""

    def __init__(self, outputs: Outputs, log: logging.Logger):
        self.outputs = outputs
        self.log = log
        self.bpm = DEFAULT_BPM
        self.running = False
        self.demo_task: asyncio.Task | None = None

    async def start(self):
        if self.running:
            return
        self.running = True
        self.outputs.start_pd()
        self.outputs.send_pd(f"bpm {self.bpm}")
        self.demo_task = asyncio.create_task(self._run_sequence(), name="demo-sequence")
        self.log.info("Demo started")

    async def stop(self):
        self.running = False
        task = self.demo_task
        self.demo_task = None
        if task and not task.done() and task is not asyncio.current_task():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        await self.outputs.stop_all()
        self.outputs.stop_pd()
        self.log.info("Demo stopped")

    async def set_bpm(self, value):
        try:
            bpm = int(value)
        except Exception:
            return
        bpm = int(clamp(bpm, MIN_BPM, MAX_BPM))
        if bpm == self.bpm:
            return
        self.bpm = bpm
        self.outputs.send_pd(f"bpm {self.bpm}")
        self.log.info("BPM -> %s", self.bpm)

    async def _run_sequence(self):
        try:
            for stage in STAGES:
                if not self.running:
                    break
                self.log.info("Stage -> %s", stage["name"])
                await self.outputs.apply_stage(stage, self.bpm)
                await asyncio.sleep(float(stage["duration_s"]))
        except asyncio.CancelledError:
            pass
        finally:
            if self.running:
                self.running = False
                await self.outputs.stop_all()
                self.outputs.stop_pd()
                self.log.info("Demo complete")


class BleListener:
    """Listens for BLE JSON messages and forwards them to the app."""

    def __init__(self, on_packet, log: logging.Logger):
        self.on_packet = on_packet
        self.log = log
        self.stop_event = asyncio.Event()

    async def run(self):
        if BleakClient is None or BleakScanner is None:
            self.log.warning("Bleak not installed; BLE disabled")
            await self.stop_event.wait()
            return

        while not self.stop_event.is_set():
            try:
                dev = await self._scan_for_bangle()
                if dev is None:
                    await asyncio.sleep(2.0)
                    continue
                await self._connect_and_listen(dev)
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                self.log.warning("BLE loop error: %s", exc)
                await asyncio.sleep(2.0)

    async def _scan_for_bangle(self):
        found = await BleakScanner.discover(return_adv=True, timeout=BLE_SCAN_TIMEOUT_S)
        best = None
        best_rssi = -999
        for dev, adv in found.values():
            name = dev.name or adv.local_name or ""
            if not name.startswith(BLE_NAME_PREFIX):
                continue
            rssi = getattr(adv, "rssi", None) or getattr(dev, "rssi", -999) or -999
            if rssi > best_rssi:
                best = dev
                best_rssi = rssi
        if best:
            self.log.info("Found BLE device: %s", best.name)
        return best

    async def _connect_and_listen(self, dev):
        disconnected = asyncio.Event()
        buffer = ""

        def on_disconnect(_client):
            disconnected.set()

        async with BleakClient(dev, timeout=BLE_CONNECT_TIMEOUT_S, disconnected_callback=on_disconnect) as client:
            self.log.info("Connected to %s", dev.name)

            def on_notify(_sender, data):
                nonlocal buffer
                buffer += bytes(data).decode("utf-8", errors="ignore")
                while "\n" in buffer or "\r" in buffer:
                    split_at = min([i for i in (buffer.find("\n"), buffer.find("\r")) if i >= 0])
                    line = buffer[:split_at].strip()
                    buffer = buffer[split_at + 1 :]
                    if not line:
                        continue
                    try:
                        pkt = json.loads(line)
                    except Exception:
                        continue
                    if isinstance(pkt, dict):
                        asyncio.create_task(self.on_packet(pkt))

            await client.start_notify(UART_TX_UUID, on_notify)

            stop_wait = asyncio.create_task(self.stop_event.wait())
            disc_wait = asyncio.create_task(disconnected.wait())
            done, pending = await asyncio.wait({stop_wait, disc_wait}, return_when=asyncio.FIRST_COMPLETED)
            for p in pending:
                p.cancel()

            try:
                await client.stop_notify(UART_TX_UUID)
            except Exception:
                pass
            if disc_wait in done:
                self.log.info("BLE disconnected")


class App:
    def __init__(self, enable_ble: bool, log: logging.Logger):
        self.log = log
        self.enable_ble = enable_ble
        self.stop_event = asyncio.Event()

        self.outputs = Outputs(log.getChild("outputs"))
        self.demo = DemoController(self.outputs, log.getChild("demo"))
        self.ble = BleListener(self.handle_packet, log.getChild("ble"))

        self.ble_task: asyncio.Task | None = None

    async def run(self, start_now: bool):
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.add_signal_handler(sig, self.stop_event.set)
            except NotImplementedError:
                pass

        if self.enable_ble:
            self.ble_task = asyncio.create_task(self.ble.run(), name="ble-listener")

        if start_now:
            await self.demo.start()

        await self.stop_event.wait()
        await self.shutdown()

    async def shutdown(self):
        self.ble.stop_event.set()
        if self.ble_task and not self.ble_task.done():
            self.ble_task.cancel()
            try:
                await self.ble_task
            except asyncio.CancelledError:
                pass

        await self.demo.stop()
        await self.outputs.close()

    async def handle_packet(self, pkt: dict):
        cmd = str(pkt.get("cmd", "")).strip().lower()

        if "bpm" in pkt:
            await self.demo.set_bpm(pkt.get("bpm"))

        if cmd in {"start", "run", "trigger"}:
            await self.demo.start()
        elif cmd in {"stop", "abort"}:
            await self.demo.stop()
        elif cmd in {"hr", "heart_rate"}:
            if "bpm" in pkt:
                await self.demo.set_bpm(pkt.get("bpm"))


def parse_args():
    parser = argparse.ArgumentParser(description="Simple first prototype demo")
    parser.add_argument("--start", action="store_true", help="Start demo immediately")
    parser.add_argument("--no-ble", action="store_true", help="Disable BLE listener")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    return parser.parse_args()


async def async_main():
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    app = App(enable_ble=not args.no_ble, log=logging.getLogger("first_demo"))
    await app.run(start_now=args.start)


def main():
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
