import asyncio
import time
from Zaid.main import start_bot


async def main():
    # Heroku boot time sync fix
    await asyncio.sleep(5)

    await start_bot()


if __name__ == "__main__":
    asyncio.run(main())
