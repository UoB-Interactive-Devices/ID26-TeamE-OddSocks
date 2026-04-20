import asyncio
import pygame
import os
from bleak import BleakScanner, BleakClient

# --- CONFIGURATION ---
# Dynamically find the path to the sound file (must be in same folder as script)
script_dir = os.path.dirname(os.path.abspath(__file__))
SOUND_FILE = os.path.join(script_dir, "blip.wav")

DEFAULT_BPM = 60            # Starting speed
MIN_BPM = 30                # Safety floor

# Standard Heart Rate UUIDs
HR_SERVICE_UUID = "0000180d-0000-1000-8000-00805f9b34fb"
HR_MEASUREMENT_UUID = "00002a37-0000-1000-8000-00805f9b34fb"

# Global variable to share data between loops
current_heart_rate = DEFAULT_BPM
stop_event = asyncio.Event()

async def audio_loop():
    """
    Plays the sound at a rhythm determined by 'current_heart_rate'.
    """
    print("🔊 Audio system initializing...")
    
    try:
        # Pre-init helps reduce lag on Pi Zero (44.1kHz, 16-bit, Mono, 2048 buffer)
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=2048)
        pygame.mixer.init()
        
        if not os.path.exists(SOUND_FILE):
            print(f"❌ Error: '{SOUND_FILE}' not found.")
            print("👉 Run: wget https://www.soundjay.com/buttons/sounds/button-1.wav -O blip.wav")
            return
            
        sound = pygame.mixer.Sound(SOUND_FILE)
        print("🔊 Audio ready.")
    except Exception as e:
        print(f"❌ Audio Error: {e}")
        return

    while not stop_event.is_set():
        # 1. Play Sound
        sound.play()
        print("   • BEEP") 
        
        # 2. Calculate Sleep Time (60 / BPM = seconds per beat)
        safe_bpm = max(current_heart_rate, MIN_BPM)
        interval = 60.0 / safe_bpm
        
        # 3. Wait
        await asyncio.sleep(interval)

async def ble_loop():
    """
    Connects to the watch and updates 'current_heart_rate'.
    """
    global current_heart_rate
    print("🔵 Scanning for HeartCast...")

    target_device = None
    
    # Scan for 10 seconds
    devices = await BleakScanner.discover(return_adv=True, timeout=10.0)
    
    for device, adv_data in devices.values():
        # Check 1: Is the Heart Rate Service UUID present?
        has_uuid = HR_SERVICE_UUID.lower() in [u.lower() for u in adv_data.service_uuids]
        
        # Check 2: Does the name contain "HeartCast"? (Case insensitive)
        dev_name = (device.name or "").lower()
        local_name = (adv_data.local_name or "").lower()
        has_name = "heartcast" in dev_name or "heartcast" in local_name
        
        if has_uuid or has_name:
            target_device = device
            break

    if not target_device:
        print("❌ No HeartCast signal found.")
        print("👉 Tip: Open the HeartCast app on your iPhone and keep the screen ON.")
        return

    print(f"✅ Found {target_device.name} ({target_device.address}). Connecting...")

    # RETRY LOOP: Try 3 times to connect
    for attempt in range(3):
        try:
            # Increased timeout to 40.0s for slow Pi Zero
            async with BleakClient(target_device, timeout=40.0) as client:
                print(f"✅ Connected! (Attempt {attempt+1}/3)")
                print("⏳ Waiting 5 seconds for encryption handshake...")
                
                # CRITICAL FIX: Wait 5 seconds for iPhone to finish encryption setup
                await asyncio.sleep(5.0)

                print("✅ Requesting Data Stream...")

                def callback(sender, data):
                    global current_heart_rate
                    flags = data[0]
                    
                    # Parse HR format (uint8 vs uint16)
                    if (flags & 0x01) == 0:
                        bpm = data[1]
                    else:
                        bpm = int.from_bytes(data[1:3], byteorder='little')
                    
                    print(f"❤️  Signal: {bpm} BPM")
                    current_heart_rate = bpm

                await client.start_notify(HR_MEASUREMENT_UUID, callback)
                
                # Keep connection alive until Ctrl+C
                while not stop_event.is_set():
                    await asyncio.sleep(1)
                return # Exit function if loop breaks naturally

        except Exception as e:
            print(f"⚠️ Connection dropped: {e}")
            if attempt < 2:
                print("🔄 Retrying in 2 seconds...")
                await asyncio.sleep(2.0)
    
    print("❌ Failed to connect after 3 attempts.")
    stop_event.set()

async def main():
    await asyncio.gather(ble_loop(), audio_loop())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopping...")
        stop_event.set()