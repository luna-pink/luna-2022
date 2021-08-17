import discord
from discord.ext import commands
import main as luna
import random
import re
import requests


class CustomizeCog(commands.Cog, name="Customization commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "ctitle",
					usage="<title>",
					description = "Customize the title")
	async def ctitle(self, ctx, *, newtitle:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed title to: {luna.bcolors.LIGHTMAGENTA}{newtitle}{luna.bcolors.RESET}")
		if newtitle == "None":
			luna.configselfbottitle("")
		else:
			luna.configselfbottitle(f"{newtitle}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed title to: **{newtitle}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "ctitleurl",
					usage="<url>",
					description = "Customize the title url")
	async def ctitleurl(self, ctx, newtitleurl:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed title url to: {luna.bcolors.LIGHTMAGENTA}{newtitleurl}{luna.bcolors.RESET}")
		if newtitleurl == "None":
			luna.configselfbottitleurl("")
		else:
			luna.configselfbottitleurl(f"{newtitleurl}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed title url to: **{newtitleurl}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "cfooter",
					usage="<footer>",
					description = "Customize the footer")
	async def cfooter(self, ctx, *, newfooter:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed footer to: {luna.bcolors.LIGHTMAGENTA}{newfooter}{luna.bcolors.RESET}")
		if newfooter == "None":
			luna.configselfbotfooter("")
		else:
			luna.configselfbotfooter(f"{newfooter}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed footer to: **{newfooter}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "cfootericon",
					usage="<url>",
					description = "Customize the footer icon")
	async def cfootericon(self, ctx, newfootericonurl:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed footer icon url to: {luna.bcolors.LIGHTMAGENTA}{newfootericonurl}{luna.bcolors.RESET}")
		if newfootericonurl == "None":
			luna.configselfbotfooter_iconurl("")
		else:
			luna.configselfbotfooter_iconurl(f"{newfootericonurl}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed footer icon url to: **{newfootericonurl}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "cimage",
					usage="<url>",
					description = "Customize the thumbnail image")
	async def cimageurl(self, ctx, newimageurl:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed thumbnail url to: {luna.bcolors.LIGHTMAGENTA}{newimageurl}{luna.bcolors.RESET}")
		if newimageurl == "None":
			luna.configselfbotimageurl("")
		else:
			luna.configselfbotimageurl(f"{newimageurl}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed thumbnail url to: **{newimageurl}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "clargeimage",
					usage="<url>",
					description = "Customize the large image")
	async def clargeimage(self, ctx, newimageurl:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed image url to: {luna.bcolors.LIGHTMAGENTA}{newimageurl}{luna.bcolors.RESET}")
		if newimageurl == "None":
			luna.configselfbotlarge_imageurl("")
		else:
			luna.configselfbotlarge_imageurl(f"{newimageurl}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed image url to: **{newimageurl}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "chexcolor",
					usage="<#hexcolor>",
					description = "Customize the hexadecimal color")
	async def chexcolor(self, ctx, newhexcolor:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed hexcolor to: {luna.bcolors.LIGHTMAGENTA}{newhexcolor}{luna.bcolors.RESET}")
		if newhexcolor == "None":
			luna.configselfbothexcolor("")
		else:
			luna.configselfbothexcolor(f"{newhexcolor}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed hexcolor to: **{newhexcolor}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "cauthor",
					usage="<text>",
					description = "Customize the author text")
	async def cauthor(self, ctx, *, newauthor:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed author to: {luna.bcolors.LIGHTMAGENTA}{newauthor}{luna.bcolors.RESET}")
		if newauthor == "None":
			luna.configselfbotauthor("")
		else:
			luna.configselfbotauthor(f"{newauthor}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed author to: **{newauthor}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "cauthoricon",
					usage="<url>",
					description = "Customize the author icon")
	async def cauthoricon(self, ctx, newauthoriconurl:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed author icon url to: {luna.bcolors.LIGHTMAGENTA}{newauthoriconurl}{luna.bcolors.RESET}")
		if newauthoriconurl == "None":
			luna.configselfbotauthor_iconurl("")
		else:
			luna.configselfbotauthor_iconurl(f"{newauthoriconurl}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed author icon url to: **{newauthoriconurl}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "cauthorurl",
					usage="<url>",
					description = "Customize the author url")
	async def cauthorurl(self, ctx, newauthorurl:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed author url to: {luna.bcolors.LIGHTMAGENTA}{newauthorurl}{luna.bcolors.RESET}")
		if newauthorurl == "None":
			luna.configselfbotauthorurl("")
		else:
			luna.configselfbotauthorurl(f"{newauthorurl}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed author url to: **{newauthorurl}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "cdescription",
					usage="<on/off>",
					description = "Hide/Show <> = required, [] = optional")
	async def cdescription(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Changed description to: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configselfbotdescription(True)

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed description to: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Changed description to: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configselfbotdescription(False)

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed description to: **off**", color=luna.hexcolorvar())
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

	@commands.command(name = "color",
					usage="<hexcode>",
					description = "Color information")
	async def color(self, ctx, hexcode:str):
		await ctx.message.delete()
		if hexcode == "random":
			hexcode = "%06x" % random.randint(0, 0xFFFFFF)
		if hexcode[:1] == "#":
			hexcode = hexcode[1:]
		if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', hexcode):
			return
		r = requests.get(f"https://react.flawcra.cc/api/generation.php?type=color&color={hexcode}").json()
		embed = discord.Embed(title=f'{r["name"]}', description=f"**HEX:** {r['hex']}\n**RGB:** {r['rgb']}\n**INT:** {r['int']}\n**Brightness:** {r['brightness']}",color=r["int"])
		embed.set_thumbnail(url=r["image"])
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		await luna.send(ctx, embed)

def setup(bot:commands.Bot):
	bot.add_cog(CustomizeCog(bot))