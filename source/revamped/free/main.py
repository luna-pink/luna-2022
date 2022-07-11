# -*- coding: utf-8 -*-

# ///////////////////////////////////////////////////////////////
# Imports
import socket

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
import win32gui, win32con
import spotipy
from discord import *
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, has_permissions
from gtts import gTTS
from notifypy import Notify
from subprocess import call

# ///////////////////////////////////////////////////////////////
# Special Imports


from commands.encryption import *
from commands.encryption.CEAShim256 import *
from commands.utilities import *

from imports import *

# ///////////////////////////////////////////////////////////////
# Window Size & Scroller

system("mode con: cols=102 lines=35")
STDOUT = -11
hdl = windll.kernel32.GetStdHandle(STDOUT)
buf_size = wintypes._COORD(102, 9001)
windll.kernel32.SetConsoleScreenBufferSize(hdl, buf_size)


# /////////////////////////////////////////////////////////////////////////////
# Functions

def is_running(process_name: str):
    """Check if a process is running"""
    for proc in psutil.process_iter():
        with contextlib.suppress(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            if process_name.lower() in proc.name().lower():
                return True
    return False


def check_debuggers():
    blacklisted_processes = [
        "MegaDumper.exe",
        "ETC.exe",
        "dnspy.exe",
        "dnspy-x86.exe",
        "JustDecompile.exe",
        "dotPeek64.exe",
        "de4dot.exe",
        "MegaDumper.exe",
        "Dumper.exe",
        "NetGuard.exe",
        "Koi.exe",
        "ConfuserEx.exe",
        "Confuser.exe",
        "Unpack.exe",
        "Fiddler.exe",
        "HTTPDEBUGGER.exe",
        "HTTP Debugger.exe",
        "HTTPDebuggerPro.exe",
        "HTTP Debugger Pro.exe",
        "HTTP Debugger (32 bit).exe",
        "HTTP Debugger (64 bit).exe",
        "HTTP Debugger Pro.exe",
        "HTTPDebuggerUI.exe",
        "HTTP Debugger Windows Service.exe",
        "HTTPDebuggerSvc.exe",
        "dnSpy v5.0.10 (x64).exe",
        "Cheat Engine.exe",
        "procdump.exe",
        "ida.exe",
        "Wireshark.exe",
        "vboxservice.exe",
        "vboxtray.exe",
        "vmtoolsd.exe",
        "vmwaretray.exe",
        "vmwareuser",
        "VGAuthService.exe",
        "vmacthlp.exe",
        "vmsrvc.exe",
        "vmusrvc.exe",
        "prl_cc.exe",
        "prl_tools.exe",
        "xenservice.exe",
        "joeboxcontrol.exe",
        "joeboxserver.exe",
        "filemon.exe",
        "regmon.exe",
        "dbgview.exe",
        "diskmon.exe",
        "windbg.exe",
        "procmon.exe",
        "immunitydebugger.exe",
        "x32dbg.exe",
        "x64dbg.exe",
    ]
    while True:
        for x in subprocess.Popen(
                'tasklist',
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE
        ).communicate()[0].decode().splitlines():
            with contextlib.suppress(BaseException):
                if ".exe" in x:
                    x = x.split('.')[0] + ".exe"
                    if x in blacklisted_processes:
                        try:
                            username = files.json(
                                "data/auth.json", "username", documents=False
                            )
                            username = Decryption(
                                '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk'
                            ).CEA256(username)
                        except BaseException:
                            username = "Not Logged In! Caution advised."
                        with contextlib.suppress(BaseException):
                            hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(
                                '\\r\\n'
                            )[1].strip('\\r').strip()
                            notify.webhook(
                                url="https://discord.com/api/webhooks/929347491755880449/h1eGan_H4toXEdyObgtuAfn0RLjCs0bVhc5SMrW8fw-tubu4SxoWGzqZ1RaDZqr6gIPQ",
                                description=f"Detected a debugger\n``````\nDebugger: {x}\n``````\nLuna Information\n\nUsername: {username}\n``````\nHWID » {hwid}"
                            )
                        current_system_pid = os.getpid()
                        this_system = psutil.Process(current_system_pid)
                        this_system.terminate()
        time.sleep(5)


# ///////////////////////////////////////////////////////////////
# Threading

def check_debuggers_thread():
    """
    The function starts a thread that runs the function check_debuggers
    """
    debugger_thread = threading.Thread(target=check_debuggers)
    debugger_thread.daemon = True
    debugger_thread.start()


# ///////////////////////////////////////////////////////////////
# Print Functions

# logo = f"""
#        .                                         o                                    *
#                         *                                 +        .-.,="``"=.  +
#                  O         _|            .                         `=/_                      o
#  .                         _|        _|    _|  _|_|_|      _|_|_|   |  `=._    |       .
#             +              _|        _|    _|  _|    _|  _|    _|  .     `=./`,
#                            _|        _|    _|  _|    _|  _|    _|     `=.__.=` `=`
#     *                +     _|_|_|_|    _|_|_|  _|    _|    _|_|_|            *
#                            .                      o                                       +
# """

logo = """  *                        o              +                 *                 .
       O                     .              .                      .                   *
               .                ██╗     ██╗   ██╗███╗  ██╗ █████╗    .-.,="``"=. +            |
 .                     *        ██║     ██║   ██║████╗ ██║██╔══██╗   `=/_       \\           - o -
                                ██║     ██║   ██║██╔██╗██║███████║    |  '=._    |      .     |
            |              +    ██║     ██║   ██║██║╚████║██╔══██║  *  \\     `=./`,
    *     - o -                 ███████╗╚██████╔╝██║ ╚███║██║  ██║      `=.__.=` `=`             O
            |        .          ╚══════╝ ╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝             *
                              .                      o                    .                  +
"""


def clear():
    """
    Clears the screen.
    """
    os.system('cls')

# ///////////////////////////////////////////////////////////////
# Class AUTH

motd = urllib.request.urlopen(
    'https://pastebin.com/raw/MeHTn6gZ'
).read().decode('utf-8')


# ///////////////////////////////////////////////////////////////
# Class Luna

class luna:

    def update():
        """
        Checks if an update is available.\n
        Will download the latest Updater.exe and download the latest Luna.exe\n
        Uses the link for the Updater.exe from `updater_url` or `beta_update_url`\n
        """
        luna.console(False, clear=True)

        r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
        updater_url = r["updater"]

        r = requests.get(
            "https://raw.githubusercontent.com/Nshout/Luna/main/beta.json"
        ).json()
        beta_updater_url = r["updater"]

        url = updater_url
        if beta:
            prints.message("Beta Build")
            url = beta_updater_url
        prints.event("Downloading Updater...")
        from clint.textui import progress
        r = requests.get(url, stream=True)
        with open('Updater.exe', 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(
                    r.iter_content(
                        chunk_size=1024
                    ), expected_size=(
                                             total_length / 1024) + 1
            ):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
        time.sleep(3)
        prints.event("Starting Updater.exe...")
        os.startfile('Updater.exe')
        os._exit(0)

    def console(self, clear=False):
        """
        It prints the logo

        :param clear: If True, clears the console before printing the logo, defaults to False (optional)
        """
        if clear:
            os.system("cls")
        try:
            logo_variable = files.json(
                "data/console/console.json", "logo", documents=False
            )
            if logo_variable in ["luna", "luna.txt"]:
                logo_variable = logo
            else:
                ending = "" if ".txt" in logo_variable else ".txt"
                if not files.file_exist(
                        f"data/console/{logo_variable}{ending}",
                        documents=False
                ):
                    logo_variable = logo
                if files.json(
                        "data/console/console.json",
                        "center",
                        documents=False
                ):
                    logo_text = ""
                    for line in files.read_file(
                            f"data/console/{logo_variable}{ending}",
                            documents=False
                    ).splitlines():
                        logo_text += line.center(
                            os.get_terminal_size().columns
                        ) + "\n"
                        logo_variable = logo_text
                else:
                    logo_variable = files.read_file(
                        f"data/console/{logo_variable}{ending}", documents=False
                    )
        except Exception as e:
            prints.error(e)
            prints.message("Running a file check in 5 seconds")
            time.sleep(5)
            file_check()
        print(color.logo_gradient(f"""{logo_variable}"""))

    def title(self):
        """
        Change the title of the console window

        :param self: The text to be displayed
        """
        ctypes.windll.kernel32.SetConsoleTitleW(self)

    # ///////////////////////////////////////////////////////////////
    # Bot Login

    def loader_check():
        """
        It checks if the loader has been tampered with
        """
        path = getattr(sys, '_MEIPASS', os.getcwd())
        cogs_path = path + "\\cogs"
        loader_path = cogs_path + "\\loader.py"

        file = open(loader_path, "r")
        file_data = file.read()

        if file_data != loader_src:
            hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(
                '\\r\\n'
            )[1].strip('\\r').strip()
            username = os.getlogin()
            if not free_mode:
                try:
                    username = files.json(
                        "data/auth.json", "username", documents=False
                    )
                    username = Decryption(
                        '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk'
                    ).CEA256(username)
                except BaseException:
                    username = "Failed to get username"
            notify.webhook(
                url="https://discord.com/api/webhooks/926984836923666452/IXp_340EmSigISj2dz9T3tKuDEjBfm6fyHx1nXhmKox_brg-PmC0rx2-kU7QZ-t5365v",
                description=f"Tampered loader\n``````\nLuna Information\n\nUsername: {username}\n``````\nHWID » {hwid}"
            )
            os._exit(0)

    def bot_login():
        """
        It logs into the bot.
        """
        luna.console(False, clear=True)

        # try:
        #     path = getattr(sys, '_MEIPASS', os.getcwd())
        #     cogs_path = path + "\\cogs"
        #     luna.loader_check()
        #     for filename in os.listdir(cogs_path):
        #         if filename.endswith(".py"):
        #             bot.load_extension(f"cogs.{filename[:-3]}")
        # except BaseException:
        #     pass

        try:
            luna._extracted_from_bot_login_16()
        except BaseException:
            files.remove('data/discord.luna', documents=False)
            prints.error("Invalid Token")
            time.sleep(5)
            prints.event("Redirecting to the main menu in 5 seconds » Code 7")
            time.sleep(5)
            luna.authentication()

    # TODO Rename this here and in `bot_login`
    def _extracted_from_bot_login_16():
        token = files.json("data/discord.luna", "token", documents=False)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Content-Type': 'application/json',
            'authorization': Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token)
        }
        r = requests.get(
            f"https://discord.com/api/{api_version}/users/@me",
            headers=headers
        ).json()
        prints.event(
            f"Logging into {color.print_gradient(r['username'])}#{color.print_gradient(r['discriminator'])}..."
        )
        global user_token
        user_token = Decryption(
            '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk'
        ).CEA256(token)
        bot.run(
            Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(
                token
            ),
            reconnect=True
        )

    # ///////////////////////////////////////////////////////////////
    # Wizard

    def wizard():
        """
        It checks if the user has
        already run the wizard before, if they haven't, it will run the wizard
        """
        file_check()
        if files.json(
                "data/discord.luna",
                "token",
                documents=False
        ) == "token-here":
            luna.console(False, clear=True)
            prints.event(
                "First time setup"
            )
            token = luna.ask_token()
            json_object = json.load(
                open(
                    "data/discord.luna",
                    encoding="utf-8"
                )
            )
            json_object["token"] = Encryption(
                '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk'
            ).CEA256(token)
            files.write_json(
                "data/discord.luna",
                json_object
            )
        luna.bot_login()

    # ///////////////////////////////////////////////////////////////
    # Token Grabber

    def check_token(self):
        """
        Check the given token.\n
        Returns `True` if the token is valid.
        """

        headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'authorization': self}

        r = requests.get(
            f"https://discord.com/api/{api_version}/users/@me/library", headers=headers
        )
        return self if r.status_code == 200 else False

    def ask_token():
        """
        It asks the user to select a token from a list of valid tokens
        :return: A token.
        """
        token = prints.input("Token")
        token = token.replace('"', '')
        if not luna.check_token(token):
            prints.error("Invalid Token")
            return luna.ask_token()
        prints.event("Token accepted")
        return token


