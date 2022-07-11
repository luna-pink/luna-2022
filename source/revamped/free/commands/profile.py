from discord.ext import commands
from .utilities import *


class ProfileCog(commands.Cog, name="Profile commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="online",
        usage="",
        description="Online status"
    )
    async def online(self, luna):

        payload = {'status': "online"}
        requests.patch(
            f'https://discord.com/api/{api_version}/users/@me/settings',
            json=payload,
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(luna, description="```\nSet status to online```")

    @commands.command(
        name="idle",
        usage="",
        description="Idle status"
    )
    async def idle(self, luna):

        payload = {'status': "idle"}
        requests.patch(
            f'https://discord.com/api/{api_version}/users/@me/settings',
            json=payload,
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(luna, description="```\nSet status to idle```")

    @commands.command(
        name="dnd",
        usage="",
        description="Do not disturb status"
    )
    async def dnd(self, luna):

        payload = {'status': "dnd"}
        requests.patch(
            f'https://discord.com/api/{api_version}/users/@me/settings',
            json=payload,
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(luna, description="```\nSet status to do not disturb```")

    @commands.command(
        name="offline",
        usage="",
        description="Offline status"
    )
    async def offline(self, luna):

        payload = {'status': "invisible"}
        requests.patch(
            f'https://discord.com/api/{api_version}/users/@me/settings',
            json=payload,
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(luna, description="```\nSet status to offline/invisible```")

    @commands.command(
        name="startup",
        usage="<online/idle/dnd/offline>",
        description="Startup status"
    )
    async def startup(self, luna, mode: str = None):

        if mode == "online" or mode == "idle" or mode == "dnd" or mode == "offline":
            prints.message(f"Startup status » {color.print_gradient(f'{mode}')}")
            config.startup_status(mode)
            await message_builder(luna, description=f"```\nStartup status » {mode}```")
        elif mode is None:
            startup_status = configs.startup_status()
            await message_builder(luna, description=f"```\nCurrent startup status » {startup_status}```")
        else:
            await mode_error(luna, "online, idle, dnd or offline")

    @commands.command(
        name="cstatus",
        usage="<text>",
        description="Custom status"
    )
    async def cstatus(self, luna, text: str):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Content-Type': 'application/json',
            'authorization': user_token
        }
        setting = {
            "custom_status": {"text": text}
        }
        requests.patch(
            f"https://discord.com/api/{api_version}/users/@me/settings",
            headers=headers,
            json=setting
        ).json()
        await message_builder(luna, description=f"```\nChanged custom status to » {text}```")

