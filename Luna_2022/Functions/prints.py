from FileHandling.jsonhandler import JsonHandler
import pwinput
from FileHandling.jsonhandler import *
from Functions.color import *
from time import localtime, strftime


class prints:
    if JsonHandler("console.json", "data/console").read_value("spacers") == True:
        spacer_2 = " " + JsonHandler("console.json", "data/console").read_value("spacer") + " "
    else:
        spacer_2 = " "
    if JsonHandler("console.json", "data/console").read_value("spacers") == True and JsonHandler("console.json", "data/console").read_value("time_stamp") == True:
        spacer_1 = " " + JsonHandler("console.json", "data/console").read_value("spacer") + " "
    elif JsonHandler("console.json", "data/console").read_value("spacers") == True and JsonHandler("console.json", "data/console").read_value("time_stamp") == False:
        spacer_1 = ""
    else:
        spacer_1 = " "

    def command(text: str):
        """Prints a command log."""
        if JsonHandler("console.json", "data/console").read_value("time_stamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Command")}{prints.spacer_2}{get_prefix()}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Command")}{prints.spacer_2}{get_prefix()}{text}')

    def shared(text: str):
        """Prints a shared log."""
        if JsonHandler("console.json", "data/console").read_value("time_stamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Sharing")}{prints.spacer_2}{get_prefix()}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Sharing")}{prints.spacer_2}{get_prefix()}{text}')

    def message(text: str):
        """Prints a message log."""
        if JsonHandler("console.json", "data/console").read_value("time_stamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Message")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Message")}{prints.spacer_2}{text}')

    def sniper(text: str):
        """Prints a sniper log."""
        if JsonHandler("console.json", "data/console").read_value("time_stamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Sniper ")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Sniper ")}{prints.spacer_2}{text}')

    def event(text: str):
        """Prints a event log."""
        if JsonHandler("console.json", "data/console").read_value("time_stamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient(" Event ")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient(" Event ")}{prints.spacer_2}{text}')

    def selfbot(text: str):
        """Prints a selfbot log."""
        if JsonHandler("console.json", "data/console").read_value("time_stamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Selfbot")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Selfbot")}{prints.spacer_2}{text}')

    def error(text: str):
        """Prints a error log."""
        if JsonHandler("console.json", "data/console").read_value("time_stamp") == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.error} Error {color.reset}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.error} Error {color.reset}{prints.spacer_2}{text}')

    def input(text: str):
        """Prints a input input."""
        if JsonHandler("console.json", "data/console").read_value("time_stamp") == True:
            var = input(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ')
        else:
            var = input(f'{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ')
        return var

    def password(text: str):
        """Prints a password input. Masked with `*`"""
        if JsonHandler("console.json", "data/console").read_value("time_stamp") == True:
            password = pwinput.pwinput(prompt=f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ', mask='*')
        else:
            password = pwinput.pwinput(prompt=f'{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ', mask='*')
        return password