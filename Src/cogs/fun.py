import discord
from discord.ext import commands
import main as luna
import random
import requests
import aiohttp
import asyncio

class FunCog(commands.Cog, name="Fun commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "impersonate",
					usage="<@member> <message>",
					description = "Make them send your message")
	async def impersonate(self, ctx, user: discord.User, *, message: str):
		await ctx.message.delete()
		webhook = await ctx.channel.create_webhook(name=user.name)
		await webhook.send(message, username=user.name, avatar_url=user.avatar_url)
		await webhook.delete()

	@commands.command(name = "shoot",
					usage="<@member>",
					description = "Shoot up someone")
	async def shoot(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Who do you want to shoot up? Please mention someone.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			embed = discord.Embed(description=f"{user.mention} got shot up!", color=luna.hexcolorvar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url="https://media1.tenor.com/images/cfb7817a23645120d4baba2dcb9205e0/tenor.gif")
			await ctx.send(embed=embed)

	@commands.command(name = "feed",
					usage="<@member>",
					description = "Feed someone")
	async def feed(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Who do you want to feed? Please mention someone.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/feed").json()
			embed = discord.Embed(description=f"{ctx.author.mention} feeds {user.mention}", color=luna.hexcolorvar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=str(r['url']))
			await ctx.send(embed=embed)

	@commands.command(name = "kiss",
					usage="<@member>",
					description = "Kiss someone")
	async def kiss(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Who do you want to kiss? Please mention someone.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/kiss").json()
			embed = discord.Embed(description=f"{ctx.author.mention} kisses {user.mention}", color=luna.hexcolorvar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=str(r['url']))
			await ctx.send(embed=embed)

	@commands.command(name = "hug",
					usage="<@member>",
					description = "Hug someone")
	async def hug(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Who do you want to hug? Please mention someone.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/hug").json()
			embed = discord.Embed(description=f"{ctx.author.mention} hugs {user.mention}", color=luna.hexcolorvar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=str(r['url']))
			await ctx.send(embed=embed)

	@commands.command(name = "pat",
					usage="<@member>",
					description = "Pat someone")
	async def pat(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Who do you want to pat? Please mention someone.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/pat").json()
			embed = discord.Embed(description=f"{ctx.author.mention} pats {user.mention}", color=luna.hexcolorvar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=str(r['url']))

	@commands.command(name = "slap",
					usage="<@member>",
					description = "Slap someone")
	async def slap(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Who do you want to slap? Please mention someone.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/slap").json()
			embed = discord.Embed(description=f"{ctx.author.mention} slaps {user.mention}", color=luna.hexcolorvar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=str(r['url']))

	@commands.command(name = "tickle",
					usage="<@member>",
					description = "Tickle someone")
	async def tickle(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Who do you want to tickle? Please mention someone.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/tickle").json()
			embed = discord.Embed(description=f"{ctx.author.mention} tickles {user.mention}", color=luna.hexcolorvar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=str(r['url']))

	@commands.command(name = "fml",
					usage="",
					description = "Fuck my life situation")
	async def fml(self, ctx):
		await ctx.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=fml')
		data = request.json()
		text = data['text']
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f'{text}', color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)
        
	@commands.command(name = "gay",
					usage="<@member>",
					description = "Gay rate somebody")
	async def gay(self, ctx, user: discord.Member = None):
		await ctx.message.delete()

		if user is None:
			user = ctx.author
		size = random.randint(1, 100)
		embed = discord.Embed(title=f"{user}'s Gay Rate", description=f"{size}% Gay 🏳️‍🌈", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "coronatest",
					usage="<@member>",
					description = "Test somebody for Corona")
	async def coronatest(self, ctx, user: discord.Member = None):
		await ctx.message.delete()

		if user is None:
			member = ctx.author
		else:
			member = user
		random.seed((member.id * 6) / 2)
		percent = random.randint(0, 100)
		embed = discord.Embed(title=f"{user}'s Corona Test", description=f'{percent}% positive!\n\nResult: Overall: {"**Positive**" if (percent > 50) else "**Negative**"}', color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "8ball",
					usage="<question>",
					description = "Ask 8 Ball!")
	async def _8ball(self, ctx, *, question:str):
		await ctx.message.delete()
		responses = [
			'That is a resounding no',
			'It is not looking likely',
			'Too hard to tell',
			'It is quite possible',
			'That is a definite yes!',
			'Maybe',
			'There is a good chance'
		]
		answer = random.choice(responses)
		embed = discord.Embed(title="8 Ball", description=f"Question: {question}\n\nAnswer: {answer}", color=luna.hexcolorvar())
		embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "slot",
					usage="",
					aliases=['slots'],
					description = "Play slots")
	async def slot(self, ctx):
		await ctx.message.delete()
		emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
		a = random.choice(emojis)
		b = random.choice(emojis)
		c = random.choice(emojis)
		slotmachine = f"**------------------\n| {a} | {b} | {c} |\n------------------\n\n{ctx.author.name}**,"
		if (a == b == c):
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} All matchings, you won!", color=luna.hexcolorvar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			await luna.send(ctx, embed)
		elif (a == b) or (a == c) or (b == c):
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} 2 in a row, you won!", color=luna.hexcolorvar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} No match, you lost!", color=luna.hexcolorvar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			await luna.send(ctx, embed)

	@commands.command(name = "dadjoke",
					usage="",
					description = "Dad jokes")
	async def dadjoke(self, ctx):
		await ctx.message.delete()
		request = requests.get(f'https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
		data = request.json()
		joke = data['joke']
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f'{joke}', color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "joke",
					usage="",
					description = "Random jokes")
	async def dadjoke(self, ctx):
		await ctx.message.delete()
		request = requests.get(f'http://www.official-joke-api.appspot.com/random_joke')
		data = request.json()
		setup = data['setup']
		punchline = data['punchline']
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f'{setup}\n\n||{punchline}||', color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "coinflip",
					usage="",
					description = "Flip a coin")
	async def coinflip(self, ctx):
		await ctx.message.delete()
		lista = ['head', 'tails']
		coin = random.choice(lista)
		try:
			if coin == 'head':
				embed = discord.Embed(title="Head", color=luna.hexcolorvar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_thumbnail(url="https://webstockreview.net/images/coin-clipart-dime-6.png")
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				await luna.send(ctx, embed)
			else:
				embed = discord.Embed(title="Tails", color=luna.hexcolorvar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				await luna.send(ctx, embed)
		except discord.HTTPException:
			if coin == 'head':
				await ctx.send("Coinflip: **Head**")
			else:
				await ctx.send("Coinflip: **Tails**")

	@commands.command(name = "farmer",
						usage="",
						description = "Dank Memer farmer.")
	async def farmer(self, ctx):
		await ctx.message.delete()
		global farming
		farming = True
		while farming:
			await ctx.send("pls beg")
			await asyncio.sleep(3)
			await ctx.send("pls deposit all")
			await asyncio.sleep(42)

	@commands.command(name = "afarmer",
						usage="",
						description = "Advanced Dank Memer farmer.")
	async def afarmer(self, ctx):
		await ctx.message.delete()
		global farming
		farming = True
		while farming:
			await ctx.send("pls beg")
			await asyncio.sleep(3)
			await ctx.send("pls deposit all")
			await asyncio.sleep(3)
			await ctx.send("pls postmeme")
			await asyncio.sleep(3)
			await ctx.send("n")
			await asyncio.sleep(3)
			await ctx.send("pls fish")
			await asyncio.sleep(33)


	@commands.command(name = "stopfarmer",
						usage="",
						description = "Stops the nickname animation")
	async def stopfarmer(self, ctx):
		await ctx.message.delete()
		global farming
		farming = False

def setup(bot:commands.Bot):
	bot.add_cog(FunCog(bot))