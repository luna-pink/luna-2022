from discord.ext import commands
from .utilities import *


class OnDelete(commands.Cog, name="on delete"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author == self.bot.user:
            return

        if f'<@!{self.bot.user.id}>' in message.content:
            if files.json(
                    "data/notifications/toasts.json",
                    "ghostpings",
                    documents=False
            ) == "on" and files.json(
                "data/notifications/toasts.json",
                "toasts",
                documents=False
            ) == "on":
                notify.toast(
                    f"You have been ghostpinged\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}"
                )
            if files.json("data/webhooks/webhooks.json", "ghostpings", documents=False) == "on" and files.json("data/webhooks/webhooks.json", "webhooks", documents=False) == "on" and webhook.ghostpings_url() != "webhook-url-here":
                notify.webhook(
                    url=webhook.ghostpings_url(),
                    name="ghostpings",
                    description=f"You have been ghostpinged\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}"
                )
            print()
            prints.sniper(f"{color.print_gradient('You have been ghostpinged')}")
            prints.sniper(f"Server  | {color.print_gradient(f'{message.guild}')}")
            prints.sniper(
                f"Channel | {color.print_gradient(f'{message.channel}')}"
            )
            prints.sniper(f"Author  | {color.print_gradient(f'{message.author}')}")
            print()

        # ///////////////////////////////////////////////////////////////
        # Anti Deleting

        if anti_deleting:
            guilds = files.json(
                "data/protections/config.json", "guilds", documents=False
            )
            if message.guild.id in guilds:
                print()
                prints.event("Anti Deleting")
                prints.event(f"Server  | {color.print_gradient(f'{message.guild}')}")
                prints.sniper(
                    f"Channel | {color.print_gradient(f'{message.channel}')}"
                )
                prints.sniper(f"Author  | {color.print_gradient(f'{message.author}')}")
                print()

        # ///////////////////////////////////////////////////////////////
        # Selfbot Detection - BETA

        # else:
        #     global cooldown
        #     prefixes = ['.', ',', '-', '_', '!', '?', '>', '+', '*', '#', '$', '%', '^', '&', '@', '~', '`', '<', ';', ':', '\\', '/', '|', '=', '{', '}', '[', ']', '"', "'"]
        #     for pref in prefixes:
        #         if message.content.startswith(pref) and message.content in command_names_list:
        #             if cooldown.count(message.author.id) == 0:
        #                 cooldown.append(message.author.id)
        #                 if files.json(
        #                     "data/snipers/selfbot.json",
        #                     "sniper",
        #                         documents=False) == "on":
        #                     if files.json(
        #                             "data/notifications/toasts.json",
        #                             "selfbot",
        #                             documents=False) == "on" and files.json(
        #                             "data/notifications/toasts.json",
        #                             "toasts",
        #                             documents=False) == "on":
        #                         notify.toast(
        #                             f"Selfbot Detected\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
        #                     if files.json(
        #                             "data/webhooks/webhooks.json",
        #                             "selfbot",
        #                             documents=False) == "on" and files.json(
        #                             "data/webhooks/webhooks.json",
        #                             "webhooks",
        #                             documents=False) == "on" and not webhook.selfbot_url() == "webhook-url-here":
        #                         notify.webhook(
        #                             url=webhook.selfbot_url(),
        #                             name="selfbot",
        #                             description=f"Selfbot Detected\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
        #                     print()
        #                     prints.sniper(
        #                         f"{color.print_gradient('Selfbot Detected')}")
        #                     prints.sniper(
        #                         f"Server  | {color.print_gradient(f'{message.guild}')}")
        #                     prints.sniper(
        #                         f"Channel | {color.print_gradient(f'{message.channel}')}")
        #                     prints.sniper(
        #                         f"Author  | {color.print_gradient(f'{message.author}')}")
        #                     print()
        #                     await asyncio.sleep(3600)
        #                     cooldown.remove(message.author.id)
        #                 else:
        #                     pass
        #             else:
        #                 pass
        #         else:
        #             pass
