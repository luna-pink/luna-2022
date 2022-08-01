from discord.ext import commands
from discord.ext.commands import has_permissions

from .utilities import *


class RoleCog(commands.Cog, name="Role commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="roleinfo",
        usage="<@role>",
        description="Information"
    )
    async def roleinfo(self, luna, role: discord.Role):

        role_amount = 0
        role_members = ""
        for member in luna.guild.members:
            for roles in member.roles:
                if roles.id == role.id:
                    role_amount += 1
                    role_members += f"{member.name}#{member.discriminator}\n"
        if role_members == "":
            role_members = "No members have this role"
        await message_builder(
            luna, title="Role Information",
            description=f"```\n{'Name':17} » {role.name}\n"
                        f"{'ID':17} » {role.id}\n"
                        f"{'Color':17} » {role.color}\n"
                        f"{'Created at':17} » {role.created_at}\n"
                        f"{'Position':17} » {role.position}\n```"
                        f"```\n{'Members':17} » {role_amount}\n\n"
                        f"Member List:\n{role_members}\n```"
                        f"```\n{'Permissions':17} » {role.permissions}\n```"
        )

    @commands.command(
        name="giverole",
        usage="<@member> <role_id>",
        description="Give a role"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def giverole(self, luna, member: discord.Member, role_id: int):

        role = discord.utils.get(luna.guild.roles, id=role_id)
        if role is None:
            await message_builder(
                luna, title="Give role",
                description=f"```\nNo role with the id {role_id} was found```"
            )
            return
        await member.add_roles(role)
        await message_builder(
            luna, title="Give role",
            description=f"```\nGave {member.name}#{member.discriminator} role » {role.name}```"
        )

    @commands.command(
        name="giveallroles",
        usage="<@member>",
        description="Give all roles"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def giveallroles(self, luna, member: discord.Member):

        for role in luna.guild.roles:
            if role.name == "@everyone":
                continue
            await member.add_roles(role)
        await message_builder(
            luna, title="Give all roles",
            description=f"```\nGave all roles to » {member.name}#{member.discriminator}```"
        )

    @commands.command(
        name="allroles",
        usage="",
        description="Give all roles"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def allroles(self, luna):

        for member in luna.guild.members:
            for role in luna.guild.roles:
                if role.name == "@everyone":
                    continue
                await member.add_roles(role)
        await message_builder(luna, title="Give all roles", description=f"```\nGave all members all roles```")

    @commands.command(
        name="removeallroles",
        usage="<@member>",
        description="Remove all roles"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def removeallroles(self, luna, member: discord.Member):

        for role in luna.guild.roles:
            if role.name == "@everyone":
                continue
            await member.remove_roles(role)
        await message_builder(
            luna, title="Remove all roles",
            description=f"```\nRemoved all roles from » {member.name}#{member.discriminator}```"
        )

    @commands.command(
        name="removerole",
        usage="<@member> <role_id>",
        description="Remove a role"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def removerole(self, luna, member: discord.Member, role_id: int):

        role = discord.utils.get(luna.guild.roles, id=role_id)
        if role is None:
            await message_builder(
                luna, title="Remove role",
                description=f"```\nNo role with the id {role_id} was found```"
            )
            return
        await member.remove_roles(role)
        await message_builder(
            luna, title="Remove role",
            description=f"```\nRemoved role {role.name} from » {member.name}#{member.discriminator}```"
        )

    @commands.command(
        name="createrole",
        usage="<role_name>",
        description="Create a role"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def createrole(self, luna, *, role_name: str):

        role = await luna.guild.create_role(name=role_name)
        await message_builder(luna, title="Create role", description=f"```\nCreated role » {role.name}```")

    @commands.command(
        name="renamerole",
        usage="<role_id> <name>",
        description="Rename a role"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def renamerole(self, luna, role_id: int, *, name: str):

        role = discord.utils.get(luna.guild.roles, id=role_id)
        if role is None:
            await message_builder(
                luna, title="Rename role",
                description=f"```\nNo role with the id {role_id} was found```"
            )
            return
        await role.edit(name=name)
        await message_builder(luna, title="Rename role", description=f"```\nRenamed role {role.name} to » {name}```")

    @commands.command(
        name="renameroles",
        usage="<name>",
        description="Rename all roles"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def renameroles(self, luna, *, name: str):

        for role in luna.guild.roles:
            if role.name == "@everyone":
                continue
            await role.edit(name=name)
        await message_builder(luna, title="Rename all roles", description=f"```\nRenamed all roles to » {name}```")

    @commands.command(
        name="deleterole",
        usage="<role_id>",
        description="Delete a role"
    )
    @commands.guild_only()
    @has_permissions(manage_roles=True)
    async def deleterole(self, luna, role_id: int):

        role = discord.utils.get(luna.guild.roles, id=role_id)
        if role is None:
            await message_builder(
                luna, title="Delete role",
                description=f"```\nNo role with the id {role_id} was found```"
            )
            return
        await role.delete()
        await message_builder(luna, title="Delete role", description=f"```\nDeleted role » {role.name}```")