import discord
from discord.ext import commands
import main as luna
import asyncio
import json
import requests

class HelpCog(commands.Cog, name="Help commands"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
  

	@commands.command(name = 'help',
					usage="[command]",
					description = "Display the help message.",
					aliases = ['h', '?'])
	async def help (self, ctx, commandName:str=None):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		commandName2 = None
		stop = False

		if commandName is not None:
			for i in self.bot.commands:
				if i.name == commandName.lower():
					commandName2 = i
					break 
				else:
					for j in i.aliases:
						if j == commandName.lower():
							commandName2 = i
							stop = True
							break
						if stop is True:
							break 

			if commandName2 is None:
				if luna.errorlog() == "console":
					luna.printerror(f"No command found with name or alias {luna.bcolors.COMMANDVAR}{commandName}{luna.bcolors.RESET}")
				else:
					embed = discord.Embed(
						title="**Error**",
						description=f"No command found with name or alias {commandName}",
						color=0xff0000
					)
					embed.set_thumbnail(url=luna.imagevar())
					embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
					embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
					embed.set_image(url=luna.largeimagevar())
					await luna.send(ctx, embed)
			else:
				if luna.mode() == 2:
					aliases = commandName2.aliases
					aliasList = ""
					if len(aliases) > 0:
						for alias in aliases:
							aliasList += alias + ", "
						aliasList = aliasList[:-2]
						if commandName2.usage is None:
							sent = await ctx.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{luna.descriptionvar()}Name\n{commandName2.name}\n\nAliases\n{aliasList}\n\nUsage\nNone\n\nDescription\n{commandName2.description}\n\n[ {luna.footervar()} ]```")
						else:
							sent = await ctx.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{luna.descriptionvar()}Name\n{commandName2.name}\n\nAliases\n{aliasList}\n\nUsage\n{prefix}{commandName2.name} {commandName2.usage}\n\nDescription\n{commandName2.description}\n\n[ {luna.footervar()} ]```")
					else:
						if commandName2.usage is None:
							sent = await ctx.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{luna.descriptionvar()}Name\n{commandName2.name}\n\nAliases\nNone\n\nUsage\nNone\n\nDescription\n{commandName2.description}\n\n[ {luna.footervar()} ]```")
						else:
							sent = await ctx.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{luna.descriptionvar()}Name\n{commandName2.name}\n\nAliases\nNone\n\nUsage\n{prefix}{commandName2.name} {commandName2.usage}\n\nDescription\n{commandName2.description}\n\n[ {luna.footervar()} ]```")
					await asyncio.sleep(luna.deletetimer())
					await sent.delete()
				elif luna.mode() == 3:

					aliases = commandName2.aliases
					aliasList = ""
					if len(aliases) > 0:
						for alias in aliases:
							aliasList += alias + ", "
						aliasList = aliasList[:-2]
						if commandName2.usage is None:
							sent = await ctx.send(f"> **{commandName2.name.title()} Command**\n> \n> **Name**\n> {commandName2.name}\n> \n> **Aliases**\n> {aliasList} \n> \n> **Usage**\n> None\n> \n> **Description**\n> {commandName2.description}\n> \n> {luna.footervar()}")
						else:
							sent = await ctx.send(f"> **{commandName2.name.title()} Command**\n> \n> **Name**\n> {commandName2.name}\n> \n> **Aliases**\n> {aliasList} \n> \n> **Usage**\n> {prefix}{commandName2.name} {commandName2.usage}\n> \n> **Description**\n> {commandName2.description}\n> \n> {luna.footervar()}")
					else:
						if commandName2.usage is None:
							sent = await ctx.send(f"> **{commandName2.name.title()} Command**\n> \n> **Name**\n> {commandName2.name}\n> \n> **Aliases**\n> None \n> \n> **Usage**\n> None\n> \n> **Description**\n> {commandName2.description}\n> \n> {luna.footervar()}")
						else:
							sent = await ctx.send(f"> **{commandName2.name.title()} Command**\n> \n> **Name**\n> {commandName2.name}\n> \n> **Aliases**\n> None \n> \n> **Usage**\n> {prefix}{commandName2.name} {commandName2.usage}\n> \n> **Description**\n> {commandName2.description}\n> \n> {luna.footervar()}")
					
					await asyncio.sleep(luna.deletetimer())
					await sent.delete()

				else:
					embed = discord.Embed(title=f"{commandName2.name.title()} Command", description=f"{luna.descriptionvar()}", color=luna.hexcolorvar())
					embed.set_thumbnail(url=luna.imagevar())
					embed.add_field(name=f"Name", value=f"{commandName2.name}", inline=False)
					aliases = commandName2.aliases
					aliasList = ""
					if len(aliases) > 0:
						for alias in aliases:
							aliasList += alias + ", "
						aliasList = aliasList[:-2]
						embed.add_field(name=f"Aliases", value=aliasList)
					else:
						embed.add_field(name=f"Aliases", value="None", inline=False)

					if commandName2.usage is None:
						embed.add_field(name=f"Usage", value=f"None", inline=False)
					else:
						embed.add_field(name=f"Usage", value=f"{prefix}{commandName2.name} {commandName2.usage}", inline=False)
					embed.add_field(name=f"Description", value=f"{commandName2.description}", inline=False)
					embed.set_thumbnail(url=luna.imagevar())
					embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
					embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
					embed.set_image(url=luna.largeimagevar())
					await luna.send(ctx, embed)
		else:
			cog = self.bot.get_cog('Help commands')
			commands = cog.get_commands()
			helptext = ""
			for command in commands:
				helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "admin",
					usage="",
					description = "Administrative commands")
	async def admin(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Administrative commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Administrative commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "animated",
					usage="",
					description = "Animated commands")
	async def animated(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Animated commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Animated commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "text",
					usage="",
					description = "Text commands")
	async def text(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Text commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Text commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "image",
					usage="",
					description = "Image commands")
	async def image(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Image commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Image commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "troll",
					usage="",
					description = "Troll commands")
	async def troll(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Troll commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Troll commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "fun",
					usage="",
					description = "Funny commands")
	async def fun(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Fun commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Funny commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "tools",
					usage="",
					description = "General tools")
	async def tools(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Tools commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="General tools", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "nettools",
					usage="",
					description = "Networking tools")
	async def nettools(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Nettool commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Networking tools", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "utils",
					usage="",
					aliases=['utility', 'utilities'],
					description = "Utilities")
	async def utils(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Util commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Utility commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "abuse",
					usage="",
					description = "Abusive commands")
	async def abuse(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Abusive commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Abusive commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "raid",
					usage="",
					description = "Raiding servers")
	async def raid(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Raid commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Raid commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "nuking",
					usage="",
					description = "Account nuking")
	async def nuking(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Nuking commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Nuking commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "protection",
					usage="",
					aliases=['protections', 'protect'],
					description = "Protections")
	async def protection(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Protection commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Protections", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "misc",
					usage="",
					description = "Miscellaneous commands")
	async def misc(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Miscellaneous commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Miscellaneous commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "settings",
					usage="",
					description = "Settings")
	async def settings(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		deletetimer = int(config.get('deletetimer'))
		errorlog = config.get('errorlog')
		riskmode = config.get('riskmode')
		themesvar = config.get('theme')
		with open(f"data/themes/{themesvar}") as f:
			customi = json.load(f)
		description = customi.get('description')

		cog = self.bot.get_cog('Settings commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Settings", description=f"{luna.descriptionvar()}Error logging: **{errorlog}**\nAuto delete timer: **{deletetimer}**\nRiskmode: **{riskmode}**\nTheme: **{(themesvar[:-5])}**\nDescription: **{description}**\n\n{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "sharing",
					usage="",
					description = "Share commands")
	async def sharing(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		with open('data/sharing.json') as f:
			slot = json.load(f)
		share = slot.get('share')
		user_id = slot.get('user_id')

		if user_id == "":
			sharinguser = "None"
		else:
			sharinguser = await self.bot.fetch_user(user_id)

		cog = self.bot.get_cog('Share commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Sharing", description=f"{luna.descriptionvar()}Share: **{share}**\nUser: **{sharinguser}**\n\n{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	# @commands.command(name = "profile",
	# 				usage="",
	# 				description = "Profile commands")
	# async def profile(self, ctx):
	# 	await ctx.message.delete()

	# 	with open("config.json", "r") as f:
	# 		config = json.load(f)
	# 	prefix = config.get('prefix')

	# 	cog = self.bot.get_cog('Profile commands')
	# 	commands = cog.get_commands()
	# 	helptext = ""
	# 	for command in commands:
	# 		helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
	# 	embed = discord.Embed(title="Profile commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
	# 	embed.set_thumbnail(url=luna.imagevar())
	# 	embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
	# 	embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
	# 	embed.set_image(url=luna.largeimagevar())
	# 	await luna.send(ctx, embed)
		
	# @commands.command(name = "richpresence",
	# 				usage="",
	# 				description = "Richpresence settings")
	# async def richpresence(self, ctx):
	# 	await ctx.message.delete()

	# 	with open("config.json", "r") as f:
	# 		config = json.load(f)
	# 	prefix = config.get('prefix')

	# 	cog = self.bot.get_cog('Richpresence settings')
	# 	commands = cog.get_commands()
	# 	helptext = ""
	# 	for command in commands:
	# 		helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
	# 	embed = discord.Embed(title="Richpresence commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
	# 	embed.set_thumbnail(url=luna.imagevar())
	# 	embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
	# 	embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
	# 	embed.set_image(url=luna.largeimagevar())
	# 	await luna.send(ctx, embed)

	@commands.command(name = "community",
					usage="",
					description = "Community suggested commands")
	async def community(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Community commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Community suggested commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "customhelp",
					usage="",
					description = "Show custom commands")
	async def custom(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Custom commands')
		commands = cog.get_commands()
		helptext = ""
		if commands == []:
			helptext = "No custom commands found!"
		else:
			for command in commands:
				helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Custom commands", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "search",
					usage="<command>",
					description = "Search for a command")
	async def search(self, ctx, commandName:str):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		helptext = ''
		for command in self.bot.commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description},"

		commandlist = helptext.split(",")
			
		commandlistfind = [ string for string in commandlist if commandName in string]
		commandlistfind='\n'.join(str(e) for e in commandlistfind)

		if not len(commandlistfind) == 0:
			embed = discord.Embed(title=f"Searched for: {commandName}", description=f"{luna.descriptionvar()}{commandlistfind}", color=luna.hexcolorvar())
		else:
			embed = discord.Embed(title=f"Searched for: {commandName}", description=f"{luna.descriptionvar()}No command has been found.", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "covid",
					aliases=['corona'],
					usage="",
					description = "Corona statistics")
	async def covid(self, ctx):
		await ctx.message.delete()

		request = requests.get(f'https://api.covid19api.com/summary')
		data = request.json()
		info = data['Global']
		totalconfirmed = info['TotalConfirmed']
		totalrecovered = info['TotalRecovered']
		totaldeaths = info['TotalDeaths']
		newconfirmed = info['NewConfirmed']
		newrecovered = info['NewRecovered']
		newdeaths = info['NewDeaths']
		date = info['Date']

		embed = discord.Embed(title="Covid-19 Statistics", description=f"**Total Confirmed Cases**\n{totalconfirmed}\n\n**Total Deaths**\n{totaldeaths}\n\n**Total Recovered**\n{totalrecovered}\n\n**New Confirmed Cases**\n{newconfirmed}\n\n**New Deaths**\n{newdeaths}\n\n**New Recovered**\n{newrecovered}\n\n**Date**\n{date}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)
	

def setup(bot:commands.Bot):
	bot.remove_command("help")
	bot.add_cog(HelpCog(bot))
