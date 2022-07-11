from .functions import *


class config:
    # ///////////////////////////////////////////////////////////////
    # File overwrite (Global)

    def _global(self, value_holder: str, new_value, add=False, delete=False):
        """Overwrites a value in a config file. (Global configs)"""
        json_object = json.load(open(self, encoding="utf-8"))

        if add:
            json_object[value_holder].append(new_value)
        elif delete:
            json_object[value_holder].remove(new_value)
        else:
            json_object[value_holder] = new_value
        files.write_json(self, json_object)

    # ///////////////////////////////////////////////////////////////
    # File overwrite (Config)

    def prefix(self):
        """Overwrites the prefix in the config file."""
        json_object = json.load(open("data/config.json", encoding="utf-8"))
        json_object["prefix"] = self
        files.write_json("data/config.json", json_object)

    def stream_url(self):
        """Overwrites the stream url in the config file."""
        json_object = json.load(open("data/config.json", encoding="utf-8"))

        json_object["stream_url"] = self
        files.write_json("data/config.json", json_object)

    def afk_message(self):
        """Overwrites the afk message in the config file."""
        json_object = json.load(open("data/config.json", encoding="utf-8"))

        json_object["afk_message"] = self
        files.write_json("data/config.json", json_object)

    def delete_timer(self):
        """Overwrites to delete timer in the config file."""
        json_object = json.load(open("data/config.json", encoding="utf-8"))

        json_object["delete_timer"] = self
        files.write_json("data/config.json", json_object)

    def mode(self):
        """Overwrites the mode in the config file."""
        json_object = json.load(open("data/config.json", encoding="utf-8"))

        json_object["mode"] = self
        files.write_json("data/config.json", json_object)

    def error_log(self):
        """Overwrites the error log in the config file."""
        json_object = json.load(open("data/config.json", encoding="utf-8"))

        json_object["error_log"] = self
        files.write_json("data/config.json", json_object)

    def risk_mode(self):
        """Overwrites the risk mode in the config file."""
        json_object = json.load(open("data/config.json", encoding="utf-8"))

        json_object["risk_mode"] = self
        files.write_json("data/config.json", json_object)

    def theme(self):
        """Overwrites the theme in the config file."""
        json_object = json.load(open("data/config.json", encoding="utf-8"))

        if self == "default":
            json_object["theme"] = self
        else:
            if ".json" in self:
                self = self.replace('.json', '')
            json_object["theme"] = f'{self}.json'
        files.write_json("data/config.json", json_object)

    def startup_status(self):
        """Overwrites the startup status in the config file."""
        json_object = json.load(open("data/config.json", encoding="utf-8"))

        json_object["startup_status"] = self
        files.write_json("data/config.json", json_object)

    def password(self):
        """Overwrites the password in the config file."""
        json_object = json.load(open("data/discord.luna"), encoding="utf-8")

        password = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(self)

        json_object["password"] = password
        files.write_json("data/discord.luna", json_object)

    # ///////////////////////////////////////////////////////////////
    # File overwrite (Snipers)

    class nitro:

        def sniper(self):
            """Overwrite the nitro sniper config"""
            json_object = json.load(open("data/snipers/nitro.json", encoding="utf-8"))

            json_object["sniper"] = self
            files.write_json("data/snipers/nitro.json", json_object)

    class privnote:

        def sniper(self):
            """Overwrite the privnote sniper config"""
            json_object = json.load(open("data/snipers/privnote.json", encoding="utf-8"))

            json_object["sniper"] = self
            files.write_json("data/snipers/privnote.json", json_object)

    class selfbot:

        def sniper(self):
            """Overwrite the selfbot sniper config"""
            json_object = json.load(open("data/snipers/selfbot.json", encoding="utf-8"))

            json_object["sniper"] = self
            files.write_json("data/snipers/selfbot.json", json_object)

    class giveaway:

        def joiner(self):
            """Overwrite the giveaway joiner config"""
            json_object = json.load(open("data/snipers/giveaway.json", encoding="utf-8"))

            json_object["joiner"] = self
            files.write_json("data/snipers/giveaway.json", json_object)

        def delay_in_minutes(self):
            """Overwrite the giveaway delay in minutes config"""
            json_object = json.load(open("data/snipers/giveaway.json", encoding="utf-8"))

            json_object["delay_in_minutes"] = self
            files.write_json("data/snipers/giveaway.json", json_object)

        def blocked_words(self):
            """Overwrite the giveaway blocked words config"""
            json_object = json.load(open("data/snipers/giveaway.json", encoding="utf-8"))

            json_object["blocked_words"] = self
            files.write_json("data/snipers/giveaway.json", json_object)

        def guild_joiner(self):
            """Overwrite the giveaway guild joiner config"""
            json_object = json.load(open("data/snipers/giveaway.json", encoding="utf-8"))

            json_object["guild_joiner"] = self
            files.write_json("data/snipers/giveaway.json", json_object)

    # ///////////////////////////////////////////////////////////////
    # File overwrite (Sharing)

    def share(self):
        """Overwrite the share config"""
        json_object = json.load(open("data/sharing.json", encoding="utf-8"))

        json_object["share"] = self
        files.write_json("data/sharing.json", json_object)

    def user_id(self):
        """Overwrite the user id config"""
        json_object = json.load(open("data/sharing.json", encoding="utf-8"))

        json_object["user_id"] = self
        files.write_json("data/sharing.json", json_object)

    # ///////////////////////////////////////////////////////////////
    # File overwrite (Themes)

    def title(self):
        """Overwrite the title config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["title"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    def title_url(self):
        """Overwrite the title url config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["title_url"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    def footer(self):
        """Overwrite the footer config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["footer"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    def footer_icon_url(self):
        """Overwrite the footer icon url config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["footer_icon_url"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    def image_url(self):
        """Overwrite the image url config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["image_url"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    def large_image_url(self):
        """Overwrite the large image url config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["large_image_url"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    def hex_color(self):
        """Overwrite the hex color config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["hex_color"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    def author(self):
        """Overwrite the author config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["author"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    def author_icon_url(self):
        """Overwrite the author icon url config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["author_icon_url"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    def author_url(self):
        """Overwrite the author url config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["author_url"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    def description(self):
        """Overwrite the description config"""
        theme = files.json("data/config.json", "theme", documents=False)
        json_object = json.load(
            open(
                f"data/themes/{theme}",
                encoding="utf-8"
            )
        )
        json_object["description"] = self
        files.write_json(
            f"data/themes/{theme}", json_object
        )

    # ///////////////////////////////////////////////////////////////
    # File overwrite (Toasts)

    class toast:
        # ///////////////////////////////////////////////////////////////
        # toast.json

        def icon(self):
            """Overwrite the icon config"""
            json_object = json.load(open("data/notifications/toast.json", encoding="utf-8"))
            json_object["icon"] = self
            files.write_json(
                "data/notifications/toast.json", json_object
            )

        def title(self):
            """Overwrite the title config"""
            json_object = json.load(
                open(

                    "data/notifications/toast.json", encoding="utf-8"
                )
            )
            json_object["title"] = self
            files.write_json(
                "data/notifications/toast.json", json_object
            )

        # ///////////////////////////////////////////////////////////////
        # toasts.json

        def toasts(self):
            """Overwrite the toasts config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["toasts"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def login(self):
            """Overwrite the login config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["login"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def nitro(self):
            """Overwrite the nitro config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["nitro"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def giveaway(self):
            """Overwrite the giveaway config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["nitro"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def privnote(self):
            """Overwrite the privnote config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["privnote"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def selfbot(self):
            """Overwrite the selfbot config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["selfbot"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def pings(self):
            """Overwrite the pings config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["pings"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def ghostpings(self):
            """Overwrite the ghostpings config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["ghostpings"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def friendevents(self):
            """Overwrite the friendevents config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["friendevents"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def guildevents(self):
            """Overwrite the guildevents config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["guildevents"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def roleupdates(self):
            """Overwrite the roleupdates config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["roleupdates"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def nickupdates(self):
            """Overwrite the nickupdates config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["nickupdates"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

        def protection(self):
            """Overwrite the protection config"""
            json_object = json.load(
                open(
                    "data/notifications/toasts.json", encoding="utf-8"
                )
            )
            json_object["protection"] = self
            files.write_json(
                "data/notifications/toasts.json", json_object
            )

    # ///////////////////////////////////////////////////////////////
    # File overwrite (Webhooks)

    class webhook:
        # ///////////////////////////////////////////////////////////////
        # webhook.json

        def title(self):
            """Overwrite the webhook title"""
            json_object = json.load(
                open(

                    "data/webhooks/webhook.json", encoding="utf-8"
                )
            )
            json_object["title"] = self
            files.write_json(
                "data/webhooks/webhook.json", json_object
            )

        def footer(self):
            """Overwrite the webhook footer"""
            json_object = json.load(
                open(

                    "data/webhooks/webhook.json", encoding="utf-8"
                )
            )
            json_object["footer"] = self
            files.write_json(
                "data/webhooks/webhook.json", json_object
            )

        def image_url(self):
            """Overwrite the image url config"""
            json_object = json.load(open("data/webhooks/webhook.json", encoding="utf-8"))

            json_object["image_url"] = self
            files.write_json("data/webhooks/webhook.json", json_object)

        def hex_color(self):
            """Overwrite the webhook hex color"""
            json_object = json.load(
                open(

                    "data/webhooks/webhook.json", encoding="utf-8"
                )
            )
            json_object["hex_color"] = self
            files.write_json(
                "data/webhooks/webhook.json", json_object
            )

        # ///////////////////////////////////////////////////////////////
        # webhooks.json

        def webhooks(self):
            """Overwrite the webhooks webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["webhooks"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def login(self):
            """Overwrite the login webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["login"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def nitro(self):
            """Overwrite the nitro webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["nitro"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def giveaway(self):
            """Overwrite the giveaway webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["nitro"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def privnote(self):
            """Overwrite the private note webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["privnote"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def selfbot(self):
            """Overwrite the selfbot webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["selfbot"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def pings(self):
            """Overwrite the pings webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["pings"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def ghostpings(self):
            """Overwrite the ghost pings webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["ghostpings"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def friendevents(self):
            """Overwrite the friend events webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["friendevents"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def guildevents(self):
            """Overwrite the guild events webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["guildevents"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def roleupdates(self):
            """Overwrite the role updates webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["roleupdates"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def nickupdates(self):
            """Overwrite the nick updates webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["nickupdates"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        def protection(self):
            """Overwrite the protection webhook"""
            json_object = json.load(
                open(

                    "data/webhooks/webhooks.json", encoding="utf-8"
                )
            )
            json_object["protection"] = self
            files.write_json(
                "data/webhooks/webhooks.json", json_object
            )

        # ///////////////////////////////////////////////////////////////
        # url.json

        def login_url(self):
            """Overwrite the login url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["login"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def nitro_url(self):
            """Overwrite the nitro url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["nitro"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def giveaway_url(self):
            """Overwrite the giveaway url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["giveaway"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def privnote_url(self):
            """Overwrite the private note url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["privnote"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def selfbot_url(self):
            """Overwrite the selfbot url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["selfbot"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def pings_url(self):
            """Overwrite the pings url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["pings"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def ghostpings_url(self):
            """Overwrite the ghost pings url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["ghostpings"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def friendevents_url(self):
            """Overwrite the friend events url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["friendevents"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def guildevents_url(self):
            """Overwrite the guild events url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["guildevents"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def roleupdates_url(self):
            """Overwrite the role updates url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["roleupdates"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def nickupdates_url(self):
            """Overwrite the nick updates url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["nickupdates"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )

        def protection_url(self):
            """Overwrite the protection url"""
            json_object = json.load(
                open(

                    "data/webhooks/url.json", encoding="utf-8"
                )
            )
            json_object["protection"] = self
            files.write_json(
                "data/webhooks/url.json", json_object
            )
