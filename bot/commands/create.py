from discord.ext import commands

from bot.ui.welcome_forum_thread_form import OpenModalButton, WelcomeForumThreadForm
from bot.utils.error_handler import catch_all_errors
from bot.utils.logging import log_function_call


def setup_create_welcome_form_command(bot: commands.Bot):
    @bot.command(name="open_form_button")
    @catch_all_errors
    @log_function_call
    async def open_form_button(ctx: commands.Context[commands.Bot]):  # type:ignore
        view = OpenModalButton()
        await ctx.send(view=view)
