from discord.ext import commands
from .utilities import *


class ToastCog(commands.Cog, name="Toast customization"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="toasticon",
        usage="<icon.ico>",
        description="Customize the toast icon"
    )
    async def toasticon(self, luna, *, newicon: str):

        if newicon.endswith(".ico"):
            prints.message(
                f"Changed toast icon to » {color.print_gradient(f'{newicon}')}"
            )
            config.toast.icon(f"{newicon}")
            await message_builder(luna, description=f"```\nChanged toast icon to » {newicon}```")
        else:
            await error_builder(luna, description=f"```\nNot a valid icon file (.ico)```")

    @commands.command(
        name="toasttitle",
        usage="<title>",
        description="Customize the toast title"
    )
    async def toasttitle(self, luna, *, newtitle: str):

        prints.message(
            f"Changed toast title to » {color.print_gradient(f'{newtitle}')}"
        )
        if newtitle == "None":
            config.toast.title("")
        else:
            config.toast.title(f"{newtitle}")
        await message_builder(luna, description=f"```\nChanged toast title to » {newtitle}```")