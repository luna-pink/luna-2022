from discord.ext import commands
from .utilities import *


class ShareCog(commands.Cog, name="Share commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="share",
        usage="<on/off>",
        description="Share on/off"
    )
    async def share(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Share » {color.print_gradient(f'{mode}')}")
            config.share(mode)
            await message_builder(luna, description=f"```\nShare » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="shareuser",
        usage="<@member>",
        description="Set the member for sharing"
    )
    async def shareuser(self, luna, user_id):

        if "<@!" and ">" in user_id:
            user_id = user_id.replace("<@!", "").replace(">", "")
            user = await self.bot.fetch_user(user_id)
        else:
            user = await self.bot.fetch_user(user_id)
        if user == self.bot.user:
            await error_builder(luna, description=f"```\nYou can't use share on yourself```")
            return
        config.user_id(user.id)
        prints.message(f"Share user set to » {color.print_gradient(f'{user}')}")
        await message_builder(luna, description=f"```\nShare user set to » {user}```")

    @commands.command(
        name="sharenone",
        usage="",
        description="Share member to none"
    )
    async def sharenone(self, luna):

        config.user_id("")
        prints.message(f"Share user set to » None")
        await message_builder(luna, description=f"```\nShare user set to » None```")