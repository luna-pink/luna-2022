from discord.ext import commands
from .utilities import *


class WebhookCog(commands.Cog, name="Webhook customisation"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="wtitle",
        usage="<title>",
        description="Customize the webhook title"
    )
    async def wtitle(self, luna, *, newtitle: str):

        prints.message(
            f"Changed webhook title to » {color.print_gradient(f'{newtitle}')}"
        )
        if newtitle == "None":
            config.webhook.title("")
        else:
            config.webhook.title(f"{newtitle}")
        await message_builder(luna, description=f"```\nChanged webhook title to » {newtitle}```")

    @commands.command(
        name="wfooter",
        usage="<footer>",
        description="Customize the webhook footer"
    )
    async def wfooter(self, luna, *, newfooter: str):

        prints.message(
            f"Changed webhook footer to » {color.print_gradient(f'{newfooter}')}"
        )
        if newfooter == "None":
            config.webhook.footer("")
        else:
            config.webhook.footer(f"{newfooter}")
        await message_builder(luna, description=f"```\nChanged webhook footer to » {newfooter}```")

    @commands.command(
        name="wimage",
        usage="<url>",
        description="Customize the thumbnail image"
    )
    async def wimage(self, luna, newimageurl: str):

        prints.message(
            f"Changed webhook thumbnail url to » {color.print_gradient(f'{newimageurl}')}"
        )
        if newimageurl == "None":
            config.webhook.image_url("")
        else:
            config.webhook.image_url(f"{newimageurl}")
        await message_builder(luna, description=f"```\nChanged webhook thumbnail url to » {newimageurl}```")

    @commands.command(
        name="whexcolor",
        usage="<#hex>",
        description="Webhook hexadecimal color"
    )
    async def whexcolor(self, luna, newhexcolor: str):

        prints.message(
            f"Changed webhook color to » {color.print_gradient(f'{newhexcolor}')}"
        )
        if newhexcolor == "None":
            config.webhook.hex_color("")
        else:
            config.webhook.hex_color(f"{newhexcolor}")
        await message_builder(luna, description=f"```\nChanged webhook color to » {newhexcolor}```")