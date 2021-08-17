import discord
from discord.ext import commands
import main as luna
import asyncio
import json


class ShareCog(commands.Cog, name="Share commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "share",
					usage="<on/off>",
					description = "Share on/off")
	async def share(self, ctx):
		await ctx.message.delete()

		with open('data/sharing.json') as f:
			slot = json.load(f)
		share = slot.get('share')

		if share == "off":
			luna.configshare("on")
			luna.printmessage(f"Share: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")

			if luna.mode() == 2:
				sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nShare: on\n\n[ {luna.footervar()} ]```")
				await asyncio.sleep(luna.deletetimer())
				await sent.delete()
			else:
				embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Share: **on**", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				sent = await ctx.send(embed=embed)
				await asyncio.sleep(luna.deletetimer())
				await sent.delete()

		if share == "on":
			luna.configshare("off")
			luna.printmessage(f"Share: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")

			if luna.mode() == 2:
				sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nShare: off\n\n[ {luna.footervar()} ]```")
				await asyncio.sleep(luna.deletetimer())
				await sent.delete()
			else:
				embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Share: **off**", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				sent = await ctx.send(embed=embed)
				await asyncio.sleep(luna.deletetimer())
				await sent.delete()

	@commands.command(name = "shareuser",
					usage="<@member>",
					description = "Set the member for sharing")
	async def shareuser(self, ctx, user_id):
		await ctx.message.delete()

		if "<@!" and ">" in user_id:
			user_id = user_id.replace("<@!", "").replace(">", "")
			user = await self.bot.fetch_user(user_id)
		else:
			user = await self.bot.fetch_user(user_id)

		print(user.avatar_url)

		if user == self.bot.user:
			if luna.errorlog() == "console":
				luna.printerror("You can't use share on yourself.")
			else:
				if luna.mode() == 2:
					sent = await ctx.send(f"```ini\n[ Error ]\n\nYou can't use share on yourself.\n\n[ {luna.footervar()} ]```")
					await asyncio.sleep(luna.deletetimer())
					await sent.delete()
				else:
					embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"You can't use share on yourself.", color=0xff0000)
					embed.set_thumbnail(url=luna.imagevar())
					embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
					embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
					embed.set_image(url=luna.largeimagevar())
					sent = await ctx.send(embed=embed)
					await asyncio.sleep(luna.deletetimer())
					await sent.delete()
			return

		luna.configshare_userid(user.id)
		luna.printmessage(f"Share user set to: {luna.bcolors.LIGHTMAGENTA}{user}{luna.bcolors.RESET}")

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nShare user set to: {user}\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Share user set to: **{user}**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

	@commands.command(name = "sharenone",
					usage="",
					description = "Set the member for sharing to none")
	async def sharenone(self, ctx):
		await ctx.message.delete()

		luna.configshare_userid("")
		luna.printmessage(f"Share user set to: {luna.bcolors.LIGHTMAGENTA}None{luna.bcolors.RESET}")

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nShare user set to: None\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Share user set to: **None**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

def setup(bot:commands.Bot):
	bot.add_cog(ShareCog(bot))