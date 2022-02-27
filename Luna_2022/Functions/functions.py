import urllib
import os
import random
import string
import ctypes
import sys
from FileHandling.filehandler import *
from FileHandling.jsonhandler import *
from Functions.notifications import *
from Luna.luna import *
from CEA256 import *
from datetime import datetime
import time
from Luna.luna import *

def motd():
    """Returns the message of the day."""
    return urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ').read().decode('utf-8')

def clear():
    """
    Clears the screen.
    """
    os.system('cls')
    
def Randprntsc():
    """
    Random print screen.
    """
    letterprn = ''.join(random.choices(string.ascii_lowercase, k=4))
    numberprn = random.randint(10, 99)
    return f'https://prnt.sc/{numberprn}{letterprn}'

def title(text):
    """Set the title of the console window."""
    ctypes.windll.kernel32.SetConsoleTitleW(text)
    
def restart_program():
    """
    Restarts the program.
    """
    if JsonHandler("toasts.json", "data/notifications").read_value("login") == "on" and JsonHandler("toasts.json", "data/notifications").read_value("toasts") == "on":
        notify.toast(message=f"Restarting Luna...")
    if JsonHandler("webhooks.json", "data/webhooks").read_value("login") == "on" and JsonHandler("webhooks.json", "data/webhooks").read_value("webhooks") == "on" and not webhook.login_url() == "webhook-url-here":
        notify.webhook(url=webhook.login_url(), name="login", description=f"Restarting Luna...")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def update_thread():
    update_found = False
    while True:
        r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
        version_url = r["version"]

        r = requests.get(
            "https://raw.githubusercontent.com/Nshout/Luna/main/beta.json").json()
        beta_version_url = r["version"]

        if beta:
            version_url = beta_version_url
        if developer_mode:
            pass
        elif version == version_url:
            pass
        else:
            if JsonHandler("toasts.json", "data/notifications").read_value("login") == "on" and JsonHandler("toasts.json", "data/notifications").read_value("toasts") == "on":
                notify.toast(message=f"Starting update {version_url}")
            if JsonHandler("webhooks.json", "data/webhooks").read_value("login") == "on" and JsonHandler("webhooks.json", "data/webhooks").read_value("webhooks") == "on" and not webhook.login_url() == "webhook-url-here":
                notify.webhook(url=webhook.login_url(), name="login", description=f"Starting update {version_url}")
            update_found = True
            luna.update()
        if not update_found:
            time.sleep(300)
    
