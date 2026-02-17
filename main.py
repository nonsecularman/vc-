import asyncio
import logging

logging.basicConfig(level=logging.INFO)

async def runner():
    from Zaid.main import start_bot
    from pytgcalls import idle

    for attempt in range(1, 6):
        try:
            await start_bot()
            break
        except Exception as e:
            logging.exception(f"start_bot() failed (attempt {attempt}/5): {e}")
            await asyncio.sleep(5)
    else:
        raise SystemExit("Bot could not start after retries.")

    await idle()

if __name__ == "__main__":
    asyncio.run(runner())
