import contextlib
import re
import time

import httpx
from discord.ext import commands
from luna import log
from dotjson import get_key, load_keys

load_keys(["data"])


class SniperCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        sniped_start_time = time.time()
        if message.author == self.bot.user:
            return
        with contextlib.suppress(BaseException):
            if 'discord.gift/' in message.content.lower():
                elapsed_snipe = '%.4fs' % (time.time() - sniped_start_time)
                code = re.search("discord.gift/(.*)", message.content)[1]
                if len(code) >= 16:
                    code = code[:16]
                    async with httpx.AsyncClient() as client:
                        start_time = time.time()
                        result = await client.post(
                            f'https://discord.com/api/v10/entitlements/gift-codes/{code}/redeem',
                            json={'channel_id': message.channel.id},
                            headers={'authorization': get_key("token"), 'user-agent': 'Mozilla/5.0'}
                        )
                        elapsed = '%.4fs' % (time.time() - start_time)
                    if 'nitro' in str(result.content):
                        status = 'Nitro successfully redeemed'
                    elif 'This gift has been redeemed already' in str(result.content):
                        status = 'Has been redeemed already'
                    else:
                        status = 'Unknown gift code'

                    log('sniper', f'Code from {message.author.name}\nCode: {code}\nSnipe: {elapsed_snipe}\nAPI: {elapsed}\nStatus: {status}')
