from discord.ext import commands
from .utilities import *


class WebhookUrlCog(commands.Cog, name="Webhook urls"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="wulogin",
        usage="<url>",
        description="Login webhook"
    )
    async def wulogin(self, luna, url: str):
        config.webhook.login_url(url)
        prints.message(
            f"Changed login webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged login webhook url to » {url}```")

    @commands.command(
        name="wunitro",
        usage="<url>",
        description="Nitro webhook"
    )
    async def wunitro(self, luna, url: str):
        config.webhook.nitro_url(url)
        prints.message(
            f"Changed nitro webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged nitro webhook url to » {url}```")

    @commands.command(
        name="wugiveaway",
        usage="<url>",
        description="Giveaways webhook"
    )
    async def wugiveaway(self, luna, url: str):
        config.webhook.giveaway_url(url)
        prints.message(
            f"Changed giveaways webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged giveaways webhook url to » {url}```")

    @commands.command(
        name="wuprivnote",
        usage="<url>",
        description="Privnotes webhook"
    )
    async def wuprivnote(self, luna, url: str):
        config.webhook.privnote_url(url)
        prints.message(
            f"Changed privnotes webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged privnotes webhook url to » {url}```")

    @commands.command(
        name="wuselfbot",
        usage="<url>",
        description="Selfbots webhook"
    )
    async def wuselfbot(self, luna, url: str):
        config.webhook.selfbot_url(url)
        prints.message(
            f"Changed selfbots webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged selfbots webhook url to » {url}```")

    @commands.command(
        name="wupings",
        usage="<url>",
        description="Pings webhook"
    )
    async def wupings(self, luna, url: str):
        config.webhook.pings_url(url)
        prints.message(
            f"Changed pings webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged pings webhook url to » {url}```")

    @commands.command(
        name="wughost",
        usage="<url>",
        description="Ghostpings webhook"
    )
    async def wughost(self, luna, url: str):
        config.webhook.ghostpings_url(url)
        prints.message(
            f"Changed ghostpings webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged ghostpings webhook url to » {url}```")

    @commands.command(
        name="wufriends",
        usage="<url>",
        description="Friend events webhook"
    )
    async def wufriends(self, luna, url: str):
        config.webhook.friendevents_url(url)
        prints.message(
            f"Changed friend events webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged friend events webhook url to » {url}```")

    @commands.command(
        name="wuguilds",
        usage="<url>",
        description="Guild events webhook"
    )
    async def wuguilds(self, luna, url: str):
        config.webhook.guildevents_url(url)
        prints.message(
            f"Changed guild events webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged guild events webhook url to » {url}```")

    @commands.command(
        name="wuroles",
        usage="<url>",
        description="Role updates webhook"
    )
    async def wuroles(self, luna, url: str):
        config.webhook.roleupdates_url(url)
        prints.message(
            f"Changed role updates webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged role updates webhook url to » {url}```")

    @commands.command(
        name="wunick",
        usage="<url>",
        description="Nick updates webhook"
    )
    async def wunick(self, luna, url: str):
        config.webhook.nickupdates_url(url)
        prints.message(
            f"Changed nick updates webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged nick updates webhook url to » {url}```")

    @commands.command(
        name="wuprotection",
        usage="<url>",
        description="Protection webhook"
    )
    async def wuprotection(self, luna, url: str):
        config.webhook.protection_url(url)
        prints.message(
            f"Changed protection webhook url to » {color.print_gradient(f'{url}')}"
        )
        await message_builder(luna, description=f"```\nChanged protection webhook url to » {url}```")