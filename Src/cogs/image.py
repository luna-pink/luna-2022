import discord
from discord.ext import commands
import main as luna
import asyncio
import requests
import json
import urllib


class ImageCog(commands.Cog, name="Image commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "nsfw",
					usage="",
					description = "NSFW commands")
	async def nsfw(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('NSFW commands')
		commands = cog.get_commands()
		helptext = ""

		if luna.mode() == 2:
			for command in commands:
				if len(command.usage) == 0:
					command.usage = command.usage+""
				else:
					command.usage = command.usage+" "
				helptext+=f"[ {prefix}{command.name} {command.usage}] {command.description}\n"
			await ctx.send(f"```ini\n[ NSFW commands ]\n\n{luna.descriptionvar()}{helptext}\n[ {luna.footervar()} ]```")
		else:
			for command in commands:
				helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
			embed = discord.Embed(title="NSFW commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	# ///////////////////////////////////////////////////////////////
	# Avatar commands

	@commands.command(name = "avatar",
					usage="<@member>",
					aliases=["av"],
					description = "Display someones avatar")
	async def av(self, ctx, user_id):
		await ctx.message.delete()
		if "<@!" and ">" in user_id:
			user_id = user_id.replace("<@!", "").replace(">", "")
			user = await self.bot.fetch_user(user_id)
		else:
			user = await self.bot.fetch_user(user_id)
		embed = discord.Embed(title=f"{user}'s avatar", color=luna.hexcolorvar())
		embed.set_image(url=user.avatar_url)
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		await luna.send(ctx, embed)

	@commands.command(name = "avatart",
					usage="<@member> <text>",
					asliases=["avt"],
					description = "Display someones avatar with a text")
	async def avatart(self, ctx, member: discord.Member, *, text: str):
		await ctx.message.delete()
		embed = discord.Embed(title=text,color=luna.hexcolorvar())
		embed.set_image(url=member.avatar_url)
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		await luna.send(ctx, embed)

	@commands.command(name = "searchav",
					usage="<@member>",
					description = "Returns a search link of someones avatar")
	async def searchav(self, ctx, member: discord.Member):
		await ctx.message.delete()
		embed = discord.Embed(title=f"Search link for {member}'s avatar",description=f"https://images.google.com/searchbyimage?image_url={member.avatar_url}" ,color=luna.hexcolorvar())
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		await luna.send(ctx, embed)

	@commands.command(name = "linkav",
					usage="<@member>",
					description = "Returns a link of someones avatar")
	async def linkav(self, ctx, member: discord.Member):
		await ctx.message.delete()
		embed = discord.Embed(title=f"Link for {member}'s avatar",description=f"{member.avatar_url}" ,color=luna.hexcolorvar())
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		await luna.send(ctx, embed)

	@commands.command(name = "stealav",
					usage="<@member>",
					description = "Steal someones avatar")
	async def stealav(self, ctx, member: discord.Member):
		await ctx.message.delete()
		url = member.avatar_url
		if luna.password() == "password-here":
			luna.printerror("You didnt put your password in the config.json file")
		else:
			luna.password()
			with open('data/images/PFP-1.png', 'wb') as f:
				r = requests.get(url, stream=True)
				for block in r.iter_content(1024):
					if not block:
						break
					f.write(block)
		try:
			with open('data/images/PFP-1.png', 'rb') as f:
				await self.bot.user.edit(password=luna.password(), avatar=f.read())
			embed = discord.Embed(description=f"**Stole {member}'s avatar!**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		except discord.HTTPException as e:
			luna.printerror(f"{e}")

	@commands.command(name = "setav",
					usage="<url>",
					description = "Set your avatar")
	async def setav(self, ctx, url: str):
		await ctx.message.delete()
		if luna.password() == "password-here":
			luna.printerror("You didnt put your password in the config.json file")
		else:
			luna.password()
			with open('data/images/PFP-1.png', 'wb') as f:
				r = requests.get(url, stream=True)
				for block in r.iter_content(1024):
					if not block:
						break
					f.write(block)
		try:
			with open('data/images/PFP-1.png', 'rb') as f:
				await self.bot.user.edit(password=luna.password(), avatar=f.read())
			embed = discord.Embed(description=f"**Set new avatar to:**\n{url}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		except discord.HTTPException as e:
			luna.printerror(f"{e}")

	@commands.command(name = "invisav",
					usage="",
					description = "Set your avatar to an invisible one")
	async def invisav(self, ctx):
		await ctx.message.delete()
		url = "https://gauginggadgets.com/wp-content/uploads/2020/07/InvisibleProfileImage.png"
		if luna.password() == "password-here":
			luna.printerror("You didnt put your password in the config.json file")
		else:
			luna.password()
			with open('data/images/PFP-1.png', 'wb') as f:
				r = requests.get(url, stream=True)
				for block in r.iter_content(1024):
					if not block:
						break
					f.write(block)
		try:
			with open('data/images/PFP-1.png', 'rb') as f:
				await self.bot.user.edit(password=luna.password(), avatar=f.read())
			embed = discord.Embed(description=f"**Set your avatar to invisible**" ,color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		except discord.HTTPException as e:
			luna.printerror(f"{e}")

	# ///////////////////////////////////////////////////////////////
	# Fun image commands
        
	@commands.command(name = "dog",
					usage="",
					description = "Send a random dog")
	async def dog(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://dog.ceo/api/breeds/image/random").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['message']))
		await luna.send(ctx, embed)

	@commands.command(name = "fox",
					usage="",
					description = "Send a random fox")
	async def fox(self, ctx):
		await ctx.message.delete()
		r = requests.get('https://randomfox.ca/floof/').json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['image']))
		await luna.send(ctx, embed)
			
	@commands.command(name = "cat",
					usage="",
					description = "Send a random cat")
	async def cat(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://api.thecatapi.com/v1/images/search").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r[0]["url"]))
		await luna.send(ctx, embed)


	@commands.command(name = "sadcat",
					usage="",
					description = "Send a random sad cat")
	async def sadcat(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://api.alexflipnote.dev/sadcat").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['file']))
		await luna.send(ctx, embed)

	@commands.command(name = "waifu",
					usage="",
					description = "Send a random waifu")
	async def waifu(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/waifu").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await luna.send(ctx, embed)

	# ///////////////////////////////////////////////////////////////
	# Image commands

	@commands.command(name = "wallpaper",
					usage="",
					description = "Send a random anime wallpaper")
	async def wallpaper(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/wallpaper").json()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await luna.send(ctx, embed)
	
	@commands.command(name = "wide",
					usage="<@member>",
					description = "Wide profile picture")
	async def wide(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/wide?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await luna.send(ctx, embed)

	@commands.command(name = "trumptweet",
					usage="<text>",
					description = "Create a trumptweet")
	async def trumptweet(self, ctx, *, text:str):
		await ctx.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=trumptweet&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=link)
		await luna.send(ctx, embed)

	@commands.command(name = "tweet",
					usage="<name> <text>",
					description = "Create a tweet")
	async def tweet(self, ctx, name, *, text:str):
		await ctx.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=tweet&username={name}&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=link)
		await luna.send(ctx, embed)

	@commands.command(name = "supreme",
					usage="<text>",
					description = "Custom supreme logo")
	async def supreme(self, ctx, *, text:str):
		await ctx.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=supreme&text={str(urllib.parse.quote(text))}').json()['url']
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f'{request}')
		await luna.send(ctx, embed)

	@commands.command(name = "changemymind",
					usage="<text>",
					description = "Changemymind meme")
	async def changemymind(self, ctx, *, text:str):
		await ctx.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=changemymind&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=link)
		await luna.send(ctx, embed)

	@commands.command(name = "phcomment",
					aliases=['pornhubcomment'],
					usage="<@member> <text>",
					description = "Pornhub comment")
	async def phcomment(self, ctx, user: discord.User, *, text: str):
		await ctx.message.delete()
		image_url = str(user.avatar_url).replace(".webp", ".png")
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=phcomment&image={image_url}&username={urllib.parse.quote(user.name)}&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=link)
		await luna.send(ctx, embed)

	@commands.command(name = "clyde",
					usage="<text>",
					description = "Custom Clyde message")
	async def clyde(self, ctx, *, text:str):
		await ctx.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=clyde&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=link)
		await luna.send(ctx, embed)

	@commands.command(name = "stonks",
					usage="<@member>",
					description = "Stonks!")
	async def stonks(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/stonks?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await luna.send(ctx, embed)

	@commands.command(name = "notstonks",
					usage="<@member>",
					description = "Notstonks!")
	async def notstonks(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/stonks?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}&notstonks=true")
		await luna.send(ctx, embed)

	@commands.command(name = "emergencymeeting",
					usage="<text>",
					description = "Emergency meeting!")
	async def emergencymeeting(self, ctx, *, text):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/emergencymeeting?text={urllib.parse.quote(text)}")
		await luna.send(ctx, embed)

	@commands.command(name = "eject",
					usage="<true/false> <color> <@member>",
					description = "Among Us eject")
	async def eject(self, ctx, impostor: bool, crewmate: str, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/ejected?name={urllib.parse.quote(user.name)}&impostor={impostor}&crewmate={crewmate}")
		await luna.send(ctx, embed)

	@commands.command(name = "drip",
					usage="<@member>",
					description = "Drip meme")
	async def drip(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/drip?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await luna.send(ctx, embed)

	@commands.command(name = "distractedbf",
					usage="<@boyfriend> <@woman> <@girlfriend>",
					description = "Distracted boyfriend meme")
	async def distractedbf(self, ctx, boyfriend: discord.User, woman: discord.User, girlfriend: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/distractedbf?boyfriend={urllib.parse.quote(str(boyfriend.avatar_url).replace('webp', 'png'))}&woman={urllib.parse.quote(str(woman.avatar_url).replace('webp', 'png'))}&girlfriend={urllib.parse.quote(str(girlfriend.avatar_url).replace('webp', 'png'))}")
		await luna.send(ctx, embed)

	@commands.command(name = "icanmilkyou",
					usage="<@member1> <@member2>",
					description = "I can milk you")
	async def icanmilkyou(self, ctx, user1: discord.User, user2: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/icanmilkyou?user1={urllib.parse.quote(str(user1.avatar_url).replace('webp', 'png'))}&user2={urllib.parse.quote(str(user2.avatar_url).replace('webp', 'png'))}")
		await luna.send(ctx, embed)

	@commands.command(name = "heaven",
					usage="<@member>",
					description = "Heaven meme")
	async def heaven(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/heaven?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await luna.send(ctx, embed)

	@commands.command(name = "dockofshame",
					usage="<@member>",
					description = "Heaven meme")
	async def dockofshame(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/dockofshame?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await luna.send(ctx, embed)

	@commands.command(name = "firsttime",
					usage="<@member>",
					description = "First time? meme")
	async def dockofshame(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/firsttime?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await luna.send(ctx, embed)

	@commands.command(name = "drake",
					usage="<no, yes>",
					description = "Drake yes and no meme")
	async def drake(self, ctx, *, text:str):
		await ctx.message.delete()
		text = text.split(', ')
		text1 = text[0]
		text2 = text[1]
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=f'https://api.popcatdev.repl.co/drake?text1={str(urllib.parse.quote(text1))}&text2={str(urllib.parse.quote(text2))}')
		await luna.send(ctx, embed)

	

def setup(bot:commands.Bot):
	bot.add_cog(ImageCog(bot))