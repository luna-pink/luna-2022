import discord
from discord.ext import commands
import os
import main as luna
import asyncio


class ThemeCog(commands.Cog, name="Theme command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "theme",
					usage="<theme>",
					description = "Change theme")
	async def theme(self, ctx, theme:str):
		await ctx.message.delete()

		if os.path.exists(f"data/themes/{theme}" + ".json"):

			luna.printmessage(f"Changed theme to: {luna.bcolors.LIGHTMAGENTA}{theme}{luna.bcolors.RESET}")
			luna.configtheme(f"{theme}")
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed theme to: **{theme}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			if luna.errorlog() == "console":
				luna.printerror(f"There is no theme called: {luna.bcolors.LIGHTMAGENTA}{theme}{luna.bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"There is no theme called: **{theme}**", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

def setup(bot:commands.Bot):
	bot.add_cog(ThemeCog(bot))