import time

import dearpygui.dearpygui as dpg


def viewport_resize(item: str = '', duration: int = 10, loop: int = 10, width: int = 0, height: int = 0, final_width: int = 0, final_height: int = 0, center: bool = False):

    viewport_width = dpg.get_viewport_width()
    viewport_height = dpg.get_viewport_height()
    viewport_position = dpg.get_viewport_pos()

    if final_width == 0:
        final_width = viewport_width

    if final_height == 0:
        final_height = viewport_height

    if center:
        viewport_x = viewport_position[0]
        viewport_y = viewport_position[1]
        calculation_width = 0
        calculation_height = 0
        for _ in range(loop):
            calculation_width += width / 2
            calculation_height += height / 2
            viewport_width += width
            if width > 0 and viewport_width > final_width or width <= 0 and viewport_width < final_width:
                viewport_width = final_width
            viewport_height += height
            if height > 0 and viewport_height > final_height or height <= 0 and viewport_height < final_height:
                viewport_height = final_height
            print(viewport_width, viewport_height)
            x_position = viewport_x - calculation_width
            y_position = viewport_y - calculation_height
            dpg.configure_viewport(item, width=viewport_width, height=viewport_height, x_pos=x_position, y_pos=y_position)
            time.sleep(duration / 1000)
    else:
        for _ in range(loop):
            viewport_width += width
            viewport_height += height
            dpg.configure_viewport(item, width=viewport_width, height=viewport_height)
            time.sleep(duration / 1000)
