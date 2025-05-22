import discord
from discord.ext import commands
from discord import app_commands

class HelpSuggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="Gợi ý các lệnh phổ biến")
    @app_commands.describe(command="Tên lệnh bạn muốn tìm hiểu")
    @app_commands.autocomplete(command=lambda interaction, current: [
        app_commands.Choice(name=cmd, value=cmd)
        for cmd in ["role_clone", "auto_tag", "ping", "userinfo"] if current.lower() in cmd
    ])
    async def help_command(self, interaction: discord.Interaction, command: str = None):
        if command:
            await interaction.response.send_message(f"Thông tin về lệnh `{command}`: ...", ephemeral=True)
        else:
            await interaction.response.send_message(
                "Các lệnh phổ biến: role_clone, auto_tag, ping, userinfo", ephemeral=True
            )

    async def cog_load(self):
        # Đăng ký slash command khi cog được load
        self.bot.tree.add_command(self.help_command)

async def setup(bot):
    await bot.add_cog(HelpSuggest(bot))