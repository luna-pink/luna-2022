from turtle import color
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(
    title='Luna', width=760, height=600, resizable=False, decorated=True, clear_color=(114, 137, 218, 255), small_icon="data/resources/luna.ico", large_icon="data/resources/luna.ico"
    )

with dpg.font_registry():
    default_font = dpg.add_font("C:/Windows/Fonts/arial.ttf", 13)

dpg.bind_font(default_font)

with dpg.window(tag="side_bar", width=140, height=500, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, no_bring_to_front_on_focus=True, pos=(0, 1)) as side_bar:
    width, height, channels, data = dpg.load_image("data/resources/luna.png")

    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    dpg.add_image(texture_id, width=75, height=75, pos=(32, 18))

with dpg.window(tag="main_window", width=604, height=500, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(140, 1), no_bring_to_front_on_focus=True) as main_window:

    width, height, channels, data = dpg.load_image("data/resources/luna_ascii.png")
    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    with dpg.child_window(label="Sniper Settings", width=278, height=150, pos=(16, 135)):
        dpg.add_text("Default", indent=3)
        with dpg.group(label="sniper_group", indent=10):
            dpg.add_text("Test")

    with dpg.child_window(label="Sniper Settings", width=278, height=150, pos=(16, 300)):
        dpg.add_text("Default", indent=3)
        with dpg.group(label="sniper_group", indent=10):
            dpg.add_text("Test")

    with dpg.child_window(label="Theme Settings", width=278, height=468, pos=(310, 135)):
        dpg.add_text("Default Theme Selected", indent=3)

    dpg.add_image(texture_id, width=570, height=119, pos=(10, 9))

with dpg.window(tag="logs_window", width=604, height=500, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(140, 1), no_bring_to_front_on_focus=True, show=False) as logs_window:

    with dpg.child_window(label="Logs", width=572, height=468, pos=(16, 16)):
        dpg.add_text("Logs", indent=3)
        with dpg.group(label="logs_group", indent=10):
            logs_text = dpg.add_text("No Commands Used Yet")

with dpg.window(tag="misc_window", width=604, height=500, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(140, 1), no_bring_to_front_on_focus=True, show=False) as misc_window:

    with dpg.child_window(label="Misc", width=278, height=500, pos=(16, 16)):
        dpg.add_text("Misc", indent=3)

    with dpg.child_window(label="Misc", width=278, height=320, pos=(310, 16)):
        dpg.add_text("Misc", indent=3)


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
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (31, 31, 31, 255), category=dpg.mvThemeCat_Core)

dpg.bind_item_theme(side_bar, side_bar_theme)

with dpg.theme() as bottom_bar_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (41, 41, 41, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (41, 41, 41, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (41, 41, 41, 255), category=dpg.mvThemeCat_Core)
        # dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (41, 41, 41, 255), category=dpg.mvThemeCat_Core)

dpg.bind_item_theme(bottom_bar, bottom_bar_theme)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
