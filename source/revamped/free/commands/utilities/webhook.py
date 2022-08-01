import random

from .functions import *


class webhook:

    def title():
        """Get the title in the config file"""
        title = files.json(
            "data/webhooks/webhook.json",
            "title", documents=False
        )
        if title is None:
            title = ""
        return str(title)

    def footer():
        """Get the title in the config file"""
        footer = files.json(
            "data/webhooks/webhook.json",
            "footer", documents=False
        )
        if footer is None:
            footer = ""
        return str(footer)

    def image_url():
        """Get the image url in the config file"""
        image_url = files.json(
            "data/webhooks/webhook.json",
            "image_url", documents=False
        )
        if image_url is None:
            image_url = ""
        return str(image_url)

    def hex_color():
        """Get the hex color in the config file"""
        hexcolorvar = files.json(
            "data/webhooks/webhook.json", "hex_color", documents=False
        )
        if hexcolorvar is None:
            hexcolorvar = "#000000"
        if hexcolorvar == "random":
            hexcolorvar = random.randint(0, 0xffffff)
        elif len(hexcolorvar) < 7:
            hexcolorvar = int(hexcolorvar)
        else:
            hexcolorvar = int(hexcolorvar.replace('#', ''), 16)
        return hexcolorvar

    def login_url():
        """Get the login webhook url in the config file"""
        login_url = files.json(
            "data/webhooks/url.json",
            "login", documents=False
        )
        return str(login_url)

    def nitro_url():
        """Get the nitro webhook url in the config file"""
        nitro_url = files.json(
            "data/webhooks/url.json",
            "nitro", documents=False
        )
        return str(nitro_url)

    def giveaway_url():
        """Get the giveaway webhook url in the config file"""
        giveaway_url = files.json(
            "data/webhooks/url.json", "giveaway", documents=False
        )
        return str(giveaway_url)

    def privnote_url():
        """Get the privnote webhook url in the config file"""
        privnote_url = files.json(
            "data/webhooks/url.json", "privnote", documents=False
        )
        return str(privnote_url)

    def selfbot_url():
        """Get the selfbot webhook url in the config file"""
        selfbot_url = files.json(
            "data/webhooks/url.json", "selfbot", documents=False
        )
        return str(selfbot_url)

    def pings_url():
        """Get the pings' webhook url in the config file"""
        pings_url = files.json(
            "data/webhooks/url.json",
            "pings", documents=False
        )
        return str(pings_url)

    def ghostpings_url():
        """Get the ghostpings webhook url in the config file"""
        ghostpings_url = files.json(
            "data/webhooks/url.json", "ghostpings", documents=False
        )
        return str(ghostpings_url)

    def friendevents_url():
        """Get the friendevents webhook url in the config file"""
        friendevents_url = files.json(
            "data/webhooks/url.json", "friendevents", documents=False
        )
        return str(friendevents_url)

    def guildevents_url():
        """Get the guildevents webhook url in the config file"""
        guildevents_url = files.json(
            "data/webhooks/url.json", "guildevents", documents=False
        )
        return str(guildevents_url)

    def roleupdates_url():
        """Get the roleupdates webhook url in the config file"""
        roleupdates_url = files.json(
            "data/webhooks/url.json", "roleupdates", documents=False
        )
        return str(roleupdates_url)

    def nickupdates_url():
        """Get the nickupdates webhook url in the config file"""
        nickupdates_url = files.json(
            "data/webhooks/url.json", "nickupdates", documents=False
        )
        return str(nickupdates_url)

    def protections_url():
        """Get the protections' webhook url in the config file"""
        protections_url = files.json(
            "data/webhooks/url.json", "protections", documents=False
        )
        return str(protections_url)
