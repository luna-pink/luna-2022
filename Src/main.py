
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
import psutil
import typing
import aiohttp
import asyncio
import discord
import hashlib
import pwinput
import requests
import threading
import playsound
import pyPrivnote
import ctypes.wintypes as wintypes

from CEA256 import *
from gtts import gTTS
from os import system
from discord import *
from ctypes import windll
from notifypy import Notify
from datetime import datetime
from discord.ext import commands
from AuthGG.client import Client as luna_gg
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, has_permissions

# ///////////////////////////////////////////////////////////////
# Window Size & Scroller

system("mode con: cols=102 lines=35")
STDOUT = -11
hdl = windll.kernel32.GetStdHandle(STDOUT)
bufsize = wintypes._COORD(102, 9001)
windll.kernel32.SetConsoleScreenBufferSize(hdl, bufsize)

# ///////////////////////////////////////////////////////////////
# ANSI Colors & Gradients

class color:
    error = '\033[38;2;225;9;89m'
    reset = "\033[0m"

    def logo_gradient(text):
        """Gradient for the logo"""
        gradient = files.json("data/console/console.json", "logo_gradient")
        match gradient:
            case "1":
                return color.purple_blue(f"""{text}""")
            case "2":
                return color.purple_cyan(f"""{text}""")
            case "3":
                return color.pink_red(f"""{text}""")
            case "4":
                return color.blue_cyan(f"""{text}""")
            case "5":
                return color.green_blue(f"""{text}""")
            case "6":
                return color.orange_red(f"""{text}""")
            case "7":
                return color.black_white(f"""{text}""")
        if int(gradient) > 7:
            return color.purple_blue(f"""{text}""")

    def print_gradient(text):
        """Gradient for the console"""
        gradient = files.json("data/console/console.json", "print_gradient")
        match gradient:
            case "1":
                return color.purple(f"{text}")
            case "2":
                return color.blue(f"{text}")
            case "3":
                return color.green(f"{text}")
            case "4":
                return color.yellow(f"{text}")
            case "5":
                return color.red(f"{text}")
            case "6":
                return color.black(f"{text}")
        if int(gradient) > 6:
            return color.purple(f"{text}")
    
    def black(text):
        system(""); faded = ""
        for line in text.splitlines():
            red = 0; green = 0; blue = 0
            for character in line:
                red += 20; green += 20; blue += 20
                if red > 255 and green > 255 and blue > 255:
                    red = 255; green = 255; blue = 255
                faded += (f"\033[38;2;{red};{green};{blue}m{character}\033[0m")
        return faded

    def green(text):
        system(""); faded = ""
        for line in text.splitlines():
            blue = 100
            for character in line:
                blue += 20
                if blue > 255:
                    blue = 255
                faded += (f"\033[38;2;0;255;{blue}m{character}\033[0m")
        return faded

    def blue(text):
        system(""); faded = ""
        for line in text.splitlines():
            green = 0
            for character in line:
                green += 20
                if green > 255:
                    green = 255
                faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
        return faded

    def purple(text):
        system(""); faded = ""
        for line in text.splitlines():
            red = 35
            for character in line:
                red += 20
                if red > 255:
                    red = 255
                faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
        return faded

    def yellow(text):
        system(""); faded = ""
        for line in text.splitlines():
            red = 0
            for character in line:
                if not red > 200:
                    red += 20
                faded += (f"\033[38;2;{red};255;0m{character}\033[0m")
        return faded

    def red(text):
        system(""); faded = ""
        for line in text.splitlines():
            green = 250
            for character in line:
                green -= 20
                if green < 0:
                    green = 0
                faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
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

    def purple_blue(text):
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

    def purple_cyan(text):
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

    def pink_red(text):
        system(""); faded = ""
        blue = 255
        for line in text.splitlines():
            faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m\n")
            if not blue == 0:
                blue -= 20
                if blue < 0:
                    blue = 0
        return faded

    def black_white(text):
        system(""); faded = ""
        red = 0; green = 0; blue = 0
        for line in text.splitlines():
            faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
            if not red == 255 and not green == 255 and not blue == 255:
                red += 20; green += 20; blue += 20
                if red > 255 and green > 255 and blue > 255:
                    red = 255; green = 255; blue = 255
        return faded

    def blue_cyan(text):
        system(""); faded = ""
        green = 10
        for line in text.splitlines():
            faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
            if not green == 255:
                green += 15
                if green > 255:
                    green = 255
        return faded

    def green_blue(text):
        system(""); faded = ""
        blue = 100
        for line in text.splitlines():
            faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
            if not blue == 255:
                blue += 15
                if blue > 255:
                    blue = 255
        return faded

    def orange_red(text):
        system(""); faded = ""
        green = 250
        for line in text.splitlines():
            faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
            if not green == 0:
                green -= 25
                if green < 0:
                    green = 0
        return faded

