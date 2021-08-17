import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, NotOwner
import time
import main as luna
import asyncio


class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):
		error_str = str(error)
		error = getattr(error, 'original', error)
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.message.delete()
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			if day > 0:
				if luna.errorlog() == "console":
					luna.printerror('This command is on cooldown, for '+str(day)+ "day(s)")
				else:
					await ctx.send('This command is on cooldown, for '+str(day)+ "day(s)", delete_after=3)
			elif hour > 0:
				if luna.errorlog() == "console":
					luna.printerror('This command is on cooldown, for '+str(hour)+ " hour(s)")
				else:
					await ctx.send('This command is on cooldown, for '+str(hour)+ " hour(s)", delete_after=3)
			elif minute > 0:
				if luna.errorlog() == "console":
					luna.printerror('This command is on cooldown, for '+ str(minute)+" minute(s)")
				else:
					await ctx.send('This command is on cooldown, for '+ str(minute)+" minute(s)", delete_after=3)
			else:
				if luna.errorlog() == "console":
					luna.printerror(f'You are being ratelimited, for {error.retry_after:.2f} second(s)')
				else:
					await ctx.send(f'You are being ratelimited, for {error.retry_after:.2f} second(s)', delete_after=3)

		if isinstance(error, CommandNotFound):
			try:
				await ctx.message.delete()
			except Exception:
				pass
			if luna.errorlog() == "console":
				luna.printerror(error)
			else:
				embed = discord.Embed(
					title="**Error**",
					description=f"**Not Found:**\n{error}",
					color=0xff0000
				)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
		elif isinstance(error, CheckFailure):
			await ctx.message.delete()
			if luna.errorlog() == "console":
				luna.printerror(error)
			else:
				embed = discord.Embed(
					title="**Error**",
					description=f"{error}",
					color=0xff0000
				)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
		elif isinstance(error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			if luna.errorlog() == "console":
				luna.printerror(error)
			else:
				embed = discord.Embed(
					title="**Error**",
					description=f"**Missing arguments:**\n{error}",
					color=0xff0000
				)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
		elif isinstance(error, MissingPermissions):
			await ctx.message.delete()
			if luna.errorlog() == "console":
				luna.printerror(error)
			else:
				embed = discord.Embed(
					title="**Error**",
					description=f"**Missing permissions:**\n{error}",
					color=0xff0000
				)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
		elif "Cannot send an empty message" in error_str:
			if luna.errorlog() == "console":
				luna.printerror(error)
			else:
				embed = discord.Embed(
					title="**Error**",
					description=f"{error}",
					color=0xff0000
				)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
		else:
			pass

def setup(bot):
	bot.add_cog(OnCommandErrorCog(bot))
