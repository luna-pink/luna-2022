from time import strftime, localtime

import pwinput

from configs import *


class prints:
    try:
        if files.json("data/console/console.json", "spacers", documents=False):
            spacer_2 = " " + \
                       files.json(
                           "data/console/console.json",
                           "spacer", documents=False
                       ) + " "
        else:
            spacer_2 = " "
        if files.json(
                "data/console/console.json",
                "spacers",
                documents=False
        ) and files.json(
            "data/console/console.json",
            "timestamp",
            documents=False
        ):
            spacer_1 = " " + \
                       files.json(
                           "data/console/console.json",
                           "spacer", documents=False
                       ) + " "
        elif files.json("data/console/console.json", "spacers", documents=False) and files.json(
                "data/console/console.json", "timestamp", documents=False
        ) is False:
            spacer_1 = ""
        else:
            spacer_1 = " "
    except Exception as e:
        print(e)

    def command(self):
        """Prints a command log."""
        if files.json(
                "data/console/console.json",
                "timestamp",
                documents=False
        ):
            return print(f"{strftime('%H:%M', localtime())}{prints.spacer_1}{color.print_gradient('Command')}{prints.spacer_2}{get_prefix()}{self}")

        else:
            return print(f"{prints.spacer_1}{color.print_gradient('Command')}{prints.spacer_2}{get_prefix()}{self}")

    def shared(self):
        """Prints a shared log."""
        if files.json(
                "data/console/console.json",
                "timestamp",
                documents=False
        ):
            return print(f"{strftime('%H:%M', localtime())}{prints.spacer_1}{color.print_gradient('Sharing')}{prints.spacer_2}{get_prefix()}{self}")

        else:
            return print(f"{prints.spacer_1}{color.print_gradient('Sharing')}{prints.spacer_2}{get_prefix()}{self}")

    def message(self):
        """Prints a message log."""
        if files.json(
                "data/console/console.json",
                "timestamp",
                documents=False
        ):
            return print(f"{strftime('%H:%M', localtime())}{prints.spacer_1}{color.print_gradient('Message')}{prints.spacer_2}{self}")

        else:
            return print(f"{prints.spacer_1}{color.print_gradient('Message')}{prints.spacer_2}{self}")

    def sniper(self):
        """Prints a sniper log."""
        if files.json(
                "data/console/console.json",
                "timestamp",
                documents=False
        ):
            return print(f"{strftime('%H:%M', localtime())}{prints.spacer_1}{color.print_gradient('Sniper ')}{prints.spacer_2}{self}")

        else:
            return print(f"{prints.spacer_1}{color.print_gradient('Sniper ')}{prints.spacer_2}{self}")

    def event(self):
        """Prints a event log."""
        if files.json(
                "data/console/console.json",
                "timestamp",
                documents=False
        ):
            return print(f"{strftime('%H:%M', localtime())}{prints.spacer_1}{color.print_gradient(' Event ')}{prints.spacer_2}{self}")

        else:
            return print(f"{prints.spacer_1}{color.print_gradient(' Event ')}{prints.spacer_2}{self}")

    def selfbot(self):
        """Prints a selfbot log."""
        if files.json(
                "data/console/console.json",
                "timestamp",
                documents=False
        ):
            return print(f"{strftime('%H:%M', localtime())}{prints.spacer_1}{color.print_gradient('Selfbot')}{prints.spacer_2}{self}")

        else:
            return print(f"{prints.spacer_1}{color.print_gradient('Selfbot')}{prints.spacer_2}{self}")

    def error(self):
        """Prints a error log."""
        if files.json(
                "data/console/console.json",
                "timestamp",
                documents=False
        ):
            return print(f"{strftime('%H:%M', localtime())}{prints.spacer_1}{color.error} Error {color.reset}{prints.spacer_2}{self}")

        else:
            return print(f'{prints.spacer_1}{color.error} Error {color.reset}{prints.spacer_2}{self}')

    def input(self):
        """Prints an input."""
        return input(f"{strftime('%H:%M', localtime())}{prints.spacer_1}{color.print_gradient(' Input ')}{prints.spacer_2}{self}: ") if files.json(
            "data/console/console.json", "timestamp", documents=False
        ) else input(
            f"{prints.spacer_1}{color.print_gradient(' Input ')}{prints.spacer_2}{self}: "
        )

    def password(self):
        """Prints a password input. Masked with `*`"""
        return pwinput.pwinput(prompt=f"{strftime('%H:%M', localtime())}{prints.spacer_1}{color.print_gradient(' Input ')}{prints.spacer_2}{self}: ", mask='*') if files.json(
            "data/console/console.json", "timestamp", documents=False
        ) else pwinput.pwinput(prompt=f"{prints.spacer_1}{color.print_gradient(' Input ')}{prints.spacer_2}{self}: ", mask='*'
                               )