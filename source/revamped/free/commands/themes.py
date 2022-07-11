from discord.ext import commands
from .utilities import *


class ThemesCog(commands.Cog, name="Theme commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="newtheme",
        usage="<name>",
        description="Create a theme"
    )
    async def newtheme(self, luna, themename: str):

        themename = themename.replace('.json', '')
        if files.file_exist(f"data/themes/{themename}.json", documents=False):
            await error_builder(luna, description=f"```\nA theme already exists with the name » {themename}```")
        else:
            prints.message(f"Created theme » {color.print_gradient(f'{themename}')}")
            data = {
                "title": "Luna",
                "footer": "www.team-luna.org",
                "description": True
            }
            files.write_json(
                f"data/themes/{themename}.json", data, documents=False
            )
            config.theme(f"{themename}")
            await message_builder(luna, description=f"```\nCreated theme » {themename}```")

    @commands.command(
        name="edittheme",
        usage="<name>",
        description="Edit current theme name"
    )
    async def edittheme(self, luna, themename: str):

        themesvar = files.json("data/config.json", "theme", documents=False)
        if files.file_exist(f"data/themes/{themename}.json", documents=False):
            await error_builder(luna, description=f"```\nA theme already exists with the name » {themename}```")
        else:
            prints.message(
                f"Edited theme name to » {color.print_gradient(f'{themename}')}"
            )
            os.rename(
                f"data/themes/{themesvar}",
                f"data/themes/{themename}.json"
            )
            config.theme(f"{themename}")
            await message_builder(luna, description=f"```\nEdited theme name to » {themename}```")

    @commands.command(
        name="deltheme",
        usage="<name>",
        description="Delete a theme"
    )
    async def deltheme(self, luna, themename: str):

        themename = themename.replace('.json', '')
        themesvar = files.json("data/config.json", "theme", documents=False)
        if themesvar == f"{themename}.json":
            await error_builder(luna, description="```\nYou cant delete the theme you are currently using```")
            return
        if files.file_exist(f"data/themes/{themename}.json", documents=False):
            files.remove(f"data/themes/{themename}.json", documents=False)
            prints.message(f"Deleted theme » {color.print_gradient(f'{themename}')}")
            await message_builder(luna, description=f"```\nDeleted theme » {themename}```")
        else:
            await error_builder(luna, description=f"```\nThere is no theme called » {themename}```")

    @commands.command(
        name="sendtheme",
        usage="",
        description="Send the current theme file"
    )
    async def sendtheme(self, luna):

        themesvar = files.json("data/config.json", "theme", documents=False)
        await luna.send(file=discord.File(f"data/themes/{themesvar}"))

    @commands.command(
        name="cthemes",
        aliases=['communitythemes'],
        usage="",
        description="Community made themes"
    )
    async def cthemes(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)
        await message_builder(
            luna, title="Community Themes",
            description=f"{theme.description()}"
                        f"```\n{prefix}preview <theme>  » Preview a theme\n```"
                        f"```\n{prefix}install luna     » Luna theme\n"
                        f"{prefix}install lunaanimated » Luna theme\n"
                        f"{prefix}install chill    » Chill theme\n"
                        f"{prefix}install midnight » Midnight theme\n"
                        f"{prefix}install vaporwave » Vaporwave theme\n"
                        f"{prefix}install sweetrevenge » Sweetrevenge theme\n"
                        f"{prefix}install error    » Error theme\n"
                        f"{prefix}install lunapearl » Pearl theme\n"
                        f"{prefix}install gamesense » Gamesense theme\n"
                        f"{prefix}install aimware  » Aimware theme\n"
                        f"{prefix}install guilded  » Guilded theme\n"
                        f"{prefix}install lucifer  » Lucifer selfbot theme\n"
                        f"{prefix}install nighty   » Nighty selfbot theme\n"
                        f"{prefix}install aries    » Aries selfbot theme```"
        )