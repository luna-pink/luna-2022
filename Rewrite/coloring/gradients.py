import os


def black(text):
    os.system("")
    faded = ""
    for line in text.splitlines():
        red = 25
        green = 25
        blue = 25
        for character in line:
            red += 20
            green += 20
            blue += 20
            if red > 255 and green > 255 and blue > 255:
                red = 255
                green = 255
                blue = 255
            faded += f"\033[38;2;{red};{green};{blue}m{character}\033[0m"
    return faded


def green(text):
    os.system("")
    faded = ""
    for line in text.splitlines():
        blue = 100
        for character in line:
            blue += 20
            blue = min(blue, 255)
            faded += f"\033[38;2;0;255;{blue}m{character}\033[0m"
    return faded


def blue(text):
    os.system("")
    faded = ""
    for line in text.splitlines():
        green = 0
        for character in line:
            green += 20
            green = min(green, 255)
            faded += f"\033[38;2;0;{green};255m{character}\033[0m"
    return faded


def pink(text):
    os.system("")
    faded = ""
    for line in text.splitlines():
        blue = 255
        for character in line:
            blue -= 20
            blue = max(blue, 0)
            faded += f"\033[38;2;255;0;{blue}m{character}\033[0m"
    return faded


def yellow(text):
    os.system("")
    faded = ""
    for line in text.splitlines():
        red = 0
        for character in line:
            if red <= 200:
                red += 20
            faded += f"\033[38;2;{red};255;0m{character}\033[0m"
    return faded


def red(text):
    os.system("")
    faded = ""
    for line in text.splitlines():
        green = 250
        for character in line:
            green -= 20
            green = max(green, 0)
            faded += f"\033[38;2;255;{green};0m{character}\033[0m"
    return faded


def purple(text):
    os.system("")
    faded = ""
    down = False
    blue = 255
    for line in text.splitlines():
        red = 137
        green = 142
        for character in line:

            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False

            if down:
                green += 3
            else:
                green -= 3
            if green > 254:
                green = 255
                down = True
            elif green < 1:
                green = 30
                down = False

            faded += f"\033[38;2;{red};{green};{blue}m{character}\033[0m"
    return faded


def purple_blue(text):
    os.system("")
    faded = ""
    red = 137
    green = 142
    blue = 255
    for line in text.splitlines():
        faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
        if green != 0:
            green -= 5
            green = max(green, 0)
        if red != 255:
            red += 5
            red = min(red, 255)
    return faded


def purple_cyan(text):
    os.system("")
    faded = ""
    red = 0
    green = 255
    blue = 255
    for line in text.splitlines():
        faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
        if red != 255:
            red += 22
            red = max(red, 0)
        if green != 0:
            green -= 40
            green = max(green, 0)
    return faded


def pink_red(text):
    os.system("")
    faded = ""
    blue = 255
    for line in text.splitlines():
        faded += f"\033[38;2;255;0;{blue}m{line}\033[0m\n"
        if blue != 0:
            blue -= 20
            blue = max(blue, 0)
    return faded


def black_white(text):
    os.system("")
    faded = ""
    red = 25
    green = 25
    blue = 25
    for line in text.splitlines():
        faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
        if red != 255 and green != 255 and blue != 255:
            red += 10
            green += 10
            blue += 10
            if red > 255 and green > 255 and blue > 255:
                red = 255
                green = 255
                blue = 255
    return faded


def blue_cyan(text):
    os.system("")
    faded = ""
    green = 10
    for line in text.splitlines():
        faded += f"\033[38;2;0;{green};255m{line}\033[0m\n"
        if green != 255:
            green += 15
            green = min(green, 255)
    return faded


def green_blue(text):
    os.system("")
    faded = ""
    blue = 100
    for line in text.splitlines():
        faded += f"\033[38;2;0;255;{blue}m{line}\033[0m\n"
        if blue != 255:
            blue += 15
            blue = min(blue, 255)
    return faded


def orange_red(text):
    os.system("")
    faded = ""
    green = 250
    for line in text.splitlines():
        faded += f"\033[38;2;255;{green};0m{line}\033[0m\n"
        if green != 0:
            green -= 25
            green = max(green, 0)
    return faded
