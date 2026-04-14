#!/usr/bin/env python3
"""
First prototype demo controller.

Triggered over BLE UART JSON and runs:
awake -> light -> deep -> rem

Commands:
  {"t":"dreamdemo","cmd":"start"}
  {"t":"dreamdemo","cmd":"stop"}
  {"t":"dreamdemo","cmd":"abort"}
  {"t":"dreamdemo","cmd":"next"}
  {"t":"dreamdemo","cmd":"set_stage","stage":"deep"}
  {"t":"dreamdemo","cmd":"set_intensity","value":0.8}
  {"t":"dreamdemo","cmd":"hr","bpm":72}

Also accepts BPM from:
  {"t":"sleepstream","bpm":72}
"""

import argparse
import asyncio
import json
import logging
import shlex
import signal
import socket
import subprocess
import time
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


UART_TX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def to_int(v, fallback):
    try:
        return int(v)
    except Exception:
        return fallback


def to_float(v, fallback):
    try:
        return float(v)
    except Exception:
        return fallback


def stage_name(v):
    if not isinstance(v, str):
        return None
    return {
        "awake": "awake",
        "light": "light",
        "light_sleep": "light",
        "deep": "deep",
        "deep_sleep": "deep",
        "rem": "rem",
    }.get(v.strip().lower().replace(" ", "_"))


def parse_color(v, fallback):
    if not isinstance(v, (list, tuple)) or len(v) != 3:
        return fallback
    return (
        int(clamp(to_int(v[0], fallback[0]), 0, 255)),
        int(clamp(to_int(v[1], fallback[1]), 0, 255)),
        int(clamp(to_int(v[2], fallback[2]), 0, 255)),
    )


def blend(a, b, t):
    return (
        int(a[0] + (b[0] - a[0]) * t),
        int(a[1] + (b[1] - a[1]) * t),
        int(a[2] + (b[2] - a[2]) * t),
    )


def deep_merge(base, override):
    out = dict(base)
    for k, v in override.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = v
    return out


DEFAULT_CONFIG = {
    "protocol": {"type": "dreamdemo"},
    "ble": {
        "name_prefix": "Bangle",
        "scan_timeout_s": 10.0,
        "connect_timeout_s": 25.0,
        "reconnect_min_s": 2.0,
        "reconnect_max_s": 30.0,
        "uart_tx_char_uuid": UART_TX_UUID,
        "stop_demo_on_disconnect": False,
    },
    "demo": {
        "start_on_launch": False,
        "default_bpm": 60,
        "min_bpm": 30,
        "max_bpm": 180,
        "default_intensity": 1.0,
        "max_intensity": 1.5,
    },
    "sequence": ["awake", "light", "deep", "rem"],
    "stages": {},
    "hardware": {
        "led": {"enabled": True, "pin": "D18", "count": 3, "startup_brightness": 0.01},
        "motor": {"enabled": True, "chip": 0, "pin": 17, "pwm_hz": 100},
        "nebuliser": {"enabled": True, "chip": 0, "pin": 27, "active_high": True},
        "puredata": {
            "enabled": True,
            "command": ["pd", "-nogui", "-open", "/home/pi/windscape.pd"],
            "working_dir": "",
            "udp_host": "127.0.0.1",
            "udp_port": 9000,
        },
    },
}


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        user_cfg = json.load(f)
    if not isinstance(user_cfg, dict):
        raise ValueError("Config must be a JSON object")

    cfg = deep_merge(DEFAULT_CONFIG, user_cfg)
    seq = [s for s in (stage_name(v) for v in cfg.get("sequence", [])) if s]
    cfg["sequence"] = seq or ["awake", "light", "deep", "rem"]
    return cfg


