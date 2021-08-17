import discord
from discord.ext import commands
import os
import main as luna
import asyncio
import json


class ThemesCog(commands.Cog, name="Theme commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "newtheme",
					usage="<name>",
					description = "Create a theme")
	async def newtheme(self, ctx, themename:str):
		await ctx.message.delete()

		if os.path.exists(f"data/themes/{themename}.json"):
			if luna.errorlog() == "console":
				luna.printerror(f"A theme already exists with the name: {luna.bcolors.LIGHTMAGENTA}{themename}{luna.bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"A theme already exists with the name: **{themename}**", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
		else:
			luna.printmessage(f"Created theme: {luna.bcolors.LIGHTMAGENTA}{themename}{luna.bcolors.RESET}")
			data = {
				"title": "Lolicon",
				"titleurl": "",
				"footer": "Lolicon",
				"footer_iconurl": "https://cdn.discordapp.com/attachments/848299943172505611/868676317174980608/LoliconRe.png",
				"imageurl": "https://cdn.discordapp.com/attachments/848299943172505611/868676317174980608/LoliconRe.png",
				"large_imageurl": "",
				"hexcolor": "#bd93f9",
				"author": "",
				"author_iconurl": "",
				"authorurl": "",
				"description": True
			}
			with open(f"data/themes/{themename}.json", "w") as studs:
				json.dump(data, studs, indent=4)
			luna.configtheme(f"{themename}")
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Created theme: **{themename}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "edittheme",
					usage="<newname>",
					description = "Edit current theme name")
	async def edittheme(self, ctx, themename:str):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')

		if os.path.exists(f"data/themes/{themename}.json"):
			if luna.errorlog() == "console":
				luna.printerror(f"A theme already exists with the name: {luna.bcolors.LIGHTMAGENTA}{themename}{luna.bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"A theme already exists with the name: **{themename}**", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
		else:
			luna.printmessage(f"Edited theme name to: {luna.bcolors.LIGHTMAGENTA}{themename}{luna.bcolors.RESET}")
			os.rename(f"data/themes/{themesvar}",f"data/themes/{themename}.json")
			luna.configtheme(f"{themename}")
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Edited theme name to: **{themename}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
        
	@commands.command(name = "deltheme",
					usage="<name>",
					description = "Delete a theme")
	async def deltheme(self, ctx, themename:str):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')

		if themesvar == f"{themename}.json":
			if luna.errorlog() == "console":
				luna.printerror(f"You cant delete the theme you are currently using.")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"There is no theme called: **{themename}**", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
			return

		if os.path.exists(f"data/themes/{themename}" + ".json"):
			os.remove(f"data/themes/{themename}" + ".json")
			luna.printmessage(f"Deleted theme: {luna.bcolors.LIGHTMAGENTA}{themename}{luna.bcolors.RESET}")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Deleted theme: **{themename}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			if luna.errorlog() == "console":
				luna.printerror(f"There is no theme called: {luna.bcolors.LIGHTMAGENTA}{themename}{luna.bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"There is no theme called: **{themename}**", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = "sendtheme",
					usage="",
					description = "Send the current theme file")
	async def sendtheme(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')

		await ctx.send(file=discord.File(f"data/themes/{themesvar}"))

	@commands.command(name = "communitythemes",
					usage="",
					description = "Show themes made by the community")
	async def communitythemes(self, ctx):
		await ctx.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Community Themes", url=luna.titleurlvar(), description=f"{luna.descriptionvar()}**{prefix}preview <theme>** » Preview a theme\n\n**{prefix}install chill** » Chill theme by $Exodus\n**{prefix}install midnight** » Midnight theme by Rainy\n**{prefix}install vaporwave** » Vaporwave theme by Rainy\n**{prefix}install sweetrevenge** » Sweetrevenge theme by Rainy\n**{prefix}install error** » Error theme by $Exodus", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

def setup(bot:commands.Bot):
	bot.add_cog(ThemesCog(bot))