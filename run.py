import asyncio
from keep_alive import keep_alive
from bot.main import run_bot

if __name__ == "__main__":
    keep_alive()
    asyncio.run(run_bot())
