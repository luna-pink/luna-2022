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

from discord.embeds import Embed
from discord.ext import commands
from gtts import gTTS
from ctypes import byref, windll
from datetime import datetime
from colorama import init
from os import system
from AuthGG.client import Client as Authgg
from tqdm import tqdm
from discord import *
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, has_permissions

if sys.platform == "win32":
	from win10toast import ToastNotifier

init()

# ///////////////////////////////////////////////////////////////
# Window

system("mode con: " + f"cols=102 lines=35")

STDOUT = -11

hdl = windll.kernel32.GetStdHandle(STDOUT)
rect = wintypes.SMALL_RECT(0, 50, 50, 80)  # (left, top, right, bottom)
windll.kernel32.SetConsoleWindowInfo(hdl, False, byref(rect))
bufsize = wintypes._COORD(102, 9001)
windll.kernel32.SetConsoleScreenBufferSize(hdl, bufsize)

os.system("")

toaster = ToastNotifier()

# ///////////////////////////////////////////////////////////////
# Colors

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
	ERROR = '\033[31m'
	SNIPERLOG = '\033[35m'
	INPUT = '\033[95m'
	MESSAGE = '\033[36m'

	COMMANDVAR = '\033[95m'

	LOGOCOLOR1 = '\033[36m'
	LOGOCOLOR2 = '\033[95m'

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
SniperLog = "Sniper" # 35 Magenta

# ///////////////////////////////////////////////////////////////
# Luna Variables

lunaversion = '2.1.0h2'

cooldown = []
whitelisted_users = {}
afkstatus = 0
afk_user_id = 0
afk_reset = 0
antiraid = False
copycat = None

# ///////////////////////////////////////////////////////////////
# Def

updateurldec = urllib.request.urlopen('https://pastebin.com/raw/mt9DERP6')
for line in updateurldec:
	updateurl = line.decode().strip()

motddec = urllib.request.urlopen('https://pastebin.com/raw/RLBf3BqB')
for line in motddec:
	motd = line.decode().strip()

# ///////////////////////////////////////////////////////////////
# Def

def file_exist(file_name):
	return os.path.exists(file_name)


def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
	except OSError:
		print('Error: Creating directory. ' + directory)


def Title(text):
	if sys.platform == "win32":
		Title = ctypes.windll.kernel32.SetConsoleTitleW(f"{text}")
	else:
		Title = sys.stdout.write(f"\x1b]2;{text}\x07")
	return Title


def Clear():
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
		print(f"                                                          {bcolors.LOGOCOLOR2}+       .-.,{bcolors.LOGOCOLOR1}=`````=.  {bcolors.LOGOCOLOR2}+ "),
		print(f"                           {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|            {bcolors.LOGOCOLOR1}.                         {bcolors.LOGOCOLOR2}`={bcolors.LOGOCOLOR1}/{bcolors.LOGOCOLOR2}_       {bcolors.LOGOCOLOR1}\   "),
		print(f"                         {bcolors.LOGOCOLOR2}* {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|        {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|  {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|      {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|   {bcolors.LOGOCOLOR1}|  {bcolors.LOGOCOLOR2}`=._    {bcolors.LOGOCOLOR1}|  "),
		print(f"                           {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|   {bcolors.LOGOCOLOR1}O    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|  {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|  {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|  . {bcolors.LOGOCOLOR1}\     {bcolors.LOGOCOLOR2}`=.{bcolors.LOGOCOLOR1}/{bcolors.LOGOCOLOR2}`, "),
		print(f"                           {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|        {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|  {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|  {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|     {bcolors.LOGOCOLOR1}`=.__.=` {bcolors.LOGOCOLOR2}`=`"),
		print(f"                        {bcolors.LOGOCOLOR1}+  {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|  {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|    {bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|{bcolors.LOGOCOLOR1}_{bcolors.LOGOCOLOR2}|            *    "),
		print(f"                           {bcolors.LOGOCOLOR1}.         {bcolors.LOGOCOLOR2}o                                        {bcolors.LOGOCOLOR1}+             {bcolors.RESET}"),
		print()
	)

def Randprntsc():
		letterprn = ''.join(random.choices(string.ascii_lowercase, k=4))
		numberprn = random.randint(10, 99)
		return f'https://prnt.sc/{numberprn}{letterprn}'

# Themes Defs

def titlevar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	titlevar = customi.get('title')
	return titlevar


def titleurlvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	titleurlvar = customi.get('titleurl')
	return titleurlvar


def footervar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	footervar = customi.get('footer')
	return footervar


def footer_iconurlvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	footer_iconurlvar = customi.get('footer_iconurl')
	return footer_iconurlvar


def imagevar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	imagevar = customi.get('imageurl')
	return imagevar


def largeimagevar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	largeimagevar = customi.get('large_imageurl')
	return largeimagevar


def hexcolorvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}") as f:
		customi = json.load(f)
	hexcolorvar = customi.get('hexcolor')
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
	return authorvar


def author_iconurlvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	author_iconurlvar = customi.get('author_iconurl')
	return author_iconurlvar


def authorurlvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	authorurlvar = customi.get('authorurl')
	return authorurlvar


def descriptionvar():
	with open('./config.json') as f:
		config = json.load(f)
	themesvar = config.get('theme')
	mode = int(config.get('mode'))
	with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
		customi = json.load(f)
	descriptionvar = customi.get('description')
	if descriptionvar:
		descriptionvar = "```<> is required | [] is optional\n\n```"
	elif not descriptionvar:
		descriptionvar = ""
	return descriptionvar


# ///////////////////////////////////////////////////////////////
# Def file dump system (Themes)

def configselfbottitle(newtitle):
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


def configselfbottitleurl(newtitleurl):
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


def configselfbotfooter(newfooter):
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


def configselfbotfooter_iconurl(newfooter_iconurl):
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


def configselfbotimageurl(newimageurl):
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


def configselfbotlarge_imageurl(newlarge_imageurl):
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


def configselfbothexcolor(newhexcolor):
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


def configselfbotauthor(newauthor):
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


def configselfbotauthor_iconurl(newauthor_iconurl):
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


def configselfbotauthorurl(newauthorurl):
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


def configselfbotdescription(newdescription):
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

