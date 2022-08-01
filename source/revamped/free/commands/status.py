from discord.ext import commands
from .utilities import *


class StatusCog(commands.Cog, name="Animated statuses"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="status",
        usage="<text>",
        description="Set a custom status"
    )
    async def status(self, luna, text: str):
        payload = {'custom_status': {"text": f"{text}"}}
        requests.patch(
            f'https://discord.com/api/{api_version}/users/@me/settings',
            json=payload,
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(luna, description=f"```\nSet custom status to » {text}```")

    @commands.command(
        name="removestatus",
        usage="",
        description="Remove custom status"
    )
    async def removestatus(self, luna):
        payload = {'custom_status': {"text": ""}}
        requests.patch(
            f'https://discord.com/api/{api_version}/users/@me/settings',
            json=payload,
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(luna, description=f"```\nRemoved custom status```")