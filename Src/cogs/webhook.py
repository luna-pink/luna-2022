import discord
from discord.ext import commands
import json
import main as luna
import asyncio


class WebhookCog(commands.Cog, name="Webhook commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "wtitle",
					usage="<title>",
					description = "Customize the webhook title")
	async def wtitle(self, ctx, *, newtitle:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed webhook title to: {luna.bcolors.LIGHTMAGENTA}{newtitle}{luna.bcolors.RESET}")
		if newtitle == "None":
			luna.configwebhooktitle("")
		else:
			luna.configwebhooktitle(f"{newtitle}")

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nChanged webhook title to: {newtitle}\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed webhook title to: **{newtitle}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

	@commands.command(name = "wfooter",
					usage="<footer>",
					description = "Customize the webhook footer")
	async def wfooter(self, ctx, *, newfooter:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed webhook footer to: {luna.bcolors.LIGHTMAGENTA}{newfooter}{luna.bcolors.RESET}")
		if newfooter == "None":
			luna.configwebhookfooter("")
		else:
			luna.configwebhookfooter(f"{newfooter}")

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nChanged webhook footer to: {newfooter}\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed webhook footer to: **{newfooter}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

	@commands.command(name = "wimage",
					usage="<url>",
					description = "Customize the thumbnail image")
	async def wimage(self, ctx, newimageurl:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed webhook thumbnail url to: {luna.bcolors.LIGHTMAGENTA}{newimageurl}{luna.bcolors.RESET}")
		if newimageurl == "None":
			luna.configwebhookimage("")
		else:
			luna.configwebhookimage(f"{newimageurl}")

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nChanged webhook thumbnail url to: {newimageurl}\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed webhook thumbnail url to: **{newimageurl}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

	@commands.command(name = "whexcolor",
					usage="<#hexcolor>",
					description = "Customize the webhook hexadecimal color")
	async def whexcolor(self, ctx, newhexcolor:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed webhook hexcolor to: {luna.bcolors.LIGHTMAGENTA}{newhexcolor}{luna.bcolors.RESET}")
		if newhexcolor == "None":
			luna.configwebhookhexcolor("")
		else:
			luna.configwebhookhexcolor(f"{newhexcolor}")

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nChanged webhook hexcolor to: {newhexcolor}\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed webhook hexcolor to: **{newhexcolor}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

	@commands.command(name = "wmatch",
					usage="",
					description = "Match webhook with current theme")
	async def wmatch(self, ctx):
		await ctx.message.delete()

		with open('./config.json') as f:
			config = json.load(f)
		themesvar = config.get('theme')
		with open(f"data/themes/{themesvar}") as f:
			theme = json.load(f)
		title = theme.get('title')
		footer = theme.get('footer')
		imageurl = theme.get('imageurl')
		hexcolor = theme.get('hexcolor')

		luna.printmessage(f"Matched webhook to: {luna.bcolors.LIGHTMAGENTA}{themesvar[:-5]}{luna.bcolors.RESET}")
		luna.configwebhooktitle(f"{title}")
		luna.configwebhookfooter(f"{footer}")
		luna.configwebhookimage(f"{imageurl}")
		luna.configwebhookhexcolor(f"{hexcolor}")

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nMatched webhook to: {themesvar[:-5]}\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Matched webhook to: **{themesvar[:-5]}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

def setup(bot:commands.Bot):
	bot.add_cog(WebhookCog(bot))