import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(
    title='Luna', width=800, height=600, resizable=False, decorated=True, clear_color=(40, 40, 40, 255), small_icon="data/resources/luna.ico", large_icon="data/resources/luna.ico"
    )

with dpg.window(tag="Primary Window", width=200, height=562, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, no_bring_to_front_on_focus=True):
    width, height, channels, data = dpg.load_image("data/resources/luna.png")

    with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width, height, data)

    dpg.add_image(texture_id, width=19, height=19, pos=(40, 29))
    dpg.add_text("Luna", color=(114, 137, 218, 255))
    dpg.add_text("Welcome back, Nshout")
    dpg.add_separator()
    dpg.add_text("518 Commands")
    dpg.add_text("1 Custom Command Loaded")
    dpg.add_separator()
    # dpg.add_button(label="Save")
    # dpg.add_input_text(label="string", default_value="Quick brown fox")
    # dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

    with dpg.menu_bar():
        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Logout")
            dpg.add_menu_item(label="Style Editor", callback=lambda: dpg.show_tool(dpg.mvTool_Style))
            dpg.add_menu_item(label="Debug", callback=lambda: dpg.show_tool(dpg.mvTool_Debug))

with dpg.window(tag="Secondary Window", width=584, height=562, no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(200, 0), no_bring_to_front_on_focus=True):
    dpg.add_text("Logged into Nshout#0001")
    dpg.add_separator()

    with dpg.window(label="Sniper Settings", width=260, height=320, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(220, 224)):
        dpg.add_text("Default")

    with dpg.window(label="Theme Settings", width=260, height=320, no_resize=True, no_move=True, no_collapse=True, no_close=True, pos=(500, 224)):
        dpg.add_text("Default Theme Selected")

with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 6, category=dpg.mvThemeCat_Core)
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

dpg.bind_theme(global_theme)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
