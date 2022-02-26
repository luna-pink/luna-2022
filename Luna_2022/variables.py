import requests

# /////////////////////////////////////////////////////////////////////////////
# Developer Control

developer_mode = True
beta = False
version = '3.2.9h2'
api_version = 'v10'

# /////////////////////////////////////////////////////////////////////////////
# Luna

logo = f"""  *                        o              +                 *                 .
       O                     .              .                      .                   *
               .                ██╗     ██╗   ██╗███╗  ██╗ █████╗    .-.,="``"=. +            |
 .                     *        ██║     ██║   ██║████╗ ██║██╔══██╗   `=/_       \           - o -
                                ██║     ██║   ██║██╔██╗██║███████║    |  '=._    |      .     |
            |              +    ██║     ██║   ██║██║╚████║██╔══██║  *  \     `=./`, 
    *     - o -                 ███████╗╚██████╔╝██║ ╚███║██║  ██║      `=.__.=` `=`             O
            |        .          ╚══════╝ ╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝             *    
                              .                      o                    .                  +
"""

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

r = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/beta.json").json()
beta_updater_url = r["updater"]
beta_version_url = r["version"]
beta_user = r["beta_user"]

if beta:
    version_url = beta_version_url

# /////////////////////////////////////////////////////////////////////////////
# Bot

default_prefix = '.'
caching = False

# /////////////////////////////////////////////////////////////////////////////
# Protections

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

# /////////////////////////////////////////////////////////////////////////////
# Proxies

proxy_list = {
    "http": "http://203.150.128.208:8080",
    "http": "http://182.111.172.108:32997",
    "http": "http://106.55.31.128:9999",
    "http": "http://47.92.234.75:80",
    "http": "http://103.245.108.186:8000",
    "http": "http://201.28.120.142:3128",
    "http": "http://47.243.200.250:59394",
    "http": "http://203.189.89.158:8080",
    "http": "http://50.206.25.109:80",
    "http": "http://43.129.174.230:9999",
    "http": "http://193.19.97.152:8080",
    "http": "http://193.164.131.202:7890",
    "http": "http://88.198.24.108:8080",
    "http": "http://59.66.142.35:7890",
    "http": "http://47.243.196.231:59394",
    "http": "http://178.73.192.3:8888",
    "http": "http://49.233.173.151:9080",
    "http": "http://20.194.181.91:80",
    "http": "http://103.99.8.106:83",
    "http": "http://212.112.127.20:8080",
    "http": "http://47.56.120.158:80",
    "http": "http://213.163.2.206:3128",
    "http": "http://51.79.144.52:8000",
    "http": "http://203.189.231.154:8080",
    "http": "http://212.95.75.12:80",
    "http": "http://85.26.146.169:80",
    "http": "http://51.159.5.133:3128",
    "http": "http://200.114.97.4:999",
    "http": "http://47.52.134.184:8118",
    "http": "http://107.151.182.247:80",
    "http": "http://50.206.25.104:80",
    "http": "http://51.81.155.78:3128",
    "http": "http://218.86.87.171:31661",
    "http": "http://221.131.158.246:8888",
    "http": "http://94.130.151.31:80",
    "http": "http://58.20.234.243:9091",
    "http": "http://212.92.204.54:8080",
    "http": "http://50.206.25.106:80",
    "http": "http://50.233.42.98:51696",
    "http": "http://159.192.226.46:8080",
    "http": "http://213.182.139.164:8080",
    "http": "http://50.206.25.110:80",
    "http": "http://159.65.132.219:1234",
    "http": "http://51.222.124.242:3128",
    "http": "http://58.187.46.247:4204",
    "http": "http://221.125.138.189:80",
    "http": "http://51.222.124.243:3128",
    "http": "http://164.163.12.50:8080",
    "http": "http://171.67.43.170:8080",
    "http": "http://58.115.241.109:80"
}

# ///////////////////////////////////////////////////////////////
# Luna

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
	bot.add_cog(CustomCog(bot))"""
