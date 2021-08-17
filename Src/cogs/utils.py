import discord
from discord import emoji
from discord.ext import commands
import requests
import main as luna
import asyncio
import random
import string
import aiohttp
from discord.ext.commands import has_permissions
import typing
import json
import os
import httpx

def file_exist(file_name):
    return os.path.exists(file_name)

class UtilsCog(commands.Cog, name="Util commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "serverjoiner",
					aliases=['joinservers', 'jservers', 'joinserver', 'joininvites'],
					usage="",
					description = "Join all invites in data/invites.txt")
	async def serverjoiner(self, ctx):
		await ctx.message.delete()
		if luna.riskmode() == "on":

			if file_exist('./data/invites.txt'):
				pass
			else:
				file = open("data/invites.txt", "w") 
				file.write("Put the invites of the servers you want to join here one after another") 
				file.close()
				embed = discord.Embed(title="Server Joiner", url=luna.titleurlvar(), description=f"No invites.txt has been found, so it has been created.\nPut all your invites there that you want to join.", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
				return

			if os.stat("data/invites.txt").st_size == 0:
				embed = discord.Embed(title="Server Joiner", url=luna.titleurlvar(), description=f"invites.txt is empty...", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
				return
			else:
				file = open("data/invites.txt", "r")
				nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
				line_count = len(nonempty_lines)
				file.close()

				with open('./config.json') as f:
					config = json.load(f)
				token = config.get('token')

				embed = discord.Embed(title="Server Joiner", url=luna.titleurlvar(), description=f"Found **{line_count}** invites in invites.txt\nJoining provided invites...", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

				with open("data/invites.txt","r+") as f:
					for line in f:
						invite = line.strip("\n")
						invite = invite.replace('https://discord.gg/', '')
						try:
							async with httpx.AsyncClient() as client:
								await client.post(f'https://canary.discord.com/api/v8/invites/{invite}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
								luna.printevent(f"Joined {invite}")
								await asyncio.sleep(0.5)
						except Exception:
							luna.printerror(f"Failed to join {invite}")
							pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "proxyserverjoiner",
					usage="",
					description = "Join all invites in data/invites.txt using proxies")
	async def proxyserverjoiner(self, ctx):
		await ctx.message.delete()
		if luna.riskmode() == "on":

			if file_exist('./data/invites.txt'):
				pass
			else:
				file = open("data/invites.txt", "w") 
				file.write("Put the invites of the servers you want to join here one after another") 
				file.close()
				embed = discord.Embed(title="Server Joiner [PROXY]", url=luna.titleurlvar(), description=f"No invites.txt has been found, so it has been created.\nPut all your invites there that you want to join.", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
				return

			if os.stat("data/invites.txt").st_size == 0:
				embed = discord.Embed(title="Server Joiner [PROXY]", url=luna.titleurlvar(), description=f"invites.txt is empty...", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
				return
			else:
				file = open("data/invites.txt", "r")
				nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
				line_count = len(nonempty_lines)
				file.close()

				with open('./config.json') as f:
					config = json.load(f)
				token = config.get('token')

				proxies = open('data/proxies.txt', 'r')
			
				proxylist = []
				
				for p, _proxy in enumerate(proxies):
					proxy = _proxy.split('\n')[0]
					proxylist.append(proxy)

				embed = discord.Embed(title="Server Joiner [PROXY]", url=luna.titleurlvar(), description=f"Found **{line_count}** invites in invites.txt\nJoining provided invites...", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

				with open("data/invites.txt","r+") as f:
					for line in f:
						invite = line.strip("\n")
						invite = invite.replace('https://discord.gg/', '')
						try:
							async with httpx.AsyncClient() as client:
								await client.post(f'https://canary.discord.com/api/v8/invites/{invite}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}, proxies={'http': f'{proxylist[p]}'})
								luna.printevent(f"[PROXY] Joined {invite}")
								await asyncio.sleep(0.5)
						except Exception:
							luna.printerror(f"[PROXY] Failed to join {invite}")
							pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "addemoji",
					usage="<emoji_name> <image_url>",
					description = "Add an emoji")
	@has_permissions(manage_emojis=True)
	async def addemoji(self, ctx, emoji_name, image_url=None):
		await ctx.message.delete()
		if ctx.message.attachments:
			image = await ctx.message.attachments[0].read()
		elif image_url:
			async with aiohttp.ClientSession() as session:
				async with session.get(image_url) as resp:
					image = await resp.read()
		await ctx.guild.create_custom_emoji(name=emoji_name, image=image)
		embed = discord.Embed(title="Emoji Added", url=luna.titleurlvar(), description=f"{emoji_name}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=image_url)
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "editemoji",
					usage="<emoji> <new_name>",
					description = "Edit an emoji")
	@has_permissions(manage_emojis=True)
	async def editemoji(self, ctx, emoji: discord.Emoji, new_name):
		await ctx.message.delete()
		oldname = emoji.name
		await emoji.edit(name=new_name)
		embed = discord.Embed(title="Emoji Edited", url=luna.titleurlvar(), description=f"{oldname} to {new_name}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=emoji.url)
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "delemoji",
					usage="<emoji>",
					description = "Delete an emoji")
	@has_permissions(manage_emojis=True)
	async def delemoji(self, ctx, emoji: discord.Emoji):
		await ctx.message.delete()
		name = emoji.name
		emojiurl = emoji.url
		await emoji.delete()
		embed = discord.Embed(title="Emoji Deleted", url=luna.titleurlvar(), description=f"{name}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=emojiurl)
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = 'playing', 
				usage="<text>", 
				description = "Change your activity to playing.")
	async def playing(self, ctx, *, status: str = None):
		await ctx.message.delete()
		if status is None:
			luna.printerror("You didnt put a text to play")
		else:
			try:
				game = discord.Activity(type=0, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Status changed to: **Playing {status}**", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
			except Exception as e:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"{e}", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)


	@commands.command(name = 'streaming', 
				usage="<text>", 
				description = "Change your activity to streaming.")
	async def streaming(self, ctx, *, status: str = None):
		await ctx.message.delete()
		if status is None:
			luna.printerror("You didnt put a text to stream")
		else:
			try:
				game = discord.Activity(type=1, name=f"{status}", url=luna.streamurl())
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Status changed to: **Streaming {status}**", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
			except Exception as e:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"{e}", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)


	@commands.command(name = 'listening', 
				usage="<text>", 
				description = "Change your activity to listening.")
	async def listening(self, ctx, *, status: str = None):
		await ctx.message.delete()
		if status is None:
			luna.printerror("You didnt put a text to listen to")
		else:
			try:
				game = discord.Activity(type=2, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Status changed to: **Listening {status}**", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
			except Exception as e:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"{e}", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = 'watching', 
				usage="<text>", 
				description = "Change your activity to watching.")
	async def watching(self, ctx, *, status: str = None):
		await ctx.message.delete()
		if status is None:
			luna.printerror("You didnt put a text to watch")
		else:
			try:
				game = discord.Activity(type=3, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Status changed to: **Watching {status}**", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				luna.send(ctx, embed)
			except Exception as e:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"{e}", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = 'stopactivity', 
				usage="", 
				aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"],
				description = "Stop your activity.")
	async def stopactivity(self, ctx):
		await ctx.message.delete()
		await self.bot.change_presence(activity=None, status=discord.Status.dnd)
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description="Stopped activity", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "clean",
					usage="<amount>",
					description = "Clean your messages")
	async def clean(self, ctx, amount: int = None):
		await ctx.message.delete()
		try:
			if amount is None:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description="Invalid amount", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
			else:
				await ctx.channel.purge(limit=amount, before=ctx.message, check=is_me)
		except:
			try:
				await asyncio.sleep(1)
				c = 0
				async for message in ctx.message.channel.history(limit=amount):
					if message.author == self.bot.user:
						c += 1
						await message.delete()
					else:
						pass
			except Exception as e:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"{e}", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = "textreact",
					aliases=['treact'],
					usage="<amount>",
					description = "Text as reaction")
	async def textreact(self, ctx, messageNo: typing.Optional[int] = 1, *, text):
		await ctx.message.delete()
		text = (c for c in text.lower())
		emotes = {
			"a": "🇦",
			"b": "🇧",
			"c": "🇨",
			"d": "🇩",
			"e": "🇪",
			"f": "🇫",
			"g": "🇬",
			"h": "🇭",
			"i": "🇮",
			"j": "🇯",
			"k": "🇰",
			"l": "🇱",
			"m": "🇲",
			"n": "🇳",
			"o": "🇴",
			"p": "🇵",
			"q": "🇶",
			"r": "🇷",
			"s": "🇸",
			"t": "🇹",
			"u": "🇺",
			"v": "🇻",
			"w": "🇼",
			"x": "🇽",
			"y": "🇾",
			"z": "🇿",
		}
		for i, m in enumerate(await ctx.channel.history(limit=100).flatten()):
			if messageNo == i:
				for c in text:
					await m.add_reaction(f"{emotes[c]}")
				break
        
	@commands.command(name = "afk",
					usage="",
					description = "AFK mode on/off")
	async def afk(self, ctx):
		await ctx.message.delete()

		if luna.afk_stat == 0:
			luna.afk_stat += 1
			luna.printmessage(f"AFK Mode: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"AFK mode: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif luna.afk_stat == 1:
			luna.afk_stat -= 1
			luna.printmessage(f"AFK Mode: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"AFK mode: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "calc",
					usage="",
					description = "Opens calculator")
	async def calc(self, ctx):
		await ctx.message.delete()
		luna.printcommand("calc")
		from subprocess import call
		call(["calc.exe"])

	@commands.command(name = "passgen",
					usage="",
					description = "Generate a password")
	async def passgen(self, ctx):
		await ctx.message.delete()

		code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Password generated:\n{code}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "invisiblenick",
					usage="",
					description = "Make your nickname invisible")
	async def invisiblenick(self, ctx):
		await ctx.message.delete()

		try:
			name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
			await ctx.author.edit(nick=name)
		except Exception as e:
			await ctx.send(f"Error: {e}")

	@commands.command(name = "hypesquad",
					usage="<bravery/brilliance/balance>",
					description = "Change Hypesquad house")
	async def hypesquad(self, ctx, house:str):
		await ctx.message.delete()
		with open('./config.json') as f:
			config = json.load(f)
		token = config.get('token')
		request = requests.session()
		headers = {
			'Authorization': token,
			'Content-Type': 'application/json'
		}

		if house == "bravery":
			payload = {'house_id': 1}
		elif house == "brilliance":
			payload = {'house_id': 2}
		elif house == "balance":
			payload = {'house_id': 3}

		try:
			request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload)
			luna.printmessage(f"Successfully set your hypesquad house to {house}")
			embed = discord.Embed(title="Hypesquad", url=luna.titleurlvar(), description=f"Successfully set your hypesquad house to {house}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		except:
			if luna.errorlog() == "console":
				luna.printerror("Failed to set your hypesquad house")
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Failed to set your hypesquad house", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

	@commands.command(name = "acceptfriends",
					usage="",
					description = "Accept all friend requests")
	async def acceptfriends(self, ctx):
		await ctx.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship == discord.RelationshipType.incoming_request:
				try:
					await relationship.accept()
					luna.printmessage(f"Accepted {relationship}")
				except Exception:
					pass


	@commands.command(name = "ignorefriends",
					usage="",
					description = "Delete all friend requests")
	async def ignorefriends(self, ctx):
		await ctx.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.incoming_request:
				relationship.delete()
				luna.printmessage(f"Deleted {relationship}")


	@commands.command(name = "delfriends",
					usage="",
					description = "Delete all friends")
	async def delfriends(self, ctx):
		await ctx.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.friend:
				try:
					await relationship.delete()
					luna.printmessage(f"Deleted {relationship}")
				except Exception:
					pass


	@commands.command(name = "clearblocked",
					usage="",
					description = "Delete all blocked friends")
	async def clearblocked(self, ctx):
		await ctx.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.blocked:
				try:
					await relationship.delete()
					luna.printmessage(f"Deleted {relationship}")
				except Exception:
					pass

	@commands.command(name = "leaveservers",
					usage="",
					description = "Leave all servers")
	async def leaveservers(self, ctx):
		await ctx.message.delete()
		try:
			guilds = requests.get('https://canary.discordapp.com/api/v8/users/@me/guilds', headers={'authorization': luna.token, 'user-agent': 'Mozilla/5.0'}).json()
			for guild in range(0, len(guilds)):
				guild_id = guilds[guild]['id']
				requests.delete(f'https://canary.discordapp.com/api/v8/users/@me/guilds/{guild_id}', headers={'authorization': luna.token, 'user-agent': 'Mozilla/5.0'})
				luna.printmessage(f"Left {guild}")
		except Exception:
			pass

def setup(bot:commands.Bot):
	bot.add_cog(UtilsCog(bot))