from discord.ext import commands
from .utilities import *


class SniperCog(commands.Cog, name="Sniper settings"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="nitrosniper",
        usage="<on/off>",
        description="Nitro sniper"
    )
    async def nitrosniper(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Nitro sniper » {color.print_gradient(f'{mode}')}")
            config.nitro.sniper(mode)
            await message_builder(luna, description=f"```\nNitro sniper » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="privsniper",
        usage="<on/off>",
        description="Privnote sniper"
    )
    async def privsniper(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Privnote sniper » {color.print_gradient(f'{mode}')}")
            config.privnote.sniper(mode)
            await message_builder(luna, description=f"```\nPrivnote sniper » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="snipercharge",
        usage="<on/off>",
        description="Sniper visual charge"
    )
    async def snipercharge(self, luna, mode: str):

        global charge_sniper
        if mode == "on" or mode == "off":
            prints.message(f"Nitro sniper charge » {color.print_gradient(f'{mode}')}")
            config._global("data/snipers/nitro.json", "charge", mode)
            if mode == "on":
                charge_sniper = True
            elif mode == "off":
                charge_sniper = False
            await message_builder(luna, description=f"```\nNitro sniper charge » {mode}```")
        else:
            await mode_error(luna, "on or off")