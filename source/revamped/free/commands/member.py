from discord.ext import commands
from discord.ext.commands import has_permissions

from .utilities import *


class MemberCog(commands.Cog, name="Member commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="userinfo",
        usage="[user_id]",
        description="User information"
    )
    async def userinfo(self, luna, user: discord.Member = None):

        if user is None:
            user = luna.author
        r = requests.get(
            f'https://discord.com/api/{api_version}/users/{user.id}',
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        ).json()
        req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
        if banner_id := req["banner"]:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
        else:
            banner_url = None
        await message_builder(
            luna, title="User information",
            description=f"```\nGeneral Information\n\n"
                        f"{'User':12} » {user.name}#{user.discriminator}\n"
                        f"{'ID':12} » {user.id}\n"
                        f"{'Status':12} » {user.status}\n"
                        f"{'Bot':12} » {user.bot}\n"
                        f"{'Public Flags':12} » {r['public_flags']}\n"
                        f"{'Banner Color':12} » {r['banner_color']}\n"
                        f"{'Accent Color':12} » {r['accent_color']}\n```"
                        f"```\nCreated at:\n{user.created_at}\n```"
                        f"```\nImage Information\n\n"
                        f"Avatar URL:\n{user.avatar_url}\n\n"
                        f"Banner URL:\n{banner_url}\n```"
        )

    @commands.command(
        name="whois",
        usage="<@member>",
        description="Guild member information"
    )
    @commands.guild_only()
    async def whois(self, luna, user: discord.Member = None):

        if user is None:
            user = luna.author
        if user.id == 406907871998246924:
            special = "\n\nSpecial » Founder & Head Dev @ Team Luna"
        elif user.id in [707355480422350848, 663516459837685770]:
            special = "\n\nSpecial » Developer @ Team Luna"
        elif user.id in [288433475831332894, 465275771523563531]:
            special = "\n\nSpecial » Member @ Team Luna"
        elif user.id in [203906692834918401, 699099683603349654, 319759781315215360]:
            special = "\n\nSpecial » Luna Beta"
        elif user.id == 254994687444779008:
            special = "\n\nSpecial » First Luna Customer"
        else:
            special = ""
        date_format = "%a, %d %b %Y %I:%M %p"
        members = sorted(luna.guild.members, key=lambda m: m.joined_at)
        role_string = ', '.join([r.name for r in user.roles][1:])
        perm_string = ', '.join(
            [str(p[0]).replace("_", " ").title()
             for p in user.guild_permissions if p[1]]
        )
        await message_builder(
            luna,
            description=f"User » {user.mention}\n"
                        f"```User information\n\n"
                        f"Joined » {user.joined_at.strftime(date_format)}\n"
                        f"Join position » {members.index(user) + 1}\n"
                        f"Registered » {user.created_at.strftime(date_format)}\n```"
                        f"```\nUser server information\n\n"
                        f"Roles Amount » {len(user.roles) - 1}\n"
                        f"Roles\n\n"
                        f"{role_string}\n\n"
                        f"Permissions\n\n"
                        f"{perm_string}{special}```"
        )

    @commands.command(
        name="report",
        usage="<message_id> <reason>",
        description="Report a user"
    )
    async def report(self, luna, message_id: str, *, reason: str):

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
        await message_builder(luna, title="Report", description=f"```\nMessage {message_id} has been reported\n\nReason » {reason}```")

    @commands.command(
        name="mute",
        usage="<@member> [reason]",
        description="Mute a user"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def mute(self, luna, user: discord.Member, *, reason: str = None):

        role = discord.utils.get(luna.guild.roles, name="Muted")
        if not role:
            role = await luna.guild.create_role(name="Muted")
            for channel in luna.guild.channels:
                await channel.set_permissions(role, send_messages=False)
        await user.add_roles(role)
        await message_builder(luna, title="Mute", description=f"```\n{user.name}#{user.discriminator} has been muted\n``````\nReason\n\n{reason}```")

    @commands.command(
        name="unmute",
        usage="<@member> [reason]",
        description="Unmute a user"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def unmute(self, luna, user: discord.Member, *, reason: str = None):

        role = discord.utils.get(luna.guild.roles, name="Muted")
        if not role:
            await message_builder(luna, title="Unmute", description="No mute role found")
            return
        await user.remove_roles(role)
        await message_builder(luna, title="Unmute", description=f"```\n{user.name}#{user.discriminator} has been unmuted\n``````\nReason\n\n{reason}```")

    @commands.command(
        name="timeout",
        usage="<user> <time>",
        description="Time out a user"
    )
    @commands.guild_only()
    @has_permissions(ban_members=True)
    async def timeout(self, luna, user: discord.Member, time: int):

        payload = {
            'user_id': user.id,
            'duration': time
        }
        requests.post(
            f'https://discord.com/api/{api_version}/guilds/{luna.guild.id}/bans',
            json=payload,
            headers={
                'authorization': user_token,
                'user-agent': 'Mozilla/5.0'
            }
        )
        await message_builder(
            luna,
            description=f"```\nTime out » {user.name}#{user.discriminator} for {time} seconds```"
        )

    @commands.command(
        name="kick",
        usage="<@member> [reason]",
        description="Kick a user"
    )
    @commands.guild_only()
    @has_permissions(kick_members=True)
    async def kick(self, luna, user: discord.Member, *, reason: str = None):

        await user.kick(reason=reason)
        await message_builder(
            luna, title="Kick",
            description=f"```\n{user.name}#{user.discriminator} has been kicked\n``````\nReason\n\n{reason}```"
        )

    @commands.command(
        name="softban",
        usage="<@member> [reason]",
        description="Softban a user"
    )
    @commands.guild_only()
    @has_permissions(ban_members=True)
    async def softban(self, luna, user: discord.Member, *, reason: str = None):

        await user.ban(reason=reason)
        await user.unban()
        await message_builder(
            luna, title="Softban",
            description=f"```\n{user.name}#{user.discriminator} has been softbanned\n``````\nReason\n\n{reason}```"
        )

    @commands.command(
        name="ban",
        usage="<@member> [reason]",
        description="Ban a user"
    )
    @commands.guild_only()
    @has_permissions(ban_members=True)
    async def ban(self, luna, user: discord.Member, *, reason: str = None):

        await user.ban(reason=reason)
        await message_builder(
            luna, title="Ban",
            description=f"```\n{user.name}#{user.discriminator} has been banned\n``````\nReason\n\n{reason}```"
        )

    @commands.command(
        name="unban",
        usage="<user_id>",
        description="Unban a user"
    )
    @commands.guild_only()
    @has_permissions(ban_members=True)
    async def unban(self, luna, user_id: int):

        banned_users = await luna.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            if user.id == user_id:
                await luna.guild.unban(user)
                await message_builder(
                    luna, title="Unban",
                    description=f"```\n{user.name}#{user.discriminator} has been unbanned```"
                )
                return
        await message_builder(
            luna, title="Unban",
            description=f"```\nNo banned user with the id {user_id} was found```"
        )

    @commands.command(
        name="banned",
        usage="[guild_id]",
        description="List all bans"
    )
    @commands.guild_only()
    @has_permissions(ban_members=True)
    async def banned(self, luna, guild_id: int = None):

        if guild_id is not None:
            guild = discord.utils.get(self.bot.guilds, id=guild_id)
        else:
            guild = luna.guild
        bans = await guild.bans()
        if len(bans) == 0:
            await message_builder(
                luna, title=f"Bans in {guild.name}",
                description=f"```\nNo users are banned in {guild.name}```"
            )
            return
        bans = [
            f"{b.user.name}#{b.user.discriminator} | {b.user.id}" for b in bans]
        bans = "\n".join(bans)
        await message_builder(luna, title=f"Bans in {guild.name}", description=f"```{bans}```")

    @commands.command(
        name="savebans",
        usage="[guild_id]",
        description="Save bans"
    )
    @commands.guild_only()
    @has_permissions(ban_members=True)
    async def savebans(self, luna, guild_id: int = None):

        if guild_id is not None:
            guild = discord.utils.get(self.bot.guilds, id=guild_id)
        else:
            guild = luna.guild
        bans = await guild.bans()
        if len(bans) == 0:
            await message_builder(
                luna, title=f"Bans in {guild.name}",
                description=f"```\nNo users are banned in {guild.name}```"
            )
            return
        bans = [
            f"{b.user.name}#{b.user.discriminator} | {b.user.id}" for b in bans]
        bans = "\n".join(bans)
        files.create_folder(f"data/backup/guilds/{guild.name}", documents=False)
        files.write_file(
            f"data/backup/guilds/{guild.name}/bans.txt", bans, documents=False
        )
        await message_builder(luna, title="Saved Bans", description=f"```\nSaved all bans in data/backup/guilds/{guild.name}/bans.txt\n``````{bans}```")

    @commands.command(
        name="loadbans",
        usage="[guild_id]",
        description="Load bans"
    )
    @commands.guild_only()
    @has_permissions(ban_members=True)
    async def loadbans(self, luna, guild_id: int = None):

        if guild_id is not None:
            guild = discord.utils.get(self.bot.guilds, id=guild_id)
        else:
            guild = luna.guild
        if not files.file_exist(
                f"data/backup/guilds/{guild.name}",
                documents=False
        ):
            await message_builder(luna, title="Load bans", description=f"```\nNo bans were found in data/backup/{guild.name}/bans.txt```")

            return
        bans = files.read_file(
            f"data/backup/guilds/{guild.name}/bans.txt", documents=False
        )
        bans = bans.split("\n")
        for ban in bans:
            if ban == "":
                continue
            user_id = int(ban.split(" | ")[1])
            user = discord.utils.get(guild.members, id=user_id)
            await guild.ban(user)
        await message_builder(luna, title="Load bans", description=f"```\nLoaded all bans from data/backup/guilds/{guild.name}/bans.txt```")
