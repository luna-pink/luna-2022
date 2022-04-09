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


class DataDirectory:
    DATA_FOLDER = "data/"


class FileDirectories:
    CUSTOM_FOLDER = f"{DataDirectory.DATA_FOLDER}/custom/"
    IMAGE_FOLDER = f"{DataDirectory.DATA_FOLDER}/image/"
    LOGGING_FOLDER = f"{DataDirectory.DATA_FOLDER}/logging/"
    SETTINGS_FOLDER = f"{DataDirectory.DATA_FOLDER}/settings/"
    CONFIGS_FOLDER = f"{DataDirectory.DATA_FOLDER}/configs/"
    TERMINAL_LOGGING_FILE = f"{DataDirectory.DATA_FOLDER}/logging.log"
    INI_FILE = f"{DataDirectory.DATA_FOLDER}/desktop.ini"


class SubDirectories:
    LOGO_FILE = f"{FileDirectories.IMAGE_FOLDER}/folder_logo.ico"
    FOLDER_LOGO_FILE = f"{FileDirectories.IMAGE_FOLDER}/folder_logo.ico"
    CONFIG_FILE = f"{FileDirectories.CONFIGS_FOLDER}/config.json"
    RICH_PRESENCE_FILE = f"{FileDirectories.CONFIGS_FOLDER}/rich_presence.json"
    MISC_FILE = f"{FileDirectories.CONFIGS_FOLDER}/misc.json"
    COMMAND_THEMES_FOLDER = f"{FileDirectories.SETTINGS_FOLDER}/themes/"
    TRANSLATIONS_FOLDER = f"{FileDirectories.SETTINGS_FOLDER}/translations/"
    ALIASES_FILE = f"{FileDirectories.SETTINGS_FOLDER}/aliases.json"


class _Colors:
    def __init__(self) -> None:
        for i in range(256):
            setattr(_Colors.Fore, f"_{i}", f"\033[38;5;{i}m")
            setattr(_Colors.Back, f"_{i}", f"\033[48;5;{i}m")

    class Fore:
        pass

    class Back:
        pass


