from re import search
import discord
from discord.ext import commands
import main as luna
import asyncio
import time

start_animation = False
cyclename = ""

class AnimatedCog(commands.Cog, name="Animated commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
    
	@commands.command(name = "animguild",
						usage="[name]",
						description = "Animates the guild name")
	async def animguild(self, ctx, *, name:str = None):
		await ctx.message.delete()
		global cyclename
		global start_animation
		start_animation = True
		if name is None:
			embed = discord.Embed(title="Animguild", description=f"Animating: {name}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			await luna.send(ctx, embed)
			name = ctx.guild.name.lower() 
			cyclename = name
			length = len(name)
			while start_animation:
				for x in range(length):
					if start_animation == True:
						time.sleep(0.5)
						letter = cyclename[x]
						first_part = cyclename[:x]
						second_part = cyclename[x+1:]
						new_data = first_part + second_part
						if letter == letter.upper():
							await ctx.guild.edit(name=new_data[:x] + letter.lower() + new_data[x:])
						else:
							await ctx.guild.edit(name=new_data[:x] + letter.upper() + new_data[x:])		
					else:
						break
			
		else:
			if len(name) > 3:
				embed = discord.Embed(title="Animguild", description=f"Animating: {name}", color=luna.hexcolorvar())
				embed.set_thumbnail(url=luna.imagevar())
				embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
				embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
				embed.set_image(url=luna.largeimagevar())
				await luna.send(ctx, embed)
				name = ctx.guild.name.lower()
				cyclename = name
				length = len(name)
				while start_animation:
					for x in range(length):
						if start_animation == True:
							time.sleep(0.5)
							letter = cyclename[x]
							first_part = cyclename[:x]
							second_part = cyclename[x+1:]
							new_data = first_part + second_part
							if letter == letter.upper():
								await ctx.guild.edit(name=new_data[:x] + letter.lower() + new_data[x:])
							else:
								await ctx.guild.edit(name=new_data[:x] + letter.upper() + new_data[x:])
						else:
							break
			else:
				if luna.errorlog() == "console":
					luna.printerror("Invalid name length, needs to be over 3 characters long")
				else:
					embed = discord.Embed(title="Error", url=luna.titleurlvar(), description=f"Invalid name length, needs to be over 3 characters long", color=0xff0000)
					embed.set_thumbnail(url=luna.imagevar())
					embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
					embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
					embed.set_image(url=luna.largeimagevar())
					await luna.send(ctx, embed)

	@commands.command(name = "stopanimguild",
						usage="",
						description = "Stops the guild name animation")
	async def stopanimguild(self, ctx, *, name:str = None):
		await ctx.message.delete()
		global start_animation
		start_animation = False
		embed = discord.Embed(title="Animguild", description="Stopped the animation", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "cyclenick",
						usage="<name>",
						description = "Animates the nickname")
	async def cyclenick(self, ctx, *, text):
		await ctx.message.delete()
		embed = discord.Embed(title="Cyclenick", description=f"Animating: {text}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)
		global cycling
		cycling = True
		while cycling:
			name = ""
			for letter in text:
				name = name + letter
				await ctx.message.author.edit(nick=name)


	@commands.command(name = "stopcyclenick",
						usage="",
						description = "Stops the nickname animation")
	async def stopcyclenick(self, ctx):
		await ctx.message.delete()
		global cycling
		cycling = False
		embed = discord.Embed(title="Cyclenick", description="Stopped the animation", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "cyclegroup",
						usage="<name>",
						description = "Animates the group name")
	async def cyclegroup(self, ctx, *, text):
		await ctx.message.delete()
		embed = discord.Embed(title="Cyclegroup", description=f"Animating: {text}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)
		global cycling_group
		cycling_group = True
		while cycling:
			name = ""
			for letter in text:
				name = name + letter
				await ctx.message.channel.edit(name=name)


	@commands.command(name = "stopcyclegroup",
						usage="",
						description = "Stops the group name animation")
	async def stopcyclegroup(self, ctx):
		await ctx.message.delete()
		global cycling_group
		cycling_group = False
		embed = discord.Embed(title="Cyclegroup", description="Stopped the animation", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await luna.send(ctx, embed)

	@commands.command(name = "virus",
				usage="[@member] <virus>",
				description = "Animated virus message")
	async def virus(self, ctx, user: discord.Member = None, *, virus: str = "trojan"):
		user = user or ctx.author
		list = (
		    f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
		    f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
		    f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
		    f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
		    f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
		    f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
		    f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
		    f"``Successfully downloaded {virus}-virus.exe``",
		    "``Injecting virus.   |``",
		    "``Injecting virus..  /``",
		    "``Injecting virus... -``",
		    f"``Successfully Injected {virus}-virus.exe into {user.name}``",
		)
		for i in list:
		    await asyncio.sleep(1.5)
		    await ctx.message.edit(content=i)

	@commands.command(name = "cathi",
						usage="[text]",
						description = "Cute cat animation")
	async def cathi(self, ctx, *, text: str = "Hi..."):
		list = (
			"""ຸ 　　　＿＿_＿＿
	　／　／　  ／|"
	　|￣￣￣￣|　|
	　|　　　　|／
	　￣￣￣￣""",
			f"""ຸ 　　　{text}
	　   　∧＿∧＿_
	　／(´･ω･`)  ／＼
	／|￣￣￣￣|＼／
	　|　　　　|／
	　￣￣￣￣""",
		)
		for i in range(3):
			for cat in list:
				await asyncio.sleep(2)
				await ctx.message.edit(content=cat)

	@commands.command(name = "flop",
						usage="",
						description = "Flop animation")
	async def flop(self, ctx):
		list = (
			"(   ° - °) (' - '   )",
			"(\\\° - °)\ (' - '   )",
			"(—°□°)— (' - '   )",
			"(╯°□°)╯(' - '   )",
			"(╯°□°)╯︵(\\\ .o.)\\",
		)
		for i in list:
			await asyncio.sleep(2)
			await ctx.message.edit(content=i)

	@commands.command(name = "poof",
						usage="",
						description = "Poof animation")
	async def poof(self, ctx):
		list = ("(   ' - ')", "' - ')", "- ')", "')", ")", "*poofness*")
		for i in list:
			await asyncio.sleep(2)
			await ctx.message.edit(content=i)

	@commands.command(name = "boom",
						usage="",
						description = "Boom animation")
	async def boom(self, ctx):
		list = (
			"```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
			"💣",
			"💥",
		)
		for i in list:
			await asyncio.sleep(2)
			await ctx.message.edit(content=i)

	@commands.command(name = "tableflip",
						usage="",
						description = "Tableflip/rage animation")
	async def tableflip(self, ctx):
		list = (
			"`(\°-°)\  ┬─┬`",
			"`(\°□°)\  ┬─┬`",
			"`(-°□°)-  ┬─┬`",
			"`(╯°□°)╯    ]`",
			"`(╯°□°)╯     ┻━┻`",
			"`(╯°□°)╯       [`",
			"`(╯°□°)╯          ┬─┬`",
			"`(╯°□°)╯                 ]`",
			"`(╯°□°)╯                  ┻━┻`",
			"`(╯°□°)╯                         [`",
			"`(\°-°)\                               ┬─┬`",
		)
		for i in list:
			await asyncio.sleep(2)
			await ctx.message.edit(content=i)

	@commands.command(name = "warning",
						usage="",
						description = "System overload warning animation")
	async def warning(self, ctx):
		list = (
			"`LOAD !! WARNING !! SYSTEM OVER`",
			"`OAD !! WARNING !! SYSTEM OVERL`",
			"`AD !! WARNING !! SYSTEM OVERLO`",
			"`D !! WARNING !! SYSTEM OVERLOA`",
			"`! WARNING !! SYSTEM OVERLOAD !`",
			"`WARNING !! SYSTEM OVERLOAD !!`",
			"`ARNING !! SYSTEM OVERLOAD !! W`",
			"`RNING !! SYSTEM OVERLOAD !! WA`",
			"`NING !! SYSTEM OVERLOAD !! WAR`",
			"`ING !! SYSTEM OVERLOAD !! WARN`",
			"`NG !! SYSTEM OVERLOAD !! WARNI`",
			"`G !! SYSTEM OVERLOAD !! WARNIN`",
			"`!! SYSTEM OVERLOAD !! WARNING`",
			"`! SYSTEM OVERLOAD !! WARNING !`",
			"`SYSTEM OVERLOAD !! WARNING !!`",
			"`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
			"`WARNING !! SYSTEM OVERLOAD !!`",
			"`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
			"`SYSTEM OVERLOAD !! WARNING !!`",
			"`IMMINENT SHUT-DOWN IN 0.01 SEC!`",
			"`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`",
			"`CTRL + R FOR MANUAL OVERRIDE..`",
		)
		for i in list:
			await asyncio.sleep(2)
			await ctx.message.edit(content=i)

def setup(bot:commands.Bot):
	bot.add_cog(AnimatedCog(bot))