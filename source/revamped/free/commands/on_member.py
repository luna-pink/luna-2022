from discord.ext import commands
from .utilities import *


class OnMember(commands.Cog, name="on member events"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if anti_raid is True:
            guilds = files.json(
                "data/protections/config.json", "guilds", documents=False
            )
            if member.guild.id in guilds:
                try:
                    guild = member.guild
                    async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
                        if member.guild.id in whitelisted_users.keys(
                        ) and i.user.id in whitelisted_users[member.guild.id].keys():
                            return
                        else:
                            prints.message(
                                f"{member.name}#{member.discriminator} banned by Anti-Raid"
                            )
                            await guild.ban(member, reason="Luna Anti-Raid")
                except Exception as e:
                    print(e)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if anti_raid is True:
            guilds = files.json(
                "data/protections/config.json", "guilds", documents=False
            )
            if member.guild.id in guilds:
                try:
                    guild = member.guild
                    async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
                        if guild.id in whitelisted_users.keys() and i.user.id in whitelisted_users[
                            guild.id
                        ].keys() and i.user.id is not self.bot.user.id:
                            prints.message(
                                f"{i.user.name}#{i.user.discriminator} not banned"
                            )
                        else:
                            prints.message(
                                f"{i.user.name}#{i.user.discriminator} banned by Anti-Raid"
                            )
                            await guild.ban(i.user, reason="Luna Anti-Raid")
                except Exception as e:
                    print(e)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        if self.bot.user is user:
            if files.json(
                    "data/notifications/toasts.json",
                    "guildevents",
                    documents=False
            ) == "on" and files.json(
                "data/notifications/toasts.json",
                "toasts",
                documents=False
            ) == "on":
                notify.toast(
                    f"You have been banned\nServer »  {guild.name}"
                )
                print()
                prints.message("You have been banned")
                prints.message(f"Server » {guild.name}")
                print()
            if files.json(
                    "data/webhooks/webhooks.json",
                    "guildevents",
                    documents=False
            ) == "on" and files.json(
                "data/webhooks/webhooks.json",
                "webhooks",
                documents=False
            ) == "on" and not webhook.ghostpings_url() == "webhook-url-here":
                notify.webhook(
                    url=webhook.ghostpings_url(),
                    name="Ban",
                    description=f"You have been banned\nServer »  {guild.name}"
                )

    # @commands.Cog.listener()
    # async def on_guild_channel_create(self, channel):
    #     if "ticket" in channel.name.lower() and channel.permissions_for(
    #             channel.guild.me
    #     ).read_messages:
    #         if files.json(
    #                 "data/notifications/toasts.json",
    #                 "guildevents",
    #                 documents=False
    #         ) == "on" and files.json(
    #             "data/notifications/toasts.json",
    #             "toasts",
    #             documents=False
    #         ) == "on":
    #             notify.toast(
    #                 f"New Ticket\nServer » {channel.guild.name}\nChannel » {channel.name}"
    #             )
    #             print()
    #             prints.message(f"{color.print_gradient('New Ticket')}")
    #             prints.message(
    #                 f"Server  | {color.print_gradient(f'{channel.guild.name}')}"
    #             )
    #             prints.message(
    #                 f"Channel | {color.print_gradient(f'{channel.name}')}"
    #             )
    #             print()
    #         if files.json(
    #                 "data/webhooks/webhooks.json",
    #                 "guildevents",
    #                 documents=False
    #         ) == "on" and files.json(
    #             "data/webhooks/webhooks.json",
    #             "webhooks",
    #             documents=False
    #         ) == "on" and not webhook.ghostpings_url() == "webhook-url-here":
    #             notify.webhook(
    #                 url=webhook.ghostpings_url(),
    #                 name="New Ticket",
    #                 description=f"New Ticket\nServer » {channel.guild.name}\nChannel » {channel.name}"
    #             )

    @commands.Cog.listener()
    async def on_relationship_add(self, relationship):
        if isinstance(relationship.type, discord.RelationshipType.incoming_request):
            if files.json(
                    "data/notifications/toasts.json",
                    "friendevents",
                    documents=False
            ) == "on" and files.json(
                "data/notifications/toasts.json",
                "toasts",
                documents=False
            ) == "on":
                notify.toast(
                    f"Incoming Friend Request\nUser » {relationship.user}\nID » {relationship.user.id}"
                )
                print()
                prints.message("Incoming Friend Request")
                prints.message(
                    f"User    | {color.print_gradient(f'{relationship.user}')}"
                )
                prints.message(
                    f"ID      | {color.print_gradient(f'{relationship.user.id}')}"
                )
                print()
            if files.json(
                    "data/webhooks/webhooks.json",
                    "friendevents",
                    documents=False
            ) == "on" and files.json(
                "data/webhooks/webhooks.json",
                "webhooks",
                documents=False
            ) == "on" and not webhook.ghostpings_url() == "webhook-url-here":
                notify.webhook(
                    url=webhook.ghostpings_url(),
                    name="friendevents",
                    description=f"Incoming Friend Request\nUser » {relationship.user}\nID » {relationship.user.id}"
                )
        if isinstance(relationship.type, discord.RelationshipType.friend):
            if files.json(
                    "data/notifications/toasts.json",
                    "friendevents",
                    documents=False
            ) == "on" and files.json(
                "data/notifications/toasts.json",
                "toasts",
                documents=False
            ) == "on":
                notify.toast(
                    f"New Friend\nUser » {relationship.user}\nID » {relationship.user.id}"
                )
                print()
                prints.message("New Friend")
                prints.message(
                    f"User    | {color.print_gradient(f'{relationship.user}')}"
                )
                prints.message(
                    f"ID      | {color.print_gradient(f'{relationship.user.id}')}"
                )
                print()
            if files.json(
                    "data/webhooks/webhooks.json",
                    "friendevents",
                    documents=False
            ) == "on" and files.json(
                "data/webhooks/webhooks.json",
                "webhooks",
                documents=False
            ) == "on" and not webhook.ghostpings_url() == "webhook-url-here":
                notify.webhook(
                    url=webhook.ghostpings_url(),
                    name="friendevents",
                    description=f"New Friend\nUser » {relationship.user}\nID » {relationship.user.id}"
                )

    @commands.Cog.listener()
    async def on_relationship_remove(self, relationship):
        if isinstance(relationship.type, discord.RelationshipType.outgoing_request):
            if files.json(
                    "data/notifications/toasts.json",
                    "friendevents",
                    documents=False
            ) == "on" and files.json(
                "data/notifications/toasts.json",
                "toasts",
                documents=False
            ) == "on":
                notify.toast(
                    f"Outgoing Friend Request\nUser » {relationship.user}\nID » {relationship.user.id}"
                )
                print()
                prints.message("Outgoing Friend Request")
                prints.message(
                    f"User    | {color.print_gradient(f'{relationship.user}')}"
                )
                prints.message(
                    f"ID      | {color.print_gradient(f'{relationship.user.id}')}"
                )
                print()
            if files.json(
                    "data/webhooks/webhooks.json",
                    "friendevents",
                    documents=False
            ) == "on" and files.json(
                "data/webhooks/webhooks.json",
                "webhooks",
                documents=False
            ) == "on" and not webhook.ghostpings_url() == "webhook-url-here":
                notify.webhook(
                    url=webhook.ghostpings_url(),
                    name="friendevents",
                    description=f"Outgoing Friend Request\nUser » {relationship.user}\nID » {relationship.user.id}"
                )

        if isinstance(relationship.type, discord.RelationshipType.blocked):
            if files.json(
                    "data/notifications/toasts.json",
                    "friendevents",
                    documents=False
            ) == "on" and files.json(
                "data/notifications/toasts.json",
                "toasts",
                documents=False
            ) == "on":
                notify.toast(
                    f"Blocked/Removed Friend\nUser » {relationship.user}\nID » {relationship.user.id}"
                )
                print()
                prints.message("Blocked/Removed Friend")
                prints.message(
                    f"User    | {color.print_gradient(f'{relationship.user}')}"
                )
                prints.message(
                    f"ID      | {color.print_gradient(f'{relationship.user.id}')}"
                )
                print()
            if files.json(
                    "data/webhooks/webhooks.json",
                    "friendevents",
                    documents=False
            ) == "on" and files.json(
                "data/webhooks/webhooks.json",
                "webhooks",
                documents=False
            ) == "on" and not webhook.ghostpings_url() == "webhook-url-here":
                notify.webhook(
                    url=webhook.ghostpings_url(),
                    name="friendevents",
                    description=f"Blocked/Removed Friend\nUser » {relationship.user}\nID » {relationship.user.id}"
                )