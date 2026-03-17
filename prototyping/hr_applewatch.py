import asyncio
from bleak import BleakScanner, BleakClient

# Standard Heart Rate Service UUID
HR_SERVICE_UUID = "0000180d-0000-1000-8000-00805f9b34fb"
# Standard Heart Rate Measurement Characteristic UUID
HR_MEASUREMENT_UUID = "00002a37-0000-1000-8000-00805f9b34fb"

async def run():
    print("Scanning for Apple Watch (via HeartCast)...")
    
    # FIX: We use return_adv=True to get the advertisement data (which contains the UUIDs)
    found_devices = await BleakScanner.discover(return_adv=True)
    
    target_device = None

    # Iterate through found devices to find one broadcasting the Heart Rate Service
    for device, adv_data in found_devices.values():
        # adv_data.service_uuids is a list of strings (e.g. ['0000180d-...'])
        if HR_SERVICE_UUID.lower() in [uuid.lower() for uuid in adv_data.service_uuids]:
            target_device = device
            break

    if not target_device:
        print("No heart rate monitor found! Make sure HeartCast is running on your Phone & Watch.")
        return

    print(f"Found device: {target_device.name} ({target_device.address})")
    print("Connecting...")

    async with BleakClient(target_device) as client:
        print(f"Connected to {target_device.name}! Waiting for data...")

        def callback(sender, data):
            # The first byte is flags
            flags = data[0]
            # The first bit of the flags indicates if the format is uint8 or uint16
            hr_format = flags & 0x01
            
            if hr_format == 0:
                # UINT8 format (1 byte)
                heart_rate = data[1]
            else:
                # UINT16 format (2 bytes)
                heart_rate = int.from_bytes(data[1:3], byteorder='little')
            
            print(f"❤️ Heart Rate: {heart_rate} BPM")

        # Subscribe to the Heart Rate Measurement characteristic
        await client.start_notify(HR_MEASUREMENT_UUID, callback)
        
        # Keep the script running to listen for data
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\nStopping...")
    except Exception as e:
        print(f"An error occurred: {e}")