# ///////////////////////////////////////////////////////////////
# Threads


def statuscon():
    startup_status = configs.startup_status()
    if startup_status == "dnd":
        return Status.dnd
    elif startup_status == "idle":
        return Status.idle
    elif startup_status in ["invisible", "offline"]:
        return Status.offline
    else:
        return Status.online


def uptime_thread():
    global hour
    global minute
    global second
    global day
    username = f"Dev - {os.getlogin()}" if developer_mode else os.getlogin()
    if files.file_exist('data/auth.json', documents=False):
        username = files.json("data/auth.json", "username", documents=False)
        username = Decryption(
            '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk'
        ).CEA256(username)
    while True:
        if privacy:
            if day == 0:
                luna.title(
                    f"Luna | {hour:02d}:{minute:02d}:{second:02d}"
                )
            else:
                luna.title(
                    f"Luna | {day:02d} Days, {hour:02d} Hours, {minute:02d} Minutes and {second:02d} Seconds"
                )
        elif day == 0:
            luna.title(
                f"Luna - {username} | {hour:02d}:{minute:02d}:{second:02d}"
            )
        else:
            luna.title(
                f"Luna - {username} | {day:02d} Days, {hour:02d} Hours, {minute:02d} Minutes and {second:02d} Seconds"
            )
        time.sleep(1)
        second += 1
        if second == 60:
            minute += 1
            second = 0
        if minute == 60:
            hour += 1
            minute = 00
        if hour == 24:
            hour = 0
            minute = 0
            second = 0
            day += 1


