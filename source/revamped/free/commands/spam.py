from discord.ext import commands
from .utilities import *
import asyncio


class SpamCog(commands.Cog, name="Spam commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="spam",
        usage="<delay> <amount> <message>",
        description="Spammer"
    )
    async def spam(self, luna, delay: int, amount: int, *, message: str):

        if configs.risk_mode() == "on":
            try:
                for each in range(0, amount):
                    await asyncio.sleep(delay)
                    await luna.send(f"{message}")
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="spamdm",
        usage="<delay> <amount> <@user> <message>",
        description="DMs"
    )
    async def spamdm(self, luna, delay: int, amount: int, user: discord.User, *, message: str):

        if configs.risk_mode() == "on":
            try:
                for each in range(0, amount):
                    await asyncio.sleep(delay)
                    await user.send(f"{message}")
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="spamch",
        usage="<delay> <amount> <message>",
        description="Channels"
    )
    async def spamch(self, luna, delay: int, amount: int, *, message: str):

        if configs.risk_mode() == "on":
            try:
                for each in range(0, amount):
                    for _ in luna.guild.text_channels:
                        try:
                            await asyncio.sleep(delay)
                            await message.channel.send(f"{message}")
                        except Exception as e:
                            await error_builder(luna, description=f"```{e}```")
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="spamgp",
        usage="<delay> <amount> <@member>",
        aliases=['spg', 'spamghostping', 'sghostping'],
        description="Ghostpings"
    )
    async def spamgp(self, luna, delay: int = None, amount: int = None, user: discord.Member = None):

        if configs.risk_mode() == "on":
            try:
                if delay is None or amount is None or user is None:
                    await luna.send(f"Usage: {self.bot.prefix}spamghostping <delay> <amount> <@member>")
                else:
                    for each in range(0, amount):
                        await asyncio.sleep(delay)
                        await luna.send(user.mention, delete_after=0)
            except Exception as e:
                await luna.send(f"Error: {e}")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="spamrep",
        usage="<message_id> <amount>",
        aliases=['spamreport'],
        description="Reports"
    )
    async def spamrep(self, luna, message_id: str, amount: int):

        if configs.risk_mode() == "on":
            try:
                prints.event(f"Spam report started...")
                for each in range(0, amount):
                    await asyncio.sleep(2)
                    reason = "Illegal Content"
                    payload = {
                        'message_id': message_id,
                        'reason': reason
                    }
                    requests.post(
                        'https://discord.com/api/{api_version}/report',
                        json=payload,
                        headers={
                            'authorization': user_token,
                            'user-agent': 'Mozilla/5.0'
                        }
                    )
                prints.event(f"Spam report finished")
                await message_builder(
                    luna, title="Report",
                    description=f"Message {message_id} has been reported {amount} times"
                )
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="spamhentai",
        usage="<delay> <amount>",
        description="Hentai"
    )
    async def spamhentai(self, luna, delay: int, amount: int):

        if configs.risk_mode() == "on":
            try:
                for each in range(0, amount):
                    await asyncio.sleep(delay)
                    r = requests.get(
                        "http://api.nekos.fun:8080/api/hentai"
                    ).json()
                    await luna.send(r['image'])
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="spamwebhook",
        usage="<delay> <amount> <url> <message>",
        description="Webhooks"
    )
    async def spamwebhook(self, luna, delay: int, amount: int, url: str, message: str):

        if configs.risk_mode() == "on":
            if "https://discord.com/api/webhooks/" not in url:
                await error_builder(luna, description="```\nInvalid URL```")
                return
            try:
                for _ in range(amount):
                    await asyncio.sleep(delay)
                    await message_builder(
                        luna,
                        description=f"```\nSending webhooks...\n``````\nAmount » {amount}\nDelay » {delay}\nMessage » {message}\n``````\nURL » {url}```"
                    )
                    hook = dhooks.Webhook(
                        url=url, avatar_url=webhook.image_url()
                    )
                    color = 0x000000
                    if color is not None:
                        color = webhook.hex_color()
                    embed = dhooks.Embed(
                        title=webhook.title(
                        ), description=message, color=color
                    )
                    embed.set_thumbnail(url=webhook.image_url())
                    embed.set_footer(text=webhook.footer())
                    hook.send(embed=embed)
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
                return
            await message_builder(luna, description=f"```\nWebhooks sent```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="spamtts",
        usage="<delay> <amount> <message>",
        description="TTS"
    )
    async def spamtts(self, luna, delay: int, amount: int, *, message: str):

        if configs.risk_mode() == "on":
            try:
                for each in range(0, amount):
                    await asyncio.sleep(delay)
                    await luna.send(message, tts=True)
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")