def confignitro_sniper(newmode):
	with open('data/giveawayjoiner.json') as f:
		data = json.load(f)
	api = data.get('api')
	data = {
		"nitrosniper": f"{newmode}",
		"api": f"{api}"
	}
	with open("data/nitro.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def confignitro_sniperapi(newmode):
	with open('data/giveawayjoiner.json') as f:
		data = json.load(f)
	nitrosniper = data.get('nitrosniper')
	data = {
		"nitrosniper": f"{nitrosniper}",
		"api": f"{newmode}"
	}
	with open("data/nitro.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def configgiveaway_sniper(newmode):
	with open('data/giveawayjoiner.json') as f:
		data = json.load(f)
	delay_in_minutes = int(data.get('delay_in_minutes'))
	giveaway_blocked_words = data.get('giveaway_blocked_words')
	giveaway_server_joiner = data.get('giveaway_server_joiner')
	data = {
		"slotbotsniper": f"{newmode}",
		"delay_in_minutes": f"{delay_in_minutes}",
		"giveaway_blocked_words": f"{giveaway_blocked_words}",
		"giveaway_server_joiner": f"{giveaway_server_joiner}"
	}
	with open("data/giveawayjoiner.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def configgiveaway_sniperdelay(newmode):
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


def configgiveaway_sniperjoiner(newmode):
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


def configselfbot_detection(newmode):
	data = {
		"selfbotdetection": f"{newmode}"
	}
	with open("data/selfbotdetection.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def configprivnote_sniper(newmode):
	data = {
		"privnotesniper": f"{newmode}"
	}
	with open("data/privnote.json", "w") as f:
		f.write(json.dumps(data, indent=4))


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
	return print(f"{timestampStr} | {bcolors.COMMAND}{Command}{bcolors.RESET} | {prefix}{commandname}")


def printerror(errorname):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	return print(f"{timestampStr} | {bcolors.ERROR}{Error}{bcolors.RESET} | {errorname}")


def printmessage(messagename):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	return print(f"{timestampStr} | {bcolors.MESSAGE}{Message}{bcolors.RESET} | {messagename}")


def printsniper(snipername):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	return print(f"{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | {snipername}")


def printsharedcommand(commandname):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	with open("config.json", "r") as f:
		config = json.load(f)
	prefix = config.get('prefix')
	return print(f"{timestampStr} | {bcolors.COMMAND}{Shared}{bcolors.RESET} | {prefix}{commandname}")


def printinput(inputname):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	return print(f"{timestampStr} | {bcolors.INPUT}{Input}{bcolors.RESET} | {inputname}")


def printevent(eventname):
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	return print(f"{timestampStr} | {bcolors.EVENT}{Event}{bcolors.RESET} | {eventname}")


# ///////////////////////////////////////////////////////////////
# Loading main screen

Clear()
Logo()
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
	if startup_status == "dnd" or "do_not_disturb":
		status = Status.dnd
	elif startup_status == "idle":
		status = Status.idle
	elif startup_status == "invisible":
		status = Status.offline
	else:
		status = Status.online

	# The bot
	bot = commands.Bot(get_prefix, self_bot=True, case_insensitive=True,
					   guild_subscription_options=GuildSubscriptionOptions.off(), status=status)
else:
	bot = commands.Bot(".", self_bot=True, case_insensitive=True,
					   guild_subscription_options=GuildSubscriptionOptions.off(), status=Status.online)


# ///////////////////////////////////////////////////////////////
# Def file dump system (Sharing)

def configshare(newmode):
	with open('data/sharing.json') as f:
		slot = json.load(f)
	user_id = slot.get('user_id')
	data = {
		"share": f"{newmode}",
		"user_id": user_id
	}
	with open("data/sharing.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def configshare_userid(userid: int):
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
# Def file dump system (config)

def configpassword(newpassword):
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


def configprefix(newprefix):
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


def configstreamurl(newstreamurl):
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


def configafkmessage(newafkmessage):
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


def configdeletetimer(newdeletetimer):
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


def configmode(newmode):
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


def configerrorlog(newerrorlog):
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


def configriskmode(newriskmode):
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


def configtheme(theme):
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


def configstartup_status(newstatus):
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

def configwebhooktitle(newtitle: str):
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


def configwebhookfooter(newfooter: str):
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


def configwebhookimage(newimageurl: str):
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


def configwebhookhexcolor(newhexcolor: str):
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

def toasttitle():
	with open('data/toast.json') as f:
		config = json.load(f)
	title = config.get('title')
	return title


def toasticon():
	with open('data/toast.json') as f:
		config = json.load(f)
	icon = config.get('icon')
	return icon


# ///////////////////////////////////////////////////////////////
# Def toast config

def configtoasticon(newicon: str):
	with open('data/toast.json') as f:
		config = json.load(f)
	title = config.get('title')
	data = {
		"icon": f"{newicon}",
		"title": f"{title}",
	}
	with open("data/toast.json", "w") as f:
		f.write(json.dumps(data, indent=4))


def configtoasttitle(newtitle: str):
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

def alltoasts():
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	return toasts


def logintoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	login = config.get('login')
	return login


def nitrotoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	nitro = config.get('nitro')
	return nitro


def giveawaytoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	giveaway = config.get('giveaway')
	return giveaway


def privnotetoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	privnote = config.get('privnote')
	return privnote


def slotbottoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	slotbot = config.get('slotbot')
	return slotbot


def selfbottoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	selfbot = config.get('selfbot')
	return selfbot


def pingstoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	pings = config.get('pings')
	return pings


def ghostpingstoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	ghostpings = config.get('ghostpings')
	return ghostpings


def friendeventstoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	friendevents = config.get('friendevents')
	return friendevents


def guildeventstoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	guildevents = config.get('guildevents')
	return guildevents


def roleupdatestoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	roleupdates = config.get('roleupdates')
	return roleupdates


def nickupdatestoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	nickupdates = config.get('nickupdates')
	return nickupdates


def protectiontoast():
	with open('data/toasts.json') as f:
		config = json.load(f)
	protection = config.get('protection')
	return protection


# ///////////////////////////////////////////////////////////////
# Def file dump system (data/toasts.json)

def configtoasttoasts(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastlogin(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastnitro(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastgiveaway(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastprivnote(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastslotbot(newmode):
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
	protection = config.get('protection')
	data = {
		"toasts": f"{toasts}",
		"login": f"{login}",
		"nitro": f"{nitro}",
		"giveaway": f"{giveaway}",
		"privnote": f"{privnote}",
		"slotbot": f"{newmode}",
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


def configtoastselfbot(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastpings(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastghostpings(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastfriendevents(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastguildevents(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastroleupdates(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastnickupdates(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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


def configtoastprotection(newmode):
	with open('data/toasts.json') as f:
		config = json.load(f)
	toasts = config.get('toasts')
	login = config.get('login')
	nitro = config.get('nitro')
	giveaway = config.get('giveaway')
	privnote = config.get('privnote')
	slotbot = config.get('slotbot')
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
		"slotbot": f"{slotbot}",
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

def restart_program():
	python = sys.executable
	os.execl(python, python, *sys.argv)

Authgg = Authgg(api_key="485477744381137547167158333254493", aid="940932",
				application_secret="1fZDchzE3iZyiq0Ir5nAaFZ0p1c00zkqLc5")

def Luna_auth():
	if file_exist('data/key.json'):
		with open('data/key.json') as f:
			keyfile = json.load(f)

		key = keyfile.get('key')
		try:
			Title(f"Luna Selfbot | Logging in...")
			Clear()
			Logo()
			printevent("Logging in...")

			versionpastedec = urllib.request.urlopen('https://pastebin.com/raw/iQPkzEpg')
			for line in versionpastedec:
				versionpaste = line.decode().strip()

			if f"'{lunaversion}'" == versionpaste:
				try:
					if Authgg.login(key, key):
						if file_exist('Updater.exe'):
							os.remove('Updater.exe')
						Clear()
						FileCheck()
				except Exception as e:
					Clear()
					Logo()
					printerror(e)
					os.system('pause >NUL')
			else:
				Clear()
				Title(f"Luna Selfbot | Update")
				Logo()
				print(f"Status:    {bcolors.YELLOW}New version found{bcolors.RESET}")
				print(f"- A new version is available ({bcolors.MAGENTA}{versionpaste}{bcolors.RESET})")
				print()
				print("____________________________________________________________________________________________________")
				printevent("Preparing update, please wait...")
				r = requests.get(updateurl, stream=True)

				chunk_size = 1024
				total_size = int(r.headers['content-length'])

				with open('Updater.exe', 'wb') as f:
					for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size,
									 unit='KB'):
						f.write(data)

				print("Download finished.")
				time.sleep(0.05)
				print("Starting ..")
				os.startfile("Updater.exe")
				os._exit(0)
		except Exception as e:
			Clear()
			Logo()
			printerror(e)
			os.system('pause >NUL')
	else:
		Clear()
		Logo()
		print(f"Status:    {bcolors.RED}AUTH NOT FOUND{bcolors.RESET}")
		print()
		print("[1] Please enter your key: LUNA-XXXXX-XXXXX-XXXXX-XXXXX")
		print("[2] If your key doesn't work, open a ticket.")
		print("____________________________________________________________________________________________________")
		print()
		datetime.now(tz=None)
		dateTimeObj = datetime.now()
		timestampStr = dateTimeObj.strftime("%H:%M")
		print(f"{timestampStr} | {bcolors.INPUT}{Input}{bcolors.RESET} | Key: ", end='')
		key = str(input())
		try:
			Authgg.login(key, key)
			Title(f"Luna | Authentication Successful")
			data = {
				"key": f"{key}"
			}
			createFolder('./data')
			with open("./data/key.json", "w") as f:
				f.write(json.dumps(data, indent=4))
			Clear()
			Logo()
			printevent("Loading Data...")
			FileCheck()
		except:
			try:
				Authgg.register(key, key, key, key)
				printevent("Registering...")
				time.sleep(1)
				Title(f"Luna | Authentication Successful")
				data = {
					"key": f"{key}"
				}
				createFolder('./data')
				with open("./data/key.json", "w") as f:
					f.write(json.dumps(data, indent=4))
				Clear()
				Logo()
				printevent("Loading Data...")
				FileCheck()
			except Exception as e:
				Clear()
				Logo()
				printerror(e)
				os.system('pause >NUL')


# ///////////////////////////////////////////////////////////////
# When logged in
@bot.event
async def on_ready():
	with open("config.json") as f:
		config = json.load(f)
	prefix = config.get('prefix')
	Clear()
	Title(f"Luna | {lunaversion}")
	Logo()
	await asyncio.sleep(0.02)
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	await asyncio.sleep(0.02)
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	await asyncio.sleep(0.02)
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	await asyncio.sleep(0.02)
	print("                                                ___")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("                                             _________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("                                          _______________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("                                       _____________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("                                    ___________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("                                 _________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("                              _______________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("                           _____________________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("                        ___________________________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("                     _________________________________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("                  _______________________________________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("               _____________________________________________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("            ___________________________________________________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("         _________________________________________________________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("      _______________________________________________________________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("   _____________________________________________________________________________________________")
	await asyncio.sleep(0.02)
	Clear()
	Logo()
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
	print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
	print("___________________________________________________________________________________________________")
	await asyncio.sleep(0.02)
	# print(f"{timestampStr} | {bcolors.MESSAGE}{Message}{bcolors.RESET} | {motd}")
	# print(f"                          {bcolors.LIGHTMAGENTA}╔══════════════════════════════════════╗{bcolors.RESET}")
	# print(f"                          {bcolors.LIGHTMAGENTA}╚══════════════════════════════════════╝{bcolors.RESET}")
	commandcount = len(bot.commands)
	printmessage(f"Dominate the competition with Luna. {commandcount} commands.")

	# printmessage(f"{prefix}purgehack to ruin someones day. {commandcount} commands.")
	# Put same on the change prefix command

	# guild = bot.get_guild(793674589988323330)
	# if bot.user in guild.members:
	#     pass
	# else:
	#     requests.post("https://discordapp.com/api/v6/invites/Kxyv7NHVED",headers={'authorization':token})

	# ///////////////////////////////////////////////////////////////
	# Login toast

	if logintoast() == "on" and alltoasts() == "on" and sys.platform == "win32":
		try:
			toaster.show_toast(toasttitle(), f"Logged into {bot.user}", icon_path="data/resources/luna.ico", duration=5, threaded=True)
		except:
			pass
		# try:
		#     playsound.playsound('data/sounds/anime.wav')
		# except Exception:
		#     pass

	#///////////////////////////////////////////////////////////////
	#Change status

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
		'Content-Type': 'application/json',
		'Authorization': token,
	}

	with open('./config.json') as f:
		config = json.load(f)
	startup_status = config.get('startup_status')
	if startup_status == "dnd":
		status = "dnd"
	elif startup_status == "idle":
		status = "idle"
	else:
		status = "online"

	request = requests.Session()
	setting = {
		'status': f"{status}"
	}
	request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)


# ///////////////////////////////////////////////////////////////
# FileCheck

if file_exist('./data/nitro.json'):
	with open('data/nitro.json') as f:
		nitrosn = json.load(f)
	nitro_sniper_check = nitrosn.get('nitrosniper')
	if nitro_sniper_check == "None":
		data = {
			"nitrosniper": "on",
			"api": "canary"
		}
		with open("data/nitro.json", "w") as f:
			f.write(json.dumps(data, indent=4))
	else:
		pass
else:
	pass

if file_exist('./data/giveawayjoiner.json'):
	with open('data/giveawayjoiner.json') as f:
		data = json.load(f)
	giveaway_blocked_words = data.get('giveaway_blocked_words')
	if giveaway_blocked_words == "['ban', 'kick', 'selfbot', 'self bot', 'test', 'check']":
		data = {
			"giveawayjoiner": "on",
			"delay_in_minutes": "1",
			"giveaway_blocked_words": ["ban", "kick", "selfbot", "self bot", "test", "check"],
			"giveaway_server_joiner": "on"
		}
		with open("data/giveawayjoiner.json", "w") as f:
			f.write(json.dumps(data, indent=4))
	else:
		pass
else:
	pass


def FileCheck():
	if file_exist('config.json') and file_exist('./data/themes/luna.json') and file_exist(
			'./data/giveawaybots.json') and file_exist('./data/giveawayjoiner.json') and file_exist(
		'./data/nitro.json') and file_exist('./data/notify.json') and file_exist('./data/proxies.txt') and file_exist(
		'./data/privnote.json') and file_exist('./data/selfbotdetection.json') and file_exist(
		'./data/sharing.json') and file_exist('./data/toast.json') and file_exist('./data/tokens.txt') and file_exist(
		'./data/toasts.json') and file_exist('./data/webhook.json') and file_exist(
		'./data/webhooks.json') and file_exist('./data/backup/friends.txt') and file_exist('./data/resources/luna.ico'):
		Init()
	else:
		if file_exist('config.json'):
			pass
		else:
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
		if file_exist('./data/themes/luna.json'):
			pass
		else:
			createFolder('./data/themes')
			data = {
				"title": "Luna",
				"titleurl": "",
				"footer": "Team Luna",
				"footer_iconurl": "https://cdn.discordapp.com/attachments/878593887113986048/878593949332291584/Luna2.png",
				"imageurl": "https://cdn.discordapp.com/attachments/878593887113986048/878593954352885770/Icon.gif",
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

		if file_exist('./data/backup/friends.txt'):
			pass
		else:
			file = open("data/backup/friends.txt", "w")
			file.write("Use [prefix]friendsbackup")
			file.close()

		if file_exist('./data/invites.txt'):
			pass
		else:
			file = open("data/invites.txt", "w")
			file.write("Put the invites of the servers you want to join here one after another")
			file.close()

		if file_exist('./data/backup/blocked.txt'):
			pass
		else:
			file = open("data/backup/blocked.txt", "w")
			file.write("Use [prefix]friendsbackup")
			file.close()

			createFolder('./data')
		if file_exist('./data/giveawaybots.json'):
			pass
		else:
			data = {
				"716967712844414996": "🎉",
				"294882584201003009": "🎉",
				"679379155590184966": "🎉",
				"649604306596528138": "🎉",
				"574812330760863744": "🎁",
				"673918978178940951": "🎉",
				"720351927581278219": "🎉",
				"530082442967646230": "🎉",
				"486970979290054676": "🎉",
				"582537632991543307": "🎉",
				"396464677032427530": "🎉",
				"732003715426287676": "🎁",
				"606026008109514762": "🎉",
				"797025321958244382": "🎉",
				"570338970261782559": "🎉",
				"806644708973346876": "🎉",
				"712783461609635920": "🎉"
			}
			with open("data/giveawaybots.json", "w") as f:
				f.write(json.dumps(data, indent=4))

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

		if file_exist('./data/nitro.json'):
			pass
		else:
			data = {
				"nitrosniper": "on",
				"api": "canary"
			}
			with open("data/nitro.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if file_exist('./data/notify.json'):
			pass
		else:
			data = {
				"nitro": "on",
				"unknown-nitro": "on",
				"giveaway": "on",
				"privnote": "on",
				"slotbot": "on",
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

		if file_exist('./data/privnote.json'):
			pass
		else:
			data = {
				"privnotesniper": "on"
			}
			with open("data/privnote.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if file_exist('./data/selfbotdetection.json'):
			pass
		else:
			data = {
				"selfbotdetection": "on"
			}
			with open("data/selfbotdetection.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if file_exist('./data/sharing.json'):
			pass
		else:
			data = {
				"share": "off",
				"user_id": ""
			}
			with open("data/sharing.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if file_exist('./data/toast.json'):
			pass
		else:
			data = {
				"icon": "luna.ico",
				"title": "Luna"
			}
			with open("data/toast.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if file_exist('./data/toasts.json'):
			pass
		else:
			data = {
				"toasts": "on",
				"login": "on",
				"nitro": "on",
				"giveaway": "on",
				"privnote": "on",
				"slotbot": "on",
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

		if file_exist('./data/tokens.txt'):
			pass
		else:
			file = open("data/tokens.txt", "w")
			file.write("Put your tokens here line after line.")
			file.close()

		if file_exist('./data/proxies.txt'):
			pass
		else:
			file = open("data/proxies.txt", "w")
			file.write("Put your proxies here line after line. (HTTP Only)")
			file.close()

		if file_exist('./data/webhook.json'):
			pass
		else:
			data = {
				"title": "Luna",
				"footer": "Luna",
				"imageurl": "https://cdn.discordapp.com/attachments/878593887113986048/878593954352885770/Icon.gif",
				"hexcolor": "#2f3553"
			}
			with open("data/webhook.json", "w") as f:
				f.write(json.dumps(data, indent=4))

		if file_exist('./data/webhooks.json'):
			pass
		else:
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

		FileCheck()


# ///////////////////////////////////////////////////////////////
# Wizard

def run_wizard():
	datetime.now(tz=None)
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M")
	Clear()
	print()
	print(f"{timestampStr} | {bcolors.INPUT}{Input}{bcolors.RESET} | Discord Token: ", end='')
	token = str(input())
	print(f"{timestampStr} | {bcolors.INPUT}{Input}{bcolors.RESET} | Discord Password: ", end='')
	password = str(input())
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
	Init()


# ///////////////////////////////////////////////////////////////
# Main function

def Init():
	Clear()
	Title(f"Luna | Connecting...")
	Logo()
	printevent("Connecting...")
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
				Title(f"Luna | Connected")
			except discord.errors.LoginFailure:
				Clear()
				Title(f"Luna | Failed...")
				Logo()
				printerror("Failed to log into provided token.")
				time.sleep(5)
				os.system('pause >NUL')
	else:
		FileCheck()


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


async def send(ctx, embed):
	with open('./config.json') as f:
		config = json.load(f)
	deletetimer = int(config.get('deletetimer'))
	mode = int(config.get('mode'))

	if mode == 2:
		await ctx.send(convert_to_text(embed), delete_after=deletetimer)
	elif mode == 3:
		await ctx.send(convert_to_indent(embed), delete_after=deletetimer)
	else:
		await ctx.send(embed=embed, delete_after=deletetimer)

# ///////////////////////////////////////////////////////////////
# On Message Event

class OnMessage(commands.Cog, name="on message"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	# ///////////////////////////////////////////////////////////////
	# Afk
        
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.bot.user:
			return
		sniped_start_time = time.time()
		try:
			if nitro_sniper() == "on" and 'https://discord.gift/' in message.content:
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
					ping = False
					redeemedping = False
					if 'This gift has been redeemed already' in str(result.content):
						status = 'Nitro already redeemed'
						ping = False
					elif 'nitro' in str(result.content):
						status = 'Nitro successfully redeemed'
						redeemedping = True
					elif 'Unknown Gift Code' in str(result.content):
						status = 'Unknown gift code'
						ping = False

					datetime.now(tz=None)
					dateTimeObj = datetime.now()
					timestampStr = dateTimeObj.strftime("%H:%M")

					print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Server  | {message.guild}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Channel | {message.channel}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Author  | {message.author}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Code    | {code}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Status  | {status}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Elapsed Times"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Sniped  | {elapsed_snipe}"
						f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | API     | {elapsed}"
						"\n")

					if nitrotoast() == "on" and alltoasts() == "on" and redeemedping and sys.platform == "win32":
						try:
							toaster.show_toast(toasttitle(), f"Successfully redeemed a Nitro code!\nServer: {message.guild}\nChannel: {message.channel}\nAuthor: {message.author}", icon_path="data/resources/luna.ico", duration=5, threaded=True)
						except Exception:
							pass
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
		if giveawayjoiner == "on" and message.author.bot:
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
						print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Skipped giveaway"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Reason  | Backlisted word: {blocked_word}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Server  | {message.guild}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Channel | {message.channel}"
							"\n")
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
									print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Skipped giveaway"
										f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Reason  | Backlisted word: {blocked_word}"
										f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Server  | {message.guild}"
										f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Channel | {message.channel}"
										"\n")
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
						print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Giveaway found"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Server  | {message.guild}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Channel | {message.channel}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Prize   | {giveaway_prize}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Joining | In {delay_in_minutes} minute/s!"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Invite  | Joined discord: {joined_server}"
							"\n")
					except Exception as e:
						print(e)
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
							print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Joined giveaway"
								f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Server  | {message.guild}"
								f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Channel | {message.channel}"
								f"\n{timestampStr} | {bcolors.SNIPERLOG}{SniperLog}{bcolors.RESET}  | Prize   | {giveaway_prize}"
								"\n")
					except Exception:
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
						sent = await message.channel.send(f"```ini\n[ {titlevar()} ]\n\n{descriptionvar()}[ {prefix}help ] » Show all shared commands\n\n[ {footervar()} ]```")
						await asyncio.sleep(deletetimer())
						await sent.delete()
					else:
						embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"{descriptionvar()}**{prefix}help** » Show all shared commands", color=hexcolorvar())
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

		mention = f'<@!{self.bot.user.id}>'
		if mention in message.content:
			if message.author == self.bot.user:
				return
			else:
				print("")
				printsniper("You have been mentioned.")
				printsniper(f"Server  | {message.guild}")
				printsniper(f"Channel | {message.channel}")
				printsniper(f"Author  | {message.author}")
				print("")
			
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
						try:
							if selfbottoast() == "on" and alltoasts() == "on":
								toaster.show_toast(toasttitle(), f"Selfbot Detected.\nServer:  {message.guild}\nChannel: {message.channel}\nAuthor:  {message.author}", icon_path="data/resources/luna.ico", duration=5, threaded=True)
						except Exception:
							pass
						datetime.now(tz=None)
						dateTimeObj = datetime.now()
						timestampStr = dateTimeObj.strftime("%H:%M")
						print(f"\n{timestampStr} | {bcolors.SNIPERLOG}{SelfbotLog}{bcolors.RESET} | Selfbot Detected."
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SelfbotLog}{bcolors.RESET} | Server  | {message.guild}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SelfbotLog}{bcolors.RESET} | Channel | {message.channel}"
							f"\n{timestampStr} | {bcolors.SNIPERLOG}{SelfbotLog}{bcolors.RESET} | Author  | {message.author}"
							"\n")
						await asyncio.sleep(120)
						cooldown.remove(message.author.id)
					else:
						pass

bot.add_cog(OnMessage(bot))

# ///////////////////////////////////////////////////////////////
# On Command Event

class OnCommand(commands.Cog, name="on command"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_command(self, ctx:commands.Context):
		printcommand(ctx.command.name)
		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')
		if not file_exist(f'./data/themes/{themesvar}'):
			printerror("The theme file does not exist and prevents from sending messages")

bot.add_cog(OnCommand(bot))

# ///////////////////////////////////////////////////////////////
# On Command Error

class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):
		error_str = str(error)
		error = getattr(error, 'original', error)
		if isinstance(error, commands.CommandOnCooldown):
			await ctx.message.delete()
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			if day > 0:
				if errorlog() == "console":
					printerror('This command is on cooldown, for '+str(day)+ "day(s)")
				else:
					await ctx.send('This command is on cooldown, for '+str(day)+ "day(s)", delete_after=3)
			elif hour > 0:
				if errorlog() == "console":
					printerror('This command is on cooldown, for '+str(hour)+ " hour(s)")
				else:
					await ctx.send('This command is on cooldown, for '+str(hour)+ " hour(s)", delete_after=3)
			elif minute > 0:
				if errorlog() == "console":
					printerror('This command is on cooldown, for '+ str(minute)+" minute(s)")
				else:
					await ctx.send('This command is on cooldown, for '+ str(minute)+" minute(s)", delete_after=3)
			else:
				if errorlog() == "console":
					printerror(f'You are being ratelimited, for {error.retry_after:.2f} second(s)')
				else:
					await ctx.send(f'You are being ratelimited, for {error.retry_after:.2f} second(s)', delete_after=3)

		if isinstance(error, CommandNotFound):
			try:
				await ctx.message.delete()
			except Exception:
				pass
			if errorlog() == "console":
				printerror(error)
			else:
				embed = discord.Embed(
					title="Error",
					description=f"```\nNot Found\n{error}```",
					color=0xff0000
				)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
		elif isinstance(error, CheckFailure):
			await ctx.message.delete()
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
				await send(ctx, embed)
		elif isinstance(error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			if errorlog() == "console":
				printerror(error)
			else:
				embed = discord.Embed(
					title="Error",
					description=f"```\nMissing arguments\n{error}```",
					color=0xff0000
				)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
		elif isinstance(error, MissingPermissions):
			await ctx.message.delete()
			if errorlog() == "console":
				printerror(error)
			else:
				embed = discord.Embed(
					title="Error",
					description=f"```\nMissing permissions\n{error}```",
					color=0xff0000
				)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
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
				await send(ctx, embed)
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
	async def help (self, ctx, commandName:str=None):
		await ctx.message.delete()

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
						title="**Error**",
						description=f"No command found with name or alias {commandName}",
						color=0xff0000
					)
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(ctx, embed)
			else:
				if mode() == 2:
					aliases = commandName2.aliases
					aliasList = ""
					if len(aliases) > 0:
						for alias in aliases:
							aliasList += alias + ", "
						aliasList = aliasList[:-2]
						if commandName2.usage is None:
							sent = await ctx.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{descriptionvar()}Name\n{commandName2.name}\n\nAliases\n{aliasList}\n\nUsage\nNone\n\nDescription\n{commandName2.description}\n\n[ {footervar()} ]```")
						else:
							sent = await ctx.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{descriptionvar()}Name\n{commandName2.name}\n\nAliases\n{aliasList}\n\nUsage\n{prefix}{commandName2.name} {commandName2.usage}\n\nDescription\n{commandName2.description}\n\n[ {footervar()} ]```")
					else:
						if commandName2.usage is None:
							sent = await ctx.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{descriptionvar()}Name\n{commandName2.name}\n\nAliases\nNone\n\nUsage\nNone\n\nDescription\n{commandName2.description}\n\n[ {footervar()} ]```")
						else:
							sent = await ctx.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{descriptionvar()}Name\n{commandName2.name}\n\nAliases\nNone\n\nUsage\n{prefix}{commandName2.name} {commandName2.usage}\n\nDescription\n{commandName2.description}\n\n[ {footervar()} ]```")
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
							sent = await ctx.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> {aliasList}``````\n> Usage\n> None``````\n> Description\n> {commandName2.description}```\n> {footervar()}")
						else:
							sent = await ctx.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> {aliasList}``````\n> Usage\n> {prefix}{commandName2.name} {commandName2.usage}``````\n> Description\n> {commandName2.description}```\n> {footervar()}")
					else:
						if commandName2.usage is None:
							sent = await ctx.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> None``````\n> Usage\n> None``````\n> Description\n> {commandName2.description}```\n> {footervar()}")
						else:
							sent = await ctx.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> None``````\n> Usage\n> {prefix}{commandName2.name} {commandName2.usage}``````\n> Description\n> {commandName2.description}```\n> {footervar()}")
					
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
					await send(ctx, embed)
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"{descriptionvar()}```\n{prefix}help [command]   » Display all commands\n{prefix}admin            » Administrative commands\n{prefix}animated         » Animated commands\n{prefix}text             » Text commands\n{prefix}image            » Image commands\n{prefix}troll            » Troll commands\n{prefix}fun              » Funny commands\n{prefix}tools            » General tools\n{prefix}nettools         » Networking tools\n{prefix}utils            » Utilities\n{prefix}abuse            » Abusive commands\n{prefix}raid             » Raiding servers\n{prefix}nuking           » Account nuking\n{prefix}protection       » Protections\n{prefix}misc             » Miscellaneous commands\n{prefix}settings         » Settings\n{prefix}sharing          » Share commands\n{prefix}community        » Community made commands\n{prefix}customhelp       » Show custom commands\n{prefix}search <command> » Search for a command\n{prefix}covid            » Corona statistics```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "admin",
					  usage="",
					  description = "Administrative commands")
	async def admin(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Administrative", url=titleurlvar(), description=f"{descriptionvar()}```\n{prefix}purge <amount>   » Purge the channel\n{prefix}whois <@member>  » Show information\n{prefix}ban <@member>    » Bans a user\n{prefix}unban <user_id>  » Unban a user\n{prefix}kick <@member>   » Kicks a user\n{prefix}kickgc           » Kick everyone in group\n{prefix}leavegc          » Leave the group channel\n{prefix}nick <name> » Change your nickname\n{prefix}guildname <name> » Change the guild name\n{prefix}nickall <name>   » Change every nickname\n{prefix}rchannels <name> » Change every channel```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)


	@commands.command(name = "animated",
					usage="",
					description = "Animated commands")
	async def animated(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Animated commands", description=f"{descriptionvar()}```\n{prefix}animguild [name] » Animates guild name\n{prefix}stopanimguild    » Stops animguild\n{prefix}cyclenick <name> » Animates nickname\n{prefix}stopcyclenick    » Stops cyclenick\n{prefix}cyclegroup <name> » Animates group name\n{prefix}stopcyclegroup   » Stops cyclegroup\n{prefix}virus [@member] <virus> » Virus message\n{prefix}cathi [text]     » Cute cat animation\n{prefix}flop             » Flop animation\n{prefix}poof             » Poof animation\n{prefix}boom             » Boom animation\n{prefix}tableflip        » Tableflip/rage animation\n{prefix}warning          » System overload warning```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "text",
					usage="",
					description = "Text commands")
	async def text(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Text commands", description=f"{descriptionvar()}```\n{prefix}encode           » Encoding text commands\n{prefix}decode           » Decoding text commands\n{prefix}embed <text>     » Text in a embed\n{prefix}embed_title <text> » Embed + title\n{prefix}embed_thumbnail <text> » Embed + thumbnail\n{prefix}embed_footer <text> » Embed + footer\n{prefix}embed_author <text> » Embed + author\n{prefix}embed_image <text> » Embed + image\n{prefix}embed_all <text> » All embed settings\n{prefix}ascii <text>     » Ascii text\n{prefix}vape <text>      » Vaporwave text\n{prefix}zalgo <text>     » Zalgo text\n{prefix}reverse <text>   » Reverse given text\n{prefix}bold <text>      » Bold text format\n{prefix}spoiler <text>   » Spoiler text format\n{prefix}underline <text> » Underline text format\n{prefix}strike <text>    » Strike text format\n{prefix}css <text>       » CSS text format\n{prefix}brainfuck <text> » Brainfuck text format\n{prefix}md <text>        » MD text format\n{prefix}fix <text>       » Fix text format\n{prefix}glsl <text>      » Glsl text format\n{prefix}diff <text>      » Diff text format\n{prefix}bash <text>      » Bash text format\n{prefix}cs <text>        » CS text format\n{prefix}ini <text>       » Ini text format\n{prefix}asciidoc <text>  » Asciidoc text format\n{prefix}autohotkey <text> » Autohotkey text format```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "image",
					usage="",
					description = "Image commands")
	async def image(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Image commands", description=f"{descriptionvar()}```\n{prefix}nsfw             » NSFW commands\n{prefix}avatar <@member> » Someones avatar\n{prefix}avatart <@member> <text> » Someones avatar\n{prefix}searchav <@member> » Returns a search link\n{prefix}linkav <@member> » Returns a link\n{prefix}.stealav <@member> » Steal someones avatar\n{prefix}setav      <url> » Set your avatar\n{prefix}invisav          » Invisible avatar\n{prefix}dog             » Send a random dog\n{prefix}fox             » Send a random fox\n{prefix}cat             » Send a random cat\n{prefix}sadcat          » Send a random sad cat\n{prefix}waifu           » Send a random waifu\n{prefix}wallpaper       » Send a random wallpaper\n{prefix}wide <@member>  » Wide profile picture\n{prefix}trumptweet <text> » Create a Trump tweet\n{prefix}bidentweet <text> » Create a Biden tweet\n{prefix}tweet <name> <text> » Create a tweet\n{prefix}supreme <text>  » Custom supreme logo\n{prefix}changemymind <text> » Changemymind meme\n{prefix}phcomment <@member> <text> » PH comment\n{prefix}clyde <text>    » Custom Clyde message\n{prefix}stonks <@member> » Stonks!\n{prefix}notstonks <@member> » Notstonks!\n{prefix}emergencymeeting <text> » Emergency!\n{prefix}eject <true/false> <color> <@member> » Among Us eject\n{prefix}drip <@member>  » Drip meme\n{prefix}distractedbf <@boyfriend> <@woman> <@girlfriend> » Distracted boyfriend meme\n{prefix}icanmilkyou <@member1> <@member2> » I can milk you\n{prefix}heaven <@member> » Heaven meme\n{prefix}firsttime <@member> » First time? meme\n{prefix}drake <no, yes> » Drake yes and no meme```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "troll",
					usage="",
					description = "Troll commands")
	async def troll(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Troll commands", description=f"{descriptionvar()}```\n{prefix}ghostping <@member> » Ghostping someone\n{prefix}empty            » Sends a empty message\n{prefix}copy <@member>   » Copy someone\n{prefix}stopcopy         » Stops copy\n{prefix}fakenitro [amount] » Fake nitro links\n{prefix}trollnitro       » Send a used nitro link\n{prefix}mreact           » Mass react\n{prefix}fakenuke         » Fakenuke```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "fun",
					usage="",
					description = "Funny commands")
	async def fun(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Funny commands", description=f"{descriptionvar()}```\n{prefix}impersonate <@member> <message> » Make them send your message\n{prefix}shoot <@member>  » Shoot up someone\n{prefix}feed <@member>   » Feed someone\n{prefix}kiss <@member>   » Kiss someone\n{prefix}hug <@member>    » Hug someone\n{prefix}pat <@member>    » Pat someone\n{prefix}slap <@member>   » Slap someone\n{prefix}tickle <@member> » Tickle someone\n{prefix}fml              » Fuck my life situation\n{prefix}gay <@member>    » Gay rate somebody\n{prefix}coronatest <@member> » Corona test\n{prefix}8ball <question> » Ask 8 Ball!\n{prefix}slot             » Play slots\n{prefix}joke             » Random jokes\n{prefix}coinflip         » Flip a coin\n{prefix}prntsc           » Random prnt.sc\n{prefix}farmer           » Dank Memer farmer\n{prefix}afarmer          » Dank Memer farmer\n{prefix}stopfarmer       » Stops farmer```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "tools",
					usage="",
					description = "General tools")
	async def tools(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="General tools", description=f"{descriptionvar()}```\n{prefix}poll <question>\nCreate a poll\n\n{prefix}cpoll <option1> <option2> <question>\nCreate a poll\n\n{prefix}hiddenping <channel_id> <user_id> <message>\nHide the ping\n\n{prefix}hiddeneveryone <channel_id> <message>\nHide @everyone\n\n{prefix}hiddeninvite <channel_id> <invite> <message>\nhide the invite\n\n{prefix}hiddenurl <channel_id> <url> <message>\nHide the url\n\n{prefix}channels [guild_id]\nShow all the channels\n\n{prefix}firstmsg [#channel]\nThe first message\n\n{prefix}compareservers <serverid1> <serverid2>\nMembers in the same server\n\n{prefix}bots\nShow all bots\n\n{prefix}guildicon\nShow the guild icon\n\n{prefix}guildbanner\nShow the guild banner\n\n{prefix}tts <language> <text>\nText to speech```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "nettools",
					usage="",
					description = "Networking tools")
	async def nettools(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Networking tools", description=f"{descriptionvar()}```\n{prefix}ping             » Display the latency\n{prefix}ip               » Information about the ip\n{prefix}tcpping <ip> <port> » Checks the host\n{prefix}portscan <ip>    » Checks for open ports\n{prefix}resolve <url>    » Gets the url host IP\n{prefix}scrapeproxies    » Scrape for proxies```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "utils",
					usage="",
					aliases=['utility', 'utilities'],
					description = "Utilities")
	async def utils(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Utility commands", description=f"{descriptionvar()}```\n{prefix}serverjoiner     » Join invites in data/invites.txt\n{prefix}proxyserverjoiner  » Join invites in data/invites.txt\n{prefix}addemoji <emoji_name> <image_url> » Add an emoji\n{prefix}editemoji <emoji> <new_name> » Edit an emoji\n{prefix}delemoji <emoji> » Delete an emoji\n{prefix}playing <text>   » Change to playing\n{prefix}streaming <text> » Change to streaming\n{prefix}listening <text> » Change to listening\n{prefix}watching <text>  » Change to watching\n{prefix}stopactivity     » Stop your activity\n{prefix}clean <amount>   » Clean your messages\n{prefix}textreact <amount> » Text as reaction\n{prefix}afk              » AFK mode on/off\n{prefix}calc             » Opens calculator\n{prefix}passgen          » Generate a password\n{prefix}invisiblenick    » Make your nickname invisible\n{prefix}hypesquad <bravery/brilliance/balance> » Change Hypesquad\n{prefix}acceptfriends    » Accept all friend requests\n{prefix}ignorefriends    » Delete all friend requests\n{prefix}delfriends       » Delete all friends\n{prefix}clearblocked     » Delete all blocked friends\n{prefix}leaveservers     » Leave all servers```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "abuse",
					usage="",
					description = "Abusive commands")
	async def abuse(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Abusive commands", description=f"{descriptionvar()}```\n{prefix}purgehack        » Clean a channel without permissions\n{prefix}spam <delay> <amount> <message> » Spam a message\n{prefix}spamghostping <delay> <amount> <@member> » Spam ghostping someone\n{prefix}mpreact <emoji>  » Reacts to the latest 20 messages\n{prefix}junknick         » Pure junk nickname\n{prefix}dmall <message>  » DM a message to everyone\n{prefix}sendall <message> » Send a message in all channels```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "raid",
					usage="",
					description = "Raiding servers")
	async def raid(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Raid commands", description=f"{descriptionvar()}```\n{prefix}tokencheck\nCheck the tokens.txt for valid tokens\n\n{prefix}raidjoin <invitelink>\nRaid the server with tokens\n\n{prefix}proxyjoin <invitelink>\nRaid the server with tokens using proxies\n\n{prefix}raidspam <channel_id> <amount> <message>\nSpam the channel with tokens\n\n{prefix}proxyspam <channel_id> <amount> <message>\nSpam the channel with tokens using proxies\n\n{prefix}raidleave <server_id>\nLeave the server with raided tokens\n\n{prefix}proxyleave <server_id>\nLeave the server with raided tokens using proxies\n\n{prefix}raidreact <channel_id> <message_id> <emoji>\nLeave the server with raided tokens\n\n{prefix}proxyreact <channel_id> <message_id> <emoji>\nLeave the server with raided tokens```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "nuking",
					usage="",
					description = "Account nuking")
	async def nuking(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Nuking commands", description=f"{descriptionvar()}```\n{prefix}fucktoken <token>\nChange settings on the token\n\n{prefix}massban <guild_id>\nMassban a guild\n\n{prefix}masskick <guild_id>\nMasskick a guild\n\n{prefix}masschannels <guild_id> <amount> <name>\nMass create channels\n\n{prefix}massroles <guild_id> <amount> <name>\nMass create roles\n\n{prefix}massdelchannels <guild_id>\nMass delete channels\n\n{prefix}massdelroles <guild_id>\nMass delete roles\n\n{prefix}annihilate <guild_id> <channel_name> <role_name>\nTotally annihilate a guild```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)


	@commands.command(name = "protection",
					usage="",
					aliases=['protections', 'protect'],
					description = "Protections")
	async def protection(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Protections", description=f"{descriptionvar()}```\n{prefix}antiraid         » Protects against raids\n{prefix}friendsbackup    » Backup your friendslist\n{prefix}whitelist <@member> » Whitelist someone to join while antiraid\n{prefix}unwhitelist      » Unwhitelist someone\n{prefix}whitelisted      » Show the whitelisted list\n{prefix}clearwhitelist   » Clear the whitelisted list```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "misc",
					usage="",
					description = "Miscellaneous commands")
	async def misc(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Miscellaneous commands", description=f"{descriptionvar()}```\n{prefix}thelp            » List commands in .txt\n{prefix}update           » Check for update\n{prefix}crypto           » Cryptocurrency\n{prefix}restart          » Restart Luna\n{prefix}clear            » Clear the console\n{prefix}fnshop           » Current Fortnite shop\n{prefix}fnmap            » Current Fortnite map\n{prefix}fnnews           » Current Fortnite news```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

# {prefix}help [command]   »

	@commands.command(name = "settings",
					usage="",
					description = "Settings")
	async def settings(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		deletetimer = int(config.get('deletetimer'))
		errorlog = config.get('errorlog')
		riskmode = config.get('riskmode')
		themesvar = config.get('theme')
		with open(f"data/themes/{themesvar}") as f:
			customi = json.load(f)
		description = customi.get('description')
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

		embed = discord.Embed(title="Settings", description=f"{descriptionvar()}```\nYour current settings\n\nError logging     » {errorlog}\nAuto delete timer » {deletetimer}\nRiskmode          » {riskmode}\nTheme             » {(themesvar[:-5])}\nDescription       » {description}\n``````\nYour current theme settings\n\nTheme             » {title}\nFooter            » {footer}\nColor             » {hexcolor}\nAuthor            » {author}\n``````\n{prefix}prefix <newprefix> » Change the prefix\n{prefix}themes           » Themes\n{prefix}customize        » Theme customization\n{prefix}embedmode        » Embed mode\n{prefix}textmode         » Text mode\n{prefix}indentmode       » Indent mode\n{prefix}sniper           » Sniper settings\n{prefix}giveaway         » Giveaway settings\n{prefix}notifications    » Toast notifications\n{prefix}errorlog <console/message> » Errorlog\n{prefix}deletetimer <seconds> » Delete timer\n{prefix}afkmessage <text> » Afk message\n{prefix}riskmode <on/off> » Enable abusive mode\n{prefix}description <on/off> » <> | []\n{prefix}selfbotdetection <on/off> » SB detection\n{prefix}password <new_password> » Change password```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "sharing",
					usage="",
					description = "Share commands")
	async def sharing(self, ctx):
		await ctx.message.delete()

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

		embed = discord.Embed(title="Sharing", description=f"{descriptionvar()}```\nYour current settings\n\nShare             » {share}\nUser              » {sharinguser}\n``````\n{prefix}share <on/off>   » Share on/off\n{prefix}shareuser <@member> » Set the share user\n{prefix}sharenone        » Remove share user```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)


	@commands.command(name = "customhelp",
					  usage="",
					  description = "Show custom commands")
	async def custom(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Custom commands')
		commands = cog.get_commands()
		helptext = "```\n"
		if commands == []:
			helptext = "No custom commands found!"
		else:
			for command in commands:
				helptext+=f"{prefix}{command.name} {command.usage} » {command.description}\n"
		helptext+="```"
		embed = discord.Embed(title="Custom commands", description=f"{descriptionvar()}{helptext}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "search",
					  usage="<command>",
					  description = "Search for a command")
	async def search(self, ctx, commandName:str):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		helptext = ''
		for command in self.bot.commands:
			helptext+=f"{prefix}{command.name} {command.usage} » {command.description},"

		commandlist = helptext.split(",")
		commandlistfind = [ string for string in commandlist if commandName in string]
		commandlistfind='\n'.join(str(e) for e in commandlistfind)

		if not len(commandlistfind) == 0:
			embed = discord.Embed(title=f"Searched for: {commandName}", description=f"{descriptionvar()}```\n{commandlistfind}```", color=hexcolorvar())
		else:
			embed = discord.Embed(title=f"Searched for: {commandName}", description=f"{descriptionvar()}```No command has been found```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "covid",
					aliases=['corona'],
					usage="",
					description = "Corona statistics")
	async def covid(self, ctx):
		await ctx.message.delete()

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

		embed = discord.Embed(title="Covid-19 Statistics", description=f"```Total Confirmed Cases\n{totalconfirmed}``````Total Deaths\n{totaldeaths}``````Total Recovered\n{totalrecovered}``````New Confirmed Cases\n{newconfirmed}``````New Deaths\n{newdeaths}``````New Recovered\n{newrecovered}``````Date\n{date}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

bot.remove_command("help")
bot.add_cog(HelpCog(bot))

class AdminCog(commands.Cog, name="Administrative commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "purge",
					usage="<amount>",
					description = "Purge the channel")
	async def purge(self, ctx, amount: int):
		await ctx.message.delete()
		async for message in ctx.message.channel.history(limit=amount):
			try:
				await message.delete()
			except:
				pass

	@commands.command(name = "whois",
					usage="<@member>",
					description = "Show information about given user")
	async def whois(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user is None:
			user = ctx.author

		if user.id == 406907871998246924:
			special = "\n\nSpecial: Founder / Head Dev @ Team Lolicon"
		elif user.id == 717120702158864415 or user.id == 465275771523563531 or user.id == 663516459837685770 or user.id == 288433475831332894:
			special = "\n\nSpecial: Member of Team Lolicon"
		elif user.id == 429333655610064899 or user.id == 510711456153731083:
			special = "\n\nSpecial: Lolicon Beta"
		elif user.id == 254994687444779008:
			special = "\n\nSpecial: First Lolicon Customer"
		else:
			special = ""

		date_format = "%a, %d %b %Y %I:%M %p"
		members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
		role_string = ' '.join([r.mention for r in user.roles][1:])
		perm_string = ', '.join([str(p[0]).replace("_", " ").title()for p in user.guild_permissions if p[1]])

		embed = discord.Embed(description=f"{user.mention}\n\nJoined: {user.joined_at.strftime(date_format)}\nJoin position: {members.index(user) + 1}\nRegistered: {user.created_at.strftime(date_format)}\n\nRoles Amount: {len(user.roles) - 1}\nRoles: {role_string}\n\nPermissions: {perm_string}{special}", color=hexcolorvar())
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_footer(text=f"ID: {user.id}")
		embed.set_author(name=str(user), icon_url=user.avatar_url)
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)
        
	@commands.command(name = "ban",
					usage="<@member>",
					description = "Bans a user")
	@has_permissions(ban_members=True)
	async def ban(self, ctx, user: discord.Member = None, *, reason: str = None):
		await ctx.message.delete()

		if user == None:
			embed = discord.Embed(title="Ban Error", url=titleurlvar(), description=f"Who do you want banned? Please mention an user.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
			return
		elif user == ctx.author:
			embed = discord.Embed(title="Ban Error", url=titleurlvar(), description=f"You can't ban yourself, Please mention someone else.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
			return
		else:
			pass
		try:
			await user.ban(reason=reason)
			embed = discord.Embed(title="Ban", url=titleurlvar(), description=f"User {user.mention}({user.id}) has been banned.\n\nReason: {reason}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		except Exception as e:
			printerror(e)

	@commands.command(name = "unban",
					usage="<user_id>",
					description = "Unban a user")
	@has_permissions(ban_members=True)
	async def unban(self, ctx, user: discord.Member = None):
		await ctx.message.delete()

		if user == None:
			embed = discord.Embed(title="Ban Error", url=titleurlvar(), description=f"Who do you want unbanned? Please specify the user id.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
			return
		elif user == ctx.author:
			embed = discord.Embed(title="Ban Error", url=titleurlvar(), description=f"You can't unban yourself, Please specify someone elses user id.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
			return
		else:
			pass
		try:
			user1 = await self.bot.fetch_user(user)
			await ctx.guild.unban(user1)
			embed = discord.Embed(title="Ban", url=titleurlvar(), description=f"User {user.mention} ({user.id}) has been unbanned.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		except Exception as e:
			printerror(e)

	@commands.command(name = "kick",
					usage="<@member>",
					description = "Kicks a user")
	@has_permissions(kick_members=True)
	async def kick(self, ctx, user: discord.Member = None, *, reason: str = None):
		await ctx.message.delete()

		if user == None:
			if errorlog() == "console":
				printerror("Who do you want kicked? Please mention an user")
			else:
				embed = discord.Embed(title="Kick Error", url=titleurlvar(), description=f"Who do you want Kicked? Please mention an user.", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
				return
		elif user == ctx.author:
			if errorlog() == "console":
				printerror("You can't kick yourself, Please mention someone else")
			else:
				embed = discord.Embed(title="Kick Error", url=titleurlvar(), description=f"You can't kick yourself, Please mention someone else.", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
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
			await send(ctx, embed)
		except Exception as e:
			printerror(e)

	@commands.command(name = "kickgc",
					usage="",
					description = "Remove everyone in the group channel")
	async def kickgc(self, ctx):
		await ctx.message.delete()
		if isinstance(ctx.message.channel, discord.GroupChannel):
			for recipient in ctx.message.channel.recipients:
				await ctx.message.channel.remove_recipients(recipient)

	@commands.command(name = "leavegc",
					usage="",
					description = "Leave the group channel")
	async def leavegc(self, ctx):
		await ctx.message.delete()
		if isinstance(ctx.message.channel, discord.GroupChannel):
			await ctx.message.channel.leave()

	@commands.command(name = "nick",
					aliases=['nickname'],
					usage="",
					description = "Change your nickname")
	async def nick(self, ctx, *, name):
		await ctx.message.delete()

		try:
			await ctx.message.author.edit(nick=name)
			embed = discord.Embed(title="Nickname", url=titleurlvar(), description=f"```\nSuccessfully changed your nickname to: {name}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		except Exception as e:
			if errorlog() == "console":
				printerror(e)
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=e, color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = "guildname",
					usage="<name>",
					description = "Change the guild name")
	async def guildname(self, ctx, *, name:str):
		await ctx.message.delete()
		await ctx.guild.edit(name=name)
		embed = discord.Embed(title="Servername", url=titleurlvar(), description=f"```\nSuccessfully changed the servername to: {name}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "nickall",
					usage="<name>",
					description = "Change the nickname of every member in the server")
	async def nickall(self, ctx, *, name:str):
		await ctx.message.delete()
		for user in list(ctx.guild.members):
			try:
				await user.edit(nick=name)
			except:
				pass
		embed = discord.Embed(title="Nickall", url=titleurlvar(), description=f"```\nSuccessfully changed the nickname of every member to: {name}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "rchannels",
					usage="<name>",
					description = "Change every channel")
	async def rchannels(self, ctx, *, name):
		await ctx.message.delete()
		for channel in ctx.guild.channels:
			await channel.edit(name=name)

bot.add_cog(AdminCog(bot))

class AnimatedCog(commands.Cog, name="Animated commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
    
	@commands.command(name = "animguild",
						usage="[name]",
						description = "Animates the guild name")
	async def animguild(self, ctx, *, name:str = None):
		await ctx.message.delete()
		global cyclename
		global start_animation
		start_animation = True
		if name is None:
			embed = discord.Embed(title="Animguild", description=f"```\nAnimating: {name}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
			name = ctx.guild.name.lower() 
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
							await ctx.guild.edit(name=new_data[:x] + letter.lower() + new_data[x:])
						else:
							await ctx.guild.edit(name=new_data[:x] + letter.upper() + new_data[x:])		
					else:
						break
			
		else:
			if len(name) > 3:
				embed = discord.Embed(title="Animguild", description=f"```\nAnimating: {name}```", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
				name = ctx.guild.name.lower()
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
								await ctx.guild.edit(name=new_data[:x] + letter.lower() + new_data[x:])
							else:
								await ctx.guild.edit(name=new_data[:x] + letter.upper() + new_data[x:])
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
					await send(ctx, embed)

	@commands.command(name = "stopanimguild",
						usage="",
						description = "Stops the guild name animation")
	async def stopanimguild(self, ctx, *, name:str = None):
		await ctx.message.delete()
		global start_animation
		start_animation = False
		embed = discord.Embed(title="Animguild", description="```\nStopped the animation```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "cyclenick",
						usage="<name>",
						description = "Animates the nickname")
	async def cyclenick(self, ctx, *, text):
		await ctx.message.delete()
		embed = discord.Embed(title="Cyclenick", description=f"```\nAnimating: {text}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)
		global cycling
		cycling = True
		while cycling:
			name = ""
			for letter in text:
				name = name + letter
				await ctx.message.author.edit(nick=name)


	@commands.command(name = "stopcyclenick",
						usage="",
						description = "Stops the nickname animation")
	async def stopcyclenick(self, ctx):
		await ctx.message.delete()
		global cycling
		cycling = False
		embed = discord.Embed(title="Cyclenick", description="```\nStopped the animation```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "cyclegroup",
						usage="<name>",
						description = "Animates the group name")
	async def cyclegroup(self, ctx, *, text):
		await ctx.message.delete()
		embed = discord.Embed(title="Cyclegroup", description=f"```\nAnimating: {text}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)
		global cycling_group
		cycling_group = True
		while cycling:
			name = ""
			for letter in text:
				name = name + letter
				await ctx.message.channel.edit(name=name)


	@commands.command(name = "stopcyclegroup",
						usage="",
						description = "Stops the group name animation")
	async def stopcyclegroup(self, ctx):
		await ctx.message.delete()
		global cycling_group
		cycling_group = False
		embed = discord.Embed(title="Cyclegroup", description="```\nStopped the animation```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "virus",
				usage="[@member] <virus>",
				description = "Animated virus message")
	async def virus(self, ctx, user: discord.Member = None, *, virus: str = "trojan"):
		user = user or ctx.author
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
		    await ctx.message.edit(content=i)

	@commands.command(name = "cathi",
						usage="[text]",
						description = "Cute cat animation")
	async def cathi(self, ctx, *, text: str = "Hi..."):
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
				await ctx.message.edit(content=cat)

	@commands.command(name = "flop",
						usage="",
						description = "Flop animation")
	async def flop(self, ctx):
		list = (
			"(   ° - °) (' - '   )",
			"(\\\° - °)\ (' - '   )",
			"(—°□°)— (' - '   )",
			"(╯°□°)╯(' - '   )",
			"(╯°□°)╯︵(\\\ .o.)\\",
		)
		for i in list:
			await asyncio.sleep(2)
			await ctx.message.edit(content=i)

	@commands.command(name = "poof",
						usage="",
						description = "Poof animation")
	async def poof(self, ctx):
		list = ("(   ' - ')", "' - ')", "- ')", "')", ")", "*poofness*")
		for i in list:
			await asyncio.sleep(2)
			await ctx.message.edit(content=i)

	@commands.command(name = "boom",
						usage="",
						description = "Boom animation")
	async def boom(self, ctx):
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
			await ctx.message.edit(content=i)

	@commands.command(name = "tableflip",
						usage="",
						description = "Tableflip/rage animation")
	async def tableflip(self, ctx):
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
			await ctx.message.edit(content=i)

	@commands.command(name = "warning",
						usage="",
						description = "System overload warning animation")
	async def warning(self, ctx):
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
			await ctx.message.edit(content=i)

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
	async def encode(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Encoding text", description=f"{descriptionvar()}```\n{prefix}encode_cea256 <key> <text>\nEncode a text with cea256 encryption\n\n{prefix}encode_base64 <text>\nEncode a text with base64\n\n{prefix}encode_leet <text>\nEncode a text with leet\n\n{prefix}encode_md5 <text>\nEncode a text with md5 (oneway)\n\n{prefix}encode_sha1 <text>\nEncode a text with sha1 (oneway)\n\n{prefix}encode_sha224 <text>\nEncode a text with sha224 (oneway)\n\n{prefix}encode_sha256 <text>\nEncode a text with sha256 (oneway)\n\n{prefix}encode_sha384 <text>\nEncode a text with sha384 (oneway)\n\n{prefix}encode_sha512 <text>\nEncode a text with sha512 (oneway)```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "decode",
					usage="",
					description = "Decoding text commands")
	async def decode(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Decoding text", description=f"{descriptionvar()}```\n{prefix}decode_cea256 <key> <text>\nDecode a text with cea256 encryption\n\n{prefix}decode_base64 <text>\nDecode a text with base64\n\n{prefix}decode_leet <text>\nDecode a text with leet```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "embed",
					usage="<text>",
					description = "Text in a embed")
	async def embed(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		await ctx.send(embed=embed)
	
	@commands.command(name = "embed_title",
					usage="<text>",
					description = "Text in a embed (as title)")
	async def embed_title(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar() ,description=f"{text}", color=hexcolorvar())
		await ctx.send(embed=embed)

	@commands.command(name = "embed_thumbnail",
					usage="<text>",
					description = "Text in a embed (with thumbnail)")
	async def embed_thumbnail(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		await ctx.send(embed=embed)

	@commands.command(name = "embed_footer",
					usage="<text>",
					description = "Text in a embed (with footer)")
	async def embed_footer(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		await ctx.send(embed=embed)

	@commands.command(name = "embed_author",
					usage="<text>",
					description = "Text in a embed (with author)")
	async def embed_author(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await ctx.send(embed=embed)

	@commands.command(name = "embed_image",
					usage="<text>",
					description = "Text in a embed (with image)")
	async def embed_image(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		embed.set_image(url=largeimagevar())
		await ctx.send(embed=embed)

	@commands.command(name = "embed_all",
					usage="<text>",
					description = "Text in a embed (all theme settings)")
	async def embed_all(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(description=f"{text}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await ctx.send(embed=embed)

	@commands.command(name = "ascii",
					usage="<text>",
					description = "Ascii text")
	async def ascii(self, ctx, *, text:str):
		await ctx.message.delete()
		r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
		if len('```' + r + '```') > 2000:
			return
		await ctx.send(f"```{r}```")

	@commands.command(name = "vape",
					usage="<text>",
					aliases=['vaporwave'],
					description = "Vaporwave text")
	async def vape(self, ctx, *, text:str):
		await ctx.message.delete()
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
		await ctx.send(f'{text}')

	@commands.command(name = "zalgo",
					usage="<text>",
					description = "Zalgo text")
	async def zarlgo(self, ctx, *, text:str):
		await ctx.message.delete()

		await ctx.send(zalgoText(text))

	@commands.command(name = "reverse",
					usage="<text>",
					description = "Reverse given text")
	async def reverse(ctx, *, text):
		await ctx.message.delete()
		text = text[::-1]
		await ctx.send(text)

	@commands.command(name = "bold",
					usage="<text>",
					description = "Bold text format")
	async def bold(self, ctx, *, text:str):
		await ctx.message.delete()
		await ctx.send(f"**{text}**")

	@commands.command(name = "spoiler",
					usage="<text>",
					description = "Spoiler text format")
	async def spoiler(self, ctx, *, text:str):
		await ctx.message.delete()

		await ctx.send(f"||{text}||")

	@commands.command(name = "underline",
					usage="<text>",
					description = "Underline text format")
	async def underline(self, ctx, *, text:str):
		await ctx.message.delete()

		await ctx.send(f"__{text}__")

	@commands.command(name = "strike",
					usage="<text>",
					description = "Strike text format")
	async def strike(self, ctx, *, text:str):
		await ctx.message.delete()

		await ctx.send(f"~~{text}~~")

	@commands.command(name = "css",
					usage="<text>",
					description = "CSS text format")
	async def css(self, ctx, *, text:str):
		await ctx.message.delete()

		await ctx.send(f"```css\n{text}\n```")
	
	@commands.command(name = "brainfuck",
					usage="<text>",
					description = "Brainfuck text format")
	async def brainfuck(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```brainfuck\n{text}\n```")

	@commands.command(name = "md",
					usage="<text>",
					description = "MD text format")
	async def md(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```md\n{text}\n```")

	@commands.command(name = "fix",
					usage="<text>",
					description = "Fix text format")
	async def fix(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```fix\n{text}\n```")

	@commands.command(name = "glsl",
					usage="<text>",
					description = "Glsl text format")
	async def glsl(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```glsl\n{text}\n```")

	@commands.command(name = "diff",
					usage="<text>",
					description = "Diff text format")
	async def diff(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```diff\n{text}\n```")
		
	@commands.command(name = "bash",
					usage="<text>",
					description = "Bash text format")
	async def bash(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```bash\n{text}\n```")
		
	@commands.command(name = "cs",
					usage="<text>",
					description = "CS text format")
	async def cs(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```cs\n{text}\n```")

	@commands.command(name = "ini",
					usage="<text>",
					description = "Ini text format")
	async def ini(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```ini\n{text}\n```")

	@commands.command(name = "asciidoc",
					usage="<text>",
					description = "Asciidoc text format")
	async def asciidoc(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```asciidoc\n{text}\n```")

	@commands.command(name = "autohotkey",
					usage="<text>",
					description = "Autohotkey text format")
	async def autohotkey(self, ctx, *, text:str):
		await ctx.message.delete()
		
		await ctx.send(f"```autohotkey\n{text}\n```")

bot.add_cog(TextCog(bot))

class ImageCog(commands.Cog, name="Image commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "nsfw",
					usage="",
					description = "NSFW commands")
	async def nsfw(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="NSFW commands", description=f"{descriptionvar()}```\n{prefix}lewdneko         » Random lewdneko image\n{prefix}hentai           » Random hentai image\n{prefix}hentaiass        » Random hentai ass\n{prefix}boobs            » Random image of boobs\n{prefix}tits             » Random image of tits\n{prefix}anal             » Random anal image\n{prefix}cumslut          » Random image of a cumslut\n{prefix}blowjob          » Random blowjob image\n{prefix}lesbian          » Random lesbian image\n{prefix}yaoi             » Random image of yaoi```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	# ///////////////////////////////////////////////////////////////
	# Avatar commands

	@commands.command(name = "avatar",
					usage="<@member>",
					aliases=["av"],
					description = "Display someones avatar")
	async def av(self, ctx, user_id):
		await ctx.message.delete()
		if "<@!" and ">" in user_id:
			user_id = user_id.replace("<@!", "").replace(">", "")
			user = await self.bot.fetch_user(user_id)
		else:
			user = await self.bot.fetch_user(user_id)
		embed = discord.Embed(title=f"{user}'s avatar", color=hexcolorvar())
		embed.set_image(url=user.avatar_url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await send(ctx, embed)

	@commands.command(name = "avatart",
					usage="<@member> <text>",
					asliases=["avt"],
					description = "Display someones avatar with a text")
	async def avatart(self, ctx, member: discord.Member, *, text: str):
		await ctx.message.delete()
		embed = discord.Embed(title=text,color=hexcolorvar())
		embed.set_image(url=member.avatar_url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await send(ctx, embed)

	@commands.command(name = "searchav",
					usage="<@member>",
					description = "Returns a search link of someones avatar")
	async def searchav(self, ctx, member: discord.Member):
		await ctx.message.delete()
		embed = discord.Embed(title=f"Search link for {member}'s avatar",description=f"https://images.google.com/searchbyimage?image_url={member.avatar_url}" ,color=hexcolorvar())
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await send(ctx, embed)

	@commands.command(name = "linkav",
					usage="<@member>",
					description = "Returns a link of someones avatar")
	async def linkav(self, ctx, member: discord.Member):
		await ctx.message.delete()
		embed = discord.Embed(title=f"Link for {member}'s avatar",description=f"{member.avatar_url}" ,color=hexcolorvar())
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await send(ctx, embed)

	@commands.command(name = "stealav",
					usage="<@member>",
					description = "Steal someones avatar")
	async def stealav(self, ctx, member: discord.Member):
		await ctx.message.delete()
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
			embed = discord.Embed(description=f"**Stole {member}'s avatar!**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		except discord.HTTPException as e:
			printerror(f"{e}")

	@commands.command(name = "setav",
					usage="<url>",
					description = "Set your avatar")
	async def setav(self, ctx, url: str):
		await ctx.message.delete()
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
			embed = discord.Embed(description=f"**Set new avatar to:**\n{url}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		except discord.HTTPException as e:
			printerror(f"{e}")

	@commands.command(name = "invisav",
					usage="",
					description = "Set your avatar to an invisible one")
	async def invisav(self, ctx):
		await ctx.message.delete()
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
			embed = discord.Embed(description=f"**Set your avatar to invisible**" ,color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		except discord.HTTPException as e:
			printerror(f"{e}")

	# ///////////////////////////////////////////////////////////////
	# Fun image commands
        
	@commands.command(name = "dog",
					usage="",
					description = "Send a random dog")
	async def dog(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://dog.ceo/api/breeds/image/random").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['message']))
		await send(ctx, embed)

	@commands.command(name = "fox",
					usage="",
					description = "Send a random fox")
	async def fox(self, ctx):
		await ctx.message.delete()
		r = requests.get('https://randomfox.ca/floof/').json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['image']))
		await send(ctx, embed)
			
	@commands.command(name = "cat",
					usage="",
					description = "Send a random cat")
	async def cat(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://api.thecatapi.com/v1/images/search").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r[0]["url"]))
		await send(ctx, embed)


	@commands.command(name = "sadcat",
					usage="",
					description = "Send a random sad cat")
	async def sadcat(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://api.alexflipnote.dev/sadcat").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['file']))
		await send(ctx, embed)

	@commands.command(name = "waifu",
					usage="",
					description = "Send a random waifu")
	async def waifu(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/waifu").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await send(ctx, embed)

	# ///////////////////////////////////////////////////////////////
	# Image commands

	@commands.command(name = "wallpaper",
					usage="",
					description = "Send a random anime wallpaper")
	async def wallpaper(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/wallpaper").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await send(ctx, embed)
	
	@commands.command(name = "wide",
					usage="<@member>",
					description = "Wide profile picture")
	async def wide(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/wide?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(ctx, embed)

	@commands.command(name = "trumptweet",
					usage="<text>",
					description = "Create a Trump tweet")
	async def trumptweet(self, ctx, *, text:str):
		await ctx.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=trumptweet&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(ctx, embed)

	@commands.command(name = "bidentweet",
					usage="<text>",
					description = "Create a Biden tweet")
	async def bidentweet(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f'https://api.popcatdev.repl.co/biden?text={str(urllib.parse.quote(text))}')
		await send(ctx, embed)

	@commands.command(name = "tweet",
					usage="<name> <text>",
					description = "Create a tweet")
	async def tweet(self, ctx, name, *, text:str):
		await ctx.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=tweet&username={name}&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(ctx, embed)

	@commands.command(name = "supreme",
					usage="<text>",
					description = "Custom supreme logo")
	async def supreme(self, ctx, *, text:str):
		await ctx.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=supreme&text={str(urllib.parse.quote(text))}').json()['url']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f'{request}')
		await send(ctx, embed)

	@commands.command(name = "changemymind",
					usage="<text>",
					description = "Changemymind meme")
	async def changemymind(self, ctx, *, text:str):
		await ctx.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=changemymind&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(ctx, embed)

	@commands.command(name = "phcomment",
					aliases=['pornhubcomment'],
					usage="<@member> <text>",
					description = "Pornhub comment")
	async def phcomment(self, ctx, user: discord.User, *, text: str):
		await ctx.message.delete()
		image_url = str(user.avatar_url).replace(".webp", ".png")
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=phcomment&image={image_url}&username={urllib.parse.quote(user.name)}&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(ctx, embed)

	@commands.command(name = "clyde",
					usage="<text>",
					description = "Custom Clyde message")
	async def clyde(self, ctx, *, text:str):
		await ctx.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=clyde&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=link)
		await send(ctx, embed)

	@commands.command(name = "pikachu",
					usage="<text>",
					description = "Surprised Pikachu")
	async def pikachu(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.popcatdev.repl.co/pikachu?text={urllib.parse.quote(str(text))}")
		await send(ctx, embed)

	@commands.command(name = "stonks",
					usage="<@member>",
					description = "Stonks!")
	async def stonks(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/stonks?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(ctx, embed)

	@commands.command(name = "notstonks",
					usage="<@member>",
					description = "Notstonks!")
	async def notstonks(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/stonks?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}&notstonks=true")
		await send(ctx, embed)

	@commands.command(name = "emergencymeeting",
					usage="<text>",
					description = "Emergency meeting!")
	async def emergencymeeting(self, ctx, *, text):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/emergencymeeting?text={urllib.parse.quote(text)}")
		await send(ctx, embed)

	@commands.command(name = "eject",
					usage="<true/false> <color> <@member>",
					description = "Among Us eject")
	async def eject(self, ctx, impostor: bool, crewmate: str, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/ejected?name={urllib.parse.quote(user.name)}&impostor={impostor}&crewmate={crewmate}")
		await send(ctx, embed)

	@commands.command(name = "drip",
					usage="<@member>",
					description = "Drip meme")
	async def drip(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/drip?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(ctx, embed)

	@commands.command(name = "gun",
					usage="<@member>",
					description = "Gun meme")
	async def gun(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.popcatdev.repl.co/gun?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(ctx, embed)

	@commands.command(name = "ad",
					usage="<@member>",
					description = "Make yourself an ad")
	async def ad(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.popcatdev.repl.co/ad?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(ctx, embed)

	@commands.command(name = "alert",
					usage="<text>",
					description = "Iphone alert")
	async def alert(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.popcatdev.repl.co/alert?text={urllib.parse.quote(str(text))}")
		await send(ctx, embed)

	@commands.command(name = "caution",
					usage="<text>",
					description = "Caution image")
	async def caution(self, ctx, *, text:str):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://api.popcatdev.repl.co/caution?text={urllib.parse.quote(str(text))}")
		await send(ctx, embed)

	@commands.command(name = "distractedbf",
					usage="<@boyfriend> <@woman> <@girlfriend>",
					description = "Distracted boyfriend meme")
	async def distractedbf(self, ctx, boyfriend: discord.User, woman: discord.User, girlfriend: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/distractedbf?boyfriend={urllib.parse.quote(str(boyfriend.avatar_url).replace('webp', 'png'))}&woman={urllib.parse.quote(str(woman.avatar_url).replace('webp', 'png'))}&girlfriend={urllib.parse.quote(str(girlfriend.avatar_url).replace('webp', 'png'))}")
		await send(ctx, embed)

	@commands.command(name = "icanmilkyou",
					usage="<@member1> <@member2>",
					description = "I can milk you")
	async def icanmilkyou(self, ctx, user1: discord.User, user2: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/icanmilkyou?user1={urllib.parse.quote(str(user1.avatar_url).replace('webp', 'png'))}&user2={urllib.parse.quote(str(user2.avatar_url).replace('webp', 'png'))}")
		await send(ctx, embed)

	@commands.command(name = "heaven",
					usage="<@member>",
					description = "Heaven meme")
	async def heaven(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/heaven?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(ctx, embed)

	@commands.command(name = "dockofshame",
					usage="<@member>",
					description = "Heaven meme")
	async def dockofshame(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/dockofshame?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(ctx, embed)

	@commands.command(name = "firsttime",
					usage="<@member>",
					description = "First time? meme")
	async def dockofshame(self, ctx, user: discord.User):
		await ctx.message.delete()
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f"https://vacefron.nl/api/firsttime?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(ctx, embed)

	@commands.command(name = "drake",
					usage="<no, yes>",
					description = "Drake yes and no meme")
	async def drake(self, ctx, *, text:str):
		await ctx.message.delete()
		text = text.split(', ')
		text1 = text[0]
		text2 = text[1]
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=f'https://api.popcatdev.repl.co/drake?text1={str(urllib.parse.quote(text1))}&text2={str(urllib.parse.quote(text2))}')
		await send(ctx, embed)

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
	async def ghostping(self, ctx):
		await ctx.message.delete()
        
	@commands.command(name = "empty",
					usage="",
					description = "Sends a empty message")
	async def empty(self, ctx):
		await ctx.message.delete()
		await ctx.send("​")

	@commands.command(name = "copy",
					usage="<@member>",
					aliases=['copycat'],
					description = "Copy every message a member")
	async def copy(self, ctx, member:discord.User):
		await ctx.message.delete()

		copycat = member
		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nNow copying {copycat}\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Now copying {copycat}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete()

	@commands.command(name = "stopcopy",
					usage="",
					aliases=['stopcopycat'],
					description = "Copy every message a member")
	async def stopcopy(self, ctx):
		await ctx.message.delete()

		global copycat

		if copycat is None:
			if mode() == 2:
				sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nNo one was getting copied.\n\n[ {footervar()} ]```")
				await asyncio.sleep(deletetimer())
				await sent.delete()
			else:
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"No one was getting copied.", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				sent = await ctx.send(embed=embed)
				await asyncio.sleep(deletetimer())
				await sent.delete()
			return

		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nStopped copying {copycat}\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Stopped copying {copycat}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete()

		copycat = None

	@commands.command(name = "fakenitro",
					usage="[amount]",
					description = "Generate fake nitro links")
	async def fakenitro(self, ctx, amount: int = None):
		await ctx.message.delete()
		try:
			if amount is None:
				await ctx.send(Nitro())
			else:
				for each in range(0, amount):
					await ctx.send(Nitro())
		except Exception as e:
			await ctx.send(f"Error: {e}")

	@commands.command(name = "trollnitro",
					usage="",
					description = "Send a used nitro link")
	async def trollnitro(self, ctx):
		await ctx.message.delete()
		await ctx.send("https://discord.gift/6PWNmA6NTuRkejaP")

	@commands.command(name = "mreact",
					usage="",
					description = "Mass spams reacts on latest message")
	async def mreact(self, ctx):
	    await ctx.message.delete()
	    messages = await ctx.message.channel.history(limit=1).flatten()
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
	async def fakenuke(self, ctx):
		await ctx.message.delete()
		message = await ctx.send(content=':bomb: :bomb: Nuking this server in 5 :rotating_light:')
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
	async def impersonate(self, ctx, user: discord.User, *, message: str):
		await ctx.message.delete()
		webhook = await ctx.channel.create_webhook(name=user.name)
		await webhook.send(message, username=user.name, avatar_url=user.avatar_url)
		await webhook.delete()

	@commands.command(name = "shoot",
					usage="<@member>",
					description = "Shoot up someone")
	async def shoot(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to shoot up? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			embed = discord.Embed(description=f"{user.mention} got shot up!", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url="https://media1.tenor.com/images/cfb7817a23645120d4baba2dcb9205e0/tenor.gif")
			await ctx.send(embed=embed)

	@commands.command(name = "feed",
					usage="<@member>",
					description = "Feed someone")
	async def feed(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to feed? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/feed").json()
			embed = discord.Embed(description=f"{ctx.author.mention} feeds {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))
			await ctx.send(embed=embed)

	@commands.command(name = "kiss",
					usage="<@member>",
					description = "Kiss someone")
	async def kiss(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to kiss? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/kiss").json()
			embed = discord.Embed(description=f"{ctx.author.mention} kisses {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))
			await ctx.send(embed=embed)

	@commands.command(name = "hug",
					usage="<@member>",
					description = "Hug someone")
	async def hug(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to hug? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/hug").json()
			embed = discord.Embed(description=f"{ctx.author.mention} hugs {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))
			await ctx.send(embed=embed)

	@commands.command(name = "pat",
					usage="<@member>",
					description = "Pat someone")
	async def pat(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to pat? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/pat").json()
			embed = discord.Embed(description=f"{ctx.author.mention} pats {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))

	@commands.command(name = "slap",
					usage="<@member>",
					description = "Slap someone")
	async def slap(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to slap? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/slap").json()
			embed = discord.Embed(description=f"{ctx.author.mention} slaps {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))

	@commands.command(name = "tickle",
					usage="<@member>",
					description = "Tickle someone")
	async def tickle(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user == None:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Who do you want to tickle? Please mention someone.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await ctx.send(embed=embed)
			return
		else:
			r = requests.get("https://nekos.life/api/v2/img/tickle").json()
			embed = discord.Embed(description=f"{ctx.author.mention} tickles {user.mention}", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=str(r['url']))

	@commands.command(name = "fml",
					usage="",
					description = "Fuck my life situation")
	async def fml(self, ctx):
		await ctx.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=fml')
		data = request.json()
		text = data['text']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f'{text}', color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)
        
	@commands.command(name = "gay",
					usage="<@member>",
					description = "Gay rate somebody")
	async def gay(self, ctx, user: discord.Member = None):
		await ctx.message.delete()

		if user is None:
			user = ctx.author
		size = random.randint(1, 100)
		embed = discord.Embed(title=f"{user}'s Gay Rate", description=f"{size}% Gay 🏳️‍🌈", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "coronatest",
					usage="<@member>",
					description = "Test somebody for Corona")
	async def coronatest(self, ctx, user: discord.Member = None):
		await ctx.message.delete()

		if user is None:
			member = ctx.author
		else:
			member = user
		random.seed((member.id * 6) / 2)
		percent = random.randint(0, 100)
		embed = discord.Embed(title=f"{user}'s Corona Test", description=f'{percent}% positive!\n\nResult: Overall: {"**Positive**" if (percent > 50) else "**Negative**"}', color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "8ball",
					usage="<question>",
					description = "Ask 8 Ball!")
	async def _8ball(self, ctx, *, question:str):
		await ctx.message.delete()
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
		await send(ctx, embed)

	@commands.command(name = "slot",
					usage="",
					aliases=['slots'],
					description = "Play slots")
	async def slot(self, ctx):
		await ctx.message.delete()
		emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
		a = random.choice(emojis)
		b = random.choice(emojis)
		c = random.choice(emojis)
		slotmachine = f"**------------------\n| {a} | {b} | {c} |\n------------------\n\n{ctx.author.name}**,"
		if (a == b == c):
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} All matchings, you won!", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			await send(ctx, embed)
		elif (a == b) or (a == c) or (b == c):
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} 2 in a row, you won!", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} No match, you lost!", color=hexcolorvar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			await send(ctx, embed)

	@commands.command(name = "dadjoke",
					usage="",
					description = "Dad jokes")
	async def dadjoke(self, ctx):
		await ctx.message.delete()
		request = requests.get(f'https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
		data = request.json()
		joke = data['joke']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f'{joke}', color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "joke",
					usage="",
					description = "Random jokes")
	async def dadjoke(self, ctx):
		await ctx.message.delete()
		request = requests.get(f'http://www.official-joke-api.appspot.com/random_joke')
		data = request.json()
		setup = data['setup']
		punchline = data['punchline']
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f'{setup}\n\n||{punchline}||', color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "coinflip",
					usage="",
					description = "Flip a coin")
	async def coinflip(self, ctx):
		await ctx.message.delete()
		lista = ['head', 'tails']
		coin = random.choice(lista)
		try:
			if coin == 'head':
				embed = discord.Embed(title="Head", color=hexcolorvar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_thumbnail(url="https://webstockreview.net/images/coin-clipart-dime-6.png")
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				await send(ctx, embed)
			else:
				embed = discord.Embed(title="Tails", color=hexcolorvar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				await send(ctx, embed)
		except discord.HTTPException:
			if coin == 'head':
				await ctx.send("Coinflip: **Head**")
			else:
				await ctx.send("Coinflip: **Tails**")

	@commands.command(name = "prntsc",
						usage="",
						description = "Send a random screenshot from prnt.sc")
	async def prntsc(self, ctx):
		await ctx.message.delete()
		await ctx.send(Randprntsc())

	@commands.command(name = "farmer",
						usage="",
						description = "Dank Memer farmer")
	async def farmer(self, ctx):
		await ctx.message.delete()
		global farming
		farming = True
		while farming:
			await ctx.send("pls beg")
			await asyncio.sleep(3)
			await ctx.send("pls deposit all")
			await asyncio.sleep(42)

	@commands.command(name = "afarmer",
						usage="",
						description = "Advanced Dank Memer farmer")
	async def afarmer(self, ctx):
		await ctx.message.delete()
		global farming
		farming = True
		while farming:
			await ctx.send("pls beg")
			await asyncio.sleep(3)
			await ctx.send("pls deposit all")
			await asyncio.sleep(3)
			await ctx.send("pls postmeme")
			await asyncio.sleep(3)
			await ctx.send("n")
			await asyncio.sleep(3)
			await ctx.send("pls fish")
			await asyncio.sleep(33)


	@commands.command(name = "stopfarmer",
						usage="",
						description = "Stops the Dank Memer farmer")
	async def stopfarmer(self, ctx):
		await ctx.message.delete()
		global farming
		farming = False

bot.add_cog(FunCog(bot))

class ToolsCog(commands.Cog, name="Tools commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "poll",
					usage="<question>",
					description = "Create a poll")
	async def poll(self, ctx, *, question):
		await ctx.message.delete()
		embed = discord.Embed(title=f"Poll", description=f"{question}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		message = await ctx.send(embed=embed)
		await message.add_reaction('👍')
		await message.add_reaction('👎')

	@commands.command(name = "cpoll",
					usage="<option1> <option2> <question>",
					description = "Create a poll")
	async def cpoll(self, ctx, option1, option2, *, poll):
		await ctx.message.delete()
		embed = discord.Embed(title=f"Poll", description=f"{poll}\n\n🅰️ = {option1}\n🅱️ = {option2}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		message = await ctx.send(embed=embed)
		await message.add_reaction('🅰️')
		await message.add_reaction('🅱️')

	@commands.command(name = "hiddenping",
					usage="<channel_id> <user_id> <message>",
					description = "Ping someone without showing @member")
	async def hiddenping(self, ctx, channel_id: int, user_id, *, message):
		await ctx.message.delete()

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

		embed = discord.Embed(title=f"Hidden Ping", description=f"Ping sent!\n\nChannel ID: {cchannel}\nChannel Name: {channel.name}\nUser ID: {user_id}\nUser Name: {cuser.name}#{cuser.discriminator}\nMessage: {message}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "hiddeneveryone",
					usage="<channel_id> <message>",
					description = "Ping everyone without showing @everyone")
	async def hiddeneveryone(self, ctx, channel_id: int, *, message):
		await ctx.message.delete()

		user = "@everyone"

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + user)

		embed = discord.Embed(title=f"Hidden Everyone", description=f"Ping sent!\n\nChannel ID: {channel_id}\nChannel Name: {cchannel.name}\nMessage: {message}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "hiddeninvite",
					usage="<channel_id> <invite> <message>",
					description = "hide the invite")
	async def hiddeninvite(self, ctx, channel_id: int, invite, *, message):
		await ctx.message.delete()

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + invite)

		embed = discord.Embed(title=f"Hidden Ping", description=f"Ping sent!\n\nChannel ID: {cchannel}\nChannel Name: {channel.name}\nInvite: {invite}\nMessage: {message}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "hiddenurl",
					usage="<channel_id> <url> <message>",
					description = "Hide the url")
	async def hiddenurl(self, ctx, channel_id: int, url, *, message):
		await ctx.message.delete()

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(message + charTT + url)

		embed = discord.Embed(title=f"Hidden Ping", description=f"Ping sent!\n\nChannel ID: {cchannel}\nChannel Name: {channel.name}\nURL: {url}\nMessage: {message}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "channels",
					usage="[guild_id]",
					description = "Show all the channels")
	async def channels(self, ctx, server_id:int=None):
		await ctx.message.delete()
		if server_id is None:
			server = discord.utils.get(ctx.bot.guilds, id=ctx.guild.id)
		else: 
			server = discord.utils.get(ctx.bot.guilds, id=server_id)
		channels = server.channels
		channel_list = []
		for channel in channels:
			channel_list.append(channel)
		embed = discord.Embed(title=f"Channels in {server}", description='\n'.join([f"{ch.name}" for ch in channel_list]) or 'None', color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "firstmsg",
					usage="[#channel]",
					description = "Shows the first message in the channel")
	async def firstmsg(self, ctx, channel: discord.TextChannel = None):
		await ctx.message.delete()
		if channel is None:
			channel = ctx.channel
		first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
		embed = discord.Embed(title="First Message", description=f"[Jump]({first_message.jump_url})", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "compareservers",
					usage="<serverid1> <serverid2>",
					description = "Checks if members are in the same server")
	async def compareservers(self, ctx, server_id:int, server_id_2:int):
		await ctx.message.delete()

		server_1 = self.bot.get_guild(server_id)
		server_2 = self.bot.get_guild(server_id_2)
		output = ""
		count = 0
		for member in server_1.members:
			if member in server_2.members:
				output += "{}\n".format(str(member.mention))
				count += 1

		embed = discord.Embed(title=f"Members in the same server: {count}", url=titleurlvar(), description=f"**{server_1}** - **{server_2}**\n\n{output}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "bots",
					usage="",
					description = "Show all bots in the guild")
	async def bots(self, ctx):
		await ctx.message.delete()
		bots = []
		for member in ctx.guild.members:
			if member.bot:
				bots.append(str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
		botslist = f"{', '.join(bots)}".replace(',', "\n")
		embed = discord.Embed(title=f"Bots ({len(bots)})", url=titleurlvar(), description=f"{botslist}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "guildicon",
					usage="",
					description = "Show the guild icon")
	async def guildicon(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title=ctx.guild.name, url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=ctx.guild.icon_url)
		await send(ctx, embed)

	@commands.command(name = "guildbanner",
					usage="",
					description = "Show the guild banner")
	async def guildbanner(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title=ctx.guild.name, url=titleurlvar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=ctx.guild.banner_url)
		await send(ctx, embed)

	@commands.command(name = "tts",
					usage="<language> <text>",
					description = "Text to speech")
	async def tts(self, ctx, lang, *, text: str):
		await ctx.message.delete()
		tts = gTTS(text, lang=lang)
		filename = f'{text}.mp3'
		tts.save(filename)
		await ctx.send(file=discord.File(fp=filename, filename=filename))
		if os.path.exists(filename):
			os.remove(filename)

bot.add_cog(ToolsCog(bot))

class NettoolCog(commands.Cog, name="Nettool commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "ping",
					usage="",
					description = "Display the latency")
	async def ping(self, ctx):
		await ctx.message.delete()

		if mode() == 2:
			before = time.monotonic()
			sent = await ctx.send(f"```ini\n[ Latency ]\n\nPinging...\n\n[ {footervar()} ]```")
			ping = (time.monotonic() - before) * 100
			await sent.edit(content=f"```ini\n[ Latency ]\n\nAPI Latency\n{int(ping)}ms\n\n[ {footervar()} ]```")
		if mode() == 3:
			before = time.monotonic()
			sent = await ctx.send(f"> **Latency**\n> \n> Pinging...\n> \n> {footervar()}")
			ping = (time.monotonic() - before) * 100
			await sent.edit(content=f"> **Latency**\n> \n> API Latency\n> {int(ping)}ms\n> \n> {footervar()}")
		else:
			embed = discord.Embed(title="Latency", url=titleurlvar(), description=f"Pinging...", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			before = time.monotonic()
			sent = await ctx.send(embed=embed)
			ping = (time.monotonic() - before) * 100
			embed = discord.Embed(title="Latency", url=titleurlvar(), description=f"**API Latency**\n{int(ping)}ms", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await sent.edit(embed=embed)

	@commands.command(name = "ip",
						usage="",
						description = "Display information about given ip")
	async def ip(self, ctx, ip:str):
		await ctx.message.delete()
		if ip is None:
			await ctx.send("Please specify a IP address")
			return
		else:
			try:
				with requests.session() as ses:
					resp = ses.get(f'https://ipinfo.io/{ip}/json')
					if "Wrong ip" in resp.text:
						await ctx.send("Invalid IP address")
						return
					else:
						try:
							j = resp.json()
							embed = discord.Embed(title=f"IP: {ip}", url=titleurlvar(), description=f'```\nCity\n{j["city"]}\n``````\nRegion\n{j["region"]}\n``````\nCountry\n{j["country"]}\n``````\nCoordinates\n{j["loc"]}\n``````\nPostal\n{j["postal"]}\n``````\nTimezone\n{j["timezone"]}\n``````\nOrganization\n{j["org"]}```', color=hexcolorvar())
							embed.set_thumbnail(url=imagevar())
							embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
							embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
							embed.set_image(url=largeimagevar())
							await send(ctx, embed)
						except discord.HTTPException:
							await ctx.send(
								f'**{ip} Info**\n\nCity: {j["city"]}\nRegion: {j["region"]}\nCountry: {j["country"]}\nCoordinates: {j["loc"]}\nPostal: {j["postal"]}\nTimezone: {j["timezone"]}\nOrganization: {j["org"]}')
			except Exception as e:
				await ctx.send(f"Error: {e}")				

	@commands.command(name="tcpping", usage="<ip> <port>", description="Checks if the host is online by connecting to the port")
	async def tcpping(self, ctx, ip, port):
		await ctx.message.delete()
		if ip is None:
			await ctx.send("Please specify a IP address")
			return
		if port is None:
			await ctx.send("Please specify a port")
			return
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.3)
		try:
			sock.connect((ip, int(port)))
		except:
			embed = discord.Embed(title="__TCP-Ping__", description=f"**Status:** Offline\n**IP:** {ip}\n**Port:** {port}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="__TCP-Ping__", description=f"**Status:** Online\n**IP:** {ip}\n**Port:** {port}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name="portscan", usage="<ip>", description="Checks for common open ports")
	async def portscan(self, ctx, ip):
		await ctx.message.delete()
		if ip is None:
			await ctx.send("Please specify a IP address")
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

		embed = discord.Embed(title="Port Scanner", description=f'**IP:** {ip}\n**Ports Checked:** {",".join(ports)}\n**Open Ports:** {",".join(open_ports)}', color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)


	@commands.command(name="resolve", usage="<url>", description="Gets the urls/website's host IP")
	async def resolve(self, ctx, url):
		await ctx.message.delete()
		import socket
		new_url = ""
		if url is None:
			await ctx.send("Please specify a URL")
			return
		if url.startswith("https://"):
			new_url = url.replace("https://", "")
		elif url.contains("http://"):
			new_url = url.replace("http://", "")
		
		try:
			ip = socket.gethostbyname(new_url)
		except:
			await ctx.send("URL is invalid")
			return
		embed = discord.Embed(title="Host Resolver", description=f"**URL:** {url}\n**IP:** {ip}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name="scrapeproxies", usage="", aliases=['proxyscrape', 'scrapeproxy'],description="Scrape for proxies")
	async def scrapeproxies(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title="Scrapeproxies", description=f"Saved all scraped proxies in data/proxies.", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)
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
	async def serverjoiner(self, ctx):
		await ctx.message.delete()
		if riskmode() == "on":

			if file_exist('./data/invites.txt'):
				pass
			else:
				file = open("data/invites.txt", "w") 
				file.write("Put the invites of the servers you want to join here one after another") 
				file.close()
				embed = discord.Embed(title="Server Joiner", url=titleurlvar(), description=f"No invites.txt has been found, so it has been created.\nPut all your invites there that you want to join.", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
				return

			if os.stat("data/invites.txt").st_size == 0:
				embed = discord.Embed(title="Server Joiner", url=titleurlvar(), description=f"invites.txt is empty...", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
				return
			else:
				file = open("data/invites.txt", "r")
				nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
				line_count = len(nonempty_lines)
				file.close()

				with open('./config.json') as f:
					config = json.load(f)
				token = config.get('token')

				embed = discord.Embed(title="Server Joiner", url=titleurlvar(), description=f"Found **{line_count}** invites in invites.txt\nJoining provided invites...", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

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
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "proxyserverjoiner",
					usage="",
					description = "Join all invites in data/invites.txt using proxies")
	async def proxyserverjoiner(self, ctx):
		await ctx.message.delete()
		if riskmode() == "on":

			if file_exist('./data/invites.txt'):
				pass
			else:
				file = open("data/invites.txt", "w") 
				file.write("Put the invites of the servers you want to join here one after another") 
				file.close()
				embed = discord.Embed(title="Server Joiner [PROXY]", url=titleurlvar(), description=f"No invites.txt has been found, so it has been created.\nPut all your invites there that you want to join.", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
				return

			if os.stat("data/invites.txt").st_size == 0:
				embed = discord.Embed(title="Server Joiner [PROXY]", url=titleurlvar(), description=f"invites.txt is empty...", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
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

				embed = discord.Embed(title="Server Joiner [PROXY]", url=titleurlvar(), description=f"Found **{line_count}** invites in invites.txt\nJoining provided invites...", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

				with open("data/invites.txt","r+") as f:
					for line in f:
						invite = line.strip("\n")
						invite = invite.replace('https://discord.gg/', '')
						try:
							async with httpx.AsyncClient() as client:
								await client.post(f'https://canary.discord.com/api/v8/invites/{invite}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}, proxies={'http': f'{proxylist[p]}'})
								printevent(f"[PROXY] Joined {invite}")
								await asyncio.sleep(0.5)
						except Exception:
							printerror(f"[PROXY] Failed to join {invite}")
							pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "addemoji",
					usage="<emoji_name> <image_url>",
					description = "Add an emoji")
	@has_permissions(manage_emojis=True)
	async def addemoji(self, ctx, emoji_name, image_url=None):
		await ctx.message.delete()
		if ctx.message.attachments:
			image = await ctx.message.attachments[0].read()
		elif image_url:
			async with aiohttp.ClientSession() as session:
				async with session.get(image_url) as resp:
					image = await resp.read()
		await ctx.guild.create_custom_emoji(name=emoji_name, image=image)
		embed = discord.Embed(title="Emoji Added", url=titleurlvar(), description=f"{emoji_name}", color=hexcolorvar())
		embed.set_thumbnail(url=image_url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "editemoji",
					usage="<emoji> <new_name>",
					description = "Edit an emoji")
	@has_permissions(manage_emojis=True)
	async def editemoji(self, ctx, emoji: discord.Emoji, new_name):
		await ctx.message.delete()
		oldname = emoji.name
		await emoji.edit(name=new_name)
		embed = discord.Embed(title="Emoji Edited", url=titleurlvar(), description=f"{oldname} to {new_name}", color=hexcolorvar())
		embed.set_thumbnail(url=emoji.url)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "delemoji",
					usage="<emoji>",
					description = "Delete an emoji")
	@has_permissions(manage_emojis=True)
	async def delemoji(self, ctx, emoji: discord.Emoji):
		await ctx.message.delete()
		name = emoji.name
		emojiurl = emoji.url
		await emoji.delete()
		embed = discord.Embed(title="Emoji Deleted", url=titleurlvar(), description=f"{name}", color=hexcolorvar())
		embed.set_thumbnail(url=emojiurl)
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = 'playing', 
				usage="<text>", 
				description = "Change your activity to playing.")
	async def playing(self, ctx, *, status: str = None):
		await ctx.message.delete()
		if status is None:
			printerror("You didnt put a text to play")
		else:
			try:
				game = discord.Activity(type=0, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Status changed to: **Playing {status}**", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
			except Exception as e:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"{e}", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)


	@commands.command(name = 'streaming', 
				usage="<text>", 
				description = "Change your activity to streaming.")
	async def streaming(self, ctx, *, status: str = None):
		await ctx.message.delete()
		if status is None:
			printerror("You didnt put a text to stream")
		else:
			try:
				game = discord.Activity(type=1, name=f"{status}", url=streamurl())
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Status changed to: **Streaming {status}**", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
			except Exception as e:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"{e}", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)


	@commands.command(name = 'listening', 
				usage="<text>", 
				description = "Change your activity to listening.")
	async def listening(self, ctx, *, status: str = None):
		await ctx.message.delete()
		if status is None:
			printerror("You didnt put a text to listen to")
		else:
			try:
				game = discord.Activity(type=2, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Status changed to: **Listening {status}**", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
			except Exception as e:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"{e}", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = 'watching', 
				usage="<text>", 
				description = "Change your activity to watching.")
	async def watching(self, ctx, *, status: str = None):
		await ctx.message.delete()
		if status is None:
			printerror("You didnt put a text to watch")
		else:
			try:
				game = discord.Activity(type=3, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Status changed to: **Watching {status}**", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				send(ctx, embed)
			except Exception as e:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"{e}", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = 'stopactivity', 
				usage="", 
				aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"],
				description = "Stop your activity.")
	async def stopactivity(self, ctx):
		await ctx.message.delete()
		await self.bot.change_presence(activity=None, status=discord.Status.dnd)
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description="Stopped activity", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "clean",
					usage="<amount>",
					description = "Clean your messages")
	async def clean(self, ctx, amount: int = None):
		await ctx.message.delete()
		try:
			if amount is None:
				embed = discord.Embed(title="Error", url=titleurlvar(), description="Invalid amount", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
			else:
				await ctx.channel.purge(limit=amount, before=ctx.message, check=is_me)
		except:
			try:
				await asyncio.sleep(1)
				c = 0
				async for message in ctx.message.channel.history(limit=amount):
					if message.author == self.bot.user:
						c += 1
						await message.delete()
					else:
						pass
			except Exception as e:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"{e}", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = "textreact",
					aliases=['treact'],
					usage="<amount>",
					description = "Text as reaction")
	async def textreact(self, ctx, messageNo: typing.Optional[int] = 1, *, text):
		await ctx.message.delete()
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
		for i, m in enumerate(await ctx.channel.history(limit=100).flatten()):
			if messageNo == i:
				for c in text:
					await m.add_reaction(f"{emotes[c]}")
				break
        
	@commands.command(name = "afk",
					usage="",
					description = "AFK mode on/off")
	async def afk(self, ctx):
		await ctx.message.delete()

		global afkstatus

		if afkstatus == 0:
			afkstatus += 1
			printmessage(f"AFK Mode: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"AFK mode: **on**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif afkstatus == 1:
			afkstatus -= 1
			printmessage(f"AFK Mode: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"AFK mode: **off**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "calc",
					usage="",
					description = "Opens calculator")
	async def calc(self, ctx):
		await ctx.message.delete()
		printcommand("calc")
		from subprocess import call
		call(["calc.exe"])

	@commands.command(name = "passgen",
					usage="",
					description = "Generate a password")
	async def passgen(self, ctx):
		await ctx.message.delete()

		code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Password generated:\n{code}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "invisiblenick",
					usage="",
					description = "Make your nickname invisible")
	async def invisiblenick(self, ctx):
		await ctx.message.delete()

		try:
			name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
			await ctx.message.author.edit(nick=name)
		except Exception as e:
			await ctx.send(f"Error: {e}")

	@commands.command(name = "hypesquad",
					usage="<bravery/brilliance/balance>",
					description = "Change Hypesquad house")
	async def hypesquad(self, ctx, house:str):
		await ctx.message.delete()
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
			embed = discord.Embed(title="Hypesquad", url=titleurlvar(), description=f"Successfully set your hypesquad house to {house}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		except:
			if errorlog() == "console":
				printerror("Failed to set your hypesquad house")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Failed to set your hypesquad house", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = "acceptfriends",
					usage="",
					description = "Accept all friend requests")
	async def acceptfriends(self, ctx):
		await ctx.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship == discord.RelationshipType.incoming_request:
				try:
					await relationship.accept()
					printmessage(f"Accepted {relationship}")
				except Exception:
					pass


	@commands.command(name = "ignorefriends",
					usage="",
					description = "Delete all friend requests")
	async def ignorefriends(self, ctx):
		await ctx.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.incoming_request:
				relationship.delete()
				printmessage(f"Deleted {relationship}")


	@commands.command(name = "delfriends",
					usage="",
					description = "Delete all friends")
	async def delfriends(self, ctx):
		await ctx.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.friend:
				try:
					await relationship.delete()
					printmessage(f"Deleted {relationship}")
				except Exception:
					pass


	@commands.command(name = "clearblocked",
					usage="",
					description = "Delete all blocked friends")
	async def clearblocked(self, ctx):
		await ctx.message.delete()
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
	async def leaveservers(self, ctx):
		await ctx.message.delete()
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
		
	@commands.command(name = "purgehack",
					usage="",
					description = "Purge a channel without permissions")
	async def purgehack(self, ctx):
		await ctx.message.delete()
		if riskmode() == "on":
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await ctx.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
		else:
			if errorlog() == "console":
				printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = "spam",
					usage="<delay> <amount> <message>",
					description = "Spam a message")
	async def spam(self, ctx, delay: int = None, amount: int = None, *, message: str = None):
		await ctx.message.delete()
		if riskmode() == "on":
			try:
				if delay is None or amount is None or message is None:
					await ctx.send(f"Usage: {self.bot.prefix}spam <delay> <amount> <message>")
				else:
					for each in range(0, amount):
						await asyncio.sleep(delay)
						await ctx.send(f"{message}")
			except Exception as e:
				await ctx.send(f"Error: {e}")
		else:
			if errorlog() == "console":
				printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = "spamghostping",
					usage="<delay> <amount> <@member>",
					aliases=['spg', 'spamgp', 'sghostping'],
					description = "Spam ghostping someone")
	async def spamghostping(self, ctx, delay: int = None, amount: int = None, user: discord.Member = None):
		await ctx.message.delete()
		if riskmode() == "on":
			try:
				if delay is None or amount is None or user is None:
					await ctx.send(f"Usage: {self.bot.prefix}spamghostping <delay> <amount> <@member>")
				else:
					for each in range(0, amount):
						await asyncio.sleep(delay)
						await ctx.send(user.mention, delete_after=0)
			except Exception as e:
				await ctx.send(f"Error: {e}")
		else:
			if errorlog() == "console":
				printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = "mpreact",
					usage="<emoji>",
					description = "Reacts to the latest 20 messages")
	async def mpreact(self, ctx, emoji):
		await ctx.message.delete()
		if riskmode() == "on":
			messages = await ctx.message.channel.history(limit=20).flatten()
			for message in messages:
				await message.add_reaction(emoji)
		else:
			if errorlog() == "console":
				printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = "junknick",
					usage="",
					description = "Change your nickname to pure junk")
	async def junknick(self, ctx):
		await ctx.message.delete()
		if riskmode() == "on":
			try:
				name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫"
				await ctx.author.edit(nick=name)
			except Exception as e:
				if errorlog() == "console":
					printerror(e)
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=e, color=0xff0000)
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					await send(ctx, embed)
		else:
			if errorlog() == "console":
				printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = "dmall",
					usage="<message>",
					description = "DM a message to every member")
	async def dmall(self, ctx, *, message: str):
		await ctx.message.delete()
		if riskmode() == "on":
			sent = 0
			try:
				members = ctx.channel.members
				for member in members:
					if member is not ctx.author:
						try:
							await member.send(message)
							printmessage(f"Sent {message} to {member}")
							sent += 1
						except Exception:
							pass
			except Exception:
				pass
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Sent **{message}** to **{sent}** users.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			if errorlog() == "console":
				printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = "sendall",
					usage="<message>",
					description = "Send a message in every channel")
	async def sendall(self, ctx, *, message):
		await ctx.message.delete()
		if riskmode() == "on":
			try:
				channels = ctx.guild.text_channels
				for channel in channels:
					await channel.send(message)
			except:
				pass
		else:
			if errorlog() == "console":
				printerror("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

bot.add_cog(AbuseCog(bot))

class RaidCog(commands.Cog, name="Raid commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "tokencheck",
					usage="",
					description = "Check the tokens.txt for valid tokens")
	async def tokencheck(self, ctx):
		await ctx.message.delete()

		file = open("data/tokens.txt", "r")
		nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
		line_count = len(nonempty_lines)
		file.close()

		if os.stat("data/tokens.txt").st_size == 0:
			embed = discord.Embed(title="Tokencheck", url=titleurlvar(), description=f"tokens.txt is empty...", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
			return

		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ Tokencheck ]\n\nDetected {line_count} tokens.\nChecking tokens...\n\n[ {footervar()} ]```")
		else:
			embed = discord.Embed(title="Tokencheck", url=titleurlvar(), description=f"Detected **{line_count}** tokens.\nChecking tokens...", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)

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
					description = "Raid the server with tokens")
	async def raidjoin(self, ctx, invitelink:str):
		await ctx.message.delete()
		if riskmode() == "on":
		# link = "https://discord.com/api/v6/invites/" + invitelink.split("/")[-1]
		# joined = 0
		# failed = 0

		# if mode() == 2:
		# 	sent = await ctx.send(f"```ini\n[ Raid Join ]\n\nRaiding...\n\n[ {footervar()} ]```")
		# else:
		# 	embed = discord.Embed(title="Raid Join", url=titleurlvar(), description=f"Raiding...", color=hexcolorvar())
		# 	embed.set_thumbnail(url=imagevar())
		# 	embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		# 	embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		# 	embed.set_image(url=largeimagevar())
		# 	sent = await ctx.send(embed=embed)

		# with open("data/tokens.txt","r") as f:
		# 	tokens = f.read().splitlines()
		# 	for token in tokens:
		# 		headers = {"Content-Type": "application/json", 
        #            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        #            "Authorization" : token}
				
		# 		response = post(link, headers=headers).status_code
		# 		if response > 199 and response < 300:
		# 			joined += 1
		# 		else:
		# 			failed += 1

		# if mode() == 2:
		# 	await sent.edit(content=f"```ini\n[ Raid Join ]\n\nAccounts that joined: "+str(joined)+"\nAccounts that could not join: "+str(failed)+f"\n\n[ {footervar()} ]```")
		# 	await asyncio.sleep(deletetimer())
		# 	await sent.delete() 
		# else:
		# 	embed = discord.Embed(title="Raid Join", url=titleurlvar(), description="Accounts that joined: **"+str(joined)+"**\nAccounts that could not join: **"+str(failed)+"**", color=hexcolorvar())
		# 	embed.set_thumbnail(url=imagevar())
		# 	embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		# 	embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		# 	embed.set_image(url=largeimagevar())
		# 	await sent.edit(embed=embed)
		# 	await asyncio.sleep(deletetimer())
		# 	await sent.delete()

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
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "proxyjoin",
					usage="<invitelink>",
					description = "Raid the server with tokens using proxies")
	async def proxyjoin(self, ctx, invitelink:str):
		await ctx.message.delete()
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
						await client.post(f'https://canary.discord.com/api/v8/invites/{invitelink}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http': f'{proxylist[p]}'})
						printevent(f"[PROXY] {_token} joined {invitelink}")
				except Exception:
					printerror(f"[PROXY] {_token} failed to join {invitelink}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "raidspam",
					usage="<channel_id> <amount> <message>",
					description = "Spam the channel with tokens")
	async def raidspam(self, ctx, channel_id:str, amount:int, *, message:str):
		await ctx.message.delete()
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
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "proxyspam",
					usage="<channel_id> <amount> <message>",
					description = "Spam the channel with tokens using proxies")
	async def proxyspam(self, ctx, channel_id:str, amount:int, *, message:str):
		await ctx.message.delete()
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
							await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{message}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http': f'{proxylist[p]}'})
							printevent(f"{_token} sent {message}")
				except Exception:
					printerror(f"{_token} failed to send {message}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "raidleave",
					usage="<server_id>",
					description = "Leave the server with raided tokens")
	async def raidleave(self, ctx, server_id:str):
		await ctx.message.delete()
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
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "proxyleave",
					usage="<server_id>",
					description = "Leave the server with raided tokens using proxies")
	async def proxyleave(self, ctx, server_id:str):
		await ctx.message.delete()
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
						await client.delete(f'https://canary.discord.com/api/v8/users/@me/guilds/{server_id}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http': f'{proxylist[p]}'})
						printevent(f"[PROXY] {_token} left {server_id}")
				except Exception:
					printerror(f"[PROXY] {_token} failed to leave {server_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "raidreact",
					usage="<channel_id> <message_id> <emoji>",
					description = "Leave the server with raided tokens")
	async def raidreact(self, ctx, channel_id: str, message_id: str, emoji: str):
		await ctx.message.delete()
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
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "proxyreact",
					usage="<channel_id> <message_id> <emoji>",
					description = "Leave the server with raided tokens")
	async def proxyreact(self, ctx, channel_id: str, message_id: str, emoji: str):
		await ctx.message.delete()
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
						await client.put(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages/{message_id}/reactions/{urllib.parse.quote(emoji)}/%40me', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http': f'{proxylist[p]}'})
						printevent(f"{_token} reacted on {message_id}")
				except Exception:
					printerror(f"{_token} failed to react on {message_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

bot.add_cog(RaidCog(bot))

start = datetime.now()

class NukingCog(commands.Cog, name="Nuking commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "nuketoken",
					usage="<token>",
					description = "Nuke and destroy the token")
	async def nuketoken(self, ctx, token:str):
		await ctx.message.delete()
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
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "fucktoken",
					usage="<token>",
					description = "Change settings on the token")
	async def nuketoken(self, ctx, token:str):
		await ctx.message.delete()
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
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
        
	@commands.command(name = "massban",
					usage="<guild_id>",
					description = "Massban a guild")
	@has_permissions(ban_members=True)
	async def massban(self, ctx, guild_id:int):
		await ctx.message.delete()
		if riskmode() == "on":
			guild_id = int(guild_id)
			guildhit = self.bot.get_guild(guild_id)
			members = guildhit.members
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for member in members:
				if member is not ctx.author:
					try:
						count = count + 1
						await member.ban()
						printmessage(f"Banned {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
					except Exception:
						printerror(f"Failed to ban {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
			printmessage(f"Finished banning in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "masskick",
					usage="<guild_id>",
					description = "Masskick a guild")
	@has_permissions(kick_members=True)
	async def masskick(self, ctx, guild_id:int):
		await ctx.message.delete()
		if riskmode() == "on":
			guild_id = int(guild_id)
			guildhit = self.bot.get_guild(guild_id)
			members = guildhit.members
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for member in members:
				if member is not ctx.author:
					try:
						count = count + 1
						await member.kick()
						printmessage(f"Kicked {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
					except Exception:
						printerror(f"Failed to kick {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
			printmessage(f"Finished kicking in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "masschannels",
					usage="<guild_id> <amount> <name>",
					description = "Mass create channels")
	@has_permissions(manage_channels=True)
	async def masschannels(self, ctx, guild_id:int, amount:int, *, name:str):
		await ctx.message.delete()
		if riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for i in range(0, amount):
				try:
					await guildhit.create_text_channel(name=f"{name}")
					printmessage(f"Created channel {bcolors.COMMANDVAR}{name}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to create channel {bcolors.COMMANDVAR}{name}{bcolors.RESET}")
			printmessage(f"Finished creating channels in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "massroles",
					usage="<guild_id> <amount> <name>",
					description = "Mass create roles")
	@has_permissions(manage_roles=True)
	async def massroles(self, ctx, guild_id:int, amount:int, *, name:str):
		await ctx.message.delete()
		if riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for i in range(0, amount):
				try:
					await guildhit.create_roles(name=f"{name}")
					printmessage(f"Created role {bcolors.COMMANDVAR}{name}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to create role {bcolors.COMMANDVAR}{name}{bcolors.RESET}")
			printmessage(f"Finished creating roles in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "massdelchannels",
					usage="<guild_id>",
					description = "Mass delete channels")
	@has_permissions(manage_channels=True)
	async def massdelchannels(self, ctx, guild_id:int):
		await ctx.message.delete()
		if riskmode() == "on":
			guildhit = self.bot.get_guild(guild_id)
			channels = guildhit.channels
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for channel in channels:
				try:
					await channel.delete()
					printmessage(f"Deleted channel {bcolors.COMMANDVAR}{channel}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to delete channel {bcolors.COMMANDVAR}{channel}{bcolors.RESET}")
			printmessage(f"Finished deleting channels in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "massdelroles",
					usage="<guild_id>",
					description = "Mass delete roles")
	@has_permissions(manage_roles=True)
	async def massdelroles(self, ctx, guild_id:int):
		await ctx.message.delete()
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
					printmessage(f"Deleted role {bcolors.COMMANDVAR}{role}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to delete role {bcolors.COMMANDVAR}{role}{bcolors.RESET}")
			printmessage(f"Finished deleting roles in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "annihilate",
					aliases=['destroy', 'wipe', 'nukeserver'],
					usage="<guild_id> <channel_name> <role_name>",
					description = "Totally annihilate a guild")
	@has_permissions(manage_roles=True, manage_channels=True, ban_members=True)
	async def annihilate(self, ctx, guild_id:int, channel_name:str, role_name:str):
		await ctx.message.delete()
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
					printmessage(f"Deleted channel {bcolors.COMMANDVAR}{channel}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to delete channel {bcolors.COMMANDVAR}{channel}{bcolors.RESET}")
			printmessage(f"Finished deleting channels in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
			for role in roles:
				try:
					await role.delete()
					printmessage(f"Deleted role {bcolors.COMMANDVAR}{role}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to delete role {bcolors.COMMANDVAR}{role}{bcolors.RESET}")
			printmessage(f"Finished deleting roles in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
			for i in range(0, amount):
				try:
					await guildhit.create_text_channel(name=f"{channel_name}")
					printmessage(f"Created channel {bcolors.COMMANDVAR}{channel_name}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to create channel {bcolors.COMMANDVAR}{channel_name}{bcolors.RESET}")
			printmessage(f"Finished creating channels in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
			for i in range(0, amount):
				try:
					await guildhit.create_roles(name=f"{role_name}")
					printmessage(f"Created role {bcolors.COMMANDVAR}{role_name}{bcolors.RESET}")
				except Exception:
					printerror(f"Failed to create role {bcolors.COMMANDVAR}{role_name}{bcolors.RESET}")
			printmessage(f"Finished creating roles in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
			for member in members:
				if member is not ctx.author:
					try:
						count = count + 1
						await member.ban()
						printmessage(f"Banned {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
					except Exception:
						printerror(f"Failed to ban {bcolors.COMMANDVAR}{member}{bcolors.RESET}")
			printmessage(f"Finished banning in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
			printmessage(f"Finished annihilating in {bcolors.COMMANDVAR}{elapsed}{bcolors.RESET}ms")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"Riskmode is disabled", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

bot.add_cog(NukingCog(bot))

class ProtectionCog(commands.Cog, name="Protection commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "antiraid",
					usage="",
					description = "Protects against raids")
	async def antiraid(self, ctx):
		await ctx.message.delete()

		global antiraid

		if antiraid == False:
			antiraid = True
			printmessage(f"Antiraid: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Antiraid: **on**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif antiraid == True:
			antiraid = False
			printmessage(f"Antiraid: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Antiraid: **off**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "friendsbackup",
					usage="",
					description = "Backup your friendslist")
	async def friendsbackup(self, ctx):
		await ctx.message.delete()
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

		embed = discord.Embed(title="Friends Backup", description=f"Backed up **{friendsamount}** friends in data/backup/friends.txt\nBacked up **{blockedamount}** blocked users in data/backup/blocked.txt", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "whitelist",
					usage="<@member>",
					description = "Whitelist someone to join while antiraid")
	async def whitelist(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user is None:
			await ctx.send("Please specify a user to whitelist")
		else:
			if ctx.guild.id not in whitelisted_users.keys():
				whitelisted_users[ctx.guild.id] = {}
			if user.id in whitelisted_users[ctx.guild.id]:
				await ctx.send('That user is already whitelisted')
			else:
				whitelisted_users[ctx.guild.id][user.id] = 0
				await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_",
																										"\_") + "#" + user.discriminator + "**")

	@commands.command(name = "unwhitelist",
					usage="",
					description = "Unwhitelist someone")
	async def unwhitelist(self, ctx, user: discord.Member = None):
		await ctx.message.delete()
		if user is None:
			await ctx.send("Please specify the user you would like to unwhitelist")
		else:
			if ctx.guild.id not in whitelisted_users.keys():
				await ctx.send("That user is not whitelisted")
				return
			if user.id in whitelisted_users[ctx.guild.id]:
				whitelisted_users[ctx.guild.id].pop(user.id, 0)
				user2 = self.bot.get_user(user.id)
				await ctx.send(
					'Successfully unwhitelisted **' + user2.name.replace('*', "\*").replace('`', "\`").replace('_',
																											"\_") + '#' + user2.discriminator + '**')

	@commands.command(name = "whitelisted",
					usage="",
					description = "Show the whitelisted list")
	async def whitelisted(self, ctx, g=None):
		await ctx.message.delete()
		if g == '-g' or g == '-global':
			whitelist = '`All Whitelisted Users:`\n'
			for key in whitelisted_users:
				for key2 in whitelisted_users[key]:
					user = self.bot.get_user(key2)
					whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
																								"\_") + "#" + user.discriminator + "** - " + self.bot.get_guild(
						key).name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "" + "\n"
			await ctx.send(whitelist)
		else:
			whitelist = "`" + ctx.guild.name.replace('*', "\*").replace('`', "\`").replace('_',
																						"\_") + '\'s Whitelisted Users:`\n'
			for key in self.bot.whitelisted_users:
				if key == ctx.guild.id:
					for key2 in self.bot.whitelisted_users[ctx.guild.id]:
						user = self.bot.get_user(key2)
						whitelist += '**+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',
																									"\_") + "#" + user.discriminator + " (" + str(
							user.id) + ")" + "**\n"
			await ctx.send(whitelist)

	@commands.command(name = "clearwhitelist",
					usage="",
					description = "Clear the whitelisted list")
	async def clearwhitelist(self, ctx):
		await ctx.message.delete()
		whitelisted_users.clear()
		embed = discord.Embed(title="Whitelist", url=titleurlvar(), description="Successfully cleared the whitelist", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

bot.add_cog(ProtectionCog(bot))

class SettingsCog(commands.Cog, name="Settings commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "prefix",
					usage="<newprefix>",
					description = "Change the prefix")
	async def prefix(self, ctx, newprefix):
		await ctx.message.delete()

		configprefix(newprefix)
		commandcount = len(self.bot.commands)

		Clear()
		Logo()
		print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
		print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {self.bot.user} | {len(self.bot.guilds)} Servers | {len(self.bot.user.friends)} Friends")
		print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {newprefix}")
		print("___________________________________________________________________________________________________")

		printmessage(f"Prefix changed to {bcolors.COMMANDVAR}{newprefix}{bcolors.RESET}")
		embed = discord.Embed(title="Prefix", url=titleurlvar(), description=f"New prefix: {newprefix}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "themes",
					usage="",
					description = "Themes")
	async def themes(self, ctx):
		await ctx.message.delete()

		path_to_json = 'data/themes/'
		json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
		themesvar = config.get('theme')

		cog = self.bot.get_cog('Theme commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		string = f"{json_files}"
		stringedit = string.replace(',', f"\n{prefix}theme").replace("'", "").replace('[', f"{prefix}theme ").replace(']', "").replace('.json', "")

		embed = discord.Embed(title="Themes", description=f"{descriptionvar()}```\nCurrent theme     » {(themesvar[:-5])}\n``````\nTheme control\n\n{prefix}newtheme <name>  » Create a theme\n{prefix}edittheme <newname> » Edit current theme name\n{prefix}deltheme <name>  » Delete a theme\n{prefix}sendtheme        » Send the current theme file\n{prefix}communitythemes  » Show themes made by the community\n``````\nAvailable themes\n\n{stringedit}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "customize",
					usage="",
					aliases=['customise', 'customization'],
					description = "Theme customization")
	async def customize(self, ctx):
		await ctx.message.delete()

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
		
		embed = discord.Embed(title="Customization", description=f"{descriptionvar()}```\nYour current theme settings\n\nTheme             » {title}\nFooter            » {footer}\nColor             » {hexcolor}\nAuthor            » {author}\n``````\nSelfbot theme settings\n\n{prefix}ctitle <title>   » Customize the title\n{prefix}ctitleurl <url>  » Customize the title url\n{prefix}cfooter <footer> » Customize the footer\n{prefix}cfootericon <url> » Customize the footer icon\n{prefix}cimage <url>     » Customize the thumbnail image\n{prefix}clargeimage <url> » Customize the large image\n{prefix}chexcolor <#hexcolor> » Change the color\n{prefix}cauthor <text>   » Customize the author text\n{prefix}cauthoricon <url> » Customize the author icon\n{prefix}cauthorurl <url> » Customize the author url\n{prefix}description <on/off> » <> | []\n{prefix}color <hexcode>  » Color information\n``````\nWebhook theme settings\n\n{prefix}wtitle <title>   » Customize the webhook title\n{prefix}wfooter <footer> » Customize the webhook footer\n{prefix}wimage <url>     » Customize the thumbnail image\n{prefix}whexcolor <#hexcolor> » Change the webhook color\n{prefix}wmatch           » Match webhook with theme\n``````\nToast theme settings\n\n{prefix}toasticon <icon.ico> » Customize the toast icon (has to be an .ico)\n{prefix}toasttitle <title> » Customize the toast title\n``````\nNote\n\nIf you want to remove a customization,\nYou can use \"None\" to remove it.\n\nIf you want to set up a random color each time\nyou run a command, you can use \"random\" as hex color.```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "embedmode",
					usage="",
					description = "Switch to embed mode")
	async def embedmode(self, ctx):
		await ctx.message.delete()

		configmode("1")
		printmessage(f"Switched to {bcolors.COMMANDVAR}embed{bcolors.RESET} mode")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Switched to embed mode.", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "textmode",
					usage="",
					description = "Switch to text mode")
	async def textmode(self, ctx):
		await ctx.message.delete()

		configmode("2")
		printmessage(f"Switched to {bcolors.COMMANDVAR}text{bcolors.RESET} mode")

		sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nSwitched to text mode.\n\n[ {footervar()} ]```")
		await asyncio.sleep(deletetimer())
		await sent.delete()

	@commands.command(name = "indentmode",
					usage="",
					description = "Switch to indent mode")
	async def indentmode(self, ctx):
		await ctx.message.delete()

		configmode("3")
		printmessage(f"Switched to {bcolors.COMMANDVAR}indent{bcolors.RESET} mode")

		sent = await ctx.send(f"> **{titlevar()}**\n> \n> Switched to **indent** mode.\n> \n> {footervar()}")
		await asyncio.sleep(deletetimer())
		await sent.delete()

	@commands.command(name = "sniper",
					usage="",
					description = "Sniper settings")
	async def sniper(self, ctx):
		await ctx.message.delete()

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
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Sniper settings", description=f"{descriptionvar()}```\nNitro Sniper      » {nitro_sniper}\nNitro API         » {api}\n``````\n{prefix}nitrosniper <on/off> » Toggle nitro sniper\n{prefix}nitroapi <canary/v6/v7/v8/v9> » Configurate nitro sniper api```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "giveaway",
					usage="",
					description = "Giveaway settings")
	async def giveaway(self, ctx):
		await ctx.message.delete()

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
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Giveaway settings", description=f"{descriptionvar()}Giveaway Joiner: **{giveawayjoiner}**\nDelay: **{delay_in_minutes} minute/s**\nServer Joiner: **{giveaway_server_joiner}**\n\n{helptext}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "notifications",
					usage="",
					description = "Toast notifications")
	async def notifications(self, ctx):
		await ctx.message.delete()

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
		slotbot = notif.get('slotbot')
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
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Toast notifications", description=f"{descriptionvar()}Toasts: **{toasts}**\nLogin toasts: **{login}**\nNitro toasts: **{nitro}**\nGiveaway toasts: **{giveaway}**\nPrivnote toasts: **{privnote}**\nSlotbot toasts: **{slotbot}**\nSelfbot toasts: **{selfbot}**\nPing toasts: **{pings}**\nGhostping toasts: **{ghostpings}**\nFriendevent toasts: **{friendevents}**\nGuildevent toasts: **{guildevents}**\nNickname toasts: **{nickupdates}**\nProtection toasts: **{protection}**\n\n{helptext}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)
	
	@commands.command(name = "errorlog",
					usage="<console/message>",
					description = "Switch errorlog")
	async def errorlog(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "console":

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Error logging: **console**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

			printmessage(f"Error logging: {bcolors.LIGHTMAGENTA}console{bcolors.RESET}")
			configerrorlog("console")

		elif mode == "message":

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Error logging: **message**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

			printmessage(f"Error logging: {bcolors.LIGHTMAGENTA}message{bcolors.RESET}")
			configerrorlog("message")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"That mode does not exist!\nOnly **console** or **message**", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "deletetimer",
					usage="<seconds>",
					description = "Auto delete timer")
	async def deletetimer(self, ctx, seconds:int):
		await ctx.message.delete()

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Auto delete timer: **{seconds} seconds**", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

		printmessage(f"Auto delete timer: {bcolors.LIGHTMAGENTA}{seconds} seconds{bcolors.RESET}")
		configdeletetimer(f"{seconds}")

	@commands.command(name = "afkmessage",
					usage="<text>",
					description = "Change the afk message")
	async def afkmessage(self, ctx, *, afkmessage):
		await ctx.message.delete()

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"AFK message: **{afkmessage}**", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

		printmessage(f"AFK message: {bcolors.LIGHTMAGENTA}{afkmessage}{bcolors.RESET}")
		configafkmessage(f"{afkmessage}")

	@commands.command(name = "riskmode",
					usage="<on/off>",
					description = "Enable abusive commands")
	async def riskmode(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Riskmode: **on**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

			printmessage(f"Riskmode: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configriskmode("on")

		elif mode == "off":

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Riskmode: **off**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

			printmessage(f"Riskmode: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configriskmode("off")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "selfbotdetection",
					usage="<on/off>",
					description = "Turn selfbot detection on or off")
	async def selfbotdetection(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Selfbot detection: **on**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

			printmessage(f"Selfbot detection: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configselfbot_detection("on")

		elif mode == "off":

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Selfbot detection: **off**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

			printmessage(f"Selfbot detection: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configselfbot_detection("off")
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "password",
					usage="<new_password>",
					description = "Change password config")
	async def password(self, ctx, password:str):
		await ctx.message.delete()

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Changed password to: **{password}**", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

		printmessage(f"Changed password to: {bcolors.LIGHTMAGENTA}{password}{bcolors.RESET}")
		configpassword(f"{password}")

bot.add_cog(SettingsCog(bot))

class ShareCog(commands.Cog, name="Share commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "share",
					usage="<on/off>",
					description = "Share on/off")
	async def share(self, ctx):
		await ctx.message.delete()

		with open('data/sharing.json') as f:
			slot = json.load(f)
		share = slot.get('share')

		if share == "off":
			configshare("on")
			printmessage(f"Share: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")

			if mode() == 2:
				sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nShare: on\n\n[ {footervar()} ]```")
				await asyncio.sleep(deletetimer())
				await sent.delete()
			else:
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Share: **on**", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				sent = await ctx.send(embed=embed)
				await asyncio.sleep(deletetimer())
				await sent.delete()

		if share == "on":
			configshare("off")
			printmessage(f"Share: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")

			if mode() == 2:
				sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nShare: off\n\n[ {footervar()} ]```")
				await asyncio.sleep(deletetimer())
				await sent.delete()
			else:
				embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Share: **off**", color=hexcolorvar())
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				sent = await ctx.send(embed=embed)
				await asyncio.sleep(deletetimer())
				await sent.delete()

	@commands.command(name = "shareuser",
					usage="<@member>",
					description = "Set the member for sharing")
	async def shareuser(self, ctx, user_id):
		await ctx.message.delete()

		if "<@!" and ">" in user_id:
			user_id = user_id.replace("<@!", "").replace(">", "")
			user = await self.bot.fetch_user(user_id)
		else:
			user = await self.bot.fetch_user(user_id)

		print(user.avatar_url)

		if user == self.bot.user:
			if errorlog() == "console":
				printerror("You can't use share on yourself.")
			else:
				if mode() == 2:
					sent = await ctx.send(f"```ini\n[ Error ]\n\nYou can't use share on yourself.\n\n[ {footervar()} ]```")
					await asyncio.sleep(deletetimer())
					await sent.delete()
				else:
					embed = discord.Embed(title="Error", url=titleurlvar(), description=f"You can't use share on yourself.", color=0xff0000)
					embed.set_thumbnail(url=imagevar())
					embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
					embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
					embed.set_image(url=largeimagevar())
					sent = await ctx.send(embed=embed)
					await asyncio.sleep(deletetimer())
					await sent.delete()
			return

		configshare_userid(user.id)
		printmessage(f"Share user set to: {bcolors.LIGHTMAGENTA}{user}{bcolors.RESET}")

		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nShare user set to: {user}\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Share user set to: **{user}**", color=hexcolorvar())
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete()

	@commands.command(name = "sharenone",
					usage="",
					description = "Set the member for sharing to none")
	async def sharenone(self, ctx):
		await ctx.message.delete()

		configshare_userid("")
		printmessage(f"Share user set to: {bcolors.LIGHTMAGENTA}None{bcolors.RESET}")

		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nShare user set to: None\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Share user set to: **None**", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete()

bot.add_cog(ShareCog(bot))

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

bot.add_cog(EncodeCog(bot))

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

bot.add_cog(DecodeCog(bot))

class GiveawayCog(commands.Cog, name="Giveaway settings"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "giveawaysniper",
					usage="<on/off>",
					description = "Turn giveaway sniper on or off")
	async def giveawaysniper(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Giveaway sniper: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configgiveaway_sniper("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nGiveaway sniper » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Giveaway sniper: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configgiveaway_sniper("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nGiveaway sniper » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "delay",
					usage="<minutes>",
					description = "Giveaway joiner delay in minutes")
	async def delay(self, ctx, minute:int):
		await ctx.message.delete()

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nGiveaway joiner delay » {minute} minute/s```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

		printmessage(f"Auto delete timer: {bcolors.LIGHTMAGENTA}{minute} minute/s{bcolors.RESET}")
		configgiveaway_sniperdelay(f"{minute}")

	@commands.command(name = "giveawayserver",
					usage="<on/off>",
					description = "Turn giveaway server joiner on or off")
	async def giveawayserver(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Server joiner: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configgiveaway_sniperjoiner("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nServer joiner » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Server joiner: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configgiveaway_sniperjoiner("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nServer joiner » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

bot.add_cog(GiveawayCog(bot))

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
	async def btc(self, ctx):
		await ctx.message.delete()
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
		await send(ctx, embed)

	@commands.command(name = "eth",
					usage="",
					description = "Show the current prizes of Ethereum")
	async def eth(self, ctx):
		await ctx.message.delete()
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
		await send(ctx, embed)

	@commands.command(name = "doge",
					usage="",
					description = "Show the current prizes of Dogecoin")
	async def doge(self, ctx):
		await ctx.message.delete()
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
		await send(ctx, embed)

bot.add_cog(CryptoCog(bot))

class CustomizeCog(commands.Cog, name="Customization commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "ctitle",
					usage="<title>",
					description = "Customize the title")
	async def ctitle(self, ctx, *, newtitle:str):
		await ctx.message.delete()

		printmessage(f"Changed title to: {bcolors.LIGHTMAGENTA}{newtitle}{bcolors.RESET}")
		if newtitle == "None":
			configselfbottitle("")
		else:
			configselfbottitle(f"{newtitle}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged title to » {newtitle}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "ctitleurl",
					usage="<url>",
					description = "Customize the title url")
	async def ctitleurl(self, ctx, newtitleurl:str):
		await ctx.message.delete()

		printmessage(f"Changed title url to: {bcolors.LIGHTMAGENTA}{newtitleurl}{bcolors.RESET}")
		if newtitleurl == "None":
			configselfbottitleurl("")
		else:
			configselfbottitleurl(f"{newtitleurl}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged title url to » {newtitleurl}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "cfooter",
					usage="<footer>",
					description = "Customize the footer")
	async def cfooter(self, ctx, *, newfooter:str):
		await ctx.message.delete()

		printmessage(f"Changed footer to: {bcolors.LIGHTMAGENTA}{newfooter}{bcolors.RESET}")
		if newfooter == "None":
			configselfbotfooter("")
		else:
			configselfbotfooter(f"{newfooter}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged footer to » {newfooter}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "cfootericon",
					usage="<url>",
					description = "Customize the footer icon")
	async def cfootericon(self, ctx, newfootericonurl:str):
		await ctx.message.delete()

		printmessage(f"Changed footer icon url to: {bcolors.LIGHTMAGENTA}{newfootericonurl}{bcolors.RESET}")
		if newfootericonurl == "None":
			configselfbotfooter_iconurl("")
		else:
			configselfbotfooter_iconurl(f"{newfootericonurl}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged footer icon url to » {newfootericonurl}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "cimage",
					usage="<url>",
					description = "Customize the thumbnail image")
	async def cimageurl(self, ctx, newimageurl:str):
		await ctx.message.delete()

		printmessage(f"Changed thumbnail url to: {bcolors.LIGHTMAGENTA}{newimageurl}{bcolors.RESET}")
		if newimageurl == "None":
			configselfbotimageurl("")
		else:
			configselfbotimageurl(f"{newimageurl}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged thumbnail url to » {newimageurl}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "clargeimage",
					usage="<url>",
					description = "Customize the large image")
	async def clargeimage(self, ctx, newimageurl:str):
		await ctx.message.delete()

		printmessage(f"Changed image url to: {bcolors.LIGHTMAGENTA}{newimageurl}{bcolors.RESET}")
		if newimageurl == "None":
			configselfbotlarge_imageurl("")
		else:
			configselfbotlarge_imageurl(f"{newimageurl}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged image url to » {newimageurl}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "chexcolor",
					usage="<#hexcolor>",
					description = "Customize the hexadecimal color")
	async def chexcolor(self, ctx, newhexcolor:str):
		await ctx.message.delete()

		printmessage(f"Changed hexcolor to: {bcolors.LIGHTMAGENTA}{newhexcolor}{bcolors.RESET}")
		if newhexcolor == "None":
			configselfbothexcolor("")
		else:
			configselfbothexcolor(f"{newhexcolor}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged hexcolor to » {newhexcolor}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "cauthor",
					usage="<text>",
					description = "Customize the author text")
	async def cauthor(self, ctx, *, newauthor:str):
		await ctx.message.delete()

		printmessage(f"Changed author to: {bcolors.LIGHTMAGENTA}{newauthor}{bcolors.RESET}")
		if newauthor == "None":
			configselfbotauthor("")
		else:
			configselfbotauthor(f"{newauthor}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged author to » {newauthor}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "cauthoricon",
					usage="<url>",
					description = "Customize the author icon")
	async def cauthoricon(self, ctx, newauthoriconurl:str):
		await ctx.message.delete()

		printmessage(f"Changed author icon url to: {bcolors.LIGHTMAGENTA}{newauthoriconurl}{bcolors.RESET}")
		if newauthoriconurl == "None":
			configselfbotauthor_iconurl("")
		else:
			configselfbotauthor_iconurl(f"{newauthoriconurl}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged author icon url to » {newauthoriconurl}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "cauthorurl",
					usage="<url>",
					description = "Customize the author url")
	async def cauthorurl(self, ctx, newauthorurl:str):
		await ctx.message.delete()

		printmessage(f"Changed author url to: {bcolors.LIGHTMAGENTA}{newauthorurl}{bcolors.RESET}")
		if newauthorurl == "None":
			configselfbotauthorurl("")
		else:
			configselfbotauthorurl(f"{newauthorurl}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged author url to » {newauthorurl}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "description",
					aliases=['cdescription'],
					usage="<on/off>",
					description = "Hide/Show <> = required, [] = optional")
	async def description(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Changed description to: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configselfbotdescription(True)

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged description to » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Changed description to: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configselfbotdescription(False)

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged description to » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "color",
					usage="<hexcode>",
					description = "Color information")
	async def color(self, ctx, hexcode:str):
		await ctx.message.delete()
		if hexcode == "random":
			hexcode = "%06x" % random.randint(0, 0xFFFFFF)
		if hexcode[:1] == "#":
			hexcode = hexcode[1:]
		if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', hexcode):
			return
		r = requests.get(f"https://react.flawcra.cc/api/generation.php?type=color&color={hexcode}").json()
		embed = discord.Embed(title=f'{r["name"]}', description=f"```\nHEX               » {r['hex']}\n``````\nRGB               » {r['rgb']}\n``````\nINT               » {r['int']}\n``````\nBrightness        » {r['brightness']}\n```",color=r["int"])
		embed.set_thumbnail(url=r["image"])
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		await send(ctx, embed)

bot.add_cog(CustomizeCog(bot))

class NSFWCog(commands.Cog, name="NSFW commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	# ///////////////////////////////////////////////////////////////
	# NSFW commands

	@commands.command(name = "lewdneko",
					usage="",
					description = "Send a random lewdneko image")
	async def lewdneko(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "hentai",
					usage="",
					description = "Send a random hentai image")
	async def hentai(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "hentaiass",
					usage="",
					description = "Send a random hentai ass")
	async def hentaiass(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekobot.xyz/api/image?type=hass").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['message']))
		await ctx.send(embed=embed)

	@commands.command(name = "ass",
					usage="",
					description = "Send a random ass")
	async def ass(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekobot.xyz/api/image?type=ass").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['message']))
		await ctx.send(embed=embed)

	@commands.command(name = "boobs",
					usage="",
					description = "Send a random image of boobs")
	async def boobs(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/boobs").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "tits",
					usage="",
					description = "Send a random image of tits")
	async def tits(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/tits").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)
        
	@commands.command(name = "anal",
					usage="",
					description = "Send a random anal image")
	async def anal(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/anal").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "cumslut",
					usage="",
					description = "Send a random image of a cumslut")
	async def cumslut(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/cum").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "blowjob",
					usage="",
					description = "Send a random blowjob image")
	async def blowjob(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/blowjob").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "lesbian",
					usage="",
					description = "Send a random lesbian image")
	async def lesbian(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/les").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['url']))
		await ctx.send(embed=embed)

	@commands.command(name = "yaoi",
					usage="",
					description = "Send a random image of yaoi")
	async def yaoi(self, ctx):
		await ctx.message.delete()
		r = requests.get("https://nekobot.xyz/api/image?type=yaoi").json()
		embed = discord.Embed(title=titlevar(), color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=str(r['message']))
		await ctx.send(embed=embed)

bot.add_cog(NSFWCog(bot))

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
						await guild.ban(member, reason="Lolicon Anti-Raid")
						await guild.ban(i.user, reason="Lolicon Anti-Raid")
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
						await guild.ban(i.user, reason="Lolicon Anti-Raid")
			except Exception as e:
				print(e)

bot.add_cog(OnMember(bot))

class SniperCog(commands.Cog, name="Sniper settings"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "nitrosniper",
					usage="<on/off>",
					description = "Turn nitro sniper on or off")
	async def nitrosniper(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Nitro sniper: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			confignitro_sniper("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nNitro sniper » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Nitro sniper: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			confignitro_sniper("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nNitro sniper » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "nitroapi",
					usage="<canary/v6/v7/v8/v9>",
					description = "Configurate nitro sniper api")
	async def sniperapi(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "canary" or mode == "v6" or mode == "v7" or mode == "v8" or mode == "v9":
			printmessage(f"Nitro sniper api: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			confignitro_sniperapi(f"{mode}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nNitro sniper api » {mode}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			print("1")
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly \"canary\", \"v6\", \"v7\", \"v8\" or \"v9\"```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

bot.add_cog(SniperCog(bot))

class ThemeCog(commands.Cog, name="Theme command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "theme",
					usage="<theme>",
					description = "Change theme")
	async def theme(self, ctx, theme:str):
		await ctx.message.delete()

		if os.path.exists(f"data/themes/{theme}" + ".json"):

			printmessage(f"Changed theme to: {bcolors.LIGHTMAGENTA}{theme}{bcolors.RESET}")
			configtheme(f"{theme}")
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged theme to » {theme}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			if errorlog() == "console":
				printerror(f"There is no theme called: {bcolors.LIGHTMAGENTA}{theme}{bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThere is no theme called » {theme}```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

bot.add_cog(ThemeCog(bot))

class ThemesCog(commands.Cog, name="Theme commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "newtheme",
					usage="<name>",
					description = "Create a theme")
	async def newtheme(self, ctx, themename:str):
		await ctx.message.delete()

		if os.path.exists(f"data/themes/{themename}.json"):
			if errorlog() == "console":
				printerror(f"A theme already exists with the name: {bcolors.LIGHTMAGENTA}{themename}{bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nA theme already exists with the name » {themename}```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
		else:
			printmessage(f"Created theme: {bcolors.LIGHTMAGENTA}{themename}{bcolors.RESET}")
			data = {
				"title": "Lolicon",
				"titleurl": "",
				"footer": "Lolicon",
				"footer_iconurl": "https://cdn.discordapp.com/attachments/848299943172505611/868676317174980608/LoliconRe.png",
				"imageurl": "https://cdn.discordapp.com/attachments/848299943172505611/868676317174980608/LoliconRe.png",
				"large_imageurl": "",
				"hexcolor": "#bd93f9",
				"author": "",
				"author_iconurl": "",
				"authorurl": "",
				"description": True
			}
			with open(f"data/themes/{themename}.json", "w") as studs:
				json.dump(data, studs, indent=4)
			configtheme(f"{themename}")
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nCreated theme » {themename}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "edittheme",
					usage="<newname>",
					description = "Edit current theme name")
	async def edittheme(self, ctx, themename:str):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')

		if os.path.exists(f"data/themes/{themename}.json"):
			if errorlog() == "console":
				printerror(f"A theme already exists with the name: {bcolors.LIGHTMAGENTA}{themename}{bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nA theme already exists with the name » {themename}```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
		else:
			printmessage(f"Edited theme name to: {bcolors.LIGHTMAGENTA}{themename}{bcolors.RESET}")
			os.rename(f"data/themes/{themesvar}",f"data/themes/{themename}.json")
			configtheme(f"{themename}")
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nEdited theme name to » {themename}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
        
	@commands.command(name = "deltheme",
					usage="<name>",
					description = "Delete a theme")
	async def deltheme(self, ctx, themename:str):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')

		if themesvar == f"{themename}.json":
			if errorlog() == "console":
				printerror(f"You cant delete the theme you are currently using.")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThere is no theme called » {themename}```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
			return

		if os.path.exists(f"data/themes/{themename}" + ".json"):
			os.remove(f"data/themes/{themename}" + ".json")
			printmessage(f"Deleted theme: {bcolors.LIGHTMAGENTA}{themename}{bcolors.RESET}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nDeleted theme » {themename}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			if errorlog() == "console":
				printerror(f"There is no theme called: {bcolors.LIGHTMAGENTA}{themename}{bcolors.RESET}")
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThere is no theme called » {themename}```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)

	@commands.command(name = "sendtheme",
					usage="",
					description = "Send the current theme file")
	async def sendtheme(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		themesvar = config.get('theme')

		await ctx.send(file=discord.File(f"data/themes/{themesvar}"))

	@commands.command(name = "communitythemes",
					usage="",
					description = "Show themes made by the community")
	async def communitythemes(self, ctx):
		await ctx.message.delete()
		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		embed = discord.Embed(title="Community Themes", url=titleurlvar(), description=f"{descriptionvar()}```\n{prefix}preview <theme>  » Preview a theme\n``````\n{prefix}install luna     » Luna theme\n{prefix}install chill    » Chill theme\n{prefix}install midnight » Midnight theme\n{prefix}install vaporwave » Vaporwave theme\n{prefix}install sweetrevenge » Sweetrevenge theme\n{prefix}install error    » Error theme```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

bot.add_cog(ThemesCog(bot))

class CommunitythemesCog(commands.Cog, name="Community themes"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "preview",
					usage="<theme>",
					description = "Preview a theme")
	async def preview(self, ctx, theme:str):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		notfound = False
		
		if theme == "luna":
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
		else:
			notfound = True

		if notfound == True:
			if errorlog() == "console":
				printerror(f"No theme called {theme} found")
				return
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nNo theme called {theme} found```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
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
		await send(ctx, embed)

	@commands.command(name = "install",
					usage="<theme>",
					description = "Install a theme")
	async def install(self, ctx, theme:str):
		await ctx.message.delete()

		notfound = False

		if theme == "luna":
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
		else:
			notfound = True

		if notfound == True:
			if errorlog() == "console":
				printerror(f"No theme called {theme} found")
				return
			else:
				embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nNo theme called {theme} found```", color=0xff0000)
				embed.set_thumbnail(url=imagevar())
				embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
				embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
				embed.set_image(url=largeimagevar())
				await send(ctx, embed)
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
		configtheme(f"{theme}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nInstalled theme {theme} and changed to it\nThis theme was made by {madeby}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

bot.add_cog(CommunitythemesCog(bot))

class ToastCog(commands.Cog, name="Toast customization"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "toasticon",
					usage="<icon.ico>",
					description = "Customize the toast icon (has to be an .ico)")
	async def toasticon(self, ctx, *, newicon:str):
		await ctx.message.delete()

		printmessage(f"Changed toast icon to: {bcolors.LIGHTMAGENTA}{newicon}{bcolors.RESET}")
		if newicon.endswith(".ico"):
			configtoasticon(f"{newicon}")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged toast title to » {newicon}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nNot a valid icon file, (.ico)```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
        
	@commands.command(name = "toasttitle",
					usage="<title>",
					description = "Customize the toast title")
	async def toasttitle(self, ctx, *, newtitle:str):
		await ctx.message.delete()

		printmessage(f"Changed toast title to: {bcolors.LIGHTMAGENTA}{newtitle}{bcolors.RESET}")
		if newtitle == "None":
			configtoasttitle("")
		else:
			configtoasttitle(f"{newtitle}")

		embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged toast title to » {newtitle}```", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

bot.add_cog(ToastCog(bot))

class ToastsCog(commands.Cog, name="Toast commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
	
	@commands.command(name = "toasts",
					usage="<on/off>",
					description = "Turn toasts on or off")
	async def toasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoasttoasts("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nToasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoasttoasts("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nToasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "logintoasts",
					usage="<on/off>",
					description = "Turn login toasts on or off")
	async def logintoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Login toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastlogin("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nLogin toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Login toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastlogin("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nLogin toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "nitrotoasts",
					usage="<on/off>",
					description = "Turn nitro toasts on or off")
	async def nitrotoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Nitro toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastnitro("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nNitro toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Nitro toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastnitro("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nNitro toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "giveawaytoasts",
					usage="<on/off>",
					description = "Turn giveaway toasts on or off")
	async def giveawaytoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Giveaway toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastgiveaway("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nGiveaway toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Giveaway toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastgiveaway("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nGiveaway toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "privnotetoasts",
					usage="<on/off>",
					description = "Turn privnote toasts on or off")
	async def privnotetoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Privnote toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastprivnote("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nPrivnote toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Privnote toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastprivnote("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nPrivnote toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "slotbottoasts",
					usage="<on/off>",
					description = "Turn slotbot toasts on or off")
	async def slotbottoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Slotbot toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastslotbot("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nSlotbot toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Slotbot toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastslotbot("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nSlotbot toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "selfbottoasts",
					usage="<on/off>",
					description = "Turn selfbot toasts on or off")
	async def selfbottoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Selfbot toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastselfbot("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nSelfbot toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Selfbot toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastselfbot("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nSelfbot toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "pingtoasts",
					usage="<on/off>",
					description = "Turn ping toasts on or off")
	async def pingtoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Ping toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastpings("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nPing toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Ping toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastpings("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nPing toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "ghostpingtoasts",
					usage="<on/off>",
					description = "Turn ghostping toasts on or off")
	async def ghostpingtoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Ghostping toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastghostpings("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nGhostping toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Ghostping toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastghostpings("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nGhostping toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "friendtoasts",
					usage="<on/off>",
					description = "Turn friendevent toasts on or off")
	async def friendtoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Friendevent toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastfriendevents("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nFriendevent toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Friendevent toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastfriendevents("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nFriendevent toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "guildtoasts",
					usage="<on/off>",
					description = "Turn guildevent toasts on or off")
	async def guildtoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Guildevent toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastguildevents("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nGuildevent toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Guildevent toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastguildevents("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nGuildevent toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "roletoasts",
					usage="<on/off>",
					description = "Turn roleupdate toasts on or off")
	async def roletoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Roleupdate toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastroleupdates("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nRoleupdate toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Roleupdate toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastroleupdates("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nRoleupdate toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "nicktoasts",
					usage="<on/off>",
					description = "Turn nicknameupdate toasts on or off")
	async def nicktoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Nicknameupdate toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastnickupdates("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nNicknameupdate toasts » on```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Nicknameupdate toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastnickupdates("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nNicknameupdate toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

	@commands.command(name = "protectiontoasts",
					usage="<on/off>",
					description = "Turn protection toasts on or off")
	async def protectiontoasts(self, ctx, mode:str):
		await ctx.message.delete()

		if mode == "on":
			printmessage(f"Protection toasts: {bcolors.LIGHTMAGENTA}on{bcolors.RESET}")
			configtoastprotection("on")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"Protection toasts » on", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

		elif mode == "off":
			printmessage(f"Protection toasts: {bcolors.LIGHTMAGENTA}off{bcolors.RESET}")
			configtoastprotection("off")

			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nProtection toasts » off```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Error", url=titleurlvar(), description=f"```\nThat mode does not exist!\nOnly on or off```", color=0xff0000)
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)

bot.add_cog(ToastsCog(bot))

class WebhookCog(commands.Cog, name="Webhook commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "wtitle",
					usage="<title>",
					description = "Customize the webhook title")
	async def wtitle(self, ctx, *, newtitle:str):
		await ctx.message.delete()

		printmessage(f"Changed webhook title to: {bcolors.LIGHTMAGENTA}{newtitle}{bcolors.RESET}")
		if newtitle == "None":
			configwebhooktitle("")
		else:
			configwebhooktitle(f"{newtitle}")

		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nChanged webhook title to: {newtitle}\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged webhook title to » {newtitle}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete()

	@commands.command(name = "wfooter",
					usage="<footer>",
					description = "Customize the webhook footer")
	async def wfooter(self, ctx, *, newfooter:str):
		await ctx.message.delete()

		printmessage(f"Changed webhook footer to: {bcolors.LIGHTMAGENTA}{newfooter}{bcolors.RESET}")
		if newfooter == "None":
			configwebhookfooter("")
		else:
			configwebhookfooter(f"{newfooter}")

		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nChanged webhook footer to: {newfooter}\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged webhook footer to » {newfooter}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete()

	@commands.command(name = "wimage",
					usage="<url>",
					description = "Customize the thumbnail image")
	async def wimage(self, ctx, newimageurl:str):
		await ctx.message.delete()

		printmessage(f"Changed webhook thumbnail url to: {bcolors.LIGHTMAGENTA}{newimageurl}{bcolors.RESET}")
		if newimageurl == "None":
			configwebhookimage("")
		else:
			configwebhookimage(f"{newimageurl}")

		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nChanged webhook thumbnail url to: {newimageurl}\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged webhook thumbnail url to » {newimageurl}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete()

	@commands.command(name = "whexcolor",
					usage="<#hexcolor>",
					description = "Customize the webhook hexadecimal color")
	async def whexcolor(self, ctx, newhexcolor:str):
		await ctx.message.delete()

		printmessage(f"Changed webhook hexcolor to: {bcolors.LIGHTMAGENTA}{newhexcolor}{bcolors.RESET}")
		if newhexcolor == "None":
			configwebhookhexcolor("")
		else:
			configwebhookhexcolor(f"{newhexcolor}")

		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nChanged webhook hexcolor to: {newhexcolor}\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nChanged webhook hexcolor to » {newhexcolor}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete()

	@commands.command(name = "wmatch",
					usage="",
					description = "Match webhook with current theme")
	async def wmatch(self, ctx):
		await ctx.message.delete()

		with open('./config.json') as f:
			config = json.load(f)
		themesvar = config.get('theme')
		with open(f"data/themes/{themesvar}") as f:
			theme = json.load(f)
		title = theme.get('title')
		footer = theme.get('footer')
		imageurl = theme.get('imageurl')
		hexcolor = theme.get('hexcolor')

		printmessage(f"Matched webhook to: {bcolors.LIGHTMAGENTA}{themesvar[:-5]}{bcolors.RESET}")
		configwebhooktitle(f"{title}")
		configwebhookfooter(f"{footer}")
		configwebhookimage(f"{imageurl}")
		configwebhookhexcolor(f"{hexcolor}")

		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ {titlevar()} ]\n\nMatched webhook to: {themesvar[:-5]}\n\n[ {footervar()} ]```")
			await asyncio.sleep(deletetimer())
			await sent.delete()
		else:
			embed = discord.Embed(title=titlevar(), url=titleurlvar(), description=f"```\nMatched webhook to » {themesvar[:-5]}```", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(deletetimer())
			await sent.delete()

bot.add_cog(WebhookCog(bot))

class MiscCog(commands.Cog, name="Miscellaneous commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "thelp",
					usage="",
					description = "All commands in a text file")
	async def thelp(self, ctx):
		await ctx.message.delete()

		#///////////////////////////////////////////////////////////////////

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		#///////////////////////////////////////////////////////////////////

		cog = self.bot.get_cog('Help commands')
		commands = cog.get_commands()
		helpcommands = ""
		for command in commands:
			helpcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Administrative commands')
		commands = cog.get_commands()
		admincommands = ""
		for command in commands:
			admincommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Animated commands')
		commands = cog.get_commands()
		animatedcommands = ""
		for command in commands:
			animatedcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Text commands')
		commands = cog.get_commands()
		textcommands = ""
		for command in commands:
			textcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"
			
		cog = self.bot.get_cog('Image commands')
		commands = cog.get_commands()
		imagecommands = ""
		for command in commands:
			imagecommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Troll commands')
		commands = cog.get_commands()
		trollcommands = ""
		for command in commands:
			trollcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Fun commands')
		commands = cog.get_commands()
		funcommands = ""
		for command in commands:
			funcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Tools commands')
		commands = cog.get_commands()
		toolscommands = ""
		for command in commands:
			toolscommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Nettool commands')
		commands = cog.get_commands()
		nettoolscommands = ""
		for command in commands:
			nettoolscommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Util commands')
		commands = cog.get_commands()
		utilscommands = ""
		for command in commands:
			utilscommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Abusive commands')
		commands = cog.get_commands()
		abusecommands = ""
		for command in commands:
			abusecommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Raid commands')
		commands = cog.get_commands()
		raidcommands = ""
		for command in commands:
			raidcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Nuking commands')
		commands = cog.get_commands()
		nukecommands = ""
		for command in commands:
			nukecommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Protection commands')
		commands = cog.get_commands()
		protectioncommands = ""
		for command in commands:
			protectioncommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Miscellaneous commands')
		commands = cog.get_commands()
		misccommands = ""
		for command in commands:
			misccommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Settings commands')
		commands = cog.get_commands()
		settingscommands = ""
		for command in commands:
			settingscommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Share commands')
		commands = cog.get_commands()
		sharecommands = ""
		for command in commands:
			sharecommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"
	
		cog = self.bot.get_cog('Toast customization')
		commands = cog.get_commands()
		toastcustomcommands = ""
		for command in commands:
			toastcustomcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Toast commands')
		commands = cog.get_commands()
		toastcommands = ""
		for command in commands:
			toastcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Customization commands')
		commands = cog.get_commands()
		customizationcommands = ""
		for command in commands:
			customizationcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Webhook commands')
		commands = cog.get_commands()
		webhookcommands = ""
		for command in commands:
			webhookcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('NSFW commands')
		commands = cog.get_commands()
		nsfwcommands = ""
		for command in commands:
			nsfwcommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Cryptocurrency commands')
		commands = cog.get_commands()
		cryptocommands = ""
		for command in commands:
			cryptocommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Encode commands')
		commands = cog.get_commands()
		encodecommands = ""
		for command in commands:
			encodecommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		cog = self.bot.get_cog('Decode commands')
		commands = cog.get_commands()
		decodecommands = ""
		for command in commands:
			decodecommands+=f"{prefix}{command.name} {command.usage} » {command.description}\n"

		#///////////////////////////////////////////////////////////////////

		commandcount = len(self.bot.commands)

		file = open("commands.txt", "w") 
		file.write(f"{commandcount} Commands\n\n<> is required | [] is optional\n\nCategories:\n{helpcommands}\nAdmin Commands:\n{admincommands}\nAnimated Commands:\n{animatedcommands}\nText Commands:\n{textcommands}\nImage Commands:\n{imagecommands}\nTroll Commands:\n{trollcommands}\nFun Commands:\n{funcommands}\nTools:\n{toolscommands}\nNetworking Tools\n{nettoolscommands}\nUtilities\n{utilscommands}\nAbusive Commands\n{abusecommands}\nRaiding\n{raidcommands}\nNuking\n{nukecommands}\nProtections\n{protectioncommands}\nMiscellaneous\n{misccommands}\nSettings\n{settingscommands}\nSharing\n{sharecommands}\nCustomization\n{customizationcommands}\nToast Settings\n{toastcommands}\nToast Customization\n{toastcustomcommands}\nWebhook Settings\n{webhookcommands}\nNSFW\n{nsfwcommands}\nCryptocurrency\n{cryptocommands}\nEncode\n{encodecommands}\nDecode\n{decodecommands}")
		file.close()

		embed = discord.Embed(title="Text Help", description=f"Saved all commands in commands.txt", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "update",
					usage="",
					description = "Updates Luna if there's an update")
	async def update(self, ctx):
		await ctx.message.delete()
		versionpastedec = urllib.request.urlopen('https://pastebin.com/raw/iQPkzEpg')
		for line in versionpastedec:
			versionpaste = line.decode().strip()
		if f"'{lunaversion}'" == versionpaste:
			embed = discord.Embed(title="Update", description=f"You are on the latest version!", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
		else:
			embed = discord.Embed(title="Update", description=f"Started update: {versionpaste}", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			await send(ctx, embed)
			Clear()
			Title(f"Luna Selfbot | Update")
			Logo()
			print(f"Status:    {bcolors.YELLOW}New version found{bcolors.RESET}")
			print(f"- A new version is available ({bcolors.MAGENTA}{versionpaste}{bcolors.RESET})")
			print()
			print("____________________________________________________________________________________________________")
			printevent("Preparing update, please wait...")
			r = requests.get(updateurl, stream=True)

			chunk_size = 1024
			total_size = int(r.headers['content-length'])

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
	async def crypto(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')

		cog = self.bot.get_cog('Cryptocurrency commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"**{prefix}{command.name} {command.usage}** » {command.description}\n"
		embed = discord.Embed(title="Cryptocurrency", description=f"{descriptionvar()}{helptext}", color=hexcolorvar())
		embed.set_thumbnail(url=imagevar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=largeimagevar())
		await send(ctx, embed)

	@commands.command(name = "restart",
					usage="",
					aliases=['reboot'],
					description = "Restart Lolicon")
	async def restart(self, ctx):
		await ctx.message.delete()

		if mode() == 2:
			sent = await ctx.send(f"```ini\n[ Restarting ]\n\nAllow up to 5 seconds.\n\n[ {footervar()} ]```")
			await asyncio.sleep(3)
			await sent.delete()
			restart_program()
		if mode() == 3:
			sent = await ctx.send(f"> **Restarting**\n> \n> Allow up to 5 seconds.\n> \n> {footervar()}")
			await asyncio.sleep(3)
			await sent.delete()
			restart_program()
		else:
			embed = discord.Embed(title="Restarting", url=titleurlvar(), description=f"Allow up to 5 seconds.", color=hexcolorvar())
			embed.set_thumbnail(url=imagevar())
			embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
			embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
			embed.set_image(url=largeimagevar())
			sent = await ctx.send(embed=embed)
			await asyncio.sleep(3)
			await sent.delete()
			restart_program()

	@commands.command(name = "clear",
					aliases=['cls'],
					usage="",
					description = "Clear the console")
	async def clear(self, ctx):
		await ctx.message.delete()

		with open("config.json", "r") as f:
			config = json.load(f)
		prefix = config.get('prefix')
        
		Clear()
		Logo()
		print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
		print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
		print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
		print("___________________________________________________________________________________________________")

	@commands.command(name = "fnshop",
					usage="",
					description = "Current Fortnite shop")
	async def fnshop(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title="Fortnite Shop", color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url="https://api.nitestats.com/v1/shop/image")
		await send(ctx, embed)

	@commands.command(name = "fnmap",
					usage="",
					description = "Current Fortnite map")
	async def fnmap(self, ctx):
		await ctx.message.delete()
		embed = discord.Embed(title="Fortnite Map", color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url="https://media.fortniteapi.io/images/map.png?showPOI=true")
		await send(ctx, embed)

	@commands.command(name = "fnnews",
					usage="",
					description = "Current Fortnite news")
	async def fnnews(self, ctx):
		await ctx.message.delete()
		fortnite = requests.get("https://fortnite-api.com/v2/news/br").json()
		embed = discord.Embed(title="Fortnite News", color=hexcolorvar())
		embed.set_footer(text=footervar(), icon_url=footer_iconurlvar())
		embed.set_author(name=authorvar(), url=authorurlvar(), icon_url=author_iconurlvar())
		embed.set_image(url=fortnite["data"]["image"])
		await send(ctx, embed)

bot.add_cog(MiscCog(bot))

if __name__ == '__main__':
	Luna_auth()
