import asyncio
import pygame
import os
from bleak import BleakScanner, BleakClient

# --- CONFIGURATION ---
SOUND_FILE = "blip.wav"     # Ensure this file is in the same folder
DEFAULT_BPM = 60            # Speed to start at before data arrives
MIN_BPM = 30                # Safety floor (prevent divide by zero)

# UUIDs for Heart Rate Service
HR_SERVICE_UUID = "0000180d-0000-1000-8000-00805f9b34fb"
HR_MEASUREMENT_UUID = "00002a37-0000-1000-8000-00805f9b34fb"

# Global variable to share data
current_heart_rate = DEFAULT_BPM
stop_event = asyncio.Event()

async def audio_loop():
    """
    Plays the sound at a rhythm determined by 'current_heart_rate'.
    """
    print("🔊 Audio system initializing...")
    
    # Pre-init helps reduce lag on Pi Zero
    try:
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=2048)
        pygame.mixer.init()
        
        # Check if file exists
        if not os.path.exists(SOUND_FILE):
            print(f"❌ Error: '{SOUND_FILE}' not found. Please download a wav file.")
            return
            
        sound = pygame.mixer.Sound(SOUND_FILE)
        print("🔊 Audio ready.")
    except Exception as e:
        print(f"❌ Audio Error: {e}")
        return

    while not stop_event.is_set():
        # 1. Play Sound
        sound.play()
        print("   • BEEP") # Visual feedback in console
        
        # 2. Calculate Sleep Time
        # Formula: 60 seconds / BPM = seconds per beat
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

    # Find device with Heart Rate Service
    target_device = None
    devices = await BleakScanner.discover(return_adv=True)
    
    for device, adv_data in devices.values():
        if HR_SERVICE_UUID.lower() in [u.lower() for u in adv_data.service_uuids]:
            target_device = device
            break

    if not target_device:
        print("❌ No HeartCast signal found. Check your phone!")
        stop_event.set()
        return

    print(f"✅ Found {target_device.name}. Connecting...")

    async with BleakClient(target_device) as client:
        print("✅ Connected! Reading Heart Rate...")

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
        
        # Keep connection alive
        while not stop_event.is_set():
            await asyncio.sleep(1)

async def main():
    await asyncio.gather(ble_loop(), audio_loop())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopping...")
        stop_event.set()