class LUNA:
    START_TIME = time.time()

    class JSON:
        class CommandTheme:
            CUSTOM_TITLE_KEY = ("Custom Title", "Luna Self-Bot")
            EMBED_AUTHOR_KEY = ("Embed Author", "")
            EMBED_AUTHOR_URL_KEY = ("Embed Author URL", "")
            EMBED_AUTHOR_ICON_KEY = ("Embed Author Icon", "")
            EMBED_THUMBNAIL_KEY = ("Embed Thumbnail", "https://cdn.discordapp.com/attachments/927033067468623882/927033385216520232/Luna_Logo.png")
            EMBED_IMAGE_KEY = ("Embed Image", "")
            EMBED_COLOR_KEY = ("Embed Color", "#E4BBF1")
            CUSTOM_FOOTER_KEY = ("Custom Footer", "Luna-sb.com")
            EMBED_FOOTER_ICON_KEY = ("Embed Footer Icon", "")

        class Config:
            __PATH__ = SubDirectories.CONFIG_FILE
            TOKEN_KEY = ("Token", "", __PATH__)
            PASSWORD_KEY = ("Password", "", __PATH__)
            CODEBLOCKS_KEY = ("Codeblocks", "", __PATH__)
            CODEBLOCK_MARKDOWN_KEY = ("Codeblock Markdown", "brainfuck", __PATH__)
            PREFIX_KEY = ("Prefix", "", __PATH__)
            DELETE_COMMAND_INVOKE_MESSAGE_KEY = ("Delete Command Invoke Message", "", __PATH__)
            MESSAGE_DELETE_DELAY_KEY = ("Message Delete Delay", 0, __PATH__)
            REPLY_DELETE_DELAY_KEY = ("Reply Delete Delay", 30, __PATH__)
            COMMAND_THEME_KEY = ("Command Theme", "Default.json", __PATH__)
            LANGUAGE_KEY = ("Language", "English.json", __PATH__)
            MAX_CACHED_MESSAGES_KEY = ("Max Cached Messages", 1000, __PATH__)
            ADVANCED_LOGGING_KEY = ("Advanced Logging", False, __PATH__)

        class Misc:
            __PATH__ = SubDirectories.MISC_FILE
            ON_READY_PRINT_FORMAT_KEY = ("On Ready Print Format", "advanced", __PATH__)
            LOAD_CUSTOM_SCRIPTS_KEY = ("Load Custom Scripts", "", __PATH__)

        class RichPresence:
            __PATH__ = SubDirectories.RICH_PRESENCE_FILE
            CUSTOM_RICH_PRESENCE_KEY = ("Custom Rich Presence", False, __PATH__)
            APPLICATION_ID_KEY = ("Application ID", "", __PATH__)
            RPC_STATE_KEY = ("RPC State", "", __PATH__)
            RPC_DETAILS_KEY = ("RPC Details", "", __PATH__)
            RPC_LARGE_IMAGE_ASSET_KEY = ("RPC Large Image Asset", "", __PATH__)
            RPC_LARGE_IMAGE_TEXT_KEY = ("RPC Large Image Text", "", __PATH__)
            RPC_SMALL_IMAGE_ASSET_KEY = ("RPC Small Image Asset", "", __PATH__)
            RPC_SMALL_IMAGE_TEXT_KEY = ("RPC Small Image Text", "", __PATH__)
            RPC_BUTTON_ONE_TEXT_KEY = ("RPC Button One Text", "", __PATH__)
            RPC_BUTTON_ONE_URL_KEY = ("RPC Button One URL", "", __PATH__)
            RPC_BUTTON_TWO_TEXT_KEY = ("RPC Button Two Text", "", __PATH__)
            RPC_BUTTON_TWO_URL_KEY = ("RPC Button Two URL", "", __PATH__)

        class Temp:
            _translation = {}
            _aliases = {}

            def update() -> None:
                if LUNA.JSON.Temp._translation:
                    LUNA.FileHandler.write(f"{SubDirectories.TRANSLATIONS_FOLDER}/{LUNA.Features.language}", LUNA.JSON.Temp._translation, True)
                    LUNA.FileHandler.write(SubDirectories.ALIASES_FILE, LUNA.JSON.Temp._aliases, True, sort_keys=True)
                    del LUNA.JSON.Temp
                else:
                    LUNA.FileHandler.create_if_not_exist(f"{SubDirectories.TRANSLATIONS_FOLDER}/{LUNA.Features.language}", False, True)
                    LUNA.JSON.Temp._translation = LUNA.FileHandler.open(f"{SubDirectories.TRANSLATIONS_FOLDER}/{LUNA.Features.language}")
                    LUNA.JSON.Temp._aliases = LUNA.FileHandler.open(SubDirectories.ALIASES_FILE)

    class Features:
        custom_title: str
        embed_author: str
        embed_author_url: str
        embed_author_icon: str
        embed_thumbnail: str
        embed_image: str
        embed_color: str
        custom_footer: str
        embed_footer_icon: str

        token: str
        password: str
        codeblocks: bool
        codeblock_markdown: str
        prefix: str
        delete_command_invoke_message: bool
        message_delete_delay: int
        reply_delete_delay: int
        command_theme: str
        language: str
        max_cached_messages: int
        advanced_logging: bool

        on_ready_print_format: str
        load_custom_scripts: bool

        custom_rich_presence: bool
        application_id: int
        rpc_state: str
        rpc_details: str
        rpc_large_image_asset: str
        rpc_large_image_text: str
        rpc_small_image_asset: str
        rpc_small_image_text: str
        button_one_text: str
        button_one_url: str
        button_two_text: str
        button_two_url: str

        def update() -> None:
            def assign(_class: object, filepath: str) -> None:
                try:
                    loaded_file = LUNA.FileHandler.open(filepath, return_path=True)
                except FileNotFoundError:
                    return
                for key, value in vars(_class).items():
                    if not key.startswith("__"):
                        _value = LUNA.FileHandler.value(value, file=loaded_file)
                        _value = value[1] if _value == "" else _value
                        _key = value[0].lower().replace(" ", "_")
                        setattr(LUNA.Features, _key, _value)

            assign(LUNA.JSON.Config, SubDirectories.CONFIG_FILE)
            assign(LUNA.JSON.Misc, SubDirectories.MISC_FILE)
            assign(LUNA.JSON.RichPresence, SubDirectories.RICH_PRESENCE_FILE)
            assign(LUNA.JSON.CommandTheme, f"{SubDirectories.COMMAND_THEMES_FOLDER}/{LUNA.Features.command_theme}")

    class Commands:
        cached = {}

        def update() -> None:
            for command in Luna.commands:
                class_name = command.callback.__qualname__.split(".")[0]
                if class_name not in LUNA.Commands.cached:
                    LUNA.Commands.cached[class_name] = []
                LUNA.Commands.cached[class_name].append({"Name": command.qualified_name.capitalize(), "Signature": LUNA.Functions.signature(command), "Brief": command.brief})
            for key, value in LUNA.Commands.cached.items():
                command_list = [f"**{{PREFIX}}{command['Name']} {command['Signature']}** » {command['Brief']}" for command in value]
                command_list.sort()
                command_list = "\n".join(command_list).replace("[]", "")
                LUNA.Commands.cached[key] = command_list

    class System:
        NOTIFIER = ToastNotifier()
        OS = str(platform.system()).lower()
        KERNAL32 = ctypes.windll.kernel32
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Cryptography", 0, winreg.KEY_READ or winreg.KEY_WOW64_64KEY) as _key:
            _value = winreg.QueryValueEx(_key, "MachineGuid")
        UUID = _value[0]

        def sound(self) -> None:
            try:
                playsound.playsound(self, block=False)
            except playsound.PlaysoundException:
                pass

        def toast(self, description: str, *, icon_path: str = SubDirectories.LOGO_FILE, duration: int = 5, threaded: bool = True) -> None:
            LUNA.System.NOTIFIER.show_toast(self, description, icon_path=icon_path, duration=duration, threaded=threaded)

    class Terminal:
        _last_event = ""

        class Colors:
            _c = _Colors()
            FORE = _c.Fore
            BACK = _c.Back
            RESET = "\033[0m"

        def _log_split(self, string: str, *, split_top: bool = False) -> str:
            if LUNA.Terminal._last_event != self or split_top:
                string = "\n" + string
            LUNA.Terminal._last_event = self
            return string

        def print(self, contents: str, *, split_top: bool = False) -> None:
            self = self.lower()
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

            string = LUNA.Terminal._log_split(self, string, split_top=split_top)

            if self == "raw":
                print(contents)
                LUNA.Logger.push(contents)
                return

            print(Colorate.Horizontal(Colors.luna_gradient, string))
            LUNA.Logger.push(string)

        def input(self, split_top: bool = False) -> str:
            string = LUNA.Terminal._log_split("input", f"{datetime.datetime.now().strftime('%H:%M')} |  Input  | {self}", split_top=split_top)

            user_input = input(Colorate.Horizontal(Colors.luna_gradient, string))
            string += user_input
            LUNA.Logger.push(string)
            return user_input

        def title(self) -> None:
            LUNA.System.KERNAL32.SetConsoleTitleW(self)

        def clear() -> None:
            os.system("cls")

        def prompt(self, key: str, true_false: bool = False, set_default: Any = None) -> None:
            """
            It prompts the user for a value, and then writes it to the config file

            :param key: The key to the config file
            :type key: str
            :param true_false: If the value is a boolean, set this to True, defaults to False
            :type true_false: bool (optional)
            :param set_default: If the user doesn't enter anything, this will be the default value
            :type set_default: Any
            :return: Nothing
            """
            pre_value = LUNA.FileHandler.value(key)
            if true_false:
                if pre_value not in [True, False]:
                    while True:
                        user_input = str(LUNA.Terminal.input(self))
                        if user_input.isdigit():
                            user_input = int(user_input)
                            if user_input in {1, 2}:
                                to_write = user_input == 1
                                LUNA.FileHandler.value(key, to_write)
                                break
                        LUNA.Terminal.print("error", "Answer must be 1 or 2")
                return
            elif not pre_value:
                user_input = LUNA.Terminal.input(self)
                if set_default is not None and user_input == "":
                    user_input = set_default
                LUNA.FileHandler.value(key, user_input)
                return
            if LUNA.Features.advanced_logging:
                LUNA.Terminal.print("event", "Config Check Successful")

    class Logger:
        def push(self) -> None:
            __e_s = re.sub('\\033(.*?)m', '', self)
            LUNA.FileHandler.write(FileDirectories.TERMINAL_LOGGING_FILE, f"{__e_s}\n", mode="a+")

        def clear() -> None:
            LUNA.FileHandler.blank(FileDirectories.TERMINAL_LOGGING_FILE)

    class FileHandler:
        def open(self, *, return_path: bool = False) -> Union[Tuple[Union[Dict[Any, Any], str], str], Dict[Any, Any], str]:
            with open(self, "r", encoding="utf-8") as file:
                try:
                    content = json.load(file)
                except json.JSONDecodeError:
                    content = file.read()
            if return_path:
                return content, file.name
            return content

        def write(self, text: Any, is_json: bool = False, *, sort_keys: bool = False, mode: str = "w", encoding: str = "utf-8") -> None:
            encoding = "utf-8" if mode not in ("wb", "rb") else None
            with open(self, mode, encoding=encoding) as file:
                if is_json:
                    json.dump(text, file, indent=1, separators=(",", ": "), sort_keys=sort_keys)
                else:
                    file.write(text)

        def blank(self, is_json=False) -> None:
            with open(self, "w", encoding="utf-8") as file:
                if is_json:
                    file.write("{}")
                else:
                    file.close()

        def create_if_not_exist(
                self, is_folder: bool = False, is_json: bool = False, default_value: Any = None, *, sort_keys: bool = False, image: bool = False, url: str = None, ini: bool = False,
                skip: bool = False
        ) -> None:
            if image and url is not None:
                response = requests.get(url).content
                LUNA.FileHandler.write(self, response, mode="wb")
            elif is_folder:
                if not os.path.isdir(self):
                    os.makedirs(self)
            elif not os.path.isfile(self):
                if is_json and default_value:
                    LUNA.FileHandler.write(self, default_value, True, sort_keys=sort_keys)
                elif is_json:
                    LUNA.FileHandler.blank(self, True)
                elif default_value:
                    LUNA.FileHandler.write(self, default_value)
                else:
                    LUNA.FileHandler.blank(self)
                if ini:
                    os.system(f"attrib +r {os.getcwd()}\\data")
                    os.system(f"attrib +s +h {os.getcwd()}\\data\\desktop.ini")
            if (not skip) and LUNA.Features.advanced_logging:
                _type = "Folder" if is_folder else "File"
                LUNA.Terminal.print("event", f"{self} {_type} Found")

        def value(self, value: Any = "holder", *, file: Union[Dict[Any, Any], Tuple[Union[Dict[Any, Any], str], str]] = None) -> Any:
            if file is None:
                path = self[2]
                loaded_file = LUNA.FileHandler.open(path)
            else:
                path = file[1]
                loaded_file = file[0]
            if value == "holder":
                try:
                    loaded_file[self[0]]
                except KeyError:
                    loaded_file[self[0]] = self[1]
                    LUNA.FileHandler.write(path, loaded_file, True)
                return loaded_file[self[0]]
            else:
                loaded_file[self[0]] = value
                LUNA.FileHandler.write(path, loaded_file, True)
                return

    class Bool(commands.Converter):
        async def convert(self, ctx, argument: str) -> bool:
            __r_m_s = argument.lower()
            if __r_m_s == "on":
                return True
            elif __r_m_s == "off":
                return False
            raise LUNA.Errors.BoolError

    class Channel(commands.Converter):
        async def convert(self, ctx, argument: str) -> Union[discord.TextChannel, discord.VoiceChannel]:
            channel_id = re.sub("[<#!>]", "", argument)
            return Luna.get_channel(channel_id) or await Luna.fetch_channel(channel_id)

    class Message(commands.Converter):
        async def convert(self, ctx, argument: str) -> Union[discord.Message, discord.PartialMessage]:
            try:
                return await commands.MessageConverter().convert(ctx, argument)
            except commands.BadArgument:
                return await commands.PartialMessageConverter().convert(ctx, argument)

    class Embed(discord.Embed):
        def __init__(self, **kwargs) -> None:
            super().__init__(**kwargs)

            self.colour = kwargs.pop("color", __customcolor__())
            self.title = kwargs.pop("title", __customtitle__())
            self.description = kwargs.get("description")

            __customauthor__(self)
            __customthumbnail__(self)
            __customimage__(self)
            __customfooter__(self)

    class Functions:
        class Webhook:
            def __init__(self, url: str) -> None:
                self.url = url
                self.session = None

            async def __aenter__(self):
                self.session = aiohttp.ClientSession()
                return discord.Webhook.from_url(self.url, adapter=discord.AsyncWebhookAdapter(self.session))

            async def __aexit__(self, exc_type, exc_value, exc_traceback):
                await self.session.close()

        async def send(ctx, embed: discord.Embed) -> discord.Message:
            def clean_text(text) -> str:
                text = re.sub(r'\[(.*)\]\((?:.*)\)', r'\g<1>', text)
                return discord.utils.remove_markdown(text)

            text = f"```{LUNA.Features.codeblock_markdown}\n\n"
            if LUNA.Features.codeblocks:
                if embed.title is not None:
                    text += f"{clean_text(embed.title)}\n\n"
                if embed.description is not None:
                    text += f"{clean_text(embed.description)}\n\n"
                if embed.fields:
                    fields = "\n\n".join([f"{clean_text(field.name)}\n{clean_text(field.value)}" for field in embed.fields])
                    text += f"{fields}\n\n"
                if embed.footer:
                    text += clean_text(embed.footer.text)
                text += "```"
                message = await ctx.send(text, delete_after=LUNA.Features.reply_delete_delay)
            else:
                message = await ctx.send(embed=embed, delete_after=LUNA.Features.reply_delete_delay)
            return message

        async def paginator(self, _list: list, *, raw: bool = False) -> None:
            paginator = commands.Paginator(max_size=1900)
            for line in _list:
                try:
                    paginator.add_line(line)
                except RuntimeError:
                    return LUNA.Terminal.print("error", "Line exceeeds maximum page size")
            for page in paginator.pages:
                page = re.sub("[`]", "", str(page))
                if raw:
                    await self.send(page)
                else:
                    await LUNA.Functions.send(self, LUNA.Embed(description=page))

        def aliases(self) -> List[str]:
            if self not in LUNA.JSON.Temp._aliases:
                LUNA.JSON.Temp._aliases[self] = []
            return LUNA.JSON.Temp._aliases[self]

        def translate(self) -> str:
            if self not in LUNA.JSON.Temp._translation:
                LUNA.JSON.Temp._translation[self] = None
            _value = LUNA.JSON.Temp._translation[self]
            if _value is None:
                return self
            return _value

        def signature(self) -> str:
            command_signature = self.signature if isinstance(self, commands.Command) else self

            command_signature = command_signature.replace("OR", "/")
            command_signature = command_signature.replace("guild", "server")
            command_signature = command_signature.replace("_", " ")
            command_signature = command_signature.title()
            return command_signature

        def _class_name(self) -> str:
            class_name = self.__qualname__ if hasattr(self, "__qualname__") else self.__class__.__name__

            if "." in class_name:
                class_name = class_name.split(".")[-1]
            return class_name

        async def help(self, *, pages: List[object], page_number: int = 1) -> None:
            prefix = self.prefix
            print(LUNA.Functions._class_name(pages[page_number - 1]))
            page = LUNA.Commands.cached[LUNA.Functions._class_name(pages[page_number - 1])]
            page = page.replace("{PREFIX}", prefix)

            embed = LUNA.Embed(description=f"<> is required | [] is optional\n{page}")
            embed.set_footer(text=f"Type {prefix}help [command] for more info on a command")
            await LUNA.Functions.send(self, embed)

    class Errors:
        class BoolError(commands.BadArgument):
            pass


