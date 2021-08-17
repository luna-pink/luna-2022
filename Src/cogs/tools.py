import asyncio
import discord
import main as luna
from discord.ext import commands
from gtts import gTTS
import os
import json

class ToolsCog(commands.Cog, name="Tools commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "poll",
					usage="<question>",
					description = "Create a poll")
	async def poll(self, ctx, *, question):
		await ctx.message.delete()
		embed = discord.Embed(title=f"Poll", description=f"{question}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		message = await ctx.send(embed=embed)
		await message.add_reaction('👍')
		await message.add_reaction('👎')

	@commands.command(name = "cpoll",
					usage="<option1> <option2> <question>",
					description = "Create a poll")
	async def cpoll(self, ctx, option1, option2, *, poll):
		await ctx.message.delete()
		embed = discord.Embed(title=f"Poll", description=f"{poll}\n\n🅰️ = {option1}\n🅱️ = {option2}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		message = await ctx.send(embed=embed)
		await message.add_reaction('🅰️')
		await message.add_reaction('🅱️')

	@commands.command(name = "hiddenping",
					usage="<channel_id> <user_id> <message>",
					description = "Ping someone without showing @member")
	async def hiddenping(self, ctx, channel_id: int, user_id, *, message):
		await ctx.message.delete()

		if user_id == "@everyone" or user_id == "everyone":
			user = "@everyone"
		elif len(user_id) == 18:
			user = "<" + "@" + user_id + ">"
		elif len(user_id) == 19:
			user = "<" + user_id + ">"
		else:
			luna.printerror("Invalid User!")

		cuser = await self.bot.fetch_user(user_id)
		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + user)

		embed = discord.Embed(title=f"Hidden Ping", description=f"Ping sent!\n\nChannel ID: {cchannel}\nChannel Name: {channel.name}\nUser ID: {user_id}\nUser Name: {cuser.name}#{cuser.discriminator}\nMessage: {message}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "hiddeneveryone",
					usage="<channel_id> <message>",
					description = "Ping everyone without showing @everyone")
	async def hiddeneveryone(self, ctx, channel_id: int, *, message):
		await ctx.message.delete()

		user = "@everyone"

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + user)

		embed = discord.Embed(title=f"Hidden Everyone", description=f"Ping sent!\n\nChannel ID: {channel_id}\nChannel Name: {cchannel.name}\nMessage: {message}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "hiddeninvite",
					usage="<channel_id> <invite> <message>",
					description = "hide the invite")
	async def hiddeninvite(self, ctx, channel_id: int, invite, *, message):
		await ctx.message.delete()

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + invite)

		embed = discord.Embed(title=f"Hidden Ping", description=f"Ping sent!\n\nChannel ID: {cchannel}\nChannel Name: {channel.name}\nInvite: {invite}\nMessage: {message}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "hiddenurl",
					usage="<channel_id> <url> <message>",
					description = "Hide the url")
	async def hiddenurl(self, ctx, channel_id: int, url, *, message):
		await ctx.message.delete()

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + url)

		embed = discord.Embed(title=f"Hidden Ping", description=f"Ping sent!\n\nChannel ID: {cchannel}\nChannel Name: {channel.name}\nURL: {url}\nMessage: {message}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "channels",
					usage="[guild_id]",
					description = "Show all the channels")
	async def channels(self, ctx, server_id:int=None):
		await ctx.message.delete()
		if server_id is None:
			server = discord.utils.get(ctx.bot.guilds, id=ctx.guild.id)
		else: 
			server = discord.utils.get(ctx.bot.guilds, id=server_id)
		channels = server.channels
		channel_list = []
		for channel in channels:
			channel_list.append(channel)
		embed = discord.Embed(title=f"Channels in {server}", description='\n'.join([f"{ch.name}" for ch in channel_list]) or 'None', color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "firstmsg",
					usage="[#channel]",
					description = "Shows the first message in the channel")
	async def firstmsg(self, ctx, channel: discord.TextChannel = None):
		await ctx.message.delete()
		if channel is None:
			channel = ctx.channel
		first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
		embed = discord.Embed(title="First Message", description=f"[Jump]({first_message.jump_url})", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "compareservers",
					usage="<serverid1> <serverid2>",
					description = "Checks if members are in the same server")
	async def compareservers(self, ctx, server_id:int, server_id_2:int):
		await ctx.message.delete()

		server_1 = self.bot.get_guild(server_id)
		server_2 = self.bot.get_guild(server_id_2)
		output = ""
		count = 0
		for member in server_1.members:
			if member in server_2.members:
				output += "{}\n".format(str(member.mention))
				count += 1

		embed = discord.Embed(title=f"Members in the same server: {count}", url=luna.titleurlvar(), description=f"**{server_1}** - **{server_2}**\n\n{output}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "bots",
					usage="",
					description = "Show all bots in the guild")
	async def bots(self, ctx):
		await ctx.message.delete()
		bots = []
		for member in ctx.guild.members:
			if member.bot:
				bots.append(str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
		botslist = f"{', '.join(bots)}".replace(',', "\n")
		embed = discord.Embed(title=f"Bots ({len(bots)})", url=luna.titleurlvar(), description=f"{botslist}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "guildicon",
					usage="",
					description = "Show the guild icon")
	async def guildicon(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title=ctx.guild.name, url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=ctx.guild.icon_url)
		await luna.send(ctx, embed)

	@commands.command(name = "guildbanner",
					usage="",
					description = "Show the guild banner")
	async def guildbanner(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title=ctx.guild.name, url=luna.titleurlvar(), color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=ctx.guild.banner_url)
		await luna.send(ctx, embed)

	@commands.command(name = "tts",
					usage="<language> <text>",
					description = "Show all the channels")
	async def tts(self, ctx, lang, *, text: str):
		await ctx.message.delete()
		tts = gTTS(text, lang=lang)
		filename = f'{text}.mp3'
		tts.save(filename)
		await ctx.send(file=discord.File(fp=filename, filename=filename))
		if os.path.exists(filename):
			os.remove(filename)
	

def setup(bot:commands.Bot):
	bot.add_cog(ToolsCog(bot))
