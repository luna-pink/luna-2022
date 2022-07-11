from discord.ext import commands
from discord.ext.commands import has_permissions

from .utilities import *


class ChannelCog(commands.Cog, name="Channel commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="channelinfo",
        usage="<#channel>",
        description="Information"
    )
    async def channelinfo(self, luna, channel: discord.TextChannel):

        await message_builder(
            luna, title="Channel Information",
            description=f"```\n{'Name':17} » {channel.name}\n"
                        f"{'ID':17} » {channel.id}\n"
                        f"{'Created at':17} » {channel.created_at}\n"
                        f"{'Category':17} » {channel.category}\n"
                        f"{'Position':17} » {channel.position}\n"
                        f"{'Topic':17} » {channel.topic}\n"
                        f"{'Is NSFW?':17} » {channel.is_nsfw()}\n```"
        )

    @commands.command(
        name="textchannel",
        usage="<name>",
        description="Create a text channel"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def textchannel(self, luna, name: str):

        channel = await luna.guild.create_text_channel(name)
        await message_builder(luna, description=f"```\nCreated text channel » {channel.mention}```")

    @commands.command(
        name="voicechannel",
        usage="<name>",
        description="Create a voice channel"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def voicechannel(self, luna, name: str):

        channel = await luna.guild.create_voice_channel(name)
        await message_builder(luna, description=f"```\nCreated voice channel » {channel.mention}```")

    @commands.command(
        name="stagechannel",
        usage="<name>",
        description="Create a stage channel"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def stagechannel(self, luna, name: str):

        payload = {
            'name': f"{name}",
            'type': 13
        }
        requests.post(
            f'https://discord.com/api/{api_version}/guilds/{luna.guild.id}/channels',
            json=payload,
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(luna, description=f"```\nCreated stage channel » {name}```")

    @commands.command(
        name="newschannel",
        usage="<name>",
        description="Create a news channel"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def newschannel(self, luna, name: str):

        payload = {
            'name': f"{name}",
            'type': 5
        }
        requests.post(
            f'https://discord.com/api/{api_version}/guilds/{luna.guild.id}/channels',
            json=payload,
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(luna, description=f"```\nCreated news channel » {name}```")

    @commands.command(
        name="renamechannel",
        usage="<#channel> <name>",
        description="Rename channel"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def renamechannel(self, luna, channel: discord.TextChannel, name: str):

        await channel.edit(name=name)
        await message_builder(luna, description=f"```\nRenamed {luna.channel.name} to » {channel.mention}```")

    @commands.command(
        name="deletechannel",
        usage="<#channel>",
        description="Delete a channel"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def deletechannel(self, luna, channel: discord.TextChannel):

        await channel.delete()
        await message_builder(luna, description=f"```\nDeleted channel » {channel.mention}```")

    @commands.command(
        name="slowmode",
        usage="<seconds>",
        description="Set slowmode"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def slowmode(self, luna, seconds: int):

        if seconds < 0:
            await message_builder(luna, title="Slowmode", description=f"```\nThe slowmode can't be negative```")
            return
        if seconds == 0:
            await luna.channel.edit(slowmode_delay=0)
            await message_builder(luna, title="Slowmode", description=f"```\nDisabled slowmode```")
            return
        await luna.channel.edit(slowmode_delay=seconds)
        await message_builder(luna, title="Slowmode", description=f"```\nSet slowmode to » {seconds} seconds```")

    @commands.command(
        name="removeslowmode",
        usage="",
        description="Remove slowmode"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def removeslowmode(self, luna):

        await luna.channel.edit(slowmode_delay=0)
        await message_builder(luna, title="Slowmode", description=f"```\nRemoved slowmode```")

    @commands.command(
        name="lock",
        usage="<#channel>",
        description="Lock a channel"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def lock(self, luna, channel: discord.TextChannel):

        await channel.set_permissions(luna.guild.default_role, send_messages=False)
        await channel.edit(name="🔒-locked")
        await message_builder(luna, description=f"```\nLocked channel » {channel.mention}```")

    @commands.command(
        name="unlock",
        usage="<#channel>",
        description="Unlock a channel"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def unlock(self, luna, channel: discord.TextChannel):

        await channel.set_permissions(luna.guild.default_role, send_messages=True)
        await channel.edit(name="🔒-unlocked")
        await message_builder(luna, description=f"```\nUnlocked channel » {channel.mention}```")

    @commands.command(
        name="category",
        usage="<name>",
        description="Create a category"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def category(self, luna, name: str):

        category = await luna.guild.create_category_channel(name)
        await message_builder(luna, description=f"```\nCreated category » {category.mention}```")

    @commands.command(
        name="deletecategory",
        usage="<category_id>",
        description="Delete a category"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def deletecategory(self, luna, category: discord.CategoryChannel):

        await category.delete()
        await message_builder(luna, description=f"```\nDeleted category » {category.mention}```")

    @commands.command(
        name="purge",
        usage="<amount>",
        description="Purge the channel"
    )
    async def purge(self, luna, amount: int):

        async for message in luna.message.channel.history(limit=amount):
            try:
                await message.delete()
            except BaseException:
                pass

    @commands.command(
        name="nuke",
        usage="[#channel]",
        description="Nuke the channel"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def nuke(self, luna, channel: discord.TextChannel = None):

        if channel is None:
            channel = luna.channel
        new_channel = await channel.clone()
        await new_channel.edit(position=channel.position)
        await channel.delete()
        await message_builder(new_channel, description=f"```\nThis channel has been nuked```")