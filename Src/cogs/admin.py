import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import main as luna
import asyncio


class AdminCog(commands.Cog, name="Administrative commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "purge",
					usage="<amount>",
					description = "Purge the channel")
	async def purge(self, ctx, amount: int):
		await ctx.message.delete()
		async for message in ctx.message.channel.history(limit=amount):
			try:
				await message.delete()
			except:
				pass

	@commands.command(name = "whois",
					usage="<@member>",
					description = "Show information about given user")
	async def whois(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user is None:
			user = ctx.author

		if user.id == 406907871998246924:
			special = "\n\nSpecial: Founder / Head Dev @ Team Lolicon"
		elif user.id == 717120702158864415 or user.id == 465275771523563531 or user.id == 663516459837685770 or user.id == 288433475831332894:
			special = "\n\nSpecial: Member of Team Lolicon"
		elif user.id == 429333655610064899 or user.id == 510711456153731083:
			special = "\n\nSpecial: Lolicon Beta"
		elif user.id == 254994687444779008:
			special = "\n\nSpecial: First Lolicon Customer"
		else:
			special = ""

		date_format = "%a, %d %b %Y %I:%M %p"
		members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
		role_string = ' '.join([r.mention for r in user.roles][1:])
		perm_string = ', '.join([str(p[0]).replace("_", " ").title()for p in user.guild_permissions if p[1]])

		embed = discord.Embed(description=f"{user.mention}\n\nJoined: {user.joined_at.strftime(date_format)}\nJoin position: {members.index(user) + 1}\nRegistered: {user.created_at.strftime(date_format)}\n\nRoles Amount: {len(user.roles) - 1}\nRoles: {role_string}\n\nPermissions: {perm_string}{special}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_footer(text=f"ID: {user.id}")
		embed.set_author(name=str(user), icon_url=user.avatar_url)
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)
        
	@commands.command(name = "ban",
					usage="<@member>",
					description = "Bans a user")
	@has_permissions(ban_members=True)
	async def ban(self, ctx, user: discord.Member = None, *, reason: str = None):
		await ctx.message.delete()

		if user == None:
			embed = discord.Embed(title="Ban Error", url=luna.titleurlvar(), description=f"Who do you want banned? Please mention an user.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
			return
		elif user == ctx.author:
			embed = discord.Embed(title="Ban Error", url=luna.titleurlvar(), description=f"You can't ban yourself, Please mention someone else.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
			return
		else:
			pass
		try:
			await user.ban(reason=reason)
			embed = discord.Embed(title="Ban", url=luna.titleurlvar(), description=f"User {user.mention}({user.id}) has been banned.\n\nReason: {reason}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		except Exception as e:
			luna.printerror(e)

	@commands.command(name = "unban",
					usage="<user_id>",
					description = "Unban a user")
	@has_permissions(ban_members=True)
	async def unban(self, ctx, user: discord.Member = None):
		await ctx.message.delete()

		if user == None:
			embed = discord.Embed(title="Ban Error", url=luna.titleurlvar(), description=f"Who do you want unbanned? Please specify the user id.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
			return
		elif user == ctx.author:
			embed = discord.Embed(title="Ban Error", url=luna.titleurlvar(), description=f"You can't unban yourself, Please specify someone elses user id.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
			return
		else:
			pass
		try:
			user1 = await self.bot.fetch_user(user)
			await ctx.guild.unban(user1)
			embed = discord.Embed(title="Ban", url=luna.titleurlvar(), description=f"User {user.mention} ({user.id}) has been unbanned.", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		except Exception as e:
			luna.printerror(e)

	@commands.command(name = "kick",
					usage="<@member>",
					description = "Kicks a user")
	@has_permissions(kick_members=True)
	async def kick(self, ctx, user: discord.Member = None, *, reason: str = None):
		await ctx.message.delete()

		if user == None:
			if luna.errorlog() == "console":
				luna.printerror("Who do you want kicked? Please mention an user")
			else:
				embed = discord.Embed(title="Kick Error", url=luna.titleurlvar(), description=f"Who do you want Kicked? Please mention an user.", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
				return
		elif user == ctx.author:
			if luna.errorlog() == "console":
				luna.printerror("You can't kick yourself, Please mention someone else")
			else:
				embed = discord.Embed(title="Kick Error", url=luna.titleurlvar(), description=f"You can't kick yourself, Please mention someone else.", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
				return
		else:
			pass
		try:
			await user.kick(reason=reason)
			embed = discord.Embed(title="Kick", url=luna.titleurlvar(), description=f"User {user.mention} ({user.id}) has been kicked.\n\nReason: {reason}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		except Exception as e:
			luna.printerror(e)

	@commands.command(name = "kickgc",
					usage="",
					description = "Remove everyone in the group channel")
	async def kickgc(self, ctx):
		await ctx.message.delete()
		if isinstance(ctx.message.channel, discord.GroupChannel):
			for recipient in ctx.message.channel.recipients:
				await ctx.message.channel.remove_recipients(recipient)

	@commands.command(name = "leavegc",
					usage="",
					description = "Leave the group channel")
	async def leavegc(self, ctx):
		await ctx.message.delete()
		if isinstance(ctx.message.channel, discord.GroupChannel):
			await ctx.message.channel.leave()

	@commands.command(name = "servername",
					usage="<name>",
					description = "Change the servername")
	async def servername(self, ctx, *, name:str):
		await ctx.message.delete()
		await ctx.guild.edit(name=name)
		embed = discord.Embed(title="Servername", url=luna.titleurlvar(), description=f"Successfully changed the servername to: {name}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "nickall",
					usage="<name>",
					description = "Change the nickname of every member in the server")
	async def nickall(self, ctx, *, name:str):
		await ctx.message.delete()
		for user in list(ctx.guild.members):
			try:
				await user.edit(nick=name)
			except:
				pass
		embed = discord.Embed(title="Nickall", url=luna.titleurlvar(), description=f"Successfully changed the nickname of every member to: {name}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "renamechannels",
					usage="<name>",
					description = "Change the name of every channel")
	async def renamechannels(self, ctx, *, name):
		await ctx.message.delete()
		for channel in ctx.guild.channels:
			await channel.edit(name=name)


def setup(bot:commands.Bot):
	bot.add_cog(AdminCog(bot))