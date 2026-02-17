import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

async def runner():
    from Zaid.main import start_bot  # sirf function import

    for attempt in range(1, 6):
        try:
            await start_bot()
            return
        except Exception as e:
            logging.exception(f"start_bot failed (attempt {attempt}/5): {e}")
            await asyncio.sleep(5)

    raise SystemExit("Bot could not start after retries.")

if __name__ == "__main__":
    asyncio.run(runner())
