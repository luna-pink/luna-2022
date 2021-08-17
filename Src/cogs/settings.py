import discord
from discord.ext import commands
import json
import main as luna
import asyncio
import os
import sys

class SettingsCog(commands.Cog, name="Settings commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "prefix",
					usage="<newprefix>",
					description = "Change the prefix")
	async def prefix(self, ctx, newprefix):
		await ctx.message.delete()

		luna.configprefix(newprefix)
		commandcount = len(self.bot.commands)

		luna.Clear()
		luna.Title(f"Lolicon | V2")
		luna.Logo()
		print(f"                           Status:    {luna.bcolors.LIGHTMAGENTA}CONNECTED{luna.bcolors.RESET}")
		print(f"                           Account:   {self.bot.user} [{len(self.bot.guilds)} Servers] [{len(self.bot.user.friends)} Friends]")
		print(f"                           Prefix:    {newprefix}")
		print("___________________________________________________________________________________________________")
		# luna.printmessage("Dominate the competition with Lolicon.\n")
		luna.printmessage(f"{newprefix}purgehack to ruin someones day. {commandcount} commands.\n")

		luna.printmessage(f"Prefix changed to {luna.bcolors.COMMANDVAR}{newprefix}{luna.bcolors.RESET}")

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ Prefix ]\n\nNew prefix: {newprefix}\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		elif luna.mode() == 3:
			sent = await ctx.send(f"> **Prefix**\n> \n> New prefix: {newprefix}\n> \n> {luna.footervar()}")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title="Prefix", url=luna.titleurlvar(), description=f"New prefix: {newprefix}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

	@commands.command(name = "themes",
					usage="",
					description = "Themes")
	async def themes(self, ctx):
		await ctx.message.delete()

		path_to_json = 'data/themes/'
		json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		themesvar = config.get('theme')

		cog = self.bot.get_cog('Theme commands')
		commands = cog.get_commands()
		helptext = ""

		if luna.mode() == 2:
			for command in commands:
				if len(command.usage) == 0:
					command.usage = command.usage+""
				else:
					command.usage = command.usage+" "
				helptext+=f"[ {prefix}{command.name} {command.usage}] {command.description}\n"

			string = f"{json_files}"
			stringedit = string.replace(',', f"\n{prefix}theme").replace("'", "").replace('[', f"{prefix}theme ").replace(']', "").replace('.json', "")

			sent = await ctx.send(f"```ini\n[ Themes ]\n\n{luna.descriptionvar()}Current theme: {(themesvar[:-5])}\n\n{helptext}\n{stringedit}\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete() 
		elif luna.mode() == 3:
			for command in commands:
				helptext+=f"> **{prefix}{command.name} {command.usage}** » {command.description}\n"

			string = f"{json_files}"
			stringedit = string.replace(',', f"\n> {prefix}theme").replace("'", "").replace('[', f"{prefix}theme ").replace(']', "").replace('.json', "")

			sent = await ctx.send(f"> **Themes**\n> \n{luna.descriptionvar()}> Current theme: **{(themesvar[:-5])}**\n> \n{helptext}> \n> **{stringedit}**\n> \n> {luna.footervar()}")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			for command in commands:
				helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"

			string = f"{json_files}"
			stringedit = string.replace(',', f"\n{prefix}theme").replace("'", "").replace('[', f"{prefix}theme ").replace(']', "").replace('.json', "")

			embed = discord.Embed(title="Themes", description=f"{luna.descriptionvar()}Current theme: **{(themesvar[:-5])}**\n\n{helptext}\n**{stringedit}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

	@commands.command(name = "customize",
					usage="",
					aliases=['customise', 'customization'],
					description = "Theme customization")
	async def customize(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		themesvar = config.get('theme')
		with open(f"data/themes/{themesvar}") as f:
			customi = json.load(f)
		title = customi.get('title')
		footer = customi.get('footer')
		hexcolor = customi.get('hexcolor')
		author = customi.get('author')

		if title == "":
			title = "None"
		if footer == "":
			footer = "None"
		if hexcolor == "":
			hexcolor = "None"
		if author == "":
			author = "None"

		cog = self.bot.get_cog('Customization commands')
		commands = cog.get_commands()
		helptext = ""

		wcog = self.bot.get_cog('Webhook commands')
		wcommands = wcog.get_commands()
		whelptext = ""

		tcog = self.bot.get_cog('Toast customization')
		tcommands = tcog.get_commands()
		thelptext = ""

		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		for command in wcommands:
			whelptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		for command in tcommands:
			thelptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Customization", description=f"{luna.descriptionvar()}Title: **{title}**\nFooter: **{footer}**\nColor: **{hexcolor}**\nAuthor: **{author}**\n\nSelfbot\n{helptext}\nWebhook\n{whelptext}\nToast\n{thelptext}\nNote\nIf you want to remove a customization,\nYou can use **None** to remove it.\n\nIf you want to set up a random color each time\nyou run a command, you can use **random** as hex color.", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "embedmode",
					usage="",
					description = "Switch to embed mode")
	async def embedmode(self, ctx):
		await ctx.message.delete()

		luna.configmode("1")
		luna.printmessage(f"Switched to {luna.bcolors.COMMANDVAR}embed{luna.bcolors.RESET} mode")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Switched to embed mode.", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "textmode",
					usage="",
					description = "Switch to text mode")
	async def textmode(self, ctx):
		await ctx.message.delete()

		luna.configmode("2")
		luna.printmessage(f"Switched to {luna.bcolors.COMMANDVAR}text{luna.bcolors.RESET} mode")

		sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nSwitched to text mode.\n\n[ {luna.footervar()} ]```")
		await asyncio.sleep(luna.deletetimer())
		await sent.delete()

	@commands.command(name = "indentmode",
					usage="",
					description = "Switch to indent mode")
	async def indentmode(self, ctx):
		await ctx.message.delete()

		luna.configmode("3")
		luna.printmessage(f"Switched to {luna.bcolors.COMMANDVAR}indent{luna.bcolors.RESET} mode")

		sent = await ctx.send(f"> **{luna.titlevar()}**\n> \n> Switched to **indent** mode.\n> \n> {luna.footervar()}")
		await asyncio.sleep(luna.deletetimer())
		await sent.delete()

	@commands.command(name = "sniper",
					usage="",
					description = "Sniper settings")
	async def sniper(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		with open('data/nitro.json') as f:
			data = json.load(f)
		nitro_sniper = data.get('nitrosniper')
		api = data.get('api')

		cog = self.bot.get_cog('Sniper settings')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Sniper settings", description=f"{luna.descriptionvar()}Nitro Sniper: **{nitro_sniper}**\nNitro API: **{api}**\n\n{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "giveaway",
					usage="",
					description = "Giveaway settings")
	async def giveaway(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		with open('data/giveawayjoiner.json') as f:
			data = json.load(f)
		giveawayjoiner = data.get('giveawayjoiner')
		delay_in_minutes = int(data.get('delay_in_minutes'))
		giveaway_server_joiner = data.get('giveaway_server_joiner')

		cog = self.bot.get_cog('Giveaway settings')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Giveaway settings", description=f"{luna.descriptionvar()}Giveaway Joiner: **{giveawayjoiner}**\nDelay: **{delay_in_minutes} minute/s**\nServer Joiner: **{giveaway_server_joiner}**\n\n{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "notifications",
					usage="",
					description = "Toast notifications")
	async def notifications(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		with open('data/toasts.json') as f:
			notif = json.load(f)
		toasts = notif.get('toasts')
		login = notif.get('login')
		nitro = notif.get('nitro')
		giveaway = notif.get('giveaway')
		privnote = notif.get('privnote')
		slotbot = notif.get('slotbot')
		selfbot = notif.get('selfbot')
		pings = notif.get('pings')
		ghostpings = notif.get('ghostpings')
		friendevents = notif.get('friendevents')
		guildevents = notif.get('guildevents')
		nickupdates = notif.get('nickupdates')
		protection = notif.get('protection')

		cog = self.bot.get_cog('Toast commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Toast notifications", description=f"{luna.descriptionvar()}Toasts: **{toasts}**\nLogin toasts: **{login}**\nNitro toasts: **{nitro}**\nGiveaway toasts: **{giveaway}**\nPrivnote toasts: **{privnote}**\nSlotbot toasts: **{slotbot}**\nSelfbot toasts: **{selfbot}**\nPing toasts: **{pings}**\nGhostping toasts: **{ghostpings}**\nFriendevent toasts: **{friendevents}**\nGuildevent toasts: **{guildevents}**\nNickname toasts: **{nickupdates}**\nProtection toasts: **{protection}**\n\n{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)
	
	@commands.command(name = "errorlog",
					usage="<console/message>",
					description = "Switch errorlog")
	async def errorlog(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "console":

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Error logging: **console**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

			luna.printmessage(f"Error logging: {luna.bcolors.LIGHTMAGENTA}console{luna.bcolors.RESET}")
			luna.configerrorlog("console")

		elif mode == "message":

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Error logging: **message**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

			luna.printmessage(f"Error logging: {luna.bcolors.LIGHTMAGENTA}message{luna.bcolors.RESET}")
			luna.configerrorlog("message")
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **console** or **message**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "deletetimer",
					usage="<seconds>",
					description = "Auto delete timer")
	async def deletetimer(self, ctx, seconds:int):
		await ctx.message.delete()

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Auto delete timer: **{seconds} seconds**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

		luna.printmessage(f"Auto delete timer: {luna.bcolors.LIGHTMAGENTA}{seconds} seconds{luna.bcolors.RESET}")
		luna.configdeletetimer(f"{seconds}")

	@commands.command(name = "afkmessage",
					usage="<text>",
					description = "Change the afk message")
	async def afkmessage(self, ctx, afkmessage):
		await ctx.message.delete()

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"AFK message: **{afkmessage}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

		luna.printmessage(f"AFK message: {luna.bcolors.LIGHTMAGENTA}{afkmessage}{luna.bcolors.RESET}")
		luna.configafkmessage(f"{afkmessage}")

	@commands.command(name = "riskmode",
					usage="<on/off>",
					description = "Enable abusive commands")
	async def riskmode(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Riskmode: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

			luna.printmessage(f"Riskmode: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configriskmode("on")

		elif mode == "off":

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Riskmode: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

			luna.printmessage(f"Riskmode: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configriskmode("off")
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "description",
					usage="<on/off>",
					description = "Turn on/off <> = required, [] = optional")
	async def description(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Description: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

			luna.printmessage(f"Description: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configselfbotdescription(True)

		elif mode == "off":

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Description: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

			luna.printmessage(f"Description: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configselfbotdescription(False)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "selfbotdetection",
					usage="<on/off>",
					description = "Turn selfbot detection on or off")
	async def selfbotdetection(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Selfbot detection: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

			luna.printmessage(f"Selfbot detection: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configselfbot_detection("on")

		elif mode == "off":

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Selfbot detection: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

			luna.printmessage(f"Selfbot detection: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configselfbot_detection("off")
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "password",
					usage="<new_password>",
					description = "Change password config")
	async def password(self, ctx, password:str):
		await ctx.message.delete()

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Changed password to: **{password}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

		luna.printmessage(f"Changed password to: {luna.bcolors.LIGHTMAGENTA}{password}{luna.bcolors.RESET}")
		luna.configpassword(f"{password}")

	@commands.command(name = "reload",
					usage="",
					description = "Reload custom commands")
	async def reload(self, ctx):
		await ctx.message.delete()
		try:
			self.bot.unload_extension(f"cogs.custom")
			self.bot.load_extension(f"cogs.custom")
		except Exception as e:
			if luna.errorlog() == "console":
				luna.printerror(e)
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Failed to reload custom commands.", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Reloaded custom commands.", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

		luna.printmessage(f"Reloaded custom commands")

def setup(bot:commands.Bot):
	bot.add_cog(SettingsCog(bot))