def file_check(console=False):
    """Run a check for the files, create if needed."""

    if console:
        luna.console(clear=True)
        now = datetime.now()
        hour = now.hour

        if hour < 12:
            greeting = "Good morning"
        elif hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"

        username = files.json("Luna/auth.json", "username", documents=True)
        username = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
        prints.message(f"{greeting}, {color.purple(username)}.")
        time.sleep(3)
        prints.message("We are getting Luna ready for you.")

    # ///////////////////////////////////////////////////////////////
    # Folder Creation

    if not files.file_exist("Luna/console", documents=True):
        files.create_folder("Luna/console", documents=True)

    if not files.file_exist("Luna/themes", documents=True):
        files.create_folder("Luna/themes", documents=True)

    if not files.file_exist("Luna/snipers", documents=True):
        files.create_folder("Luna/snipers", documents=True)

    if not files.file_exist("Luna/custom", documents=True):
        files.create_folder("Luna/custom", documents=True)

    if not files.file_exist("Luna/webhooks", documents=True):
        files.create_folder("Luna/webhooks", documents=True)

    if not files.file_exist("Luna/notifications", documents=True):
        files.create_folder("Luna/notifications", documents=True)

    if not files.file_exist("Luna/backup", documents=True):
        files.create_folder("Luna/backup", documents=True)

    if not files.file_exist("Luna/backup/guilds", documents=True):
        files.create_folder("Luna/backup/guilds", documents=True)

    if not files.file_exist("Luna/resources", documents=True):
        files.create_folder("Luna/resources", documents=True)

    if not files.file_exist("Luna/raiding", documents=True):
        files.create_folder("Luna/raiding", documents=True)

    if not files.file_exist("Luna/raiding/proxies", documents=True):
        files.create_folder("Luna/raiding/proxies", documents=True)

    if not files.file_exist("Luna/notes", documents=True):
        files.create_folder("Luna/notes", documents=True)

    if not files.file_exist("Luna/emojis", documents=True):
        files.create_folder("Luna/emojis", documents=True)

    if not files.file_exist("Luna/privnote", documents=True):
        files.create_folder("Luna/privnote", documents=True)

    if not files.file_exist("Luna/protections", documents=True):
        files.create_folder("Luna/protections", documents=True)

    if not files.file_exist("Luna/dumping", documents=True):
        files.create_folder("Luna/dumping", documents=True)

    if not files.file_exist("Luna/dumping/images", documents=True):
        files.create_folder("Luna/dumping/images", documents=True)

    if not files.file_exist("Luna/dumping/emojis", documents=True):
        files.create_folder("Luna/dumping/emojis", documents=True)

    if not files.file_exist("Luna/dumping/urls", documents=True):
        files.create_folder("Luna/dumping/urls", documents=True)

    if not files.file_exist("Luna/dumping/audio", documents=True):
        files.create_folder("Luna/dumping/audio", documents=True)

    if not files.file_exist("Luna/dumping/videos", documents=True):
        files.create_folder("Luna/dumping/videos", documents=True)

    if not files.file_exist("Luna/dumping/messages", documents=True):
        files.create_folder("Luna/dumping/messages", documents=True)

    if not files.file_exist("Luna/dumping/channels", documents=True):
        files.create_folder("Luna/dumping/channels", documents=True)

    if not files.file_exist("Luna/dumping/avatars", documents=True):
        files.create_folder("Luna/dumping/avatars", documents=True)

        # ///////////////////////////////////////////////////////////////
        # Python Files

    if not files.file_exist("Luna/custom/custom.py", documents=True):
        content = """
# Its as simple as writing commands for cogs! (Note: You need to use"self\")
        
@commands.command(name = "example",
            usage="<text>",
            description = "Example of a custom command")
async def example(self, luna, *, text):
    await luna.message.delete()
    await luna.send(f"```{text}```")
        """
        files.write_file("Luna/custom/custom.py", content, documents=True)

    # ///////////////////////////////////////////////////////////////
    # Protection Files

    if not files.file_exist("Luna/protections/config.json", documents=True):
        data = {
            "footer": True,
            "guilds": []
        }
        files.write_json("Luna/protections/config.json",
                            data, documents=True)

    if not files.file_exist("Luna/protections/invite.json", documents=True):
        data = {
            "delete": True,
            "action": "warn"
        }
        files.write_json("Luna/protections/invite.json",
                            data, documents=True)

    # ///////////////////////////////////////////////////////////////
    # Json Files

    if not files.file_exist("Luna/rpc.json", documents=True):
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
        files.write_json("Luna/rpc.json", data, documents=True)

    if not files.file_exist("Luna/config.json", documents=True):
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
        files.write_json("Luna/config.json", data, documents=True)

    if not files.file_exist("Luna/discord.json", documents=True):
        data = {
            "token": "token-here",
            "password": "password-here"
        }
        files.write_json("Luna/discord.json", data, documents=True)

    if not files.file_exist("Luna/console/console.json", documents=True):
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
        files.write_json("Luna/console/console.json", data, documents=True)

    if not files.file_exist("Luna/snipers/nitro.json", documents=True):
        data = {
            "sniper": "on"
        }
        files.write_json("Luna/snipers/nitro.json", data, documents=True)

    if not files.file_exist("Luna/snipers/privnote.json", documents=True):
        data = {
            "sniper": "on"
        }
        files.write_json("Luna/snipers/privnote.json",
                            data, documents=True)

    if not files.file_exist("Luna/snipers/selfbot.json", documents=True):
        data = {
            "sniper": "on"
        }
        files.write_json("Luna/snipers/selfbot.json", data, documents=True)

    if not files.file_exist("Luna/snipers/giveaway.json", documents=True):
        data = {
            "joiner": "on",
            "delay_in_minutes": "1",
            "blocked_words": ["ban", "kick", "selfbot", "self bot", "test", "check"],
            "guild_joiner": "on"
        }
        files.write_json("Luna/snipers/giveaway.json",
                            data, documents=True)

    if not files.file_exist("Luna/snipers/giveaway_bots.json", documents=True):
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
        files.write_json("Luna/snipers/giveaway_bots.json",
                            data, documents=True)

    if not files.file_exist("Luna/resources/luna.ico", documents=True):
        r = requests.get(
            "https://cdn.discordapp.com/attachments/878593887113986048/926101890608025650/Luna_Logo.ico",
            stream=True)
        open(os.path.join(files.documents(),
                'Luna/resources/luna.ico'), 'wb').write(r.content)

    if not files.file_exist("Luna/resources/luna.png", documents=True):
        r = requests.get("https://cdn.discordapp.com/attachments/878593887113986048/925797624374759434/Luna_Logo.png", stream=True)
        open(os.path.join(files.documents(), 'Luna/resources/luna.png'), 'wb').write(r.content)

    if not files.file_exist("Luna/backup/friends.txt", documents=True):
        content = "Use [prefix]friendsbackup"
        files.write_file("Luna/backup/friends.txt", content, documents=True)

    if not files.file_exist("Luna/invites.txt", documents=True):
        content = "Put the invites of the servers you want to join here one after another"
        files.write_file("Luna/invites.txt", content, documents=True)

    if not files.file_exist("Luna/backup/blocked.txt", documents=True):
        content = "Use [prefix]friendsbackup"
        files.write_file("Luna/backup/blocked.txt", content, documents=True)

    if not files.file_exist("Luna/notifications/toasts.json", documents=True):
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
        files.write_json("Luna/notifications/toasts.json", data, documents=True)

    if not files.file_exist("Luna/sharing.json", documents=True):
        data = {
            "share": "off",
            "user_id": ""
        }
        files.write_json("Luna/sharing.json", data, documents=True)

    if not files.file_exist("Luna/notifications/console.json", documents=True):
        data = {
            "pings": "on"
        }
        files.write_json("Luna/notifications/console.json", data, documents=True)

    if not files.file_exist("Luna/notifications/toast.json", documents=True):
        data = {
            "icon": "luna.ico",
            "title": "Luna"
        }
        files.write_json("Luna/notifications/toast.json", data, documents=True)

    if not files.file_exist("Luna/raiding/tokens.txt", documents=True):
        content = "Put your tokens here line after line"
        files.write_file("Luna/raiding/tokens.txt", content, documents=True)

    if not files.file_exist("Luna/raiding/proxies.txt", documents=True):
        content = "Put your proxies here line after line. (HTTP Only)"
        files.write_file("Luna/raiding/proxies.txt", content, documents=True)

    if not files.file_exist("Luna/webhooks/webhook.json", documents=True):
        data = {
            "title": "Luna",
            "footer": "Luna",
            "image_url": "https://cdn.discordapp.com/attachments/878593887113986048/925797624374759434/Luna_Logo.png",
            "hex_color": "#898eff"
        }
        files.write_json("Luna/webhooks/webhook.json", data, documents=True)

    if not files.file_exist("Luna/webhooks/url.json", documents=True):
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
        files.write_json("Luna/webhooks/url.json", data, documents=True)

    if not files.file_exist("Luna/webhooks/webhooks.json", documents=True):
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
        files.write_json("Luna/webhooks/webhooks.json", data, documents=True)

    if console:
        time.sleep(5)