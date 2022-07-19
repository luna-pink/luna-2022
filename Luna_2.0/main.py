from dotjson import load_keys, get_key, write_key, write_new, remove_key
from discord import *
from discord.ext import commands

# ----------------------------------------------------------------------------------------------------------------------

from events.miscellaneous.on_ready import OnReadyCog

from commands.help.help import HelpCog

# ----------------------------------------------------------------------------------------------------------------------

load_keys(['data'])

bot = commands.Bot(
    command_prefix=get_key('prefix'),
    case_insensitive=True,
    strip_after_prefix=True,
    self_bot=True,
    help_command=None,
    guild_subscription_options=GuildSubscriptionOptions.off(),
    key="Jgy67HUXLH!Luna",
)


bot.add_cog(OnReadyCog(bot))
bot.add_cog(HelpCog(bot))


def load_luna():
    print('Logging in...')
    bot.run(get_key('token'))


if __name__ == '__main__':
    load_luna()
