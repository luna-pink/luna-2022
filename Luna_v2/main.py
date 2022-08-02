import ctypes
import os
import sys
import threading
import dearpygui.dearpygui as dpg
from contextlib import suppress
from types import FrameType
from typing import Callable, Any

from win32api import GetSystemMetrics
import style
import animation as dpg_anim
import dearpygui.demo as demo

import requests

from dotjson import load_keys, get_key, write_key, write_new, remove_key, backup_path
from discord import *
from discord.ext import commands
from luna import log

# ----------------------------------------------------------------------------------------------------------------------

from events.miscellaneous.on_ready import OnReadyCog
from events.sniper.nitro import SniperCog

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

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

window_width = 740
window_height = 570

x_pos = int((screen_width - window_width) / 2)
y_pos = int((screen_height - window_height) / 2)

trigger = False

scripts = []
loaded_scripts = []
loaded_scripts_ids = {}

# ----------------------------------------------------------------------------------------------------------------------

load_keys(['data'])
backup_path(['data'])

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
bot.add_cog(SniperCog(bot))


def load_script():
    try:
        log('scripts', f'Loading {dpg.get_value("scripts_listbox")}')
        bot.load_extension(f'data.scripts.{dpg.get_value("scripts_listbox")}')
        tab_id = dpg.get_item_children("scripts_tab_bar", slot=1)  # {0: [], 1: [80], 2: [], 3: []} | {0: [], 1: [80, 193], 2: [], 3: []}
        loaded_scripts.append(dpg.get_value("scripts_listbox"))
        loaded_scripts_ids[dpg.get_value("scripts_listbox")] = tab_id[-1]
        dpg.configure_item("loaded_scripts_listbox", items=loaded_scripts)
        dpg.set_value("loaded_scripts_text", f"Loaded scripts: {len(loaded_scripts)}")
        log('scripts', f'{dpg.get_value("scripts_listbox")} has been loaded')
    except Exception as e:
        log('error', f'Failed to load script:\n{e}')
        return


def unload_script():
    try:
        log('scripts', f'Unloading {dpg.get_value("loaded_scripts_listbox")}')
        bot.unload_extension(f'data.scripts.{dpg.get_value("loaded_scripts_listbox")}')
        dpg.delete_item(loaded_scripts_ids[dpg.get_value("loaded_scripts_listbox")])
        loaded_scripts.remove(dpg.get_value("loaded_scripts_listbox"))
        loaded_scripts_ids.pop(dpg.get_value("loaded_scripts_listbox"))
        dpg.configure_item("loaded_scripts_listbox", items=loaded_scripts)
        dpg.set_value("loaded_scripts_text", f"Loaded scripts: {len(loaded_scripts)}")
        log('scripts', f'{dpg.get_value("loaded_scripts_listbox")} has been unloaded')
    except Exception as e:
        log('error', f'Failed to unload script:\n{e}')
        return


def reload_scripts():
    scripts.clear()
    scripts.extend(filename[:-3] for filename in os.listdir('data/scripts') if filename.endswith('.py'))
    dpg.configure_item("scripts_listbox", items=scripts)
    log('scripts', 'Scripts reloaded')


# ----------------------------------------------------------------------------------------------------------------------

dpg.create_context()

dpg.create_viewport(
    title='Luna',
    width=window_width,
    height=window_height,
    resizable=False,
    y_pos=y_pos,
    x_pos=x_pos,
    small_icon="data/resources/luna.ico",
    large_icon="data/resources/luna.ico"
)


def authentication_process():
    with dpg.window(label="Authentication", tag="authentication_modal", modal=True, no_close=True, no_resize=True, no_collapse=True, no_move=True, width=319, height=154):
        dpg.set_item_pos(
            "authentication_modal", pos=[
                (dpg.get_viewport_width() - dpg.get_item_width("authentication_modal")) / 2,
                (dpg.get_viewport_height() - dpg.get_item_height("authentication_modal")) / 2
            ]
        )
        username = dpg.add_input_text(label="Username", default_value="", no_spaces=True)
        dpg.add_spacer()
        password = dpg.add_input_text(label="Password", default_value="", password=True, no_spaces=True)
        dpg.add_spacer()
        dpg.add_separator()
        status = dpg.add_text("Status: Not Authenticated")
        dpg.add_separator()
        dpg.add_spacer()
        with dpg.group(horizontal=True, label="group_buttons"):
            dpg.add_button(label="Login")
            dpg.add_button(label="Register")
            dpg.add_button(label="HWID Reset")
            dpg.add_button(label="Password Reset")


