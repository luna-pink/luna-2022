import discord
from discord.ext import commands
import time
import main as luna
import asyncio

class ToastsCog(commands.Cog, name="Toast commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
	
	@commands.command(name = "toasts",
					usage="<on/off>",
					description = "Turn toasts on or off")
	async def toasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoasttoasts("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoasttoasts("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "logintoasts",
					usage="<on/off>",
					description = "Turn login toasts on or off")
	async def logintoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Login toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastlogin("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Login toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Login toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastlogin("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Login toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "nitrotoasts",
					usage="<on/off>",
					description = "Turn nitro toasts on or off")
	async def nitrotoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Nitro toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastnitro("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Nitro toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Nitro toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastnitro("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Nitro toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "giveawaytoasts",
					usage="<on/off>",
					description = "Turn giveaway toasts on or off")
	async def giveawaytoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Giveaway toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastgiveaway("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Giveaway toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Giveaway toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastgiveaway("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Giveaway toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "privnotetoasts",
					usage="<on/off>",
					description = "Turn privnote toasts on or off")
	async def privnotetoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Privnote toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastprivnote("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Privnote toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Privnote toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastprivnote("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Privnote toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "slotbottoasts",
					usage="<on/off>",
					description = "Turn slotbot toasts on or off")
	async def slotbottoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Slotbot toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastslotbot("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Slotbot toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Slotbot toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastslotbot("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Slotbot toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "selfbottoasts",
					usage="<on/off>",
					description = "Turn selfbot toasts on or off")
	async def selfbottoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Selfbot toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastselfbot("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Selfbot toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Selfbot toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastselfbot("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Selfbot toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "pingtoasts",
					usage="<on/off>",
					description = "Turn ping toasts on or off")
	async def pingtoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Ping toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastpings("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Ping toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Ping toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastpings("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Ping toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "ghostpingtoasts",
					usage="<on/off>",
					description = "Turn ghostping toasts on or off")
	async def ghostpingtoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Ghostping toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastghostpings("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Ghostping toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Ghostping toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastghostpings("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Ghostping toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "friendtoasts",
					usage="<on/off>",
					description = "Turn friendevent toasts on or off")
	async def friendtoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Friendevent toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastfriendevents("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Friendevent toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Friendevent toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastfriendevents("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Friendevent toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "guildtoasts",
					usage="<on/off>",
					description = "Turn guildevent toasts on or off")
	async def guildtoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Guildevent toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastguildevents("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Guildevent toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Guildevent toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastguildevents("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Guildevent toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "roletoasts",
					usage="<on/off>",
					description = "Turn roleupdate toasts on or off")
	async def roletoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Roleupdate toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastroleupdates("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Roleupdate toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Roleupdate toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastroleupdates("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Roleupdate toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "nicktoasts",
					usage="<on/off>",
					description = "Turn nicknameupdate toasts on or off")
	async def nicktoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Nicknameupdate toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastnickupdates("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Nicknameupdate toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Nicknameupdate toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastnickupdates("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Nicknameupdate toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

	@commands.command(name = "protectiontoasts",
					usage="<on/off>",
					description = "Turn protection toasts on or off")
	async def protectiontoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			luna.printmessage(f"Protection toasts: {luna.bcolors.LIGHTMAGENTA}on{luna.bcolors.RESET}")
			luna.configtoastprotection("on")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Protection toasts: **on**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)

		elif mode == "off":
			luna.printmessage(f"Protection toasts: {luna.bcolors.LIGHTMAGENTA}off{luna.bcolors.RESET}")
			luna.configtoastprotection("off")

			embed = discord.Embed(title=luna.titlevar(), url=luna.titleurlvar(), description=f"Protection toasts: **off**", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"That mode does not exist!\nOnly **on** or **off**", color=0xff0000)
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)


def setup(bot:commands.Bot):
	bot.add_cog(ToastsCog(bot))