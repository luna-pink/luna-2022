from discord.ext import commands
from discord.ext.commands import has_permissions

from .utilities import *


class InviteCog(commands.Cog, name="Invite commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="inviteinfo",
        usage="<invite>",
        description="Invite information"
    )
    @commands.guild_only()
    async def inviteinfo(self, luna, invite: str):

        invite = await self.bot.get_invite(invite)
        if invite is None:
            await message_builder(
                luna, title="Invite info",
                description=f"```\nNo invite with the id {invite} was found```"
            )
            return
        await message_builder(
            luna, title="Invite info",
            description=f"```\nInvite » {invite.code}\n"
                        f"Created at » {invite.created_at}\n"
                        f"Channel » {invite.channel.mention}\n"
                        f"Guild » {invite.guild.name}\n"
                        f"Created by » {invite.inviter.name}#{invite.inviter.discriminator}\n"
                        f"Max uses » {invite.max_uses}\n"
                        f"Uses » {invite.uses}```"
        )

    @commands.command(
        name="invite",
        usage="[channel_id] [age] [uses]",
        description="Invite"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def invite(self, luna, channel_id: int = None, max_age: int = 0, max_uses: int = 0):

        if channel_id is None:
            channel = luna.channel
        else:
            channel = discord.utils.get(luna.guild.channels, id=channel_id)
        if channel is None:
            await message_builder(
                luna, title="Invite",
                description=f"```\nNo channel with the id » {channel_id} was found```"
            )
            return
        invite = await channel.create_invite(max_age=max_age, max_uses=max_uses)
        await message_builder(luna, title="Invite", description=f"```\nCreated invite » {invite.url}```")

    @commands.command(
        name="delinvite",
        usage="<invite_id>",
        description="Delete invite"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def delinvite(self, luna, invite_id: int):

        invite = discord.utils.get(luna.guild.invites, id=invite_id)
        if invite is None:
            await message_builder(
                luna, title="Delete invite",
                description=f"```\nNo invite with the id » {invite_id} was found```"
            )
            return
        await invite.delete()
        await message_builder(luna, title="Delete invite", description=f"```\nDeleted invite » {invite.url}```")

    @commands.command(
        name="delallinvite",
        usage="",
        description="Delete all invites"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def delallinvite(self, luna):

        for invite in luna.guild.invites:
            await invite.delete()
        await message_builder(luna, title="Delete invite", description=f"```\nDeleted all invites```")

    @commands.command(
        name="invitelist",
        usage="",
        description="List all invites"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def invitelist(self, luna):

        invites = luna.guild.invites
        if len(invites) == 0:
            await message_builder(luna, title="Invite list", description=f"```\nNo invites were found```")
            return
        invite_list = ""
        for invite in invites:
            invite_list += f"{invite.url}\n"
        await message_builder(luna, title="Invite list", description=f"```\n{invite_list}```")

    @commands.command(
        name="invitechannel",
        usage="<channel_id>",
        description="Channel invites"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def invitelistchannel(self, luna, channel_id: int):

        channel = discord.utils.get(luna.guild.channels, id=channel_id)
        if channel is None:
            await message_builder(
                luna, title="Invite list",
                description=f"```\nNo channel with the id » {channel_id} was found```"
            )
            return
        invites = channel.invites
        if len(invites) == 0:
            await message_builder(luna, title="Invite list", description=f"```\nNo invites were found```")
            return
        invite_list = ""
        for invite in invites:
            invite_list += f"{invite.url}\n"
        await message_builder(luna, title="Invite list", description=f"```\n{invite_list}```")

    @commands.command(
        name="inviteguild",
        usage="",
        description="Invites of a guild"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def invitelistguild(self, luna):

        invites = luna.guild.invites
        if len(invites) == 0:
            await message_builder(luna, title="Invite list", description=f"```\nNo invites were found```")
            return
        invite_list = ""
        for invite in invites:
            invite_list += f"{invite.url}\n"
        await message_builder(luna, title="Invite list", description=f"```\n{invite_list}```")

    @commands.command(
        name="inviteuser",
        usage="<user_id>",
        description="Invites of a user"
    )
    @commands.guild_only()
    @has_permissions(manage_channels=True)
    async def invitelistuser(self, luna, user_id: int):

        user = discord.utils.get(luna.guild.members, id=user_id)
        if user is None:
            await message_builder(
                luna, title="Invite list",
                description=f"```\nNo user with the id » {user_id} was found```"
            )
            return
        invites = user.invites
        if len(invites) == 0:
            await message_builder(luna, title="Invite list", description=f"```\nNo invites were found```")
            return
        invite_list = ""
        for invite in invites:
            invite_list += f"{invite.url}\n"
        await message_builder(luna, title="Invite list", description=f"```\n{invite_list}```")