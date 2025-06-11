from typing import Any
import discord


class WelcomeForumThreadForm(discord.ui.Modal):
    # Khai báo kiểu rõ ràng để tránh Pylance warning
    language: Any
    title_input: Any
    content: Any

    def __init__(self):
        super().__init__(title="Tạo Welcome Forum Thread")

        self.language = discord.ui.TextInput(
            label="Ngôn ngữ",
            style=discord.TextStyle.short,
            placeholder="Nhập `vi` hoặc `en`",
            required=True,
        )
        self.title_input = discord.ui.TextInput(
            label="Tiêu đề", placeholder="Nhập tiêu đề", required=True
        )
        self.content = discord.ui.TextInput(
            label="Nội dung",
            style=discord.TextStyle.paragraph,
            placeholder="Nhập nội dung",
            required=True,
        )

        # Thêm các TextInput vào modal
        self.add_item(self.language)
        self.add_item(self.title_input)
        self.add_item(self.content)

    async def on_submit(self, interaction: discord.Interaction):
        lang = self.language.value.strip().lower()

        if lang not in ["vi", "en"]:
            await interaction.response.send_message(
                "❌ Ngôn ngữ phải là `vi` hoặc `en`.",
                ephemeral=True,
            )
            return

        if not interaction.guild:
            return

        thread = await interaction.client.fetch_channel(1382170144725532783)

        if thread and isinstance(thread, discord.Thread):
            await thread.join()
            await thread.send(
                f"[Ngôn ngữ]\n"
                f"{self.language.value}\n"
                f"[Tiêu đề]\n"
                f"{self.title_input.value}\n"
                f"[Nội dung]\n"
                f"{self.content.value}",
            )

            await interaction.response.send_message(
                f"✅ Đã gửi bài viết vào {thread.jump_url}", ephemeral=False
            )


class OpenModalButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)  # View không bị timeout

    @discord.ui.button(
        label="Tạo bài viết chào mừng Hội Viên mới", style=discord.ButtonStyle.primary
    )
    async def open_modal(
        self, interaction: discord.Interaction, button: discord.ui.Button  # type:ignore
    ):
        await interaction.response.send_modal(WelcomeForumThreadForm())
