from discord.ext import commands
from .utilities import *


class WebhooksCog(commands.Cog, name="Webhook commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="webhooks",
        usage="<on/off>",
        description="Webhooks"
    )
    async def webhooks(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.webhooks(mode)
            await message_builder(luna, description=f"```\nWebhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wlogin",
        usage="<on/off>",
        description="Login webhooks"
    )
    async def wlogin(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Login webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.login(mode)
            await message_builder(luna, description=f"```\nLogin webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wnitro",
        usage="<on/off>",
        description="Nitro webhooks"
    )
    async def wnitro(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Nitro webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.nitro(mode)
            await message_builder(luna, description=f"```\nNitro webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wgiveaways",
        usage="<on/off>",
        description="Giveaway webhooks"
    )
    async def wgiveaways(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Giveaway webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.giveaway(mode)
            await message_builder(luna, description=f"```\nGiveaway webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wprivnote",
        usage="<on/off>",
        description="Privnote webhooks"
    )
    async def wprivnote(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Privnote webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.privnote(mode)
            await message_builder(luna, description=f"```\nPrivnote webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wselfbot",
        usage="<on/off>",
        description="Selfbot webhooks"
    )
    async def wselfbot(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Selfbot webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.selfbot(mode)
            await message_builder(luna, description=f"```\nSelfbot webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wpings",
        usage="<on/off>",
        description="Pings webhooks"
    )
    async def wpings(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Pings webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.pings(mode)
            await message_builder(luna, description=f"```\nPings webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wghostpings",
        usage="<on/off>",
        description="Ghostpings webhooks"
    )
    async def wghostpings(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Ghostpings webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.ghostpings(mode)
            await message_builder(luna, description=f"```\nGhostpings webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wfriends",
        usage="<on/off>",
        description="Friend event webhooks"
    )
    async def wfriends(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(
                f"Friend event webhooks » {color.print_gradient(f'{mode}')}"
            )
            config.webhook.friendevents(mode)
            await message_builder(luna, description=f"```\nFriend event webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wguilds",
        usage="<on/off>",
        description="Guild event webhooks"
    )
    async def wguilds(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Guild event webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.guildevents(mode)
            await message_builder(luna, description=f"```\nGuild event webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wroles",
        usage="<on/off>",
        description="Role update webhooks"
    )
    async def wroles(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Role event webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.roleupdates(mode)
            await message_builder(luna, description=f"```\nRole event webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wnick",
        usage="<on/off>",
        description="Nickname update webhooks"
    )
    async def wnick(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(
                f"Nickname event webhooks » {color.print_gradient(f'{mode}')}"
            )
            config.webhook.nickupdates(mode)
            await message_builder(luna, description=f"```\nNickname event webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(
        name="wprotection",
        usage="<on/off>",
        description="Protection webhooks"
    )
    async def wprotection(self, luna, mode: str):

        if mode == "on" or mode == "off":
            prints.message(f"Protection webhooks » {color.print_gradient(f'{mode}')}")
            config.webhook.protection(mode)
            await message_builder(luna, description=f"```\nProtection webhooks » {mode}```")
        else:
            await mode_error(luna, "on or off")