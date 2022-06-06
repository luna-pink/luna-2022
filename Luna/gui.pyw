import dearpygui.dearpygui as dpg

import asyncio
import base64
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
import qrcode
from discord import *
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, has_permissions
from gtts import gTTS
from notifypy import Notify
from subprocess import call

# ///////////////////////////////////////////////////////////////
# Special Imports

from Authentication.atlas import *
from Functions import *
from variables import *
from Encryption import *
from Encryption.CEAShim256 import *

auth_luna = Atlas(
    "45.41.240.7", 9696,
    "97555040593864335346", "RPstUMSxDn9qXLnABEt3UdwZnJnBfNSa"
)

motd = urllib.request.urlopen(
    'https://pastebin.com/raw/MeHTn6gZ'
).read().decode('utf-8')

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


def login():
    if not files.file_exist('data/auth.json', documents=False):
        def auth_connect(username, password):
            dpg.set_value(status, "Status: Connecting to server...")
            print("Connecting to Atlas...")
            try:
                auth_luna.connect()
                dpg.set_value(status, "Status: Connected to server")
            except BaseException:
                dpg.set_value(status, "Status: Connection failed")
                print("Failed to connect to Atlas")
            auth_luna.Identify(username)

        def auth_validate():
            hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(
                '\\r\\n'
            )[1].strip('\\r').strip()
            auth_luna.ValidateUserHWID(hwid)
            auth_luna.ValidateEntitlement("LunaSB")

        def auth_register():
            def register_check():
                hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(
                    '\\r\\n'
                )[1].strip('\\r').strip()

                username_value = dpg.get_value(username)
                password_value = dpg.get_value(password)
                confirm_password_value = dpg.get_value(confirm_password)
                key_value = dpg.get_value(key)
                invite_value = dpg.get_value(invite)

                if username_value == "" or password_value == "" or confirm_password_value == "" or key_value == "" or invite_value == "":
                    dpg.set_value(status, "Status: Please fill in all fields")
                    return

                if password_value != confirm_password_value:
                    print("Passwords do not match")
                    dpg.set_value(status, "Status: Passwords do not match")
                    return

                try:
                    dpg.set_value(status, "Status: Connecting to server...")
                    print("Connecting to Atlas...")
                    auth_luna.connect()
                    dpg.set_value(status, "Status: Connected to server")
                except BaseException:
                    dpg.set_value(status, "Status: Connection failed")
                    print("Failed to connect to Atlas")
                    return
                try:
                    auth_luna.CheckLicenseKeyValidity(key_value)
                    dpg.set_value(status, "Status: Checking license key...")
                    auth_luna.Register(username_value, password_value)
                    dpg.set_value(status, "Status: Registering...")
                    auth_luna.Identify(username_value)
                    auth_luna.Login(username_value, password_value)
                    dpg.set_value(status, "Status: Logging in...")
                    auth_luna.InitAppUser(hwid)
                    auth_luna.RedeemEntitlement(key_value, "LunaSB")
                    auth_luna.disconnect()
                except Exception as e:
                    dpg.set_value(status, f"Status: {str(e)}")
                    print(e)
                    auth_luna.disconnect()
                    return

                print("Successfully registered")
                dpg.set_value(status, "Status: Successfully registered")
                username_value = Encryption(
                    '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk'
                ).CEA256(username_value)
                password_value = Encryption(
                    '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk'
                ).CEA256(password_value)
                data = {
                    "username": f"{username_value}",
                    "password": f"{password_value}"
                }
                files.write_json("data/auth.json", data, documents=False)

                # dpg.delete_item(item="register")

            def close_register():
                dpg.delete_item(item="register")

            with dpg.window(label="Register", tag="register", width=784, height=600, no_resize=True, no_collapse=True):
                username = dpg.add_input_text(label="Username", default_value="")
                password = dpg.add_input_text(label="Password", default_value="", password=True)
                confirm_password = dpg.add_input_text(label="Confirm Password", default_value="", password=True)
                key = dpg.add_input_text(label="Key", default_value="")
                invite = dpg.add_input_text(label="Invite", default_value="")
                dpg.add_separator()
                status = dpg.add_text("Status: Not Registered.")
                dpg.add_separator()
                with dpg.group(horizontal=True, label="group_buttons"):
                    dpg.add_button(label="Register", callback=register_check)
                    dpg.add_button(label="Login", callback=close_register)

        def auth_login():
            username_value = dpg.get_value(username)
            password_value = dpg.get_value(password)
            if username_value == "" or password_value == "":
                print("Username or password is empty")
                dpg.set_value(status, "Status: Please enter a username and password.")
                return
            try:
                auth_connect(username_value, password_value)
                auth_luna.Login(username_value, password_value)
                auth_validate()
                username_value = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username_value)

                password_value = Encryption(
                    '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk'
                ).CEA256(password_value)
                data = {"username": f"{username_value}", "password": f"{password_value}"}
                files.write_json("data/auth.json", data, documents=False)
                dpg.set_value(status, "Status: Logged in")
                # dpg.delete_item(item="auth")
                auth_luna.disconnect()
                return login()
            except BaseException:
                print("Failed to login.")
                dpg.set_value(status, "Status: Failed to login")
                return

        # ///////////////////////////////////////////////////////////////

        with dpg.window(label="Authentication", tag="auth", width=784, height=600, no_resize=True, no_collapse=True):
            username = dpg.add_input_text(label="Username", default_value="")
            password = dpg.add_input_text(label="Password", default_value="", password=True)
            dpg.add_separator()
            status = dpg.add_text("Status: Not Authenticated")
            dpg.add_separator()
            with dpg.group(horizontal=True, label="group_buttons"):
                dpg.add_button(label="Register", callback=auth_register)
                dpg.add_button(label="Login", callback=auth_login)
    else:

        # ///////////////////////////////////////////////////////////////

        if files.json("data/discord.luna", "token", documents=False) == "token-here":
            print("login()")

            def get_token_value():
                token = dpg.get_value(token_input)
                check = dpg.get_value(account)
                if check == "No Token Entered" or token == "":
                    dpg.set_value(account, "Enter the token first")
                    return
                elif check == "Invalid Token":
                    dpg.set_value(account, "Cannot log into an invalid token")
                    return
                elif check == "Check the account after entering the token" or "Valid Token" not in check:
                    dpg.set_value(account, "Check the account first")
                    return
                print("Valid Token Entered")
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
                print("Token Saved")
                dpg.set_value(account, "Logging in...")

                # ///////////////////////////////////////////////////////////////
                dpg.delete_item(item="setup")

                return login()

            def get_token_user():
                token = dpg.get_value(token_input)
                token = token.replace('"', '')
                if token == "":
                    dpg.set_value(account, "No Token Entered")
                    return
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                        'Content-Type': 'application/json',
                        'authorization': token
                    }
                    r = requests.get(
                        f"https://discordapp.com/api/{api_version}/users/@me",
                        headers=headers
                    ).json()
                    dpg.set_value(account, f"Valid Token: {r['username']}#{r['discriminator']}")
                except BaseException:
                    dpg.set_value(account, "Invalid Token")

            with dpg.window(label="First Time Setup", tag="setup", width=784, height=600, no_resize=True, no_collapse=True, no_close=True):
                dpg.add_text("Please enter your Discord token")
                token_input = dpg.add_input_text(label="Token", default_value="", password=True)
                dpg.add_separator()
                account = dpg.add_text("Check the account after entering the token")
                dpg.add_separator()
                with dpg.group(horizontal=True, label="group_buttons"):
                    dpg.add_button(label="Check", callback=get_token_user)
                    dpg.add_button(label="Login", callback=get_token_value)
        else:
            token = files.json("data/discord.luna", "token", documents=False)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Content-Type': 'application/json',
                'authorization': Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token)
            }
            r = requests.get(
                f"https://discordapp.com/api/{api_version}/users/@me",
                headers=headers
            ).json()
            print(
                f"Logging into {color.print_gradient(r['username'])}#{color.print_gradient(r['discriminator'])}..."
            )
            dpg.set_value(logged, f"Logging into {r['username']}#{r['discriminator']}...")
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


