from discord.ext import commands
from .utilities import *


class OnTyping(commands.Cog, name="on typing"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_typing(self, channel, member, when):
        if member in self.bot.user.friends and isinstance(
                channel, discord.DMChannel
        ):
            if files.json(
                    "data/notifications/toasts.json",
                    "friendevents",
                    documents=False
            ) == "on" and files.json(
                "data/notifications/toasts.json",
                "toasts",
                documents=False
            ) == "on":
                notify.toast(f"{member} is typing")
            if files.json("data/webhooks/webhooks.json", "friendevents", documents=False) == "on" and files.json("data/webhooks/webhooks.json", "webhooks", documents=False) == "on" and webhook.friendevents_url() != "webhook-url-here":
                notify.webhook(
                    url=webhook.friendevents_url(
                    ), name="friendevents", description=f"{member} is typing"
                )
