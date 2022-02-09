import discord
from discord import *
from discord.ext import commands

import time

# /////////////////////////////////////////////////////////////////////////////

from filehandler import *
from jsonhandler import *

# /////////////////////////////////////////////////////////////////////////////

# bot = commands.Bot(command_prefix=, self_bot=True, , case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off(), status=statuscon()))
bot = commands.Bot(command_prefix=get_prefix(), self_bot=True, case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off())