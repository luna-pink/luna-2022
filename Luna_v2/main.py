import ctypes
import sys
import threading
import dearpygui.dearpygui as dpg
from contextlib import suppress
from types import FrameType
from typing import Callable, Any

import requests

from dotjson import load_keys, get_key, write_key, write_new, remove_key
from gui import start_gui
from discord import *
from discord.ext import commands
from luna import log

# ----------------------------------------------------------------------------------------------------------------------

from events.miscellaneous.on_ready import OnReadyCog

from commands.help.help import HelpCog

# ----------------------------------------------------------------------------------------------------------------------

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

# ----------------------------------------------------------------------------------------------------------------------

load_keys(['data'])

bot = commands.Bot(
    command_prefix=get_key('prefix'),
    case_insensitive=True,
    strip_after_prefix=True,
    self_bot=True,
    help_command=None,
    guild_subscription_options=GuildSubscriptionOptions.off(),
    key="Jgy67HUXLEY!Luna",
)

bot.add_cog(OnReadyCog(bot))
bot.add_cog(HelpCog(bot))


def check_if_debug() -> Callable[[FrameType, str, Any], Callable[[FrameType, str, Any], Any] | None] | None:
    with suppress(AttributeError):
        return sys.gettrace()


def check_if_admin():
    admin = ctypes.windll.shell32.IsUserAnAdmin()
    return admin != 0


def run():
    log('event', 'Logging in...')
    bot.run(get_key('token'))


def run_thread():
    bot_thread = threading.Thread(target=run)
    bot_thread.daemon = True
    bot_thread.start()


def initialize_luna():
    print(logo)
    debug_mode = False
    if check_if_debug() is not None:
        debug_mode = True
        log('info', 'Luna is running in debug mode.')
    run_thread()
    start_gui(debug_mode)


if __name__ == '__main__':
    initialize_luna()
