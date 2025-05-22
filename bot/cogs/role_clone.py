class RoleCloneCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def clonerolegui(self, ctx):
        roles = [
            r for r in ctx.guild.roles
            if r != ctx.guild.default_role and r.position < ctx.guild.me.top_role.position
        ]
        if not roles:
            await ctx.send("❌ Không có role nào để clone.")
            return

        await ctx.send("🧩 Chọn role để clone:", view=RoleDropdown(roles))

class RoleNameModal(discord.ui.Modal, title="Nhập tên role mới"):
    def __init__(self, role: discord.Role):
        super().__init__()
        self.role = role
        self.new_name_input = discord.ui.TextInput(label="Tên role mới", placeholder="VD: Mod 2", required=False)
        self.add_item(self.new_name_input)

    async def on_submit(self, interaction: discord.Interaction):
        new_name = self.new_name_input.value or f"{self.role.name} Clone"
        try:
            cloned = await interaction.guild.create_role(
                name=new_name,
                permissions=self.role.permissions,
                colour=self.role.colour,
                hoist=self.role.hoist,
                mentionable=self.role.mentionable,
                reason=f"Cloned from {self.role.name} by {interaction.user}"
            )
            await interaction.response.send_message(f"✅ Đã clone role **{self.role.name}** thành **{cloned.name}**", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("❌ Bot không đủ quyền để clone role này.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Lỗi: {e}", ephemeral=True)

class RoleDropdown(discord.ui.View):
    def __init__(self, roles):
        super().__init__(timeout=60)
        self.add_item(RoleSelect(roles))

class RoleSelect(discord.ui.Select):
    def __init__(self, roles):
        options = [
            discord.SelectOption(label=role.name, value=str(role.id))
            for role in roles
        ]
        super().__init__(placeholder="Chọn role cần clone", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        role_id = int(self.values[0])
        role = discord.utils.get(interaction.guild.roles, id=role_id)
        if role:
            await interaction.response.send_modal(RoleNameModal(role))

def setup(bot):
    bot.add_cog(RoleCloneCog(bot))