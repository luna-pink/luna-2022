import urllib
import os
import random
import string
import ctypes

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