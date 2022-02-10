from asyncio.windows_events import NULL
from http.client import RESET_CONTENT
from sqlite3.dbapi2 import Timestamp, connect
import sys
import asyncio
import aiohttp
from discord.ext import commands, tasks
import re
from win10toast import ToastNotifier
import asyncio, threading
import json
from aiohttp.helpers import TimeoutHandle
from colorama import init
from requests.utils import CaseInsensitiveDict
from itertools import cycle
from discord import embeds, guild, message, user
from discord.enums import Theme
from colour import Color
from discord.ext import commands
import datetime
from selenium import webdriver
import time
from os import system
from random import choices, randint
from discord.ext import commands
from gtts import gTTS
import codecs, datetime, io, random, numpy, datetime
import re
import httpx
from colorama import Fore, init
import platform
import json
import time
import traceback
from discord.ext import tasks
from os import system
from random import randint
from discord.ext import commands
import re
import httpx
from colorama import Fore, init
import platform
import sys
import traceback
import youtube_dl
import platform
import subprocess
import re
import shutil
import random
import asyncio
import json
import psutil
import time
import traceback
import sys
import urllib
import requests
import discord
import ctypes
from pypresence import Presence, presence
from discord.embeds import Embed
import requests, wmi
import asyncio
import random
from colorama import init
from discord.ext import commands
init()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from AuthGG.client import Client
from AuthGG.admin import AdminClient
from AuthGG.logging import Logging
from PIL import Image
import time
from colorama import Fore
from hashlib import sha512
import json, hmac, math, zlib
import colorsys
import sys
import os
#config = json.load(open('config.json', 'rb'))
#login = json.load(open('login.json', 'rb'))


########### >> Defining
os.system("color")

########### >> Variables


########### >> Classes
class Colours:
    White = "\x1b[38;2;250;250;250m"
    Magenta = "\x1b[38;2;255;94;255m"

def new_splash():
    print(f"""                                           {Colours.White}Welcome to Cotra Selfbot
  {Colours.Magenta}╔════════════════════════╗    ╔══════════════════════════════════════════════╗    ╔════════════════════════╗              
 {Colours.Magenta}╔╝         {Colours.White}Rules          {Colours.Magenta}╚╗  ╔╝                                              ╚╗  ╔╝        {Colours.White}Profile         {Colours.Magenta}╚╗             
                            {Colours.Magenta}║  ║    ██████{Colours.White}{Colours.White}╗ {Colours.Magenta}██████{Colours.White}{Colours.White}╗ {Colours.Magenta}████████{Colours.White}{Colours.White}╗{Colours.Magenta}██████{Colours.White}{Colours.White}╗  {Colours.Magenta}█████{Colours.White}{Colours.White}╗    {Colours.Magenta}║  ║                                     
        {Colours.White}No exe {Colours.Magenta}Sharing      {Colours.Magenta}║  ║   ██{Colours.White}╔════╝{Colours.Magenta}██{Colours.White}╔═══{Colours.Magenta}██{Colours.White}╗╚══{Colours.Magenta}██{Colours.White}╔══╝{Colours.Magenta}██{Colours.White}╔══{Colours.Magenta}██{Colours.White}╗{Colours.Magenta}██{Colours.White}╔══{Colours.Magenta}██{Colours.White}╗   {Colours.Magenta}║  ║   Username: {Colours.White}{str(bot.user)}                                 
     {Colours.White}No {Colours.Magenta}tampering {Colours.White}allowed   {Colours.Magenta}╚══╝   {Colours.Magenta}██{Colours.White}║     {Colours.Magenta}██{Colours.White}║   {Colours.Magenta}██{Colours.White}║   {Colours.Magenta}██{Colours.White}║   {Colours.Magenta}██████{Colours.White}╔╝{Colours.Magenta}███████{Colours.White}║   {Colours.Magenta}╚══╝   Friends: {Colours.White}{len(bot.user.friends)}                                   
      {Colours.White}No {Colours.Magenta}account {Colours.White}sharing    {Colours.Magenta}{Colours.Magenta}╔══╗   {Colours.Magenta}{Colours.Magenta}██{Colours.White}║     {Colours.Magenta}{Colours.Magenta}██{Colours.White}║   {Colours.Magenta}{Colours.Magenta}██{Colours.White}║   {Colours.Magenta}{Colours.Magenta}██{Colours.White}║   {Colours.Magenta}{Colours.Magenta}██{Colours.White}╔══{Colours.Magenta}{Colours.Magenta}██{Colours.White}╗{Colours.Magenta}{Colours.Magenta}██{Colours.White}╔══{Colours.Magenta}{Colours.Magenta}██{Colours.White}║   {Colours.Magenta}{Colours.Magenta}╔══╗   Guilds: {Colours.White}{len(bot.guilds)}                                     
                            {Colours.Magenta}║  ║   ╚{Colours.Magenta}██████{Colours.White}╗╚{Colours.Magenta}██████{Colours.White}╔╝   {Colours.Magenta}██{Colours.White}║   {Colours.Magenta}██{Colours.White}║  {Colours.Magenta}██{Colours.White}║{Colours.Magenta}██{Colours.White}║  {Colours.Magenta}██{Colours.White}║   {Colours.Magenta}║  ║   Prefix: {Colours.White}{config['prefix']}                                  
    {Colours.Magenta}discord.gg/{Colours.White}j8VV2RzKs3   {Colours.Magenta}║  ║    {Colours.White}╚═════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   {Colours.Magenta}║  ║                                     
 {Colours.Magenta}╚╗                        ╔╝  ╚╗                                              ╔╝  ╚╗                        ╔╝             
  {Colours.Magenta}╚════════════════════════╝    ╚═════════════════════╗ ╔══════════════════════╝    ╚════════════════════════╝                         
                                                      {Colours.Magenta}║ ║  
                         {Colours.Magenta}╔════════════════════════════╝ ╚════════════════════════════╗
                        {Colours.Magenta}╔╝                          {Colours.White}Selfbot                          {Colours.Magenta}╚╗
                                                 
                                {Colours.Magenta}Nitro Sniper: {Colours.White}True           {Colours.Magenta}Giveaway Joiner: {Colours.White}True
                                {Colours.Magenta}Commands: {Colours.White}{len(bot.commands)}                {Colours.Magenta}Delete Timer: {Colours.White}{config['deletetime']} 
                                {Colours.Magenta}Theme: {Colours.White}{config['theme']['name']}               {Colours.Magenta}Version: {Colours.White}{version}
                        {Colours.Magenta}╚╗                                                           ╔╝
                        {Colours.Magenta} ╚═══════════════════════════════════════════════════════════╝
""")
def ResetUserHWID():
    try:
        AdminClientKey = AdminClient("WDSMDRHYVFHD") # Stupid motherfucker
        usernameHWID = input("USERNAME: ")
        AdminClientKey.resetHWID(username=usernameHWID)
    except Exception as HWIDErr:
        print(HWIDErr)

client_auth = Client(api_key="54282951781642493394158259185792966598253178428264228845", aid="71812", application_secret="sN2co4zW5Uoc97EYO0KpX6A4Sa3uWfQcJQd") #ty
clear = lambda: os.system('cls')
def auth():
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    domain = ''

    if domain == '':
        domains = ['outlook.com', 'gmail.com', 'yandex.com', 'yahoo.com', 'pm.me', 'protonmail.com', 'coolmail.com', 'mail.com', 'sexymail.com', 'email.com', 'mymail.com', 'thisismyemail.com', 'freshmail.com', 'coolmail.com', 'easymail.com', 'freemail.com']

    first = ''.join((random.choice(chars) for i in range (4)))
    second = ''.join((random.choice(chars) for i in range (4)))
    third = ''.join((random.choice(chars) for i in range (4)))
    result1 = first + second + third + '@' + random.choice(domains)

    clear()
    def login(username, password):
        try:
            client_auth.login(username, password)
            with open('login.json', 'r') as f:
                configs = json.load(f)
            configs['username'] = username
            configs['password'] = password
            with open('login.json', 'w') as f:
                json.dump(configs, f, indent=4)
        except Exception as e:
            print(e)
            input("Press Enter to continue...")
            return auth()
    def register(email, license_key, username, password):
        try:
            client_auth.register(email=email, username=username, password=password, license_key=license_key)
            print("Successfully Registered\nNow Logging In")
            login(username, password)
        except Exception as e:
            print(e)
            input("Press Enter to continue...")
            return auth()
            
    with open('login.json') as f:
        t = json.load(f)
        username = t['username']
        password = t['password']
    if username and password != "":
        
        login(username, password)
    else:
        print(f'''{Fore.MAGENTA} ██████╗ ██████╗ ████████╗██████╗  █████╗     ██╗   ██╗██╗'''.center(os.get_terminal_size().columns))
        print(f'''{Fore.MAGENTA}██╔════╝██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗    ██║   ██║██║'''.center(os.get_terminal_size().columns))
        print(f'''{Fore.MAGENTA}██║     ██║   ██║   ██║   ██████╔╝███████║    ██║   ██║██║'''.center(os.get_terminal_size().columns))
        print(f'''{Fore.MAGENTA}██║     ██║   ██║   ██║   ██╔══██╗██╔══██║    ██║   ██║██║'''.center(os.get_terminal_size().columns))
        print(f'''{Fore.MAGENTA}╚██████╗╚██████╔╝   ██║   ██║  ██║██║  ██║    ╚██████╔╝██║'''.center(os.get_terminal_size().columns))
        print(f'''{Fore.MAGENTA} ╚═════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝'''.center(os.get_terminal_size().columns))
        print(f'''{Fore.MAGENTA}1: LOGIN   |   2: REGISTER   |   3: HWID'''.center(os.get_terminal_size().columns))
        print(f'''{Fore.MAGENTA}╚═════════════════════════════════════════════════════════╝'''.center(os.get_terminal_size().columns))
        auth_choice = input(f'''                               CHOICE: ''')
        clear()
        if auth_choice == "1":
            username = input("CotraUI Username: ")
            password = input("CotraUI Password: ")
            login(username, password)
            input(f'{Fore.LIGHTBLUE_EX}PLEASE RESTART THE SELFBOT')
            time.sleep(9999)
        elif auth_choice == "2":
            email = result1
            license_key = input("License Key: ")
            username = input("CotraUI Username: ")
            password = input("CotraUI Password: ")
            register(email, license_key, username, password)
            python = sys.executable
            os.execl(python, python, * sys.argv)
        elif auth_choice == "3":
            ResetUserHWID()
        else:
            print("Invalid choice")
            auth()
auth()
prefix = config['prefix']
version = "4.5"
dev = "4.9"
cmds = "201"
bot = commands.Bot(command_prefix=prefix, self_bot=True)
toaster = ToastNotifier()
toaster.show_toast("Cotra Selfbot",
                   "Is now loading...",
                   icon_path="A.ico",
                   duration=10)

toaster.show_toast("Cotra Selfbot",
                   "Is now loaded. Please wait 5 seconds",
                   icon_path="A.ico",
                   duration=5,
                   threaded=True)
# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(0.1)
bot.remove_command('help')
def restart_bot(): 
  #os.execv(sys.executable, ['python'] + sys.argv)
  os.execv(sys.executable,sys.argv)

print(chr(27) + "[2J")

def Clear():
    os.system('cls')

def is_me(m):
    return m.author == bot.user

snipermode = 1
gsniper= 1

giveaway_ids =   ["294882584201003009","716967712844414996","796315281688494081","673918978178940951","396464677032427530"]

