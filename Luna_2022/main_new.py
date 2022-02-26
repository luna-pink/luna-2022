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
from Luna.luna import *

# /////////////////////////////////////////////////////////////////////////////

bot = commands.Bot(command_prefix=get_prefix(), self_bot=True, case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off(), status=statuscon())

# /////////////////////////////////////////////////////////////////////////////
# On_Ready

@bot.event
async def on_ready():
    """Prints a ready log."""
    if files.json("Luna/notifications/toasts.json", "login", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
        notify.toast(message=f"Logged into {bot.user}\nLuna Version » {version}")
    if files.json("Luna/webhooks/webhooks.json", "login", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.login_url() == "webhook-url-here":
        notify.webhook(url=webhook.login_url(), name="login", description=f"Logged into {bot.user}")
    
    luna.console(clear=True)
    command_count = len(bot.commands)
    cog = bot.get_cog('Custom commands')
    try:
        custom = cog.get_commands()
        custom_command_count = 0
        for command in custom:
            custom_command_count += 1
    except:
        custom_command_count = 0
    print(motd.center(os.get_terminal_size().columns))
    if beta:
        print("Beta Build".center(os.get_terminal_size().columns))
        bot_id = str(bot.user.id)
        if not bot_id in beta_user:
            prints.message(
                "You are not a beta user, Luna will close in 5 seconds.")
            time.sleep(5)
            exit()
    prefix = files.json("Luna/config.json", "prefix", documents=True)
    console_mode = files.json("Luna/console/console.json", "mode", documents=True)
    if console_mode == "2":
        mode = int(files.json("Luna/config.json", "mode", documents=True))
        errorlog = files.json("Luna/config.json", "error_log", documents=True)
        riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
        themesvar = files.json("Luna/config.json", "theme", documents=True)
        deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
        startup_status = files.json("Luna/config.json", "startup_status", documents=True)
        nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
        giveawayjoiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
        delay_in_minutes = int(files.json("Luna/snipers/giveaway.json", "delay_in_minutes", documents=True))
        giveaway_server_joiner = files.json("Luna/snipers/giveaway.json", "guild_joiner", documents=True)
        if mode == 1:
            mode = "Embed"
        elif mode == 2:
            mode = "Text"
        elif mode == 3:
            mode = "Indent"
        else:
            mode = "Unknown"
        if afk_status == 1:
            afk = "on"
        else:
            afk = "off"
        if themesvar == "default":
            pass
        else:
            themesvar = themesvar[:-5]
        bot_user = f"{bot.user}"
        ui_user = f" {color.purple('User:')} {bot_user:<26}"
        ui_guilds = f" {color.purple('Guilds:')} {len(bot.guilds):<24}"
        ui_friends = f" {color.purple('Friends:')} {len(bot.user.friends):<23}"
        ui_prefix = f" {color.purple('Prefix:')} {prefix:<24}"
        ui_mode = f" {color.purple('Mode:')} {mode:<26}"
        ui_theme = f" {color.purple('Theme:')} {themesvar:<25}"
        ui_commands = f" {color.purple('Commands:')} {command_count - custom_command_count:<22}"
        ui_commands_custom = f" {color.purple('Custom Commands:')} {custom_command_count:<15}"
        ui_nitro_sniper = f" {color.purple('Nitro Sniper:')} {nitro_sniper}"
        ui_giveaway_sniper = f" {color.purple('Giveaway Joiner:')} {giveawayjoiner}"
        ui_giveaway_delay = f" {color.purple('Giveaway Delay:')} {delay_in_minutes}"
        ui_giveaway_joiner = f" {color.purple('Giveaway Guilds:')} {giveaway_server_joiner}"
        ui_afk = f" {color.purple('AFK Messager:')} {afk}"
        ui_riskmode = f" {color.purple('Riskmode:')} {riskmode}"
        ui_errorlog = f" {color.purple('Errorlog:')} {errorlog}"
        ui_deletetimer = f" {color.purple('Delete Timer:')} {deletetimer}"
        ui_startup = f" {color.purple('Startup Status:')} {startup_status}"
        print()
        print(f"               ═════════════ {color.purple('User')} ═════════════      ═══════════ {color.purple('Settings')} ═══════════")
        print(f"               {ui_user}     {ui_prefix}")
        print(f"               {ui_guilds}     {ui_theme}")
        print(f"               {ui_friends}     {ui_nitro_sniper}")
        print(f"               ════════════════════════════════      {ui_giveaway_sniper}")
        print(f"               ═════════════ {color.purple('Luna')} ═════════════      {ui_riskmode}")
        print(f"               {ui_commands}     {ui_deletetimer}")
        print(f"               {ui_commands_custom}     {ui_startup}")
        print(f"               ════════════════════════════════      ════════════════════════════════\n")
    else:
        print()
        print(f"                           {color.purple('[')}+{color.purple('] CONNECTED')}")
        print(f"                           {color.purple('[')}+{color.purple(']')} {bot.user} | {color.purple(f'{len(bot.guilds)}')} Guilds | {color.purple(f'{len(bot.user.friends)}')} Friends")
        print(f"                           {color.purple('[')}+{color.purple(']')} {prefix}\n")
    print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
    prints.message(f"{color.purple(f'{command_count - custom_command_count}')} commands | {color.purple(f'{custom_command_count}')} custom commands")
    debugger_thread = threading.Thread(target=uptime_thread)
    debugger_thread.daemon = True
    debugger_thread.start()
    upd_thread = threading.Thread(target=update_thread)
    upd_thread.daemon = True
    upd_thread.start()

# /////////////////////////////////////////////////////////////////////////////


def bot_login():
        """Logs in the bot."""
        luna.console(clear=True)

        try:
            path = getattr(sys, '_MEIPASS', os.getcwd())
            cogs_path = path + "\\cogs"
            luna.loader_check()
            for filename in os.listdir(cogs_path):
                if filename.endswith(".py"):
                    bot.load_extension(f"cogs.{filename[:-3]}")
        except:
            pass

        try:
            token = files.json("Luna/discord.json", "token", documents=True)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Content-Type': 'application/json',
                'authorization': Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token)
                }
            r = requests.get(f"https://discordapp.com/api/{api_version}/users/@me", headers=headers).json()
            prints.event(f"Logging into {color.purple(r['username'])}#{color.purple(r['discriminator'])}...")
            global user_token
            user_token = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token)
            bot.run(Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token))
        except Exception as e:
            files.remove('Luna/discord.json', documents=True)
            prints.error(e)
            time.sleep(5)
            prints.event("Redirecting to the main menu in 5 seconds")
            time.sleep(5)
            luna.authentication()
            
bot_login()

