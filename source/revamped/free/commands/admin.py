from discord.ext import commands
from discord.ext.commands import has_permissions

from .utilities import *


class AdminCog(commands.Cog, name="Administrative commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="guildname",
        usage="<name>",
        description="Change guild name"
    )
    @commands.guild_only()
    @has_permissions(manage_guild=True)
    async def guildname(self, luna, *, name: str):

        await luna.guild.edit(name=name)
        await message_builder(luna, title="Guildname", description=f"```\nChanged the name of the guild to » {name}```")

    @commands.command(
        name="guildimage",
        usage="<image_url>",
        description="Change guild image"
    )
    @commands.guild_only()
    @has_permissions(manage_guild=True)
    async def guildimage(self, luna, *, image_url: str):

        await luna.guild.edit(icon=image_url)
        await message_builder(
            luna, title="Guildimage",
            description=f"```\nChanged the image of the guild to » {image_url}```"
        )

    @commands.command(
        name="guildbanner",
        usage="<image_url>",
        description="Change guild banner"
    )
    @commands.guild_only()
    @has_permissions(manage_guild=True)
    async def guildbanner(self, luna, *, image_url: str):

        await luna.guild.edit(banner=image_url)
        await message_builder(
            luna, title="Guildbanner",
            description=f"```\nChanged the banner of the guild to » {image_url}```"
        )

    @commands.command(
        name="getguildimage",
        usage="[guild_id]",
        description="Get the guild image"
    )
    @commands.guild_only()
    @has_permissions(manage_guild=True)
    async def getguildimage(self, luna, guild_id: int = None):

        if guild_id is None:
            guild_id = luna.guild.id
        guild = discord.utils.get(luna.guilds, id=guild_id)
        if guild is None:
            await message_builder(
                luna, title="Guildimage",
                description=f"```\nNo guild with the id » {guild_id} was found```"
            )
            return
        await message_builder(luna, title="Guildimage", description=f"```\n{guild.icon_url}```")

    @commands.command(
        name="getguildbanner",
        usage="[guild_id]",
        description="Get the guild banner"
    )
    @commands.guild_only()
    @has_permissions(manage_guild=True)
    async def getguildbanner(self, luna, guild_id: int = None):

        if guild_id is None:
            guild_id = luna.guild.id
        guild = discord.utils.get(luna.guilds, id=guild_id)
        if guild is None:
            await message_builder(
                luna, title="Guildbanner",
                description=f"```\nNo guild with the id » {guild_id} was found```"
            )
            return
        await message_builder(luna, title="Guildbanner", description=f"```\n{guild.banner_url}```")

    @commands.command(
        name="guildinfo",
        usage="[guild_id]",
        description="Guild information"
    )
    @commands.guild_only()
    @has_permissions(manage_guild=True)
    async def guildinfo(self, luna, guild_id: int = None):

        if guild_id is None:
            guild = luna.guild
        else:
            guild = discord.utils.get(self.bot.guilds, id=guild_id)
            if guild is None:
                await message_builder(
                    luna, title="Guildinfo",
                    description=f"```\nNo guild with the id {guild_id} was found```"
                )
                return
        await message_builder(
            luna, title="Guildinfo",
            description=f"```\nGeneral Information\n\n"
                        f"{'Guild':<17} » {guild.name}\n"
                        f"{'ID':17} » {guild.id}\n"
                        f"{'Owner':17} » {guild.owner}\n"
                        f"{'Created at':17} » {guild.created_at}\n"
                        f"{'Boost':17} » {guild.premium_subscription_count}\n"
                        f"{'Boost status':17} » {guild.premium_subscription_count is not None}\n"
                        f"{'Region':17} » {guild.region}\n"
                        f"{'Verification':17} » {guild.verification_level}\n```"
                        f"```\nMember Information\n\n"
                        f"{'Member count':17} » {guild.member_count}\n```"
                        f"```\nChannel Information\n\n"
                        f"{'Text channels':17} » {len(guild.text_channels)}\n"
                        f"{'Voice channels':17} » {len(guild.voice_channels)}\n```"
                        f"```\nRole Information\n\n"
                        f"{'Role count':17} » {len(guild.roles)}```"
        )
