from discord.ext import commands
from .utilities import *


class GamesCog(commands.Cog, name="Game commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="fnshop",
        usage="",
        description="Fortnite shop"
    )
    async def fnshop(self, luna):
        await message_builder(luna, title="Fortnite Shop", large_image="https://api.nitestats.com/v1/shop/image")

    @commands.command(
        name="fnmap",
        usage="",
        description="Fortnite map"
    )
    async def fnmap(self, luna):
        await message_builder(
            luna, title="Fortnite Map",
            large_image="https://media.fortniteapi.io/images/map.png?showPOI=true"
        )

    @commands.command(
        name="fnnews",
        usage="",
        description="Fortnite news"
    )
    async def fnnews(self, luna):
        fortnite = requests.get("https://fortnite-api.com/v2/news/br").json()
        await message_builder(luna, title="Fortnite News", large_image=fortnite["data"]["image"])
