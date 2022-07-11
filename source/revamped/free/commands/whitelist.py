from discord.ext import commands
from .utilities import *


class WhitelistCog(commands.Cog, name="Whitelist commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="whitelist",
        usage="<@member>",
        description="Whitelist someone"
    )
    async def whitelist(self, luna, user: discord.Member = None):

        if user is None:
            await luna.send("Please specify a user to whitelist")
        else:
            if luna.guild.id not in whitelisted_users.keys():
                whitelisted_users[luna.guild.id] = {}
            if user.id in whitelisted_users[luna.guild.id]:
                await message_builder(
                    luna,
                    description=f"```\n{user.name}#{user.discriminator} is already whitelisted```"
                )
            else:
                whitelisted_users[luna.guild.id][user.id] = 0
                await message_builder(
                    luna, description=f"```\nWhitelisted " + user.name.replace("*", "\\*").replace(
                        "`",
                        "\\`"
                    ).replace(
                        "_", "\\_"
                    ) + "#" + user.discriminator + "```"
                )

    @commands.command(
        name="unwhitelist",
        usage="",
        description="Unwhitelist someone"
    )
    async def unwhitelist(self, luna, user: discord.Member = None):

        if user is None:
            await luna.send("Please specify the user you would like to unwhitelist")
        else:
            if luna.guild.id not in whitelisted_users.keys():
                await luna.send("That user is not whitelisted")
                return
            if user.id in whitelisted_users[luna.guild.id]:
                whitelisted_users[luna.guild.id].pop(user.id, 0)
                await message_builder(
                    luna,
                    description=f"```\nUnwhitelisted " + user.name.replace("*", "\\*").replace(
                        "`",
                        "\\`"
                    ).replace(
                        "_", "\\_"
                    ) + "#" + user.discriminator + "```"
                )

    @commands.command(
        name="whitelisted",
        usage="",
        description="Show the whitelisted list"
    )
    async def whitelisted(self, luna, g=None):

        if g in ['-g', '-global']:
            whitelist = '`All Whitelisted Users:`\n'
            for key in whitelisted_users:
                for key2 in whitelisted_users[key]:
                    user = self.bot.get_user(key2)
                    whitelist += '+ ' + user.name.replace('*', "\\*").replace('`', "\\`").replace('_', "\\_") + "#" + user.discriminator + " - " + \
                                 self.bot.get_guild(key).name.replace(
                                     '*', "\\*"
                                 ).replace('`', "\\`").replace('_', "\\_") + "" + "\n"
        else:
            whitelist = "`" + luna.guild.name.replace('*', "\\*").replace(
                '`', "\\`"
            ).replace('_', "\\_") + '\'s Whitelisted Users:`\n'
            for key in self.bot.whitelisted_users:
                if key == luna.guild.id:
                    for key2 in self.bot.whitelisted_users[luna.guild.id]:
                        user = self.bot.get_user(key2)
                        whitelist += '+ ' + user.name.replace('*', "\\*").replace('`', "\\`").replace(
                            '_', "\\_"
                        ) + "#" + user.discriminator + " (" + str(user.id) + ")" + "\n"

        await message_builder(luna, description=f"```\n{whitelist}```")

    @commands.command(
        name="clearwhitelist",
        usage="",
        description="Clear the whitelisted list"
    )
    async def clearwhitelist(self, luna):

        whitelisted_users.clear()
        await message_builder(luna, description=f"```\nCleared the whitelist```")
