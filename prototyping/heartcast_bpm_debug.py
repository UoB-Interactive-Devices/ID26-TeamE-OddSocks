#!/usr/bin/env python3
"""
HeartCast BPM reader for Raspberry Pi Zero W (1st gen).

Automates the full BLE flow, including iOS address rotation:
  1. Checks for an existing paired HeartCast device in BlueZ
  2. If none, scans with Bleak (which works reliably on Pi),
     then drives bluetoothctl via PTY for pairing only:
     connect → pair → auto-confirm passkey →
     detect the resolved public MAC → trust → disconnect
  3. Connects via Bleak and streams BPM

iOS rotates random BLE addresses.  The real public MAC only appears
after pairing completes (BlueZ resolves it via the Identity Resolving
Key).  The script detects this address swap automatically.

Usage:
    python3 heartcast_bpm_debug.py                      # fully automatic
    python3 heartcast_bpm_debug.py --address DC:...     # skip discovery
    python3 heartcast_bpm_debug.py --remove             # wipe bond, re-pair
    python3 heartcast_bpm_debug.py --reset-adapter      # reset hci0 first

Note: bluetoothctl commands are run via 'sudo' internally, so you
may get a password prompt.  Do NOT run the whole script as sudo
(that breaks the Python environment / bleak import).
"""

import asyncio
import argparse
import os
import re
import select
import subprocess
import sys
import time
import traceback
from datetime import datetime
from typing import Optional

try:
    import pty
    _HAS_PTY = True
except ImportError:
    _HAS_PTY = False

from bleak import BleakClient, BleakScanner

# ── constants ────────────────────────────────────────────────────────

HR_SERVICE_UUID     = "0000180d-0000-1000-8000-00805f9b34fb"
HR_MEASUREMENT_UUID = "00002a37-0000-1000-8000-00805f9b34fb"

SCAN_TIMEOUT          = 12.0
CONNECT_TIMEOUT       = 45.0
MAX_ATTEMPTS          = 6
RETRY_DELAY           = 4.0
POST_CONNECT_SETTLE   = 2.0
NOTIFY_TIMEOUT        = 15.0
PAIR_CONNECT_TIMEOUT  = 20
PAIR_EXCHANGE_TIMEOUT = 50