def resize():
    global window_width, window_height, trigger
    trigger = not trigger
    if not trigger:
        dpg_anim.viewport_resize("Luna", duration=10, loop=38, width=-7, height=0, final_width=740, center=True)
        dpg.delete_item("third_window")
    else:
        with dpg.child_window(label="Child Window", width=258, parent="main_group", tag="third_window"):
            dpg.add_text("Documentation")
            dpg.add_separator()
            with dpg.collapsing_header(label="Discord"):
                with dpg.tree_node(label="Basic"):
                    dpg.add_text("https://discord.gg/QWQWQWQ")
                with dpg.tree_node(label="Advanced"):
                    dpg.add_text("https://discord.gg/QWQWQWQ")
            with dpg.collapsing_header(label="Luna"):
                with dpg.tree_node(label="Basic"):
                    dpg.add_text("https://discord.gg/QWQWQWQ")
                with dpg.tree_node(label="Advanced"):
                    dpg.add_text("https://discord.gg/QWQWQWQ")

        dpg_anim.viewport_resize("Luna", duration=10, loop=38, width=7, height=0, final_width=1006, center=True)


with dpg.window(tag="primary_window"):
    width, height, channels, data = dpg.load_image("data/resources/background.jpg")
    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    dpg.add_image(texture_id, width=1006, height=522, pos=(0, 0))

    with dpg.child_window(label="Child Window", height=38, no_scrollbar=True):
        dpg.add_text("Nshout 1 | Version 2.0")

    dpg.add_spacer()

    with dpg.group(horizontal=True):
        with dpg.child_window(label="Child Window", width=160, height=422):
            width, height, channels, data = dpg.load_image("data/resources/luna.png")
            with dpg.texture_registry():
                texture_id = dpg.add_static_texture(width, height, data)

            dpg.add_image(texture_id, width=75, height=75, pos=(42, 13))

            # width, height, channels, data = dpg.load_image("data/resources/mlp.png")
            # with dpg.texture_registry():
            #     texture_id = dpg.add_static_texture(width, height, data)
            #
            # dpg.add_image(texture_id, width=75, height=78, pos=(42, 13))

            dpg.add_spacer(height=90)
            dpg.add_separator()
            dpg.add_spacer()
            dpg.add_button(label="Expand", callback=resize, width=144, height=25)
            dpg.add_spacer()
            dpg.add_button(label="Style", callback=dpg.show_style_editor, width=144, height=25)
            dpg.add_spacer()
            dpg.add_button(label="Demo", callback=demo.show_demo, width=144, height=25)

            width, height, channels, data = dpg.load_image("data/resources/mlp.png")
            with dpg.texture_registry():
                texture_id = dpg.add_static_texture(width, height, data)

            dpg.add_image(texture_id, width=150, height=155, pos=(5, 256))

        with dpg.child_window(label="Child Window", height=422, tag="main_window"):
            with dpg.tab_bar(tag="top_tab_bar"):
                with dpg.tab(label="Home"):
                    width, height, channels, data = dpg.load_image("data/resources/luna_ascii.png")
                    with dpg.texture_registry():
                        texture_id = dpg.add_static_texture(width, height, data)

                    dpg.add_image(texture_id, tag="luna_ascii", width=516, height=108)

                    with dpg.group(horizontal=True, tag="main_group"):
                        with dpg.child_window(label="Child Window", width=258):
                            dpg.add_text("Discord")
                            dpg.add_separator()
                            dpg.add_text("Not logged in", tag="logged_in_text")
                            dpg.add_text("Loading friends...", tag="friends_text")
                            dpg.add_text("Loading blocked...", tag="blocked_text")
                            dpg.add_text("Loading guilds...", tag="guilds_text")
                            dpg.add_text("Loading status...", tag="status_text")
                            dpg.add_text("Loading settings...", tag="settings_text")
                            dpg.add_text("Loading nitro...", tag="nitro_text")

                        with dpg.child_window(label="Child Window", width=258):
                            dpg.add_text("Luna")
                            dpg.add_separator()
                            dpg.add_text("Prefix: .", tag="prefix_text")
                            dpg.add_text("Loading commands...", tag="commands_text")
                            dpg.add_text("Loading custom commands...", tag="custom_commands_text")
                            dpg.add_text("Current theme: default", tag="current_theme_text")
                            dpg.add_text("Nitro sniper: enabled", tag="nitro_sniper_text")
                            dpg.add_text("Giveaway joiner: enabled", tag="giveaway_joiner_text")
                            dpg.add_text("Giveaway delay: 1 minute/s", tag="giveaway_delay_text")
                            dpg.add_text("Privnote sniper: enabled", tag="privnote_sniper_text")
                            dpg.add_text("Auto delete delay: 30 seconds", tag="delete_delay_text")

                with dpg.tab(label="Logs"):
                    with dpg.child_window(label="Logs Window"):
                        dpg.add_text("Logs")
                        dpg.add_separator()
                        dpg.add_text("Nothing logged yet", tag="logs_text")

                with dpg.tab(label="Scripts"):
                    with dpg.tab_bar(tag="scripts_tab_bar"):
                        with dpg.tab(label="Loader"):
                            with dpg.group(horizontal=True):
                                with dpg.child_window(label="Child Window", width=258):
                                    dpg.add_text("Scripts")
                                    dpg.add_separator()
                                    dpg.add_spacer()
                                    dpg.add_button(label="Reload Scripts", callback=reload_scripts, width=242, height=25)
                                    scripts.extend(filename[:-3] for filename in os.listdir('data/scripts') if filename.endswith('.py'))
                                    dpg.add_listbox(scripts, tag="scripts_listbox", width=242)
                                with dpg.child_window(label="Child Window", width=258):
                                    dpg.add_text("Scripts Control")
                                    dpg.add_separator()
                                    dpg.add_spacer()
                                    dpg.add_button(label="Load", callback=load_script, width=242, height=25)
                                    dpg.add_button(label="Unload", callback=unload_script, width=242, height=25, enabled=True)
                                    dpg.add_text("Loaded scripts: 0", tag="loaded_scripts_text")
                                    dpg.add_listbox(loaded_scripts, tag="loaded_scripts_listbox", width=242)
                                dpg.add_text("Hello, world")

                with dpg.tab(label="Sniper"):
                    dpg.add_text("Hello, world")

                with dpg.tab(label="Protections"):
                    dpg.add_text("Hello, world")

                with dpg.tab(label="Misc"):
                    with dpg.tab_bar(tag="second_tab_bar"):
                        with dpg.tab(label="Commands List"):
                            dpg.add_text("Hello, world")

                        with dpg.tab(label="Rich Presence"):
                            dpg.add_text("Hello, world")

                with dpg.tab(label="Settings"):
                    with dpg.tab_bar(tag="third_tab_bar"):
                        with dpg.tab(label="Config"):
                            dpg.add_text("Hello, world")

                        with dpg.tab(label="Theme"):
                            dpg.add_text("Hello, world")

            # with dpg.child_window(label="Child Window", height=532):
            #     dpg.add_text("test")

    dpg.add_spacer()

    with dpg.child_window(label="Child Window", height=38, no_scrollbar=True):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Content-Type': 'application/json',
            'authorization': get_key("token")
        }
        r = requests.get("https://discord.com/api/v10/users/@me", headers=headers).json()

        dpg.add_text(f"Logging into {r['username']}#{r['discriminator']}...", tag='status')

# -----------------------------------------------------------------------------------------

with dpg.font_registry():
    default_font = dpg.add_font("c:/windows/fonts/arial.ttf", 15)

dpg.bind_font(default_font)

style.load_themes()
dpg.bind_theme("Dark")


def start_gui(debug):
    # authentication_process()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("primary_window", True)
    if debug is False:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    dpg.start_dearpygui()
    dpg.destroy_context()


# ----------------------------------------------------------------------------------------------------------------------


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
