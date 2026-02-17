import asyncio
from pytgcalls import PyTgCalls
from pyrogram import Client

class MeraBot:
    def __init__(self):
        self.app = Client("my_account", 
                         api_id="YOUR_API_ID",
                         api_hash="YOUR_API_HASH")
        self.pytgcalls = PyTgCalls(self.app)
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
    
    async def start(self):
        """Bot ko start karo"""
        await self.app.start()
        await self.pytgcalls.start()
        print("✅ Bot successfully start ho gaya!")
    
    async def stop(self):
        """Bot ko properly band karo"""
        print("🛑 Bot band ho raha hai...")
        await self.pytgcalls.stop()
        await self.app.stop()
        print("✅ Bot sahi se band ho gaya!")
    
    def run(self):
        """Bot ko chalaao"""
        try:
            self.loop.run_until_complete(self.start())
            print("🤖 Bot chal raha hai...")
            self.loop.run_forever()
        except KeyboardInterrupt:
            print("\n⚠️ Keyboard se interrupt kiya gaya")
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            self.loop.run_until_complete(self.stop())
            self.loop.close()
            print("👋 Bye!")

if __name__ == "__main__":
    bot = MeraBot()
    bot.run()
