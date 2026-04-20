
from __future__ import annotations

import argparse
import asyncio
import logging
import signal
from pathlib import Path

from app import MasterApp
from config import DEFAULT_DB_PATH
from db import Database


def parse_args() -> argparse.Namespace:
    #Used in the command line to help add arguments during runtime, primarily used for debugging and the like
    #They should be all pretty self-explanatory
    parser = argparse.ArgumentParser(description="Simple overnight Pi sleep controller")
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH), help="SQLite database path")
    parser.add_argument("--no-ble", action="store_true", help="Disable BLE and use local test flow")
    parser.add_argument("--cli-test", action="store_true", help="Run interactive CLI test mode")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    return parser.parse_args()


async def async_main(args: argparse.Namespace) -> None:
    #From the library pathlib, this creates a filesystem path, them makes an object that is usable in the code
    #Hence, making a parent directory makes a directory depending on the arguments given
    db_path = Path(args.db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    #Database is within the db file, MasterApp is within the ble_transport file
    db = Database(db_path=db_path)
    app = MasterApp(db=db, log=logging.getLogger("sleep_pi_core"))

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, app.stop_event.set)
        except NotImplementedError:
            pass

    if args.cli_test:
        await app.run_cli_test_mode()
        await app.shutdown()
        return

    await app.run(enable_ble=not args.no_ble)


def main() -> None:
    #parse_args is just prerequisite arguments you can put in for like, debugging and the like
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
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