# ///////////////////////////////////////////////////////////////
# File Functions

class files:
    def file_exist(file_name):
        """Checks if a file exists"""
        return os.path.exists(file_name)
    def write_file(path, content):
        """Writes a file"""
        with open(path, 'w') as f:
            f.write(content)
    def write_json(path, content):
        """Writes a json file"""
        with open(path, "w") as f:
            f.write(json.dumps(content, indent=4))
    def read_file(path):
        """Reads a file"""
        with open(path, 'r', encoding="utf-8") as f:
            return f.read()
    def append_file(path, content):
        """Appends to a file"""
        with open(path, 'a') as f:
            f.write(content)
    def delete_file(path):
        """Deletes a file"""
        os.remove(path)
    def create_folder(path):
        """Creates a folder"""
        if not os.path.exists(path):
            os.makedirs(path)
    def json(file_name, value):
        """Reads a json file"""
        return json.load(open(file_name, encoding="utf-8"))[value]

class path:
    def console():
        return "data/console/"
    def data():
        return "data/"
    def theme():
        return "data/theme/"

def get_prefix():
    """
    Gets the prefix from the config file.
    """
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config["prefix"]

def get_token():
    """Gets the token from the config.json file"""
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config["token"]

def is_running(process_name):
    """Check if a process is running"""
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def check_debuggers():
    """Checks if any debuggers are running."""
    while True:
        if is_running("HTTPDebuggerUI.exe") or is_running("HTTPDebuggerSvc.exe"):
            sys.exit()

# ///////////////////////////////////////////////////////////////
# Print Functions

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

def clear():
    os.system("cls")

def restart_program():
	python = sys.executable
	os.execl(python, python, *sys.argv)

# ///////////////////////////////////////////////////////////////
# File Check

