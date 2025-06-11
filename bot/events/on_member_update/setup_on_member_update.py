from typing import Dict
from typing import Any
from bot.config import settings
import discord
from discord.ext import commands

from bot.events.on_member_update import (
    on_member_added_vi_member_role,
    on_member_added_vi_unknown_role,
)
from bot.events.on_member_update.on_member_added_en_member_role import (
    on_member_added_en_member_role,
)
from bot.events.on_member_update.on_member_added_en_unknown_role import (
    on_member_added_en_unknown_role,
)
from bot.events.on_member_update.on_member_added_unknown_role import (
    on_member_added_unknown_role,
)
from bot.helpers.has_added_role import has_added_role
from bot.utils.error_handler import catch_all_errors
from bot.utils.logging import log_function_call


def setup_on_member_update(bot: commands.Bot):

    @bot.event
    @catch_all_errors
    @log_function_call
    async def on_member_update(  # type:ignore
        before: discord.Member, after: discord.Member
    ):
        role_event_map: Dict[int, Any] = {
            settings.UNKNOWN_ROLE_ID: on_member_added_unknown_role,
            settings.VI_UNKNOWN_ROLE_ID: on_member_added_vi_unknown_role,
            settings.EN_UNKNOWN_ROLE_ID: on_member_added_en_unknown_role,
            settings.VI_MEMBER_ROLE_ID: on_member_added_vi_member_role,
            settings.EN_MEMBER_ROLE_ID: on_member_added_en_member_role,
        }

        # Kiểm tra các role đơn lẻ
        for role_id, handler in role_event_map.items():
            role = after.guild.get_role(role_id)
            if has_added_role(before.roles, after.roles, role):
                await handler(bot, before, after)
