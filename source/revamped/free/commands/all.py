from discord.ext import commands
from .utilities import *


class AllCog(commands.Cog, name="All commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="banall",
        usage="[reason]",
        description="Ban all"
    )
    async def banall(self, luna, *, reason: str = None):

        if configs.risk_mode() == "on":
            try:
                for each in luna.guild.members:
                    if each is not luna.author or each is not luna.guild.owner:
                        await each.ban(reason=reason)
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="banbots",
        usage="[reason]",
        description="Ban all bots"
    )
    async def banbots(self, luna, *, reason: str = None):

        if configs.risk_mode() == "on":
            try:
                for each in luna.guild.members:
                    if each.bot:
                        await each.ban(reason=reason)
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="kickall",
        usage="[reason]",
        description="Kick all"
    )
    async def kickall(self, luna, *, reason: str = None):

        if configs.risk_mode() == "on":
            try:
                for each in luna.guild.members:
                    if each is not luna.author or each is not luna.guild.owner:
                        await each.kick(reason=reason)
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="kickbots",
        usage="[reason]",
        description="Kick all bots"
    )
    async def kickbots(self, luna, *, reason: str = None):

        if configs.risk_mode() == "on":
            try:
                for each in luna.guild.members:
                    if each.bot:
                        await each.kick(reason=reason)
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="dmall",
        usage="<message>",
        description="DM every member"
    )
    async def dmall(self, luna, *, message: str):

        if configs.risk_mode() == "on":
            sent = 0
            try:
                members = luna.channel.members
                for member in members:
                    if member is not luna.author:
                        with contextlib.suppress(Exception):
                            await member.send(message)
                            prints.message(f"Sent {message} to {member}")
                            sent += 1
            except Exception:
                prints.error(f"Failed to send {message} to {member}")
            await message_builder(luna, description=f"```\nSent {message} to {sent} users```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="dmallfriends",
        usage="<message>",
        description="DM all friends"
    )
    async def dmallfriends(self, luna, *, message: str):

        if configs.risk_mode() == "on":
            sent = 0
            with contextlib.suppress(Exception):
                for user in self.user.friends:
                    try:
                        await user.send(message)
                        prints.message(f"Sent {message} to {user}")
                        sent += 1
                    except Exception:
                        prints.error(f"Failed to send {message} to {user}")
            await message_builder(luna, description=f"```\nSent {message} to {sent} friends```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="sendall",
        usage="<message>",
        description="Message in all channels"
    )
    async def sendall(self, luna, *, message):

        if configs.risk_mode() == "on":
            with contextlib.suppress(BaseException):
                channels = luna.guild.text_channels
                for _ in channels:
                    await message.channel.send(message)
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="blockall",
        usage="",
        description="Block everyone"
    )
    async def blockall(self, luna):

        if configs.risk_mode() == "on":
            with contextlib.suppress(Exception):
                members = luna.guild.members
                for member in members:
                    if member is not luna.author:
                        with contextlib.suppress(Exception):
                            await member.ban()
                            prints.message(f"Banned {member}")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")