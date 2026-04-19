"""Entry point for the new simple overnight Pi implementation."""

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
    parser = argparse.ArgumentParser(description="Simple overnight Pi sleep controller")
    parser.add_argument("--db-path", default=str(DEFAULT_DB_PATH), help="SQLite database path")
    parser.add_argument("--no-ble", action="store_true", help="Disable BLE and use local test flow")
    parser.add_argument("--cli-test", action="store_true", help="Run interactive CLI test mode")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    return parser.parse_args()


async def async_main(args: argparse.Namespace) -> None:
    db_path = Path(args.db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

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
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    try:
        asyncio.run(async_main(args))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
