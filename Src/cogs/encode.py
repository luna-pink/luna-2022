from discord.ext import commands
import base64
import hashlib
import CEA256
from CEA256 import *

class EncodeCog(commands.Cog, name="Encode commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "encode_cea256", usage = "<key> <text>", description = "Encode a text with cea256 encryption")  # Encryption made by Exodus <3 
	async def encode_cea256(self, ctx, key, *, text):
		await ctx.message.delete()
		if len(key) != 32:
			await ctx.send("Invalid key, needs to be 256-bits / 32 Chars in length")
			return
		encoded = Encryption(key).CEA256(text)
		await ctx.send(f"{encoded}")

	@commands.command(name = "encode_base64",
					usage="<text>",
					description = "Encode a text with base64")
	async def encode_base64(self, ctx, *, text:str):
		await ctx.message.delete()
		enc = base64.b64encode('{}'.format(text).encode('ascii'))
		encoded = str(enc)
		encoded = encoded[2:len(encoded)-1]
		await ctx.send(f"{encoded}")

	@commands.command(name = "encode_leet",
					usage="<text>",
					description = "Encode a text with leet")
	async def encode_leet(self, ctx, *, text:str):
		await ctx.message.delete()
		encoded = text.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')
		await ctx.send(f"{encoded}")

	@commands.command(name = "encode_md5",
					usage="<text>",
					description = "Encode a text with md5 (oneway)")
	async def encode_md5(self, ctx, *, text:str):
		await ctx.message.delete()
		enc = hashlib.md5(text.encode())
		encoded = enc.hexdigest()
		await ctx.send(f"{encoded}")

	@commands.command(name = "encode_sha1",
					usage="<text>",
					description = "Encode a text with sha1 (oneway)")
	async def encode_sha1(self, ctx, *, text:str):
		await ctx.message.delete()
		enc = hashlib.sha1(text.encode())
		encoded = enc.hexdigest()
		await ctx.send(f"{encoded}")

	@commands.command(name = "encode_sha224",
					usage="<text>",
					description = "Encode a text with sha224 (oneway)")
	async def encode_sha224(self, ctx, *, text:str):
		await ctx.message.delete()
		enc = hashlib.sha3_224(text.encode())
		encoded = enc.hexdigest()
		await ctx.send(f"{encoded}")

	@commands.command(name = "encode_sha256",
					usage="<text>",
					description = "Encode a text with sha256 (oneway)")
	async def encode_sha256(self, ctx, *, text:str):
		await ctx.message.delete()
		enc = hashlib.sha3_256(text.encode())
		encoded = enc.hexdigest()
		await ctx.send(f"{encoded}")

	@commands.command(name = "encode_sha384",
					usage="<text>",
					description = "Encode a text with sha384 (oneway)")
	async def encode_sha384(self, ctx, *, text:str):
		await ctx.message.delete()
		enc = hashlib.sha3_384(text.encode())
		encoded = enc.hexdigest()
		await ctx.send(f"{encoded}")

	@commands.command(name = "encode_sha512",
					usage="<text>",
					description = "Encode a text with sha512 (oneway)")
	async def encode_sha512(self, ctx, *, text:str):
		await ctx.message.delete()
		enc = hashlib.sha3_512(text.encode())
		encoded = enc.hexdigest()
		await ctx.send(f"{encoded}")

def setup(bot:commands.Bot):
	bot.add_cog(EncodeCog(bot))