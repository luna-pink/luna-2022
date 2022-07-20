import ctypes
import time

from win32api import GetSystemMetrics
import dearpygui.dearpygui as dpg
import style
from style.palette import rose_pine


# ----------------------------------------------------------------------------------------------------------------------

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

window_width = 740
window_height = 570

x_pos = int((screen_width - window_width) / 2)
y_pos = int((screen_height - window_height) / 2)

trigger = False

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


def resize():
    global window_width, window_height, trigger
    trigger = not trigger
    for _ in range(25):
        if not trigger:
            window_width -= 5
            window_height -= 5
        else:
            window_width += 5
            window_height += 5
        x_pos = int((screen_width - window_width) / 2)
        y_pos = int((screen_height - window_height) / 2)
        dpg.configure_viewport("Luna", height=window_height, width=window_width, x_pos=x_pos, y_pos=y_pos)
        time.sleep(0.001)


with dpg.window(tag="Primary Window"):

    with dpg.child_window(label="Child Window", height=38, no_scrollbar=True):
        dpg.add_text("Nshout 1", color=rose_pine.subtle)

    dpg.add_spacer()

    with dpg.group(horizontal=True):
        with dpg.child_window(label="Child Window", width=160, height=422):
            width, height, channels, data = dpg.load_image("data/resources/luna.png")
            with dpg.texture_registry():
                texture_id = dpg.add_static_texture(width, height, data)

            dpg.add_image(texture_id, width=75, height=75, pos=(40, 13))

            dpg.add_spacer(height=90)
            dpg.add_separator()

            # dpg.add_text("Start Luna")
            dpg.add_spacer()
            dpg.add_button(label="Button", callback=resize, width=144, height=25)
            dpg.add_spacer()
            dpg.add_button(label="Style", callback=dpg.show_style_editor, width=144, height=25)

        with dpg.child_window(label="Child Window", height=422, tag="main_window"): # width 600, height 532
            with dpg.tab_bar(tag="top_tab_bar"):
                with dpg.tab(label="Home"):
                    width, height, channels, data = dpg.load_image("data/resources/luna_ascii.png")
                    with dpg.texture_registry():
                        texture_id = dpg.add_static_texture(width, height, data)

                    dpg.add_image(texture_id, tag="luna_ascii", width=516, height=108) # , width=516, height=108 / , width=690, height=144

                    with dpg.group(horizontal=True):
                        with dpg.child_window(label="Child Window", width=258): # 342
                            dpg.add_text("Discord")
                            dpg.add_separator()
                            dpg.add_text("Not logged in")
                            dpg.add_text("Loading friends...")
                            dpg.add_text("Loading guilds...")
                            dpg.add_text("Loading status...")
                            dpg.add_text("Loading settings...")
                            dpg.add_text("Loading nitro...")

                        with dpg.child_window(label="Child Window", width=258):
                            dpg.add_text("Luna")
                            dpg.add_separator()
                            dpg.add_text("Prefix: .")
                            dpg.add_text("Loading commands...")
                            dpg.add_text("Loading custom commands...")
                            dpg.add_text("Current theme: default")
                            dpg.add_text("Nitro sniper: enabled")
                            dpg.add_text("Giveaway joiner: enabled")
                            dpg.add_text("Giveaway delay: 1 minute/s")
                            dpg.add_text("Privnote sniper: enabled")
                            dpg.add_text("Auto delete delay: 30 seconds")


                with dpg.tab(label="Logs"):
                    with dpg.child_window(label="Logs Window"):
                        dpg.add_text("Logs")
                        dpg.add_separator()
                        dpg.add_text("Nothing logged yet")

                with dpg.tab(label="Scripts"):
                    with dpg.tab_bar(tag="scripts_tab_bar"):
                        with dpg.tab(label="Editor"):
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
        dpg.add_text("Logging into Nshout#0001...", color=rose_pine.subtle)

# -----------------------------------------------------------------------------------------

with dpg.tab(label="Custom Window", parent="scripts_tab_bar"):
    with dpg.group(horizontal=True):
        with dpg.child_window(label="Child Window", width=258):
            dpg.add_text("Window 1")
        with dpg.child_window(label="Child Window", width=258):
            dpg.add_text("Window 2")

with dpg.font_registry():
    default_font = dpg.add_font("c:/windows/fonts/arial.ttf", 15)

dpg.bind_font(default_font)

style.load_themes()
dpg.bind_theme("Dark")


def start_gui():
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    start_gui()