class luna:
    version = '2.1.1'
    updater_url = urllib.request.urlopen('https://pastebin.com/raw/mt9DERP6').read().decode('utf-8')
    motd = urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ').read().decode('utf-8')
    version_url = urllib.request.urlopen('https://pastebin.com/raw/iQPkzEpg').read().decode('utf-8').replace('\'', '')
    auth = luna_gg(api_key="485477744381137547167158333254493", aid="940932", application_secret="1fZDchzE3iZyiq0Ir5nAaFZ0p1c00zkqLc5")

    def authentication():
        """
        The main Luna authentication function
        """
        luna.console(clear=True)
        if files.file_exist('Updater.exe'):
            os.remove('Updater.exe')
        if not luna.version == luna.version_url:
            luna.update()
        else:
            if files.file_exist('data/authentication/login.json'):
                luna.login(exists=True)
            else:
                prints.message("1 = Log into an existing Luna account")
                prints.message("2 = Register a new Luna account")
                prints.message("If you forgot your password, open a ticket\n")
                print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
                choice = prints.input("Choice")
                if choice == "1":
                    luna.login()
                elif choice == "2":
                    luna.register()
                else:
                    prints.error("That choice does not exist!")
                    time.sleep(5)
                    restart_program()

    def login(exists=False):
        """
        The authentication login function
        """
        if exists:
            try:
                username = files.json("data/authentication/login.json", "username")
                password = files.json("data/authentication/login.json", "password")
                username = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
                password = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
            except:
                os.remove('data/authentication/login.json')
                prints.error("There has been an issue with your login.")
                time.sleep(5)
                prints.event("Redirecting to the main menu in 5 seconds")
                time.sleep(5)
                luna.authentication()
            try:
                prints.event("Logging in...")
                luna.auth.login(username, password)
            except Exception as e:
                prints.error(e)
                time.sleep(5)
                prints.event("Redirecting to the main menu in 5 seconds")
                time.sleep(5)
                luna.authentication()
        else:
            files.create_folder("data")
            files.create_folder("data/authentication")
            username = prints.input("Username")
            password = prints.password("Password")
            try:
                prints.event("Logging in...")
                luna.auth.login(username=username, password=password)
                username = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
                password = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
                data = {
                    "username": f"{username}",
                    "password": f"{password}"
                }
                files.write_json("data/authentication/login.json", data)
            except Exception as e:
                prints.error(e)
                time.sleep(5)
                prints.event("Redirecting to the main menu in 5 seconds")
                time.sleep(5)
                luna.authentication()

    def register():
        """
        The authentication register function
        """
        username = prints.input("Username")
        password = prints.password("Password")
        key = prints.input("Key")
        try:
            prints.event("Registering...")
            luna.auth.register(email=key, username=username, password=password, license_key=key)
            prints.message("Successfully registered")
            time.sleep(3)
            username = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
            password = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
            files.create_folder("data")
            files.create_folder("data/authentication")
            data = {
                "username": f"{username}",
                "password": f"{password}"
            }
            files.write_json("data/authentication/login.json", data)
            luna.login()
        except Exception as e:
            prints.error(e)
            time.sleep(5)
            prints.event("Redirecting to the main menu in 5 seconds")
            time.sleep(5)
            luna.authentication()

    def update():
        """
        The updater function
        """
        luna.console(clear=True)
        prints.event("Downloading Luna...")
        from clint.textui import progress
        r = requests.get(luna.updater_url, stream=True)
        with open('Updater.exe', 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
        time.sleep(5)
        prints.event("Starting Updater.exe...")
        os.startfile('Updater.exe')
        exit()

    def console(menu = False, clear = False):
        """
        Print the console design of Luna.\n
        `menu = True` if you want to print the informations (e.g. User: Luna#0000 etc...).\n
        `clear = True` if you want to clear (`cls`) the console on print.
        """
        if clear:
            os.system("cls")
        try:
            logo_variable = files.json("data/console/console.json", "logo")
            if logo_variable == "luna" or logo_variable == "luna.txt":
                logo_variable = logo
            else:
                ending = ".txt"
                if ".txt" in logo_variable:
                    ending = ""
                if not files.file_exist(f"data/console/{logo_variable}{ending}"):
                    logo_variable = logo
                if files.json("data/console/console.json", "center") == True:
                    logo_text = ""
                    for line in files.read_file(f"data/console/{logo_variable}{ending}").splitlines():
                        logo_text += line.center(os.get_terminal_size().columns) + "\n"
                        logo_variable = logo_text
                else:
                    logo_variable = files.read_file(f"data/console/{logo_variable}{ending}")
        except:
            luna.file_check()
        print(color.logo_gradient(f"""{logo_variable}"""))

    def title(text):
        ctypes.windll.kernel32.SetConsoleTitleW(text)

# ///////////////////////////////////////////////////////////////
# File Check

    def file_check():
        """Run a check for the files, create if needed."""
        clear()
        if not files.file_exist("config.json"):
            data = {
                "token": "token-here",
                "password": "password-here",
                "prefix": ".",
                "streamurl": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "afkmessage": "I am not here right now, DM me later.",
                "deletetimer": "30",
                "mode": "1",
                "errorlog": "message",
                "riskmode": "on",
                "theme": "luna.json",
                "startup_status": "online"
            }
            files.write_json("config.json", data)

        if not files.file_exist("data/"):
            files.create_folder("data/")

        if not files.file_exist("data/console/"):
            files.create_folder("data/console/")

        if not files.file_exist("data/console/console.json"):
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
            files.write_json("data/console/console.json", data)

        luna.console()
        prints.event("Checking files...")

# ///////////////////////////////////////////////////////////////
# Print Functions
from time import localtime, strftime
class prints:
    try:
        if files.json("data/console/console.json", "spacers") == True:
            spacer_2 = " " + files.json("data/console/console.json", "spacer") + " "
        else:
            spacer_2 = " "
        if files.json("data/console/console.json", "spacers") == True and files.json("data/console/console.json", "timestamp") == True:
            spacer_1 = " " + files.json("data/console/console.json", "spacer") + " "
        elif files.json("data/console/console.json", "spacers") == True and files.json("data/console/console.json", "timestamp") == False:
            spacer_1 = ""
        else:
            spacer_1 = " "
    except:
        luna.file_check()
    def command(text:str):
        """Prints a command log."""
        if files.json("data/console/console.json", "timestamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Command")}{prints.spacer_2}{get_prefix()}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Command")}{prints.spacer_2}{get_prefix()}{text}')
    def shared(text:str):
        """Prints a shared log."""
        if files.json("data/console/console.json", "timestamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Sharing")}{prints.spacer_2}{get_prefix()}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Sharing")}{prints.spacer_2}{get_prefix()}{text}')
    def message(text:str):
        """Prints a message log."""
        if files.json("data/console/console.json", "timestamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Message")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Message")}{prints.spacer_2}{text}')
    def sniper(text:str):
        """Prints a sniper log."""
        if files.json("data/console/console.json", "timestamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Sniper ")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Sniper ")}{prints.spacer_2}{text}')
    def input(text:str):
        """Prints a input log."""
        if files.json("data/console/console.json", "timestamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}')
    def event(text:str):
        """Prints a event log."""
        if files.json("data/console/console.json", "timestamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient(" Event ")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient(" Event ")}{prints.spacer_2}{text}')
    def selfbot(text:str):
        """Prints a selfbot log."""
        if files.json("data/console/console.json", "timestamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Selfbot")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Selfbot")}{prints.spacer_2}{text}')
    def error(text:str):
        """Prints a error log."""
        if files.json("data/console/console.json", "timestamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.error} Error {color.reset}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.error} Error {color.reset}{prints.spacer_2}{text}')
    def input(text:str):
        """Prints a input input."""
        if files.json("data/console/console.json", "timestamp") == True:
            var = input(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ')
        else:
            var = input(f'{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ')
        return var
    def password(text:str):
        """Prints a password input. Masked with `*`"""
        if files.json("data/console/console.json", "timestamp") == True:
            password = pwinput.pwinput(prompt=f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ', mask='*')
        else:
            password = pwinput.pwinput(prompt=f'{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ', mask='*')
        return password

# ///////////////////////////////////////////////////////////////
# Token Grabber

def check_token(token):
    """
    Check the given token.\n
    Returns `True` if the token is valid.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v9/users/@me/library"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return token
    else:
        return False

def find_token():
    """
    Search for tokens on the system.\n
    Checks the token if any are found and prompts the user.
    """
    tokens = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {'Discord': roaming + '\\Discord', 'Discord Canary': roaming + '\\DiscordCanary', 'Discord PTB': roaming + '\\discordptb', 'Discord PTB Canary': roaming + '\\discordptbcanary', 'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default', 'Opera': local + '\\Opera Software\\Opera Stable'}
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        path += '\\Local Storage\\leveldb\\'
        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue
            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        if not token in tokens:
                            tokens.append(token)
    prints.message(f"Detected a token")
    prints.event("Running a check on the token...")
    if not check_token(tokens[0]) == False:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v9/users/@me"
        r = requests.get(url, headers=headers).json()
        prints.message(f"Detected a valid token | {r['username']}#{r['discriminator']}")
        json_object = json.load(open("config.json", encoding="utf-8"))
        json_object["token"] = str(tokens[0])
        files.write_json("config.json", json_object)
        return True
    else:
        prints.error("Invalid token (auto grab). Please manually enter a valid token.")
        return False

# ///////////////////////////////////////////////////////////////
# Main Thread

luna.title("Luna")
luna.file_check()
luna.authentication()