from keep_alive import keep_alive
import asyncio
from bot.main import run_bot

def main():
    keep_alive()
    asyncio.run(run_bot())

if __name__ == "__main__":
    main()
