import discord
from discord.ext import commands
import main as luna
import asyncio
import requests
import os
from requests import post
import httpx
import urllib

class RaidCog(commands.Cog, name="Raid commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "tokencheck",
					usage="",
					description = "Check the tokens.txt for valid tokens")
	async def tokencheck(self, ctx):
		await ctx.message.delete()

		file = open("data/tokens.txt", "r")
		nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
		line_count = len(nonempty_lines)
		file.close()

		if os.stat("data/tokens.txt").st_size == 0:
			embed = discord.Embed(title="Tokencheck", url=luna.titleurlvar(), description=f"tokens.txt is empty...", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
			return

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ Tokencheck ]\n\nDetected {line_count} tokens.\nChecking tokens...\n\n[ {luna.footervar()} ]```")
		else:
			embed = discord.Embed(title="Tokencheck", url=luna.titleurlvar(), description=f"Detected **{line_count}** tokens.\nChecking tokens...", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)

		valid_tokens=[]
		success = 0
		failed = 0

		with open("data/tokens.txt","r+") as f:
			for line in f:
				token=line.strip("\n")
				headers = {'Content-Type': 'application/json', 'authorization': token}
				url = "https://discordapp.com/api/v6/users/@me/library"
				request = requests.get(url, headers=headers)
				if request.status_code == 200:
					valid_tokens.append(token)
					success += 1
				else:
					failed += 1
					pass

		with open("data/tokens.txt","w+") as f:
			for i in valid_tokens:
				f.write(i+"\n")

		if luna.mode() == 2:
			await sent.edit(f"```ini\n[ Tokencheck ]\n\nSuccessfully checked all tokens and removed invalid ones.\nValid tokens: "+str(success)+"\nInvalid tokens: "+str(failed)+"\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete() 
		else:
			embed = discord.Embed(title="Tokencheck", url=luna.titleurlvar(), description=f"Successfully checked all tokens and removed invalid ones.\nValid tokens: **"+str(success)+"**\nInvalid tokens: **"+str(failed)+"**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await sent.edit(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete() 

	@commands.command(name = "raidjoin",
					usage="<invitelink>",
					description = "Raid the server with tokens")
	async def raidjoin(self, ctx, invitelink:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":
		# link = "https://discord.com/api/v6/invites/" + invitelink.split("/")[-1]
		# joined = 0
		# failed = 0

		# if luna.mode() == 2:
		# 	sent = await ctx.send(f"```ini\n[ Raid Join ]\n\nRaiding...\n\n[ {luna.footervar()} ]```")
		# else:
		# 	embed = discord.Embed(title="Raid Join", url=luna.titleurlvar(), description=f"Raiding...", color=luna.hexcolorvar())
		# 	embed.set_thumbnail(url=luna.imagevar())
		# 	embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		# 	embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		# 	embed.set_image(url=luna.largeimagevar())
		# 	sent = await ctx.send(embed=embed)

		# with open("data/tokens.txt","r") as f:
		# 	tokens = f.read().splitlines()
		# 	for token in tokens:
		# 		headers = {"Content-Type": "application/json", 
        #            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        #            "Authorization" : token}
				
		# 		response = post(link, headers=headers).status_code
		# 		if response > 199 and response < 300:
		# 			joined += 1
		# 		else:
		# 			failed += 1

		# if luna.mode() == 2:
		# 	await sent.edit(content=f"```ini\n[ Raid Join ]\n\nAccounts that joined: "+str(joined)+"\nAccounts that could not join: "+str(failed)+f"\n\n[ {luna.footervar()} ]```")
		# 	await asyncio.sleep(luna.deletetimer())
		# 	await sent.delete() 
		# else:
		# 	embed = discord.Embed(title="Raid Join", url=luna.titleurlvar(), description="Accounts that joined: **"+str(joined)+"**\nAccounts that could not join: **"+str(failed)+"**", color=luna.hexcolorvar())
		# 	embed.set_thumbnail(url=luna.imagevar())
		# 	embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		# 	embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		# 	embed.set_image(url=luna.largeimagevar())
		# 	await sent.edit(embed=embed)
		# 	await asyncio.sleep(luna.deletetimer())
		# 	await sent.delete()

			tokens = open('data/tokens.txt', 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.post(f'https://canary.discord.com/api/v8/invites/{invitelink}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
						luna.printevent(f"{_token} joined {invitelink}")
				except Exception:
					luna.printerror(f"{_token} failed to join {invitelink}")
					pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "proxyjoin",
					usage="<invitelink>",
					description = "Raid the server with tokens using proxies")
	async def proxyjoin(self, ctx, invitelink:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":

			tokens = open('data/tokens.txt', 'r')
			proxies = open('data/proxies.txt', 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)
				
			for p, _token in enumerate(tokens):
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.post(f'https://canary.discord.com/api/v8/invites/{invitelink}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http': f'{proxylist[p]}'})
						luna.printevent(f"[PROXY] {_token} joined {invitelink}")
				except Exception:
					luna.printerror(f"[PROXY] {_token} failed to join {invitelink}")
					pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "raidspam",
					usage="<channel_id> <amount> <message>",
					description = "Spam the channel with tokens")
	async def raidspam(self, ctx, channel_id:str, amount:int, *, message:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":

			tokens = open('data/tokens.txt', 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						for i in range(0, amount):
							await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{message}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
							luna.printevent(f"{_token} sent {message}")
				except Exception:
					luna.printerror(f"{_token} failed to send {message}")
					pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "proxyspam",
					usage="<channel_id> <amount> <message>",
					description = "Spam the channel with tokens using proxies")
	async def proxyspam(self, ctx, channel_id:str, amount:int, *, message:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":

			tokens = open('data/tokens.txt', 'r')
			proxies = open('data/proxies.txt', 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)

			tokens = open('data/tokens.txt', 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						for i in range(0, amount):
							await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{message}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http': f'{proxylist[p]}'})
							luna.printevent(f"{_token} sent {message}")
				except Exception:
					luna.printerror(f"{_token} failed to send {message}")
					pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "raidleave",
					usage="<server_id>",
					description = "Leave the server with raided tokens")
	async def raidleave(self, ctx, server_id:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":

			tokens = open('data/tokens.txt', 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.delete(f'https://canary.discord.com/api/v8/users/@me/guilds/{server_id}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
						luna.printevent(f"{_token} left {server_id}")
				except Exception:
					luna.printerror(f"{_token} failed to leave {server_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "proxyleave",
					usage="<server_id>",
					description = "Leave the server with raided tokens using proxies")
	async def proxyleave(self, ctx, server_id:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":

			tokens = open('data/tokens.txt', 'r')
			proxies = open('data/proxies.txt', 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)

			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.delete(f'https://canary.discord.com/api/v8/users/@me/guilds/{server_id}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http': f'{proxylist[p]}'})
						luna.printevent(f"[PROXY] {_token} left {server_id}")
				except Exception:
					luna.printerror(f"[PROXY] {_token} failed to leave {server_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "raidreact",
					usage="<channel_id> <message_id> <emoji>",
					description = "Leave the server with raided tokens")
	async def raidreact(self, ctx, channel_id: str, message_id: str, emoji: str):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			tokens = open('data/tokens.txt', 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.put(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages/{message_id}/reactions/{urllib.parse.quote(emoji)}/%40me', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
						luna.printevent(f"{_token} reacted on {message_id}")
				except Exception:
					luna.printerror(f"{_token} failed to react on {message_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "proxyreact",
					usage="<channel_id> <message_id> <emoji>",
					description = "Leave the server with raided tokens")
	async def proxyreact(self, ctx, channel_id: str, message_id: str, emoji: str):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			tokens = open('data/tokens.txt', 'r')
			proxies = open('data/proxies.txt', 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)

			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.put(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages/{message_id}/reactions/{urllib.parse.quote(emoji)}/%40me', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http': f'{proxylist[p]}'})
						luna.printevent(f"{_token} reacted on {message_id}")
				except Exception:
					luna.printerror(f"{_token} failed to react on {message_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

def setup(bot:commands.Bot):
	bot.add_cog(RaidCog(bot))