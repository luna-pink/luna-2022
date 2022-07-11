from discord.ext import commands
from .utilities import *


ignore_list = []


class IgnoreCog(commands.Cog, name="Ignore commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="ignore",
        usage="<@user>",
        description="Ignore user DMs"
    )
    async def ignore(self, luna, *, user: discord.Member):

        global ignore_list
        if user.id in ignore_list:
            await message_builder(luna, title="Ignore", description=f"```\n{user} is already ignored```")
            return
        ignore_list.append(user.id)
        await message_builder(luna, title="Ignore", description=f"```\n{user} is now ignored```")

    @commands.command(
        name="unignore",
        usage="<@user>",
        description="Unignore user DMs"
    )
    async def unignore(self, luna, *, user: discord.Member):

        global ignore_list
        if user.id not in ignore_list:
            await message_builder(luna, title="Unignore", description=f"```\n{user} is not ignored```")
            return
        ignore_list.remove(user.id)
        await message_builder(luna, title="Unignore", description=f"```\n{user} is now unignored```")

    @commands.command(
        name="ignorelist",
        usage="",
        description="List ignored users"
    )
    async def ignorelist(self, luna):

        global ignore_list
        if len(ignore_list) == 0:
            await message_builder(luna, title="Ignorelist", description=f"```\nNo users are ignored```")
            return
        await message_builder(luna, title="Ignorelist", description=f"```\n{ignore_list}```")

    @commands.command(
        name="ignorelistclear",
        usage="",
        description="Clear ignore list"
    )
    async def ignorelistclear(self, luna):

        global ignore_list
        if len(ignore_list) == 0:
            await message_builder(luna, title="Ignorelist", description=f"```\nNo users are ignored```")
            return
        ignore_list.clear()
        await message_builder(luna, title="Ignorelist", description=f"```\nIgnore list is now cleared```")