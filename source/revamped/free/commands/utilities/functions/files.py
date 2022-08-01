# pyarmor options: no-spp-mode

import contextlib
import os
import json


# ///////////////////////////////////////////////////////////////
# File Functions
import time
from datetime import datetime

import requests


class files:
    def documents():
        """
        It returns the path to the Documents' folder in the user's home directory
        :return: The path to the Documents' folder in the user's home directory.
        """
        return os.path.expanduser("~/Documents")

    def file_exist(self, documents=False):
        """
        It checks if a file exists in the documents folder or not

        :param documents: If True, the file will be searched for in the documents' folder, defaults to False (optional)
        :return: The file_exist method is being returned.
        """
        if documents:
            return os.path.exists(os.path.join(files.documents(), self))
        else:
            return os.path.exists(self)

    def write_file(self, content, documents=False, byte=False, append=False):
        """
        It writes a file.

        :param content: The content to write to the file
        :param documents: If True, the file will be written to the documents' folder, defaults to False (optional)
        :param byte: If the file is a byte file, set this to True, defaults to False (optional)
        :param append: If you want to append to the file, set this to True, defaults to False (optional)
        """
        if documents and byte:
            with open(os.path.join(files.documents(), self), "wb") as f:
                f.write(content)
        elif documents:
            mode = "a" if append else "w"
            with open(os.path.join(files.documents(), self), mode) as f:
                f.write(content)
        elif byte:
            with open(self, 'wb') as f:
                f.write(content)
        else:
            with open(self, 'w') as f:
                f.write(content)

    def write_json(self, content, documents=False):
        """
        It writes a json file to the documents folder

        :param content: The content to write to the file
        :param documents: If True, the file will be saved in the documents' folder, defaults to False (optional)
        """
        if documents:
            with open(os.path.join(files.documents(), self), "w") as f:
                f.write(json.dumps(content, indent=4))
        else:
            with open(self, "w") as f:
                f.write(json.dumps(content, indent=4))

    def read_file(self, documents=False):
        """
        It opens a file, reads it, and returns the contents of the file

        :param documents: If True, the file will be read from the documents' folder, defaults to False (optional)
        :return: The read() method returns the specified number of bytes from the file.
        """
        if documents:
            with open(os.path.join(files.documents(), self), 'r', encoding="utf-8") as f:
                return f.read()
        else:
            with open(self, 'r', encoding="utf-8") as f:
                return f.read()

    def append_file(self, content):
        """
        Append the content to the file.

        :param content: The content to be written to the file
        """
        with open(self, 'a') as f:
            f.write(content)

    def delete_file(self, documents=False):
        """
        It deletes a file

        :param documents: If True, the file will be deleted from the documents' folder. If False, the file will be deleted from the current directory, defaults to False (optional)
        """
        if documents:
            os.remove(os.path.join(files.documents(), self))
        else:
            os.remove(self)

    def create_folder(self, documents=False):
        """
        If the folder doesn't exist, create it

        :param documents: If True, the folder will be created in the documents' folder, defaults to False (optional)
        """
        if documents:
            if not os.path.exists(os.path.join(files.documents(), self)):
                os.makedirs(os.path.join(files.documents(), self))
        elif not os.path.exists(self):
            os.makedirs(self)

    def json(self, value: str, documents=False):
        """
        It returns a value from a JSON file

        :param value: The value you want to get from the json file
        :type value: str
        :param documents: If you want to get a value from a json file in the documents' folder, set this to True, defaults to False (optional)
        :return: The value of the key in the json file.
        """
        if documents:
            return json.load(open(os.path.join(files.documents(), self), encoding="utf-8"))[value]

        else:
            return json.load(open(self, encoding="utf-8"))[value]

    def remove(self, documents=False):
        """
        It removes a file

        :param documents: If True, the file will be removed from the documents' folder, defaults to False (optional)
        """
        with contextlib.suppress(BaseException):
            if documents:
                if os.path.exists(os.path.join(files.documents(), self)):
                    os.remove(os.path.join(files.documents(), self))
            elif os.path.exists(self):
                os.remove(self)


