from time import strftime, localtime
import dearpygui.dearpygui as dpg

logs = ""


def log(log_type: str, message: str):
    global logs
    for line in message.split('\n'):
        print(f"{strftime('%H:%M', localtime())} |{f' {log_type.title()}':<9}| {line}")
        logs += f"{strftime('%H:%M', localtime())} |{f' {log_type.title()}':<9}| {line}\n"
        dpg.set_value("logs_text", logs)
    return
