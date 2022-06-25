import dearpygui.dearpygui as dpg
import urllib
from datetime import datetime
import os

from Authentication.atlas import *
from Functions import *
from variables import *
from Encryption import *
from Encryption.CEAShim256 import *

# //////////////////////////////////////////////////////////////////////////
# Create viewport and bind font
# //////////////////////////////////////////////////////////////////////////

dpg.create_context()
dpg.create_viewport(
    title='Luna', width=760, height=600, resizable=False, decorated=True, clear_color=(114, 137, 218, 255), small_icon="data/resources/luna.ico", large_icon="data/resources/luna.ico"
    )

with dpg.font_registry():
    default_font = dpg.add_font("C:/Windows/Fonts/arial.ttf", 13)

dpg.bind_font(default_font)


# //////////////////////////////////////////////////////////////////////////
# Functions
# //////////////////////////////////////////////////////////////////////////

def close_account():
    files.remove('data/auth.luna', documents=False)
    os._exit(0)

def close_token():
    files.remove('data/discord.luna', documents=False)
    os._exit(0)

# //////////////////////////////////////////////////////////////////////////
# Create Windows
# //////////////////////////////////////////////////////////////////////////

def button_main_window():
    dpg.show_item("luna_ascii")
    dpg.show_item("user_info")
    dpg.show_item("luna_info")
    dpg.show_item("discord_info")
    dpg.show_item("general_info")
    dpg.show_item("motd_info")
    dpg.hide_item("general_settings")
    dpg.hide_item("theme_settings")
    dpg.hide_item("sniper_settings")
    dpg.hide_item("privacy_settings")

def button_general_window():
    dpg.show_item("general_settings")
    dpg.show_item("theme_settings")
    dpg.show_item("privacy_settings")
    dpg.hide_item("user_info")
    dpg.hide_item("luna_info")
    dpg.hide_item("discord_info")
    dpg.hide_item("general_info")
    dpg.hide_item("motd_info")
    dpg.hide_item("sniper_settings")
    dpg.hide_item("luna_ascii")

def button_sniper_window():
    dpg.show_item("sniper_settings")
    dpg.hide_item("user_info")
    dpg.hide_item("luna_info")
    dpg.hide_item("discord_info")
    dpg.hide_item("general_info")
    dpg.hide_item("motd_info")
    dpg.hide_item("general_settings")
    dpg.hide_item("theme_settings")
    dpg.hide_item("luna_ascii")
    dpg.hide_item("privacy_settings")

with dpg.window(tag="side_bar", width=140, height=500, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, no_bring_to_front_on_focus=True, pos=(0, 1)) as side_bar:
    width, height, channels, data = dpg.load_image("data/resources/luna.png")

    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    dpg.add_image(texture_id, width=75, height=75, pos=(32, 18))
    dpg.add_spacer(height=94)
    dpg.add_button(label="Main", tag="button_main", callback=button_main_window)
    dpg.add_button(label="General", tag="button_general", callback=button_general_window)
    dpg.add_button(label="Sniper", tag="button_sniper", callback=button_sniper_window)

