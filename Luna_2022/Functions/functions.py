import urllib
import os
import random
import string
import ctypes
import sys
from FileHandling.jsonhandler import *
from Functions.notifications import *

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