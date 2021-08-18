import asyncio
import discord
from discord.embeds import Embed
from discord.ext import commands

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

# Imports for the cogs to prevent hidden imports.
import pyPrivnote
import CEA256
import httpx
import dhooks
import gtts

from ctypes import byref, windll
from datetime import datetime
from colorama import init
from os import system
from AuthGG.client import Client as Authgg
from tqdm import tqdm
from discord import *

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
# Datetime Timestamp


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

# ///////////////////////////////////////////////////////////////
# Luna Variables

lunaversion = "2.0.9"

cooldown = []
whitelisted_users = {}
afk_stat = 0
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
    with open(f"data/themes/{themesvar}", encoding='utf-8') as f:
        customi = json.load(f)
    descriptionvar = customi.get('description')
    if descriptionvar:
        descriptionvar = "<> = required, [] = optional\n\n"
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


path = getattr(sys, '_MEIPASS', os.getcwd())
ico_path = path + "\\images\\ico\\"
cogs_path = path + "\\cogs"

if __name__ == '__main__':
    # bot.load_extension(f"data.custom.custom")
    # for filename in os.listdir("cogs"):
    for filename in os.listdir(cogs_path):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
            # print(f"Cogs.{filename[:-3]}")

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

            if lunaversion in versionpaste:
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
                print(
                    "____________________________________________________________________________________________________")
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
                print("Starting Luna...")
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
        print("[1] Please enter your key: LOLICON-XXXXX-XXXXX-XXXXX-XXXXX")
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
    # print(f"                          {bcolors.LIGHTMAGENTA}╔══════════════════════════════════════╗{bcolors.RESET}")
    print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bcolors.LIGHTMAGENTA}CONNECTED{bcolors.RESET}")
    print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {bot.user} | {len(bot.guilds)} Servers | {len(bot.user.friends)} Friends")
    print(f"                           {bcolors.LOGOCOLOR2}[{bcolors.LOGOCOLOR1}+{bcolors.LOGOCOLOR2}]{bcolors.RESET} {prefix}")
    # print(f"                          {bcolors.LIGHTMAGENTA}╚══════════════════════════════════════╝{bcolors.RESET}")
    print("___________________________________________________________________________________________________")
    await asyncio.sleep(0.02)
    # print(f"{timestampStr} | {bcolors.MESSAGE}{Message}{bcolors.RESET} | {motd}")
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

    # ///////////////////////////////////////////////////////////////
    # Charge status

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    #     'Content-Type': 'application/json',
    #     'Authorization': token,
    # }
    #
    # with open('./config.json') as f:
    #     config = json.load(f)
    # startup_status = config.get('startup_status')
    # if startup_status == "dnd":
    #     status = "dnd"
    # elif startup_status == "idle":
    #     status = "idle"
    # else:
    #     status = "online"
    #
    # request = requests.Session()
    # setting = {
    #     'status': f"{status}",
    #     "custom_status": {"text": "Charge [##########]"}
    # }
    # # request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)


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
        './data/webhooks.json') and file_exist('./data/backup/friends.txt') and file_exist('./data/backup/blocked.txt'):
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
                "footer_iconurl": "https://cdn.discordapp.com/attachments/848299943172505611/876947469555093584/Luna.png",
                "imageurl": "https://cdn.discordapp.com/attachments/848299943172505611/876947469555093584/Luna.png",
                "large_imageurl": "",
                "hexcolor": "#A96DD8",
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

                r = requests.get(
                    "https://cdn.discordapp.com/attachments/848299943172505611/876944029017845790/luna.ico",
                    stream=True)

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
                "imageurl": "https://cdn.discordapp.com/attachments/848299943172505611/868676317174980608/LunaRe.png",
                "hexcolor": "#bd93f9"
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
        "theme": "luna.json",
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
            text_mode_builder = f"```ini\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('**', '')}\n[ {embed.footer.text} ]\n```"
        else:
            text_mode_builder = f"```ini\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('**', '')}\n\n[ {embed.footer.text} ]\n```"
        return text_mode_builder
    elif embed.image.url == largeimagevar:
        if embed.description.endswith("\n"):
            text_mode_builder = f"```ini\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('**', '')}\n[ {embed.footer.text} ]\n```"
        else:
            text_mode_builder = f"```ini\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('**', '')}\n\n[ {embed.footer.text} ]\n```"
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
            indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
        else:
            indent_builder = f"> **{embed.title}**\n> \n{text}> \n> {embed.footer.text}"
        return indent_builder
    elif embed.image.url == largeimagevar:
        text = ""

        for line in embed.description.split("\n"):
            indent = "> " + line
            text += indent + "\n"

        if embed.description.endswith("\n"):
            indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
        else:
            indent_builder = f"> **{embed.title}**\n> \n{text}> \n> {embed.footer.text}"
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

if __name__ == '__main__':
    Luna_auth()
