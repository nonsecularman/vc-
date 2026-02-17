import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls, idle

API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"
SESSION_NAME = "my_account"


# =========================
# CLIENTS
# =========================

app = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH
)

pytgcalls = PyTgCalls(app)


# =========================
# START BOT
# =========================

async def start_bot():
    print("🚀 Starting Bot...")

    await app.start()
    await pytgcalls.start()

    me = await app.get_me()
    print(f"✅ Logged in as: {me.first_name}")

    print("🎵 Music Bot Running...")
    await idle()


# =========================
# MAIN ENTRY
# =========================

if __name__ == "__main__":
    asyncio.run(start_bot())
