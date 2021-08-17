import discord
from discord.ext import commands
import random
import main as luna
import asyncio
import json
import requests
import urllib

def zalgoText(string):
        result = ''

        for char in string:
            for i in range(0, random.randint(20, 40)):
                randBytes = random.randint(0x300, 0x36f).to_bytes(2, 'big')
                char += randBytes.decode('utf-16be')
                i + 1
            result += char
        return result

class TextCog(commands.Cog, name="Text commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "encode",
					usage="",
					description = "Encoding text commands")
	async def encode(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Encode commands')
		commands = cog.get_commands()
		helptext = ""

		if luna.mode() == 2:
			for command in commands:
				if len(command.usage) == 0:
					command.usage = command.usage+""
				else:
					command.usage = command.usage+" "
				helptext+=f"[ {prefix}{command.name} {command.usage}] {command.description}\n"
			sent = await ctx.send(f"```ini\n[ Encoding text ]\n\n{luna.descriptionvar()}{helptext}\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete() 
		else:
			for command in commands:
				helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
			embed = discord.Embed(title="Encoding text", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

	@commands.command(name = "decode",
					usage="",
					description = "Decoding text commands")
	async def decode(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Decode commands')
		commands = cog.get_commands()
		helptext = ""

		if luna.mode() == 2:
			for command in commands:
				if len(command.usage) == 0:
					command.usage = command.usage+""
				else:
					command.usage = command.usage+" "
				helptext+=f"[ {prefix}{command.name} {command.usage}] {command.description}\n"
			sent = await ctx.send(f"```ini\n[ Decoding text ]\n\n{luna.descriptionvar()}{helptext}\n[ {luna.footervar()} ]```")
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()
		else:
			for command in commands:
				helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
			embed = discord.Embed(title="Decoding text", description=f"{luna.descriptionvar()}{helptext}", color=luna.hexcolorvar())
			embed.set_thumbnail(url=luna.imagevar())
			embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
			embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
			embed.set_image(url=luna.largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(luna.deletetimer())
			await sent.delete()

	@commands.command(name = "embed",
					usage="<text>",
					description = "Text in a embed")
	async def embed(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=luna.hexcolorvar())
		await ctx.send(embed=embed)
	
	@commands.command(name = "embed_title",
					usage="<text>",
					description = "Text in a embed (as title)")
	async def embed_title(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(title=luna.titlevar() ,description=f"{text}", color=luna.hexcolorvar())
		await ctx.send(embed=embed)

	@commands.command(name = "embed_thumbnail",
					usage="<text>",
					description = "Text in a embed (with thumbnail)")
	async def embed_thumbnail(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		await ctx.send(embed=embed)

	@commands.command(name = "embed_footer",
					usage="<text>",
					description = "Text in a embed (with footer)")
	async def embed_footer(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=luna.hexcolorvar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		await ctx.send(embed=embed)

	@commands.command(name = "embed_author",
					usage="<text>",
					description = "Text in a embed (with author)")
	async def embed_author(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=luna.hexcolorvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		await ctx.send(embed=embed)

	@commands.command(name = "embed_image",
					usage="<text>",
					description = "Text in a embed (with image)")
	async def embed_image(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=luna.hexcolorvar())
		embed.set_image(url=luna.largeimagevar())
		await ctx.send(embed=embed)

	@commands.command(name = "embed_all",
					usage="<text>",
					description = "Text in a embed (all theme settings)")
	async def embed_all(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=luna.hexcolorvar())
		embed.set_thumbnail(url=luna.imagevar())
		embed.set_footer(text=luna.footervar(), icon_url=luna.footer_iconurlvar())
		embed.set_author(name=luna.authorvar(), url=luna.authorurlvar(), icon_url=luna.author_iconurlvar())
		embed.set_image(url=luna.largeimagevar())
		await ctx.send(embed=embed)

	@commands.command(name = "ascii",
					usage="<text>",
					description = "Ascii text")
	async def ascii(self, ctx, *, text:str):
		await ctx.message.delete()
		r = requests.get(
			f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
		if len('```' + r + '```') > 2000:
			return
		await ctx.send(f"```{r}```")

	@commands.command(name = "vape",
					usage="<text>",
					aliases=['vaporwave'],
					description = "Vaporwave text")
	async def vape(self, ctx, *, text:str):
		await ctx.message.delete()
		text = text.replace('a', 'ａ').replace('A', 'Ａ').replace('b', 'ｂ') \
			.replace('B', 'Ｂ').replace('c', 'ｃ').replace('C', 'Ｃ') \
			.replace('d', 'ｄ').replace('D', 'Ｄ').replace('e', 'ｅ') \
			.replace('E', 'Ｅ').replace('f', 'ｆ').replace('F', 'Ｆ') \
			.replace('g', 'ｇ').replace('G', 'Ｇ').replace('h', 'ｈ') \
			.replace('H', 'Ｈ').replace('i', 'ｉ').replace('I', 'Ｉ') \
			.replace('j', 'ｊ').replace('J', 'Ｊ').replace('k', 'ｋ') \
			.replace('K', 'Ｋ').replace('l', 'ｌ').replace('L', 'Ｌ') \
			.replace('m', 'ｍ').replace('M', 'Ｍ').replace('n', 'ｎ') \
			.replace('N', 'Ｎ').replace('o', 'ｏ').replace('O', 'Ｏ') \
			.replace('p', 'ｐ').replace('P', 'Ｐ').replace('q', 'ｑ') \
			.replace('Q', 'Ｑ').replace('r', 'ｒ').replace('R', 'Ｒ') \
			.replace('s', 'ｓ').replace('S', 'Ｓ').replace('t', 'ｔ') \
			.replace('T', 'Ｔ').replace('u', 'ｕ').replace('U', 'Ｕ') \
			.replace('v', 'ｖ').replace('V', 'Ｖ').replace('w', 'ｗ') \
			.replace('W', 'Ｗ').replace('x', 'ｘ').replace('X', 'Ｘ') \
			.replace('1', '１').replace('2', '２').replace('3', '３') \
			.replace('4', '４').replace('5', '５').replace('6', '６').replace(' ', '　') \
			.replace('7', '７').replace('8', '８').replace('9', '９').replace('0', '０') \
			.replace('?', '？').replace('.', '．').replace('!', '！').replace('[', '［') \
			.replace(']', '］').replace('{', '｛').replace('}', '｝').replace('=', '＝') \
			.replace('(', '（').replace(')', '）').replace('&', '＆').replace('%', '％').replace('"', '＂') \
			.replace('y', 'ｙ').replace('Y', 'Ｙ').replace('z', 'ｚ').replace('Z', 'Ｚ')
		await ctx.send(f'{text}')

	@commands.command(name = "zalgo",
					usage="<text>",
					description = "Zalgo text")
	async def zarlgo(self, ctx, *, text:str):
		await ctx.message.delete()

		await ctx.send(zalgoText(text))

	@commands.command(name = "reverse",
					usage="<text>",
					description = "Reverse given text")
	async def reverse(ctx, *, text):
		await ctx.message.delete()
		text = text[::-1]
		await ctx.send(text)

	@commands.command(name = "bold",
					usage="<text>",
					description = "Bold text format")
	async def bold(self, ctx, *, text:str):
		await ctx.message.delete()
		await ctx.send(f"**{text}**")

	@commands.command(name = "spoiler",
					usage="<text>",
					description = "Spoiler text format")
	async def spoiler(self, ctx, *, text:str):
		await ctx.message.delete()

		await ctx.send(f"||{text}||")

	@commands.command(name = "underline",
					usage="<text>",
					description = "Underline text format")
	async def underline(self, ctx, *, text:str):
		await ctx.message.delete()

		await ctx.send(f"__{text}__")

	@commands.command(name = "strike",
					usage="<text>",
					description = "Strike text format")
	async def strike(self, ctx, *, text:str):
		await ctx.message.delete()

		await ctx.send(f"~~{text}~~")

	@commands.command(name = "css",
					usage="<text>",
					description = "CSS text format")
	async def css(self, ctx, *, text:str):
		await ctx.message.delete()

		await ctx.send(f"```css\n{text}\n```")
	
	@commands.command(name = "brainfuck",
					usage="<text>",
					description = "Brainfuck text format")
	async def brainfuck(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```brainfuck\n{text}\n```")

	@commands.command(name = "md",
					usage="<text>",
					description = "MD text format")
	async def md(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```md\n{text}\n```")

	@commands.command(name = "fix",
					usage="<text>",
					description = "Fix text format")
	async def fix(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```fix\n{text}\n```")

	@commands.command(name = "glsl",
					usage="<text>",
					description = "Glsl text format")
	async def glsl(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```glsl\n{text}\n```")

	@commands.command(name = "diff",
					usage="<text>",
					description = "Diff text format")
	async def diff(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```diff\n{text}\n```")
		
	@commands.command(name = "bash",
					usage="<text>",
					description = "Bash text format")
	async def bash(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```bash\n{text}\n```")
		
	@commands.command(name = "cs",
					usage="<text>",
					description = "CS text format")
	async def cs(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```cs\n{text}\n```")

	@commands.command(name = "ini",
					usage="<text>",
					description = "Ini text format")
	async def ini(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```ini\n{text}\n```")

	@commands.command(name = "asciidoc",
					usage="<text>",
					description = "Asciidoc text format")
	async def asciidoc(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```asciidoc\n{text}\n```")

	@commands.command(name = "autohotkey",
					usage="<text>",
					description = "Autohotkey text format")
	async def autohotkey(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```autohotkey\n{text}\n```")

def setup(bot:commands.Bot):
	bot.add_cog(TextCog(bot))