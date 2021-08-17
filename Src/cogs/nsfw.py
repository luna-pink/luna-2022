import discord
from discord.ext import commands
import main as luna
import requests


class NSFWCog(commands.Cog, name="NSFW commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	# ///////////////////////////////////////////////////////////////
	# NSFW commands

	@commands.command(name = "lewdneko",
					usage="",
					description = "Send a random lewdneko image")
	async def lewdneko(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "hentai",
					usage="",
					description = "Send a random hentai image")
	async def hentai(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "hentaiass",
					usage="",
					description = "Send a random hentai ass")
	async def hentaiass(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekobot.xyz/api/image?type=hass").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['message']))
		await ctx.send(embed=embed)

	@commands.command(name = "boobs",
					usage="",
					description = "Send a random image of boobs")
	async def boobs(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/boobs").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "tits",
					usage="",
					description = "Send a random image of tits")
	async def tits(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/tits").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)
        
	@commands.command(name = "anal",
					usage="",
					description = "Send a random anal image")
	async def anal(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/anal").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "cumslut",
					usage="",
					description = "Send a random image of a cumslut")
	async def cumslut(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/cum").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "blowjob",
					usage="",
					description = "Send a random blowjob image")
	async def blowjob(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/blowjob").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "lesbian",
					usage="",
					description = "Send a random lesbian image")
	async def lesbian(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/les").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "yaoi",
					usage="",
					description = "Send a random image of yaoi")
	async def yaoi(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekobot.xyz/api/image?type=yaoi").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['message']))
		await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(NSFWCog(bot))