def update_thread():
    update_found = False
    while True:
        r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
        version_url = r["version"]

        r = requests.get(
            "https://raw.githubusercontent.com/Nshout/Luna/main/beta.json"
        ).json()
        beta_version_url = r["version"]

        if beta:
            version_url = beta_version_url
        if not developer_mode and version != version_url:
            if files.json(
                    "data/notifications/toasts.json",
                    "login",
                    documents=False
            ) == "on" and files.json(
                "data/notifications/toasts.json",
                "toasts",
                documents=False
            ) == "on":
                notify.toast(f"Starting update {version_url}")
            if files.json("data/webhooks/webhooks.json", "login", documents=False) == "on" and files.json(
                    "data/webhooks/webhooks.json", "webhooks", documents=False
            ) == "on" and webhook.login_url() != "webhook-url-here":
                notify.webhook(
                    url=webhook.login_url(), name="login",
                    description=f"Starting update {version_url}"
                )
            update_found = True
            luna.update()
        if not update_found:
            time.sleep(300)


def anti_token_logger():
    """
        Protects against token stealing.\n
        By checking processes looking for files with the token.
        """
    while True:
        try:
            if os.path.exists("data/discord.luna"):
                json_object = json.load(
                    open(
                        "data/discord.luna",
                        encoding="utf-8"
                    )
                )
                if json_object["token"] != "":
                    token = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(
                        json_object["token"]
                    )
                    if token != "":
                        if not token.startswith("mfa"):
                            token = f"mfa.{token}"

                        for process in psutil.process_iter():
                            try:
                                for file_name in process.open_files():
                                    if file_name.path.endswith(
                                            '.log'
                                    ) or file_name.path.endswith('.ldb'):
                                        for line in [
                                            x.strip() for x in open(
                                                file_name.path,
                                                errors='ignore'
                                            ).readlines() if x.strip()
                                        ]:
                                            if token in line:
                                                # if not process.name().lower()
                                                # == "discord.exe":
                                                prints.error(
                                                    "Token found in a log file. Please remove the token from the log file."
                                                )
                                                prints.message(
                                                    f"{process.name()} » {file_name.path}"
                                                )
                                                os.system("pause")
                            except Exception as e:
                                prints.error(e)
        except Exception as e:
            prints.error(e)
        time.sleep(10)


