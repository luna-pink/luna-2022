import requests

# ///////////////////////////////////////////////////////////////
# Developer Variables

developer_mode = True
beta = False
version = '3.2.9h2'
api_version = 'v9'

# ///////////////////////////////////////////////////////////////
# Luna Variables

anti_raid = False
anti_invite = False
anti_upper = False
anti_phishing = False

farming = False

active_protections = 0
active_list = []

phishing_list = [
    "discordgg.",
    "withereum.com",
    "amazon.com/exec/obidos",
    "csgo500.org",
    "steamconmunity",
    "steamcommunuty",
    "steamconmunuty",
    "steamcommunity.ru",
    "crypto24cap",
    "steamcummynutu.ru",
    "discordgifts.one",
    "discordgifts",
    "disocrde.gift"
]

# ///////////////////////////////////////////////////////////////
# Luna Protections

cooldown = []
nitro_cooldown = []
afk_status = 0
afk_user_id = 0
afk_reset = 0
user_token = ""
whitelisted_users = {}
crosshair_mode = 0
privacy = False
copycat = None
charge_sniper = False

r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
updater_url = r["updater"]
version_url = r["version"]

r = requests.get(
    "https://raw.githubusercontent.com/Nshout/Luna/main/beta.json").json()
beta_updater_url = r["updater"]
beta_version_url = r["version"]
beta_user = r["beta_user"]

if beta:
    version_url = beta_version_url

loader_src = """import os
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
			exit()
		if "inspect" and "import" in str(file_data):
			print("Importing inspect is not allowed.")
			time.sleep(5)
			exit()
		if "dill" and "import" in str(file_data):
			print("Importing dill is not allowed.")
			time.sleep(5)
			exit()
		if "exec" in str(file_data):
			print("Using exec is not allowed.")
			time.sleep(5)
			exit()
		exec(file_data)
	except Exception as e:
		print(e)
		os.system('pause')
def setup(bot:commands.Bot):
	bot.add_cog(CustomCog(bot))"""