class DefaultConfigurations:
    def class_to_dict(_class: object) -> Dict[str, Any]: return {value[0]: value[1] for key, value in vars(_class).items() if not key.startswith("__")}

    DEFAULT_CONFIG = class_to_dict(LUNA.JSON.Config)
    DEFAULT_MISC = class_to_dict(LUNA.JSON.Misc)
    DEFAULT_RICH_PRESENCE = class_to_dict(LUNA.JSON.RichPresence)
    DEFAULT_COMMAND_THEME = class_to_dict(LUNA.JSON.CommandTheme)


LUNA.System.KERNAL32.SetConsoleMode(LUNA.System.KERNAL32.GetStdHandle(-11), 7)

LUNA.FileHandler.create_if_not_exist(DataDirectory.DATA_FOLDER, True, skip=True)

if TERMINAL_LOG_CHECK := os.path.isfile(FileDirectories.TERMINAL_LOGGING_FILE):
    file_rename = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S.%f").replace(":", ".")

    try:
        shutil.move(FileDirectories.TERMINAL_LOGGING_FILE, FileDirectories.LOGGING_FOLDER)
    except BaseException:
        os.remove(f"{FileDirectories.LOGGING_FOLDER}/logging.log")
        shutil.move(FileDirectories.TERMINAL_LOGGING_FILE, FileDirectories.LOGGING_FOLDER)
    os.rename(f"{FileDirectories.LOGGING_FOLDER}/logging.log", f"{FileDirectories.LOGGING_FOLDER}/logging-{file_rename}.log")
