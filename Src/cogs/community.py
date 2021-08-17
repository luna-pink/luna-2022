import discord
from discord.ext import commands
import main
import asyncio
import random
import string

def Randprntsc():
		letterprn = ''.join(random.choices(string.ascii_lowercase, k=4))
		numberprn = random.randint(10, 99)
		return f'https://prnt.sc/{numberprn}{letterprn}'

class CommunityCog(commands.Cog, name="Community commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "prntsc",
						usage="",
						description = "Send a random screenshot from prnt.sc")
	async def prntsc(self, ctx):
		await ctx.message.delete()
		await ctx.send(Randprntsc())

def setup(bot:commands.Bot):
	bot.add_cog(CommunityCog(bot))