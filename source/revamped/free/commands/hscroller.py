from discord.ext import commands
from .utilities import *


class HScrollerCog(commands.Cog, name="HScroller commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="anime",
        usage="",
        description="High quality anime"
    )
    async def anime(self, luna):
        r = requests.post(
            "http://project-atlas.xyz:8880/api/FetchMediaContent?amount=1&NSFWEnabled=false&NSFWType=None"
        ).json()
        await message_builder(luna, large_image=str(r[0]['FileURL']))

    @commands.command(
        name="nsfw",
        usage="",
        description="High quality nsfw"
    )
    async def nsfw(self, luna):
        r = requests.post(
            "http://project-atlas.xyz:8880/api/FetchMediaContent?amount=1&NSFWEnabled=true&NSFWType=nsfw"
        ).json()
        await message_builder(luna, large_image=str(r[0]['FileURL']))

    @commands.command(
        name="yuri",
        usage="",
        description="High quality yuri"
    )
    async def yuri(self, luna):
        r = requests.post(
            "http://project-atlas.xyz:8880/api/FetchMediaContent?amount=1&NSFWEnabled=true&NSFWType=yuri"
        ).json()
        await message_builder(luna, large_image=str(r[0]['FileURL']))