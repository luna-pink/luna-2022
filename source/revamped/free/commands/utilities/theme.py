from functions import *

from request import *


class theme:

    def title():
        """Get the title in the config file"""
        theme = files.json("data/config.json", "theme", documents=False)
        if theme == "default":
            title = title_request
        else:
            title = files.json(f"data/themes/{theme}", "title", documents=False)
            if title is None:
                title = ""
        return str(title)

    def footer():
        """Get the footer in the config file"""
        theme = files.json("data/config.json", "theme", documents=False)
        if theme == "default":
            footer = footer_request
        else:
            footer = files.json(
                f"data/themes/{theme}", "footer", documents=False
            )
            if footer is None:
                footer = ""
        return str(footer)

    def description():
        """Get the description in the config file"""
        theme = files.json("data/config.json", "theme", documents=False)
        if theme == "default":
            descriptionvar = descriptionvar_request
            descriptionvar = "```\n<> is required | [] is optional\n```" if descriptionvar == "true" else ""

        else:
            descriptionvar = files.json(
                f"data/themes/{theme}", "description", documents=False
            )
            if descriptionvar is None:
                descriptionvar = True
            descriptionvar = "```\n<> is required | [] is optional\n```" if descriptionvar else ""
        return descriptionvar
