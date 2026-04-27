
from __future__ import annotations

import argparse
import asyncio
import logging
import signal
from pathlib import Path

from app import MasterApp
from db import Database
from hardware_setup import DEFAULT_AUDIO_DEVICE, DEFAULT_SPEAKER_VOLUME_PERCENT, setup_preflight

#We grab file path location later, so we need a default
DEFAULT_DB_PATH = Path(__file__).resolve().parent / "sleep_core.db"


def parse_args() -> argparse.Namespace:
    #Used in the command line to help add arguments during runtime, primarily used for debugging and the like
    #They should be all pretty self-explanatory
    parser = argparse.ArgumentParser(description="Simple overnight Pi sleep controller")
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH), help="SQLite database path")
    parser.add_argument("--no-ble", action="store_true", help="Disable BLE and use local test flow")
    parser.add_argument("--cli-test", action="store_true", help="Run interactive CLI test mode")
    parser.add_argument("--cli-test-ble", action="store_true", help="Enable BLE in CLI test mode and wait for watch connection")
    parser.add_argument("--debug", action="store_true", help="Enable app debug logs (packets/state), without noisy BLE backend logs")
    parser.add_argument("--bleak-debug", action="store_true", help="Enable verbose Bleak/backend debug logs")
    parser.add_argument("--preflight", action="store_true", help="Run startup hardware prerequisite checks, then exit")
    parser.add_argument("--no-auto-setup", action="store_true", help="Do not try to power on Bluetooth automatically")
    parser.add_argument("--audio-device", default=DEFAULT_AUDIO_DEVICE, help="ALSA speaker device, e.g. auto, plughw:0,0, plughw:1,0, default")
    parser.add_argument("--speaker-volume", type=int, default=DEFAULT_SPEAKER_VOLUME_PERCENT, help="Safe startup speaker volume percent")
    parser.add_argument("--no-speaker-volume", action="store_true", help="Do not change mixer volume at startup")
    parser.add_argument("--no-spi-check", action="store_true", help="Skip /dev/spidev0.0 LED prerequisite check")
    return parser.parse_args()


def configure_logging(args: argparse.Namespace) -> None:
    # Keep root logger at INFO so third-party libraries stay quiet by default.
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    app_level = logging.DEBUG if args.debug else logging.INFO
    logging.getLogger("sleep_pi_core").setLevel(app_level)

    # Bleak logs are very verbose; only enable when explicitly requested.
    bleak_level = logging.DEBUG if args.bleak_debug else logging.WARNING
    logging.getLogger("bleak").setLevel(bleak_level)


async def async_main(args: argparse.Namespace) -> None:
    #From the library pathlib, this creates a filesystem path, them makes an object that is usable in the code
    #Hence, making a parent directory makes a directory depending on the arguments given
    db_path = Path(args.db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    log = logging.getLogger("sleep_pi_core")
    setup_preflight(
        enable_ble=not args.no_ble,
        auto_setup=not args.no_auto_setup,
        audio_device=args.audio_device,
        speaker_volume=None if args.no_speaker_volume else args.speaker_volume,
        check_spi=not args.no_spi_check,
        log=log,
    )
    if args.preflight:
        return

    #Database is within the db file, MasterApp is within the ble_transport file
    #More detail within those files
    db = Database(db_path=db_path)
    app = MasterApp(db=db, log=log)

    #event loop is how the program is async in the first place
    #This returns and gets an active loop for later
    loop = asyncio.get_running_loop()

    #We imported signal above, it basically
    #It's more async stuff, it lets us have the keyboard interrupt later down, that's basically what SIGINT and SIGTERM are)
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            #Essentially error control, with the signal to stop the events as positional arguments within sig
            #Needing async stuff means most of main is kinda just one big debug function tbh
            loop.add_signal_handler(sig, app.stop_event.set)
        except NotImplementedError:
            pass

    if args.cli_test:
        ble_task = None
        if args.cli_test_ble:
            ble_task = asyncio.create_task(app.ble.run_forever(), name="ble-loop")
            app.log.info("CLI test BLE mode: waiting for watch connection...")
            while not app.ble.connected:
                await asyncio.sleep(0.2)
            app.log.info("CLI test BLE mode: watch connected")

        await app.run_cli_test_mode()

        if ble_task is not None:
            app.ble.request_stop()
            ble_task.cancel()
            try:
                await ble_task
            except asyncio.CancelledError:
                pass
        await app.shutdown()
        return

    #You know how Go has wait points so no parts of the program rush ahead? This is basically that
    await app.run(enable_ble=not args.no_ble)


def main() -> None:
    #parse_args is just prerequisite arguments you can put in for like, debugging and the like
    args = parse_args()
    configure_logging(args)
    #try is used in case of an error, and is used here so we can interrupt the program running with a Keyboard Interrupt
    #The interrupt is Ctrl + C
    try:
        #The async is used because there is concurrent parts of the program, the ble communication being a clear example
        #So to not have dependency issues we need to run it like this
        asyncio.run(async_main(args))
    except KeyboardInterrupt:
        pass

#Tells you if a python file is running itself as a standalone script or if it's imported as a module
#So the program will only run if main is executed directly
if __name__ == "__main__":
    main()
