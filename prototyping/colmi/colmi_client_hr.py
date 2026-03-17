import asyncio
from colmi_r02_client.client import Client
from colmi_r02_client.real_time import RealTimeReading

RING_NAME = "R02_341C"  # use CLI with --name first, or replace with address

async def main():
    from bleak import BleakScanner
    devices = await BleakScanner.discover()
    dev = next(d for d in devices if d.name == RING_NAME)
    async with Client(dev.address) as client:
        hr = await client.get_realtime_reading(RealTimeReading.HEART_RATE)
        print(hr)

asyncio.run(main())