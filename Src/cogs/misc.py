import discord
from discord.ext import commands
import main as luna
import asyncio
import json
import requests
import urllib

class MiscCog(commands.Cog, name="Miscellaneous commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "thelp",
					usage="",
					description = "All commands in a text file")
	async def thelp(self, ctx):
		await ctx.message.delete()

		#///////////////////////////////////////////////////////////////////

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		#///////////////////////////////////////////////////////////////////

		cog = self.bot.get_cog('Help commands')
		commands = cog.get_commands()
		helpcommands = ""
		for command in commands:
			helpcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Administrative commands')
		commands = cog.get_commands()
		admincommands = ""
		for command in commands:
			admincommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Animated commands')
		commands = cog.get_commands()
		animatedcommands = ""
		for command in commands:
			animatedcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Text commands')
		commands = cog.get_commands()
		textcommands = ""
		for command in commands:
			textcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"
			
		cog = self.bot.get_cog('Image commands')
		commands = cog.get_commands()
		imagecommands = ""
		for command in commands:
			imagecommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Troll commands')
		commands = cog.get_commands()
		trollcommands = ""
		for command in commands:
			trollcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Fun commands')
		commands = cog.get_commands()
		funcommands = ""
		for command in commands:
			funcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Tools commands')
		commands = cog.get_commands()
		toolscommands = ""
		for command in commands:
			toolscommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Nettool commands')
		commands = cog.get_commands()
		nettoolscommands = ""
		for command in commands:
			nettoolscommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Util commands')
		commands = cog.get_commands()
		utilscommands = ""
		for command in commands:
			utilscommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Abusive commands')
		commands = cog.get_commands()
		abusecommands = ""
		for command in commands:
			abusecommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Raid commands')
		commands = cog.get_commands()
		raidcommands = ""
		for command in commands:
			raidcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Nuking commands')
		commands = cog.get_commands()
		nukecommands = ""
		for command in commands:
			nukecommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Protection commands')
		commands = cog.get_commands()
		protectioncommands = ""
		for command in commands:
			protectioncommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Miscellaneous commands')
		commands = cog.get_commands()
		misccommands = ""
		for command in commands:
			misccommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Settings commands')
		commands = cog.get_commands()
		settingscommands = ""
		for command in commands:
			settingscommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Share commands')
		commands = cog.get_commands()
		sharecommands = ""
		for command in commands:
			sharecommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Community commands')
		commands = cog.get_commands()
		communitycommands = ""
		for command in commands:
			communitycommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Toast customization')
		commands = cog.get_commands()
		toastcustomcommands = ""
		for command in commands:
			toastcustomcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Toast commands')
		commands = cog.get_commands()
		toastcommands = ""
		for command in commands:
			toastcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Customization commands')
		commands = cog.get_commands()
		customizationcommands = ""
		for command in commands:
			customizationcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Webhook commands')
		commands = cog.get_commands()
		webhookcommands = ""
		for command in commands:
			webhookcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('NSFW commands')
		commands = cog.get_commands()
		nsfwcommands = ""
		for command in commands:
			nsfwcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Cryptocurrency commands')
		commands = cog.get_commands()
		cryptocommands = ""
		for command in commands:
			cryptocommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Cryptocurrency commands page 2')
		commands = cog.get_commands()
		for command in commands:
			cryptocommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"
		
		cog = self.bot.get_cog('Cryptocurrency commands page 3')
		commands = cog.get_commands()
		for command in commands:
			cryptocommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Cryptocurrency commands page 4')
		commands = cog.get_commands()
		for command in commands:
			cryptocommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Cryptocurrency commands page 5')
		commands = cog.get_commands()
		for command in commands:
			cryptocommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Cryptocurrency commands page 6')
		commands = cog.get_commands()
		for command in commands:
			cryptocommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Cryptocurrency commands page 7')
		commands = cog.get_commands()
		for command in commands:
			cryptocommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Cryptocurrency commands page 8')
		commands = cog.get_commands()
		for command in commands:
			cryptocommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		#///////////////////////////////////////////////////////////////////

		commandcount = len(self.bot.commands)

		file = open("commands.txt", "w") 
		file.write(f"{commandcount} Commands\n\n{luna.descriptionvar()}Categories:\n{helpcommands}\nAdmin Commands:\n{admincommands}\nAnimated Commands:\n{animatedcommands}\nText Commands:\n{textcommands}\nImage Commands:\n{imagecommands}\nTroll Commands:\n{trollcommands}\nFun Commands:\n{funcommands}\nTools:\n{toolscommands}\nNetworking Tools\n{nettoolscommands}\nUtilities\n{utilscommands}\nAbusive Commands\n{abusecommands}\nRaiding\n{raidcommands}\nNuking\n{nukecommands}\nProtections\n{protectioncommands}\nMiscellaneous\n{misccommands}\nSettings\n{settingscommands}\nSharing\n{sharecommands}\nCommunity Suggested Commands\n{communitycommands}\nCustomization\n{customizationcommands}\nToast Settings\n{toastcommands}\nToast Customization\n{toastcustomcommands}\nWebhook Settings\n{webhookcommands}\nNSFW\n{nsfwcommands}\nCryptocurrency\n{cryptocommands}")
		file.close()

		embed = discord.Embed(title=luna.titlevar(), description=f"Saved all commands in commands.txt", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "update",
					usage="",
					description = "Updates Luna if there's an update")
	async def update(self, ctx):
		await ctx.message.delete()
		versionpastedec = urllib.request.urlopen('https://pastebin.com/raw/iQPkzEpg')
		for line in versionpastedec:
			versionpaste = line.decode().strip()
		if luna.lunaversion in versionpaste:
			embed = discord.Embed(title="Update", description=f"You are on the latest version!", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Update", description=f"Started update: {luna.versionpaste}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
			luna.restart_program()

	@commands.command(name = "crypto",
					usage="",
					description = "Cryptocurrency")
	async def crypto(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Cryptocurrency commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Cryptocurrency", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "restart",
					usage="",
					aliases=['reboot'],
					description = "Restart Lolicon")
	async def restart(self, ctx):
		await ctx.message.delete()

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ Restarting ]\n\nAllow up to 5 seconds.\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(3)
			await sent.delete()
			luna.restart_program()
		if luna.mode() == 3:
			sent = await ctx.send(f"> **Restarting**\n> \n> Allow up to 5 seconds.\n> \n> {luna.footervar()}")
			await asyncio.sleep(3)
			await sent.delete()
			luna.restart_program()
		else:
			embed = discord.Embed(title="Restarting", url=luna.titleurlvar(), description=f"Allow up to 5 seconds.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(3)
			await sent.delete()
			luna.restart_program()

	@commands.command(name = "clear",
					aliases=['cls'],
					usage="",
					description = "Clear the console")
	async def clear(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
        
		luna.Clear()
		luna.Logo()
		print(f"                           Status:    {luna.bcolors.LIGHTMAGENTA}CONNECTED{luna.bcolors.RESET}")
		print(f"                           Account:   {self.bot.user} [{len(self.bot.guilds)} Servers] [{len(self.bot.user.friends)} Friends]")
		print(f"                           Prefix:    {prefix}")
		print("___________________________________________________________________________________________________")

	@commands.command(name = "fnshop",
					usage="",
					description = "Current Fortnite shop")
	async def fnshop(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title="Fortnite Shop", color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url="https://api.nitestats.com/v1/shop/image")
		await luna.send(ctx, embed)

	@commands.command(name = "fnmap",
					usage="",
					description = "Current Fortnite map")
	async def fnmap(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title="Fortnite Map", color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url="https://media.fortniteapi.io/images/map.png?showPOI=true")
		await luna.send(ctx, embed)

	@commands.command(name = "fnnews",
					usage="",
					description = "Current Fortnite news")
	async def fnnews(self, ctx):
		await ctx.message.delete()
		fortnite = requests.get("https://fortnite-api.com/v2/news/br").json()
		embed = discord.Embed(title="Fortnite News", color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=fortnite["data"]["image"])
		await luna.send(ctx, embed)

def setup(bot:commands.Bot):
	bot.add_cog(MiscCog(bot))