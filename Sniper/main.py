import re
import sys
import time
import httpx
import ctypes
import asyncio
import pwinput
import requests
import threading

from discord.ext import commands
from time import localtime, strftime

import discord
from discord import *

# /////////////////////////////////////////////////////////////////////////////
# Special Imports

from jsonhandler import *

# /////////////////////////////////////////////////////////////////////////////
# Variables

logo = f"""         *                        o              +                 *                 .
              O                     .              .                      .                   *                 .
    *                 .                 ██╗     ██╗   ██╗███╗  ██╗ █████╗    .-.,="``"=. +            |     o
        .                     *         ██║     ██║   ██║████╗ ██║██╔══██╗   `=/_       \           - o -           .
                                        ██║     ██║   ██║██╔██╗██║███████║    |  '=._    |      .     |         *
  o                |              +     ██║     ██║   ██║██║╚████║██╔══██║  *  \     `=./`,                           +
           *     - o -                  ███████╗╚██████╔╝██║ ╚███║██║  ██║      `=.__.=` `=`             O
 .                 |        .           ╚══════╝ ╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝             *                            *
                                     .                      o                    .                  +          .
"""

if JsonHandler("config.json").read_value("enabled", "caching"):
    bot = commands.Bot(command_prefix='.', self_bot=True, guild_subscription_options=GuildSubscriptionOptions.default())
else:
    bot = commands.Bot(command_prefix='.', self_bot=True, guild_subscription_options=GuildSubscriptionOptions.off())

user_token = ""
nitro_cooldown = []

attempts = 0
redeemed = 0

# /////////////////////////////////////////////////////////////////////////////
# Functions

clear = lambda: os.system('cls')
title = lambda text: ctypes.windll.kernel32.SetConsoleTitleW(text)

def purple_blue(text):
    os.system(""); faded = ""
    red = 137
    green = 142
    blue = 255
    for line in text.splitlines():
        faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
        if not green == 0:
            green -= 5
            if green < 0:
                green = 0
        if not red == 255:
            red += 5
            if red > 255:
                red = 255
    return faded

def purple(text):
    os.system(""); faded = ""; down = False
    for line in text.splitlines():
        red = 137
        green = 142
        blue = 255
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
            if down:
                green += 3
            else:
                green -= 3
            if green > 254:
                green = 255
                down = True
            elif green < 1:
                green = 30
                down = False
            faded += f"\033[38;2;{red};{green};{blue}m{character}\033[0m"
    return faded


class prints:
    error_color = '\033[38;2;225;9;89m'
    reset = "\033[0m"
    
    def message(text: str):
        """Prints a message log."""
        return print(f'{strftime("%H:%M", localtime())} | {purple("Message")} | {text}')

    def sniper(text: str):
        """Prints a sniper log."""
        return print(f'{strftime("%H:%M", localtime())} | {purple("Sniper ")} | {text}')

    def event(text: str):
        """Prints a event log."""
        return print(f'{strftime("%H:%M", localtime())} | {purple(" Event ")} | {text}')

    def selfbot(text: str):
        """Prints a selfbot log."""
        return print(f'{strftime("%H:%M", localtime())} | {purple("Selfbot")} | {text}')

    def error(text: str):
        """Prints a error log."""
        return print(f'{strftime("%H:%M", localtime())} | {prints.error_color} Error {prints.reset} | {text}')

    def input(text: str):
        """Prints an input."""
        var = input(f'{strftime("%H:%M", localtime())} | {purple(" Input ")} | {text}: ')
        return var

    def password(text: str):
        """Prints a password input. Masked with `*`"""
        password = pwinput.pwinput(prompt=f'{strftime("%H:%M", localtime())} | {purple(" Input ")} | {text}: ', mask='*')
        return password

# /////////////////////////////////////////////////////////////////////////////
# Main

clear()
print(purple_blue(logo))

# /////////////////////////////////////////////////////////////////////////////
# Client Threads

client = discord.Client()

async def bot_async_start():
    await client.start("")

def bot_loop_start(loop):
    loop.run_forever()

