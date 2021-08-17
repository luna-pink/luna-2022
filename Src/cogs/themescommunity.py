import discord
from discord.ext import commands
import os
import main as luna
import asyncio
import json

# class chill:
# 	"title"= "F R E E D O M"
# 	"titleurl"= ""
# 	"footer"= "No one knows what it is so it exists as an illusion"
# 	"footer_iconurl"= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
# 	"imageurl"= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
# 	"large_imageurl"= ""
# 	"hexcolor"= "#FF7C78"
# 	"author"= ""
# 	"author_iconurl"= ""
# 	"authorurl"= ""
# 	"description"= True

class CommunitythemesCog(commands.Cog, name="Community themes"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "preview",
					usage="<theme>",
					description = "Preview a theme")
	async def preview(self, ctx, theme:str):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		notfound = False

		cog = self.bot.get_cog('Help commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"

		if theme == "chill":
			title= "F R E E D O M"
			titleurl= ""
			footer= "No one knows what it is so it exists as an illusion"
			footer_iconurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			imageurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			large_imageurl= ""
			hexcolor= 0xFF7C78
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		elif theme == "midnight":
			title= "Midnight."
			titleurl= ""
			footer= "It's Midnight."
			footer_iconurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			imageurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			large_imageurl= ""
			hexcolor= 0x4205B8
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "vaporwave":
			title= "Vapor Wave"
			titleurl= ""
			footer= "Ride the vapor wave."
			footer_iconurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			imageurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			large_imageurl= ""
			hexcolor= 0x400476
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "sweetrevenge":
			title= "Sweet Revenge."
			titleurl= ""
			footer= "Sweet revenge is nice."
			footer_iconurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			imageurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			large_imageurl= ""
			hexcolor= 0xff38d4
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "error":
			title= "Error™"
			titleurl= ""
			footer= "Error displaying footer, please contact support"
			footer_iconurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			imageurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			large_imageurl= ""
			hexcolor= 0x2e2e2e
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		else:
			notfound = True

		if notfound == True:
			if luna.errorlog() == "console":
				luna.printerror(f"No theme called {theme} found")
				return
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"No theme called **{theme}** found", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
				return

		if description == True:
			description = "<> = required, [] = optional\n\n"
		elif description == False:
			description = ""

		embed = discord.Embed(title=title, url=titleurl, description=f"{description}{helptext}\nThis is a preview of the theme **{theme}**\nThis theme was made by **{madeby}**", color=hexcolor)
		embed.set_thumbnail(url=imageurl)
		embed.set_footer(text=footer, icon_url=footer_iconurl)
		embed.set_author(name=author, url=authorurl, icon_url=author_iconurl)
		embed.set_image(url=large_imageurl)
		await luna.send(ctx, embed)

	@commands.command(name = "install",
					usage="<theme>",
					description = "Install a theme")
	async def install(self, ctx, theme:str):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		notfound = False

		if theme == "chill":
			title= "F R E E D O M"
			titleurl= ""
			footer= "No one knows what it is so it exists as an illusion"
			footer_iconurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			imageurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			large_imageurl= ""
			hexcolor= "#FF7C78"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		elif theme == "midnight":
			title= "Midnight."
			titleurl= ""
			footer= "It's Midnight."
			footer_iconurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			imageurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			large_imageurl= ""
			hexcolor= "#4205B8"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "vaporwave":
			title= "Vapor Wave"
			titleurl= ""
			footer= "Ride the vapor wave."
			footer_iconurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			imageurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			large_imageurl= ""
			hexcolor= "#400476"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "sweetrevenge":
			title= "Sweet Revenge."
			titleurl= ""
			footer= "Sweet revenge is nice."
			footer_iconurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			imageurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			large_imageurl= ""
			hexcolor= "#ff38d4"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "error":
			title= "Error™"
			titleurl= ""
			footer= "Error displaying footer, please contact support"
			footer_iconurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			imageurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			large_imageurl= ""
			hexcolor= "#2e2e2e"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		else:
			notfound = True

		if notfound == True:
			if luna.errorlog() == "console":
				luna.printerror(f"No theme called {theme} found")
				return
			else:
				embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"No theme called **{theme}** found", color=0xff0000)
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
				return

		data = {
			"title": f"{title}",
			"titleurl": f"{titleurl}",
			"footer": f"{footer}",
			"footer_iconurl": f"{footer_iconurl}",
			"imageurl": f"{imageurl}",
			"large_imageurl": f"{large_imageurl}",
			"hexcolor": f"{hexcolor}",
			"author": f"{author}",
			"author_iconurl": f"{author_iconurl}",
			"authorurl": f"{authorurl}",
			"description": description
		}
		with open(f"data/themes/{theme}.json", "w") as studs:
			json.dump(data, studs, indent=4)
		luna.configtheme(f"{theme}")

		embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Installed theme **{theme}** and changed to it\nThis theme was made by **{madeby}**", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

def setup(bot:commands.Bot):
	bot.add_cog(CommunitythemesCog(bot))