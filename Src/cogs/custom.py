from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, NotOwner, has_permissions
from discord.ext import commands
from datetime import datetime
import main as luna
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
import json
import sys
import os

def file_exist(file_name):
    return os.path.exists(file_name)

class CustomCog(commands.Cog, name="Custom commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	if file_exist('./data/custom/custom.py'):
		pass
	else:
		luna.createFolder('./data/custom')
		file = open("data/custom/custom.py", "w") 
		file.write("# Its as simple as coding commands for cogs! #") 
		file.close() 

	try:
		directory = "data\\custom\\custom.py"
		file = open(directory, "rb")
		file_data = file.read()
		exec(file_data)
	except Exception as e:
		luna.printerror(e)

def setup(bot:commands.Bot):
	bot.add_cog(CustomCog(bot))