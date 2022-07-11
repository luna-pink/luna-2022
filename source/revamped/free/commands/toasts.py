from discord.ext import commands
from .utilities import *


class ToastsCog(commands.Cog, name="Toast commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="toasts",
        usage="<on/off>",
        description="Turn toasts on or off"
    )
    async def toasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Toasts » {color.print_gradient(f'{mode}')}")
            config.toast.toasts(mode)
            await message_builder(luna, description=f"```\nToasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="logintoasts",
        usage="<on/off>",
        description="Login toasts"
    )
    async def logintoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Login toasts » {color.print_gradient(f'{mode}')}")
            config.toast.login(mode)
            await message_builder(luna, description=f"```\nLogin toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="nitrotoasts",
        usage="<on/off>",
        description="Nitro toasts"
    )
    async def nitrotoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Nitro sniper toasts » {color.print_gradient(f'{mode}')}")
            config.toast.nitro(mode)
            await message_builder(luna, description=f"```\nNitro sniper toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="giveawaytoasts",
        usage="<on/off>",
        description="Giveaway toasts"
    )
    async def giveawaytoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Giveaway toasts » {color.print_gradient(f'{mode}')}")
            config.toast.giveaway(mode)
            await message_builder(luna, description=f"```\nGiveaway toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="privnotetoasts",
        usage="<on/off>",
        description="Privnote toasts"
    )
    async def privnotetoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Privnote toasts » {color.print_gradient(f'{mode}')}")
            config.toast.privnote(mode)
            await message_builder(luna, description=f"```\nPrivnote toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="selfbottoasts",
        usage="<on/off>",
        description="Selfbot toasts"
    )
    async def selfbottoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Selfbot toasts » {color.print_gradient(f'{mode}')}")
            config.toast.selfbot(mode)
            await message_builder(luna, description=f"```\nSelfbot toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="pingtoasts",
        usage="<on/off>",
        description="Ping toasts"
    )
    async def pingtoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Pings toasts » {color.print_gradient(f'{mode}')}")
            config.toast.pings(mode)
            await message_builder(luna, description=f"```\nPings toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="ghostpingtoasts",
        usage="<on/off>",
        description="Ghostping toasts"
    )
    async def ghostpingtoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Ghostping toasts » {color.print_gradient(f'{mode}')}")
            config.toast.ghostpings(mode)
            await message_builder(luna, description=f"```\nGhostping toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="friendtoasts",
        usage="<on/off>",
        description="Friend event toasts"
    )
    async def friendtoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Friend event toasts » {color.print_gradient(f'{mode}')}")
            config.toast.friendevents(mode)
            await message_builder(luna, description=f"```\nFriend event toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="guildtoasts",
        usage="<on/off>",
        description="Guild event toasts"
    )
    async def guildtoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Guild event toasts » {color.print_gradient(f'{mode}')}")
            config.toast.guildevents(mode)
            await message_builder(luna, description=f"```\nGuild event toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="roletoasts",
        usage="<on/off>",
        description="Role update toasts"
    )
    async def roletoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Role update toasts » {color.print_gradient(f'{mode}')}")
            config.toast.roleupdates(mode)
            await message_builder(luna, description=f"```\nRole update toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="nicktoasts",
        usage="<on/off>",
        description="Nickname update toasts"
    )
    async def nicktoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(
                f"Nickname update toasts » {color.print_gradient(f'{mode}')}"
            )
            config.toast.nickupdates(mode)
            await message_builder(luna, description=f"```\nNickname update toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="protectiontoasts",
        usage="<on/off>",
        description="Protection toasts"
    )
    async def protectiontoasts(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Protection toasts » {color.print_gradient(f'{mode}')}")
            config.toast.protection(mode)
            await message_builder(luna, description=f"```\nProtection toasts » {mode}```")
        else:
            await mode_error(luna, "on or off")