with dpg.window(tag="main_window", width=604, height=500, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(140, 1), no_bring_to_front_on_focus=True) as main_window:

    width, height, channels, data = dpg.load_image("data/resources/luna_ascii.png")
    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    dpg.add_image(texture_id, tag="luna_ascii", width=570, height=119, pos=(10, 9))

    with dpg.child_window(tag="user_info", width=278, height=84, pos=(16, 135), show=True):
        dpg.add_text("User", indent=3)
        with dpg.group(label="user_group", indent=10):
            luna_user = dpg.add_text("Unknown User")
            luna_uid_text = dpg.add_text("UID: Unknown")

    with dpg.child_window(tag="discord_info", width=278, height=108, pos=(16, 235), show=True):
        dpg.add_text("Discord", indent=3)
        with dpg.group(label="discord_group", indent=10):
            logged = dpg.add_text("Idle")
            friends_text = dpg.add_text("Loading Friends...")
            guilds_text = dpg.add_text("Loading Guilds...")

    with dpg.child_window(tag="general_info", width=278, height=108, pos=(16, 359), show=True):
        dpg.add_text("Info", indent=3)
        with dpg.group(label="general_info_group", indent=10):
            dpg.add_text("92 Platinum Users")
            commands_used_text = dpg.add_text("Commands Used: 0")
            uptime_text = dpg.add_text("Uptime: Loading...")

    with dpg.child_window(tag="luna_info", width=278, height=246, pos=(310, 135), show=True):
        dpg.add_text("Luna", indent=3)
        with dpg.group(label="luna_group", indent=10):
            prefix = files.json("data/config.json", "prefix", documents=False)
            prefix_text = dpg.add_text(f"Prefix: {prefix}")
            commands_amount_text = dpg.add_text("Loading Commands...")
            custom_amount_text = dpg.add_text("Loading custom commands...")
            current_theme_text = dpg.add_text("Current Theme: default")
            nitro_sniper_text = dpg.add_text("Nitro Sniper: On")
            giveaway_joiner_text = dpg.add_text("Giveaway Joiner: On")
            giveaway_joiner_delay_text = dpg.add_text("Giveaway Joiner Delay: 1 Minute/s")
            privnote_sniper_text = dpg.add_text("Privnote Sniper: On")
            auto_delete_delay_text = dpg.add_text("Auto Delete Delay: 40 Seconds")

    with dpg.child_window(tag="motd_info", width=278, height=62, pos=(310, 397), show=True):
        dpg.add_text("MOTD", indent=3)
        with dpg.group(label="motd_group", indent=10):
            motd = urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ')
            for line in motd:
                motd = line.decode().strip()
            dpg.add_text(motd)

    with dpg.child_window(tag="sniper_settings", width=278, height=256, pos=(16, 16), show=False):
        dpg.add_text("Sniper", indent=3)
        with dpg.group(label="sniper_group", indent=10):
            dpg.add_spacer(height=1)
            dpg.add_checkbox(label="Nitro Sniper", default_value=True)
            dpg.add_spacer(height=1)
            dpg.add_checkbox(label="Ratelimit Status", default_value=False)
            dpg.add_spacer(height=1)
            dpg.add_checkbox(label="Privnote Sniper", default_value=True)
            dpg.add_spacer(height=1)
            dpg.add_checkbox(label="Giveaway Joiner", default_value=True)
            dpg.add_text("Giveaway Joiner Delay (Minutes)")
            minutes_slider = dpg.add_slider_int(default_value=1, min_value=1, max_value=60, width=242)
            dpg.add_spacer(height=1)
            dpg.add_button(label="Save")
            dpg.add_spacer(height=1)
            dpg.add_checkbox(label="Guild Joiner On Giveaways", default_value=False)

    with dpg.child_window(tag="general_settings", width=278, height=192, pos=(16, 16), show=False):
        dpg.add_text("General", indent=3)
        with dpg.group(label="general_group", indent=10):
            dpg.add_text("Prefix")
            gui_input_prefix = dpg.add_input_text(default_value=".", width=242)
            dpg.add_spacer(height=1)
            dpg.add_button(label="Save Prefix")
            dpg.add_text("Delete Timer (Seconds)")
            gui_delete_timer = dpg.add_slider_int(default_value=1, min_value=0, max_value=300, width=242)
            dpg.add_spacer(height=1)
            dpg.add_button(label="Save Delete Timer")

    with dpg.child_window(tag="privacy_settings", width=278, height=70, pos=(16, 224), show=False):
        dpg.add_text("Privacy", indent=3)
        with dpg.group(label="privacy_group", indent=10):
            dpg.add_spacer(height=1)
            dpg.add_checkbox(label="Privacy Mode", tag="privacy_checkbox", default_value=False)

    with dpg.child_window(tag="theme_settings", width=278, height=338, pos=(310, 16), show=False):
        dpg.add_text("Theme", indent=3)
        with dpg.group(label="theme_group", indent=10):
            themes = ['default', 'luna']
            dpg.add_text("Themes")
            themes_box = dpg.add_combo(items=themes, default_value=themes[0], width=242)
            dpg.add_spacer(height=1)
            with dpg.group(horizontal=True, label="group_buttons"):
                dpg.add_button(label="Reload")
                dpg.add_button(label="Delete")
            dpg.add_spacer(height=1)
            dpg.add_checkbox(label="Protections Footer", default_value=True)
            dpg.add_text("Name")
            editor_theme = dpg.add_input_text(default_value="Luna", width=242)
            dpg.add_text("Title")
            editor_title = dpg.add_input_text(default_value="Luna", width=242)
            dpg.add_text("Footer")
            editor_footer = dpg.add_input_text(default_value="www.team-luna.org", width=242)
            dpg.add_spacer(height=1)
            description_footer = dpg.add_checkbox(label="Description", default_value=True)
            dpg.add_spacer(height=1)
            dpg.add_button(label="Save")

