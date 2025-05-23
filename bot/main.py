import asyncio
from bot.client import CustomBot
from bot.config import settings
from bot.events.on_presence_update import setup_on_presence_update
from bot.tasks.loop_task import start_background_tasks
from bot.events.on_ready import setup_on_ready
from bot.events.on_member_update import setup_on_member_update
from bot.commands.ping import setup_ping_command

bot = CustomBot()


def register_events():
    setup_on_ready(bot)
    setup_on_member_update(bot)
    setup_on_presence_update(bot)


def register_commands():
    setup_ping_command(bot)


async def run_bot():
    register_events()
    register_commands()
    start_background_tasks(bot)
    await bot.start(settings.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(run_bot())
