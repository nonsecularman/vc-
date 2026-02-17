import asyncio
from Zaid.main import start_bot


async def main():
    await start_bot()

    # loop alive रखेगा (py-tgcalls crash fix)
    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())
