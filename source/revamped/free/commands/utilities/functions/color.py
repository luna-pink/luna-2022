# pyarmor options: no-spp-mode

# ///////////////////////////////////////////////////////////////
# ANSI Colors & Gradients
import json
import os


class color:
    error = '\033[38;2;225;9;89m'
    reset = "\033[0m"

    def logo_gradient(self):
        """Gradient for the logo"""
        gradient = json.load(open("data/console/console.json", encoding="utf-8"))["logo_gradient"]
        match gradient:
            case "1":
                return color.purple_blue(f"""{self}""")
            case "2":
                return color.purple_cyan(f"""{self}""")
            case "3":
                return color.pink_red(f"""{self}""")
            case "4":
                return color.blue_cyan(f"""{self}""")
            case "5":
                return color.green_blue(f"""{self}""")
            case "6":
                return color.orange_red(f"""{self}""")
            case "7":
                return color.black_white(f"""{self}""")
        if int(gradient) > 7:
            return color.purple_blue(f"""{self}""")

    def print_gradient(self):
        """Gradient for the console"""
        gradient = json.load(open("data/console/console.json", encoding="utf-8"))["print_gradient"]
        match gradient:
            case "1":
                return color.purple(f"{self}")
            case "2":
                return color.blue(f"{self}")
            case "3":
                return color.pink(f"{self}")
            case "4":
                return color.yellow(f"{self}")
            case "5":
                return color.green(f"{self}")
            case "6":
                return color.red(f"{self}")
            case "7":
                return color.black(f"{self}")
        if int(gradient) > 7:
            return color.purple(f"{self}")

    def black(self):
        os.system("")
        faded = ""
        for line in self.splitlines():
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

    def green(self):
        os.system("")
        faded = ""
        for line in self.splitlines():
            blue = 100
            for character in line:
                blue += 20
                blue = min(blue, 255)
                faded += f"\033[38;2;0;255;{blue}m{character}\033[0m"
        return faded

    def blue(self):
        os.system("")
        faded = ""
        for line in self.splitlines():
            green = 0
            for character in line:
                green += 20
                green = min(green, 255)
                faded += f"\033[38;2;0;{green};255m{character}\033[0m"
        return faded

    def pink(self):
        os.system("")
        faded = ""
        for line in self.splitlines():
            blue = 255
            for character in line:
                blue -= 20
                blue = max(blue, 0)
                faded += f"\033[38;2;255;0;{blue}m{character}\033[0m"
        return faded

    def yellow(self):
        os.system("")
        faded = ""
        for line in self.splitlines():
            red = 0
            for character in line:
                if red <= 200:
                    red += 20
                faded += f"\033[38;2;{red};255;0m{character}\033[0m"
        return faded

    def red(self):
        os.system("")
        faded = ""
        for line in self.splitlines():
            green = 250
            for character in line:
                green -= 20
                green = max(green, 0)
                faded += f"\033[38;2;255;{green};0m{character}\033[0m"
        return faded

    def purple(self):
        os.system("")
        faded = ""
        down = False
        for line in self.splitlines():
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

    def purple_blue(self):
        os.system("")
        faded = ""
        red = 114
        green = 137
        blue = 218
        for line in self.splitlines():
            faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
            if green != 0:
                green -= 5
                green = max(green, 0)
            if blue != 255:
                blue += 5
                blue = min(blue, 255)
        return faded

    def purple_cyan(self):
        os.system("")
        faded = ""
        red = 0
        green = 255
        blue = 255
        for line in self.splitlines():
            faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
            if red != 255:
                red += 22
                red = max(red, 0)
            if green != 0:
                green -= 40
                green = max(green, 0)
        return faded

    def pink_red(self):
        os.system("")
        faded = ""
        blue = 255
        for line in self.splitlines():
            faded += f"\033[38;2;255;0;{blue}m{line}\033[0m\n"
            if blue != 0:
                blue -= 20
                blue = max(blue, 0)
        return faded

    def black_white(self):
        os.system("")
        faded = ""
        red = 25
        green = 25
        blue = 25
        for line in self.splitlines():
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

    def blue_cyan(self):
        os.system("")
        faded = ""
        green = 10
        for line in self.splitlines():
            faded += f"\033[38;2;0;{green};255m{line}\033[0m\n"
            if green != 255:
                green += 15
                green = min(green, 255)
        return faded

    def green_blue(self):
        os.system("")
        faded = ""
        blue = 100
        for line in self.splitlines():
            faded += f"\033[38;2;0;255;{blue}m{line}\033[0m\n"
            if blue != 255:
                blue += 15
                blue = min(blue, 255)
        return faded

    def orange_red(self):
        os.system("")
        faded = ""
        green = 250
        for line in self.splitlines():
            faded += f"\033[38;2;255;{green};0m{line}\033[0m\n"
            if green != 0:
                green -= 25
                green = max(green, 0)
        return faded

    def splitlines(self):
        pass