@bot.event
async def on_message(message):
    time = datetime.datetime.now().strftime("%H:%M")
    start = datetime.datetime.now()
    token = config.get('token')
    headers = {'Authorization': token}

    def GiveawayData():
        print(f"{Fore.CYAN}[blicky Sniper] Giveaway Bot Used: {message.author}" + Fore.RESET)
        print(f"{Fore.CYAN}[blicky Sniper] Server: {message.guild}" + Fore.RESET)
        print(f"{Fore.CYAN}[blicky Sniper] Channel: {message.channel}" + Fore.RESET)
        print(f"{Fore.CYAN}[blicky Sniper] Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}" + Fore.RESET)
    
    def GiveawayData2():
        print(f"{Fore.CYAN}[blicky Skipped] Giveaway Bot Used: {message.author}" + Fore.RESET)
        print(f"{Fore.CYAN}[blicky Skipped] Server: {message.guild}" + Fore.RESET)
        print(f"{Fore.CYAN}[blicky Skipped] Channel: {message.channel}" + Fore.RESET)
        print(f"{Fore.CYAN}[blicky Skipped] Reason: ITS SUS CUTIE I SAVED YOU" + Fore.RESET)
        print(f"{Fore.CYAN}[blicky Skipped] Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}" + Fore.RESET)

    def NitroData(delay, code):
        response = round(bot.latency * 1000)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Nitro Code sent by: {Fore.WHITE}{message.author}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Nitro Code: {Fore.WHITE}{code}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Server: {Fore.WHITE}{message.guild}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Channel: {Fore.WHITE}{message.channel}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Status: {Fore.LIGHTGREEN_EX}REAL" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Snipe Time: {Fore.WHITE}{delay}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}API Delay: {Fore.WHITE}{response}ms" + Fore.RESET)

    def NitroData2(delay, code):
        response = round(bot.latency * 1000)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Nitro Code sent by: {Fore.WHITE}{message.author}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Nitro Code: {Fore.WHITE}{code}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Server: {Fore.WHITE}{message.guild}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Channel: {Fore.WHITE}{message.channel}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Status: {Fore.LIGHTRED_EX}FAKE" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Snipe Time: {Fore.WHITE}{delay}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}API Delay: {Fore.WHITE}{response}ms" + Fore.RESET)

    def NitroData3(delay, code):
        response = round(bot.latency * 1000)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Nitro Code sent by: {Fore.WHITE}{message.author}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Nitro Code: {Fore.WHITE}{code}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Server: {Fore.WHITE}{message.guild}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Channel: {Fore.WHITE}{message.channel}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Status: {Fore.YELLOW}ALREADY REDEEMED" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}Snipe Time: {Fore.WHITE}{delay}" + Fore.RESET)
        print(f"{Fore.CYAN}[Sniper] {Fore.CYAN}API Delay: {Fore.WHITE}{response}ms" + Fore.RESET)

    if 'discord.gift/' in message.content:
        if snipermode == 1:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')
            r = requests.post(f'https://discord.com/api/v9/entitlements/gift-codes/{code}/redeem',headers=headers).text
            delay = datetime.datetime.now() - start
            delay = f'{delay.seconds}.{delay.microseconds}'
            if 'This gift has been redeemed already.' in r:
                print(""f"\n[{time}] - {Fore.LIGHTBLUE_EX}NITRO SNIPER"+ Fore.RESET)
                NitroData3(delay, code)

            elif 'subscription_plan' in r:
                print(""f"\n[{time}] - {Fore.LIGHTBLUE_EX}NITRO SNIPER"+ Fore.RESET)
                NitroData(delay, code)

            elif 'Unknown Gift Code' in r:
                print(""f"\n[{time}] - {Fore.LIGHTBLUE_EX}NITRO SNIPER"+ Fore.RESET)
                NitroData2(delay, code)
            else:
                return

    if 'GIVEAWAY' in message.content:
        if gsniper == 1:
            if str(message.author.id) in giveaway_ids:
                embed = message.embeds[0].to_dict()
                prize = embed["author"]["name"]
                if "ban" in prize.lower() or "kick" in prize.lower() or "mute" in prize.lower() or "punish" in prize.lower() or "lol" in prize.lower() or "test" in prize.lower() or "fake" in prize.lower():
                    print(f"\n[{time}] - Giveaway Skipped")
                    GiveawayData2()
                else:
                    await asyncio.sleep(5)
                    await message.add_reaction("🎉")          
                    print(f"\n[{time}] - Giveaway Sniped And Entered")
                    GiveawayData()

    if f'Congratulations <@{bot.user.id}>' in message.content:
        if gsniper == 1:
            if str(message.author.id) in giveaway_ids:   
                print(f"\n[{time}] - Giveaway Has Been Won")
                GiveawayData()
        else:
            return

    await bot.process_commands(message)

@bot.event
async def on_connect():
    title = ctypes.windll.kernel32.SetConsoleTitleW(f"CotraUI") 
    time.sleep(1)
    title
    new_splash()


@bot.command()
async def nitrosnipermode(ctx):
        await ctx.message.delete()
        global snipermode
        if snipermode == 0:
            snipermode += 1        
        elif snipermode == 1:
            snipermode  -= 1


@bot.command()
async def gsnipermode(ctx):
        await ctx.message.delete()
        global gsniper
        if gsniper == 0:
            gsniper += 1        
        elif gsniper == 1:
            gsniper -= 1

ritchy_pres = config['rpc']

if ritchy_pres == True:
    rpc = Presence("926564240259711107")
    rpc.connect()
    rpc.update(state="Using Cotra Selfbot",large_image="uwu",start=time.time(),large_text=f"Logged in as : {login['username']}",buttons=[{"label": "Discord", "url": "https://discord.gg/6EzTsPnbbA"}],small_image="uwu",small_text=f"Version : {version}")


def color_fade(fade_ticks, *colors: list, repeat=False):
        if colors == ():
            colors = [[255, 0, 0], [255, 255, 0], [0, 128, 0], [0, 0, 255]]
        else:
            colors = list(colors)
        if repeat:
            colors.append(colors[0])
        active_RGB = colors[0].copy()
        active_RGB_list = []
        for color_pos, color in enumerate(colors[:-1]):
            for i in range(fade_ticks):
                active_RGB_list.append(active_RGB.copy())
                for pos, RGB in enumerate(color):
                    if color_pos == len(colors) - 1:
                        color_pos = 0
                        RGB2 = colors[color_pos+1][pos]
                    else:
                        RGB2 = colors[color_pos+1][pos]
                    distance = RGB2 - RGB
                    active_RGB[pos] += int(distance / fade_ticks)
        return active_RGB_list

def rgb_to_hex(rgb):
        return '%02x%02x%02x' % rgb

def RGB_to_hex(RGB):
        for pos in range(len(RGB)):
            RGB[pos] = str(RGB[pos])
        hex_list = []
        hex_list.extend("0123456789ABCDEF")
        all_combo = [f"{x}{y}" for x in hex_list for y in hex_list]
        for pos, color in enumerate(RGB.copy()):
            RGB[pos] = all_combo[int(color)]
        return f"0x{''.join(RGB)}"



#/////// HELP ///////


@bot.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.description = f"**```Help Panel```**\n{bot.command_prefix}general »» Displays general commands\n{bot.command_prefix}fun »» Displays fun commands (**SOME RISKY**)\n{bot.command_prefix}helpsec »» Displays helpsection commands\n{bot.command_prefix}memes »» Displays meme commands\n{bot.command_prefix}server »» Displays server commands\n{bot.command_prefix}text »» Displays text commands\n{bot.command_prefix}images »» Displays image commands\n{bot.command_prefix}token »» Displays token commands\n{bot.command_prefix}nsfw »» Displays nsfw commands\n{bot.command_prefix}promo »» Displays promo commands\n{bot.command_prefix}settings »» Displays settings commands"
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.add_field(name="**```info:```**", value=f"```|Version: {version} |Commands: {len(bot.commands)} |Prefix: {config['prefix']}```")
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])
        print(Fore.CYAN+"[Command] <>Help Panel<>"+Fore.RESET)

#/////// GENERAL ///////

