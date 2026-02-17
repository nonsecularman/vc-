import asyncio
import logging

logging.basicConfig(level=logging.INFO)

async def runner():
    from Zaid.main import start_bot, bot  # bot object import

    for attempt in range(1, 11):
        try:
            await start_bot()
            return
        except Exception as e:
            logging.exception(f"Start failed attempt {attempt}/10: {e}")
            # cleanup so next retry doesn't hit "already connected"
            try:
                if bot.is_connected:
                    await bot.stop()
            except Exception:
                pass
            await asyncio.sleep(10)

    raise SystemExit("Failed to start after retries")

if __name__ == "__main__":
    asyncio.run(runner())
