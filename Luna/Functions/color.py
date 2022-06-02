from Functions import *


# ///////////////////////////////////////////////////////////////
# ANSI Colors & Gradients

class color:
    error = '\033[38;2;225;9;89m'
    reset = "\033[0m"

    def logo_gradient(text):
        """Gradient for the logo"""
        gradient = files.json(
            "data/console/console.json",
            "logo_gradient", documents=False
        )
        match gradient:
            case "1":
                return color.purple_blue(f"""{text}""")
            case "2":
                return color.purple_cyan(f"""{text}""")
            case "3":
                return color.pink_red(f"""{text}""")
            case "4":
                return color.blue_cyan(f"""{text}""")
            case "5":
                return color.green_blue(f"""{text}""")
            case "6":
                return color.orange_red(f"""{text}""")
            case "7":
                return color.black_white(f"""{text}""")
        if int(gradient) > 7:
            return color.purple_blue(f"""{text}""")

    def print_gradient(text):
        """Gradient for the console"""
        gradient = files.json(
            "data/console/console.json",
            "print_gradient", documents=False
        )
        match gradient:
            case "1":
                return color.purple(f"{text}")
            case "2":
                return color.blue(f"{text}")
            case "3":
                return color.pink(f"{text}")
            case "4":
                return color.yellow(f"{text}")
            case "5":
                return color.green(f"{text}")
            case "6":
                return color.red(f"{text}")
            case "7":
                return color.black(f"{text}")
        if int(gradient) > 7:
            return color.purple(f"{text}")

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
                if blue > 255:
                    blue = 255
                faded += f"\033[38;2;0;255;{blue}m{character}\033[0m"
        return faded

    def blue(text):
        os.system("")
        faded = ""
        for line in text.splitlines():
            green = 0
            for character in line:
                green += 20
                if green > 255:
                    green = 255
                faded += f"\033[38;2;0;{green};255m{character}\033[0m"
        return faded

    def pink(text):
        os.system("")
        faded = ""
        for line in text.splitlines():
            blue = 255
            for character in line:
                blue -= 20
                if blue < 0:
                    blue = 0
                faded += f"\033[38;2;255;0;{blue}m{character}\033[0m"
        return faded

    def yellow(text):
        os.system("")
        faded = ""
        for line in text.splitlines():
            red = 0
            for character in line:
                if not red > 200:
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
                if green < 0:
                    green = 0
                faded += f"\033[38;2;255;{green};0m{character}\033[0m"
        return faded

    def purple(text):
        os.system("")
        faded = ""
        down = False
        for line in text.splitlines():
            red = 114
            green = 137
            blue = 218
            for character in line:

                if down:
                    blue -= 3
                else:
                    blue += 3
                if blue > 254:
                    blue = 255
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
        red = 114
        green = 137
        blue = 218
        for line in text.splitlines():
            faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
            if not green == 0:
                green -= 5
                if green < 0:
                    green = 0
            if not blue == 255:
                blue += 5
                if blue > 255:
                    blue = 255
        return faded

    def purple_cyan(text):
        os.system("")
        faded = ""
        red = 0
        green = 255
        blue = 255
        for line in text.splitlines():
            faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
            if not red == 255:
                red += 22
                if red < 0:
                    red = 0
            if not green == 0:
                green -= 40
                if green < 0:
                    green = 0
        return faded

    def pink_red(text):
        os.system("")
        faded = ""
        blue = 255
        for line in text.splitlines():
            faded += f"\033[38;2;255;0;{blue}m{line}\033[0m\n"
            if not blue == 0:
                blue -= 20
                if blue < 0:
                    blue = 0
        return faded

    def black_white(text):
        os.system("")
        faded = ""
        red = 25
        green = 25
        blue = 25
        for line in text.splitlines():
            faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
            if not red == 255 and not green == 255 and not blue == 255:
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
            if not green == 255:
                green += 15
                if green > 255:
                    green = 255
        return faded

    def green_blue(text):
        os.system("")
        faded = ""
        blue = 100
        for line in text.splitlines():
            faded += f"\033[38;2;0;255;{blue}m{line}\033[0m\n"
            if not blue == 255:
                blue += 15
                if blue > 255:
                    blue = 255
        return faded

    def orange_red(text):
        os.system("")
        faded = ""
        green = 250
        for line in text.splitlines():
            faded += f"\033[38;2;255;{green};0m{line}\033[0m\n"
            if not green == 0:
                green -= 25
                if green < 0:
                    green = 0
        return faded
