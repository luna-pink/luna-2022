import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, NotOwner
import time
import main as luna
import asyncio

class OnCommand(commands.Cog, name="on command"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_command(self, ctx:commands.Context):
		luna.printcommand(ctx.command.name)


def setup(bot):
	bot.add_cog(OnCommand(bot))
