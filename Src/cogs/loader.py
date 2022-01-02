import os
import re
import sys
import json
import time
import httpx
import base64
import qrcode
import dhooks
import string
import socket
import urllib
import ctypes
import random
import psutil
import typing
import aiohttp
import asyncio
import discord
import hashlib
import pwinput
import requests
import threading
import pyPrivnote
import subprocess
import pypresence
import ctypes.wintypes as wintypes
from CEA256 import *
from gtts import gTTS
from discord import *
from ctypes import windll
from notifypy import Notify
from os import error, name, system
from datetime import datetime
from pypresence import Presence
from discord.ext import commands
from urllib.request import urlopen
from urllib.parse import quote_plus
from time import localtime, strftime
from AuthGG.client import Client as luna_gg
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, has_permissions
class files:
	def documents():
		return os.path.expanduser("~/Documents")
	def file_exist(file_name, documents=False):
		if documents:
			return os.path.exists(os.path.join(files.documents(), file_name))
		else:
			return os.path.exists(file_name)
	def write_file(path, content, documents=False):
		if documents:
			with open(os.path.join(files.documents(), path), 'w') as f:
				f.write(content)
		else:
			with open(path, 'w') as f:
				f.write(content)
	def write_json(path, content, documents=False):
		if documents:
			with open(os.path.join(files.documents(), path), "w", encoding="utf-8") as f:
				f.write(json.dumps(content, indent=4))
		else:
			with open(path, "w", encoding="utf-8") as f:
				f.write(json.dumps(content, indent=4))
	def read_file(path, documents=False):
		if documents:
			with open(os.path.join(files.documents(), path), 'r', encoding="utf-8") as f:
				return f.read()
		else:
			with open(path, 'r', encoding="utf-8") as f:
				return f.read()
	def append_file(path, content):
		with open(path, 'a') as f:
			f.write(content)
	def delete_file(path, documents=False):
		if documents:
			os.remove(os.path.join(files.documents(), path))
		else:
			os.remove(path)
	def create_folder(path, documents=False):
		if documents:
			if not os.path.exists(os.path.join(files.documents(), path)):
				os.makedirs(os.path.join(files.documents(), path))
		else:
			if not os.path.exists(path):
				os.makedirs(path)
	def json(file_name, value, documents=False):
		if documents:
			return json.load(open(os.path.join(files.documents(), file_name), encoding="utf-8"))[value]
		else:
			return json.load(open(file_name, encoding="utf-8"))[value]
	def remove(path, documents=False):
		if documents:
			if os.path.exists(os.path.join(files.documents(), path)):
				os.remove(os.path.join(files.documents(), path))
		else:
			if os.path.exists(path):
				os.remove(path)
class CustomCog(commands.Cog, name="Custom commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
	try:
		file = open(os.path.join(files.documents(), "Luna/custom/custom.py"), "r")
		file_data = file.read()
		if "sys.modules" in str(file_data):
			print("Using sys.modules is not allowed.")
			time.sleep(5)
			os._exit(0)
		if "inspect" and "import" in str(file_data):
			print("Importing inspect is not allowed.")
			time.sleep(5)
			os._exit(0)
		if "dill" and "import" in str(file_data):
			print("Importing dill is not allowed.")
			time.sleep(5)
			os._exit(0)
		if "exec" in str(file_data):
			print("Using exec is not allowed.")
			time.sleep(5)
			os._exit(0)
		exec(file_data)
	except Exception as e:
		print(e)
		os.system('pause')
def setup(bot:commands.Bot):
	bot.add_cog(CustomCog(bot))