import discord
from discord.ext import commands
import main as luna
import asyncio
import json
import requests

class CryptoCog(commands.Cog, name="Cryptocurrency commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "btc",
					usage="",
					description = "Show the current prizes of Bitcoin")
	async def btc(self, ctx):
		await ctx.message.delete()
		request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP,CHF,CAD,AUD,RUB,JPY,CNY,INR,TRY,PLN')
		data = request.json()
		usd = data['USD']
		eur = data['EUR']
		gbp = data['GBP']
		chf = data['CHF']
		cad = data['CAD']
		aud = data['AUD']
		rub = data['RUB']
		jpy = data['JPY']
		cny = data['CNY']
		inr = data['INR']
		pln = data['PLN']
		__try = data['TRY']
		embed = discord.Embed(title="BTC (Bitcoin)", color=luna.hexcolorvar())
		embed.description = f"""USD: `{usd}`
EUR: `{eur}`
GBP: `{gbp}`
CHF: `{chf}`
CAD: `{cad}`
AUD: `{aud}`
RUB: `{rub}`
JPY: `{jpy}`
CNY: `{cny}`
INR: `{inr}`
TRY: `{__try}`
PLN: `{pln}`"""
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "eth",
					usage="",
					description = "Show the current prizes of Ethereum")
	async def eth(self, ctx):
		await ctx.message.delete()
		request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP,CHF,CAD,AUD,RUB,JPY,CNY,INR,TRY,PLN')
		data = request.json()
		usd = data['USD']
		eur = data['EUR']
		gbp = data['GBP']
		chf = data['CHF']
		cad = data['CAD']
		aud = data['AUD']
		rub = data['RUB']
		jpy = data['JPY']
		cny = data['CNY']
		inr = data['INR']
		pln = data['PLN']
		__try = data['TRY']
		embed = discord.Embed(title="ETH (Ethereum)", color=luna.hexcolorvar())
		embed.description = f"""USD: `{usd}`
EUR: `{eur}`
GBP: `{gbp}`
CHF: `{chf}`
CAD: `{cad}`
AUD: `{aud}`
RUB: `{rub}`
JPY: `{jpy}`
CNY: `{cny}`
INR: `{inr}`
TRY: `{__try}`
PLN: `{pln}`"""
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "doge",
					usage="",
					description = "Show the current prizes of Dogecoin")
	async def doge(self, ctx):
		await ctx.message.delete()
		request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR,GBP,CHF,CAD,AUD,RUB,JPY,CNY,INR,TRY,PLN')
		data = request.json()
		usd = data['USD']
		eur = data['EUR']
		gbp = data['GBP']
		chf = data['CHF']
		cad = data['CAD']
		aud = data['AUD']
		rub = data['RUB']
		jpy = data['JPY']
		cny = data['CNY']
		inr = data['INR']
		pln = data['PLN']
		__try = data['TRY']
		embed = discord.Embed(title="DOGE (Dogecoin)", color=luna.hexcolorvar())
		embed.description = f"""USD: `{usd}`
EUR: `{eur}`
GBP: `{gbp}`
CHF: `{chf}`
CAD: `{cad}`
AUD: `{aud}`
RUB: `{rub}`
JPY: `{jpy}`
CNY: `{cny}`
INR: `{inr}`
TRY: `{__try}`
PLN: `{pln}`"""
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	

def setup(bot:commands.Bot):
	bot.add_cog(CryptoCog(bot))