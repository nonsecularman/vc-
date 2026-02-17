import asyncio
import signal
from Zaid.main import start_bot


async def main():
    # bot start
    await start_bot()

    # bot को exit होने से रोकता है
    stop_event = asyncio.Event()

    for sig in (signal.SIGINT, signal.SIGTERM):
        asyncio.get_event_loop().add_signal_handler(
            sig, stop_event.set
        )

    await stop_event.wait()


if __name__ == "__main__":
    asyncio.run(main())