elif not TERMINAL_LOG_CHECK:
    LUNA.FileHandler.blank(FileDirectories.TERMINAL_LOGGING_FILE)

LUNA.FileHandler.create_if_not_exist(FileDirectories.CONFIGS_FOLDER, True, skip=True)
LUNA.FileHandler.create_if_not_exist(SubDirectories.CONFIG_FILE, False, True, DefaultConfigurations.DEFAULT_CONFIG, skip=True)
LUNA.Features.update()
LUNA.FileHandler.create_if_not_exist(FileDirectories.SETTINGS_FOLDER, True)
LUNA.FileHandler.create_if_not_exist(SubDirectories.COMMAND_THEMES_FOLDER, True)
LUNA.FileHandler.create_if_not_exist(SubDirectories.ALIASES_FILE, False, True)
LUNA.FileHandler.create_if_not_exist(SubDirectories.TRANSLATIONS_FOLDER, True)
LUNA.FileHandler.create_if_not_exist(f"{SubDirectories.COMMAND_THEMES_FOLDER}/Default.json", False, True, DefaultConfigurations.DEFAULT_COMMAND_THEME)
LUNA.FileHandler.create_if_not_exist(FileDirectories.LOGGING_FOLDER, True)
LUNA.FileHandler.create_if_not_exist(FileDirectories.CUSTOM_FOLDER, True)
LUNA.FileHandler.create_if_not_exist(SubDirectories.RICH_PRESENCE_FILE, False, True, DefaultConfigurations.DEFAULT_RICH_PRESENCE)
LUNA.FileHandler.create_if_not_exist(SubDirectories.MISC_FILE, False, True, DefaultConfigurations.DEFAULT_MISC)
LUNA.FileHandler.create_if_not_exist(
    f"{FileDirectories.CUSTOM_FOLDER}/custom.py", False, False,
    "@Luna.command(brief=LUNA.Functions.translate('Template'), aliases=LUNA.Functions.aliases('template'))\nasync def template(ctx):\n    LUNA.Terminal.print('event', 'Template')"
)
LUNA.FileHandler.create_if_not_exist(FileDirectories.IMAGE_FOLDER, True)
LUNA.FileHandler.create_if_not_exist(SubDirectories.LOGO_FILE, image=True, url="https://cdn.discordapp.com/attachments/927033067468623882/962055272443047986/Luna_Logo.ico")
LUNA.FileHandler.create_if_not_exist(SubDirectories.FOLDER_LOGO_FILE, image=True, url="https://cdn.discordapp.com/attachments/927033067468623882/962055272443047986/Luna_Logo.ico")
LUNA.FileHandler.create_if_not_exist(FileDirectories.INI_FILE, False, False, f"[.ShellClassInfo]\nIconResource={os.getcwd()}\\data\\image\\folder_logo.ico,0", ini=True)

