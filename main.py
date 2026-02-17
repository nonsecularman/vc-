import asyncio
import logging

logging.basicConfig(level=logging.INFO)

async def runner():
    from Zaid.main import start_bot
    await start_bot()

if __name__ == "__main__":
    asyncio.run(runner())
