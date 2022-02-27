import time
from Luna.luna import *
from Functions.prints import *
import re

# ///////////////////////////////////////////////////////////////
# Token Grabber

def prompt_token():
    """Prompts user for token."""
    token = prints.input("Enter your token")
    if luna.check_token(token):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Content-Type': 'application/json',
            'authorization': token}
        r = requests.get(
            "https://discordapp.com/api/v9/users/@me",
            headers=headers).json()
        if token.startswith("mfa"):
            _2fa = " » 2FA Active"
        else:
            _2fa = ""
        prints.message(
            f"Detected a valid token » {color.purple(r['username'])}#{color.purple(r['discriminator'])}{_2fa}")
        prompt = prints.input("Do you want to use it? (y/n)")
        if prompt.lower() == "y" or prompt.lower() == "yes":
            json_object = json.load(
                open(
                    os.path.join(
                        files.documents(),
                        "Luna/discord.json"),
                    encoding="utf-8"))
            json_object["token"] = Encryption(
                '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token)
            files.write_json(os.path.join(
                files.documents(), "Luna/discord.json"), json_object)
            return True
        else:
            luna.prompt_token()
    else:
        return False

def check_token(token):
    """
            Check the given token.\n
            Returns `True` if the token is valid.
            """
    global valid_tokens
    valid_tokens = []
    if isinstance(token, list):
        for i in token:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Content-Type': 'application/json',
                'authorization': i}
            r = requests.get(
                "https://discordapp.com/api/v9/users/@me/library",
                headers=headers)
            if r.status_code == 200:
                valid_tokens.append(i)
        return valid_tokens[0]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'authorization': token}
    r = requests.get(
        "https://discordapp.com/api/v9/users/@me/library", headers=headers)
    if r.status_code == 200:
        return token
    else:
        return False

def find_token():
    """
            Search for tokens on the system.\n
            Checks the token if any are found and prompts the user.
            """
    try:
        tokens = []
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')
        paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\DiscordCanary',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default'}
        for platform, path in paths.items():
            if not os.path.exists(path):
                continue
            path += '\\Local Storage\\leveldb\\'
            for file_name in os.listdir(path):
                if not file_name.endswith(
                        '.log') and not file_name.endswith('.ldb'):
                    continue
                for line in [
                    x.strip() for x in open(
                        f'{path}\\{file_name}',
                        errors='ignore').readlines() if x.strip()]:
                    for regex in (
                        r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',
                            r'mfa\.[\w-]{84}'):
                        for token in re.findall(regex, line):
                            if token not in tokens:
                                tokens.append(token)
        if not tokens == []:
            if luna.check_token(tokens):
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                    'Content-Type': 'application/json',
                    'authorization': valid_tokens[0]}
                r = requests.get(
                    "https://discordapp.com/api/v9/users/@me",
                    headers=headers).json()
                if token.startswith("mfa"):
                    _2fa = " » 2FA Active"
                else:
                    _2fa = ""
                prints.message(
                    f"Detected a valid token » {color.purple(r['username'])}#{color.purple(r['discriminator'])}{_2fa}")
                prompt = prints.input("Do you want to use it? (y/n)")
                if prompt.lower() == "y" or prompt.lower() == "yes":
                    json_object = json.load(
                        open(
                            os.path.join(
                                files.documents(),
                                "Luna/discord.json"),
                            encoding="utf-8"))
                    json_object["token"] = Encryption(
                        '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(valid_tokens[0])
                    files.write_json(
                        os.path.join(
                            files.documents(),
                            "Luna/discord.json"),
                        json_object)
                    return True
                else:
                    prints.message("Please manually enter a valid token.")
                    if luna.prompt_token():
                        prints.event("Starting Luna...")
                    else:
                        prints.error("Invalid token")
                        time.sleep(5)
                        prints.event(
                            "Redirecting to the main menu in 5 seconds")
                        time.sleep(5)
                        luna.authentication()
            else:
                prints.error(
                    "Failed to find any valid tokens. Please manually enter a valid token.")
                if luna.prompt_token():
                    prints.event("Starting Luna...")
                else:
                    prints.error("Invalid token")
                    time.sleep(5)
                    prints.event(
                        "Redirecting to the main menu in 5 seconds")
                    time.sleep(5)
                    luna.authentication()
        else:
            prints.error(
                "Failed to find any valid tokens. Please manually enter a valid token.")
            if luna.prompt_token():
                prints.event("Starting Luna...")
            else:
                prints.error("Invalid token")
                time.sleep(5)
                prints.event("Redirecting to the main menu in 5 seconds")
                time.sleep(5)
                luna.authentication()
    except BaseException:
        prints.error(
            "Failed to find any valid tokens. Please manually enter a valid token.")
        if luna.prompt_token():
            prints.event("Starting Luna...")
        else:
            prints.error("Invalid token")
            time.sleep(5)
            prints.event("Redirecting to the main menu in 5 seconds")
            time.sleep(5)
            luna.authentication()