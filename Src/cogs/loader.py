import discord
from discord.ext import commands
import time
import os

def documents():
	return os.path.expanduser("~/Documents")

class CustomCog(commands.Cog, name="Custom commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
	try:
		file = open(os.path.join(documents(), "Luna/custom/custom.py"), "r")
		file_data = file.read()
		if "sys.modules" in str(file_data):
			print("Tampering attempt detected")
			time.sleep(5)
			os._exit(0)
		elif "import main" in str(file_data):
			print("Importing main is not allowed")
			time.sleep(5)
			os._exit(0)
		elif "import inspect" in str(file_data):
			print("Importing inspect is not allowed")
			time.sleep(5)
			os._exit(0)
		exec(file_data)
	except Exception as e:
		print(e)
		os.system('pause')

def setup(bot:commands.Bot):
	bot.add_cog(CustomCog(bot))