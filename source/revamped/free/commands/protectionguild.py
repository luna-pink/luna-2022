from discord.ext import commands
from .utilities import *


class ProtectionGuildCog(commands.Cog, name="Protection Guild commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="pguilds",
        aliases=['pguild', 'protectguild'],
        usage="<guild_id>",
        description="Protect a guild"
    )
    async def pguilds(self, luna, guild_id: int):

        try:
            self.bot.get_guild(guild_id)
        except BaseException:
            await error_builder(luna, description="Invalid guild")
            return
        config._global(
            "data/protections/config.json",
            "guilds", guild_id, add=True
        )
        prints.message(
            f"Added » {color.print_gradient(f'{guild_id}')} to the list of protected guilds"
        )
        await message_builder(luna, description=f"```\nAdded » {guild_id} to the list of protected guilds```")

    @commands.command(
        name="rguilds",
        aliases=['rguild', 'removeguild'],
        usage="<guild_id>",
        description="Remove a protected guild"
    )
    async def rguilds(self, luna, guild_id: int):

        try:
            self.bot.get_guild(guild_id)
        except BaseException:
            await error_builder(luna, description="Invalid guild")
            return
        config._global(
            "data/protections/config.json",
            "guilds", guild_id, delete=True
        )
        prints.message(
            f"Removed » {color.print_gradient(f'{guild_id}')} from the list of protected guilds"
        )
        await message_builder(luna, description=f"```\nRemoved » {guild_id} from the list of protected guilds```")