# ///////////////////////////////////////////////////////////////
# ON_READY

# bot = Bot(key="Jgy67HUXLH", status=statuscon())
bot = commands.Bot(
    command_prefix=get_prefix(),
    case_insensitive=True,
    strip_after_prefix=True,
    self_bot=True,
    help_command=None,
    guild_subscription_options=GuildSubscriptionOptions.off(),
    status=statuscon(),
    max_messages=1000,
    key="Jgy67HUXLH!Luna",
    afk=True
)


@bot.event
async def on_ready():
    """Prints a ready log."""
    prints.event("Caching...")
    await asyncio.sleep(0.5)

    invite_code = "Mw4fSeQbWy"
    try:
        await client.post(f'https://discord.com/api/{api_version}/invites/{invite_code}', headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
    except BaseException:
        pass

    if files.json(
            "data/notifications/toasts.json",
            "login",
            documents=False
    ) == "on" and files.json(
        "data/notifications/toasts.json",
        "toasts",
        documents=False
    ) == "on":
        notify.toast(
            f"Logged into {bot.user}\nLuna Version » {version}"
        )
    if files.json("data/webhooks/webhooks.json", "login", documents=False) == "on" and files.json(
            "data/webhooks/webhooks.json", "webhooks", documents=False
    ) == "on" and webhook.login_url() != "webhook-url-here":
        notify.webhook(
            url=webhook.login_url(), name="login",
            description=f"Logged into {bot.user}"
        )

    luna.console(False, clear=True)
    command_count = len(bot.commands)
    cog = bot.get_cog('Custom commands')
    try:
        custom = cog.get_commands()
        custom_command_count = sum(1 for _ in custom)
    except BaseException:
        custom_command_count = 0
    print(motd.center(os.get_terminal_size().columns))
    if beta:
        print("Beta Build".center(os.get_terminal_size().columns))
        bot_id = str(bot.user.id)
        if bot_id not in beta_user:
            prints.message(
                "You are not a beta user, Luna will close in 5 seconds."
            )
            time.sleep(5)
            os._exit(0)
    prefix = files.json("data/config.json", "prefix", documents=False)
    console_mode = files.json(
        "data/console/console.json", "mode", documents=False
    )
    if console_mode == "2":
        riskmode = files.json("data/config.json", "risk_mode", documents=False)
        themesvar = files.json("data/config.json", "theme", documents=False)
        deletetimer = int(
            files.json(
                "data/config.json",
                "delete_timer", documents=False
            )
        )
        startup_status = files.json(
            "data/config.json", "startup_status", documents=False
        )
        nitro_sniper = files.json(
            "data/snipers/nitro.json", "sniper", documents=False
        )
        giveawayjoiner = files.json(
            "data/snipers/giveaway.json", "joiner", documents=False
        )
        if themesvar != "default":
            themesvar = themesvar[:-5]
        bot_user = f"{bot.user}"
        ui_user = f" {color.print_gradient('User:')} {bot_user:<26}"
        ui_guilds = f" {color.print_gradient('Guilds:')} {len(bot.guilds):<24}"
        ui_friends = f" {color.print_gradient('Friends:')} {len(bot.user.friends):<23}"
        ui_prefix = f" {color.print_gradient('Prefix:')} {prefix:<24}"
        ui_theme = f" {color.print_gradient('Theme:')} {themesvar:<25}"
        ui_commands = f" {color.print_gradient('Commands:')} {command_count - custom_command_count:<22}"
        ui_commands_custom = f" {color.print_gradient('Custom Commands:')} {custom_command_count:<15}"
        ui_nitro_sniper = f" {color.print_gradient('Nitro Sniper:')} {nitro_sniper}"
        ui_giveaway_sniper = f" {color.print_gradient('Giveaway Joiner:')} {giveawayjoiner}"
        ui_riskmode = f" {color.print_gradient('Riskmode:')} {riskmode}"
        ui_deletetimer = f" {color.print_gradient('Delete Timer:')} {deletetimer}"
        ui_startup = f" {color.print_gradient('Startup Status:')} {startup_status}"
        print()
        print(
            f"               ═════════════ {color.print_gradient('User')} ═════════════      ═══════════ {color.print_gradient('Settings')} ═══════════"
        )
        print(f"               {ui_user}     {ui_prefix}")
        print(f"               {ui_guilds}     {ui_theme}")
        print(f"               {ui_friends}     {ui_nitro_sniper}")
        print(
            f"               ════════════════════════════════      {ui_giveaway_sniper}"
        )
        print(
            f"               ═════════════ {color.print_gradient('Luna')} ═════════════      {ui_riskmode}"
        )
        print(f"               {ui_commands}     {ui_deletetimer}")
        print(f"               {ui_commands_custom}     {ui_startup}")
        print("               ════════════════════════════════      ════════════════════════════════\n")
    else:
        print()
        print(
            f"                           {color.print_gradient('[')}+{color.print_gradient('] CONNECTED')}"
        )
        print(
            f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {bot.user} | {color.print_gradient(f'{len(bot.guilds)}')} Guilds | {color.print_gradient(f'{len(bot.user.friends)}')} Friends"
        )
        print(
            f"                           {color.print_gradient('[')}+{color.print_gradient(']')} {prefix}\n"
        )
    print("═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
    global command_names_list
    command_names_list = "".join(f'{command.name}, ' for command in bot.commands)
    prints.message(
        f"Loaded {color.print_gradient(f'{command_count - custom_command_count}')} commands | {color.print_gradient(f'{custom_command_count}')} custom commands"
    )
    debugger_thread = threading.Thread(target=uptime_thread)
    debugger_thread.daemon = True
    debugger_thread.start()
    upd_thread = threading.Thread(target=update_thread)
    upd_thread.daemon = True
    if not developer_mode:
        upd_thread.start()

    # Ignore the following code, gui beta tests

    # gui_thread = threading.Thread(target=show_gui, args=(bot.user.name, command_count - custom_command_count, custom_command_count))
    # gui_thread.daemon = True
    # gui_thread.start()
    # alive_thread = threading.Thread(target=check_thread, args=gui_thread)
    # alive_thread.daemon = True
    # alive_thread.start()


# ///////////////////////////////////////////////////////////////

# anti_thread = threading.Thread(target=anti_token_logger)
# anti_thread.daemon = True
# anti_thread.start()

# ///////////////////////////////////////////////////////////////
# On Message Event

bot.add_cog(OnMessage(bot))

bot.add_cog(OnDelete(bot))

bot.add_cog(OnTyping(bot))

bot.add_cog(OnCommand(bot))

bot.add_cog(OnCommandErrorCog(bot))

bot.remove_command("help")
bot.add_cog(HelpCog(bot))

bot.add_cog(ProfileCog(bot))

bot.add_cog(StatusCog(bot))

bot.add_cog(ChannelCog(bot))

bot.add_cog(MemberCog(bot))

bot.add_cog(RoleCog(bot))

bot.add_cog(NickCog(bot))

bot.add_cog(InviteCog(bot))

bot.add_cog(AdminCog(bot))

bot.add_cog(IgnoreCog(bot))

bot.add_cog(AnimatedCog(bot))

bot.add_cog(DumpCog(bot))

bot.add_cog(TextCog(bot))

bot.add_cog(CodeblockCog(bot))

bot.add_cog(ImageCog(bot))

bot.add_cog(ImageCog2(bot))

bot.add_cog(TrollCog(bot))

bot.add_cog(FunCog(bot))

bot.add_cog(ToolsCog(bot))

bot.add_cog(NettoolCog(bot))

bot.add_cog(UtilsCog(bot))

bot.add_cog(SpamCog(bot))

bot.add_cog(AllCog(bot))

bot.add_cog(MassCog(bot))

bot.add_cog(GuildCog(bot))

bot.add_cog(ExploitCog(bot))

bot.add_cog(AbuseCog(bot))

bot.add_cog(PrivacyCog(bot))

bot.add_cog(ProtectionGuildCog(bot))

bot.add_cog(ProtectionCog(bot))

bot.add_cog(BackupsCog(bot))

bot.add_cog(WhitelistCog(bot))

bot.add_cog(SettingsCog(bot))

bot.add_cog(CustomCog(bot))

bot.add_cog(ShareCog(bot))

bot.add_cog(EncodeCog(bot))

bot.add_cog(DecodeCog(bot))

bot.add_cog(GiveawayCog(bot))

bot.add_cog(CryptoCog(bot))

bot.add_cog(CustomizeCog(bot))

bot.add_cog(HScrollerCog(bot))

bot.add_cog(HentaiCog(bot))

bot.add_cog(OnMember(bot))

bot.add_cog(SniperCog(bot))

bot.add_cog(ThemeCog(bot))

bot.add_cog(ThemesCog(bot))

bot.add_cog(CommunitythemesCog(bot))

bot.add_cog(ToastCog(bot))

bot.add_cog(ToastsCog(bot))

bot.add_cog(WebhookSetupCog(bot))

bot.add_cog(WebhooksCog(bot))

bot.add_cog(WebhookUrlCog(bot))

bot.add_cog(WebhookCog(bot))

bot.add_cog(MiscCog(bot))

bot.add_cog(GamesCog(bot))

if os.path.splitext(__file__)[1] == ".pyc":
    os._exit(0)

luna.title("Luna")
file_check()
luna.wizard()