def bot_start():
    print("3")
    if sys.platform != 'win32':
        asyncio.get_child_watcher()
    print("4")
    loop = asyncio.get_event_loop()
    loop.create_task(bot_async_start())
    bot_thread = threading.Thread(target=bot_loop_start, args=(loop,))
    bot_thread.start()

async def init(token):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'authorization': token}
    r = requests.get("https://discordapp.com/api/v9/users/@me", headers=headers).json()
    await client.start(token)

async def start(token):
    task = asyncio.create_task(init(token))
    await task

@client.event
async def on_message(message):
    sniped_time = time.time()
    if message.author == client.user:
        return
    try:
        global nitro_cooldown
        global redeemed
        global attempts
        if 'discord.gift/' in message.content.lower():
            elapsed_snipe = '%.4fs' % (time.time() - sniped_time)
            code = re.search("discord.gift/(.*)", message.content).group(1)
            if len(code) >= 16:
                code = code[:16]
                async with httpx.AsyncClient() as cli:
                    start_time = time.time()
                    result = await cli.post(
                        f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem',
                        json={'channel_id': message.channel.id},
                        headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
                    elapsed = '%.3fs' % (time.time() - start_time)
                if 'nitro' in str(result.content):
                    status = 'Nitro successfully redeemed'
                    redeemed += 1
                    title(f"{attempts} Attempts | {redeemed} Redeemed | Luna Nitro Sniper")
                elif 'This gift has been redeemed already' in str(result.content):
                    status = 'Has been redeemed already'
                else:
                    status = 'Unknown gift code'

                if nitro_cooldown.count(code) == 0:
                    nitro_cooldown.append(code)

                    print()
                    prints.sniper(purple(status))
                    prints.sniper(f"Account | {purple(client.user.name)}#{purple(client.user.discriminator)}")
                    prints.sniper(f"Server  | {purple(f'{message.guild}')}")
                    prints.sniper(f"Channel | {purple(f'{message.channel}')}")
                    prints.sniper(f"Author  | {purple(f'{message.author}')}")
                    prints.sniper(f"Code    | {purple(f'{code}')}")
                    prints.sniper(purple('Elapsed Times'))
                    prints.sniper(f"Sniped  | {purple(f'{elapsed_snipe}')}")
                    prints.sniper(f"Request | {purple(f'{elapsed}')}")
                    print()

                    attempts += 1
                    title(f"{attempts} Attempts | {redeemed} Redeemed | Luna Nitro Sniper")

                    # if files.json("Luna/notifications/toasts.json", "nitro", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
                    #     notify.toast(message=f"{status}\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
                    # if files.json("Luna/webhooks/webhooks.json", "nitro", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.nitro_url() == "webhook-url-here":
                    #     notify.webhook(url=webhook.nitro_url(), name="nitro", description=f"{status}\nServer » {message.guild}\nChannel » {message.channel}\nAuthor » {message.author}\nCode » {code}\nElapsed Times\nSniped » {elapsed_snipe}\nRequest » {elapsed}")

        elif 'discord.com/gifts' in message.content.lower():
            elapsed_snipe = '%.4fs' % (time.time() - sniped_time)
            code = re.search("discord.com/gifts/(.*)", message.content).group(1)
            if len(code) >= 16:
                async with httpx.AsyncClient() as cli:
                    start_time = time.time()
                    result = await cli.post(
                        f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem',
                        json={'channel_id': message.channel.id},
                        headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
                    elapsed = '%.3fs' % (time.time() - start_time)
                if 'nitro' in str(result.content):
                    status = 'Nitro successfully redeemed'
                    redeemed += 1
                    title(f"{attempts} Attempts | {redeemed} Redeemed | Luna Nitro Sniper")
                elif 'This gift has been redeemed already' in str(result.content):
                    status = 'Has been redeemed already'
                else:
                    status = 'Unknown gift code'

                if nitro_cooldown.count(code) == 0:
                    nitro_cooldown.append(code)

                    print()
                    prints.sniper(purple(status))
                    prints.sniper(f"Account | {purple(client.user.name)}#{purple(client.user.discriminator)}")
                    prints.sniper(f"Server  | {purple(f'{message.guild}')}")
                    prints.sniper(f"Channel | {purple(f'{message.channel}')}")
                    prints.sniper(f"Author  | {purple(f'{message.author}')}")
                    prints.sniper(f"Code    | {purple(f'{code}')}")
                    prints.sniper(purple('Elapsed Times'))
                    prints.sniper(f"Sniped  | {purple(f'{elapsed_snipe}')}")
                    prints.sniper(f"Request | {purple(f'{elapsed}')}")
                    print()

                    attempts += 1
                    title(f"{attempts} Attempts | {redeemed} Redeemed | Luna Nitro Sniper")

                    # if files.json("Luna/notifications/toasts.json", "nitro", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
                    #     notify.toast(message=f"{status}\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
                    # if files.json("Luna/webhooks/webhooks.json", "nitro", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.nitro_url() == "webhook-url-here":
                    #     notify.webhook(url=webhook.nitro_url(), name="nitro", description=f"{status}\nServer » {message.guild}\nChannel » {message.channel}\nAuthor » {message.author}\nCode » {code}\nElapsed Times\nSniped » {elapsed_snipe}\nRequest » {elapsed}")
    except Exception as e:
        prints.error("{}".format(e))

@client.event
async def on_ready():
    prints.message(f"Logged into {purple(f'{client.user.name}')}#{purple(f'{client.user.discriminator}')} | {purple(f'{len(client.guilds)}')} Guilds | {purple(f'{len(client.user.friends)}')} Friends")

# /////////////////////////////////////////////////////////////////////////////
# Bot

@bot.event
async def on_ready():
    clear()
    print(purple_blue(logo))
    print("Luna Nitro Sniper".center(os.get_terminal_size().columns))
    print()
    print(f"                                         {purple(f'{bot.user.name}')}#{purple(f'{bot.user.discriminator}')} | {purple(f'{len(bot.guilds)}')} Guilds | {purple(f'{len(bot.user.friends)}')} Friends\n")
    print(f'═' * os.get_terminal_size().columns)
    print()
    prints.event("Awaiting Nitro Codes...")
    title(f"{attempts} Attempts | {redeemed} Redeemed | Luna Nitro Sniper")
    # try:
    #     for token in JsonHandler("config.json").read_value("alt_tokens", "tokens"):
    #         if not token == "":
    #             print("1")
    #             # start(token)
    #             bot_start()
    #             print("2")
    #             await asyncio.sleep(1)
    # except Exception as e:
    #     prints.error(f"{e}")
    #     pass

@bot.event
async def on_message(message):
    sniped_start_time = time.time()
    if message.author == bot.user:
        return
    try:
        global nitro_cooldown
        global redeemed
        global attempts
        if 'discord.gift/' in message.content.lower():
            elapsed_snipe = '%.4fs' % (time.time() - sniped_start_time)
            code = re.search("discord.gift/(.*)", message.content).group(1)
            if len(code) >= 16:
                code = code[:16]
                async with httpx.AsyncClient() as client:
                    start_time = time.time()
                    result = await client.post(
                        f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem',
                        json={'channel_id': message.channel.id},
                        headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
                    elapsed = '%.3fs' % (time.time() - start_time)
                if 'nitro' in str(result.content):
                    status = 'Nitro successfully redeemed'
                    redeemed += 1
                    title(f"{attempts} Attempts | {redeemed} Redeemed | Luna Nitro Sniper")
                elif 'This gift has been redeemed already' in str(result.content):
                    status = 'Has been redeemed already'
                else:
                    status = 'Unknown gift code'

                if nitro_cooldown.count(code) == 0:
                    nitro_cooldown.append(code)

                    print()
                    prints.sniper(purple(status))
                    prints.sniper(f"Account | {purple(bot.user.name)}#{purple(bot.user.discriminator)}")
                    prints.sniper(f"Server  | {purple(f'{message.guild}')}")
                    prints.sniper(f"Channel | {purple(f'{message.channel}')}")
                    prints.sniper(f"Author  | {purple(f'{message.author}')}")
                    prints.sniper(f"Code    | {purple(f'{code}')}")
                    prints.sniper(purple('Elapsed Times'))
                    prints.sniper(f"Sniped  | {purple(f'{elapsed_snipe}')}")
                    prints.sniper(f"Request | {purple(f'{elapsed}')}")
                    print()

                    attempts += 1
                    title(f"{attempts} Attempts | {redeemed} Redeemed | Luna Nitro Sniper")

                    # if files.json("Luna/notifications/toasts.json", "nitro", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
                    #     notify.toast(message=f"{status}\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
                    # if files.json("Luna/webhooks/webhooks.json", "nitro", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.nitro_url() == "webhook-url-here":
                    #     notify.webhook(url=webhook.nitro_url(), name="nitro", description=f"{status}\nServer » {message.guild}\nChannel » {message.channel}\nAuthor » {message.author}\nCode » {code}\nElapsed Times\nSniped » {elapsed_snipe}\nRequest » {elapsed}")

        elif 'discord.com/gifts' in message.content.lower():
            elapsed_snipe = '%.4fs' % (time.time() - sniped_start_time)
            code = re.search("discord.com/gifts/(.*)", message.content).group(1)
            if len(code) >= 16:
                async with httpx.AsyncClient() as client:
                    start_time = time.time()
                    result = await client.post(
                        f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem',
                        json={'channel_id': message.channel.id},
                        headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
                    elapsed = '%.3fs' % (time.time() - start_time)
                if 'nitro' in str(result.content):
                    status = 'Nitro successfully redeemed'
                    redeemed += 1
                    title(f"{attempts} Attempts | {redeemed} Redeemed | Luna Nitro Sniper")
                elif 'This gift has been redeemed already' in str(result.content):
                    status = 'Has been redeemed already'
                else:
                    status = 'Unknown gift code'

                if nitro_cooldown.count(code) == 0:
                    nitro_cooldown.append(code)

                    print()
                    prints.sniper(purple(status))
                    prints.sniper(f"Account | {purple(bot.user.name)}#{purple(bot.user.discriminator)}")
                    prints.sniper(f"Server  | {purple(f'{message.guild}')}")
                    prints.sniper(f"Channel | {purple(f'{message.channel}')}")
                    prints.sniper(f"Author  | {purple(f'{message.author}')}")
                    prints.sniper(f"Code    | {purple(f'{code}')}")
                    prints.sniper(purple('Elapsed Times'))
                    prints.sniper(f"Sniped  | {purple(f'{elapsed_snipe}')}")
                    prints.sniper(f"Request | {purple(f'{elapsed}')}")
                    print()

                    attempts += 1
                    title(f"{attempts} Attempts | {redeemed} Redeemed | Luna Nitro Sniper")

                    # if files.json("Luna/notifications/toasts.json", "nitro", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
                    #     notify.toast(message=f"{status}\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
                    # if files.json("Luna/webhooks/webhooks.json", "nitro", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.nitro_url() == "webhook-url-here":
                    #     notify.webhook(url=webhook.nitro_url(), name="nitro", description=f"{status}\nServer » {message.guild}\nChannel » {message.channel}\nAuthor » {message.author}\nCode » {code}\nElapsed Times\nSniped » {elapsed_snipe}\nRequest » {elapsed}")
    except Exception as e:
        prints.error("{}".format(e))

# /////////////////////////////////////////////////////////////////////////////
# Bot Run

def bot_login():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Content-Type': 'application/json',
            'authorization': JsonHandler("config.json").read_value("main_token", "tokens")}
        r = requests.get("https://discordapp.com/api/v9/users/@me", headers=headers).json()
        prints.event(f"Logging into {purple(r['username'])}#{purple(r['discriminator'])}...")
        if JsonHandler("config.json").read_value("enabled", "caching"):
            prints.message("Caching enabled, login will take longer.")
        global user_token
        user_token = JsonHandler("config.json").read_value("main_token", "tokens")
        bot.run(JsonHandler("config.json").read_value("main_token", "tokens"))
    except Exception as e:
        prints.error("{}".format(e))

# /////////////////////////////////////////////////////////////////////////////
# Initialize

bot_login()

