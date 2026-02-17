import asyncio
import logging

logging.basicConfig(level=logging.INFO)

async def runner():
    from Zaid.main import start_bot

    for attempt in range(1, 11):
        try:
            await start_bot()
            return
        except Exception as e:
            logging.exception(f"Start failed attempt {attempt}/10: {e}")
            await asyncio.sleep(10)

    raise SystemExit("Failed to start after retries")

if __name__ == "__main__":
    asyncio.run(runner())
