import asyncio

from discord.ext import commands
from .utilities import *


class MassCog(commands.Cog, name="Mass commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="massping",
        usage="<delay> <amount>",
        description="Mass ping members"
    )
    async def massping(self, luna, delay: int, amount: int):

        if configs.risk_mode() == "on":
            try:
                for _ in range(amount):
                    members = [m.mention for m in luna.guild.members]
                    mentionamount = min(len(members), 30)
                    sendamount = len(members) - mentionamount + 1
                    for _ in range(sendamount):
                        if mentionamount == 0:
                            break
                        pingtext = "".join(members.pop() for _ in range(mentionamount))
                        await luna.send(pingtext)
                        await asyncio.sleep(delay)
                        mentionamount = min(len(members), 30)
            except Exception as e:
                prints.error(f"{e}")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="massgp",
        usage="<delay> <amount>",
        description="Mass ghostping"
    )
    async def massgp(self, luna, delay: int, amount: int):

        if configs.risk_mode() == "on":
            try:
                for _ in range(amount):
                    members = [m.mention for m in luna.guild.members]
                    mentionamount = min(len(members), 30)
                    sendamount = len(members) - mentionamount + 1
                    for _ in range(sendamount):
                        if mentionamount == 0:
                            break
                        pingtext = "".join(members.pop() for _ in range(mentionamount))
                        msg = await luna.send(pingtext)
                        await msg.delete()
                        await asyncio.sleep(delay)
                        mentionamount = min(len(members), 40)
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="massnick",
        usage="<name>",
        description="Mass change nicknames"
    )
    async def massnick(self, luna, name: str):
        import discum
        if configs.risk_mode() == "on":
            bot = discum.Client(
                token=user_token, log=False,
                user_agent="Mozilla/5.0"
            )

            def done_fetching(_, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    members = bot.gateway.session.guild(guild_id).members
                    bot.gateway.removeCommand(
                        {'function': done_fetching, 'params': {'guild_id': guild_id}}
                    )
                    bot.gateway.close()
                    return members

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(
                    guild_id, channel_id, keep="all", wait=1
                )
                bot.gateway.command(
                    {'function': done_fetching, 'params': {'guild_id': guild_id}}
                )
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            amount = 0
            members = get_members(str(luna.guild.id), str(luna.channel.id))
            for member in members:
                try:
                    member = await luna.guild.fetch_member(member.id)
                    await member.edit(nick=name)
                    amount += 1
                    await asyncio.sleep(1)
                except BaseException:
                    pass
            await message_builder(luna, title="Success", description=f"```\nChanged nicknames of {amount} members```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="masschannels",
        usage="<amount>",
        description="Mass create channels"
    )
    async def masschannels(self, luna, amount: int):
        if configs.risk_mode() == "on":
            try:
                for _ in range(amount):
                    await luna.guild.create_text_channel("Created by Luna")
                    await asyncio.sleep(1)
                await message_builder(luna, title="Success", description=f"```\nCreated {amount} channels```")
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="massroles",
        usage="<amount>",
        description="Mass create roles"
    )
    async def massroles(self, luna, amount: int):
        if configs.risk_mode() == "on":
            try:
                for _ in range(amount):
                    await luna.guild.create_role(name="Created by Luna")
                    await asyncio.sleep(1)
                await message_builder(luna, title="Success", description=f"```\nCreated {amount} roles```")
            except Exception as e:
                await error_builder(luna, description=f"```{e}```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="prune",
        usage="<@role> [reason]",
        description="Prune a role"
    )
    async def prune(self, luna, role, *, reason: str = None):

        if configs.risk_mode() == "on":
            with contextlib.suppress(Exception):
                reason = "No reason provided" if reason is None else reason
                role = luna.guild.get_role(role)
                if role is None:
                    await error_builder(luna, description="```\nRole not found```")
                    return
                members = luna.guild.members
                for member in members:
                    if role in member.roles:
                        with contextlib.suppress(Exception):
                            await member.send(f"You have been pruned from {luna.guild.name} for {reason}")
                            await member.kick(reason=reason)
                await message_builder(luna, description=f"```\nPruned {len(members)} members```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")

    @commands.command(
        name="pruneban",
        usage="<@role> [reason]",
        description="Prune & ban a role"
    )
    async def pruneban(self, luna, role, *, reason: str = None):

        if configs.risk_mode() == "on":
            with contextlib.suppress(Exception):
                reason = "No reason provided" if reason is None else reason
                role = luna.guild.get_role(role)
                if role is None:
                    await error_builder(luna, description="```\nRole not found```")
                    return
                members = luna.guild.members
                for member in members:
                    if role in member.roles:
                        with contextlib.suppress(Exception):
                            await member.send(f"You have been pruned and banned from {luna.guild.name} for {reason}")
                            await member.ban(reason=reason)
                await message_builder(luna, description=f"```\nPruned and banned {len(members)} members```")
        else:
            await error_builder(luna, description="```\nRiskmode is disabled```")