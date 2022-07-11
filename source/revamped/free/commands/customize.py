from discord.ext import commands
from .utilities import *


class CustomizeCog(commands.Cog, name="Customization commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="ctitle",
        usage="<title>",
        description="Customize the title"
    )
    async def ctitle(self, luna, *, newtitle: str):

        if files.json(
                "data/config.json",
                "theme",
                documents=False
        ) == "default":
            await error_builder(
                luna,
                f"```\nYou can't change the title if you're using the default theme\n```"
                f"```\nPlease change the theme first with {get_prefix()}theme\n\n"
                f"({get_prefix()}themes to show all available themes)```"
            )
        else:
            prints.message(f"Changed title to » {color.print_gradient(f'{newtitle}')}")
            if newtitle == "None":
                config.title("")
            else:
                config.title(f"{newtitle}")
            await message_builder(luna, description=f"```\nChanged title to » {newtitle}```")

    @commands.command(
        name="cfooter",
        usage="<footer>",
        description="Customize the footer"
    )
    async def cfooter(self, luna, *, newfooter: str):

        if files.json(
                "data/config.json",
                "theme",
                documents=False
        ) == "default":
            await error_builder(
                luna,
                f"```\nYou can't change the footer if you're using the default theme\n```"
                f"```\nPlease change the theme first with {get_prefix()}theme\n\n"
                f"({get_prefix()}themes to show all available themes)```"
            )
        else:
            prints.message(
                f"Changed footer to » {color.print_gradient(f'{newfooter}')}"
            )
            if newfooter == "None":
                config.footer("")
            else:
                config.footer(f"{newfooter}")
            await message_builder(luna, description=f"```\nChanged footer to » {newfooter}```")

    @commands.command(
        name="description",
        aliases=['cdescription'],
        usage="<on/off>",
        description="Hide/Show <> | []"
    )
    async def description(self, luna, mode: str):

        if files.json(
                "data/config.json",
                "theme",
                documents=False
        ) == "default":
            await error_builder(
                luna,
                f"```\nYou can't change the description mode if you're using the default theme\n```"
                f"```\nPlease change the theme first with {get_prefix()}theme\n\n"
                f"({get_prefix()}themes to show all available themes)```"
            )
        elif mode == "off":
            prints.message(
                f"Changed description to » {color.print_gradient('off')}"
            )
            config.description(False)
            await message_builder(luna, description=f"```\nChanged description to » off```")
        elif mode == "on":
            prints.message(
                f"Changed description to » {color.print_gradient('on')}"
            )
            config.description(True)
            await message_builder(luna, description=f"```\nChanged description to » on```")
        else:
            await mode_error(luna, "on or off")
