import asyncio

from discord.ext import commands
from .utilities import *


class GuildCog(commands.Cog, name="Guild commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="renamechannels",
        usage="<name>",
        description="Rename all channels"
    )
    async def renamechannels(self, luna, name: str):
        if configs.risk_mode() == "on":
            try:
                for channel in luna.guild.channels:
                    await channel.edit(name=name)
                    await asyncio.sleep(1)
                await message_builder(luna, title="Success", description=f"```\nRenamed all channels to {name}```")
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="delchannels",
        usage="",
        description="Delete all channels"
    )
    async def delchannels(self, luna):
        if configs.risk_mode() == "on":
            try:
                for channel in luna.guild.channels:
                    if channel.name != "general":
                        await channel.delete()
                await message_builder(luna, title="Success", description="```\nDeleted all channels```")
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="delroles",
        usage="",
        description="Delete all roles"
    )
    async def delroles(self, luna):
        if configs.risk_mode() == "on":
            try:
                for role in luna.guild.roles:
                    if role.name != "@everyone":
                        await role.delete()
                await message_builder(luna, title="Success", description="```\nDeleted all roles```")
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")

    @commands.command(
        name="delemojis",
        usage="",
        description="Delete all emojis"
    )
    async def delemojis(self, luna):
        if configs.risk_mode() == "on":
            try:
                for emoji in luna.guild.emojis:
                    await emoji.delete()
                await message_builder(luna, title="Success", description="```\nDeleted all emojis```")
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
