# ///////////////////////////////////////////////////////////////
# Imports

import asyncio
import ctypes
import ctypes.wintypes as wintypes
import hashlib
import platform
import re
import subprocess
import sys
import threading
import time
import typing
import urllib
from ctypes import windll
from os import error, system
from time import localtime, strftime
from datetime import datetime

import aiohttp
import dhooks
import discord
import httpx
import psutil
import pwinput
import pyPrivnote
import qrcode
import pypresence
from discord import *
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, has_permissions
from gtts import gTTS
from notifypy import Notify

# ///////////////////////////////////////////////////////////////
# Special Imports


from Authentication.atlas import *
from Functions import *
from variables import *
# from wrapper import Bot

# bot = Bot(key="Jgy67HUXLH", status="online")
bot = commands.Bot(command_prefix=".", case_insensitive=True, self_bot=True, help_command=None)


@bot.event
async def on_ready():
    print("Bot is ready")
    await bot.change_presence(activity=discord.Game(name="with humans"))

token = "mfa.eJQ5-hd9LUUnnmbYGD_LPD1Ag9X986AK8D5b3rYLvVEkkW_73GOQVdhb_yyLWurykM-d_a-zPlrDGhIDpoHK"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'authorization': token
}
r = requests.get(
    f"https://discordapp.com/api/{api_version}/users/@me",
    headers=headers
).json()
print(
    f"Logging into {r['username']}#{r['discriminator']}..."
)
global user_token
user_token = token
bot.run(
    token, reconnect=True
)