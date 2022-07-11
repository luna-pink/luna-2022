from discord.ext import commands
from .utilities import *


class WebhookSetupCog(commands.Cog, name="Webhook setup"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="webhooksetup",
        usage="",
        description="Set up all webhooks"
    )
    async def webhooksetup(self, luna):

        try:
            prints.event("Creating webhooks...")
            await message_builder(luna, description="```\nCreating webhooks...```")
            category = await luna.guild.create_category_channel(name="Luna Webhooks")
            login = await category.create_text_channel("login")
            nitro = await category.create_text_channel("nitro")
            giveaway = await category.create_text_channel("giveaways")
            privnote = await category.create_text_channel("privnotes")
            selfbot = await category.create_text_channel("selfbots")
            pings = await category.create_text_channel("pings")
            ghostpings = await category.create_text_channel("ghostpings")
            friendevents = await category.create_text_channel("friend-events")
            guildevents = await category.create_text_channel("guild-events")
            roleupdates = await category.create_text_channel("role-updates")
            nickupdates = await category.create_text_channel("nickname-updates")
            protection = await category.create_text_channel("protections")

            wlogin = await login.create_webhook(name="Login Webhook")
            wnitro = await nitro.create_webhook(name="Nitro Webhook")
            wgiveaways = await giveaway.create_webhook(name="Giveaways Webhook")
            wprivnote = await privnote.create_webhook(name="Privnotes Webhook")
            wselfbot = await selfbot.create_webhook(name="Selfbots Webhook")
            wpings = await pings.create_webhook(name="Pings Webhook")
            wghostpings = await ghostpings.create_webhook(name="Ghostpings Webhook")
            wfriendevents = await friendevents.create_webhook(name="Friend Events Webhook")
            wguildevents = await guildevents.create_webhook(name="Guild Events Webhook")
            wroleupdates = await roleupdates.create_webhook(name="Role Updates Webhook")
            wnickupdates = await nickupdates.create_webhook(name="Nickname Updates Webhook")
            wprotection = await protection.create_webhook(name="Protections Webhook")

            config.webhook.login_url(wlogin.url)
            config.webhook.nitro_url(wnitro.url)
            config.webhook.giveaway_url(wgiveaways.url)
            config.webhook.privnote_url(wprivnote.url)
            config.webhook.selfbot_url(wselfbot.url)
            config.webhook.pings_url(wpings.url)
            config.webhook.ghostpings_url(wghostpings.url)
            config.webhook.friendevents_url(wfriendevents.url)
            config.webhook.guildevents_url(wguildevents.url)
            config.webhook.roleupdates_url(wroleupdates.url)
            config.webhook.nickupdates_url(wnickupdates.url)
            config.webhook.protection_url(wprotection.url)
            prints.message(
                "Successfully created all webhooks and stored them in the config"
            )
            await message_builder(
                luna, title="Webhooks Setup",
                description=f"```\nSuccessfully created all webhooks and stored them in the config```"
            )
        except Exception as e:
            await error_builder(luna, description=f"```{e}```")