import discord
from discord.ext import commands
import time
import main as luna
import asyncio


class ProtectionCog(commands.Cog, name="Protection commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "antiraid",
					usage="",
					description = "Protects against raids")
	async def antiraid(self, ctx):
		await ctx.message.delete()

		if luna.antiraid == False:
			luna.antiraid = True
			luna.printmessage(f"Antiraid: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Antiraid: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif luna.antiraid == True:
			luna.antiraid = False
			luna.printmessage(f"Antiraid: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Antiraid: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "friendsbackup",
					usage="",
					description = "Backup your friendslist")
	async def friendsbackup(self, ctx):
		await ctx.message.delete()
		luna.printevent("Backing up friendslist...")
		friendsamount = 0
		blockedamount = 0
		friendslist = ""
		blockedlist = ""
		for friend in self.bot.user.friends:
			friendslist += f"{friend.name}#{friend.discriminator}\n"
			friendsamount += 1
		file = open("data/backup/friends.txt", "w", encoding='utf-8') 
		file.write(friendslist)
		file.close()
		for block in self.bot.user.blocked:
			blockedlist += f"{block.name}#{block.discriminator}\n"
			blockedamount += 1
		file = open("data/backup/blocked.txt", "w", encoding='utf-8') 
		file.write(blockedlist)
		file.close()

		embed = discord.Embed(title="Friends Backup", description=f"Backed up **{friendsamount}** friends in data/backup/friends.txt\nBacked up **{blockedamount}** blocked users in data/backup/blocked.txt", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "whitelist",
					usage="<@member>",
					description = "Whitelist someone to join while antiraid")
	async def whitelist(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user is None:
			await ctx.send("Please specify a user to whitelist")
		else:
			if ctx.guild.id not in luna.whitelisted_users.keys():
				luna.whitelisted_users[ctx.guild.id] = {}
			if user.id in luna.whitelisted_users[ctx.guild.id]:
				await ctx.send('That user is already whitelisted')
			else:
				luna.whitelisted_users[ctx.guild.id][user.id] = 0
				await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_",
																										"\_") + "#" + user.discriminator + "**")

	@commands.command(name = "unwhitelist",
					usage="",
					description = "Unwhitelist someone")
	async def unwhitelist(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user is None:
			await ctx.send("Please specify the user you would like to unwhitelist")
		else:
			if ctx.guild.id not in luna.whitelisted_users.keys():
				await ctx.send("That user is not whitelisted")
				return
			if user.id in luna.whitelisted_users[ctx.guild.id]:
				luna.whitelisted_users[ctx.guild.id].pop(user.id, 0)
				user2 = self.bot.get_user(user.id)
				await ctx.send(
					'Successfully unwhitelisted **' + user2.name.replace('*', "\*").replace('`', "\`").replace('_',
																											"\_") + '#' + user2.discriminator + '**')

	@commands.command(name = "whitelisted",
					usage="",
					description = "Show the whitelisted list")
	async def whitelisted(self, ctx, g=None):
		await ctx.message.delete()
		if g == '-g' or g == '-global':
			whitelist = '`All Whitelisted Users:`\n'
			for key in luna.whitelisted_users:
				for key2 in luna.whitelisted_users[key]:
					user = self.bot.get_user(key2)
					whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
																								"\_") + "#" + user.discriminator + "** - " + self.bot.get_guild(
						key).name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "" + "\n"
			await ctx.send(whitelist)
		else:
			whitelist = "`" + ctx.guild.name.replace('*', "\*").replace('`', "\`").replace('_',
																						"\_") + '\'s Whitelisted Users:`\n'
			for key in self.bot.whitelisted_users:
				if key == ctx.guild.id:
					for key2 in self.bot.whitelisted_users[ctx.guild.id]:
						user = self.bot.get_user(key2)
						whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
																									"\_") + "#" + user.discriminator + " (" + str(
							user.id) + ")" + "**\n"
			await ctx.send(whitelist)

	@commands.command(name = "clearwhitelist",
					usage="",
					description = "Clear the whitelisted list")
	async def clearwhitelist(self, ctx):
		await ctx.message.delete()
		luna.whitelisted_users.clear()
		embed = discord.Embed(title="Whitelist", url=luna.titleurlvar(), description="Successfully cleared the whitelist", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

def setup(bot:commands.Bot):
	bot.add_cog(ProtectionCog(bot))