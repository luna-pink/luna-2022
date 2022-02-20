import requests
import random

from FileHandling.jsonhandler import *

# /////////////////////////////////////////////////////////////////////////////
# Default Theme

title_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["title"]
title_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["title_url"]
footer_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["footer"]
footer_icon_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["footer_icon_url"]
image_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["image_url"]
large_image_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["large_image_url"]
hexcolorvar_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["hex_color"]
author_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["author"]
author_icon_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["author_icon_url"]
author_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["author_url"]
descriptionvar_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["description"]

# /////////////////////////////////////////////////////////////////////////////

class theme:
    """
    This class handles the themes.
    """
    def __init__(self, file_name: str, file_path: str = "./"):
        """
        Initialize the JsonHandler class.
        Does a check if the file exists, if not creates it, before writing to it.
        (Default: "./", if "Luna" in the file_path, the path is changed to "Documents/Luna/")
        
        Initialize:
            >>> JsonHandler("foo.json", "data/foo")
            
        Example:
            >>> JsonHandler("foo.json", "data/foo").read_value("foo")

        Args:
            file_name: The name of the file.
            file_path: The path of the file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if file_path.title().startswith("Luna"):
            file_path = os.path.expanduser(f"~/Documents/{file_path}")
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        self.file_path = file_path
        if not file_name.endswith(".json"):
            file_name += ".json"
        self.file_name = file_name
        self.file_path_name = os.path.join(self.file_path, self.file_name)
        if not os.path.exists(self.file_path_name):
            with open(self.file_path_name, "w+", encoding="utf-8") as file:
                file.write("{}")

    def title():
        """Get the title in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            title = title_request
        else:
            title = files.json(f"Luna/themes/{theme}", "title", documents=True)
            if title == None:
                title = ""
        return str(title)

    def title_url():
        """Get the title url in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            title_url = title_url_request
        else:
            title_url = files.json(
                f"Luna/themes/{theme}", "title_url", documents=True)
            if title_url == None:
                title_url = ""
        return str(title_url)

    def footer():
        """Get the footer in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            footer = footer_request
        else:
            footer = files.json(
                f"Luna/themes/{theme}", "footer", documents=True)
            if footer == None:
                footer = ""
        return str(footer)

    def footer_icon_url():
        """Get the footer icon url in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            footer_icon_url = footer_icon_url_request
            if footer_icon_url == "$avatar":
                footer_icon_url = bot.user.avatar_url
        else:
            footer_icon_url = files.json(f"Luna/themes/{theme}", "footer_icon_url", documents=True)
            if footer_icon_url == None:
                footer_icon_url = ""
            elif footer_icon_url == "$avatar":
                footer_icon_url = bot.user.avatar_url
        return str(footer_icon_url)

    def image_url():
        """Get the image url in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            image_url = image_url_request
            if image_url == "$avatar":
                image_url = bot.user.avatar_url
        else:
            image_url = files.json(f"Luna/themes/{theme}", "image_url", documents=True)
            if image_url == None:
                image_url = ""
            elif image_url == "$avatar":
                image_url = bot.user.avatar_url
        return str(image_url)

    def large_image_url():
        """Get the large image url in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            large_image_url = large_image_url_request
            if large_image_url == "$avatar":
                large_image_url = bot.user.avatar_url
        else:
            large_image_url = files.json(
                f"Luna/themes/{theme}", "large_image_url", documents=True)
            if large_image_url == None:
                large_image_url = ""
            elif large_image_url == "$avatar":
                large_image_url = bot.user.avatar_url
        return str(large_image_url)

    def hex_color():
        """Get the hex color in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            hexcolorvar = hexcolorvar_request
            if hexcolorvar == "":
                hexcolorvar = "#000000"
            elif hexcolorvar == "random":
                hexcolorvar = random.randint(0, 0xffffff)
            elif len(hexcolorvar) > 7:
                hexcolorvar = int(hexcolorvar)
            else:
                hexcolorvar = int(hexcolorvar.replace('#', ''), 16)
        else:
            hexcolorvar = files.json(
                f"Luna/themes/{theme}", "hex_color", documents=True)
            if hexcolorvar == None:
                hexcolorvar = "#000000"
            if hexcolorvar == "random":
                hexcolorvar = random.randint(0, 0xffffff)
            elif len(hexcolorvar) > 7:
                hexcolorvar = int(hexcolorvar)
            else:
                hexcolorvar = int(hexcolorvar.replace('#', ''), 16)
        return hexcolorvar

    def author():
        """Get the author in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            author = author_request
        else:
            author = files.json(f"Luna/themes/{theme}", "author", documents=True)
            if author == None:
                author = ""
        return str(author)

    def author_icon_url():
        """Get the author icon url in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            author_icon_url = author_icon_url_request
            if author_icon_url == "$avatar":
                author_icon_url = bot.user.avatar_url
        else:
            author_icon_url = files.json(f"Luna/themes/{theme}", "author_icon_url", documents=True)
            if author_icon_url == None:
                author_icon_url = ""
            elif author_icon_url == "$avatar":
                author_icon_url = bot.user.avatar_url
        return str(author_icon_url)

    def author_url():
        """Get the author url in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            author_url = author_url_request
        else:
            author_url = files.json(f"Luna/themes/{theme}", "author_url", documents=True)
            if author_url == None:
                author_url = ""
        return str(author_url)

    def description():
        """Get the description in the config file"""
        theme = files.json("Luna/config.json", "theme", documents=True)
        if theme == "default":
            descriptionvar = descriptionvar_request
            if not descriptionvar == "true":
                descriptionvar = ""
            else:
                # descriptionvar = "```ansi\n[35m<>[0m is required | [34m[][0m is optional\n```"
                descriptionvar = "```\n<> is required | [] is optional\n```"
        else:
            descriptionvar = files.json(f"Luna/themes/{theme}", "description", documents=True)
            if descriptionvar == None:
                descriptionvar = True
            if not descriptionvar:
                descriptionvar = ""
            else:
                descriptionvar = "```\n<> is required | [] is optional\n```"
            # descriptionvar = "```ansi\n[35m<>[0m is required | [34m[][0m is optional\n```"
        return str(descriptionvar)