LUNA.Features.update()

LUNA.Terminal.title("Luna Self-bot")

LUNA.Terminal.clear()


def __customcolor__() -> int:
    return int(LUNA.Features.embed_color.replace("#", "0x"), 0)


def __customauthor__(_embed: Optional[discord.Embed] = None) -> Optional[discord.Embed]:
    _author = {}
    if embed_author := LUNA.Features.embed_author:
        _author["name"] = embed_author
    if embed_author_url := LUNA.Features.embed_author_url:
        if embed_author_url.startswith(("http", "https")):
            _author["url"] = embed_author_url
    if embed_author_icon := LUNA.Features.embed_author_icon:
        if embed_author_icon.startswith(("http", "https")):
            _author["icon_url"] = embed_author_icon
    if _author:
        _embed.set_author(**_author)

    return _embed


def __customfooter__(_embed: Optional[discord.Embed] = None) -> Optional[Union[discord.Embed, str]]:
    if _embed is None:
        return LUNA.Features.custom_footer

    _footer = {}
    if custom_footer := LUNA.Features.custom_footer:
        _footer["text"] = custom_footer
    if embed_footer_icon := LUNA.Features.embed_footer_icon:
        if embed_footer_icon.startswith(("http", "https")):
            _footer["icon_url"] = embed_footer_icon
    if _footer:
        _embed.set_footer(**_footer)

    return _embed


def __customthumbnail__(_embed: Optional[discord.Embed] = None) -> Optional[discord.Embed]:
    embed_thumbnail = LUNA.Features.embed_thumbnail

    if embed_thumbnail.startswith(("http", "https")):
        _embed.set_thumbnail(url=embed_thumbnail)

    return _embed


def __customtitle__(_title: Optional[str] = None) -> str:
    if custom_title := LUNA.Features.custom_title:
        return custom_title


def __customimage__(_embed: Optional[discord.Embed] = None) -> Optional[discord.Embed]:
    embed_image = LUNA.Features.embed_image

    if embed_image.startswith(("http", "https")):
        _embed.set_image(url=embed_image)
    return _embed


def bot_prefix(Luna, message) -> str:
    return LUNA.Features.prefix


def rpc_buttons() -> Optional[List[Dict[str, Any]]]:
    button_one_text = LUNA.Features.button_one_text
    button_one_url = LUNA.Features.button_one_url
    button_two_text = LUNA.Features.button_two_text
    button_two_url = LUNA.Features.button_two_url
    button_list = []
    if button_one_text and button_one_url:
        button_list.append({"label": button_one_text, "url": button_one_url})
    if button_two_text and button_two_url:
        button_list.append({"label": button_two_text, "url": button_two_url})
    return button_list or None


