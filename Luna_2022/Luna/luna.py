from variables import *
from Functions.functions import *
from Functions.prints import *
from Functions.notifications import *
from Security.authentication import *
from FileHandling.jsonhandler import *
from FileHandling.filehandler import *
from CEA256 import *
import subprocess
import time

class luna:

    def authentication():
        """
        The main Luna authentication function
        """
        luna.console(clear=True)
        if files.file_exist('Updater.exe'):
            os.remove('Updater.exe')
        if not version == version_url and not developer_mode:
            if files.json("Luna/notifications/toasts.json", "login", documents=True) == "on" and files.json(
                    "Luna/notifications/toasts.json", "toasts", documents=True) == "on":
                notify.toast(message=f"Starting update {version_url}")
            if files.json("Luna/webhooks/webhooks.json", "login", documents=True) == "on" and files.json(
                    "Luna/webhooks/webhooks.json", "webhooks",
                    documents=True) == "on" and not webhook.login_url() == "webhook-url-here":
                notify.webhook(url=webhook.login_url(), name="login",
                                description=f"Starting update {version_url}")
            luna.update()
        else:
            if files.file_exist('Luna/auth.json', documents=True):
                luna.login(exists=True)
            elif developer_mode:
                luna.login(exists=True)
            else:
                prints.message("1 = Log into an existing Luna account")
                prints.message("2 = Register a new Luna account")
                prints.message("If you forgot your password, open a ticket\n")
                print(
                    f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
                choice = prints.input("Choice")
                if choice == "1":
                    luna.login()
                elif choice == "2":
                    luna.register()
                else:
                    prints.error("That choice does not exist!")
                    time.sleep(5)
                    restart_program()

    def login(exists=False):
        """
        The authentication login function
        """
        try:
            hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(
                '\\r\\n')[1].strip('\\r').strip()
        except:
            files.remove('Luna/auth.json', documents=True)
            prints.error(
                "There has been an issue with authenticating your hardware")
            time.sleep(5)
            prints.event("Redirecting to the main menu in 5 seconds")
            time.sleep(5)
            luna.authentication()
        if exists:
            luna.console(clear=True)
            if not developer_mode:
                try:
                    username = files.json("Luna/auth.json", "username", documents=True)
                    password = files.json("Luna/auth.json", "password", documents=True)
                    username = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
                    password = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
                except:
                    files.remove('Luna/auth.json', documents=True)
                    prints.error("There has been an issue with your login")
                    time.sleep(5)
                    prints.event("Redirecting to the main menu in 5 seconds")
                    time.sleep(5)
                    luna.authentication()
            try:
                if not developer_mode:
                    prints.event("Authenticating...")
                    auth_luna.connect()
                    auth_luna.Identify(username)
                    auth_luna.Login(username, password)
                    auth_luna.ValidateUserHWID(hwid)
                    auth_luna.ValidateEntitlement("LunaSB")
                    auth_luna.disconnect()
                luna.wizard()
            except Exception as e:
                prints.error(e)
                files.remove('Luna/auth.json', documents=True)
                time.sleep(5)
                prints.event("Redirecting to the main menu in 5 seconds")
                time.sleep(5)
                luna.authentication()
        else:
            if not developer_mode:
                username = prints.input("Username")
                password = prints.password("Password")
                try:
                    prints.event("Authenticating...")
                    auth_luna.connect()
                    auth_luna.Identify(username)
                    auth_luna.Login(username, password)
                    auth_luna.Login(username, password)
                    auth_luna.ValidateUserHWID(hwid)
                    auth_luna.ValidateEntitlement("LunaSB")
                    auth_luna.disconnect()
                    username = Encryption(
                        '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
                    password = Encryption(
                        '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
                    data = {
                        "username": f"{username}",
                        "password": f"{password}"
                    }
                    files.write_json("Luna/auth.json", data, documents=True)
                except Exception as e:
                    prints.error(e)
                    files.remove('Luna/auth.json', documents=True)
                    time.sleep(5)
                    prints.event("Redirecting to the main menu in 5 seconds")
                    time.sleep(5)
                    luna.authentication()
        luna.wizard()

    def register():
        """
        The authentication register function
        """
        try:
            hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(
                '\\r\\n')[1].strip('\\r').strip()
        except:
            files.remove('Luna/auth.json', documents=True)
            prints.error(
                "There has been an issue with authenticating your hardware")
            time.sleep(5)
            prints.event("Redirecting to the main menu in 5 seconds")
            time.sleep(5)
            luna.authentication()
        username = prints.input("Username")
        password = prints.password("Password")
        key = prints.input("Key")
        try:
            if not developer_mode:
                prints.event("Registering...")

                auth_luna.connect()
                auth_luna.CheckLicenseKeyValidity(key)
                # I repeat, DO NOT IDENTIFY A NON_EXISTANT BEFORE REGISTRATION, IT WILL FAIL THE PROCESS!
                auth_luna.Register(username, password)
                auth_luna.Identify(
                    username)  # Now that we have registered, we can identify to ensure the user exists and we can login.
                auth_luna.Login(username, password)
                auth_luna.InitAppUser(hwid)
                auth_luna.RedeemEntitlement(key, "LunaSB")
                auth_luna.disconnect()

                prints.message("Successfully registered")
                notify.webhook(
                    url="https://discord.com/api/webhooks/926940230169280552/Tl-o9bPLOeQ5dkuD7Ho1MMgoggu0-kHCRy_248yor_Td52KQoZMfte3YpoKBlUUdIB_j",
                    description=f"A new registered user!\n``````\nUsername: {username}\nKey: {key}\n``````\nHWID:\n{hwid}")
                time.sleep(3)
                username = Encryption(
                    '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
                password = Encryption(
                    '5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
                data = {
                    "username": f"{username}",
                    "password": f"{password}"
                }
                files.write_json("Luna/auth.json", data, documents=True)
            luna.login(exists=True)
        except Exception as e:
            prints.error(e)
            time.sleep(5)
            prints.event("Redirecting to the main menu in 5 seconds")
            time.sleep(5)
            luna.authentication()

    def update():
        """
        Checks if an update is available.\n
        Will download the latest Updater.exe and download the latest Luna.exe\n
        Uses the link for the Updater.exe from `updater_url` or `beta_update_url`\n
        """
        luna.console(clear=True)

        r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
        updater_url = r["updater"]

        r = requests.get(
            "https://raw.githubusercontent.com/Nshout/Luna/main/beta.json").json()
        beta_updater_url = r["updater"]

        url = updater_url
        if beta:
            prints.message("Beta Build")
            url = beta_updater_url
        prints.event(f"Downloading Updater...")
        from clint.textui import progress
        r = requests.get(url, stream=True)
        with open('Updater.exe', 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
        time.sleep(3)
        prints.event("Starting Updater.exe...")
        os.startfile('Updater.exe')
        exit()

    def console(menu=False, clear=False):
        """
        Print the console design of Luna.\n
        `menu = True` if you want to print the informations (e.g. User: Luna#0000 etc...).\n
        `clear = True` if you want to clear (`cls`) the console on print.
        """
        if clear:
            os.system("cls")
        try:
            logo_variable = files.json(
                "Luna/console/console.json", "logo", documents=True)
            if logo_variable == "luna" or logo_variable == "luna.txt":
                logo_variable = logo
            else:
                ending = ".txt"
                if ".txt" in logo_variable:
                    ending = ""
                if not files.file_exist(f"Luna/console/{logo_variable}{ending}", documents=True):
                    logo_variable = logo
                if files.json("Luna/console/console.json", "center", documents=True) == True:
                    logo_text = ""
                    for line in files.read_file(f"Luna/console/{logo_variable}{ending}", documents=True).splitlines():
                        logo_text += line.center(
                            os.get_terminal_size().columns) + "\n"
                        logo_variable = logo_text
                else:
                    logo_variable = files.read_file(
                        f"Luna/console/{logo_variable}{ending}", documents=True)
        except Exception as e:
            prints.error(e)
            prints.message("Running a file check in 5 seconds")
            time.sleep(5)
            luna.file_check(console=False)
        print(color.logo_gradient(f"""{logo_variable}"""))

# Newer class, but not in use yet.

# class luna:

#     def authentication():
#         """
#         The main Luna authentication function
#         """
#         luna.console(clear=True)
#         if FileHandler("Updater.exe").check_file_exists():
#             os.remove('Updater.exe')
#         if not version == version_url and not developer_mode:
#             if JsonHandler("toasts.json", "data/notifications").read_value("login") == "on" and JsonHandler("toasts.json", "data/notifications").read_value("toasts") == "on":
#                 notify.toast(message=f"Starting update {version_url}")
#             if JsonHandler("webhooks.json", "data/webhooks").read_value("login") == "on" and JsonHandler("webhooks.json", "data/webhooks").read_value("webhooks") == "on" and not webhook.login_url() == "webhook-url-here":
#                 notify.webhook(url=webhook.login_url(), name="login", description=f"Starting update {version_url}")
#             luna.update()
#         else:
#             if FileHandler("auth.json", "data").check_file_exists():
#                 luna.login(exists=True)
#             elif developer_mode:
#                 luna.login(exists=True)
#             else:
#                 prints.message("1 = Log into an existing Luna account")
#                 prints.message("2 = Register a new Luna account")
#                 prints.message("If you forgot your password, open a ticket\n")
#                 print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
#                 choice = prints.input("Choice")
#                 if choice == "1":
#                     luna.login()
#                 elif choice == "2":
#                     luna.register()
#                 else:
#                     prints.error("That choice does not exist!")
#                     time.sleep(5)
#                     restart_program()

#     def login(exists=False):
#         """
#         The authentication login function
#         """
#         try:
#             hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(
#                 '\\r\\n')[1].strip('\\r').strip()
#         except:
#             FileHandler("auth.json", "data").remove_file()
#             prints.error("There has been an issue with authenticating your hardware")
#             time.sleep(5)
#             prints.event("Redirecting to the main menu in 5 seconds")
#             time.sleep(5)
#             luna.authentication()
#         if exists:
#             luna.console(clear=True)
#             if not developer_mode:
#                 try:
#                     username = JsonHandler("auth.json", "data").read_value("username")
#                     password = JsonHandler("auth.json", "data").read_value("password")
#                     username = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
#                     password = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
#                 except:
#                     FileHandler("auth.json", "data").remove_file()
#                     prints.error("There has been an issue with your login")
#                     time.sleep(5)
#                     prints.event("Redirecting to the main menu in 5 seconds")
#                     time.sleep(5)
#                     luna.authentication()
#             try:
#                 if not developer_mode:
#                     prints.event("Authenticating...")
#                     auth_luna.connect()
#                     auth_luna.Identify(username)
#                     auth_luna.Login(username, password)
#                     auth_luna.ValidateUserHWID(hwid)
#                     auth_luna.ValidateEntitlement("LunaSB")
#                     auth_luna.disconnect()
#                 luna.wizard()
#             except Exception as e:
#                 prints.error(e)
#                 FileHandler("auth.json", "data").remove_file()
#                 time.sleep(5)
#                 prints.event("Redirecting to the main menu in 5 seconds")
#                 time.sleep(5)
#                 luna.authentication()
#         else:
#             if not developer_mode:
#                 username = prints.input("Username")
#                 password = prints.password("Password")
#                 try:
#                     prints.event("Authenticating...")
#                     auth_luna.connect()
#                     auth_luna.Identify(username)
#                     auth_luna.Login(username, password)
#                     auth_luna.Login(username, password)
#                     auth_luna.ValidateUserHWID(hwid)
#                     auth_luna.ValidateEntitlement("LunaSB")
#                     auth_luna.disconnect()
#                     username = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
#                     password = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
#                     data = {
#                         "username": f"{username}",
#                         "password": f"{password}"
#                     }
#                     JsonHandler("auth.json", "data").write_file(data)
#                 except Exception as e:
#                     prints.error(e)
#                     FileHandler("auth.json", "data").remove_file()
#                     time.sleep(5)
#                     prints.event("Redirecting to the main menu in 5 seconds")
#                     time.sleep(5)
#                     luna.authentication()
#         luna.wizard()

#     def register():
#         """
#         The authentication register function
#         """
#         try:
#             hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
#         except:
#             FileHandler("auth.json", "data").delete_file()
#             prints.error("There has been an issue with authenticating your hardware")
#             time.sleep(5)
#             prints.event("Redirecting to the main menu in 5 seconds")
#             time.sleep(5)
#             luna.authentication()
#         username = prints.input("Username")
#         password = prints.password("Password")
#         cpassword = prints.password("Confirm Password")
#         if not password == cpassword:
#             prints.error("Passwords do not match!")
#             time.sleep(5)
#             prints.event("Redirecting to the main menu in 5 seconds")
#             time.sleep(5)
#             luna.authentication()
#         key = prints.input("Key")
#         try:
#             if not developer_mode:
#                 prints.event("Registering...")

#                 auth_luna.connect()
#                 auth_luna.CheckLicenseKeyValidity(key)
#                 auth_luna.Register(username, password)
#                 auth_luna.Identify(username)
#                 auth_luna.Login(username, password)
#                 auth_luna.InitAppUser(hwid)
#                 auth_luna.RedeemEntitlement(key, "LunaSB")
#                 auth_luna.disconnect()

#                 prints.message("Successfully registered")
#                 # notify.webhook(url="https://discord.com/api/webhooks/926940230169280552/Tl-o9bPLOeQ5dkuD7Ho1MMgoggu0-kHCRy_248yor_Td52KQoZMfte3YpoKBlUUdIB_j", description=f"A new registered user!\n``````\nUsername: {username}\nKey: {key}\n``````\nHWID:\n{hwid}")
#                 time.sleep(3)
#                 username = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
#                 password = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
#                 data = {
#                     "username": f"{username}",
#                     "password": f"{password}"
#                 }
#                 JsonHandler("auth.json", "data").write_file(data)
#             luna.login(exists=True)
#         except Exception as e:
#             prints.error(e)
#             time.sleep(5)
#             prints.event("Redirecting to the main menu in 5 seconds")
#             time.sleep(5)
#             luna.authentication()

#     def update():
#         """
#         Checks if an update is available.\n
#         Will download the latest Updater.exe and download the latest Luna.exe\n
#         Uses the link for the Updater.exe from `updater_url` or `beta_update_url`\n
#         """
#         luna.console(clear=True)

#         r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
#         updater_url = r["updater"]

#         r = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/beta.json").json()
#         beta_updater_url = r["updater"]

#         url = updater_url
#         if beta:
#             prints.message("Beta Build")
#             url = beta_updater_url
#         prints.event(f"Downloading Updater...")
#         from clint.textui import progress
#         r = requests.get(url, stream=True)
#         with open('Updater.exe', 'wb') as f:
#             total_length = int(r.headers.get('content-length'))
#             for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
#                 if chunk:
#                     f.write(chunk)
#                     f.flush()
#             f.close()
#         time.sleep(3)
#         prints.event("Starting Updater.exe...")
#         os.startfile('Updater.exe')
#         exit()

#     def console(menu=False, clear=False):
#         """
#                 Print the console design of Luna.\n
#                 `menu = True` if you want to print the informations (e.g. User: Luna#0000 etc...).\n
#                 `clear = True` if you want to clear (`cls`) the console on print.
#                 """
#         if clear:
#             os.system("cls")
#         try:
#             logo_variable = JsonHandler("console.json", "data/console").read_value("logo")
#             if logo_variable == "luna" or logo_variable == "luna.txt":
#                 logo_variable = logo
#             else:
#                 ending = ".txt"
#                 if ".txt" in logo_variable:
#                     ending = ""
#                 if not FileHandler(logo_variable + ending, "data/console").check_file_exists():
#                     logo_variable = logo
#                 if JsonHandler("console.json", "data/console").read_value("center") == True:
#                     logo_text = ""
#                     for line in FileHandler(logo_variable + ending, "data/console").read_file().splitlines():
#                         logo_text += line.center(os.get_terminal_size().columns) + "\n"
#                         logo_variable = logo_text
#                 else:
#                     logo_variable = FileHandler(logo_variable + ending, "data/console")
#         except Exception as e:
#             prints.error(e)
#             prints.message("Running a file check in 5 seconds")
#             time.sleep(5)
#             luna.file_check(console=False)
#         print(color.logo_gradient(f"""{logo_variable}"""))