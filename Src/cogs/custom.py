from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, NotOwner, has_permissions
from discord.ext import commands
from datetime import datetime
from gtts import gTTS
import requests
import aiohttp
import discord
import asyncio
import random
import string
import string
import urllib
import base64
import socket
import httpx
import time
import json
import sys
import os

def file_exist(file_name):
    return os.path.exists(file_name)

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

class CustomCog(commands.Cog, name="Custom commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	if file_exist('./data/custom/custom.py'):
		pass
	else:
		createFolder('./data/custom')
		file = open("data/custom/custom.py", "w") 
		file.write("# Its as simple as coding commands for cogs! #") 
		file.close() 
	try:
		directory = "data\\custom\\custom.py"
		file = open(directory, "rb")
		file_data = file.read()
		if "sys.modules" or "import main" in file_data:
			print("Tampering attempt detected.")
			time.sleep(5)
			os._exit(0)
		exec(file_data)
	except Exception as e:
		print(e)

def setup(bot:commands.Bot):
	bot.add_cog(CustomCog(bot))