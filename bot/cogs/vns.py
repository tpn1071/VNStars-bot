import discord
from discord import app_commands
from discord.ext import commands

class VNS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="VNS", description="Các lệnh của VNStars bot")
    async def vns(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hãy chọn một lệnh con!", ephemeral=True)

    @app_commands.command(name="role_clone", description="Clone role")
    async def role_clone(self, interaction: discord.Interaction):
        await interaction.response.send_message("Đây là lệnh clone role!")

    @app_commands.command(name="auto_tag", description="Auto tag")
    async def auto_tag(self, interaction: discord.Interaction):
        await interaction.response.send_message("Đây là lệnh auto tag!")

    @app_commands.command(name="help_suggest", description="Gợi ý lệnh")
    async def help_suggest(self, interaction: discord.Interaction):
        await interaction.response.send_message("Đây là lệnh gợi ý!")

    @vns.subcommand(name="role_clone", description="Clone role")
    async def vns_role_clone(self, interaction: discord.Interaction):
        await interaction.response.send_message("Đây là lệnh con /VNS role_clone!")

    @vns.subcommand(name="auto_tag", description="Auto tag")
    async def vns_auto_tag(self, interaction: discord.Interaction):
        await interaction.response.send_message("Đây là lệnh con /VNS auto_tag!")

    @vns.subcommand(name="help_suggest", description="Gợi ý lệnh")
    async def vns_help_suggest(self, interaction: discord.Interaction):
        await interaction.response.send_message("Đây là lệnh con /VNS help_suggest!")

async def setup(bot):
    await bot.add_cog(VNS(bot))