with dpg.window(tag="logs_window", width=604, height=500, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(140, 1), no_bring_to_front_on_focus=True, show=False) as logs_window:

    with dpg.child_window(label="Logs", width=572, height=468, pos=(16, 16)):
        dpg.add_text("Logs", indent=3)
        with dpg.group(label="logs_group", indent=10):
            logs_block = dpg.add_text("No Commands Used Yet")

with dpg.window(tag="misc_window", width=604, height=500, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(140, 1), no_bring_to_front_on_focus=True, show=False) as misc_window:

    with dpg.child_window(label="Misc", width=278, height=320, pos=(16, 16)):
        dpg.add_text("Misc", indent=3)
        with dpg.group(label="misc_group", indent=10):
            dpg.add_spacer(height=1)
            dpg.add_button(label="Logout Account", callback=close_account)
            dpg.add_spacer(height=1)
            dpg.add_button(label="Logout Token", callback=close_token)

    with dpg.child_window(label="Misc", width=278, height=320, pos=(310, 16)):
        dpg.add_text("Misc", indent=3)


# //////////////////////////////////////////////////////////////////////////
# Functions for the bottom bar
# //////////////////////////////////////////////////////////////////////////


def toggle_main_window():
    dpg.show_item("main_window")
    dpg.hide_item("logs_window")
    dpg.hide_item("misc_window")
    dpg.show_item(main_text_colored)
    dpg.hide_item(main_text)
    dpg.show_item(logs_text)
    dpg.hide_item(logs_text_colored)
    dpg.show_item(misc_text)
    dpg.hide_item(misc_text_colored)
    dpg.show_item("button_main")
    dpg.show_item("button_general")
    dpg.show_item("button_sniper")


def toggle_logs_window():
    dpg.show_item("logs_window")
    dpg.hide_item("main_window")
    dpg.hide_item("misc_window")
    dpg.show_item(main_text)
    dpg.hide_item(main_text_colored)
    dpg.show_item(logs_text_colored)
    dpg.hide_item(logs_text)
    dpg.show_item(misc_text)
    dpg.hide_item(misc_text_colored)
    dpg.hide_item("button_main")
    dpg.hide_item("button_general")
    dpg.hide_item("button_sniper")


def toggle_misc_window():
    dpg.show_item("misc_window")
    dpg.hide_item("main_window")
    dpg.hide_item("logs_window")
    dpg.show_item(main_text)
    dpg.hide_item(main_text_colored)
    dpg.show_item(logs_text)
    dpg.hide_item(logs_text_colored)
    dpg.show_item(misc_text_colored)
    dpg.hide_item(misc_text)
    dpg.hide_item("button_main")
    dpg.hide_item("button_general")
    dpg.hide_item("button_sniper")


