from bot.client import CustomBot
from bot.commands.create import setup_create_welcome_form_command
from bot.commands.ping import setup_ping_command
from bot.config import settings
from bot.events.on_member_join import setup_on_member_join
from bot.events.on_message import setup_on_message
from bot.events.on_presence_update import setup_on_presence_update
from bot.events.on_reaction_add import setup_on_reaction_add
from bot.events.on_ready import setup_on_ready
from bot.events.on_member_update.setup_on_member_update import setup_on_member_update
from bot.tasks.loop_task import start_background_tasks


custom_bot = CustomBot()


def register_events():
    setup_on_ready(custom_bot)
    setup_on_member_update(custom_bot)
    setup_on_presence_update(custom_bot)
    setup_on_member_join(custom_bot)
    setup_on_reaction_add(custom_bot)
    setup_on_message(custom_bot)


def register_commands():
    setup_ping_command(custom_bot)
    setup_create_welcome_form_command(custom_bot)


async def run_bot():
    register_events()
    register_commands()
    start_background_tasks(custom_bot)
    await custom_bot.start(settings.BOT_TOKEN)
