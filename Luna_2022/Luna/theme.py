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
    Initialize the Theme class.
    
    Initialize:
        >>> theme
        
    Example:
        >>> theme.title()
    """

    def title():
        """Get the title in the config file"""
        theme = JsonHandler("config.json").read_value("theme")
        if theme == "default":
            title = title_request
        else:
            title = JsonHandler(theme, "data/themes").read_value("title")
            if title == None:
                title = ""
        return str(title)

    def footer():
        """Get the footer in the config file"""
        theme = JsonHandler("config.json").read_value("theme")
        if theme == "default":
            footer = footer_request
        else:
            footer = JsonHandler(theme, "data/themes").read_value("footer")
            if footer == None:
                footer = ""
        return str(footer)

    def description():
        """Get the description in the config file"""
        theme = JsonHandler("config.json").read_value("theme")
        if theme == "default":
            descriptionvar = descriptionvar_request
            if not descriptionvar == "true":
                descriptionvar = ""
            else:
                descriptionvar = "```\n<> is required | [] is optional\n```"
        else:
            descriptionvar = JsonHandler(theme, "data/themes").read_value("description")
            if descriptionvar == None:
                descriptionvar = True
            if not descriptionvar:
                descriptionvar = ""
            else:
                descriptionvar = "```\n<> is required | [] is optional\n```"
        return str(descriptionvar)