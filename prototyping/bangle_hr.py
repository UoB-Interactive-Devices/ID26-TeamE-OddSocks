import asyncio
from bleak import BleakScanner, BleakClient

# Standard Bluetooth SIG UUIDs for Heart Rate
HR_SERVICE_UUID = "0000180d-0000-1000-8000-00805f9b34fb"
HR_MEASUREMENT_UUID = "00002a37-0000-1000-8000-00805f9b34fb"

# Prefix of the device name we are looking for
DEVICE_NAME_PREFIX = "Bangle.js"

def hr_val_handler(sender, data):
    """
    Callback triggered every time the watch sends a new Heart Rate measurement.
    """
    # The first byte contains the flags
    flags = data[0]
    
    # Bit 0 of the flags indicates if the HR value is 8-bit (0) or 16-bit (1)
    is_16bit = flags & 0x01
    
    if is_16bit:
        # 16-bit HR value (Bytes 1 and 2, little-endian)
        hr_value = int.from_bytes(data[1:3], byteorder='little')
    else:
        # 8-bit HR value (Byte 1)
        hr_value = data[1]
        
    print(f"❤️ Heart Rate: {hr_value} bpm")

async def main():
    print(f"Scanning for devices matching '{DEVICE_NAME_PREFIX}'...")
    # Scan for BLE devices in range for 5 seconds
    devices = await BleakScanner.discover(timeout=5.0)
    
    target_address = None
    for d in devices:
        if d.name and d.name.startswith(DEVICE_NAME_PREFIX):
            print(f"Found {d.name} with address {d.address}")
            target_address = d.address
            break
            
    if not target_address:
        print(f"Could not find a device starting with '{DEVICE_NAME_PREFIX}'.")
        print("Make sure the Bangle.js is broadcasting its HR service.")
        return

    print(f"Connecting to {target_address}...")
    
    # Connect and subscribe to the Heart Rate characteristic
    async with BleakClient(target_address) as client:
        print(f"Connected: {client.is_connected}")
        
        await client.start_notify(HR_MEASUREMENT_UUID, hr_val_handler)
        print("Subscribed to HR measurements. Press Ctrl+C to stop.\n")
        
        # Keep the event loop running to listen for incoming notifications
        try:
            while True:
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass
        finally:
            await client.stop_notify(HR_MEASUREMENT_UUID)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nDisconnected gracefully.")