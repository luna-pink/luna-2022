import discord
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
import discum
import psutil
import typing
import aiohttp
import asyncio
import hashlib
import pwinput
import requests
import platform
import threading
import subprocess
import pypresence

import pyPrivnote
import ctypes.wintypes as wintypes

from gtts import gTTS
from ctypes import windll
from notifypy import Notify
from os import error, system
from datetime import datetime
from pypresence import Presence
from discord.ext import commands
from time import localtime, strftime

import discord
from discord import *
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, core, has_permissions

# /////////////////////////////////////////////////////////////////////////////

from FileHandling.filehandler import *
from FileHandling.jsonhandler import *
from Security.cea256 import *
from Security.authentication import *
from variables import *
from Functions.color import *
from Functions.threads import *

# /////////////////////////////////////////////////////////////////////////////

bot = commands.Bot(command_prefix=get_prefix(), self_bot=True, case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off(), status=statuscon())

# /////////////////////////////////////////////////////////////////////////////
