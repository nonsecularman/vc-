import random

from config import (
    API_HASH,
    API_ID,
    BOT_TOKEN,
    STRING_SESSION,
    SESSION2,
    SESSION3,
    SESSION4,
    SESSION5,
)

# ✅ IMPORTANT (idle pyrogram से लेना है)
from pyrogram import Client, idle
from pytgcalls import PyTgCalls


# ================= BOT CLIENT =================

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Zaid.Player"},
)


# ================= ASSISTANT CLIENTS =================
# Pyrogram 1.4.12 में session_string use नहीं होता

ASS_CLI_1 = (
    Client(STRING_SESSION, api_id=API_ID, api_hash=API_HASH)
    if STRING_SESSION and STRING_SESSION != "None"
    else None
)

user = (
    Client(SESSION2, api_id=API_ID, api_hash=API_HASH)
    if SESSION2 and SESSION2 != "None"
    else None
)

user3 = (
    Client(SESSION3, api_id=API_ID, api_hash=API_HASH)
    if SESSION3 and SESSION3 != "None"
    else None
)

user4 = (
    Client(SESSION4, api_id=API_ID, api_hash=API_HASH)
    if SESSION4 and SESSION4 != "None"
    else None
)

user5 = (
    Client(SESSION5, api_id=API_ID, api_hash=API_HASH)
    if SESSION5 and SESSION5 != "None"
    else None
)


# ================= PYTG CALLS =================

call_py = PyTgCalls(ASS_CLI_1) if ASS_CLI_1 else None
call_py2 = PyTgCalls(user) if user else None
call_py3 = PyTgCalls(user3) if user3 else None
call_py4 = PyTgCalls(user4) if user4 else None
call_py5 = PyTgCalls(user5) if user5 else None


random_assistant = []


# ================= START BOT =================

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")

    # Start Bot
    await bot.start()
    me_bot = await bot.get_me()
    print(f"[INFO]: Bot started as @{me_bot.username}")

    # Assistant 1
    if ASS_CLI_1:
        await ASS_CLI_1.start()
        if call_py:
            await call_py.start()
        random_assistant.append(1)

    # Assistant 2
    if user:
        await user.start()
        if call_py2:
            await call_py2.start()
        random_assistant.append(2)

    # Assistant 3
    if user3:
        await user3.start()
        if call_py3:
            await call_py3.start()
        random_assistant.append(3)

    # Assistant 4
    if user4:
        await user4.start()
        if call_py4:
            await call_py4.start()
        random_assistant.append(4)

    # Assistant 5
    if user5:
        await user5.start()
        if call_py5:
            await call_py5.start()
        random_assistant.append(5)

    random_assistant.append(6)

    print("[INFO]: All clients started successfully.")
    print("[INFO]: Bot is now idle...")

    # ✅ bot alive रहेगा
    await idle()
