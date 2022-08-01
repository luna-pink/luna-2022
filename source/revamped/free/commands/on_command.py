import contextlib
from discord.ext import commands
from .utilities import *
import asyncio


class OnCommand(commands.Cog, name="on command"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command(self, luna: commands.Context):
        with contextlib.suppress(discord.NotFound, AttributeError, RuntimeError):
            if "mreact" not in luna.command.name:
                await asyncio.sleep(0)
                await luna.message.delete()
        global last_used
        if luna.command.name != "repeat":
            last_used = luna.command.name
        prints.command(luna.command.name)
        theme_json = files.json("data/config.json", "theme", documents=False)
        try:
            if theme_json != "default":
                files.json(
                    f"data/themes/{theme_json}",
                    "title", documents=False
                )
        except BaseException:
            config.theme("default")
            await error_builder(
                luna,
                description=f"```\nThe configurated theme file was missing and has been set to \"default\"```"
            )
        return