class Outputs:
    def __init__(self, cfg, log):
        self.cfg = cfg
        self.log = log
        self.led_task = None
        self.motor_task = None
        self.neb_task = None

        hw = cfg.get("hardware", {})

        led_cfg = hw.get("led", {})
        self.pixels = None
        if bool(led_cfg.get("enabled", True)) and board is not None and neopixel is not None:
            pin = getattr(board, str(led_cfg.get("pin", "D18")), None)
            if pin is not None:
                self.pixels = neopixel.NeoPixel(
                    pin,
                    to_int(led_cfg.get("count", 3), 3),
                    brightness=clamp(to_float(led_cfg.get("startup_brightness", 0.01), 0.01), 0.0, 1.0),
                    auto_write=True,
                )
                self._set_led((0, 0, 0), 0.0)

        motor_cfg = hw.get("motor", {})
        self.motor_handle = None
        self.motor_pin = to_int(motor_cfg.get("pin", 17), 17)
        self.motor_hz = max(1, to_int(motor_cfg.get("pwm_hz", 100), 100))
        if lgpio is not None and bool(motor_cfg.get("enabled", True)):
            try:
                self.motor_handle = lgpio.gpiochip_open(to_int(motor_cfg.get("chip", 0), 0))
                lgpio.gpio_claim_output(self.motor_handle, self.motor_pin)
                self._set_motor(0)
            except Exception as exc:
                self.log.warning("Motor setup failed: %s", exc)
                self.motor_handle = None

        neb_cfg = hw.get("nebuliser", {})
        self.neb_handle = None
        self.neb_pin = to_int(neb_cfg.get("pin", 27), 27)
        self.neb_active_high = bool(neb_cfg.get("active_high", True))
        if lgpio is not None and bool(neb_cfg.get("enabled", True)):
            try:
                self.neb_handle = lgpio.gpiochip_open(to_int(neb_cfg.get("chip", 0), 0))
                lgpio.gpio_claim_output(self.neb_handle, self.neb_pin)
                self._set_nebuliser(False)
            except Exception as exc:
                self.log.warning("Nebuliser setup failed: %s", exc)
                self.neb_handle = None

        self.pd_cfg = hw.get("puredata", {})
        self.pd_process = None
        self.pd_sock = None

    async def close(self):
        await self.off_all()
        self.stop_pd()
        if self.motor_handle is not None and lgpio is not None:
            try:
                lgpio.gpiochip_close(self.motor_handle)
            except Exception:
                pass
        if self.neb_handle is not None and lgpio is not None:
            try:
                lgpio.gpiochip_close(self.neb_handle)
            except Exception:
                pass

    async def off_all(self):
        await self.stop_led()
        await self.stop_motor()
        await self.stop_nebuliser()

    async def apply_stage(self, stage, stage_cfg, intensity, bpm):
        await self.start_led(stage_cfg.get("led", {}), intensity)
        await self.start_motor(stage_cfg.get("motor", {}), intensity)
        await self.start_nebuliser(stage_cfg.get("nebuliser", {}), intensity)
        self.send_pd(f"stage {stage}")
        self.send_pd(f"bpm {bpm}")
        self.send_pd(f"intensity {intensity:.3f}")

    # LED
    def _set_led(self, color, brightness):
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

    async def start_led(self, profile, intensity):
        await self.stop_led()
        if self.pixels is None:
            return
        pattern = str(profile.get("pattern", "off")).lower()
        if pattern in {"off", "none"} or intensity <= 0:
            return
        if pattern == "steady":
            color = parse_color(profile.get("color"), (255, 0, 0))
            b = to_float(profile.get("brightness", profile.get("max_brightness", 0.05)), 0.05)
            self._set_led(color, clamp(b * intensity, 0.0, 1.0))
            return
        self.led_task = asyncio.create_task(self.led_loop(profile, intensity), name="led-loop")

    async def led_loop(self, profile, intensity):
        pattern = str(profile.get("pattern", "pulse")).lower()
        steps = max(2, to_int(profile.get("steps", 60), 60))
        step_s = max(0.001, to_float(profile.get("step_s", 0.02), 0.02))
        min_b = clamp(to_float(profile.get("min_brightness", 0.01), 0.01) * intensity, 0.0, 1.0)
        max_b = clamp(to_float(profile.get("max_brightness", 0.10), 0.10) * intensity, min_b, 1.0)
        color = parse_color(profile.get("color"), (255, 0, 0))
        color_a = parse_color(profile.get("color_a"), (255, 0, 0))
        color_b = parse_color(profile.get("color_b"), (255, 75, 0))

        while True:
            if pattern == "crossfade":
                for i in range(steps):
                    t = i / (steps - 1)
                    self._set_led(blend(color_a, color_b, t), min_b + (max_b - min_b) * t)
                    await asyncio.sleep(step_s)
                for i in range(steps - 1, -1, -1):
                    t = i / (steps - 1)
                    self._set_led(blend(color_a, color_b, t), min_b + (max_b - min_b) * t)
                    await asyncio.sleep(step_s)
            else:
                for i in range(steps):
                    t = i / (steps - 1)
                    self._set_led(color, min_b + (max_b - min_b) * t)
                    await asyncio.sleep(step_s)
                for i in range(steps - 1, -1, -1):
                    t = i / (steps - 1)
                    self._set_led(color, min_b + (max_b - min_b) * t)
                    await asyncio.sleep(step_s)

    # Motor
    def _set_motor(self, duty):
        if self.motor_handle is None or lgpio is None:
            return
        safe = clamp(duty, 0.0, 100.0)
        lgpio.tx_pwm(self.motor_handle, self.motor_pin, self.motor_hz, safe)
        if safe <= 0:
            lgpio.gpio_write(self.motor_handle, self.motor_pin, 0)

    async def stop_motor(self):
        if self.motor_task and not self.motor_task.done():
            self.motor_task.cancel()
            try:
                await self.motor_task
            except asyncio.CancelledError:
                pass
        self.motor_task = None
        self._set_motor(0)

    async def start_motor(self, profile, intensity):
        await self.stop_motor()
        if self.motor_handle is None:
            return
        mode = str(profile.get("mode", "off")).lower()
        if mode == "off" or intensity <= 0:
            return
        if mode == "steady":
            self._set_motor(to_float(profile.get("duty", 25), 25) * intensity)
            return
        self.motor_task = asyncio.create_task(self.motor_loop(profile, intensity), name="motor-loop")

    async def motor_loop(self, profile, intensity):
        duty = to_float(profile.get("duty", 30), 30) * intensity
        on_s = max(0.02, to_float(profile.get("on_s", profile.get("pulse_on_s", 0.3)), 0.3))
        off_s = max(0.02, to_float(profile.get("off_s", profile.get("pulse_off_s", 2.0)), 2.0))
        while True:
            self._set_motor(duty)
            await asyncio.sleep(on_s)
            self._set_motor(0)
            await asyncio.sleep(off_s)

    # Nebuliser
    def _set_nebuliser(self, on):
        if self.neb_handle is None or lgpio is None:
            return
        level = 1 if on else 0
        if not self.neb_active_high:
            level = 0 if on else 1
        lgpio.gpio_write(self.neb_handle, self.neb_pin, level)

    async def stop_nebuliser(self):
        if self.neb_task and not self.neb_task.done():
            self.neb_task.cancel()
            try:
                await self.neb_task
            except asyncio.CancelledError:
                pass
        self.neb_task = None
        self._set_nebuliser(False)

    async def start_nebuliser(self, profile, intensity):
        await self.stop_nebuliser()
        if self.neb_handle is None:
            return
        mode = str(profile.get("mode", "off")).lower()
        if mode == "off" or intensity <= 0:
            return
        if mode == "steady":
            self._set_nebuliser(True)
            return
        self.neb_task = asyncio.create_task(self.neb_loop(profile, intensity), name="neb-loop")

    async def neb_loop(self, profile, intensity):
        base_on = max(0.05, to_float(profile.get("on_s", 0.6), 0.6))
        base_off = max(0.05, to_float(profile.get("off_s", 6.0), 6.0))
        on_s = max(0.05, base_on * max(0.25, intensity))
        off_s = max(0.05, base_off / max(0.25, intensity))
        while True:
            self._set_nebuliser(True)
            await asyncio.sleep(on_s)
            self._set_nebuliser(False)
            await asyncio.sleep(off_s)

    # PureData
    def start_pd(self):
        if not bool(self.pd_cfg.get("enabled", True)):
            return
        if self.pd_process and self.pd_process.poll() is None:
            return

        cmd = self.pd_cfg.get("command", [])
        if not isinstance(cmd, list) or not cmd:
            return

        cwd = str(self.pd_cfg.get("working_dir", "") or "").strip() or None
        if cwd:
            cwd = str(Path(cwd).expanduser())

        try:
            self.pd_process = subprocess.Popen(cmd, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
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

    def send_pd(self, msg):
        if self.pd_sock is None or not bool(self.pd_cfg.get("enabled", True)):
            return
        payload = str(msg).strip()
        if not payload:
            return
        if not payload.endswith(";"):
            payload += ";"
        host = str(self.pd_cfg.get("udp_host", "127.0.0.1"))
        port = to_int(self.pd_cfg.get("udp_port", 9000), 9000)
        try:
            self.pd_sock.sendto(payload.encode("utf-8"), (host, port))
        except OSError:
            pass


class BleListener:
    def __init__(self, cfg, queue, stop_event):
        self.cfg = cfg
        self.queue = queue
        self.stop_event = stop_event
        self.loop = None
        self.buffer = ""
        self.disconnect_event = asyncio.Event()

    async def run(self):
        if BleakClient is None or BleakScanner is None:
            return

        self.loop = asyncio.get_running_loop()

        prefix = str(self.cfg.get("name_prefix", "Bangle"))
        scan_timeout = to_float(self.cfg.get("scan_timeout_s", 10.0), 10.0)
        connect_timeout = to_float(self.cfg.get("connect_timeout_s", 25.0), 25.0)
        tx_uuid = str(self.cfg.get("uart_tx_char_uuid", UART_TX_UUID))
        backoff = to_float(self.cfg.get("reconnect_min_s", 2.0), 2.0)
        backoff_max = to_float(self.cfg.get("reconnect_max_s", 30.0), 30.0)

        while not self.stop_event.is_set():
            try:
                dev = await self.scan(prefix, scan_timeout)
                if dev is None:
                    await asyncio.sleep(backoff)
                    backoff = min(backoff * 1.5, backoff_max)
                    continue

                await self.connect(dev, connect_timeout, tx_uuid)
                backoff = to_float(self.cfg.get("reconnect_min_s", 2.0), 2.0)
            except asyncio.CancelledError:
                raise
            except Exception:
                await asyncio.sleep(backoff)
                backoff = min(backoff * 1.5, backoff_max)

    async def scan(self, prefix, timeout_s):
        found = await BleakScanner.discover(return_adv=True, timeout=timeout_s)
        best = None
        best_rssi = -999
        for dev, adv in found.values():
            name = dev.name or adv.local_name or ""
            if not name.startswith(prefix):
                continue
            rssi = getattr(adv, "rssi", None) or getattr(dev, "rssi", -999) or -999
            if rssi > best_rssi:
                best = dev
                best_rssi = rssi
        return best

    async def connect(self, dev, timeout_s, tx_uuid):
        self.buffer = ""
        self.disconnect_event.clear()

        async with BleakClient(dev, timeout=timeout_s, disconnected_callback=self.on_disconnect) as client:
            await asyncio.sleep(0.8)

            def callback(_sender, data):
                self.buffer += bytes(data).decode("utf-8", errors="ignore")
                self.drain()

            await client.start_notify(tx_uuid, callback)

            stop_wait = asyncio.create_task(self.stop_event.wait())
            disc_wait = asyncio.create_task(self.disconnect_event.wait())
            done, pending = await asyncio.wait({stop_wait, disc_wait}, return_when=asyncio.FIRST_COMPLETED)
            for p in pending:
                p.cancel()

            try:
                await client.stop_notify(tx_uuid)
            except Exception:
                pass

    def on_disconnect(self, _client):
        if self.loop:
            self.loop.call_soon_threadsafe(self.disconnect_event.set)

    def drain(self):
        while self.buffer:
            idx_n = self.buffer.find("\n")
            idx_r = self.buffer.find("\r")
            endings = [i for i in (idx_n, idx_r) if i >= 0]
            if endings:
                idx = min(endings)
                line = self.buffer[:idx]
                self.buffer = self.buffer[idx + 1 :]
                self.handle_line(line)
                continue

            chunk = self.buffer.lstrip()
            if not chunk.startswith("{"):
                self.buffer = ""
                return

            try:
                obj, end = json.JSONDecoder().raw_decode(chunk)
            except json.JSONDecodeError:
                return

            self.buffer = chunk[end:]
            self.handle_line(json.dumps(obj))

    def handle_line(self, line):
        line = line.strip()
        if not line:
            return
        try:
            pkt = json.loads(line)
        except Exception:
            return
        if isinstance(pkt, dict) and self.loop:
            self.loop.call_soon_threadsafe(self.push_now, pkt)

    def push_now(self, pkt):
        try:
            self.queue.put_nowait(pkt)
        except asyncio.QueueFull:
            pass


class App:
    def __init__(self, cfg, enable_ble, log):
        self.cfg = cfg
        self.enable_ble = enable_ble
        self.log = log

        self.stop_event = asyncio.Event()
        self.queue = asyncio.Queue(maxsize=256)
        self.demo = Demo(cfg, log.getChild("demo"))
        self.ble = BleListener(cfg.get("ble", {}), self.queue, self.stop_event)

        self.command_task = None
        self.ble_task = None

    async def run(self, start_now):
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.add_signal_handler(sig, self.stop_event.set)
            except NotImplementedError:
                pass

        self.command_task = asyncio.create_task(self.command_loop(), name="command-loop")
        if self.enable_ble:
            self.ble_task = asyncio.create_task(self.ble.run(), name="ble-loop")

        if start_now or bool(self.cfg.get("demo", {}).get("start_on_launch", False)):
            await self.demo.start("startup")

        await self.stop_event.wait()
        await self.shutdown()

    async def shutdown(self):
        for t in [self.ble_task, self.command_task]:
            if t and not t.done():
                t.cancel()
        await asyncio.gather(*(t for t in [self.ble_task, self.command_task] if t), return_exceptions=True)
        await self.demo.shutdown()

    async def command_loop(self):
        while not self.stop_event.is_set():
            try:
                pkt = await asyncio.wait_for(self.queue.get(), timeout=0.5)
            except asyncio.TimeoutError:
                continue
            await self.demo.handle_packet(pkt)


def parse_args():
    parser = argparse.ArgumentParser(description="First prototype demo controller")
    parser.add_argument("--config", default=str(Path(__file__).with_name("demo_config.json")), help="Path to config JSON")
    parser.add_argument("--start", action="store_true", help="Start demo immediately")
    parser.add_argument("--no-ble", action="store_true", help="Disable BLE listener")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    return parser.parse_args()


async def async_main():
    args = parse_args()
    cfg_path = Path(args.config).expanduser().resolve()
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config not found: {cfg_path}")

    cfg = load_config(cfg_path)

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    app = App(cfg, enable_ble=not args.no_ble, log=logging.getLogger("first_demo"))
    await app.run(start_now=args.start)


def main():
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
