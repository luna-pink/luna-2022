import discord
from discord.ext import commands
import json
import main as luna
import asyncio


class SniperCog(commands.Cog, name="Sniper settings"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "nitrosniper",
					usage="<on/off>",
					description = "Turn nitro sniper on or off")
	async def nitrosniper(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Nitro sniper: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.confignitro_sniper("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Nitro sniper: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Nitro sniper: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.confignitro_sniper("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Nitro sniper: **off**", color=luna.hexcolorvar())
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

	@commands.command(name = "nitroapi",
					usage="<canary/v6/v7/v8/v9>",
					description = "Configurate nitro sniper api")
	async def sniperapi(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "canary" or mode == "v6" or mode == "v7" or mode == "v8" or mode == "v9":
			luna.printmessage(f"Nitro sniper api: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.confignitro_sniperapi(f"{mode}")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Nitro sniper api: **{mode}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			print("1")
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **canary**, **v6**, **v7**, **v8** or **v9**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

def setup(bot:commands.Bot):
	bot.add_cog(SniperCog(bot))