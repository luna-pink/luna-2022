import urllib

def motd():
    return urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ').read().decode('utf-8')