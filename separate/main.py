import dearpygui.dearpygui as dpg

import asyncio
import base64
import contextlib
import ctypes
import ctypes.wintypes as wintypes
import hashlib
import platform
import random
import re
import string
import subprocess
import sys
import threading
import time
import typing
import urllib
import json
import gzip
from ctypes import windll
from datetime import datetime
from os import error, system
from time import localtime, strftime

import aiohttp
import dhooks
import discord
import httpx
import psutil
import pwinput
import pyPrivnote
import discord_rpc
import qrcode
import sys
import os
import win32gui, win32con
import spotipy
from discord import *
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, has_permissions
from gtts import gTTS
from notifypy import Notify
from subprocess import call

from pathlib import Path

# ////////////////////////////////////////////////////////////////////////////

token = "OTkxMDM1NDg3OTQ0ODM5MTY5.GPiYVZ.MVIgHCw8u0GAWhL8_XUeK0d0zMcs6Am7lIUIA8"

bot = commands.Bot(
    command_prefix=".",
    case_insensitive=True,
    strip_after_prefix=True,
    self_bot=True,
    help_command=None,
    guild_subscription_options=GuildSubscriptionOptions.off(),
    max_messages=1000,
    key="Jgy67HUXLH!Luna",
    afk=True
)

# ////////////////////////////////////////////////////////////////////////////

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    bundle_dir = Path(sys._MEIPASS)
else:
    bundle_dir = Path(__file__).parent
print(bundle_dir)

for f in os.listdir(f"{bundle_dir}/cogs"):
    if f.endswith(".py"):
        bot.load_extension("cogs." + f[:-3])
        print("cogs." + f[:-3])

# ////////////////////////////////////////////////////////////////////////////

print("logging in")
bot.run(token)