import ctypes
from win32api import GetSystemMetrics
import dearpygui.dearpygui as dpg
import style


# ----------------------------------------------------------------------------------------------------------------------

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

width = 960
height = 680

x_pos = int((screen_width - width) / 2)
y_pos = int((screen_height - height) / 2)

# ----------------------------------------------------------------------------------------------------------------------

dpg.create_context()

dpg.create_viewport(
    title='Luna',
    width=width,
    height=height,
    resizable=False,
    y_pos=y_pos,
    x_pos=x_pos
)

with dpg.window(tag="Primary Window"):
    # dpg.add_text("Hello, world")

    with dpg.child_window(label="Child Window", height=38, no_scrollbar=True):
        dpg.add_text("Hello, world")

    dpg.add_spacer()

    with dpg.group(horizontal=True):
        with dpg.child_window(label="Child Window", width=170, height=532):
            dpg.add_text("Hello, world")

        with dpg.child_window(label="Child Window", width=600, height=532):
            dpg.add_text("Hello, world")

        with dpg.child_window(label="Child Window", width=142, height=532):
            dpg.add_text("Hello, world")

    dpg.add_spacer()

    with dpg.child_window(label="Child Window", height=38, no_scrollbar=True):
        dpg.add_text("Hello, world")

# -----------------------------------------------------------------------------------------

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
