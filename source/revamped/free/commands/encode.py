import hashlib

from discord.ext import commands
from .encryption import *


class EncodeCog(commands.Cog, name="Encode commands"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(
        name="encode_cea256",
        usage="<key> <text>",
        description="cea256"
    )
    async def encode_cea256(self, luna, key, *, text):
        if len(key) != 32:
            await luna.send("Invalid key, needs to be 256-bits / 32 Chars in length")
            return
        encoded = Encryption(key).CEA256(text)
        await luna.send(f"{encoded}")

    @commands.command(
        name="encode_base64",
        usage="<text>",
        description="base64"
    )
    async def encode_base64(self, luna, *, text: str):
        enc = base64.b64encode(f'{text}'.encode('ascii'))
        encoded = str(enc)
        encoded = encoded[2:-1]
        await luna.send(f"{encoded}")

    @commands.command(
        name="encode_leet",
        usage="<text>",
        description="leet"
    )
    async def encode_leet(self, luna, *, text: str):
        encoded = text.replace(
            'e',
            '3'
        ).replace(
            'a',
            '4'
        ).replace(
            'i',
            '!'
        ).replace(
            'u',
            '|_|'
        ).replace(
            'U',
            '|_|'
        ).replace(
            'E',
            '3'
        ).replace(
            'I',
            '!'
        ).replace(
            'A',
            '4'
        ).replace(
            'o',
            '0'
        ).replace(
            'O',
            '0'
        ).replace(
            't',
            '7'
        ).replace(
            'T',
            '7'
        ).replace(
            'l',
            '1'
        ).replace(
            'L',
            '1'
        ).replace(
            'k',
            '|<'
        ).replace(
            'K',
            '|<'
        ).replace(
            'CK',
            'X'
        ).replace(
            'ck',
            'x'
        ).replace(
            'Ck',
            'X'
        ).replace(
            'cK',
            'x'
        )
        await luna.send(f"{encoded}")

    @commands.command(
        name="encode_md5",
        usage="<text>",
        description="md5 (oneway)"
    )
    async def encode_md5(self, luna, *, text: str):
        enc = hashlib.md5(text.encode())
        encoded = enc.hexdigest()
        await luna.send(f"{encoded}")

    @commands.command(
        name="encode_sha1",
        usage="<text>",
        description="sha1 (oneway)"
    )
    async def encode_sha1(self, luna, *, text: str):
        enc = hashlib.sha1(text.encode())
        encoded = enc.hexdigest()
        await luna.send(f"{encoded}")

    @commands.command(
        name="encode_sha224",
        usage="<text>",
        description="sha224 (oneway)"
    )
    async def encode_sha224(self, luna, *, text: str):
        enc = hashlib.sha3_224(text.encode())
        encoded = enc.hexdigest()
        await luna.send(f"{encoded}")

    @commands.command(
        name="encode_sha256",
        usage="<text>",
        description="sha256 (oneway)"
    )
    async def encode_sha256(self, luna, *, text: str):
        enc = hashlib.sha3_256(text.encode())
        encoded = enc.hexdigest()
        await luna.send(f"{encoded}")

    @commands.command(
        name="encode_sha384",
        usage="<text>",
        description="sha384 (oneway)"
    )
    async def encode_sha384(self, luna, *, text: str):
        enc = hashlib.sha3_384(text.encode())
        encoded = enc.hexdigest()
        await luna.send(f"{encoded}")

    @commands.command(
        name="encode_sha512",
        usage="<text>",
        description="sha512 (oneway)"
    )
    async def encode_sha512(self, luna, *, text: str):
        enc = hashlib.sha3_512(text.encode())
        encoded = enc.hexdigest()
        await luna.send(f"{encoded}")