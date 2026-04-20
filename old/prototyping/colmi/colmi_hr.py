import asyncio
from bleak import BleakClient

# --- Configuration ---
# Your specific Colmi R02 MAC Address
TARGET_ADDRESS = "C5661474-4C1A-46F1-8D4E-F474EE5DEA12"

SERVICE_UUID = "6e40fff0-b5a3-f393-e0a9-e50e24dcca9e"
WRITE_UUID   = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
NOTIFY_UUID  = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

def calculate_crc(data_bytes):
    """Calculate the CRC by summing the command ID and data, then masking with 0xFF."""
    return sum(data_bytes) & 0xFF

def create_command(command_id, data):
    """
    Creates the 16-byte command payload:
    [commandId (1 byte)] + [data (14 bytes)] + [crc (1 byte)]
    """
    padded_data = data + [0] * (14 - len(data))
    cmd = [command_id] + padded_data
    crc = calculate_crc(cmd)
    return bytearray(cmd + [crc])

def notification_handler(sender, data):
    """Handles incoming data from the Colmi Ring."""
    raw_id = data[0]
    actual_id = raw_id & 127
    
    # ---------------------------------------------------------
    # 1. Realtime Heart Rate Stream (Command 105)
    # ---------------------------------------------------------
    if actual_id == 105:
        data_type = data[1]
        if data_type == 6:  # 6 means Realtime Heart Rate
            heart_rate = data[3]
            if heart_rate > 0:
                print(f"❤️ Realtime HR: {heart_rate} bpm")
            else:
                print("⏳ Reading sensor... (Keep still)")
                
    # ---------------------------------------------------------
    # 2. Device Notifications (Command 115)
    # ---------------------------------------------------------
    elif actual_id == 115:
        notify_type = data[1]
        
        # NotifyType 1 = Heart Rate push
        if notify_type == 1: 
            print(f"❤️ Device Notify HR: {data[2]} bpm")
            
        # NotifyType 18 = Activity/Pedometer update (triggered by movement)
        elif notify_type == 18:
            # Byte 4 seems to track steps
            steps = data[4]
            # Bytes 6 & 7 combine for a larger metric (likely distance or calories)
            metric_x = (data[6] << 8) | data[7] 
            print(f"🏃 Activity Update! Steps: {steps} | Metric X: {metric_x}")
            
    # Print out any unrecognized commands for debugging
    else:
         print(f"📥 Raw Rx -> ID: {actual_id} | Data: {list(data)}")

async def main():
    print(f"Attempting to connect directly to {TARGET_ADDRESS}...")
    
    # Connect directly using the hardcoded MAC address
    async with BleakClient(TARGET_ADDRESS) as client:
        if not client.is_connected:
            print("❌ Failed to connect. Is the ring nearby and charged?")
            return
            
        print("✅ Connected! Subscribing to notifications...")
        await client.start_notify(NOTIFY_UUID, notification_handler)
        
        await asyncio.sleep(1.0) 

        print("📡 Sending Command 105 (Start Sensor)...")
        # Command 105, Type 6 (RealtimeHR), Action 1 (Start)
        cmd_105 = create_command(105, [6, 1])
        await client.write_gatt_char(WRITE_UUID, cmd_105, response=True)
        
        await asyncio.sleep(0.5)

        print("📡 Sending Command 30 (Request RT HR Stream)...")
        # Command 30, Type 3
        cmd_30 = create_command(30, [3])
        await client.write_gatt_char(WRITE_UUID, cmd_30, response=True)

        print("\n🎧 Listening for data... (Press Ctrl+C to stop)")
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Stopping...")
            
        # Clean up and turn off the sensor to save battery!
        stop_cmd = create_command(105, [6, 4])
        await client.write_gatt_char(WRITE_UUID, stop_cmd, response=True)
        await client.stop_notify(NOTIFY_UUID)
        print("Disconnected cleanly.")

if __name__ == "__main__":
    asyncio.run(main())