import discord
from typing import List


def has_added_role(
    before_roles: List[discord.Role],
    after_roles: List[discord.Role],
    role: discord.Role | None,
) -> bool:
    return role is not None and role in after_roles and role not in before_roles
