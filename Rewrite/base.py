import aiohttp
import asyncio
import ctypes
import datetime
import json
import os
import platform
import playsound
import pypresence
import random
import re
import requests
import shutil
import sys
import time
import traceback
import winreg
import urllib

import discord
from discord import GuildSubscriptionOptions

from discord.ext import commands, tasks
from pystyle import Center, Colorate, Colors
from sys import exit
from typing import Any, Dict, List, Optional, Tuple, Union
from win10toast import ToastNotifier


class data_directory:
    config = "config.json"
    discord = "discord.json"
    data_folder = "data/"


class file_directory:
    scripts_folder = f"{data_directory.data_folder}/scripts/"
    images_folder = f"{data_directory.data_folder}/images/"
    logging_folder = f"{data_directory.data_folder}/logging/"
    settings_folder = f"{data_directory.data_folder}/settings/"
    languages_folder = f"{data_directory.data_folder}/languages/"
    themes_folder = f"{data_directory.data_folder}/themes/"
    sniper_folder = f"{data_directory.data_folder}/sniper/"
    notifications_folder = f"{data_directory.data_folder}/notifications/"
    webhooks_folder = f"{data_directory.data_folder}/webhooks/"
    dumping_folder = f"{data_directory.data_folder}/dumping/"
    misc_folder = f"{data_directory.data_folder}/misc/"
    animations_folder = f"{data_directory.data_folder}/animations/"
    backups_folder = f"{data_directory.data_folder}/backups/"
    custom_status_folder = f"{data_directory.data_folder}/custom_status/"

    rich_presence_config = f"{data_directory.data_folder}/rich_presence.json"


class sub_directories:
    logo_file = f"{file_directory.images_folder}/luna.ico"
    invisible_file = f"{file_directory.images_folder}/invisible.png"
    nitro_sniper_config = f"{file_directory.sniper_folder}/nitro_sniper.json"
    giveaway_joiner_config = f"{file_directory.sniper_folder}/giveaway_joiner.json"
    privnote_sniper_config = f"{file_directory.sniper_folder}/privnote_sniper.json"
    toasts_config = f"{file_directory.notifications_folder}/toasts.json"
    webhook_config = f"{file_directory.webhooks_folder}/webhooks.json"


class luna:
    start_time = time.time()

    class json:
        class discord:
            __path__ = data_directory.discord
            token = ("token", "", __path__)
            password = ("password", "", __path__)

        class config:
            __path__ = data_directory.config
            prefix = ("prefix", ".", __path__)
            message_mode = ("message_mode", 1, __path__)
            risk_mode = ("risk_mode", "off", __path__)
            error_log = ("error_log", "message", __path__)
            delete_timer = ("delete_timer", 45, __path__)
            theme = ("theme", "default", __path__)
            startup_status = ("startup_status", "online", __path__)
            afk_message = ("afk_message", "I am not here right now, message me later.", __path__)
            stream_url = ("stream_url", "https://www.youtube.com/watch?v=dQw4w9WgXcQ", __path__)

        class theme:
            title = ("title", "Luna")
            footer = ("footer", "www.team-luna.org")
            description = ("description", True)

        class rich_presence:
            __path__ = file_directory.rich_presence_config
            rich_presence_enabled = ("rich_presence_enabled", True, __path__)
            application_id = ("application_id", "", __path__)
            state = ("state", "", __path__)
            details = ("details", "", __path__)
            large_image = ("large_image", "", __path__)
            large_text = ("large_text", "", __path__)
            small_image = ("small_image", "", __path__)
            small_text = ("small_text", "", __path__)
            button_one_text = ("button_one_text", "", __path__)
            button_one_url = ("button_one_url", "", __path__)
            button_two_text = ("button_two_text", "", __path__)
            button_two_url = ("button_two_url", "", __path__)

        class features:
            token: str
            password: str

            prefix: str
            message_mode: int
            risk_mode: str
            error_log: str
            delete_timer: int
            theme: str
            startup_status: str
            afk_message: str
            stream_url: str

            title: str
            footer: str
            description: bool

            rich_presence_enabled: bool
            application_id: str
            state: str
            details: str
            large_image: str
            large_text: str
            small_image: str
            small_text: str
            button_one_text: str
            button_one_url: str
            button_two_text: str
            button_two_url: str

    class terminal:

        def print(self, contents: str) -> None:
            string = f"{datetime.datetime.now().strftime('%H:%M')} "

            if self == "event":
                string += f"|  Event  | {contents}"
            elif self == "command":
                string += f"| Command | {contents}"
            elif self == "error":
                string += f"|  Error  | {contents}"
            elif self == "info":
                string += f"|  Info   | {contents}"
            elif self == "warning":
                string += f"| Warning | {contents}"
            elif self == "debug":
                string += f"|  Debug  | {contents}"
            elif self == "success":
                string += f"| Success | {contents}"
            elif self == "failure":
                string += f"| Failure | {contents}"
            elif self == "system":
                string += f"|  System | {contents}"
            elif self == "input":
                string += f"|  Input  | {contents}"

    class file_handler:
        def value(self, file: str, key: str) -> str:
            with open(file, "r") as f:
                data = json.load(f)
            return data[key]

        def set(self, file: str, key: str, value: str) -> None:
            with open(file, "r") as f:
                data = json.load(f)
            data[key] = value
            with open(file, "w") as f:
                json.dump(data, f)

        def append(self, file: str, key: str, value: str) -> None:
            with open(file, "r") as f:
                data = json.load(f)
            data[key].append(value)
            with open(file, "w") as f:
                json.dump(data, f)

        def remove(self, file: str, key: str, value: str) -> None:
            with open(file, "r") as f:
                data = json.load(f)
            data[key].remove(value)
            with open(file, "w") as f:
                json.dump(data, f)

        def remove_key(self, file: str, key: str) -> None:
            with open(file, "r") as f:
                data = json.load(f)
            del data[key]
            with open(file, "w") as f:
                json.dump(data, f)

        def remove_all(self, file: str) -> None:
            with open(file, "w") as f:
                f.write("{}")

        def exists(self, file: str) -> bool:
            return os.path.isfile(file)

        def create(self, file: str) -> None:
            with open(file, "w") as f:
                f.write("{}")

        def get_all(self, file: str) -> dict:
            with open(file, "r") as f:
                data = json.load(f)
            return data

        def get_keys(self, file: str) -> list:
            with open(file, "r") as f:
                data = json.load(f)
            return list(data.keys())

        def get_values(self, file: str) -> list:
            with open(file, "r") as f:
                data = json.load(f)
            return list(data.values())


bot = commands.Bot(
    command_prefix=get_prefix(),
    case_insensitive=True,
    strip_after_prefix=True,
    self_bot=True,
    help_command=None,
    guild_subscription_options=GuildSubscriptionOptions.off(),
    status=statuscon(),
    max_messages=1000,
    key="Jgy67HUXLH!Luna"
)

bot.remove_command("help")


def main():
    try:
        bot.run(get_token())
    except Exception as e:
        print(e)


main()
