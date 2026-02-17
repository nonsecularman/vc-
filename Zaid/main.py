import random
from config import API_HASH, API_ID, BOT_TOKEN, STRING_SESSION, SESSION2, SESSION3, SESSION4, SESSION5

from pyrogram import Client
from pytgcalls import PyTgCalls, idle

# BOT client
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Zaid.Player"},
)

# Assistants (strings should be empty/None if not used)
ASS_CLI_1 = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH) if SESSION_NAME and SESSION_NAME != "None" else None
user     = Client(SESSION2,     api_id=API_ID, api_hash=API_HASH) if SESSION2     and SESSION2     != "None" else None
user3    = Client(SESSION3,     api_id=API_ID, api_hash=API_HASH) if SESSION3     and SESSION3     != "None" else None
user4    = Client(SESSION4,     api_id=API_ID, api_hash=API_HASH) if SESSION4     and SESSION4     != "None" else None
user5    = Client(SESSION5,     api_id=API_ID, api_hash=API_HASH) if SESSION5     and SESSION5     != "None" else None

# PyTgCalls (sirf jab client exist kare tab start karna)
call_py  = PyTgCalls(ASS_CLI_1) if ASS_CLI_1 else None
call_py2 = PyTgCalls(user)      if user      else None
call_py3 = PyTgCalls(user3)     if user3     else None
call_py4 = PyTgCalls(user4)     if user4     else None
call_py5 = PyTgCalls(user5)     if user5     else None

random_assistant = []

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")

    # Start bot
    await bot.start()
    me_bot = await bot.get_me()
    print(f"[INFO]: Bot started as @{me_bot.username} (id={me_bot.id})")

    # Start assistants + calls safely
    if ASS_CLI_1:
        await ASS_CLI_1.start()
        if call_py:
            await call_py.start()
        random_assistant.append(1)

    if user:
        await user.start()
        if call_py2:
            await call_py2.start()
        random_assistant.append(2)

    if user3:
        await user3.start()
        if call_py3:
            await call_py3.start()
        random_assistant.append(3)

    if user4:
        await user4.start()
        if call_py4:
            await call_py4.start()
        random_assistant.append(4)

    if user5:
        await user5.start()
        if call_py5:
            await call_py5.start()
        random_assistant.append(5)

    # Extra value tum rakh rahe the, keep it
    random_assistant.append(6)

    print("[INFO]: All clients started. Going idle...")
    await idle()
