from discord.ext import commands
from .utilities import *


class GiveawayCog(commands.Cog, name="Giveaway settings"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="giveawayjoiner",
        usage="<on/off>",
        description="Giveaway sniper"
    )
    async def giveawayjoiner(self, luna, mode: str):

        if mode in {"on", "off"}:
            prints.message(f"Giveaway sniper » {color.print_gradient(f'{mode}')}")
            config.giveaway.joiner(mode)
            await message_builder(luna, description=f"```\nGiveaway sniper » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="delay",
        usage="<minutes>",
        description="Delay in minutes"
    )
    async def delay(self, luna, minute: int):

        await message_builder(luna, description=f"```\nGiveaway joiner delay » {minute} minute/s```")

        prints.message(f"Auto delete timer » {color.print_gradient(str(minute))}")
        config.giveaway.delay_in_minutes(f"{minute}")

    @commands.command(
        name="giveawayguild",
        usage="<on/off>",
        description="Giveaway server joiner"
    )
    async def giveawayguild(self, luna, mode: str):

        if mode in {"on", "off"}:
            prints.message(f"Server joiner » {color.print_gradient(f'{mode}')}")
            config.giveaway.guild_joiner(mode)
            await message_builder(luna, description=f"```\nServer joiner » {mode}```")
        else:
            await mode_error(luna, "on or off")