import asyncio
from bot.client import CustomBot
from bot.config import settings
from bot.commands.ping import setup_ping_command
from bot.events.on_member_join import setup_on_member_join
from bot.events.on_message import setup_on_message
from bot.events.on_presence_update import setup_on_presence_update
from bot.events.on_reaction_add import setup_on_reaction_add
from bot.events.on_ready import setup_on_ready
from bot.events.on_member_update.setup_on_member_update import setup_on_member_update
from bot.tasks.loop_task import start_background_tasks

bot = CustomBot()


def register_events():
    setup_on_ready(bot)
    setup_on_member_update(bot)
    setup_on_presence_update(bot)
    setup_on_member_join(bot)
    setup_on_reaction_add(bot)
    setup_on_message(bot)


def register_commands():
    setup_ping_command(bot)


async def run_bot():
    register_events()
    register_commands()
    start_background_tasks(bot)
    await bot.start(settings.BOT_TOKEN)


if __name__ == "__main__":
    asyncio.run(run_bot())