@bot.command()
async def general(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```General Panel```\n{bot.command_prefix}allcmds »» Displays all commands\n{bot.command_prefix}purge »» Deletes messages\n{bot.command_prefix}userinfo »» Displays user info\n{bot.command_prefix}first »» Displays first ever message\n{bot.command_prefix}yt »» searches youtube\n{bot.command_prefix}getpfp »» Posts Users Pfp\n{bot.command_prefix}dmdel »» deletes dms by amount\n{bot.command_prefix}dnd »» sets status dnd\n{bot.command_prefix}aboutme »» sets about me\n{bot.command_prefix}status »» sets status\n{bot.command_prefix}online »» sets status online\n{bot.command_prefix}idle »» sets status idle\n{bot.command_prefix}invisible »» sets status invisible\n{bot.command_prefix}clockon »» sets clock in status\n{bot.command_prefix}embed »» creates an embed\n{bot.command_prefix}emptymessage »» sends empty message\n{bot.command_prefix}dele »» deletes messages"
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>General Panel<>"+Fore.RESET)

#/////// MEMES ///////

@bot.command()
async def memes(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```Memes Panel```\n{bot.command_prefix}blm »» Shows a BLM image\n{bot.command_prefix}discum »» Shows a Discum meme\n{bot.command_prefix}pp »» Displays users PP size\n{bot.command_prefix}meme »» Posts memes\n{bot.command_prefix}balls »» Posts my balls are cold\n{bot.command_prefix}gay »» see how gay someone is\n{bot.command_prefix}gaypfp »» gay pfp user\n{bot.command_prefix}pixel »» pixel pfp user\n{bot.command_prefix}lolice »» lolice pfp user\n{bot.command_prefix}passed »» mission passed pfp user\n{bot.command_prefix}wasted »» wasted pfp user\n{bot.command_prefix}horny »» gives horny card to user\n{bot.command_prefix}jail »» jails user\n{bot.command_prefix}triggered »» triggered pfp user\n{bot.command_prefix}joke »» stick bug user\n{bot.command_prefix}8ball »» Uses 8ball"   
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Memes Panel<>"+Fore.RESET)

#/////// FUN ///////

@bot.command()
async def fun(ctx):
    if not is_me(ctx.message):
        await ctx.message.delete()
        return
    embed=discord.Embed(title=str(config['theme']['title']), description="commands", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.description = f"```Fun Panel```\n{bot.command_prefix}killvc »» kills a VC\n{bot.command_prefix}massgc »» mass adds user to gc\n{bot.command_prefix}animnick »» animates server nickname\n{bot.command_prefix}rgbrole »» makes a role rainbow\n{bot.command_prefix}hideinvite »» hides discord invite\n{bot.command_prefix}hidelink »» Hides link\n{bot.command_prefix}gcleave »» leaves all gcs\n{bot.command_prefix}tts »» message to tts\n{bot.command_prefix}loopstatus »» loops online and invisible"
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Fun Panel<>"+Fore.RESET)

#/////// NSFW ///////

@bot.command()
async def nsfw(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```NSFW Panel Commands```\n{bot.command_prefix}hentai »» Shows hentai options\n{bot.command_prefix}pgif »» Posts a porn gif\n{bot.command_prefix}niko »» Posts a lovely vid\n{bot.command_prefix}lewdneko »» Posts lewd neko pictures\n{bot.command_prefix}yiff »» Posts yiff pictures\n{bot.command_prefix}femboy »» Posts femboy pictures\n{bot.command_prefix}cum »» Posts cum pictures\n{bot.command_prefix}spank »» Posts spank pictures\n{bot.command_prefix}feet »» Posts feet pictures\n{bot.command_prefix}pokeporn »» Posts pokemon porn\n{bot.command_prefix}gyiff »» Posts Gay yiff\n{bot.command_prefix}r34 »» Posts random r34 porn\n{bot.command_prefix}fortnite »» Posts random fortnite porn\n{bot.command_prefix}paizuri »» posts paizuri\n{bot.command_prefix}hthighs »» posts hentai thighs\n{bot.command_prefix}holo »» Posts holo\n{bot.command_prefix}femdom »» Posts femdom\n{bot.command_prefix}lewdkemo »» Posts lewdkemo\n{bot.command_prefix}erokemo »» Posts erokemo\n{bot.command_prefix}pwankg »» Posts pwankg\n{bot.command_prefix}keta »» Posts keta\n{bot.command_prefix}lewdk »» Posts lewdk\n{bot.command_prefix}eron »» Posts eron\n{bot.command_prefix}eroyuri »» Posts eroyuri\n{bot.command_prefix}solo »» Posts solo"
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>NSFW Panel<>"+Fore.RESET)

#/////// Settings ///////

@bot.command()
async def settings(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```Settings Panel```\n{bot.command_prefix}restart »» Restarts the bot\n{bot.command_prefix}info »» Displays bot info\n{bot.command_prefix}clearconsole »» Clears the console\n{bot.command_prefix}uptime »» Shows how long bots been up\n{bot.command_prefix}themeinfo »» Displays theme information\n{bot.command_prefix}support »» Displays support information\n{bot.command_prefix}gsnipermode »» turns on/off giveaway sniper\n{bot.command_prefix}nitrosnipermode »» turns on/off nitro sniper"
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Settings Panel<>"+Fore.RESET)

#/////// token commands ///////

@bot.command()
async def token(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```Token Panel```\n{bot.command_prefix}riptoken »» Kills the token\n{bot.command_prefix}tkninfo »» Displays token info"
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Token Panel<>"+Fore.RESET)

#/////// Server commands ///////

@bot.command()
async def server(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```Server Panel```\n{bot.command_prefix}yoink »» Clones a server\n{bot.command_prefix}invnick »» Makes nick Invisible\n{bot.command_prefix}ban »» Bans a user from server\n{bot.command_prefix}unban »» Unbans a user from server\n{bot.command_prefix}kick »» kicks a user from server\n{bot.command_prefix}sinfo »» Displays server info\n{bot.command_prefix}nick »» change server nickname\n{bot.command_prefix}police »» Police Role"
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Server Panel<>"+Fore.RESET)

#/////// Text commands ///////

@bot.command()
async def text(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```Text Panel```\n{bot.command_prefix}spam »» spams message\n{bot.command_prefix}asci »» makes text asci\n{bot.command_prefix}rv »» reverses text\n{bot.command_prefix}encrypt »» encrypts message\n{bot.command_prefix}decrypt »» decrypts message\n{bot.command_prefix}gp »» ghost pings user\n{bot.command_prefix}shrek »» what are ye doin in ma swamp\n{bot.command_prefix}boldunderline »» bold underline\n{bot.command_prefix}underline »» underlines message\n{bot.command_prefix}bolditalic »» bold italics message\n{bot.command_prefix}bold »» bolds message\n{bot.command_prefix}lenny »» posts lenny face\n{bot.command_prefix}emojify »» emojifys message\n{bot.command_prefix}spoiler »» spoilers message"
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Text Panel<>"+Fore.RESET)


#/////// images ///////

@bot.command()
async def images(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```Images Panel```\n{bot.command_prefix}rick »» rick rolls user\n{bot.command_prefix}neko »» posts neko\n{bot.command_prefix}foximg »» posts a cute fox\n{bot.command_prefix}pat »» pats user\n{bot.command_prefix}kiss »» kisses user\n{bot.command_prefix}hug »» hugs user\n{bot.command_prefix}furry »» Posts furry image\n{bot.command_prefix}wallpaper »» Posts wallpaper\n{bot.command_prefix}cuddle »» Cuddles user\n{bot.command_prefix}gasm »» gasm\n{bot.command_prefix}feed »» Feeds user\n{bot.command_prefix}poke »» Pokes user\n{bot.command_prefix}tickle »» Tickles user\n{bot.command_prefix}baka »» bakas user\n{bot.command_prefix}play »» sends cute play img\n{bot.command_prefix}warcrimes »» commits warcrimes\n{bot.command_prefix}trampoline »» bouncy bouncy\n{bot.command_prefix}ducking »» ducks cutely\n{bot.command_prefix}trump »» sends trump tweet\n{bot.command_prefix}ph »» fake pornhub comment\n{bot.command_prefix}stickbug »» stickbugs user\n{bot.command_prefix}gah »» omg\n{bot.command_prefix}coffeee »» steamy coffee\n{bot.command_prefix}waifu »» waifu uwu"
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Images Panel<>"+Fore.RESET)

#/////// Promotions ///////

@bot.command()
async def promo(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```Promotion Panel```\n{bot.command_prefix}bot »» Sponsor botsb\n{bot.command_prefix}mysite »» Displays CotraUI Site\n{bot.command_prefix}shop »» Displays Shop Info\n{bot.command_prefix}cactus »» Sponsor cactus reselling\n{bot.command_prefix}buy »» Buy CotraUI\n{bot.command_prefix}troop »» Official CotraUI Reseller\n{bot.command_prefix}pathetic »» Official CotraUI Reseller\n{bot.command_prefix}complex »» Official CotraUI Reseller\n{bot.command_prefix}flop »» Official CotraUI Reseller"
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Promotions Panel<>"+Fore.RESET)

#/////// help section ///////

@bot.command()
async def helpsec(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```Help Section```\n{bot.command_prefix}helpallcmds »» Displays help for command\n{bot.command_prefix}helppurge »» Displays help for command\n{bot.command_prefix}helpuserinfo »» Displays help for command\n{bot.command_prefix}helpfirst »» Displays help for command\n{bot.command_prefix}helpblm »» Displays help for command\n{bot.command_prefix}helpdiscum »» Displays help for command\n{bot.command_prefix}helpgay »» Displays help for command\n{bot.command_prefix}helpkillvc »» Displays help for command\n{bot.command_prefix}helpmassgc »» Displays help for command\n{bot.command_prefix}helpanimnick »» Displays help for command\n{bot.command_prefix}helprgbrole »» Displays help for command\n{bot.command_prefix}helpcotra »» Displays help for command\n{bot.command_prefix}helpasci »» Displays help for command\n{bot.command_prefix}helprv »» Displays help for command\n{bot.command_prefix}helppgif »» Displays help for command\n{bot.command_prefix}helpniko »» Displays help for command\n{bot.command_prefix}helprestart »» Displays help for command\n{bot.command_prefix}helpinfo »» Displays help for command\n{bot.command_prefix}helpclearconsole »» Displays help for command\n{bot.command_prefix}helptkninfo »» Displays help for command\n{bot.command_prefix}helprick »» Displays help for command\n{bot.command_prefix}helpuwu »» Displays help for command\n{bot.command_prefix}helpneko »» Displays help for command\n{bot.command_prefix}helppat »» Displays help for command\n**{bot.command_prefix}helpsec2 »» Goes to Help Section 2**"
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Help section Panel<>"+Fore.RESET)

@bot.command()
async def helpsec2(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```Help Section 2```\n{bot.command_prefix}helpkiss »» Displays help for command\n{bot.command_prefix}helphug »» Displays help for command\n{bot.command_prefix}helpbot »» Displays help for command\n{bot.command_prefix}helpmysite »» Displays help for command\n{bot.command_prefix}helpshop »» Displays help for command\n{bot.command_prefix}helpcactus »» Displays help for command\n{bot.command_prefix}helpyoink »» Displays help for command\n{bot.command_prefix}helpriptoken »» Displays help for command\n{bot.command_prefix}helphidelink »» Displays help for command\n{bot.command_prefix}helphideinvite »» Displays help for command\n{bot.command_prefix}helpspam »» Displays help for command\n ```Dm cotra#0001 If any issues persist```"
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```info:```", value=f"```Type {bot.command_prefix}command-name```")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Help Section2 Panel<>"+Fore.RESET)

#/////// Commands below ///////

# async def killvc(ctx,channelid,times):
#     if not is_me(ctx.message):
#         return
#     await ctx.message.delete()
#     for x in range(int(times)):
#         url = "https://canary.discord.com/api/v9/channels/"+str(channelid)+"/call"
#         headers = {"Authorization": config["token"],"Content-Type": "application/json",
#             "Accept": "*/*",
#             "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}


#         regeion = ['europe', 'hongkong', 'india', 'russia', 'brazil', 'japan', 'singapore', 'southafrica', 'sydney', 'us-central', 'us-east', 'us-west', 'us-south']
#         data = {"region":random.choice(regeion)}

#         pp = requests.patch(url=url, headers=headers, json=data)

@bot.command()
async def joke(ctx):
    await ctx.message.delete()
    headers = requests.structures.CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers=headers)
    stuff = json.loads(response.text)
    joke = stuff["joke"]
    embed=discord.Embed(title=str(config['theme']['title']), Description="i cant find my shoes" ,color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def killvc(ctx,times):
    if not is_me(ctx.message):
        return
    await ctx.message.delete()
    for ch in bot.private_channels:
         channelid = ch.id
    for x in range(int(times)):
        url = "https://canary.discord.com/api/v9/channels/"+str(channelid)+"/call"
        headers = {"Authorization": config["token"],"Content-Type": "application/json",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}


        regeion = ['europe', 'hongkong', 'india', 'russia', 'brazil', 'japan', 'singapore', 'southafrica', 'sydney', 'us-central', 'us-east', 'us-west', 'us-south']
        data = {"region":random.choice(regeion)}

        pp = requests.patch(url=url, headers=headers, json=data)


@bot.command()
async def helphidelink(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="hidelink command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}hidelink (url) (word or url)```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helphideinvite(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="hideinvite command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}hideinvite (discord invite) (word or url)```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

# @bot.command(name="rgbrole")
# async def rgbrole(ctx, role: discord.Role):
#         while True:
#             for color in color_fade(50):
#                 await role.edit(reason = None, color = int(RGB_to_hex(color), 16))

# @bot.command()
# async def rgbrole(ctx, *, role: discord.Role):
#     await ctx.message.delete()
#     oldcolour = role.color
#     red = Color("#ff3d3d")
#     pink = Color("#f54287")
#     rainbow = list(red.range_to(pink, 50))
#     for _ in range(9999999):
#         for x in rainbow:
#             colour = f'{x}'
#             await role.edit(color=int(colour.replace('#', '0x'), 0))
#     await role.edit(color=oldcolour)

rainboo = 0
@bot.command()
async def rgbrole(ctx, *, role: discord.Role):
    await ctx.message.delete()
    global rainboo
    oldcolour = role.color
    red = Color("#ff3d3d")
    pink = Color("#f54287")
    rainbow = list(red.range_to(pink, 50))
    if rainboo == 0:
        rainboo +=1
    elif rainboo == 1:
        rainboo -=1
    while rainboo == 1:
        for x in rainbow:
            colour = f'{x}'
            await role.edit(color=int(colour.replace('#', '0x'), 0))
    await role.edit(color=oldcolour)

@bot.command(name="police")
async def policerole(ctx, role: discord.Role):
        print(Fore.CYAN+"[Command] <>Police Role<>"+Fore.RESET)
        await ctx.message.delete()
        cols = [0xff0002,0x001eff]
        color = random.choice(cols)
        while True:
                await role.edit(reason = None, color = random.choice(cols))
                await asyncio.sleep(1.5)

@bot.command(name="pcinfo", aliases=["pcstats","pcspecs","pcspec"])
async def pcinfo(ctx):
        computer = wmi.WMI()
        await ctx.message.delete()
        os_info = computer.Win32_OperatingSystem()[0]
        os_name = os_info.Name.encode('utf-8').split(b'|')[0]
        embed = discord.Embed(title='Pc Specs', color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name=f'```WIN```', value=str(os_name).replace("'", "").replace("b", "", 1), inline=False)
        embed.add_field(name=f'```CPU```', value=f'{computer.Win32_Processor()[0].Name}', inline=False)
        embed.add_field(name=f'```RAM```', value=f'{str(round(psutil.virtual_memory().total / (1024.0 **3)))} GB', inline=False)
        embed.add_field(name=f'```GPU```', value=f'{computer.Win32_VideoController()[0].Name}', inline=False)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])



@bot.command(pass_context=True)
async def meme(ctx):
        await ctx.message.delete()
        embed=discord.Embed(title=str(config['theme']['title']), Description="i cant find my shoes" ,color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.add_field(name="Enjoy some memes", value=":rofl:")
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                embed.set_thumbnail(url=str(config['theme']['thumbnail']))
                embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
                await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command()
async def staring(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), Description="i cant find my shoes" ,color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Stop staring =w=", value="fine... :flushed:")
    embed.set_image(url="https://cdn.discordapp.com/attachments/917896528927019012/932138950804537404/unknown.png")
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def embed(ctx, *, msg=None):
    await ctx.message.delete()
    if msg == None:
        return await ctx.channel.send("You need to specify a message to send")
    embed = discord.Embed(
        title=f"{bot.user.display_name} says",
        description=msg,
        color=int(config['theme']['embed_color'].replace('#', '0x'), 0)
    )
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def dmdel(ctx, ammount=None):
    try:
        limit = int(ammount)
    except:
        limit=None
    await ctx.message.delete()
    for  m in await ctx.channel.history(limit=limit).flatten():
        try:
            await m.delete()
        except:
            pass

@bot.command()
async def dele(ctx, ammount=None):
    try:
        limit = int(ammount)
    except:
        limit=None
    await ctx.message.delete()
    for  m in await ctx.channel.history(limit=limit).flatten():
        try:
            await m.delete()
        except:
            pass

@bot.command(pass_context=True)
async def femboy(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']),color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/FemBoys/new.json?sort=hot') as r:
            res = await r.json()
            embed.add_field(name="Enjoy some femboy", value=":flushed:")
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_thumbnail(url=str(config['theme']['thumbnail']))
            embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
            await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def anime(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']),color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/anime/new.json?sort=hot') as r:
            res = await r.json()
            embed.add_field(name="Enjoy some anime", value=":flushed:")
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_thumbnail(url=str(config['theme']['thumbnail']))
            embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
            await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def r34(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']),color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/rule34/new.json?sort=hot') as r:
            res = await r.json()
            embed.add_field(name="Enjoy some rule34", value=":flushed:")
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_thumbnail(url=str(config['theme']['thumbnail']))
            embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
            await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def gyiff(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']),color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/gfur/new.json?sort=hot') as r:
            res = await r.json()
            embed.add_field(name="Enjoy Some Gay Yiff", value=":flushed:")
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_thumbnail(url=str(config['theme']['thumbnail']))
            embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
            await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def fortnite(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']),color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/FortniteNSFW/new.json?sort=top') as r:
            res = await r.json()
            embed.add_field(name="Enjoy Some Fortnite Porn", value=":flushed:")
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_thumbnail(url=str(config['theme']['thumbnail']))
            embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
            await ctx.send(embed=embed, delete_after=config['deletetime'])



@bot.command(pass_context=True)
async def pokeporn(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']),color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/pokeporn/new.json?sort=hot') as r:
            res = await r.json()
            embed.add_field(name="Enjoy some pokemon porn", value=":flushed:")
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_thumbnail(url=str(config['theme']['thumbnail']))
            embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
            await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def yiff(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']),color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/yiff/new.json?sort=top') as r:
            res = await r.json()
            embed.add_field(name="Enjoy some yiff", value=":flushed:")
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_thumbnail(url=str(config['theme']['thumbnail']))
            embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
            await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command(pass_context=True)
async def furry(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']),color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/furry/new.json?sort=hot') as r:
            res = await r.json()
            embed.add_field(name="Enjoy some furry", value=":flushed:")
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_thumbnail(url=str(config['theme']['thumbnail']))
            embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
            await ctx.send(embed=embed, delete_after=config['deletetime'])



@bot.command()
async def helpallcmds(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="allcmds command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}allcmds```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def themeinfo(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Posted Theme info<>"+Fore.RESET)
    embed=discord.Embed(title="Theme Info", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.add_field(name=f"```Theme name```", value=(config['theme']['name']), inline=False)
    embed.add_field(name=f"```Theme Header```", value=(config['theme']['title']), inline=False)
    embed.add_field(name=f"```Thumbnail```", value=(config['theme']['thumbnail']), inline=False)
    embed.add_field(name=f"```Embed color```", value=config['theme']['embed_color'], inline=False)
    embed.add_field(name=f"```footer image```", value=(config['theme']['footer_img']), inline=False)
    embed.add_field(name=f"```footer text```", value=(config['theme']['footer_text']), inline=False)
    embed.add_field(name=f"```Delete time```", value=(config['deletetime']), inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helppurge(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="Purge command", color=config['color'], timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}purge [amount]```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command()
async def helpuserinfo(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="userinfo command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}userinfo [mention]```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpfirst(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="first command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}first```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command()
async def helpblm(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="blm command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}blm```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command()
async def helpspam(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="spam command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}spam (how many times) (word)```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpdiscum(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="discum command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}discum```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command()
async def helpgay(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="gay command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}gay```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpkillvc(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="killvc command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}killvc [5000]```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpyoink(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="copy command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}yoink (in server)```", inline=False)
    embed.add_field(name="info", value="```copys all server channels to another server (not roles)```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

@bot.command()
@commands.guild_only()
async def sinfo(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name = f"```{ctx.guild.name}:``` ", value = f":space_invader: ID: ```{ctx.guild.id}``` \n:detective: Owner: **```{ctx.guild.owner}```**\n:comet: Creation: ```{ctx.guild.created_at.strftime(format)}``` \n:man_pouting: Members: ```{ctx.guild.member_count}``` \n:zap: Channels: ```{channels} Channels; {text_channels} Text, {voice_channels} Voice, {categories}```\n:white_check_mark: Verification: ```{str(ctx.guild.verification_level).upper()}```")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>ServerInfo<>"+Fore.RESET)


@bot.command()
async def helpriptoken(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="riptoken command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}riptoken (token)```", inline=False)
    embed.add_field(name="info", value="```kills the token```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpmassgc(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="massgc command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}massgc [victim id] [1-10]```", inline=False)
    embed.add_field(name="info", value="```post this in another persons dms``` ```[not the victims dms]```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpanimnick(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="animnick command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}animnick [desired name 1] [desired name 2]```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helprgbrole(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="rgbrole command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}rgbrole [mention role]```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpcotra(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="cotra command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}cotra [encode/decode] [message]```", inline=False)
    embed.add_field(name="info", value=f"```Encodes/decodes base64 to a message```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command(name="helpasciitext", aliases=["helpasc","helpasci","helpascii"])
async def helpasci(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="ascii command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}ascii [message]```", inline=False)
    embed.add_field(name="info", value=f"```Creates ascii text```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helprv(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="rv command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}rv [message]```", inline=False)
    embed.add_field(name="info", value=f"```reverses text```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helppgif(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="pgif command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}pgif```", inline=False)
    embed.add_field(name="info", value=f"```Posts porn gif```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpniko(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="niko command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}niko```", inline=False)
    embed.add_field(name="info", value=f"```Posts porn of nikocado avocado```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helprestart(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="restart command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}restart```", inline=False)
    embed.add_field(name="info", value=f"```restarts bot```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpinfo(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="info command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}info```", inline=False)
    embed.add_field(name="info", value=f"```displays info about selfbot```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpclearconsole(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="clearconsole command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}clearconsole```", inline=False)
    embed.add_field(name="info", value=f"```clears the console```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helptkninfo(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="tkninfo command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}tkninfo```", inline=False)
    embed.add_field(name="info", value=f"```Displays token info```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helprick(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="rick command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}rick```", inline=False)
    embed.add_field(name="info", value=f"```Posts a rickroll```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command()
async def helpuwu(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="uwu command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}uwu [mention user]```", inline=False)
    embed.add_field(name="info", value=f"```Posts a uwu image```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpneko(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="uwu command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}neko```", inline=False)
    embed.add_field(name="info", value=f"```Posts a neko image```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helppat(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="pat command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}pat [mention]```", inline=False)
    embed.add_field(name="info", value=f"```Posts a pat image```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def support(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.description = f"```Support Panel```\n```Discord »» https://discord.gg/j8VV2RzKs3```\n```Contact »» cotra#0001```"
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Support<>"+Fore.RESET)


@bot.command()
async def helpkiss(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="kiss command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}kiss [mention]```", inline=False)
    embed.add_field(name="info", value=f"```Posts a kiss image```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helphug(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="hug command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}hug [mention]```", inline=False)
    embed.add_field(name="info", value=f"```Posts a hug image```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpbot(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="bot command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}bot```", inline=False)
    embed.add_field(name="info", value=f"```Posts bot sponsor```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpmysite(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="mysite command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}mysite```", inline=False)
    embed.add_field(name="info", value=f"```Posts mysite sponsor```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpshop(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="shop command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}shop```", inline=False)
    embed.add_field(name="info", value=f"```Posts shop sponsor```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def helpcactus(ctx):
    await ctx.message.delete()
    print(Fore.CYAN+"[Command] <>Help posted<>"+Fore.RESET)
    embed=discord.Embed(title="cactus command", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Example", value=f"```{bot.command_prefix}cactus```", inline=False)
    embed.add_field(name="info", value=f"```Posts cactus sponsor```", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])



@bot.command()
async def uptime(ctx):
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    embed=discord.Embed(title="CotraUI has been online:", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name=f"{f'`'+uptime+'`'}", value=f"Enjoy the rest of your day")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
start_time = datetime.datetime.utcnow()

@bot.command()
async def foximg(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    embed=discord.Embed(title="Cute fox images",description="Enjoy <3", color=int(config['theme']['embed_color'].replace('#', '0x'), 0),timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_image(url=r["image"])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command()
async def gcleave(ctx):
    await ctx.message.delete()
    for channel in bot.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()


@bot.command()
async def hentai(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.add_field(name="**Hentai Catagories**", value=f"anal\nboobs\npussy\nblowjob\nlesbian\nfeet\ntentacle", inline=True)
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])

        await ctx.send(embed=embed)
    elif str(category).lower() == "anal":
        r = requests.get("https://nekos.life/api/v2/img/anal")
        res = r.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
   
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
    elif str(category).lower() == "boobs":
        r = requests.get("https://nekos.life/api/v2/img/boobs")
        res = r.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
  
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
    elif str(category).lower() == "pussy":
        r = requests.get("https://nekos.life/api/v2/img/pussy")
        res = r.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
   
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
    elif str(category).lower() == "blowjob":
        r = requests.get("https://nekos.life/api/v2/img/blowjob")
        res = r.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
   
        embed.set_image(url=res['url'])
        await ctx.send(embed=embed)
    elif str(category).lower() == "lesbian":
        r = requests.get("https://nekos.life/api/v2/img/les")
        res = r.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
   
        embed.set_image(url=res['url'])
    elif str(category).lower() == "feet":
        r = requests.get("https://nekos.life/api/v2/img/feet")
        res = r.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        
        embed.set_image(url=res['url'])
    elif str(category).lower() == "tentacle":    
        r = requests.get(f'https://nekobot.xyz/api/image?type=tentacle')
        res = r.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])

@bot.command(name="pgif",)
async def pgif(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=pgif')
        res = request.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.add_field(name="**Enjoy some lovely porn**", value=":)", inline=True)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command(name="coffee",)
async def coffee(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=coffee')
        res = request.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.add_field(name=f"coffee for all!", value=":coffee:")
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])
        print(Fore.CYAN+"[Command] <>coffee<>"+Fore.RESET)

@bot.command(name="paizuri",)
async def paizuri(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=paizuri')
        res = request.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.add_field(name=f"paizuri for all!", value=":flushed:")
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])
        print(Fore.CYAN+"[Command] <>paizuri<>"+Fore.RESET)

@bot.command(name="hthighs",)
async def hthighs(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=hthigh')
        res = request.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.add_field(name=f"thighs for all!", value=":flushed:")
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])
        print(Fore.CYAN+"[Command] <>hthighs<>"+Fore.RESET)

@bot.command(name="thighs",)
async def thighs(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=thigh')
        res = request.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.add_field(name=f"thighs for all!", value=":flushed:")
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])
        print(Fore.CYAN+"[Command] <>thighs<>"+Fore.RESET)

@bot.command(name="gah",)
async def gah(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=gah')
        res = request.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.add_field(name=f"omg!!", value=":flushed:")
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])
        print(Fore.CYAN+"[Command] <>gah<>"+Fore.RESET)

@bot.command(name="holo",)
async def holo(ctx):
        await ctx.message.delete()
        request = requests.get(f'https://nekobot.xyz/api/image?type=holo')
        res = request.json()
        embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.add_field(name=f"idk what this is", value=":rofl:")
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        embed.set_image(url=res['message'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])
        print(Fore.CYAN+"[Command] <>holo<>"+Fore.RESET)

@bot.command()
async def femdom(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/femdom")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="uwu", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>femdom<>"+Fore.RESET)

@bot.command()
async def lewdkemo(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/lewdkemo")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="uwu", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>lewdkemo<>"+Fore.RESET)

@bot.command()
async def erokemo(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erokemo")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="OwO", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>erokemo<>"+Fore.RESET)

@bot.command()
async def pwankg(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pwankg")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="OwO you like?", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>pwankg<>"+Fore.RESET)

@bot.command()
async def keta(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/keta")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="cute~", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>keta<>"+Fore.RESET)

@bot.command()
async def lewdk(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/lewdk")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="cute~", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>lewdk<>"+Fore.RESET)

@bot.command()
async def waifu(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/waifu")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="cute~", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>waifu<>"+Fore.RESET)

@bot.command()
async def eron(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/eron")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="cute~", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>eron<>"+Fore.RESET)

@bot.command()
async def eroyuri(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/eroyuri")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="cute~", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>eroyuri<>"+Fore.RESET)

@bot.command()
async def solo(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/solo")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="cute~", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>solo<>"+Fore.RESET)

@bot.command()
async def massgc(ctx,userid1,times):
    if not is_me(ctx.message):
        return
    await ctx.message.delete()
    for x in range(int(times)):
            
        headers = {
            'authority': 'discord.com',
            'content-length': '0',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0Mjc2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IkFkZCBGcmllbmRzIHRvIERNIn0=',
            'authorization': config["token"],
            'x-debug-options': 'bugReporterEnabled',
            'accept-language': 'en-US',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://discord.com/channels/@me/895409258785550406',
            'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
        }

        response = requests.put(f'https://discord.com/api/v9/channels/{str(ctx.channel.id)}/recipients/{userid1}', headers=headers)
        
        #print(response.text)
        createdserver = response.json()
        for x in createdserver["recipients"]:
            if userid1 != x["id"]:
                cotra=x["id"]

        headers = {
            'authority': 'discord.com',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0Mjc2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'authorization': config['token'],
            'x-debug-options': 'bugReporterEnabled',
            'accept-language': 'en-US',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://discord.com/channels/@me/908312413412155404',
            'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
        }

        response = requests.delete(f'https://discord.com/api/v9/channels/{str(createdserver["id"])}/recipients/{cotra}', headers=headers)
        #print(cotra)
        #print(response.text)
        choices = ["haha lol","bitchnigga","fatty","https://www.cotra.xyz","U suck","die bitch","CotraUI Selfbot"]
        headers = {
            'authority': 'discord.com',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0Mjc2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'authorization': config['token'],
            'x-debug-options': 'bugReporterEnabled',
            'accept-language': 'en-US',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
            'content-type': 'application/json',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://discord.com/channels/@me/908317396379525160',
            'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
        }
        xyz = random.choice(choices)
        data = '{"name":"'+xyz+'"}'

        response = requests.patch(f'https://discord.com/api/v9/channels/{str(createdserver["id"])}', headers=headers, data=data)

        headers = {
            'authority': 'discord.com',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0Mjc2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
            'authorization': config['token'],
            'x-debug-options': 'bugReporterEnabled',
            'accept-language': 'en-US',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://discord.com/channels/@me',
            'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
        }

        response = requests.delete(f'https://discord.com/api/v9/channels/{str(createdserver["id"])}', headers=headers)
       # print(response.text)

# (pass_context)= True
# async def rainbowrole(ctx,*,rolename):
#     if not is_me(ctx.message): #i like lines
#         return
#     await ctx.message.delete()
#     print("<>rainbowrole<>")
    
#     role = discord.utils.get(ctx.message.guild.roles,name=rolename)
#     colors = ["16711685","15105570","16771840","2067276","3447003","10181046","15277667"]
#     num1 = 0
#     while True:


#         headers = {
#             'authority': 'discord.com',
#             'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0Mjc2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
#             'authorization': config['token'],
#             'x-debug-options': 'bugReporterEnabled',
#             'accept-language': 'en-US',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
#             'content-type': 'application/json',
#             'accept': '*/*',
#             'origin': 'https://discord.com',
#             'sec-fetch-site': 'same-origin',
#             'sec-fetch-mode': 'cors',
#             'sec-fetch-dest': 'empty',
#             'referer': 'https://discord.com/channels/889840534754054145/907218560248610836',
#             'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
#         }

#         data = '{"name":"'+rolename+'","permissions":"1071728021057","color":'+str(random.choice(colors))+',"hoist":false,"mentionable":false,"icon":null,"unicode_emoji":null}'

#         response = requests.patch(f'https://discord.com/api/v9/guilds/{str(ctx.message.guild.id)}/roles/{str(role.id)}', headers=headers, data=data)
#         await asyncio.sleep(1.5)
#         #if num1 + 1000 > 16777215:
#             #num1 = 0
#         #num1 += 1000
#         #print(response.text)
#         if "retry_after" in response.text:
#             kk=response.json()
#             print(f"hit retry limit waiting {str(kk['retry_after'])} second(s)")
#             await asyncio.sleep(int(kk["retry_after"]))

@bot.command()
async def mysite(ctx,):
    await ctx.message.delete()
    embed=discord.Embed(title="CotraUI", description="Cotra selfbot is op", url="https://www.cotra.xyz/", color=str(config['theme']['embed_color']), timestamp=ctx.message.created_at)
    embed.add_field(name="Website", value="https://cotra.xyz",inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    if not is_me(ctx.message):
        return
    print(Fore.CYAN+"[Command] <>MySite<>"+Fore.RESET)

@bot.command()
async def balls(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="**My balls are cold**", value=":flushed:", inline=True)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.set_image(url="https://media.discordapp.net/attachments/824953552324788273/908661319488634910/image0-5-2.gif")
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command()
async def nitroking(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Nitro King", discription="Fraudion Ontop", color=int(config['theme']['embed_color'].replace('#', '0x'), 0),timestamp=ctx.message.created_at)
    embed.add_field(name="94 Boosts in 1 day", value="Cotra on top", inline=True)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.set_image(url="https://images-ext-1.discordapp.net/external/Ma42_cB-hgi9YnQKzK5iELhamXlDktUk-7-U9JtGXWo/https/cdn.upload.systems/uploads/GM5MIAlZ.png?width=393&height=671")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    if not is_me(ctx.message):
        return
    print(Fore.CYAN+"[Command] <>NitroPosted<>"+Fore.RESET)

@bot.command()
async def neko(ctx):
    if not is_me(ctx.message):
        return
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/neko")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Enjoy Nekos", value=":)", inline=True)
    embed.set_thumbnail(url=str(config['theme']['thumbnail'])) 
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def emptymessage(ctx):
    await ctx.message.delete()
    await ctx.send("_ _")

@bot.command()
async def first(ctx):
        channel = ctx.channel
        first_message = (await channel.history(limit = 1, oldest_first = True).flatten())[0]                                        
        embed = discord.Embed(title=f'First Message',color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
        embed.add_field(name = "Content", value = f"{first_message.content}", inline=True)
        embed.set_thumbnail(url=str(config['theme']['thumbnail']))
        embed.add_field(name = "Jump URL", value = f"{first_message.jump_url}", inline=False)
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command(name="store", aliases=["shop","sellix"])
async def store(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="My store", discription="DiscordTokens", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.add_field(name="My Shop", value="https://sellix.io/Cotra || https://discord.gg/Auqbm85DUS", inline=True)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    if not is_me(ctx.message):
        return
    print(Fore.CYAN+"[Command] <>store<>"+Fore.RESET)

@bot.command()
async def animnick(ctx,*,names):
    print(Fore.CYAN+"[Command] <>animnick started<>"+Fore.RESET)
    if not is_me(ctx.message):
        return
    await ctx.message.delete()
    names=names.split(" ")
    while True:
    


        headers = {
        'authority': 'discord.com',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0NTk3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        'x-fingerprint': '908477669916692491.kcb2l619Luz24fNTGCkHM-OklWM',
        'authorization': config['token'],
        'x-debug-options': 'bugReporterEnabled',
        'accept-language': 'en-US',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://discord.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://discord.com/channels/907501014914060329/907501015341858824',
        'cookie': '__dcfduid=0f52e1903dce11eca260a166ca1ce2a2; __sdcfduid=0f52e1913dce11eca260a166ca1ce2a26685cf1817e5918f525ccb544c7b38dd469403cf86d6082435cd8cbb46d620ef; __stripe_mid=b0aea78a-f66f-4067-b204-0a7ee4db6acaf58e16',
    }
        for x in names:
            data = '{"nick":"'+x+'"}'

            response = requests.patch(f'https://discord.com/api/v9/guilds/{str(ctx.guild.id)}/members/@me', headers=headers, data=data)
            await asyncio.sleep(12)
            if "retry_after" in response.text:
                kk=response.json()
                print(f"hit retry limit waiting {str(kk['retry_after'])} second(s)")
                await asyncio.sleep(int(kk["retry_after"]))


@animnick.error
async def animnick_error(ctx,error):
    await ctx.message.delete()
    embed=discord.Embed(title=":no_entry_sign: Critical Error :no_entry_sign:", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.add_field(name="example", value=f"{bot.command_prefix}animnick (text 1) (text 2) ", inline=True)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


# @bot.event
# async def on_command_error(ctx, error:commands.CommandError):
#     await ctx.message.delete()
#     embed=discord.Embed(title=":no_entry_sign: Critical Error :no_entry_sign:", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
#     embed.add_field(name="Command doesn't exist", value=f"Contact support if this is wrong", inline=True)
#     embed.set_thumbnail(url=str(config['theme']['thumbnail']))
#     embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
#     await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.event
async def on_command_error(ctx, error):
    try:
        if isinstance(error, commands.CommandNotFound):
            await ctx.message.delete()
            cmd = ctx.message.content.split()[0]
            cmd = cmd.lstrip(prefix)
            embed = discord.Embed(
                title=":no_entry_sign: Critical Error :no_entry_sign:",
                description=f"The Command **{cmd}** Does Not Exist",
                color=int(config['theme']['embed_color'].replace('#', '0x'), 0)
            )
            embed.set_thumbnail(url=str(config['theme']['thumbnail']))
            embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
            await ctx.send(embed=embed, delete_after=("30"))
            print(Fore.RED+f"[ERROR] invalid command used {cmd}"+Fore.RESET)
        else:
            pass
    except:
        pass


@yiff.error
async def yiff_error(ctx,error):
    await ctx.message.delete()
    embed=discord.Embed(title=":no_entry_sign: Critical Error :no_entry_sign:", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.add_field(name="Uh Oh", value=f"something broke", inline=True)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@furry.error
async def furry_error(ctx,error):
    await ctx.message.delete()
    embed=discord.Embed(title=":no_entry_sign: Critical Error :no_entry_sign:", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.add_field(name="Uh Oh", value=f"something broke", inline=True)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@femboy.error
async def femboy_error(ctx,error):
    await ctx.message.delete()
    embed=discord.Embed(title=":no_entry_sign: Critical Error :no_entry_sign:", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.add_field(name="Uh Oh", value=f"something broke", inline=True)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@rgbrole.error
async def rgbrole_error(ctx,error):
    await ctx.message.delete()
    embed=discord.Embed(title=":no_entry_sign: Critical Error :no_entry_sign:", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.add_field(name="example:", value=f"```{bot.command_prefix}rgbrole (@role)```", inline=False)
    embed.add_field(name="Info:", value="```You must do this in a server```", inline=True)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@sinfo.error
async def sinfo_error(ctx,error):
    await ctx.message.delete()
    embed=discord.Embed(title=":no_entry_sign: Critical Error :no_entry_sign:", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.add_field(name="Command Error:", value="```YOU CAN ONLY DO THIS IN A SERVER```", inline=True)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@massgc.error
async def massgc_error(ctx,error):
    await ctx.message.delete()
    embed=discord.Embed(title=":no_entry_sign: Critical Error :no_entry_sign:", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.add_field(name="example", value=f"{bot.command_prefix}massgc (victim ID) (times) ", inline=True)
    embed.add_field(name="info", value=f"send the command in the persons dms you **DONT** want to massgc", inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command(name="restart", aliases=["shutdown","botgobrrr","goaway"])
async def restart(ctx):
    await ctx.message.delete()
    if not is_me(ctx.message):
        return
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="```Restarting```", value=f"```CotraUI Is Restarting...```", inline=False)
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print("restarting bot")
    print(Fore.CYAN+"[Command] <>restarting<>"+Fore.RESET)
    restart_bot()


@bot.command(aliases=['youtube','yt'])
async def _youtube(ctx, *, search):
    await ctx.message.delete()
    author=ctx.message.author
    guild=ctx.guild
    query_string = urllib.parse.urlencode({'search_query': search})
    html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_content= html_content.read().decode()
    search_results = re.findall(r'\/watch\?v=\w+', search_content)
    #print(search_results)
    await ctx.send(f'{author.mention} result:\n https://www.youtube.com' + search_results[0])



@bot.command('tts')
async def tts(ctx, *, text):
    await ctx.message.delete()
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save(f"{os.getcwd()}/tts.mp3")
    await ctx.send(file=discord.File(f'{os.getcwd()}/tts.mp3'))
    await asyncio.sleep(5)
    os.remove(f'{os.getcwd()}/tts.mp3')

@bot.command()
async def colorfulem(ctx,times): 
    await ctx.message.delete()
    cols = [0x32a852, 0x3296a8, 0xb700ff, 0x9232a8, 0xa8326f, 0xf25207, 0x3efa00, 0xfa0000,0xff0000, 0xe07878, 0xf4ff00, 0x059700, 0x00afdd, 0x0800dd, 0x6800dd]
    embed = discord.Embed(
        title = "colorful embed",
        color = random.choice(cols)
    )

    msg = await ctx.send(embed=embed)

    for x in range(int(times)):
        embed = discord.Embed(
            title = "Colorful embed",
            color = random.choice(cols)
        )
        await asyncio.sleep(1.5)
        await msg.edit(embed=embed)


@bot.command()
async def ban(ctx, *, user: discord.Member):
    await ctx.message.delete()
    await user.ban()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name=f"{user.name} has been banned", value="Enjoy death kid")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command()
async def getpfp(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_image(url=(member.avatar_url))
    embed.add_field(name=f"{member.display_name}'s Pfp", value=":flushed:")
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command(name='unban')
async def _unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name=f"{user.name} has been unbanned", value="Don't be a retard next time")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def kick(ctx,*, user: discord.Member):
   await ctx.message.delete()
   await user.kick()
   embed=discord.Embed(title=(f'{user.name} was kicked'), description="Dont come back retard", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
   embed.set_thumbnail(url=str(config['theme']['thumbnail']))
   embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
   await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def pp(ctx, user: discord.Member = None):
    await ctx.message.delete()
    if user == None:
        user = ctx.author
    else:
        user = ctx.message.mentions[0]
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    embed = discord.Embed(title=f"{user.display_name}'s Dick size", description=f"8{dong}D",color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])



@bot.command()
async def yoink(ctx): 
    await ctx.message.delete()
    wow = await bot.create_guild(f'{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in bot.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
            except:
                break

@bot.command()
async def niko(ctx):
    await ctx.message.delete()
    if not is_me(ctx.message):
        return
    embed=discord.Embed(title="Nikocado Avocado", description="enjoy some nikocado", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed)
    await ctx.send("https://cdn.discordapp.com/attachments/867153594142687302/872394286564540486/5bd354ffd5f3baf0e9fa45d2f25b5a78a04c3100.mp4")


@bot.command()
async def info(ctx,):
    await ctx.message.delete()
    totalcommands = len(bot.commands)
    if not is_me(ctx.message):
        return
    
    embed=discord.Embed(title="CotraUI Info", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.add_field(name="Total Commands:", value=f"```{totalcommands}```", inline=True)
    embed.add_field(name="Prefix:", value=f'```{bot.command_prefix}```', inline=True)
    embed.add_field(name="Version:", value=f'```{version}```', inline=True)
    embed.add_field(name="Theme:", value="```"+str(config['theme']['name'])+"```", inline=True)
    embed.description = f"```Developed By cotra#0001```\n"
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


# @.command()
# async def devbuild(ctx,):
#     await ctx.message.delete()
#     totalcommands = len(bot.commands)
#     if not is_me(ctx.message):
#         return
    
#     embed=discord.Embed(title="CotraUI Info", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
#     embed.add_field(name="Total Commands:", value=f"```{cmds}```", inline=True)
#     embed.add_field(name="Prefix:", value=f'```{bot.command_prefix}```', inline=True)
#     embed.add_field(name="Version:", value=f'```{dev}```', inline=True)
#     embed.add_field(name="Theme:", value="```"+str(config['theme']['name'])+"```", inline=True)
#     embed.description = f"```Developed By cotra#0001```\n"
#     embed.set_thumbnail(url=str(config['theme']['thumbnail']))
#     embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
#     await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def tkninfo(ctx, *, token):
        await ctx.message.delete()
        request = requests.get("https://discord.com/api/users/@me", headers={"Authorization": token})
        if request.status_code == 200:
            request = request.json()
            id = request["id"]
            username = request["username"]
            discriminator = request["discriminator"]
            avatar = avatarUrl(id, request["avatar"])
            publicflags = request["public_flags"]
            bio = request["bio"]
            nitro = ""
            if "premium_type" in request:
                if request["premium_type"] == 0:
                    nitro = "None"
                elif request["premium_type"] == 1:
                    nitro = "Classic Nitro"
                elif request["premium_type"] == 2:
                    nitro = "Nitro"
            else:
                nitro = "None"
            email = request["email"]
            phone = request["phone"]
            if bio == "":
                bio = " "
            
            embed = discord.Embed(title="Token info:", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at,)
            embed.add_field(name="Username", value="```" + str(username) + "```",inline=False)
    
            embed.add_field(name="Email", value="```" + str(email) + "```" ,inline=False)
            embed.add_field(name="Discriminator", value="```" + str(discriminator) + "```",inline=False)
            embed.add_field(name="User ID", value="```" + str(id) + "```" ,inline=False)
            embed.add_field(name="Bio", value="```" + str(bio) + "```", inline=False)
            embed.set_thumbnail(url=str(config['theme']['thumbnail']))
            embed.add_field(name="Nitro", value="```" + str(nitro) + "```",inline=False)
            embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
            await ctx.send(embed=embed, delete_after=config['deletetime'])
        else:
            await ctx.send("oops bad token kid") 


@bot.command()
async def encrypt(ctx, *, text: str):
    await ctx.message.delete()
    to_morse = { 
        "a" : "ɗรٱคร",
        "b" : "ɗรٱค",
        "c" : "รɗﻉ",
        "d" : "Շร๔є",
        "e" : "ፕነዕቿ",
        "f" : "丂d乇",
        "g" : "Շรɗﻉ",
        "h" : "ዪዐጌረዐሸሠሁነቿፕ5",
        "i" : "ዪዐጌረዐሸሠሁነቿፕ",
        "j" : "ዪዐጌረዐሸሠሁነቿ",
        "k" : "ዪዐጌረዐሸሠሁነ",
        "l" : "ዪዐጌረዐሸሠሁነቿ5",
        "m" : "ዪዐጌረዐሸሠሁዐ",
        "n" : "ዪዐጌረዐሸሠሁ",
        "o" : "ዪዐጌረዐሁነቿፕ5",
        "p" : "ዪዐጌረሸሠሁነቿፕ5",
        "q" : "ዪዐረዐሸሠሁነቿፕ5",
        "r" : "ዪዐጌረዐሸሠሁነቿ?5",
        "s" : "ዪዐጌረዐሠሁነቿፕ5",
        "t" : "ዐጌረዐሸሠሁነቿፕ5",
        "u" : "ҀФГЯД",
        "v" : "ҀФГЯ",
        "w" : "ҀФr",
        "x" : "ҀФГ",
        "y" : "ℜ𝔄",
        "z" : "ｷ乇ｲg",
        "1" : ".คŦгเςค",
        "2" : ".. ልቻዪጎርል",
        "3" : "ₐfᵣᵢcₐ",
        "4" : "丂 乃o尺刀",
        "5" : "ﾶﾘ ﾶoﾶ",
        "6" : "🇲🇾 🇲🇴🇲",
        "7" : "cﾑ",
        "8" : "Ў",
        "9" : "𝓶𝓸𝓶",
        "0" : "-----",
        "-" : "ልዪፕዐር",
        "." : "ↄoTᴙA",
        "?" : "£$R%T:$£PT",
        "!" : "𝐜𝐨𝐭𝐫𝐚",
        "/" : "???????",
        "£" : "ȼøŧɍȺ",
        "$" : "ᶜᵒᵗʳᵃ",
        "," : "ዪልኗክልዪዐጕ",
        "_" : " ",
        ":" : "???!??!sped!?!?!",
        "#" : "???!??!cotra!?!?!"
    }
    cipher = ''
    for letter in text:
        if letter != ' ':
            cipher += to_morse[letter.lower()] + ' '
        else:
            cipher += ' '
    embed=discord.Embed(title=str(config['theme']['title']),description=(cipher), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="```Only CotraUI users can decode this```", value="try it ;)")
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def decrypt(ctx, *, text: str):
    await ctx.message.delete()
    to_morse = { 
        "a" : "ɗรٱคร",
        "b" : "ɗรٱค",
        "c" : "รɗﻉ",
        "d" : "Շร๔є",
        "e" : "ፕነዕቿ",
        "f" : "丂d乇",
        "g" : "Շรɗﻉ",
        "h" : "ዪዐጌረዐሸሠሁነቿፕ5",
        "i" : "ዪዐጌረዐሸሠሁነቿፕ",
        "j" : "ዪዐጌረዐሸሠሁነቿ",
        "k" : "ዪዐጌረዐሸሠሁነ",
        "l" : "ዪዐጌረዐሸሠሁነቿ5",
        "m" : "ዪዐጌረዐሸሠሁዐ",
        "n" : "ዪዐጌረዐሸሠሁ",
        "o" : "ዪዐጌረዐሁነቿፕ5",
        "p" : "ዪዐጌረሸሠሁነቿፕ5",
        "q" : "ዪዐረዐሸሠሁነቿፕ5",
        "r" : "ዪዐጌረዐሸሠሁነቿ?5",
        "s" : "ዪዐጌረዐሠሁነቿፕ5",
        "t" : "ዐጌረዐሸሠሁነቿፕ5",
        "u" : "ҀФГЯД",
        "v" : "ҀФГЯ",
        "w" : "ҀФr",
        "x" : "ҀФГ",
        "y" : "ℜ𝔄",
        "z" : "ｷ乇ｲg",
        "1" : ".คŦгเςค",
        "2" : ".. ልቻዪጎርል",
        "3" : "ₐfᵣᵢcₐ",
        "4" : "丂 乃o尺刀",
        "5" : "ﾶﾘ ﾶoﾶ",
        "6" : "🇲🇾 🇲🇴🇲",
        "7" : "cﾑ",
        "8" : "Ў",
        "9" : "𝓶𝓸𝓶",
        "0" : "-----",
        "-" : "ልዪፕዐር",
        "." : "ↄoTᴙA",
        "?" : "£$R%T:$£PT",
        "!" : "𝐜𝐨𝐭𝐫𝐚",
        "/" : "???????",
        "£" : "ȼøŧɍȺ",
        "$" : "ᶜᵒᵗʳᵃ",
        "," : "ዪልኗክልዪዐጕ",
        "_" : " ",
        ":" : "???!??!sped!?!?!",
        "#" : "???!??!cotra!?!?!"
    }
    text += ' '
    decipher = ''
    cipher = ''
    for letter in text:
        if letter != ' ':
            i = 0
            cipher += letter
        else:
            i += 1 
            if i == 2:
                decipher += ' '
            else:
                decipher += list(to_morse.keys())[list(to_morse.values()).index(cipher)]
                cipher = ''
    embed=discord.Embed(title=str(config['theme']['title']),description=(decipher), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="```Only CotraUI users can decode this```", value="try it ;)")
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def gp(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]

@bot.command()
async def discum(ctx,):
    await ctx.message.delete()
    if not is_me(ctx.message):
        return
    embed=discord.Embed(title="Discum is poo", description="", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.set_image(url="https://cdn.discordapp.com/attachments/900114227862323210/913448547574251621/poop-emoji-png-transparent-background-image-free-png-templates-poop-emoji-transparent-1000_824.png")
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@bot.command()
async def blm(ctx):
    await ctx.message.delete()
    if not is_me(ctx.message):
        return
    embed=discord.Embed(title="Black Lives Matter", description="Not really", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.set_image(url="https://cdn.discordapp.com/attachments/900098205738475551/913912873019924540/aprilfoolsdaymsn.jpg")
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def allcmds(ctx):
    await ctx.send(f"{prefix}general", delete_after=0.1)
    asyncio.sleep(2)
    await ctx.send(f"{prefix}fun", delete_after=0.1)
    asyncio.sleep(2)
    await ctx.send(f"{prefix}memes", delete_after=0.1)
    asyncio.sleep(2)
    await ctx.send(f"{prefix}images", delete_after=0.1)
    asyncio.sleep(2)
    await ctx.send(f"{prefix}nsfw", delete_after=0.1)
    asyncio.sleep(2)
    await ctx.send(f"{prefix}server", delete_after=0.1)
    asyncio.sleep(2)
    await ctx.send(f"{prefix}text", delete_after=0.1)
    asyncio.sleep(2)
    await ctx.send(f"{prefix}token", delete_after=0.1)
    asyncio.sleep(2)
    await ctx.send(f"{prefix}promo", delete_after=0.1)
    asyncio.sleep(2)
    await ctx.send(f"{prefix}settings", delete_after=0.1)

@bot.command()
async def spam(ctx, *, message, amount: int):
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)


@bot.command(aliases=['tokenfucker', 'disable', 'crash']) 
async def riptoken(ctx, _token): # b'\xfc' 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
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
    guild = {
        'channels': None,
        'icon': "https://cdn.discordapp.com/attachments/895394887904686100/900058818048843796/A-gift-ig.png",
        'name': "CotraUI",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }

        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break   
locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

@bot.command()
async def cactus(ctx):
    if not is_me(ctx.message):
        await ctx.message.delete()
        return
    embed=discord.Embed(title="Cactus Reselling", url="https://CactusReselling.com", description="Official Reseller", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Website", value="https://cactusreselling.com/", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/900098205738475551/914278466755653642/Cactus_web.gif")
    embed.set_image(url="https://cdn.discordapp.com/attachments/900098205738475551/913957444936429638/Cactus_banner.gif")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Cactus posted<>"+Fore.RESET)


@bot.command()
async def troop(ctx):
    if not is_me(ctx.message):
        await ctx.message.delete()
        return
    embed=discord.Embed(title="Troop keys", url="https://discord.gg/ts38Bbth", description="Official Reseller", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Discord Server:", value="https://discord.gg/ts38Bbth", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929149666510135346/929435362231726110/TroopKeys_logo_2.png")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>troop posted<>"+Fore.RESET)


@bot.command()
async def pathetic(ctx):
    if not is_me(ctx.message):
        await ctx.message.delete()
        return
    embed=discord.Embed(title="Pathetic", url="https://lamahook.xyz/", description="Official Reseller", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Discord Server:", value="https://discord.gg/QxrAEmatJ3", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/927495636570488856/929444162640691362/qtLGvat9AgETaaaS7dsjF3bGRO1xgHqaBV8Hsq6y.jpg")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>pathetic posted<>"+Fore.RESET)

@bot.command()
async def complex(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Complex Services", url="https://discord.gg/RXTf4f7bTc", description="Official Reseller", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Discord Server:", value="https://discord.gg/RXTf4f7bTc", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/920481035991527454/931920588883251260/a_65fce1f5594f03697b5ae031a37aa8c1.gif")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>complex posted<>"+Fore.RESET)

@bot.command()
async def flop(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Flops Lounge", url="https://discord.com/invite/4GzYd6AuGk", description="Official Reseller", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name="Discord Server:", value="https://discord.com/invite/4GzYd6AuGk", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/783328529043030057/a_b5deb967f3fa665485ec093abb60a003.gif?size=128")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>flop posted<>"+Fore.RESET)

@bot.command(name="ascii",  aliases=["asci","asc"])
async def ascii(ctx, *, text: str):
        if text is None:
            return
        else:
            r = requests.get(f'https://artii.herokuapp.com/make?text={urllib.parse.quote(text)}')
            rr = r.text
            try:
                await ctx.send(f'```{rr}```')
            except discord.HTTPException:
                return
            await ctx.message.delete()
def avatarUrl(id, avatar):
            url = ""
            if not str(avatar).startswith("http"):
                if str(avatar).startswith("a_"):
                    url =  f"https://cdn.discordapp.com/avatars/{id}/{avatar}.gif?size=1024"
                else:
                    url =  f"https://cdn.discordapp.com/avatars/{id}/{avatar}.png?size=1024"
@bot.command()
async def userinfo(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    embed = discord.Embed(title=str(config['theme']['title']), description=f"**INFO ABOUT: {member.display_name}**", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.add_field(name='ID', value=(member.id), inline=False)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name='Tag', value=f"#{member.discriminator}", inline=False)
    embed.add_field(name='Account Created', value=(member.created_at.strftime('%d/%m/%Y')), inline=False)
    embed.add_field(name='Bot', value=(member.bot), inline=False)
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Userinfo<>"+Fore.RESET)

@bot.command(name="rv", description="Reverses the text", usage="Reverse <text>")
async def reverse(ctx, *, text: str):
    await ctx.message.delete()
    await ctx.send(''.join(reversed(text)))


# async def uwu(ctx, member=None):
#     await ctx.message.delete()
#     if member == None:
#         member = ctx.author
#     else:
#         member = ctx.message.mentions[0]
#     r = requests.get("https://nekos.life/api/v2/img/cum")
#     res = r.json()
#     embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
#     embed.set_thumbnail(url=str(config['theme']['thumbnail']))
#     embed.add_field(name="You got uwu'd", value=f"{member.mention}")
#     embed.set_image(url=res['url'])
#     embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
#     await ctx.send(embed=embed, delete_after=config['deletetime'])
#     print(Fore.CYAN+"<>UwU<>"+Fore.RESET)
@bot.command()
async def nshout(ctx):
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="nshout is a femboy", value=f":flushed:")
    embed.set_image(url="https://cdn.discordapp.com/attachments/927495636570488856/929860390534385714/d2a5e5addccd1c9082b127fd0dca67e3.gif")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>nshout<>"+Fore.RESET)

@bot.command()
async def stickbug(ctx, member=None):
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    await ctx.message.delete()
    url = member.avatar_url_as(format="png")
    response = requests.get(f"https://nekobot.xyz/api/imagegen?type=stickbug&url={url}")
    stuff = json.loads(response.text)
    await ctx.send(stuff["message"])

@bot.command()
async def warcrimes(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="I pwomise i didnt!", value=f":flushed:")
    embed.set_image(url="https://media.discordapp.net/attachments/927495636570488856/927557846827151370/klee-genshin-impact-klee.gif")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>warcrimes<>"+Fore.RESET)

@bot.command()
async def ducking(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="dwuck dwuck uwu", value=f":flushed:")
    embed.set_image(url="https://media.discordapp.net/attachments/916823128351588382/916824513021353984/fakeduck_p.gif")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>ducking<>"+Fore.RESET)

@bot.command()
async def gay(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member=ctx.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    embed=discord.Embed(
        title="Gay",
        description=f"{member.display_name} is {random.randint(0,100)}% gay",
        color=int(config['theme']['embed_color'].replace('#', '0x'), 0)
    )
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    await ctx.send(embed=embed)

@bot.command()
async def trampoline(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="Bwoing Bwoing uwu", value=f":flushed:")
    embed.set_image(url="https://cdn.discordapp.com/attachments/927312578022092880/928423819025203290/god-i-love-trampolining-katieverse.gif")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>trampoline<>"+Fore.RESET)

@bot.command()
async def play(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="Pwease Pway with me", value=f":flushed:")
    embed.set_image(url="https://media.discordapp.net/attachments/927495636570488856/927557571802447922/klee-genshin-impact.gif")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>play<>"+Fore.RESET)

@bot.command()
async def ohno(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="oh no horny is back", value=f":flushed:")
    embed.set_image(url="https://cdn.discordapp.com/attachments/927312578022092880/928387835382349894/863823606831120426.png")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>ohno<>"+Fore.RESET)

@bot.command()
async def spfp(ctx):
    await ctx.message.delete()
    f = ctx.guild
    await ctx.send(f.icon_url)

@bot.command()
async def trump(ctx, *, msg):
    await ctx.message.delete()
    response = requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={msg}")
    stuff = json.loads(response.text)
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="The man himself", value=f":levitate:")
    embed.set_image(url=stuff["message"])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Trump has tweeted<>"+Fore.RESET)

@bot.command() 
async def loopstatus(ctx): # b'\xfc' 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': config["token"],
    }
    request = requests.Session()
    payload = {
        'theme': "darkmode",
        'locale': "en-GB",
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
        'status': "online"
    } 
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    statuses = cycle(["online", "invisible"])
    while True:
        setting = {
            'status': next(statuses)
        }

        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break 
            return

@bot.command()
async def ph(ctx, member=None, *, msg):
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    await ctx.message.delete()
    url = member.avatar_url_as(format="png")
    response = requests.get(f"https://nekobot.xyz/api/imagegen?type=phcomment&image={url}&username={member.display_name}&text={msg}")
    stuff = json.loads(response.text)
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="Caught red handed", value=f":open_hands:")
    embed.set_image(url=stuff["message"])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>searching the interwebs<>"+Fore.RESET)



@bot.command()
async def gaypfp(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def trap(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://nekobot.xyz/api/image?type=trap?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def triggered(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def passed(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/passed?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def jail(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/jail?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def wasted(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
        
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def lolice(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/lolice?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def horny(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def pixel(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member = ctx.message.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/pixelate?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
            imageData = io.BytesIO(await trigImg.read()) 
            
            await trigSession.close()
            
            await ctx.send(file=discord.File(imageData, 'CotraUI.gif'))

@bot.command()
async def clyde(ctx,*, msg):
    await ctx.message.delete()
    response = requests.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={msg}")
    stuff = json.loads(response.text)
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="Clyde is on it", value=f":flushed:")
    embed.set_image(url=stuff["message"])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>searching the interwebs<>"+Fore.RESET)

@bot.command()
async def status(ctx,*, msg):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "custom_status": {
            "text": f"{msg}"
        }
    }

    requests.patch(url, headers=headers, json=data)


@bot.command()
async def cs(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="The Revolutionary gaming", value=f":flushed:")
    embed.set_image(url="https://cdn.discordapp.com/attachments/927312578022092880/928388235590271026/914413812378112040.png")
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>UwU<>"+Fore.RESET)

@bot.command()
async def cum(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="Yummy Cummy In My Tummy", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>cum<>"+Fore.RESET)

@bot.command(pass_context=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        embed=discord.Embed(title="CotraUI", color=int(config['theme']['embed_color'].replace('#', '0x'), 0))
        embed.add_field(name="**PURGED**", value=f"`{limit}` Messages got purged by {ctx.author.mention}", inline=True)
        embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
        await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def invnick(ctx):
    await ctx.message.delete()
    try:
            name = ' ឵឵ ឵឵ ឵឵ ឵឵‎'
            await ctx.author.edit(nick=name)

    except Exception:
            return

@bot.command()
async def rick(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    embed = discord.Embed(title=f"You got RickRolled", description=f"**@{member.display_name}#{member.discriminator}**", color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_image(url="https://cdn.discordapp.com/attachments/907863077712703508/915238064811544686/rickroll-rick.gif")
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Rickroll posted<>"+Fore.RESET)


@bot.command()
async def clearconsole(ctx):
    await ctx.message.delete()
    Clear()
    await new_splash()

@bot.command()
async def aboutme(ctx, *, text):
    await ctx.message.delete()

    url = "https://discord.com/api/v9/users/@me"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "bio": text
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def pat(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="You got patted", value=f"{member.mention}")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Pat<>"+Fore.RESET)

@bot.command()
async def buy(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="CotraUI", description="```https://discord.gg/j8VV2RzKs3```", color=int(config['theme']['embed_color'].replace('#','0x'), 0), Timestamp=ctx.message.created_at)
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Posted Buying discord server<>"+Fore.RESET)

@bot.command()
async def lewdneko(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.add_field(name="You got lewd neko", value=f":flushed:")
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>lewdneko<>"+Fore.RESET)



@bot.command()
async def hideinvite(ctx, url, *, message: str='Hi'):
        await ctx.message.delete()
        await ctx.send(f'‎{message}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||‎‎||‎||‎‎||‎‎||‎‎||‎‎||{url}')

@bot.command()
async def hidelink(ctx, url, spoofed_url):
    await ctx.message.delete()
    await ctx.send(f'‎<{spoofed_url}>||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||‎‎||‎||‎‎||‎‎||‎‎||‎‎||{url}')

@bot.command()
async def kiss(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="You got kissed", value=f"{member.mention}")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>kiss<>"+Fore.RESET)

@bot.command()
async def hug(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="You got hugged", value=f"{member.mention}")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>hug<>"+Fore.RESET)


@bot.command()
async def spank(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/spank")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="You got spanked", value=f"{member.mention}")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Spank<>"+Fore.RESET)



@bot.command()
async def feed(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_image(url=res['url'])
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="You got Fed", value=f"{member.mention}")
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>feed<>"+Fore.RESET)

@bot.command()
async def slap(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="You got slapped", value=f"{member.mention}")
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>slap<>"+Fore.RESET)


@bot.command()
async def poke(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/poke")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="You got poked", value=f"{member.mention}")
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>poke<>"+Fore.RESET)

@bot.command()
async def tickle(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="You got tickled", value=f"{member.mention}")
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>tickle<>"+Fore.RESET)

@bot.command()
async def gasm(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/gasm")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)#
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="uwu", value=f":flushed:")
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>gasm<>"+Fore.RESET)

@bot.command()
async def cuddle(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="You got cuddled", value=f"{member.mention}")
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>cuddle<>"+Fore.RESET)

@bot.command()
async def baka(ctx, member=None):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
    r = requests.get("https://nekos.life/api/v2/img/baka")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="You baka!!!", value=f"{member.mention}")
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>baka<>"+Fore.RESET)

@bot.command()
async def feet(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feet")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)#
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="Enjoy some feet", value=f":flushed:")
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>feet<>"+Fore.RESET)

@bot.command()
async def wallpaper(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/wallpaper")
    res = r.json()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)#
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="Enjoy the nice wallpaper", value=f":heart:")
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+"[Command] <>Wallpaper<>"+Fore.RESET)


@bot.command()
async def dnd(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "status": "dnd"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def online(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "status": "online"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def idle(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "status": "idle"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def invisible(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "status": "invisible"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def lightmode(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "theme": "light"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def test345(ctx):
    await ctx.message.delete()


@bot.command()
async def darkmode(ctx):
    await ctx.message.delete()

    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "theme": "dark"
    }

    requests.patch(url, headers=headers, json=data)

@bot.command()
async def uwu(ctx):
    await ctx.message.delete()
    print("uwu")

@bot.command()
async def easteregg(ctx):
    await ctx.message.delete()
    print("you found the easter egg")

@bot.command()
async def shrek(ctx): ## Thanks yeet pizza :) 
    await ctx.message.delete()
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="What are ye doin in ma swamp!!", value=("""⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉"""))
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def lenny(ctx):
    await ctx.message.delete()
    await ctx.send("( ͡° ͜ʖ ͡°)")

@bot.command()
async def bold(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"**{msg}**")

@bot.command()
async def italic(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"*{msg}*")

@bot.command()
async def bolditalic(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"***{msg}***")

@bot.command()
async def underline(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"__{msg}__")

@bot.command()
async def boldunderline(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"__**{msg}**__")

@bot.command()
async def spoiler(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(f"||**{msg}**||")

@bot.command()
async def emojify(ctx, *, msg):
    dict = {
        "a": ":regional_indicator_a:",
        "b": ":regional_indicator_b:",
        "c": ":regional_indicator_c:",
        "d": ":regional_indicator_d:",
        "e": ":regional_indicator_e:",
        "f": ":regional_indicator_f:",
        "g": ":regional_indicator_g:",
        "h": ":regional_indicator_h:",
        "i": ":regional_indicator_i:",
        "j": ":regional_indicator_j:",
        "k": ":regional_indicator_k:",
        "l": ":regional_indicator_l:",
        "m": ":regional_indicator_m:",
        "n": ":regional_indicator_n:",
        "o": ":regional_indicator_o:",
        "p": ":regional_indicator_p:",
        "q": ":regional_indicator_q:",
        "r": ":regional_indicator_r:",
        "s": ":regional_indicator_s:",
        "t": ":regional_indicator_t:",
        "u": ":regional_indicator_u:",
        "v": ":regional_indicator_v:",
        "w": ":regional_indicator_w:",
        "x": ":regional_indicator_x:",
        "y": ":regional_indicator_y:",
        "z": ":regional_indicator_z:",
        " ": "    "
    }
    f = ""
    await ctx.message.delete()
    for let in msg:
        for letter in dict:
            if let == letter:
                f += dict.get(letter)
    
    await ctx.send(f)

@bot.command(pass_context=True)
async def nick(ctx,member: discord.Member, *, nick):
    await ctx.message.delete()
    if member == None:
        member = ctx.author
    else:
        member = ctx.message.mentions[0]
        await member.edit(nick=nick)
    embed=discord.Embed(title=str(config['theme']['title']), color=int(config['theme']['embed_color'].replace('#', '0x'), 0), timestamp=ctx.message.created_at)#
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    embed.add_field(name="Changed!", value=(f'Nickname was changed for {member.mention} '))
    await ctx.send(embed=embed, delete_after=config['deletetime'])
    print(Fore.CYAN+f"<>changed username<>"+Fore.RESET)

@bot.command()
async def spamchannel(ctx, ammount: int=None, *, name=None):
    await ctx.message.delete()
    if name == None:
        return await ctx.send("Specify a name")
    if ammount == None:
        return await ctx.send("Specify a ammount")
    f = 0
    while f < ammount:
        await ctx.guild.create_text_channel(name)
        f += 1

@bot.command(name="8ball")
async def _8ball(ctx, *, question=None):
    if question==None:
        return await ctx.send("You didnt say a question")
    await ctx.message.delete()
    answers = ["It is certain.", "It is decidedly so.", "Without a doubt", "Yes definitely.", "You may rely on it.","As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy try again.","Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.","Don\'t count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
    embed=discord.Embed(
        title="8 Ball",
        description=f"Question: {question}\n\nAnswer: {random.choice(answers)}",
        color=int(config['theme']['embed_color'].replace('#', '0x'), 0)
    )
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def simp(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member=ctx.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    embed=discord.Embed(
        title="Simprate",
        description=f"{member.display_name} is {random.randint(0,100)}% simp",
        color=int(config['theme']['embed_color'].replace('#', '0x'), 0)
    )
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])

@bot.command()
async def cute(ctx, member=None):
    await ctx.message.delete()
    if member==None:
        member=ctx.author
    else:
        member = ctx.message.mentions[0]
        member = await bot.fetch_user(int(member.id))
    embed=discord.Embed(
        title="Cute",
        description=f"{member.display_name} is {random.randint(0,100)}% cute",
        color=int(config['theme']['embed_color'].replace('#', '0x'), 0)
    )
    embed.set_thumbnail(url=str(config['theme']['thumbnail']))
    embed.set_footer(text=config['theme']['footer_text'], icon_url=config['theme']['footer_img'])
    await ctx.send(embed=embed, delete_after=config['deletetime'])


@tasks.loop(seconds=15)
async def clock(text):
    hour = datetime.datetime.now().strftime("%H")
    hour = int(hour)
    minute = datetime.datetime.now().strftime("%M")
    minute = int(minute)
    if hour >= 12:
        time = f"{hour-12}:{minute}PM"
    else:
        time = f"{hour}:{minute}AM"
    data = {"custom_status": {"text": f"{time} {text}", "emoji_name": "🕰️"}}
    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]
    requests.patch(url, headers=headers, json=data)

@bot.command()
async def clockon(ctx, *, text: str=None):
    await ctx.message.delete()
    if not text==None:
        clock.start(text)
    else:
        clock.start("")

@bot.command()
async def clockoff(ctx):
    await ctx.message.delete()
    clock.stop()
    url = "https://discordapp.com/api/v9/users/@me/settings"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    headers["Authorization"] = config["token"]

    data = {
        "custom_status": NULL
    }

    requests.patch(url, headers=headers, json=data)



# bot run #
    
# bot.run(config["token"], bot=False)
def Init():
    with open('config.json', encoding="utf-8") as f:
        config = json.load(f)
    token = config.get('token')
    try:
        bot.run(token, bot=False, reconnect=True)
    except discord.errors.LoginFailure:
        input(f"{Fore.RED}[SYSTEM] TOKEN IS INVALID CHECK CONFIG"+Fore.RESET)
        sys.exit
        python = sys.executable
        os.execl(python, python, * sys.argv)
Init()