def file_check():
    """Run a check for the files, create if needed."""
    # ///////////////////////////////////////////////////////////////
    # Folder Creation

    if not files.file_exist("data/console", documents=False):
        files.create_folder("data/console", documents=False)

    if not files.file_exist("data/themes", documents=False):
        files.create_folder("data/themes", documents=False)

    if not files.file_exist("data/snipers", documents=False):
        files.create_folder("data/snipers", documents=False)

    if not files.file_exist("data/scripts", documents=False):
        files.create_folder("data/scripts", documents=False)

    if not files.file_exist("data/webhooks", documents=False):
        files.create_folder("data/webhooks", documents=False)

    if not files.file_exist("data/notifications", documents=False):
        files.create_folder("data/notifications", documents=False)

    if not files.file_exist("data/backup", documents=False):
        files.create_folder("data/backup", documents=False)

    if not files.file_exist("data/backup/guilds", documents=False):
        files.create_folder("data/backup/guilds", documents=False)

    if not files.file_exist("data/resources", documents=False):
        files.create_folder("data/resources", documents=False)

    if not files.file_exist("data/raiding", documents=False):
        files.create_folder("data/raiding", documents=False)

    if not files.file_exist("data/raiding/proxies", documents=False):
        files.create_folder("data/raiding/proxies", documents=False)

    if not files.file_exist("data/notes", documents=False):
        files.create_folder("data/notes", documents=False)

    if not files.file_exist("data/emojis", documents=False):
        files.create_folder("data/emojis", documents=False)

    if not files.file_exist("data/privnote", documents=False):
        files.create_folder("data/privnote", documents=False)

    if not files.file_exist("data/protections", documents=False):
        files.create_folder("data/protections", documents=False)

    if not files.file_exist("data/dumping", documents=False):
        files.create_folder("data/dumping", documents=False)

    if not files.file_exist("data/dumping/images", documents=False):
        files.create_folder("data/dumping/images", documents=False)

    if not files.file_exist("data/dumping/emojis", documents=False):
        files.create_folder("data/dumping/emojis", documents=False)

    if not files.file_exist("data/dumping/urls", documents=False):
        files.create_folder("data/dumping/urls", documents=False)

    if not files.file_exist("data/dumping/audio", documents=False):
        files.create_folder("data/dumping/audio", documents=False)

    if not files.file_exist("data/dumping/videos", documents=False):
        files.create_folder("data/dumping/videos", documents=False)

    if not files.file_exist("data/dumping/messages", documents=False):
        files.create_folder("data/dumping/messages", documents=False)

    if not files.file_exist("data/dumping/channels", documents=False):
        files.create_folder("data/dumping/channels", documents=False)

    if not files.file_exist("data/dumping/avatars", documents=False):
        files.create_folder("data/dumping/avatars", documents=False)

    # ///////////////////////////////////////////////////////////////
    # Python Files

    if not files.file_exist("data/scripts/example.py", documents=False):
        content = """# Its as simple as writing commands for cogs! (Note: You need to use \"self\")
# Documentation for custom commands can be found here: https://docs.team-luna.org/

@commands.command(
    name="example",
    usage="<text>",
    description="Example of a custom command"
)
async def example(self, luna, *, text):
    await luna.send(f"```{text}```")
"""
        files.write_file("data/scripts/example.py", content, documents=False)

    # ///////////////////////////////////////////////////////////////
    # Protection Files

    if not files.file_exist(
            "data/protections/config.json",
            documents=False
    ):
        data = {
            "footer": True,
            "guilds": []
        }
        files.write_json(
            "data/protections/config.json",
            data, documents=False
        )

    if not files.file_exist(
            "data/protections/invite.json",
            documents=False
    ):
        data = {
            "delete": True,
            "action": "warn"
        }
        files.write_json(
            "data/protections/invite.json",
            data, documents=False
        )

    # ///////////////////////////////////////////////////////////////
    # Json Files

    if not files.file_exist("data/rpc.json", documents=False):
        data = {
            "rich_presence": "on",
            "client_id": "911815236825268234",
            "details": "Luna",
            "state": "",
            "large_image": "lunarpc",
            "large_text": "",
            "small_image": "",
            "small_text": "",
            "button_1_text": "Luna Public",
            "button_1_url": "https://discord.gg/Kxyv7NHVED",
            "button_2_text": "",
            "button_2_url": "",
        }
        files.write_json("data/rpc.json", data, documents=False)

    if not files.file_exist("data/config.json", documents=False):
        data = {
            "prefix": ".",
            "stream_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "afk_message": "I am not here right now, DM me later.",
            "delete_timer": "30",
            "mode": "1",
            "error_log": "message",
            "risk_mode": "off",
            "theme": "default",
            "startup_status": "online"
        }
        files.write_json("data/config.json", data, documents=False)

    if not files.file_exist("data/discord.luna", documents=False):
        data = {
            "token": "token-here",
            "password": "password-here"
        }
        files.write_json("data/discord.luna", data, documents=False)

    if not files.file_exist("data/console/console.json", documents=False):
        data = {
            "logo": "luna",
            "logo_gradient": "1",
            "center": True,
            "print_gradient": "1",
            "spacers": True,
            "spacer": "|",
            "timestamp": True,
            "mode": "1"
        }
        files.write_json("data/console/console.json", data, documents=False)

    if not files.file_exist("data/snipers/nitro.json", documents=False):
        data = {
            "sniper": "on",
            "charge": "off"
        }
        files.write_json("data/snipers/nitro.json", data, documents=False)

    if not files.file_exist("data/snipers/privnote.json", documents=False):
        data = {
            "sniper": "on"
        }
        files.write_json(
            "data/snipers/privnote.json",
            data, documents=False
        )

    if not files.file_exist("data/snipers/selfbot.json", documents=False):
        data = {
            "sniper": "on"
        }
        files.write_json("data/snipers/selfbot.json", data, documents=False)

    if not files.file_exist("data/snipers/giveaway.json", documents=False):
        data = {
            "joiner": "on",
            "delay_in_minutes": "1",
            "blocked_words": [
                "ban",
                "kick",
                "selfbot",
                "self bot",
                "test",
                "check"],
            "guild_joiner": "on"
        }
        files.write_json(
            "data/snipers/giveaway.json",
            data, documents=False
        )

    if not files.file_exist(
            "data/snipers/giveaway_bots.json",
            documents=False
    ):
        data = {
            "716967712844414996": "🎉",
            "294882584201003009": "🎉",
            "679379155590184966": "🎉",
            "649604306596528138": "🎉",
            "673918978178940951": "🎉",
            "720351927581278219": "🎉",
            "530082442967646230": "🎉",
            "486970979290054676": "🎉",
            "582537632991543307": "🎉",
            "396464677032427530": "🎉",
            "606026008109514762": "🎉",
            "797025321958244382": "🎉",
            "570338970261782559": "🎉",
            "806644708973346876": "🎉",
            "712783461609635920": "🎉",
            "897642275868393493": "🎉",
            "574812330760863744": "🎁",
            "732003715426287676": "🎁"
        }
        files.write_json(
            "data/snipers/giveaway_bots.json",
            data, documents=False
        )

    if not files.file_exist("data/resources/luna.ico", documents=False):
        r = requests.get(
            "https://cdn.discordapp.com/attachments/927033067468623882/981645188785111040/Luna_Logo.ico",
            stream=True
        )
        open(
            'data/resources/luna.ico',
            'wb'
        ).write(
            r.content
        )

    if not files.file_exist("data/resources/luna.png", documents=False):
        r = requests.get(
            "https://cdn.discordapp.com/attachments/927033067468623882/967102261060833310/Luna_Blurple.png",
            stream=True
        )
        open(
            'data/resources/luna.png',
            'wb'
        ).write(
            r.content
        )

    if not files.file_exist("data/backup/friends.txt", documents=False):
        content = "Use [prefix]friendsbackup"
        files.write_file(
            "data/backup/friends.txt",
            content, documents=False
        )

    if not files.file_exist("data/invites.txt", documents=False):
        content = "Put the invites of the servers you want to join here one after another"
        files.write_file("data/invites.txt", content, documents=False)

    if not files.file_exist("data/backup/blocked.txt", documents=False):
        content = "Use [prefix]friendsbackup"
        files.write_file(
            "data/backup/blocked.txt",
            content, documents=False
        )

    if not files.file_exist(
            "data/notifications/toasts.json",
            documents=False
    ):
        data = {
            "toasts": "on",
            "login": "on",
            "nitro": "on",
            "giveaway": "on",
            "privnote": "on",
            "selfbot": "on",
            "pings": "on",
            "ghostpings": "on",
            "friendevents": "on",
            "guildevents": "on",
            "roleupdates": "on",
            "nickupdates": "on",
            "protection": "on"
        }
        files.write_json(
            "data/notifications/toasts.json",
            data, documents=False
        )

    if not files.file_exist("data/sharing.json", documents=False):
        data = {
            "share": "off",
            "user_id": ""
        }
        files.write_json("data/sharing.json", data, documents=False)

    if not files.file_exist(
            "data/notifications/console.json",
            documents=False
    ):
        data = {
            "pings": "on"
        }
        files.write_json(
            "data/notifications/console.json",
            data, documents=False
        )

    if not files.file_exist(
            "data/notifications/toast.json",
            documents=False
    ):
        data = {
            "icon": "luna.ico",
            "title": "Luna"
        }
        files.write_json(
            "data/notifications/toast.json",
            data, documents=False
        )

    if not files.file_exist("data/raiding/tokens.txt", documents=False):
        content = "Put your tokens here line after line"
        files.write_file(
            "data/raiding/tokens.txt",
            content, documents=False
        )

    if not files.file_exist("data/raiding/proxies.txt", documents=False):
        content = "Put your proxies here line after line. (HTTP Only)"
        files.write_file(
            "data/raiding/proxies.txt",
            content, documents=False
        )

    if not files.file_exist("data/webhooks/webhook.json", documents=False):
        data = {
            "title": "Luna",
            "footer": "Luna",
            "image_url": "https://cdn.discordapp.com/attachments/927033067468623882/967102261060833310/Luna_Blurple.png",
            "hex_color": "#898eff"
        }
        files.write_json(
            "data/webhooks/webhook.json",
            data, documents=False
        )

    if not files.file_exist("data/webhooks/url.json", documents=False):
        data = {
            "login": "webhook-url-here",
            "nitro": "webhook-url-here",
            "giveaway": "webhook-url-here",
            "privnote": "webhook-url-here",
            "selfbot": "webhook-url-here",
            "pings": "webhook-url-here",
            "ghostpings": "webhook-url-here",
            "friendevents": "webhook-url-here",
            "guildevents": "webhook-url-here",
            "roleupdates": "webhook-url-here",
            "nickupdates": "webhook-url-here",
            "protection": "webhook-url-here"
        }
        files.write_json("data/webhooks/url.json", data, documents=False)

    if not files.file_exist("data/webhooks/webhooks.json", documents=False):
        data = {
            "webhooks": "on",
            "login": "on",
            "nitro": "on",
            "giveaway": "on",
            "privnote": "on",
            "selfbot": "on",
            "pings": "on",
            "ghostpings": "on",
            "friendevents": "on",
            "guildevents": "on",
            "roleupdates": "on",
            "nickupdates": "on",
            "protection": "on"
        }
        files.write_json(
            "data/webhooks/webhooks.json",
            data, documents=False
        )
