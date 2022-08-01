from discord.ext import commands
from discord.ext.commands import has_permissions

from .utilities import *


class NickCog(commands.Cog, name="Nickname commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="nick",
        usage="<name>",
        description="Change nickname"
    )
    @commands.guild_only()
    @has_permissions(manage_nicknames=True)
    async def nick(self, luna, *, name: str):

        await luna.author.edit(nick=name)
        await message_builder(luna, title="Nickname", description=f"```\nChanged nickname to » {name}```")

    @commands.command(
        name="nickmember",
        usage="<@member> <name>",
        description="Change nickname"
    )
    @commands.guild_only()
    @has_permissions(manage_nicknames=True)
    async def nickmember(self, luna, member: discord.Member, *, name: str):

        await member.edit(nick=name)
        await message_builder(
            luna, title="Nickname",
            description=f"```\nChanged nickname of {member.name}#{member.discriminator} to » {name}```"
        )

    @commands.command(
        name="nickall",
        usage="<name>",
        description="Change nickname of everyone"
    )
    @commands.guild_only()
    @has_permissions(manage_nicknames=True)
    async def nickall(self, luna, *, name: str):

        for member in luna.guild.members:
            await member.edit(nick=name)
        await message_builder(luna, title="Nickall", description=f"```\nChanged nickname of everyone to » {name}```")

    @commands.command(
        name="clearnick",
        usage="[@member]",
        description="Clear nickname"
    )
    @commands.guild_only()
    @has_permissions(manage_nicknames=True)
    async def clearnick(self, luna, member: discord.Member = None):

        if member is None:
            member = luna.author
        await member.edit(nick=None)
        await message_builder(
            luna, title="Clearnick",
            description=f"```\nCleared nickname of » {member.name}#{member.discriminator}```"
        )

    @commands.command(
        name="clearallnick",
        usage="",
        description="Clear all nicknames"
    )
    @commands.guild_only()
    @has_permissions(manage_nicknames=True)
    async def clearallnick(self, luna):

        for member in luna.guild.members:
            await member.edit(nick=None)
        await message_builder(luna, title="Clearnick", description=f"```\nCleared nickname of everyone```")