def file_check(self):
    """Run a check for the files, create if needed."""
    # if self:
    #     _extracted_from_file_check_4()
    # ///////////////////////////////////////////////////////////////
    # Folder Creation

    if not files.file_exist("data/console", documents=False):
        files.create_folder("data/console", documents=False)

    if not files.file_exist("data/themes", documents=False):
        files.create_folder("data/themes", documents=False)

    if not files.file_exist("data/snipers", documents=False):
        files.create_folder("data/snipers", documents=False)

    if not files.file_exist("data/scripts", documents=False):
        files.create_folder("data/scripts", documents=False)

    if not files.file_exist("data/webhooks", documents=False):
        files.create_folder("data/webhooks", documents=False)

    if not files.file_exist("data/notifications", documents=False):
        files.create_folder("data/notifications", documents=False)

    if not files.file_exist("data/backup", documents=False):
        files.create_folder("data/backup", documents=False)

    if not files.file_exist("data/backup/guilds", documents=False):
        files.create_folder("data/backup/guilds", documents=False)

    if not files.file_exist("data/resources", documents=False):
        files.create_folder("data/resources", documents=False)

    if not files.file_exist("data/raiding", documents=False):
        files.create_folder("data/raiding", documents=False)

    if not files.file_exist("data/raiding/proxies", documents=False):
        files.create_folder("data/raiding/proxies", documents=False)

    if not files.file_exist("data/notes", documents=False):
        files.create_folder("data/notes", documents=False)

    if not files.file_exist("data/emojis", documents=False):
        files.create_folder("data/emojis", documents=False)

    if not files.file_exist("data/privnote", documents=False):
        files.create_folder("data/privnote", documents=False)

    if not files.file_exist("data/protections", documents=False):
        files.create_folder("data/protections", documents=False)

    if not files.file_exist("data/dumping", documents=False):
        files.create_folder("data/dumping", documents=False)

    if not files.file_exist("data/dumping/images", documents=False):
        files.create_folder("data/dumping/images", documents=False)

    if not files.file_exist("data/dumping/emojis", documents=False):
        files.create_folder("data/dumping/emojis", documents=False)

    if not files.file_exist("data/dumping/urls", documents=False):
        files.create_folder("data/dumping/urls", documents=False)

    if not files.file_exist("data/dumping/audio", documents=False):
        files.create_folder("data/dumping/audio", documents=False)

    if not files.file_exist("data/dumping/videos", documents=False):
        files.create_folder("data/dumping/videos", documents=False)

    if not files.file_exist("data/dumping/messages", documents=False):
        files.create_folder("data/dumping/messages", documents=False)

    if not files.file_exist("data/dumping/channels", documents=False):
        files.create_folder("data/dumping/channels", documents=False)

    if not files.file_exist("data/dumping/avatars", documents=False):
        files.create_folder("data/dumping/avatars", documents=False)

    # ///////////////////////////////////////////////////////////////
    # Python Files

    if not files.file_exist("data/scripts/example.py", documents=False):
        content = """# Its as simple as writing commands for cogs! (Note: You need to use \"self\")
# Documentation for custom commands can be found here: https://www.team-luna.org/documentation

@commands.command(
    name="example",
    usage="<text>",
    description="Example of a custom command"
)
async def example(self, luna, *, text):
    await luna.send(f"```{text}```")
"""
        files.write_file("data/scripts/example.py", content, documents=False)

    # ///////////////////////////////////////////////////////////////
    # Protection Files

    if not files.file_exist(
            "data/protections/config.json",
            documents=False
    ):
        data = {
            "footer": True,
            "guilds": []
        }
        files.write_json(
            "data/protections/config.json",
            data, documents=False
        )

    if not files.file_exist(
            "data/protections/invite.json",
            documents=False
    ):
        data = {
            "delete": True,
            "action": "warn"
        }
        files.write_json(
            "data/protections/invite.json",
            data, documents=False
        )

    # ///////////////////////////////////////////////////////////////
    # Json Files

    if not files.file_exist("data/rpc.json", documents=False):
        data = {
            "rich_presence": "on",
            "client_id": "911815236825268234",
            "details": "Luna",
            "state": "",
            "large_image": "lunarpc",
            "large_text": "",
            "small_image": "",
            "small_text": "",
            "button_1_text": "Luna Public",
            "button_1_url": "https://discord.gg/Kxyv7NHVED",
            "button_2_text": "",
            "button_2_url": "",
        }
        files.write_json("data/rpc.json", data, documents=False)

    if not files.file_exist("data/config.json", documents=False):
        data = {
            "prefix": ".",
            "stream_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "afk_message": "I am not here right now, DM me later.",
            "delete_timer": "30",
            "mode": "1",
            "error_log": "message",
            "risk_mode": "off",
            "theme": "default",
            "startup_status": "online"
        }
        files.write_json("data/config.json", data, documents=False)

    if not files.file_exist("data/discord.luna", documents=False):
        data = {
            "token": "token-here",
            "password": "password-here"
        }
        files.write_json("data/discord.luna", data, documents=False)

    if not files.file_exist("data/console/console.json", documents=False):
        data = {
            "logo": "luna",
            "logo_gradient": "1",
            "center": True,
            "print_gradient": "1",
            "spacers": True,
            "spacer": "|",
            "timestamp": True,
            "mode": "1"
        }
        files.write_json("data/console/console.json", data, documents=False)

    if not files.file_exist("data/snipers/nitro.json", documents=False):
        data = {
            "sniper": "on",
            "charge": "off"
        }
        files.write_json("data/snipers/nitro.json", data, documents=False)

    if not files.file_exist("data/snipers/privnote.json", documents=False):
        data = {
            "sniper": "on"
        }
        files.write_json(
            "data/snipers/privnote.json",
            data, documents=False
        )

    if not files.file_exist("data/snipers/selfbot.json", documents=False):
        data = {
            "sniper": "on"
        }
        files.write_json("data/snipers/selfbot.json", data, documents=False)

    if not files.file_exist("data/snipers/giveaway.json", documents=False):
        data = {
            "joiner": "on",
            "delay_in_minutes": "1",
            "blocked_words": [
                "ban",
                "kick",
                "selfbot",
                "self bot",
                "test",
                "check"],
            "guild_joiner": "on"
        }
        files.write_json(
            "data/snipers/giveaway.json",
            data, documents=False
        )

    if not files.file_exist(
            "data/snipers/giveaway_bots.json",
            documents=False
    ):
        data = {
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
            "897642275868393493": "🎉",
            "574812330760863744": "🎁",
            "732003715426287676": "🎁"
        }
        files.write_json(
            "data/snipers/giveaway_bots.json",
            data, documents=False
        )

    if not files.file_exist("data/resources/luna.ico", documents=False):
        r = requests.get(
            "https://cdn.discordapp.com/attachments/927033067468623882/983136712093990952/luna.ico",
            stream=True
        )
        open(
            'data/resources/luna.ico',
            'wb'
        ).write(
            r.content
        )

    if not files.file_exist("data/resources/luna.png", documents=False):
        r = requests.get(
            "https://cdn.discordapp.com/attachments/927033067468623882/983136712328896522/luna.png?size=4096",
            stream=True
        )
        open(
            'data/resources/luna.png',
            'wb'
        ).write(
            r.content
        )

    if not files.file_exist("data/resources/luna_ascii.png", documents=False):
        r = requests.get(
            "https://cdn.discordapp.com/attachments/927033067468623882/983136712681209876/luna_ascii.png?size=4096",
            stream=True
        )
        open(
            'data/resources/luna_ascii.png',
            'wb'
        ).write(
            r.content
        )

    if not files.file_exist("data/backup/friends.txt", documents=False):
        content = "Use [prefix]friendsbackup"
        files.write_file(
            "data/backup/friends.txt",
            content, documents=False
        )

    if not files.file_exist("data/invites.txt", documents=False):
        content = "Put the invites of the servers you want to join here one after another"
        files.write_file("data/invites.txt", content, documents=False)

    if not files.file_exist("data/backup/blocked.txt", documents=False):
        content = "Use [prefix]friendsbackup"
        files.write_file(
            "data/backup/blocked.txt",
            content, documents=False
        )

    if not files.file_exist(
            "data/notifications/toasts.json",
            documents=False
    ):
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
        files.write_json(
            "data/notifications/toasts.json",
            data, documents=False
        )

    if not files.file_exist("data/sharing.json", documents=False):
        data = {
            "share": "off",
            "user_id": ""
        }
        files.write_json("data/sharing.json", data, documents=False)

    if not files.file_exist(
            "data/notifications/console.json",
            documents=False
    ):
        data = {
            "pings": "on"
        }
        files.write_json(
            "data/notifications/console.json",
            data, documents=False
        )

    if not files.file_exist(
            "data/notifications/toast.json",
            documents=False
    ):
        data = {
            "icon": "luna.ico",
            "title": "Luna"
        }
        files.write_json(
            "data/notifications/toast.json",
            data, documents=False
        )

    if not files.file_exist("data/raiding/tokens.txt", documents=False):
        content = "Put your tokens here line after line"
        files.write_file(
            "data/raiding/tokens.txt",
            content, documents=False
        )

    if not files.file_exist("data/raiding/proxies.txt", documents=False):
        content = "Put your proxies here line after line. (HTTP Only)"
        files.write_file(
            "data/raiding/proxies.txt",
            content, documents=False
        )

    if not files.file_exist("data/webhooks/webhook.json", documents=False):
        data = {
            "title": "Luna",
            "footer": "Luna",
            "image_url": "https://cdn.discordapp.com/attachments/927033067468623882/983136712328896522/luna.png?size=4096",
            "hex_color": "#898eff"
        }
        files.write_json(
            "data/webhooks/webhook.json",
            data, documents=False
        )

    if not files.file_exist("data/webhooks/url.json", documents=False):
        data = {
            "login": "webhook-url-here",
            "nitro": "webhook-url-here",
            "giveaway": "webhook-url-here",
            "privnote": "webhook-url-here",
            "selfbot": "webhook-url-here",
            "pings": "webhook-url-here",
            "ghostpings": "webhook-url-here",
            "friendevents": "webhook-url-here",
            "guildevents": "webhook-url-here",
            "roleupdates": "webhook-url-here",
            "nickupdates": "webhook-url-here",
            "protection": "webhook-url-here"
        }
        files.write_json("data/webhooks/url.json", data, documents=False)

    if not files.file_exist("data/webhooks/webhooks.json", documents=False):
        data = {
            "webhooks": "on",
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
        files.write_json(
            "data/webhooks/webhooks.json",
            data, documents=False
        )


file_check(False)


@bot.event
async def on_ready():
    print(f"Logged into {color.print_gradient(bot.user)}")
    dpg.set_value(logged, f"Logged into {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


privacy_mode = False


@bot.command()
async def privacy(ctx):
    await ctx.message.delete()
    global privacy_mode
    if privacy_mode:
        dpg.set_value(logged, f"Logged into {bot.user}")
        privacy_mode = False
        await ctx.send("Privacy mode disabled.")
    else:
        dpg.set_value(logged, "Logged into Luna#0000")
        privacy_mode = True
        await ctx.send("Privacy mode enabled.")


command_count = len(bot.commands)

dpg.create_context()
dpg.create_viewport(
    title='Luna', width=800, height=600, resizable=False, decorated=True, clear_color=(40, 40, 40, 255), small_icon="data/resources/luna.ico", large_icon="data/resources/luna.ico"
)
with dpg.font_registry():
    default_font = dpg.add_font("C:/Windows/Fonts/arial.ttf", 13)

dpg.bind_font(default_font)

with dpg.window(tag="Primary Window", width=200, height=562, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, no_bring_to_front_on_focus=True):
    width, height, channels, data = dpg.load_image("data/resources/luna.png")

    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    dpg.add_image(texture_id, width=75, height=75, pos=(58, 28))
    dpg.add_spacer(height=80)
    dpg.add_separator()
    dpg.add_text(f"Welcome back, {os.getlogin()}")
    dpg.add_text("Beta Build V1 (Paid)")
    dpg.add_separator()
    dpg.add_text(f"{command_count} Commands")
    dpg.add_text("1 Custom Command Loaded")
    dpg.add_separator()

    with dpg.menu_bar():
        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Style Editor", callback=lambda: dpg.show_tool(dpg.mvTool_Style))
            dpg.add_menu_item(label="Font Manager", callback=lambda: dpg.show_tool(dpg.mvTool_Font))
            dpg.add_menu_item(label="Metrics", callback=lambda: dpg.show_tool(dpg.mvTool_Metrics))
            dpg.add_menu_item(label="Debug", callback=lambda: dpg.show_tool(dpg.mvTool_Debug))

with dpg.window(tag="Secondary Window", width=586, height=562, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(199, 0), no_bring_to_front_on_focus=True):
    logged = dpg.add_text("Idle")
    dpg.add_separator()

    width, height, channels, data = dpg.load_image("data/resources/luna_ascii.png")

    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    dpg.add_image(texture_id, width=570, height=119, pos=(0, 37))
    dpg.add_spacer(height=122)
    dpg.add_separator()
    dpg.add_text(motd)
    dpg.add_text("Last used command")
    dpg.add_separator()

    with dpg.window(label="Sniper Settings", width=260, height=320, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(220, 224)):
        dpg.add_checkbox(label="Nitro Sniper", default_value=True)
        dpg.add_checkbox(label="Giveaway Sniper", default_value=True)
        dpg.add_checkbox(label="Privnote Sniper", default_value=True)
        dpg.add_separator()
        dpg.add_text("Nitro Sniper")
        dpg.add_checkbox(label="Charge Status", default_value=False)
        dpg.add_separator()
        dpg.add_text("Giveaway Sniper")
        dpg.add_slider_int(label="Minutes", default_value=1, min_value=1, max_value=10)
        dpg.add_checkbox(label="Server Joiner", default_value=True)

    themes = ["Default", "Dark"]


    def print_theme(sender, app_data, user_data):
        print(app_data)
        dpg.set_value(selected_theme, f"Active Theme: {app_data}")


    with dpg.window(label="Theme Settings", width=260, height=320, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(500, 224)):
        selected_theme = dpg.add_text("Active Theme: " + themes[0])
        dpg.add_separator()
        dpg.add_text("Available Themes")
        dpg.add_combo(label="Themes", items=themes, callback=print_theme, default_value=themes[0])
        dpg.add_separator()
        dpg.add_text("Theme Editor")
        dpg.add_input_text(label="Theme Name", default_value="Luna")
        dpg.add_input_text(label="Title", default_value="Luna")
        dpg.add_input_text(label="Footer", default_value="www.team-luna.org")
        dpg.add_button(label="Save")

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 6, category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_TabActive, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_Button, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (80, 100, 150, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (50, 50, 50, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, (80, 100, 150, 255), category=dpg.mvThemeCat_Core)

        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)

debugger_thread = threading.Thread(target=login)
debugger_thread.daemon = True
debugger_thread.start()

dpg.bind_theme(global_theme)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