# Matches ANSI escapes more broadly: colors, cursor moves, erase, etc.
ANSI_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]|\x1b\].*?\x07|\x1b\(B")
MAC_RE  = re.compile(r"([0-9A-Fa-f]{2}(?::[0-9A-Fa-f]{2}){5})")


# ── helpers ──────────────────────────────────────────────────────────

def parse_bpm(data: bytearray) -> int:
    flags = data[0]
    if (flags & 0x01) == 0:
        return data[1]
    return int.from_bytes(data[1:3], byteorder="little")


def strip_ansi(text: str) -> str:
    return ANSI_RE.sub("", text).replace("\r", "")


def _clean_lines(text: str) -> list[str]:
    """Strip ANSI codes, carriage returns, and blank lines."""
    return [strip_ansi(l).strip()
            for l in text.splitlines()
            if strip_ansi(l).strip()]


# ── adapter management ───────────────────────────────────────────────

def reset_adapter() -> None:
    """Hard-reset hci0 and restart the bluetooth service."""
    print("  Resetting Bluetooth adapter ...")
    for cmd in (
        ["sudo", "hciconfig", "hci0", "down"],
        ["sudo", "hciconfig", "hci0", "up"],
        ["sudo", "systemctl", "restart", "bluetooth"],
    ):
        try:
            subprocess.run(cmd, timeout=10, check=False,
                           capture_output=True, text=True)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
    time.sleep(3)
    print("  Adapter reset done.")


# ── bluetoothctl one-shot helpers ────────────────────────────────────

def btctl(*args: str, timeout: int = 10) -> str:
    """Run a single non-interactive bluetoothctl command via sudo."""
    try:
        r = subprocess.run(
            ["sudo", "bluetoothctl", *args],
            timeout=timeout, check=False,
            capture_output=True, text=True,
        )
        return strip_ansi((r.stdout or "") + "\n" + (r.stderr or ""))
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return ""


def find_paired_heartcast() -> Optional[str]:
    """Return MAC of an already-paired HeartCast device, or None."""
    output = btctl("paired-devices")

    candidates = []
    for line in output.splitlines():
        m = MAC_RE.search(line)
        if not m:
            continue
        if "heartcast" in line.lower():
            return m.group(1)
        candidates.append(m.group(1))

    # Slow pass: check each paired device for the HR service UUID
    for mac in candidates:
        info = btctl("info", mac)
        if HR_SERVICE_UUID in info.lower():
            return mac

    return None


def remove_device(address: str) -> None:
    print(f"  Removing {address} from BlueZ ...")
    btctl("remove", address, timeout=8)


def disconnect_device(address: str) -> None:
    """Ensure the device is disconnected in BlueZ."""
    btctl("disconnect", address, timeout=5)
    time.sleep(1)


# ── Bleak scan (works reliably on Pi) ────────────────────────────────

async def bleak_scan_heartcast(
    timeout: float = SCAN_TIMEOUT,
    fixed_address: Optional[str] = None,
):
    """Scan via Bleak and return (BLEDevice, address_str) or (None, None)."""
    t = 6.0 if fixed_address else timeout
    print(f"  Bleak scan ({t:.0f}s) ...")
    devices = await BleakScanner.discover(return_adv=True, timeout=t)

    if fixed_address:
        want = fixed_address.upper()
        for dev, _ in devices.values():
            if (dev.address or "").upper() == want:
                print(f"  Found: {dev.name or '?'} ({dev.address})")
                return dev, dev.address
        return None, None

    best, best_rssi = None, -999
    for dev, adv in devices.values():
        uuids = [u.lower() for u in (adv.service_uuids or [])]
        name = ((dev.name or "") + " " + (adv.local_name or "")).lower()
        if HR_SERVICE_UUID not in uuids and "heartcast" not in name:
            continue
        rssi = getattr(adv, "rssi", None) or getattr(dev, "rssi", -999) or -999
        label = dev.name or adv.local_name or "?"
        print(f"  Found: {label} ({dev.address})  RSSI {rssi}")
        if rssi > best_rssi:
            best, best_rssi = dev, rssi

    if best:
        return best, best.address
    return None, None


# ── PTY-based auto-pair (uses address found by Bleak scan) ──────────

def _auto_pair_pty(scan_address: str) -> Optional[str]:
    """
    Drive bluetoothctl in a real PTY to pair with a known address:

        connect <scan_addr>  →  pair <scan_addr>  →  yes
        →  detect resolved MAC  →  trust <resolved>  →  disconnect

    Returns the resolved public MAC, or the original if no resolution.
    """
    if not _HAS_PTY:
        print("  PTY module not available; pair manually via sudo bluetoothctl.")
        return None

    print(f"\n  Auto-pairing {scan_address} via bluetoothctl ...")
    print("  Accept the pairing prompt on your iPhone when it appears.\n")

    master_fd, slave_fd = pty.openpty()
    proc = subprocess.Popen(
        ["sudo", "bluetoothctl"],
        stdin=slave_fd, stdout=slave_fd, stderr=slave_fd,
        close_fds=True,
    )
    os.close(slave_fd)

    def send(cmd: str, delay: float = 0.5):
        os.write(master_fd, (cmd + "\n").encode())
        time.sleep(delay)

    def read_all(timeout: float = 1.0) -> str:
        chunks: list[str] = []
        t = timeout
        while True:
            r, _, _ = select.select([master_fd], [], [], t)
            if not r:
                break
            try:
                data = os.read(master_fd, 8192)
            except OSError:
                break
            if not data:
                break
            chunks.append(data.decode(errors="replace"))
            t = 0.15
        return "".join(chunks)

    def read_and_log(timeout: float = 1.5) -> list[str]:
        """Read PTY output, print it prefixed with '    btctl> ', return lines."""
        raw = read_all(timeout)
        lines = _clean_lines(raw)
        for line in lines:
            print(f"    btctl> {line}")
        return lines

    resolved_address: Optional[str] = None

    try:
        # ── startup ──
        send("power on", 1.0)
        read_and_log(2.0)
        send("agent KeyboardDisplay", 0.5)
        send("default-agent", 0.5)
        read_and_log(1.0)

        # ── connect (matches manual flow: connect before pair) ──
        print(f"  Connecting to {scan_address} ...")
        send(f"connect {scan_address}", 1.0)

        connected = False
        conn_deadline = time.time() + PAIR_CONNECT_TIMEOUT
        while time.time() < conn_deadline:
            lines = read_and_log(2.0)
            joined = " ".join(lines).lower()
            if "connection successful" in joined or "connected: yes" in joined:
                connected = True
                print("  bluetoothctl: Connected.")
                break
            if "failed to connect" in joined or "not available" in joined:
                print("  bluetoothctl: Connect failed; trying pair directly ...")
                break
            if not lines:
                pass  # keep waiting

        # ── pair (triggers service discovery + iOS address resolution) ──
        print(f"  Pairing with {scan_address} ...")
        print("  (waiting for passkey exchange — accept on iPhone)")
        send(f"pair {scan_address}", 1.0)

        pairing_ok = False
        passkey_confirmed = False
        pair_deadline = time.time() + PAIR_EXCHANGE_TIMEOUT

        while time.time() < pair_deadline:
            lines = read_and_log(2.0)
            for line in lines:
                lower = line.lower()

                # Auto-confirm passkey (only once)
                if not passkey_confirmed and (
                    "confirm passkey" in lower
                    or "request confirmation" in lower
                    or ("passkey" in lower and "yes/no" in lower)
                ):
                    print("    → auto-confirming 'yes'")
                    send("yes", 1.0)
                    passkey_confirmed = True

                # Detect address resolution
                if "paired: yes" in lower or "bonded: yes" in lower:
                    pm = MAC_RE.search(line)
                    if pm:
                        addr = pm.group(1).upper()
                        if addr != scan_address.upper():
                            resolved_address = addr
                            print(f"  iOS address resolved: "
                                  f"{scan_address} → {resolved_address}")

                if "pairing successful" in lower:
                    pairing_ok = True
                    print("  Pairing successful!")
                    break

                if "failed to pair" in lower or "authentication canceled" in lower:
                    print(f"  Pairing error: {line}")
                    break

                if "already exists" in lower:
                    pairing_ok = True
                    print("  Bond already exists.")
                    break

            if pairing_ok:
                break

        # Drain a bit more if needed
        if not pairing_ok:
            time.sleep(3)
            lines = read_and_log(3.0)
            for line in lines:
                lower = line.lower()
                if "pairing successful" in lower:
                    pairing_ok = True
                pm = MAC_RE.search(line)
                if pm and ("paired: yes" in lower or "bonded: yes" in lower):
                    addr = pm.group(1).upper()
                    if addr != scan_address.upper():
                        resolved_address = addr
                    pairing_ok = True

        final_address = resolved_address or scan_address

        if not pairing_ok:
            print("  Pairing did not complete.")
            print("  Accept the prompt on iPhone, then re-run.")
            send("exit", 0.5)
            return None

        # ── trust the resolved address ──
        print(f"  Trusting {final_address} ...")
        send(f"trust {final_address}", 2.0)
        lines = read_and_log(2.0)
        for line in lines:
            if "trust succeeded" in line.lower():
                print("  Trust succeeded.")

        # ── disconnect so Bleak gets a clean link ──
        print("  Disconnecting for Bleak handoff ...")
        send(f"disconnect {final_address}", 2.0)
        read_and_log(2.0)
        send("exit", 0.5)

        time.sleep(2)
        print(f"\n  Auto-pair complete.  Address: {final_address}")
        return final_address

    except Exception as exc:
        print(f"  Auto-pair error: {exc}")
        traceback.print_exc()
        return None

    finally:
        try:
            os.close(master_fd)
        except OSError:
            pass
        try:
            proc.kill()
            proc.wait(timeout=5)
        except Exception:
            pass


async def auto_pair(scan_address: str) -> Optional[str]:
    """Async wrapper — runs the blocking PTY auto-pair in a thread."""
    return await asyncio.to_thread(_auto_pair_pty, scan_address)


# ── resolve address (re-use bond, or Bleak scan + auto-pair) ────────

async def resolve_address(
    fixed_address: Optional[str] = None,
    force_remove: bool = False,
) -> Optional[str]:
    """
    Determine the correct MAC to connect to.

    Priority:
      1. --address flag  →  use directly
      2. Existing paired HeartCast in BlueZ  →  re-use
      3. No bond  →  Bleak scan + auto_pair()
    """
    if fixed_address:
        print(f"  Using provided address: {fixed_address}")
        return fixed_address

    if force_remove:
        existing = find_paired_heartcast()
        if existing:
            remove_device(existing)

    paired = find_paired_heartcast()
    if paired:
        print(f"  Found existing HeartCast bond: {paired}")
        return paired

    # ── no bond: scan with Bleak, then pair via bluetoothctl ──
    print("  No paired HeartCast found — scanning with Bleak ...")
    _, scan_addr = await bleak_scan_heartcast()

    if not scan_addr:
        print("  No HeartCast device found in Bleak scan.")
        print("  Make sure HeartCast is open on iPhone + Watch.")
        return None

    print(f"  Bleak found HeartCast at: {scan_addr}")
    print("  Now pairing via bluetoothctl ...")

    resolved = await auto_pair(scan_addr)
    return resolved


# ── connect & stream BPM ────────────────────────────────────────────

async def stream_bpm(target, label: str) -> None:
    """Connect → subscribe to HR notifications → print BPM."""
    print(f"  Connecting to {label} ...")

    async with BleakClient(target, timeout=CONNECT_TIMEOUT) as client:
        print("  Connected.")
        await asyncio.sleep(POST_CONNECT_SETTLE)

        if not client.is_connected:
            raise RuntimeError("Connection dropped during settle.")

        got_data = asyncio.Event()

        def on_hr(_sender, data: bytearray):
            bpm = parse_bpm(data)
            ts = datetime.now().strftime("%H:%M:%S")
            print(f"  [{ts}]  BPM: {bpm}")
            if not got_data.is_set():
                got_data.set()

        await client.start_notify(HR_MEASUREMENT_UUID, on_hr)
        print("  Subscribed to HR notifications. Waiting for data ...")

        try:
            await asyncio.wait_for(got_data.wait(), timeout=NOTIFY_TIMEOUT)
        except asyncio.TimeoutError:
            raise RuntimeError(
                f"No HR data within {NOTIFY_TIMEOUT:.0f}s — "
                "keep HeartCast active on iPhone + Watch."
            )

        print("  Streaming. Ctrl-C to stop.\n")
        while client.is_connected:
            await asyncio.sleep(1)

    print("  Disconnected.")


# ── main loop ────────────────────────────────────────────────────────

async def run(
    fixed_address: Optional[str],
    max_attempts: int,
    do_reset: bool,
    force_remove: bool,
) -> None:

    if do_reset:
        reset_adapter()

    # Step 1: figure out which MAC to use
    address = await resolve_address(fixed_address, force_remove)
    if not address:
        print("\nCould not determine HeartCast address.")
        print("Fallback: pair manually in sudo bluetoothctl, then:")
        print("  python3 heartcast_bpm_debug.py --address <MAC>")
        return

    # Step 2: retry loop
    for attempt in range(1, max_attempts + 1):
        print(f"\n{'=' * 44}")
        print(f"  Attempt {attempt} / {max_attempts}")
        print(f"{'=' * 44}")

        # Release any lingering bluetoothctl connection
        disconnect_device(address)

        device, _ = await bleak_scan_heartcast(fixed_address=address)
        if device is None:
            print(f"  {address} not seen in Bleak scan; trying raw address.")
            target = address
            label = address
        else:
            target = device
            label = f"{device.name or '?'} ({device.address})"
            btctl("trust", device.address, timeout=5)

        try:
            await stream_bpm(target, label)
            return
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            print(f"\n  Error: {type(exc).__name__}: {exc}")
            traceback.print_exc()

            msg = str(exc).lower()
            is_dbus_corruption = isinstance(exc, (EOFError, KeyError))
            is_stale_state = "br-connection-unknown" in msg

            if is_dbus_corruption or is_stale_state:
                print("\n  BlueZ/D-Bus state issue → resetting adapter ...")
                disconnect_device(address)
                reset_adapter()
            else:
                disconnect_device(address)
                await asyncio.sleep(RETRY_DELAY)

    print("\nAll attempts exhausted.")
    print(f"Try:  sudo bluetoothctl remove {address}")
    print(f"Then: python3 heartcast_bpm_debug.py --remove")


# ── entry point ──────────────────────────────────────────────────────

if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="HeartCast BPM reader for Raspberry Pi Zero W.",
    )
    p.add_argument("--address", type=str, default=None,
                   help="Fixed BLE MAC (skip auto-discovery/pairing).")
    p.add_argument("--attempts", type=int, default=MAX_ATTEMPTS,
                   help=f"Max connection retries (default {MAX_ATTEMPTS}).")
    p.add_argument("--reset-adapter", action="store_true",
                   help="Reset hci0 + bluetooth service before starting.")
    p.add_argument("--remove", action="store_true",
                   help="Remove existing HeartCast bond and re-pair from scratch.")
    args = p.parse_args()

    try:
        asyncio.run(run(
            args.address,
            max(1, args.attempts),
            args.reset_adapter,
            args.remove,
        ))
    except KeyboardInterrupt:
        print("\nStopped.")
