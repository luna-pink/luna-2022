import discord
from discord.ext import commands
import string
import main as luna
import asyncio
import random

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

class TrollCog(commands.Cog, name="Troll commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "ghostping",
					usage="<@member>",
					aliases=['gp'],
					description = "Ghostping someone")
	async def ghostping(self, ctx):
		await ctx.message.delete()
        
	@commands.command(name = "empty",
					usage="",
					description = "Sends a empty message")
	async def empty(self, ctx):
		await ctx.message.delete()
		await ctx.send("​")

	@commands.command(name = "copy",
					usage="<@member>",
					aliases=['copycat'],
					description = "Copy every message a member")
	async def copy(self, ctx, member:discord.User):
		await ctx.message.delete()

		luna.copycat = member
		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nNow copying {luna.copycat}\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Now copying {luna.copycat}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

	@commands.command(name = "stopcopy",
					usage="",
					aliases=['stopcopycat'],
					description = "Copy every message a member")
	async def stopcopy(self, ctx):
		await ctx.message.delete()

		if luna.copycat is None:
			if luna.mode() == 2:
				sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nNo one was getting copied.\n\n[ {luna.footervar()} ]```")
				await asyncio.sleep(luna.deletetimer())
				await sent.delete()
			else:
				embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"No one was getting copied.", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				sent = await ctx.send(embed=embed)
				await asyncio.sleep(luna.deletetimer())
				await sent.delete()
			return

		if luna.mode() == 2:
			sent = await ctx.send(f"```ini\n[ {luna.titlevar()} ]\n\nStopped copying {luna.copycat}\n\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Stopped copying {luna.copycat}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

		luna.copycat = None

	@commands.command(name = "fakenitro",
					usage="[amount]",
					description = "Generate fake nitro links")
	async def fakenitro(self, ctx, amount: int = None):
		await ctx.message.delete()
		try:
			if amount is None:
				await ctx.send(Nitro())
			else:
				for each in range(0, amount):
					await ctx.send(Nitro())
		except Exception as e:
			await ctx.send(f"Error: {e}")

	@commands.command(name = "trollnitro",
					usage="",
					description = "Send a used nitro link")
	async def trollnitro(self, ctx):
		await ctx.message.delete()
		await ctx.send("https://discord.gift/6PWNmA6NTuRkejaP")

	@commands.command(name = "mreact",
					usage="",
					description = "Mass spams reacts on latest message")
	async def mreact(self, ctx):
	    await ctx.message.delete()
	    messages = await ctx.message.channel.history(limit=1).flatten()
	    for message in messages:
	        await message.add_reaction("😂")
	        await message.add_reaction("😡")
	        await message.add_reaction("🤯")
	        await message.add_reaction("👍")
	        await message.add_reaction("👎")
	        await message.add_reaction("💯")
	        await message.add_reaction("🍑")
	        await message.add_reaction("❗")
	        await message.add_reaction("🥳")
	        await message.add_reaction("👏")
	        await message.add_reaction("🔞")
	        await message.add_reaction("🇫")
	        await message.add_reaction("🥇")
	        await message.add_reaction("🤔")
	        await message.add_reaction("💀")
	        await message.add_reaction("❤️")

	@commands.command(name = "fakenuke",
					usage="",
					description = "Fakenuke")
	async def fakenuke(self, ctx):
		await ctx.message.delete()
		message = await ctx.send(content=':bomb: :bomb: Nuking this server in 5 :rotating_light:')
		await asyncio.sleep(1)
		await message.edit(content='0')
		await asyncio.sleep(1)
		await message.edit(content='1')
		await asyncio.sleep(1)
		await message.edit(content='2')
		await asyncio.sleep(1)
		await message.edit(content='3')
		await asyncio.sleep(1)
		await message.edit(content='4')
		await asyncio.sleep(1)
		await message.edit(content='This server will be destoyed now')
		await asyncio.sleep(1)
		await message.edit(content=':bomb:')
		await asyncio.sleep(1)
		await message.edit(content=':boom:')
		await asyncio.sleep(1)
		await message.edit(content='Shouldn\'t have even created it ig')
		await asyncio.sleep(1)
		await message.edit(content=':bomb: :bomb:')
		await asyncio.sleep(1)
		await message.edit(content=':boom: :boom:')
		await asyncio.sleep(1)
		await message.edit(content='You will wish you never lived to know about discord')
		await asyncio.sleep(1)
		await message.edit(content=':bomb: :bomb: :bomb:')
		await asyncio.sleep(1)
		await message.edit(content=':boom: :boom: :boom:')
		await asyncio.sleep(1)
		await message.edit(content='There it comes...')
		await asyncio.sleep(1)
		await message.edit(content='https://giphy.com/gifs/rick-roll-lgcUUCXgC8mEo')


def setup(bot:commands.Bot):
	bot.add_cog(TrollCog(bot))