from discord.ext import commands
from .utilities import *


class HentaiCog(commands.Cog, name="Hentai commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="hrandom",
        usage="",
        description="Random hentai"
    )
    async def hrandom(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/hentai"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="hass",
        usage="",
        description="Random hentai ass"
    )
    async def hass(self, luna):
        r = requests.get(
            "https://nekobot.xyz/api/image?type=hass"
        ).json()
        await message_builder(luna, large_image=str(r['message']))

    @commands.command(
        name="ass",
        usage="",
        description="Random ass"
    )
    async def ass(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/ass"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="boobs",
        usage="",
        description="Real breasts"
    )
    async def ass(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/boobs"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="pussy",
        usage="",
        description="Random pussy"
    )
    async def pussy(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/pussy"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="4k",
        usage="",
        description="4k NSFW"
    )
    async def fk(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/4k"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="cum",
        usage="",
        description="Baby gravy!"
    )
    async def cum(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/cum"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="hblowjob",
        usage="",
        description="Self explainable"
    )
    async def blowjob(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/blowjob"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="ahegao",
        usage="",
        description="Ahegao"
    )
    async def ahegao(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/gasm"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="lewd",
        usage="",
        description="Lewd loli"
    )
    async def lewd(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/lewd"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="feet",
        usage="",
        description="Random feet"
    )
    async def feet(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/feet"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="feet",
        usage="",
        description="Random feet"
    )
    async def feet(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/feet"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="lesbian",
        usage="",
        description="Girls rule!"
    )
    async def lesbian(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/lesbian"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="spank",
        usage="",
        description="NSFW for butts"
    )
    async def spank(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/spank"
        ).json()
        await message_builder(luna, large_image=str(r['image']))

    @commands.command(
        name="hwallpaper",
        usage="",
        description="99% SFW"
    )
    async def hwallpaper(self, luna):
        r = requests.get(
            "http://api.nekos.fun:8080/api/wallpaper"
        ).json()
        await message_builder(luna, large_image=str(r['image']))