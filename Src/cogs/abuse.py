from os import add_dll_directory
import discord
from discord.ext import commands
import main as luna
import asyncio

class AbuseCog(commands.Cog, name="Abusive commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
		
	@commands.command(name = "purgehack",
					usage="",
					description = "Purge a channel without permissions")
	async def purgehack(self, ctx):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
		else:
			if luna.errorlog() == "console":
				luna.printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = "spam",
					usage="<delay> <amount> <message>",
					description = "Spam a message")
	async def spam(self, ctx, delay: int = None, amount: int = None, *, message: str = None):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			try:
				if delay is None or amount is None or message is None:
					await ctx.send(f"Usage: {self.bot.prefix}spam <delay> <amount> <message>")
				else:
					for each in range(0, amount):
						await asyncio.sleep(delay)
						await ctx.send(f"{message}")
			except Exception as e:
				await ctx.send(f"Error: {e}")
		else:
			if luna.errorlog() == "console":
				luna.printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = "spamghostping",
					usage="<delay> <amount> <@member>",
					aliases=['spg', 'spamgp', 'sghostping'],
					description = "Spam ghostping someone")
	async def spamghostping(self, ctx, delay: int = None, amount: int = None, user: discord.Member = None):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			try:
				if delay is None or amount is None or user is None:
					await ctx.send(f"Usage: {self.bot.prefix}spamghostping <delay> <amount> <@member>")
				else:
					for each in range(0, amount):
						await asyncio.sleep(delay)
						await ctx.send(user.mention, delete_after=0)
			except Exception as e:
				await ctx.send(f"Error: {e}")
		else:
			if luna.errorlog() == "console":
				luna.printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = "mpreact",
					usage="<emoji>",
					description = "Reacts to the latest 20 messages")
	async def mpreact(self, ctx, emoji):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			messages = await ctx.message.channel.history(limit=20).flatten()
			for message in messages:
				await message.add_reaction(emoji)
		else:
			if luna.errorlog() == "console":
				luna.printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = "junknick",
					usage="",
					description = "Change your nickname to pure junk")
	async def junknick(self, ctx):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			try:
				name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫"
				await ctx.author.edit(nick=name)
			except Exception as e:
				if luna.errorlog() == "console":
					luna.printerror(e)
				else:
					embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=e, color=0xff0000)
					embed.set_thumbnail(url=luna.imagevar())
					embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
					embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
					embed.set_image(url=luna.largeimagevar())
					await luna.send(ctx, embed)
		else:
			if luna.errorlog() == "console":
				luna.printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = "dmall",
					usage="<message>",
					description = "DM a message to every member")
	async def dmall(self, ctx, *, message: str):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			sent = 0
			try:
				members = ctx.channel.members
				for member in members:
					if member is not ctx.author:
						try:
							await member.send(message)
							luna.printmessage(f"Sent {message} to {member}")
							sent += 1
						except Exception:
							pass
			except Exception:
				pass
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Sent **{message}** to **{sent}** users.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			if luna.errorlog() == "console":
				luna.printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = "sendall",
					usage="<message>",
					description = "Send a message in every channel")
	async def sendall(self, ctx, *, message):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			try:
				channels = ctx.guild.text_channels
				for channel in channels:
					await channel.send(message)
			except:
				pass
		else:
			if luna.errorlog() == "console":
				luna.printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)


def setup(bot:commands.Bot):
	bot.add_cog(AbuseCog(bot))