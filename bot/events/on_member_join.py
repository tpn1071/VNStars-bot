import discord
from discord.ext import commands
from bot.config import settings


def setup_on_member_join(bot: commands.Bot):
    @bot.event
    async def on_member_join(member: discord.Member):  # type:ignore
        await add_unknown_role(member)

        # log check run
        print(f"on_member_join: {member.name} ({member.id})")


# Hàm này sẽ thêm vai trò "Unknown" cho thành viên mới tham gia
async def add_unknown_role(member: discord.Member):
    role_id = settings.UNKNOWN_ROLE_ID
    role = member.guild.get_role(role_id)
    if role:
        try:
            await member.add_roles(role)
            # log để xem hàm chạy chưa
            print(f"Added role {role.name} to {member.name}")
        except discord.Forbidden:
            print(f"Failed to add role {role.name} to {member.name}: Forbidden")
        except discord.HTTPException as e:
            print(f"Failed to add role {role.name} to {member.name}: {e}")
    else:
        print(f"Role with ID {role_id} not found in guild {member.guild.name}")

    # log check run
    print(f"add_unknown_role_on_member_join: {member.name} ({member.id})")