# //////////////////////////////////////////////////////////////////////////
# Bottom Bar
# //////////////////////////////////////////////////////////////////////////


with dpg.window(tag="bottom_bar", width=744, height=10, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(0, 502), no_bring_to_front_on_focus=True) as bottom_bar:
    with dpg.group(horizontal=True, label="tab_buttons", indent=290, pos=(0, 5)):

        width, height, channels, data = dpg.load_image("data/resources/home.png")
        with dpg.texture_registry():
            texture_home = dpg.add_static_texture(width, height, data)

        width, height, channels, data = dpg.load_image("data/resources/logs.png")
        with dpg.texture_registry():
            texture_logs = dpg.add_static_texture(width, height, data)

        width, height, channels, data = dpg.load_image("data/resources/misc.png")
        with dpg.texture_registry():
            texture_misc = dpg.add_static_texture(width, height, data)

        dpg.add_image_button(texture_home, width=28, height=28, callback=toggle_main_window, indent=2)
        dpg.add_image_button(texture_logs, width=30, height=30, callback=toggle_logs_window)
        dpg.add_image_button(texture_misc, width=28, height=28, callback=toggle_misc_window, indent=95)
    with dpg.group(horizontal=True, label="tab_text", indent=290):
        main_text = dpg.add_text("Main", indent=6, pos=(0, 40), show=False)
        logs_text = dpg.add_text("Logs", indent=52, pos=(0, 40))
        misc_text = dpg.add_text("Misc", indent=100, pos=(0, 40))
        main_text_colored = dpg.add_text("Main", indent=6, pos=(0, 40), color=(114, 137, 218, 255))
        logs_text_colored = dpg.add_text("Logs", indent=52, pos=(0, 40), show=False, color=(114, 137, 218, 255))
        misc_text_colored = dpg.add_text("Misc", indent=100, pos=(0, 40), show=False, color=(114, 137, 218, 255))


# //////////////////////////////////////////////////////////////////////////
# Theme Settings
# //////////////////////////////////////////////////////////////////////////


with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        # dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 6, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0, category=dpg.mvThemeCat_Core)
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
        dpg.add_theme_color(dpg.mvThemeCol_Text, (201, 201, 201, 255), category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

with dpg.theme() as main_window_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (21, 21, 21, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (31, 31, 31, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Border, (41, 41, 41, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (21, 21, 21, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)

        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 5, category=dpg.mvThemeCat_Core)

dpg.bind_item_theme(main_window, main_window_theme)

with dpg.theme() as logs_window_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (21, 21, 21, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (31, 31, 31, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Border, (41, 41, 41, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (21, 21, 21, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)

        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 5, category=dpg.mvThemeCat_Core)

dpg.bind_item_theme(logs_window, logs_window_theme)


with dpg.theme() as misc_window_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (21, 21, 21, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (31, 31, 31, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Border, (41, 41, 41, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (21, 21, 21, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (114, 137, 218, 255), category=dpg.mvThemeCat_Core)

        dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 5, category=dpg.mvThemeCat_Core)

dpg.bind_item_theme(misc_window, misc_window_theme)


with dpg.theme() as side_bar_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Border, (31, 31, 31, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (31, 31, 31, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (31, 31, 31, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (26, 26, 26, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (26, 26, 26, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (31, 31, 131, 255), category=dpg.mvThemeCat_Core)


dpg.bind_item_theme(side_bar, side_bar_theme)

with dpg.theme() as bottom_bar_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (41, 41, 41, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (41, 41, 41, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (41, 41, 41, 255), category=dpg.mvThemeCat_Core)

dpg.bind_item_theme(bottom_bar, bottom_bar_theme)


# //////////////////////////////////////////////////////////////////////////
# Create viewport and context
# //////////////////////////////////////////////////////////////////////////

def start_gui():
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()