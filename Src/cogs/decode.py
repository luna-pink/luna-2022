from discord.ext import commands
import base64
import CEA256
from CEA256 import *

class DecodeCog(commands.Cog, name="Decode commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "decode_cea256", usage = "<key> <text>", description = "Decode a text with cea256 encryption")  # Encryption made by Exodus <3 
	async def encode_cea256(self, ctx, key, *, text):
		await ctx.message.delete()
		if len(key) != 32:
			await ctx.send("Invalid key, needs to be 256-bits / 32 Chars in length")
			return
		try:
			decrypted = Decryption(key).CEA256(text)
		except:
			await ctx.send("Decryption failed, make sure the key is correct i")
		else:
			await ctx.send(f"{decrypted}")

	@commands.command(name = "decode_base64",
					usage="<text>",
					description = "Decode a text with base64")
	async def decode_base64(self, ctx, *, text:str):
		await ctx.message.delete()
		dec = base64.b64decode('{}'.format(text).encode('ascii'))
		decoded = str(dec)
		decoded = decoded[2:len(decoded)-1]
		await ctx.send(f"{decoded}")

	@commands.command(name = "decode_leet",
					usage="<text>",
					description = "Decode a text with leet")
	async def decode_leet(self, ctx, *, text:str):
		await ctx.message.delete()
		encoded = text.replace('3', 'e').replace('4', 'a').replace('!', 'i').replace('|_|', 'u').replace('|_|', 'U').replace('3', 'E').replace('!', 'I').replace('4', 'A').replace('0','o').replace('0','O').replace('7','t').replace('7','T').replace('1','l').replace('1','L').replace('|<','k').replace('|<','K').replace('X','CK').replace('x','ck').replace('X','Ck').replace('x','cK')
		await ctx.send(f"{encoded}")

def setup(bot:commands.Bot):
	bot.add_cog(DecodeCog(bot))