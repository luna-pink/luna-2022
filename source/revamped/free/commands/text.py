import urllib

from discord.ext import commands
from .utilities import *


class TextCog(commands.Cog, name="Text commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="encode",
        usage="",
        description="Encoding text commands"
    )
    async def encode(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)

        cog = self.bot.get_cog('Encode commands')
        commands = cog.get_commands()
        helptext = ""
        for command in commands:
            helptext += f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

        embed = discord.Embed(
            title="Encode Text",

            description=f"{theme.description()}```\n{helptext}```"
        )

        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="decode",
        usage="",
        description="Decoding text commands"
    )
    async def decode(self, luna):

        prefix = files.json("data/config.json", "prefix", documents=False)

        cog = self.bot.get_cog('Decode commands')
        commands = cog.get_commands()
        helptext = ""
        for command in commands:
            helptext += f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

        embed = discord.Embed(
            title="Decode Text",

            description=f"{theme.description()}```\n{helptext}```"
        )

        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="indent",
        usage="<text>",
        description="Text in a embed"
    )
    async def indent(self, luna, *, text: str):

        embed = discord.Embed(description=f"{text}")
        await send(luna, embed)

    @commands.command(
        name="indent_title",
        usage="<text>",
        description="Text in a embed"
    )
    async def indent_title(self, luna, *, text: str):

        embed = discord.Embed(
            title=theme.title(),
            description=f"{text}"
        )
        await send(luna, embed)

    @commands.command(
        name="indent_footer",
        usage="<text>",
        description="Text in a embed"
    )
    async def indent_footer(self, luna, *, text: str):

        embed = discord.Embed(description=f"{text}")
        embed.set_footer(text=theme.footer())
        await send(luna, embed)

    @commands.command(
        name="indent_all",
        usage="<text>",
        description="Text in a embed"
    )
    async def indent_all(self, luna, *, text: str):

        embed = discord.Embed(description=f"{text}")

        embed.set_footer(text=theme.footer())

        await send(luna, embed)

    @commands.command(
        name="ascii",
        usage="<text>",
        description="Ascii text"
    )
    async def ascii(self, luna, *, text: str):

        r = requests.get(
            f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}'
        ).text
        if len(f'```{r}```') > 2000:
            return
        await luna.send(f"```{r}```")

    @commands.command(
        name="vape",
        usage="<text>",
        aliases=['vaporwave'],
        description="Vaporwave text"
    )
    async def vape(self, luna, *, text: str):

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
        await luna.send(f'{text}')

    @commands.command(
        name="zalgo",
        usage="<text>",
        description="Zalgo text"
    )
    async def zarlgo(self, luna, *, text: str):

        await luna.send(zalgoText(text))

    @commands.command(
        name="reverse",
        usage="<text>",
        description="Reverse given text"
    )
    async def reverse(luna, *, text):

        text = text[::-1]
        await luna.send(text)

    @commands.command(
        name="bold",
        usage="<text>",
        description="Bold codeblock"
    )
    async def bold(self, luna, *, text: str):

        await luna.send(f"**{text}**")

    @commands.command(
        name="spoiler",
        usage="<text>",
        description="Spoiler codeblock"
    )
    async def spoiler(self, luna, *, text: str):

        await luna.send(f"||{text}||")

    @commands.command(
        name="underline",
        usage="<text>",
        description="Underline codeblock"
    )
    async def underline(self, luna, *, text: str):

        await luna.send(f"__{text}__")

    @commands.command(
        name="strike",
        usage="<text>",
        description="Strike codeblock"
    )
    async def strike(self, luna, *, text: str):

        await luna.send(f"~~{text}~~")