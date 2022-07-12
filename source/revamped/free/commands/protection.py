from discord.ext import commands
from .utilities import *


class ProtectionCog(commands.Cog, name="Protection commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="pfooter",
        usage="<on/off>",
        description="Protections footer info"
    )
    async def pfooter(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(
                f"Protections footer info » {color.print_gradient(f'{mode}')}"
            )
            if mode == "on":
                config._global("data/protections/config.json", "footer", True)
            else:
                config._global("data/protections/config.json", "footer", False)
            await message_builder(luna, description=f"```\nProtections footer info » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="anti_raid",
        usage="<on/off>",
        description="Protects against raids"
    )
    async def antiraid(self, luna, mode: str):

        global anti_raid
        global active_protections
        global active_list
        if mode in {"on", "off"}:
            prints.message(f"Antiraid » {color.print_gradient(f'{mode}')}")
            if mode == "on":
                anti_raid = True
                active_protections += 1
                active_list.append("anti_raid")
            else:
                anti_raid = False
                active_protections -= 1
                active_list.remove("anti_raid")
            await message_builder(luna, description=f"```\nAntiraid » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="anti_invite",
        usage="<on/off>",
        description="Protects against invites"
    )
    async def antiinvite(self, luna, mode: str):

        global anti_invite
        global active_protections
        global active_list
        if mode in {"on", "off"}:
            prints.message(f"Antiinvite » {color.print_gradient(f'{mode}')}")
            if mode == "on":
                anti_invite = True
                active_protections += 1
                active_list.append("anti_invite")
            else:
                anti_invite = False
                active_protections -= 1
                active_list.remove("anti_invite")
            await message_builder(luna, description=f"```\nAntiinvite » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="anti_upper",
        usage="<on/off>",
        description="Protects against uppercase"
    )
    async def antiupper(self, luna, mode: str):

        global anti_upper
        global active_protections
        global active_list
        if mode == "on" or mode == "off":
            prints.message(f"Antiupper » {color.print_gradient(f'{mode}')}")
            if mode == "on":
                anti_upper = True
                active_protections += 1
                active_list.append("anti_upper")
            else:
                anti_upper = False
                active_protections -= 1
                active_list.remove("anti_upper")
            await message_builder(luna, description=f"```\nAntiupper » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="anti_phishing",
        usage="<on/off>",
        description="Protects against phishing"
    )
    async def antiphishing(self, luna, mode: str):

        global anti_phishing
        global active_protections
        global active_list
        if mode == "on" or mode == "off":
            prints.message(f"Anti phishing links » {color.print_gradient(f'{mode}')}")
            if mode == "on":
                anti_phishing = True
                active_protections += 1
                active_list.append("Anti Phishing Links")
            else:
                anti_phishing = False
                active_protections -= 1
                active_list.remove("Anti Phishing Links")
            await message_builder(luna, description=f"```\nAnti phishing links » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="anti_deleting",
        usage="<on/off>",
        description="Log deleted messages"
    )
    async def antideleting(self, luna, mode: str):

        global anti_deleting
        global active_protections
        global active_list
        if mode == "on" or mode == "off":
            prints.message(f"Anti deleting » {color.print_gradient(f'{mode}')}")
            if mode == "on":
                anti_deleting = True
                active_protections += 1
                active_list.append("Anti Deleting")
            else:
                anti_deleting = False
                active_protections -= 1
                active_list.remove("Anti Deleting")
            await message_builder(luna, description=f"```\nAnti deleting » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="sbcheck",
        usage="",
        description="Check for bad selfbots"
    )
    async def sbcheck(self, luna):

        await message_builder(luna, title="GIVEAWAY")
        await message_builder(luna, description="```\nThose that reacted, could be running selfbots```")