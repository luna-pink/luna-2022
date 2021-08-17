import discord
from discord.ext import commands
import json
import main as luna
import asyncio


class ToastCog(commands.Cog, name="Toast customization"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "toasticon",
					usage="<icon.ico>",
					description = "Customize the toast icon (has to be an .ico)")
	async def toasticon(self, ctx, *, newicon:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed toast icon to: {luna.bcolors.LIGHTMAGENTA}{newicon}{luna.bcolors.RESET}")
		if newicon.endswith(".ico"):
			luna.configtoasticon(f"{newicon}")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed toast title to: **{newicon}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Not a valid icon file, (.ico)", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
        
	@commands.command(name = "toasttitle",
					usage="<title>",
					description = "Customize the toast title")
	async def toasttitle(self, ctx, *, newtitle:str):
		await ctx.message.delete()

		luna.printmessage(f"Changed toast title to: {luna.bcolors.LIGHTMAGENTA}{newtitle}{luna.bcolors.RESET}")
		if newtitle == "None":
			luna.configtoasttitle("")
		else:
			luna.configtoasttitle(f"{newtitle}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed toast title to: **{newtitle}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)
def setup(bot:commands.Bot):
	bot.add_cog(ToastCog(bot))