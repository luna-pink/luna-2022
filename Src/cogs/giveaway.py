import discord
from discord.ext import commands
import json
import main as luna
import asyncio


class GiveawayCog(commands.Cog, name="Giveaway settings"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "giveawaysniper",
					usage="<on/off>",
					description = "Turn giveaway sniper on or off")
	async def giveawaysniper(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Giveaway sniper: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configgiveaway_sniper("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Giveaway sniper: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Giveaway sniper: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configgiveaway_sniper("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Giveaway sniper: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "delay",
					usage="<minutes>",
					description = "Giveaway joiner delay in minutes")
	async def delay(self, ctx, minute:int):
		await ctx.message.delete()

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Giveaway joiner delay: **{minute} minute/s**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

		luna.printmessage(f"Auto delete timer: {luna.bcolors.LIGHTMAGENTA}{minute} minute/s{luna.bcolors.RESET}")
		luna.configgiveaway_sniperdelay(f"{minute}")

	@commands.command(name = "giveawayserver",
					usage="<on/off>",
					description = "Turn giveaway server joiner on or off")
	async def giveawayserver(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Server joiner: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configgiveaway_sniperjoiner("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Server joiner: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Server joiner: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configgiveaway_sniperjoiner("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Server joiner: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

def setup(bot:commands.Bot):
	bot.add_cog(GiveawayCog(bot))