from discord.ext import commands
from .utilities import *
from discord.ext.commands import MissingPermissions, CheckFailure


class OnCommandErrorCog(commands.Cog, name="on command error"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, luna: commands.Context, error: Exception):
        error_str = str(error)
        if isinstance(error, commands.CommandOnCooldown):
            try:
                await luna.message.delete()
            except BaseException:
                pass
            day = round(error.retry_after / 86400)
            hour = round(error.retry_after / 3600)
            minute = round(error.retry_after / 60)
            if day > 0:
                if configs.error_log() == "console":
                    prints.error(
                        'This command is on cooldown, for ' +
                        str(day) +
                        "day(s)"
                    )
                else:
                    await luna.send('This command is on cooldown, for ' + str(day) + "day(s)", delete_after=3)
            elif hour > 0:
                if configs.error_log() == "console":
                    prints.error(
                        'This command is on cooldown, for ' +
                        str(hour) +
                        " hour(s)"
                    )
                else:
                    await luna.send('This command is on cooldown, for ' + str(hour) + " hour(s)", delete_after=3)
            elif minute > 0:
                if configs.error_log() == "console":
                    prints.error(
                        'This command is on cooldown, for ' +
                        str(minute) +
                        " minute(s)"
                    )
                else:
                    await luna.send('This command is on cooldown, for ' + str(minute) + " minute(s)", delete_after=3)
            else:
                if configs.error_log() == "console":
                    prints.error(
                        f'You are being ratelimited, for {error.retry_after:.2f} second(s)'
                    )
                else:
                    await luna.send(f'You are being ratelimited, for {error.retry_after:.2f} second(s)', delete_after=3)

        if isinstance(error, commands.CommandNotFound):
            try:
                await luna.message.delete()
            except BaseException:
                pass
            prefix = files.json("data/config.json", "prefix", documents=False)
            helptext = ""
            amount = 0
            for command in self.bot.commands:
                helptext += f"{prefix + command.name + ' ' + command.usage:<17} » {command.description},"

            error_text = f"{error}"
            subtract = len(error_text) - 14
            error_strip = error_text[9:subtract]
            commandlist = helptext.split(",")
            # commandlistfind = [ string for string in commandlist if error_strip in string]
            commandlistfind = [""]
            for string in commandlist:
                if amount < 5:
                    if error_strip in string:
                        commandlistfind = [string]
                        amount += 1
                else:
                    pass
            try:
                commandlistfind = '\n'.join(str(e) for e in commandlistfind)
            except BaseException:
                commandlistfind = ""
            if not len(commandlistfind) == 0:
                found = f"```\n\nDid you mean?\n\n{commandlistfind}```"
            else:
                found = ""
            if configs.error_log() == "message":
                await error_builder(
                    luna, f"```\nNot Found\n\n{error}```{found}```\nNote\n\nYou can use \"search\" to search for a command.\n{prefix}search <command> » Search for a command```"
                )
            else:
                await error_builder(luna, f"```\nNot Found\n\n{error}```")
        elif isinstance(error, CheckFailure):
            try:
                await luna.message.delete()
            except BaseException:
                pass
            await error_builder(luna, f"```\n{error}```")
        elif isinstance(error, commands.MissingRequiredArgument):
            try:
                await luna.message.delete()
            except BaseException:
                pass
            await error_builder(luna, f"```\nMissing arguments\n\n{error}```")
        elif isinstance(error, MissingPermissions):
            try:
                await luna.message.delete()
            except BaseException:
                pass
            await error_builder(luna, f"```\nMissing permissions\n\n{error}```")
        elif isinstance(error, commands.CommandInvokeError):
            try:
                await luna.message.delete()
            except BaseException:
                pass
            await error_builder(luna, f"```\n{error}```")
        elif "Cannot send an empty message" in error_str:
            try:
                await luna.message.delete()
            except BaseException:
                pass
            await error_builder(luna, f"```\n{error}```")
        elif "Cannot send messages to this user" in error_str:
            try:
                await luna.message.delete()
            except BaseException:
                pass
            await error_builder(luna, f"```\nCannot send a message to this user\n\n{error}```")
        elif "Cannot send messages in this channel" in error_str:
            try:
                await luna.message.delete()
            except BaseException:
                pass
            await error_builder(luna, f"```\nCannot send a message in this channel\n\n{error}```")
        elif "Cannot send files bigger than" in error_str:
            try:
                await luna.message.delete()
            except BaseException:
                pass
            await error_builder(luna, f"```\nCannot send files bigger than 8MB\n\n{error}```")
        else:
            try:
                await luna.message.delete()
            except BaseException:
                pass
            await error_builder(luna, f"```\n{error}```")