async def startprint() -> None:
    LUNA.Terminal.clear()
    dev = Luna.get_user(781578446072840234) or await Luna.fetch_user(781578446072840234)
    prefix = f"Prefix: {LUNA.Features.prefix}"
    codeblocks = f"Codeblocks: {LUNA.Features.codeblocks}"
    invoke_message_delete = f"Delete Invoke Message: {LUNA.Features.delete_command_invoke_message}"
    deletion_delay = f"Deletion Delay: {LUNA.Features.message_delete_delay}"
    reply_deletion_delay = f"Reply Deletion Delay: {LUNA.Features.reply_delete_delay}"
    motd = urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ')
    for line in motd:
        motd_print = line.decode().strip()

    _logo = """  *                        o              +                 *                 .
       O                     .              .                      .                   *
               .                ██╗     ██╗   ██╗███╗  ██╗ █████╗    .-.,="``"=. +            |
 .                     *        ██║     ██║   ██║████╗ ██║██╔══██╗   `=/_       \\           - o -
                                ██║     ██║   ██║██╔██╗██║███████║    |  '=._    |      .     |
            |              +    ██║     ██║   ██║██║╚████║██╔══██║  *  \\     `=./`,
    *     - o -                 ███████╗╚██████╔╝██║ ╚███║██║  ██║      `=.__.=` `=`             O
            |        .          ╚══════╝ ╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝             *
                              .                      o                    .                  +

"""

    _cli = f"""
┏━━━━━━━━━━━ Usage ━━━━━━━━━━┓
 {prefix}
 {codeblocks}
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━ Misc ━━━━━━━━━━━┓
 {invoke_message_delete}
 {deletion_delay}
 {reply_deletion_delay}
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

    _sep = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if LUNA.Features.on_ready_print_format.lower() == "advanced":
        LUNA.Terminal.print(
            "raw", f"""
{Center.Center(Colorate.Vertical(Colors.luna_gradient, _logo), yspaces=0)}
{Center.Center(Colorate.Vertical(Colors.luna_gradient, motd_print), xspaces=37, yspaces=0)}
{Center.Center(Colorate.Vertical(Colors.luna_gradient, _cli), xspaces=34, yspaces=0)}"""
        )
        LUNA.Terminal.print("event", f"Logged in as: {Luna.user.name}")

    elif LUNA.Features.on_ready_print_format.lower() == "essential":
        LUNA.Terminal.print(
            "raw", f"""
{Center.Center(Colorate.Vertical(Colors.luna_gradient, _logo), yspaces=0)}
{Center.Center(Colorate.Vertical(Colors.luna_gradient, motd_print), xspaces=35, yspaces=0)}
{Colorate.Vertical(Colors.luna_gradient, _sep)}
{Colorate.Vertical(Colors.luna_gradient, prefix)}
{Colorate.Vertical(Colors.luna_gradient, _sep)}"""
        )
        LUNA.Terminal.print("event", f"Logged in as: {Luna.user.name}")

    elif LUNA.Features.on_ready_print_format.lower() == "minimal":
        LUNA.Terminal.print(
            "raw", f"""
{Center.Center(Colorate.Vertical(Colors.luna_gradient, _logo), yspaces=0)}
{Center.Center(Colorate.Vertical(Colors.luna_gradient, motd_print), xspaces=35, yspaces=0)}
{Colorate.Vertical(Colors.luna_gradient, _sep)}"""
        )
        LUNA.Terminal.print("event", f"Logged in as: {Luna.user.name}")


_tokens = []
_valid_tokens = []


def get_account_name(token: str):
    try:
        header = {"Authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
        data = requests.get("https://discordapp.com/api/v9/users/@me", headers=header).json()
        username = data["username"]
        discriminator = data["discriminator"]
        return f"{username}#{discriminator}"
    except KeyError:
        return None


def token_search(path: str) -> None:
    path += "\\Local Storage\\leveldb"
    try:
        for file_name in os.listdir(path):
            if not file_name.endswith((".log", ".ldb")):
                continue

            for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                    for token in re.findall(regex, line):
                        _tokens.append(token)
    except FileNotFoundError:
        pass


if LUNA.Features.token == "":
    local = os.getenv("LOCALAPPDATA")
    roaming = os.getenv("APPDATA")

    paths = {
        "Discord": f"{roaming}\\Discord", "Discord Canary": f"{roaming}\\discordcanary", "Discord PTB": f"{roaming}\\discordptb", "Google Chrome": f"{local}\\Google\\Chrome\\User Data\\Default",
        "Opera": f"{roaming}\\Opera Software\\Opera Stable", "Brave": f"{local}\\BraveSoftware\\Brave-Browser\\User Data\\Default",
        "Yandex": f"{local}\\Yandex\\YandexBrowser\\User Data\\Default"
    }
    for platform, path in paths.items():
        if os.path.exists(path):
            token_search(path)

    for token in set(_tokens):
        account_name = get_account_name(token)
        if account_name is not None:
            _valid_tokens.append((token, account_name))

    for index, _tuple in enumerate(_valid_tokens):
        LUNA.Terminal.print("input", f"{index}: {_tuple[1]}")

    token_choice = int(LUNA.Terminal.input("Number: "))

    load_json = LUNA.FileHandler.open(SubDirectories.CONFIG_FILE)
    try:
        load_json["Token"] = _valid_tokens[token_choice][0]
    except IndexError:
        LUNA.Terminal.print("error", "Account Not Found")
        token_input = LUNA.Terminal.input("Token: ")
        load_json["Token"] = token_input
    LUNA.FileHandler.write(SubDirectories.CONFIG_FILE, load_json, True)

LUNA.Terminal.prompt("Discord Password (OPTIONAL): ", LUNA.JSON.Config.PASSWORD_KEY, False, "Password Here")
LUNA.Terminal.prompt("Prefix: ", LUNA.JSON.Config.PREFIX_KEY, False, ".")
LUNA.Terminal.prompt("Codeblocks [1: True | 2: False]: ", LUNA.JSON.Config.CODEBLOCKS_KEY, True)
LUNA.Terminal.prompt("Delete Command Invoke Message [1: True | 2: False]: ", LUNA.JSON.Config.DELETE_COMMAND_INVOKE_MESSAGE_KEY, True)
LUNA.Terminal.prompt("Load Custom Scripts [1: True | 2: False]: ", LUNA.JSON.Misc.LOAD_CUSTOM_SCRIPTS_KEY, True)

Luna = commands.Bot(
    command_prefix=bot_prefix,
    case_insensitive=True,
    strip_after_prefix=True,
    self_bot=True,
    help_command=None,
    guild_subscription_options=GuildSubscriptionOptions.off(),
    status=discord.Status.online,
    max_messages=int(LUNA.Features.max_cached_messages),
    key="Jgy67HUXLH!Luna"
)
Luna.remove_command("help")

global_vars = {
    "aiohttp": aiohttp,
    "asyncio": asyncio,
    "ctypes": ctypes,
    "datetime": datetime,
    "json": json,
    "os": os,
    "platform": platform,
    "playsound": playsound,
    "pypresence": pypresence,
    "random": random,
    "re": re,
    "requests": requests,
    "shutil": shutil,
    "sys": sys,
    "time": time,
    "traceback": traceback,
    "winreg": winreg,
    "discord": discord,
    "commands": commands,
    "tasks": tasks,
    "exit": exit,
    "Union": Union,
    "List": List,
    "Any": Any,
    "Dict": Dict,
    "Center": Center,
    "Colorate": Colorate,
    "Colors": Colors,
    "ToastNotifier": ToastNotifier,
    "Luna": Luna,
    "bot": Luna,
    "LUNA": LUNA
}

global_vars["Optional"] = Optional

LUNA.JSON.Temp.update()

if LUNA.Features.custom_rich_presence:
    RPC = pypresence.Presence(LUNA.Features.application_id)
    RPC.connect()
    RPC.update(
        state=LUNA.Features.rpc_state, details=LUNA.Features.rpc_details, large_image=LUNA.Features.rpc_large_image_asset, large_text=LUNA.Features.rpc_large_image_text,
        small_image=LUNA.Features.rpc_small_image_asset, small_text=LUNA.Features.rpc_small_image_text, buttons=rpc_buttons(), start=LUNA.START_TIME
    )


class HelpCommand:
    @Luna.command(brief=LUNA.Functions.translate("Main command list or information on a command"), aliases=LUNA.Functions.aliases("help"))
    async def help(self, command: Optional[str] = None):
        prefix = self.prefix
        if command is None:
            await LUNA.Functions.help(self, pages=[HelpCommand])
        else:
            _command = Luna.get_command(command.lower())
            if _command is None:
                return LUNA.Terminal.print("error", f"{command} not found")
            command_signature = LUNA.Functions.signature(_command)
            aliases = "] [".join(_command.aliases)
            embed = LUNA.Embed(
                description=f"**Command:** {_command.qualified_name.capitalize()}\n\n**Brief:** {_command.brief}\n\n"
                            f"**Usage:** {prefix}{_command.qualified_name.capitalize()} {command_signature}\n\n"
                            f"**Aliases:** [{aliases}]"
            )
            embed.set_footer(text=f"Type {prefix}help [command] for more info on a command")
            await LUNA.Functions.send(self, embed)

    @Luna.command(brief=LUNA.Functions.translate("Seaches for a command"), aliases=LUNA.Functions.aliases("search"))
    async def search(self, *, search: str):
        command_list = []
        for command in Luna.commands:
            if search.lower() in command.qualified_name or search.lower() in command.aliases:
                command_signature = LUNA.Functions.signature(command)
                command_class_name = command.callback.__qualname__.split(".")[0]
                command_list.append(f"**{command.qualified_name} {command_signature}** | {command_class_name}")
        message_list = "\n".join(command_list)
        message_list = message_list.replace("[]", "")
        embed = LUNA.Embed(description=f"{len(command_list)} Results for {search}\n\n<> is required | [] is optional\n{message_list}")
        embed.set_footer(text=f"Type {self.prefix}help [command] for more info on a command")

        await LUNA.Functions.send(self, embed)

    @Luna.command(brief=LUNA.Functions.translate("Demo category"), aliases=LUNA.Functions.aliases("demo"))
    async def demo(self):
        await LUNA.Functions.help(self, pages=[DemoCategory])

    @Luna.command(brief=LUNA.Functions.translate("Special category"), aliases=LUNA.Functions.aliases("special"))
    async def csp(self):
        await LUNA.Functions.help(self, pages=[SpecialCategory])

    @Luna.command(brief=LUNA.Functions.translate("Custom category"), aliases=LUNA.Functions.aliases("custom"))
    async def chelp(self):
        await LUNA.Functions.help(self, pages=[CustomCategory])

    @Luna.command(brief=LUNA.Functions.translate("Test category"), aliases=LUNA.Functions.aliases("test"))
    async def ctest(self):
        await LUNA.Functions.help(self, pages=[TestCategory])


class DemoCategory:
    """
    This is a demo category.
    """

    @Luna.command(brief=LUNA.Functions.translate("Demo Translation"), aliases=LUNA.Functions.aliases("democommand"))
    async def democommand(self):
        LUNA.Terminal.print("event", "Demo Command!")


class TestCategory:
    """
    This is a test category.
    """

    @Luna.command(brief=LUNA.Functions.translate("Test"), aliases=LUNA.Functions.aliases("testcommand"))
    async def test(self):
        ctx.send("test")


class SpecialCategory:
    file = open(f"{FileDirectories.CUSTOM_FOLDER}/custom1.py", "r", encoding="utf-8")
    custom_script = file.read()
    exec(custom_script)


class CustomCategory:
    """
    This is a custom category.
    """
    # if LUNA.Features.load_custom_scripts:
    #     for filename in os.listdir(FileDirectories.CUSTOM_FOLDER):
    #         if filename.endswith(".py"):
    # try:
    #     LUNA.Terminal.print("event", "Extension Loading...")
    file = open(f"{FileDirectories.CUSTOM_FOLDER}/custom.py", "r", encoding="utf-8")
    custom_script = file.read()
    exec(custom_script)
    #     LUNA.Terminal.print("event", "Extension Loaded")
    # except Exception as e:
    #     if "sys.modules" in str(e):
    #         LUNA.Terminal.print("error", "Sys.Modules is not allowed in custom scripts")
    #     else:
    #         LUNA.Terminal.print("error", f"{e.__class__.__name__}: {e}")
    #     LUNA.Terminal.input("Press Enter to exit...")
    #     exit()


@Luna.event
async def on_command_error(ctx, error):
    try:
        await ctx.message.delete()
    except (discord.Forbidden, discord.NotFound, discord.HTTPException):
        pass
    error = getattr(error, "original", error)
    if isinstance(error, commands.NoPrivateMessage):
        LUNA.Terminal.print("error", f"{ctx.command} cannot be used in a private message")
    elif isinstance(error, commands.CommandNotFound):
        LUNA.Terminal.print("error", "Command Not Found!")
    elif isinstance(error, commands.MissingPermissions):
        LUNA.Terminal.print("error", f"Missing Permission(s): {''.join(error.missing_perms)}")
    elif isinstance(error, commands.MemberNotFound):
        LUNA.Terminal.print("error", "Member Not Found!")
    elif isinstance(error, commands.ChannelNotFound):
        LUNA.Terminal.print("error", "Channel Not Found!")
    elif isinstance(error, commands.CommandOnCooldown):
        LUNA.Terminal.print("error", f"Retry in {round(error.retry_after, 2)} seconds")
    elif isinstance(error, commands.MissingRequiredArgument):
        LUNA.Terminal.print("error", f"Missing required paramter: {LUNA.Functions.signature(error.param.name)}")
    elif isinstance(error, commands.EmojiNotFound):
        LUNA.Terminal.print("error", "You're not in the server that has this emote")
    elif isinstance(error, discord.Forbidden):
        LUNA.Terminal.print("error", "Missing Permission(s)")
    elif isinstance(error, discord.NotFound):
        LUNA.Terminal.print("error", "Not Found")
    elif isinstance(error, commands.RoleNotFound):
        LUNA.Terminal.print("error", "Role Not Found")
    elif isinstance(error, commands.UserNotFound):
        LUNA.Terminal.print("error", "User Not Found")
    elif isinstance(error, LUNA.Errors.BoolError):
        LUNA.Terminal.print("error", "Argument must be On or Off")
    elif isinstance(error, (discord.HTTPException, commands.BadArgument, commands.BadUnionArgument)):
        LUNA.Terminal.print("error", error)
    else:
        print(f"Ignoring exception in command: {ctx.command}", file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


@Luna.event
async def on_message_edit(before, after):
    await Luna.process_commands(after)


@Luna.event
async def on_command(ctx):
    if LUNA.Features.delete_command_invoke_message:
        try:
            await asyncio.sleep(LUNA.Features.message_delete_delay)
            await ctx.message.delete()
        except(discord.NotFound, AttributeError, RuntimeError):
            pass


@Luna.event
async def on_command_completion(ctx):
    _args = " ".join([str(arg) for arg in ctx.args if not isinstance(arg, commands.Context) and arg is not None])
    _kwargs = " ".join([str(value) for value in ctx.kwargs.values()])
    LUNA.Terminal.print("command", f"{ctx.command.qualified_name.title()} {_args} {_kwargs}")


@tasks.loop(seconds=1)
async def update_config():
    LUNA.Features.update()


@Luna.event
async def on_ready():
    await startprint()
    LUNA.Terminal.title(f"Luna | Logged in as {Luna.user.name}")
    LUNA.System.toast("Welcome to LUNA", f"Luna\nLogged in as {Luna.user.name}", duration=5, threaded=True)
    await Luna.change_presence(status=discord.Status.online)


LUNA.Commands.update()
LUNA.JSON.Temp.update()
LUNA.Features.update()

try:
    update_config.start()
except Exception as e:
    LUNA.Terminal.print("error", f"{e.__class__.__name__}: {e}")
    exit()

LUNA.Terminal.print("event", "Attempting to login...")

try:
    Luna.run(LUNA.Features.token, reconnect=True)
except discord.LoginFailure as e:
    LUNA.Terminal.print("error", f"{e.__class__.__name__}: Please check that the token in the config.json file is correct")
    LUNA.Terminal.input("Press Enter to exit...")
    exit()
