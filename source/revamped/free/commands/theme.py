from discord.ext import commands
from .utilities import *


class ThemeCog(commands.Cog, name="Theme command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="theme",
        usage="<theme>",
        description="Change theme"
    )
    async def theme(self, luna, theme: str):

        theme = theme.replace('.json', '')
        if theme == "default":
            config.theme(theme)
            await message_builder(luna, description=f"```\nChanged theme to » {theme}```")
        elif files.file_exist(f"data/themes/{theme}.json", documents=False):
            config.theme(theme)
            await message_builder(luna, description=f"```\nChanged theme to » {theme}```")
        else:
            await error_builder(luna, description=f"```\nThere is no theme called » {theme}```")