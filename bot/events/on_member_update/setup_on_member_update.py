import discord
from discord.ext import commands
from bot.config import settings

from bot.events.on_member_update import (
    on_member_added_unknown_role,
    on_member_added_vi_and_en_unknown_role,
    on_member_added_member_role,
)


def setup_on_member_update(bot: commands.Bot):
    @bot.event
    async def on_member_update(  # type:ignore
        before: discord.Member, after: discord.Member
    ):
        before_roles = set(before.roles)
        after_roles = set(after.roles)
        added_roles = after_roles - before_roles

        unknown_role = settings.UNKNOWN_ROLE_ID
        if unknown_role in added_roles:
            await on_member_added_unknown_role(before, after)

        await on_member_added_vi_and_en_unknown_role(before, after)

        member_role = settings.MEMBER_ROLE_ID
        if member_role in added_roles:
            await on_member_added_member_role(before, after)
