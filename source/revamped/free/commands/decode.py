from discord.ext import commands
from .encryption import *


class DecodeCog(commands.Cog, name="Decode commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="decode_cea256",
        usage="<key> <text>",
        description="cea256"
    )
    async def decode_cea256(self, luna, key, *, text):

        if len(key) != 32:
            await luna.send("Invalid key, needs to be 256-bits / 32 Chars in length")
            return
        try:
            decrypted = Decryption(key).CEA256(text)
        except BaseException:
            await luna.send("Decryption failed, make sure the key is correct i")
        else:
            await luna.send(f"{decrypted}")

    @commands.command(
        name="decode_base64",
        usage="<text>",
        description="base64"
    )
    async def decode_base64(self, luna, *, text: str):

        dec = base64.b64decode(f'{text}'.encode('ascii'))
        decoded = str(dec)
        decoded = decoded[2:-1]
        await luna.send(f"{decoded}")

    @commands.command(
        name="decode_leet",
        usage="<text>",
        description="leet"
    )
    async def decode_leet(self, luna, *, text: str):

        encoded = text.replace(
            '3',
            'e'
        ).replace(
            '4',
            'a'
        ).replace(
            '!',
            'i'
        ).replace(
            '|_|',
            'u'
        ).replace(
            '|_|',
            'U'
        ).replace(
            '3',
            'E'
        ).replace(
            '!',
            'I'
        ).replace(
            '4',
            'A'
        ).replace(
            '0',
            'o'
        ).replace(
            '0',
            'O'
        ).replace(
            '7',
            't'
        ).replace(
            '7',
            'T'
        ).replace(
            '1',
            'l'
        ).replace(
            '1',
            'L'
        ).replace(
            '|<',
            'k'
        ).replace(
            '|<',
            'K'
        ).replace(
            'X',
            'CK'
        ).replace(
            'x',
            'ck'
        ).replace(
            'X',
            'Ck'
        ).replace(
            'x',
            'cK'
        )
        await luna.send(f"{encoded}")
