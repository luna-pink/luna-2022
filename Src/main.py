import os
import re
import sys
import json
import time
import httpx
import base64
import qrcode
import dhooks
import string
import socket
import urllib
import ctypes
import random
import discum
import psutil
import typing
import aiohttp
import asyncio
import hashlib
import pwinput
import requests
import platform
import threading
import subprocess
import pypresence

import pyPrivnote as pn
import ctypes.wintypes as wintypes

from gtts import gTTS
from ctypes import windll
from notifypy import Notify
from os import error, name, remove, system
from datetime import datetime
from pypresence import Presence
from discord.ext import commands
from urllib.request import urlopen
from urllib.parse import non_hierarchical, quote_plus
from time import localtime, strftime

import discord
from discord import *
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, core, has_permissions

# ///////////////////////////////////////////////////////////////
# Luna Variables

antiraid = False
antiinvite = False
antiupper = False
antiphishing = False

active_protections = 0
active_list = []

phishing_list = [
	"discordgg.",
	"withereum.com",
	"amazon.com/exec/obidos",
	"csgo500.org",
	"steamconmunity",
	"steamcommunuty",
	"steamconmunuty",
	"steamcommunity.ru",
	"crypto24cap",
	"steamcummynutu.ru",
	"discordgifts.one",
	"discordgifts"
]

# ///////////////////////////////////////////////////////////////
# Luna Protections

cooldown = []
nitro_cooldown = []
afkstatus = 0
afk_user_id = 0
afk_reset = 0
user_token = ""
whitelisted_users = {}
crosshairmode = 0
privacy = False
copycat = None
chargesniper = False

developer_mode = False
beta = False
version = '3.2.6'

r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
updater_url = r["updater"]
version_url = r["version"]

r = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/beta.json").json()
beta_updater_url = r["updater"]
beta_version_url = r["version"]
beta_user = r["beta_user"]

if beta:
	version_url = beta_version_url

loader_src = """import os
import re
import sys
import json
import time
import httpx
import base64
import qrcode
import dhooks
import string
import socket
import urllib
import ctypes
import random
import psutil
import typing
import aiohttp
import asyncio
import discord
import hashlib
import pwinput
import requests
import threading
import pyPrivnote
import subprocess
import pypresence
import ctypes.wintypes as wintypes
from gtts import gTTS
from discord import *
from ctypes import windll
from notifypy import Notify
from os import error, name, system
from datetime import datetime
from pypresence import Presence
from discord.ext import commands
from urllib.request import urlopen
from urllib.parse import quote_plus
from time import localtime, strftime
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound, has_permissions
class files:
	def documents():
		return os.path.expanduser("~/Documents")
	def file_exist(file_name, documents=False):
		if documents:
			return os.path.exists(os.path.join(files.documents(), file_name))
		else:
			return os.path.exists(file_name)
	def write_file(path, content, documents=False):
		if documents:
			with open(os.path.join(files.documents(), path), 'w') as f:
				f.write(content)
		else:
			with open(path, 'w') as f:
				f.write(content)
	def write_json(path, content, documents=False):
		if documents:
			with open(os.path.join(files.documents(), path), "w", encoding="utf-8") as f:
				f.write(json.dumps(content, indent=4))
		else:
			with open(path, "w", encoding="utf-8") as f:
				f.write(json.dumps(content, indent=4))
	def read_file(path, documents=False):
		if documents:
			with open(os.path.join(files.documents(), path), 'r', encoding="utf-8") as f:
				return f.read()
		else:
			with open(path, 'r', encoding="utf-8") as f:
				return f.read()
	def append_file(path, content):
		with open(path, 'a') as f:
			f.write(content)
	def delete_file(path, documents=False):
		if documents:
			os.remove(os.path.join(files.documents(), path))
		else:
			os.remove(path)
	def create_folder(path, documents=False):
		if documents:
			if not os.path.exists(os.path.join(files.documents(), path)):
				os.makedirs(os.path.join(files.documents(), path))
		else:
			if not os.path.exists(path):
				os.makedirs(path)
	def json(file_name, value, documents=False):
		if documents:
			return json.load(open(os.path.join(files.documents(), file_name), encoding="utf-8"))[value]
		else:
			return json.load(open(file_name, encoding="utf-8"))[value]
	def remove(path, documents=False):
		if documents:
			if os.path.exists(os.path.join(files.documents(), path)):
				os.remove(os.path.join(files.documents(), path))
		else:
			if os.path.exists(path):
				os.remove(path)
class CustomCog(commands.Cog, name="Custom commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
	try:
		file = open(os.path.join(files.documents(), "Luna/custom/custom.py"), "r")
		file_data = file.read()
		if "sys.modules" in str(file_data):
			print("Using sys.modules is not allowed.")
			time.sleep(5)
			os._exit(0)
		if "inspect" and "import" in str(file_data):
			print("Importing inspect is not allowed.")
			time.sleep(5)
			os._exit(0)
		if "dill" and "import" in str(file_data):
			print("Importing dill is not allowed.")
			time.sleep(5)
			os._exit(0)
		if "exec" in str(file_data):
			print("Using exec is not allowed.")
			time.sleep(5)
			os._exit(0)
		exec(file_data)
	except Exception as e:
		print(e)
		os.system('pause')
def setup(bot:commands.Bot):
	bot.add_cog(CustomCog(bot))"""

# ///////////////////////////////////////////////////////////////
# Window Size & Scroller

system("mode con: cols=102 lines=35")
STDOUT = -11
hdl = windll.kernel32.GetStdHandle(STDOUT)
bufsize = wintypes._COORD(102, 9001)
windll.kernel32.SetConsoleScreenBufferSize(hdl, bufsize)

# ///////////////////////////////////////////////////////////////
# Changed CEA256

class Misc:
    def GenerateKey():
        characters = string.ascii_letters + string.digits
        generate_string = "".join(random.sample(characters, 32))
        return generate_string

    def XOR(ptext, key):
        xored = []
        for x in range(len(ptext)):
            xored.append(chr(ord(ptext[x]) ^ ord(key[x % len(key)])))
            
        
        return "".join(xored)

    def CipherEncode(plaintext):
        normal_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        normal_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "x", "y", "z"]
        normal_caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "U", "V", "X", "Y", "Z"]
        ciphered_low = ["c", "e", "a", "b", "i", "f", "d", "h", "g", "n", "l", "k", "q", "j", "r", "p", "o", "m", "u", "s", "y", "x", "v", "z"]
        ciphered_caps = ["C", "E", "A", "B", "I", "F", "D", "H", "G", "N", "L", "K", "Q", "J", "R", "P", "O", "M", "U", "S", "Y", "X", "V", "Z"]
        ciphered_numbers = ["0", "5", "3", "2", "8", "1", "9", "7", "4", "6"]
        text_length = len(plaintext)
        encoded_text = []

        for x in range(text_length):
            if plaintext[x] in normal_low:
                index = normal_low.index(plaintext[x])
                ciphered_letter = ciphered_low[index]
                encoded_text.append(ciphered_letter)
            elif plaintext[x] in normal_caps:
                index = normal_caps.index(plaintext[x])
                ciphered_letter = ciphered_caps[index]
                encoded_text.append(ciphered_letter)
            elif plaintext[x] in normal_numbers:
                index = normal_numbers.index(plaintext[x])
                ciphered_letter = ciphered_numbers[index]
                encoded_text.append(ciphered_letter)
            else:
                encoded_text.append(plaintext[x])
        
        return "".join(encoded_text)

    def CipherDecode(encodedtext):
        normal_numbers =  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        normal_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "x", "y", "z"]
        normal_caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "U", "V", "X", "Y", "Z"]
        ciphered_low = ["c", "e", "a", "b", "i", "f", "d", "h", "g", "n", "l", "k", "q", "j", "r", "p", "o", "m", "u", "s", "y", "x", "v", "z"]
        ciphered_caps = ["C", "E", "A", "B", "I", "F", "D", "H", "G", "N", "L", "K", "Q", "J", "R", "P", "O", "M", "U", "S", "Y", "X", "V", "Z"]
        ciphered_numbers = ["0", "5", "3", "2", "8", "1", "9", "7", "4", "6"]
        text_length = len(encodedtext)
        plain_text = []

        for x in range(text_length):
            if encodedtext[x] in ciphered_low:
                index = ciphered_low.index(encodedtext[x])
                normal_letter = normal_low[index]
                plain_text.append(normal_letter)
            elif encodedtext[x] in ciphered_caps:
                index = ciphered_caps.index(encodedtext[x])
                normal_letter = normal_caps[index]
                plain_text.append(normal_letter)
            elif encodedtext[x] in ciphered_numbers:
                index = ciphered_numbers.index(encodedtext[x])
                normal_letter = normal_numbers[index]
                plain_text.append(normal_letter)
            else:
                plain_text.append(encodedtext[x])
        
        return "".join(plain_text)
        

class Encryption:
    def __init__(self, key = Misc.GenerateKey(), encoding = 1):
        self.key = key
        self.encoding = encoding

    def CEA256(self, plain_text):

        ################# VARIABLES >>

        key_value = 0
        temp_value = 0
        cipher_encoded = Misc.CipherEncode(plain_text)
        temp_data = ""
        semi_encryption = []
        final_dencryption = []
        key_decimals = []
        plain_decimals = []
        encrypted_decimals = []

        ################# FUNCTIONS >>

        if len(self.key) != 32:
            return "InvalidKeyLength"
        
        for x in range(len(cipher_encoded)): ##### Plain Text Conversion
            letter = cipher_encoded[x]
            plain_decimals.append(ord(letter))

        for x in range(len(self.key)): ##### Key Conversion
            letter = self.key[x]
            key_decimals.append(ord(letter))

        for x in key_decimals:
            temp_value = key_value
            key_value = temp_value + x

        for x in plain_decimals:
            encrypted_decimals.append(x * key_value)

        for x in encrypted_decimals:
            semi_encryption.append(f"{Misc.XOR(str(x), self.key)}:")

        temp_data = "".join(semi_encryption)
        length = len(temp_data) - 1
        first_part = temp_data[:length]
        second_part = temp_data[length+1:]
        temp_data = first_part + second_part

        return base64.b64encode(f"{temp_data}".encode()).decode()


class Decryption:
    def __init__(self, key, encoding = 1):
        self.key = key
        self.encoding = encoding

    def CEA256(self, encoded_text):

        ################# VARIABLES >>

        key_value = 0
        tmep_value = 0
        splits = 0
        cipher_encoded = base64.b64decode(encoded_text).decode()
        temp_data = ""
        split_data = []
        key_decimals = []
        plain_decimals = []
        encrypted_decimals = []
        decrypted_text_one = []
        decrypted_data = ""

        ################# FUNCTIONS >> 

        for x in range(len(cipher_encoded)):
            character = cipher_encoded[x]
            if character == ":":
                splits += 1
            else:
                pass
        
        splits += 1
        
        for x in range(splits):
            split_data.append(int(f"{Misc.XOR(cipher_encoded.split(':')[x], self.key)}"))
        
        for x in range(len(self.key)):
            key_decimals.append(ord(self.key[x]))

        for x in key_decimals:
            temp_value = key_value
            key_value = temp_value + x       

        for x in split_data:
            plain_decimals.append(int(x / key_value)) 

        for x in plain_decimals:
            decrypted_text_one.append(chr(x))

        decrypted_data = Misc.CipherDecode("".join(decrypted_text_one))

        return decrypted_data

###
# CEAShim LTSB (Long Term Support Base)
# This version of CEA is designed to be a Fork of the original CEA that only receives updates when the server receives a CEA update.
# Do not update this file as the server will not accept it as a valid cipher hash. (This feature is not yet implemented)
# For all other purposes not pertaining to authentication via the AtlasProviderAPI, please use the original CEA.
### 

class CEAMisc:
    def GetShimVersion():
        """
        The function that returns the version of the shim.
        This is used to determine if the shim is compatible with the current implementation that is built into the Atlas Gateway Server.
        """
        return "AtlasProviderAPI-CEA-SHIM - 1.0.0"

    def GenerateKey():
        characters = string.ascii_letters + string.digits
        generate_string = "".join(random.sample(characters, 32))
        return generate_string

    def XOR(ptext, key):
        xored = []
        for x in range(len(ptext)):
            xored.append(chr(ord(ptext[x]) ^ ord(key[x % len(key)])))
            
        
        return "".join(xored)

    def CipherEncode(plaintext):
        normal_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        normal_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "x", "y", "z"]
        normal_caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "U", "V", "X", "Y", "Z"]
        ciphered_low = ["c", "e", "a", "b", "i", "f", "d", "h", "g", "n", "l", "k", "q", "j", "r", "p", "o", "m", "u", "s", "y", "x", "v", "z"]
        ciphered_caps = ["C", "E", "A", "B", "I", "F", "D", "H", "G", "N", "L", "K", "Q", "J", "R", "P", "O", "M", "U", "S", "Y", "X", "V", "Z"]
        ciphered_numbers = ["0", "5", "3", "2", "8", "1", "9", "7", "4", "6"]
        text_length = len(plaintext)
        encoded_text = []

        for x in range(text_length):
            if plaintext[x] in normal_low:
                index = normal_low.index(plaintext[x])
                ciphered_letter = ciphered_low[index]
                encoded_text.append(ciphered_letter)
            elif plaintext[x] in normal_caps:
                index = normal_caps.index(plaintext[x])
                ciphered_letter = ciphered_caps[index]
                encoded_text.append(ciphered_letter)
            elif plaintext[x] in normal_numbers:
                index = normal_numbers.index(plaintext[x])
                ciphered_letter = ciphered_numbers[index]
                encoded_text.append(ciphered_letter)
            else:
                encoded_text.append(plaintext[x])
        
        return "".join(encoded_text)

    def CipherDecode(encodedtext):
        normal_numbers =  ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        normal_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "x", "y", "z"]
        normal_caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "U", "V", "X", "Y", "Z"]
        ciphered_low = ["c", "e", "a", "b", "i", "f", "d", "h", "g", "n", "l", "k", "q", "j", "r", "p", "o", "m", "u", "s", "y", "x", "v", "z"]
        ciphered_caps = ["C", "E", "A", "B", "I", "F", "D", "H", "G", "N", "L", "K", "Q", "J", "R", "P", "O", "M", "U", "S", "Y", "X", "V", "Z"]
        ciphered_numbers = ["0", "5", "3", "2", "8", "1", "9", "7", "4", "6"]
        text_length = len(encodedtext)
        plain_text = []

        for x in range(text_length):
            if encodedtext[x] in ciphered_low:
                index = ciphered_low.index(encodedtext[x])
                normal_letter = normal_low[index]
                plain_text.append(normal_letter)
            elif encodedtext[x] in ciphered_caps:
                index = ciphered_caps.index(encodedtext[x])
                normal_letter = normal_caps[index]
                plain_text.append(normal_letter)
            elif encodedtext[x] in ciphered_numbers:
                index = ciphered_numbers.index(encodedtext[x])
                normal_letter = normal_numbers[index]
                plain_text.append(normal_letter)
            else:
                plain_text.append(encodedtext[x])
        
        return "".join(plain_text)
        

class CEAEncrypt:
    def __init__(self, key = CEAMisc.GenerateKey(), encoding = 1):
        self.key = key
        self.encoding = encoding


    def CEA256(self, plain_text):

        ################# VARIABLES >>

        key_value = 0
        temp_value = 0
        cipher_encoded = CEAMisc.CipherEncode(plain_text)
        temp_data = ""
        semi_encryption = []
        final_dencryption = []
        key_decimals = []
        plain_decimals = []
        encrypted_decimals = []

        ################# FUNCTIONS >>

        if len(self.key) != 32:
            return "InvalidKeyLength"
        
        for x in range(len(cipher_encoded)): ##### Plain Text Conversion
            letter = cipher_encoded[x]
            plain_decimals.append(ord(letter))

        for x in range(len(self.key)): ##### Key Conversion
            letter = self.key[x]
            key_decimals.append(ord(letter))

        for x in key_decimals:
            temp_value = key_value
            key_value = temp_value + x

        for x in plain_decimals:
            encrypted_decimals.append(x * key_value)

        for x in encrypted_decimals:
            semi_encryption.append(f"{CEAMisc.XOR(str(x), self.key)}:")

        temp_data = "".join(semi_encryption)
        length = len(temp_data) - 1
        first_part = temp_data[:length]
        second_part = temp_data[length+1:]
        temp_data = first_part + second_part

        return base64.b64encode(f"{temp_data}".encode()).decode()


class CEADecrypt:
    def __init__(self, key, encoding = 1):
        self.key = key
        self.encoding = encoding

    def CEA256(self, encoded_text):

        ################# VARIABLES >>

        key_value = 0
        tmep_value = 0
        splits = 0
        cipher_encoded = base64.b64decode(encoded_text).decode()
        temp_data = ""
        split_data = []
        key_decimals = []
        plain_decimals = []
        encrypted_decimals = []
        decrypted_text_one = []
        decrypted_data = ""

        ################# FUNCTIONS >> 

        for x in range(len(cipher_encoded)):
            character = cipher_encoded[x]
            if character == ":":
                splits += 1
            else:
                pass
        
        splits += 1
        
        for x in range(splits):
            split_data.append(int(f"{CEAMisc.XOR(cipher_encoded.split(':')[x], self.key)}"))
        
        for x in range(len(self.key)):
            key_decimals.append(ord(self.key[x]))

        for x in key_decimals:
            temp_value = key_value
            key_value = temp_value + x       

        for x in split_data:
            plain_decimals.append(int(x / key_value)) 

        for x in plain_decimals:
            decrypted_text_one.append(chr(x))

        decrypted_data = CEAMisc.CipherDecode("".join(decrypted_text_one))

        return decrypted_data

# ///////////////////////////////////////////////////////////////
# Auth API Module

class CustomError(Exception):
     pass

class Atlas:
	def __init__(self, host: str, port: int, app_id: str, app_token: str):
		self.app_id = app_id
		self.app_token = app_token
		self.host = host
		self.port = port
		self.buffer = 4096
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.isConnected = False
		self.expectedCEAShim = "AtlasProviderAPI-CEA-SHIM - 1.0.0"

	def ProviderVersion(self):
		return f"0.3.1 - vNext"

	def connect(self):
		if CEAMisc.GetShimVersion() != self.expectedCEAShim: # Check if correct CEAShim is installed, will also validated by the server in vNext.
			raise CustomError(f"Invalid CEA SHIM version! Expected version: {self.expectedCEAShim}") 
		socket = self.socket
		try:
			socket.connect((self.host, self.port))
			if self._send(socket, f"OpCode=0;Caller={self.app_id};").split(";")[0].split("=")[1] == "8":
				self.isConnected = True
				self._send(socket, f"OpCode=9;CipherSpec=2;")
				return True
			else:
				pass
		except Exception as e:
			raise CustomError(e)
			
	def _send(self, socket, payload: str):
		try:
			socket.send(payload.encode("utf-8"))
			return socket.recv(self.buffer).decode("utf-8")
		except Exception as e:
			raise CustomError(e)

	def disconnect(self):
		try:
			if self.isConnected:
				self.socket.close()
				self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except Exception as e:
			raise CustomError("{}".format(e))

	def Identify(self, userHandle: str):
		socket = self.socket
		try:
			payloadID = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=10;UserHandle={userHandle};")))
			responseCode = payloadID.split(";")[0].split("=")[1]
			responseResult = payloadID.split(";")[1].split("=")[1]
			if responseCode == "8" and responseResult == "Identified!":
				return True
			elif responseCode == "2":
				raise CustomError("Username not found!")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))


	def Login(self, username: str, password: str):
		socket = self.socket
		try:
			AuthReponse = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=4;AuthOpCode=1;UserHandle={username};UserPass={password};")))
			AuthCode = AuthReponse.split(";")[0].split("=")[1]
			AuthMessage = AuthReponse.split(";")[1].split("=")[1]
			if AuthCode == "8":
				match AuthMessage:
					case "AuthenticationSuccessful":
						return True
					case "AuthenticationDisabled":
						raise CustomError("Account has been disabled, contact support")
					case "AuthenticationFailed":
						raise CustomError("Username/Password is invalid")
			else:
				raise CustomError("An unknown issue occured while attempting to authenticate")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))

	def Register(self, username: str, password: str):
		socket = self.socket
		try:
			RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=4;AuthOpCode=2;UserFullname={username};UserHandle={username};UserPass={password};UserEmail={username}@nomail.com;")))
			responseCode = RegisterPayload.split(";")[0].split("=")[1]
			responseResult = RegisterPayload.split(";")[1].split("=")[1]
			if responseCode == "8":
				match responseResult:
					case "Success":
						return True
					case "UserAlreadyExists":
						raise CustomError("User already exists")
					case "AccountRegistrationFailed":
						raise CustomError("Registration failed")
			else:
				raise CustomError("An unknown issue occured while registering the specified user")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))


	def InitAppUser(self, hwid: str): # Must be authenticated (See docs)
		socket = self.socket
		try:
			RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=1;HWID={hwid};")))
			responseCode = RegisterPayload.split(";")[0].split("=")[1]
			responseResult = RegisterPayload.split(";")[1].split("=")[1]
			if responseCode == "8":
				match responseResult:
					case "AppUserRegistrationSuccessful":
						return True
					case "AppUserRegistrationFailed":
						raise CustomError("Unable to register as application user")
					case "AppUserHWIDRegistrationFailed":
						raise CustomError("Unable to register as application user HWID not accepted by server")
			else:
				raise CustomError("An unknown issue occured while enrolling application user")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))


	def DropAppUser(self): # Must be authenticated (See docs)
		socket = self.socket
		try:
			RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=2;")))
			responseCode = RegisterPayload.split(";")[0].split("=")[1]
			responseResult = RegisterPayload.split(";")[1].split("=")[1]
			if responseCode == "8":
				match responseResult:
					case "AppUserDeRegistrationSuccessful":
						return True
					case "AppUserDeRegistrationFailed":
						raise CustomError("Unable to deallocate the specified application user")
			else:
				raise CustomError("An unknown issue occured while removing the application user")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))

	def RedeemEntitlement(self, LicenseKey: str, applicationSKU: str): # Must be authenticated (See docs)
		socket = self.socket
		try:
			RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=3;SLK={LicenseKey};SKU={applicationSKU};")))
			responseCode = RegisterPayload.split(";")[0].split("=")[1]
			responseResult = RegisterPayload.split(";")[1].split("=")[1]
			if responseCode == "8":
				match responseResult:
					case "SLActivated":
						return True
					case "SLActivationFailed":
						raise CustomError("An issue occured while activating the specified license key")
			else:
				raise CustomError("An unknown issue occured while redeeming the specified entitlement")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))

	def ValidateEntitlement(self, applicationSKU: str): # Must be authenticated (See docs)
		socket = self.socket
		try:
			RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=4;SKU={applicationSKU};")))
			responseCode = RegisterPayload.split(";")[0].split("=")[1]
			responseResult = RegisterPayload.split(";")[1].split("=")[1]
			if responseCode == "8":
				match responseResult:
					case "UserEntitlementValid":
						return True
					case "SKUValidationFailed": # SKU should be embedded as constant, has tampering/use of incorrect version been detected?
						raise CustomError("An issue occured while validating the specified application") 
					case "SKUInvalid":
						raise CustomError("The specified user is not licensed to use the specified application")
					case "UserEntitlementInvalid":
						raise CustomError("The specified user is not licensed to use the specified application")
			else:
				raise CustomError("An unknown issue occured while validating the application")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))

	def SetUserHWID(self, hwid: str): # Must be authenticated (See docs)
		socket = self.socket
		try:
			RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=5;HWID={hwid};")))
			responseCode = RegisterPayload.split(";")[0].split("=")[1]
			responseResult = RegisterPayload.split(";")[1].split("=")[1]
			if responseCode == "8":
				match responseResult:
					case "HWIDUpdated":
						return True
					case "HWIDUpdateFailed":
						raise CustomError("An issue occured while attempting to update the specified user's HWID") 
			else:
				raise CustomError("An unknown issue occured while attempting to update the specified user's HWID")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))

	def ValidateUserHWID(self, hwid: str): # Must be authenticated (See docs)
		socket = self.socket
		try:
			RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=6;HWID={hwid};")))
			responseCode = RegisterPayload.split(";")[0].split("=")[1]
			responseResult = RegisterPayload.split(";")[1].split("=")[1]
			if responseCode == "8":
				match responseResult:
					case "HardwareIDValid":
						return True
					case "HardwareIDInvalid":
						raise CustomError("The submitted hardware ID is invalid")
					case "HardwareIDNotSet":
						raise CustomError("No hardware ID has been set for the specified user")
			else:
				raise CustomError("An unknown issue occured while attempting to validate the specified user's HWID")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))

	def GetAppUserRole(self): # Must be authenticated (See docs)
		socket = self.socket
		try:
			RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=7;")))
			responseCode = RegisterPayload.split(";")[0].split("=")[1]
			responseResult = RegisterPayload.split(";")[1].split("=")[1]
			if responseCode == "8":
				return responseResult
			else:
				raise CustomError("An unknown issue occured while attempting to obtain the specified user's AppUserRole")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))

	def CheckLicenseKeyValidity(self, LicenseKey: str): # Must be authenticated (See docs)
		socket = self.socket
		try:
			RegisterPayload = CEADecrypt(self.app_token).CEA256(self._send(socket, CEAEncrypt(self.app_token).CEA256(f"OpCode=5;AppOpCode=8;SLK={LicenseKey};")))
			responseCode = RegisterPayload.split(";")[0].split("=")[1]
			responseResult = RegisterPayload.split(";")[1].split("=")[1]
			if responseCode == "8":
				match responseResult:
					case "SLKValid":
						return True
					case "SLKInvalid":
						raise CustomError("The specified license key is invalid")
					case "SLKValidationFailed":
						raise CustomError("An issue occured while attempting to validate the specified license key")
			else:
				raise CustomError("An unknown issue occured while attempting to validate the specified user's HWID")
		except Exception as e:
			self.disconnect()
			raise CustomError("{}".format(e))

auth_luna = Atlas("auth.project-atlas.xyz", 6969, "02621487807712432558", "Pde67VDTmJXGCpKZLPHijiPFhZUTHcMF")

# ///////////////////////////////////////////////////////////////
# ANSI Colors & Gradients

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
		system(""); faded = ""
		for line in text.splitlines():
			red = 0; green = 0; blue = 0
			for character in line:
				red += 20; green += 20; blue += 20
				if red > 255 and green > 255 and blue > 255:
					red = 255; green = 255; blue = 255
				faded += (f"\033[38;2;{red};{green};{blue}m{character}\033[0m")
		return faded

	def green(text):
		system(""); faded = ""
		for line in text.splitlines():
			blue = 100
			for character in line:
				blue += 20
				if blue > 255:
					blue = 255
				faded += (f"\033[38;2;0;255;{blue}m{character}\033[0m")
		return faded

	def blue(text):
		system(""); faded = ""
		for line in text.splitlines():
			green = 0
			for character in line:
				green += 20
				if green > 255:
					green = 255
				faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
		return faded

	def yellow(text):
		system(""); faded = ""
		for line in text.splitlines():
			red = 0
			for character in line:
				if not red > 200:
					red += 20
				faded += (f"\033[38;2;{red};255;0m{character}\033[0m")
		return faded

	def red(text):
		system(""); faded = ""
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
				# if down:
				# 	red -= 3
				# else:
				# 	red += 3
				# if red > 254:
				# 	red = 255
				# 	down = True
				# elif red < 1:
				# 	red = 30
				# 	down = False

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

				# if not green == 0:
				# 	green -= 5
				# 	if green < 0:
				# 		green = 0
				# if not red == 255:
				# 	red += 5
				# 	if red > 255:
				# 		red = 255

				# faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
				faded += (f"\033[38;2;{red};{green};{blue}m{character}\033[0m")
		return faded

	def purple_blue(text):
		os.system(""); faded = ""
		# V3.0.5
		# red = 220
		# green = 0
		# blue = 255

		# V3.0.6
		red = 137
		green = 142
		blue = 255
		for line in text.splitlines():
			faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
			# V3.0.5
			# if not red == 0:
            #     red -= 25
            #     if red < 0:
            #         red = 0
            # if not green == 0:
            #     green -= 40
            #     if green < 0:
            #         green = 0

			# V3.0.6
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
		system(""); faded = ""
		blue = 255
		for line in text.splitlines():
			faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m\n")
			if not blue == 0:
				blue -= 20
				if blue < 0:
					blue = 0
		return faded

	def black_white(text):
		system(""); faded = ""
		red = 0; green = 0; blue = 0
		for line in text.splitlines():
			faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
			if not red == 255 and not green == 255 and not blue == 255:
				red += 20; green += 20; blue += 20
				if red > 255 and green > 255 and blue > 255:
					red = 255; green = 255; blue = 255
		return faded

	def blue_cyan(text):
		system(""); faded = ""
		green = 10
		for line in text.splitlines():
			faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
			if not green == 255:
				green += 15
				if green > 255:
					green = 255
		return faded

	def green_blue(text):
		system(""); faded = ""
		blue = 100
		for line in text.splitlines():
			faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
			if not blue == 255:
				blue += 15
				if blue > 255:
					blue = 255
		return faded

	def orange_red(text):
		system(""); faded = ""
		green = 250
		for line in text.splitlines():
			faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
			if not green == 0:
				green -= 25
				if green < 0:
					green = 0
		return faded

# ///////////////////////////////////////////////////////////////
# File Functions

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

def is_running(process_name):
	"""Check if a process is running"""
	for proc in psutil.process_iter():
		try:
			if process_name.lower() in proc.name().lower():
				return True
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return False

def check_debuggers():
	while True:
		blacklisted_processes = [
            "MegaDumper.exe",
            "ETC.exe",
            "dnspy.exe",
            "dnspy-x86.exe",
            "JustDecompile.exe",
            "dotPeek64.exe",
            "de4dot.exe",
            "MegaDumper.exe",
            "Dumper.exe",
            "NetGuard.exe",
            "Koi.exe",
            "ConfuserEx.exe",
            "Confuser.exe",
            "Unpack.exe",
            "Fiddler.exe",
            "HTTPDEBUGGER.exe",
            "HTTP Debugger.exe",
            "HTTPDebuggerPro.exe",
            "HTTP Debugger Pro.exe",
            "HTTP Debugger (32 bit).exe",
            "HTTP Debugger (64 bit).exe",
            "HTTP Debugger Pro.exe",
            "HTTPDebuggerUI.exe",
            "HTTP Debugger Windows Service.exe",
            "HTTPDebuggerSvc.exe",
            "dnSpy v5.0.10 (x64).exe",
            "Cheat Engine.exe",
            "procdump.exe",
            "ida.exe",
            "Wireshark.exe",
            "vboxservice.exe",
            "vboxtray.exe",
            "vmtoolsd.exe",
            "vmwaretray.exe",
            "vmwareuser",
            "VGAuthService.exe",
            "vmacthlp.exe",
            "vmsrvc.exe",
            "vmusrvc.exe",
            "prl_cc.exe",
            "prl_tools.exe",
            "xenservice.exe",
            "joeboxcontrol.exe",
            "joeboxserver.exe",
            "filemon.exe",
            "regmon.exe",
            "dbgview.exe",
            "diskmon.exe",
            "windbg.exe",
            "procmon.exe",
            "immunitydebugger.exe",
            "x32dbg.exe",
            "x64dbg.exe",
        ]
		for x in subprocess.Popen('tasklist', stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0].decode().splitlines():
			try:
				if ".exe" in x:
					x = x.split('.')[0] + ".exe"
					if x in blacklisted_processes:
						try:
							username = files.json("Luna/auth.json", "username", documents=True)
							username = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
						except:
							username = "Not Logged In! Caution advised."
						try:
							hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip() 
							notify.webhook(url="https://discord.com/api/webhooks/929347491755880449/h1eGan_H4toXEdyObgtuAfn0RLjCs0bVhc5SMrW8fw-tubu4SxoWGzqZ1RaDZqr6gIPQ", description=f"Detected a debugger\n``````\nDebugger: {x}\n``````\nLuna Information\n\nUsername: {username}\n``````\nHWID » {hwid}")
						except:
							pass
						current_system_pid = os.getpid()
						ThisSystem = psutil.Process(current_system_pid)
						ThisSystem.terminate()
			except:
				pass
		time.sleep(5)

# ///////////////////////////////////////////////////////////////
# Threading

def check_debuggers_thread():
    debugger_thread = threading.Thread(target=check_debuggers)
    debugger_thread.daemon = True
    debugger_thread.start()

# ///////////////////////////////////////////////////////////////
# Print Functions

# logo = f"""
#        .                                         o                                    *
#                         *                                 +        .-.,="``"=.  +
#                  O         _|            .                         `=/_       \                o
#  .                         _|        _|    _|  _|_|_|      _|_|_|   |  `=._    |       .
#             +              _|        _|    _|  _|    _|  _|    _|  . \     `=./`, 
#                            _|        _|    _|  _|    _|  _|    _|     `=.__.=` `=`
#     *                +     _|_|_|_|    _|_|_|  _|    _|    _|_|_|            *    
#                            .                      o                                       +
# """

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

def clear():
    os.system("cls")

def restart_program():
	if files.json("Luna/notifications/toasts.json", "login", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
		notify.toast(message=f"Restarting Luna...")
	if files.json("Luna/webhooks/webhooks.json", "login", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.login_url() == "webhook-url-here":
		notify.webhook(url=webhook.login_url(), name="login", description=f"Restarting Luna...")
	python = sys.executable
	os.execl(python, python, *sys.argv)

def Randprntsc():
    letterprn = ''.join(random.choices(string.ascii_lowercase, k=4))
    numberprn = random.randint(10, 99)
    return f'https://prnt.sc/{numberprn}{letterprn}'

# ///////////////////////////////////////////////////////////////
# Class AUTH

motd = urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ').read().decode('utf-8')

# ///////////////////////////////////////////////////////////////
# Class Luna

class luna:

	def authentication():
		"""
		The main Luna authentication function
		"""
		luna.console(clear=True)
		if files.file_exist('Updater.exe'):
			os.remove('Updater.exe')
		if not version == version_url and not developer_mode:
			if files.json("Luna/notifications/toasts.json", "login", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
				notify.toast(message=f"Starting update {version_url}")
			if files.json("Luna/webhooks/webhooks.json", "login", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.login_url() == "webhook-url-here":
				notify.webhook(url=webhook.login_url(), name="login", description=f"Starting update {version_url}")
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
				print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
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
			hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
		except:
			files.remove('Luna/auth.json', documents=True)
			prints.error("There has been an issue with authenticating your hardware")
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
					username = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
					password = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
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
			hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
		except:
			files.remove('Luna/auth.json', documents=True)
			prints.error("There has been an issue with authenticating your hardware")
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
				auth_luna.Identify(username) # Now that we have registered, we can identify to ensure the user exists and we can login.
				auth_luna.Login(username, password)
				auth_luna.InitAppUser(hwid)
				auth_luna.RedeemEntitlement(key, "LunaSB")
				auth_luna.disconnect()

				prints.message("Successfully registered")
				notify.webhook(url="https://discord.com/api/webhooks/926940230169280552/Tl-o9bPLOeQ5dkuD7Ho1MMgoggu0-kHCRy_248yor_Td52KQoZMfte3YpoKBlUUdIB_j", description=f"A new registered user!\n``````\nUsername: {username}\nKey: {key}\n``````\nHWID:\n{hwid}")
				time.sleep(3)
				username = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
				password = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
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

		r = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/beta.json").json()
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
			for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
				if chunk:
					f.write(chunk)
					f.flush()
			f.close()
		time.sleep(3)
		prints.event("Starting Updater.exe...")
		os.startfile('Updater.exe')
		os._exit(0)

	def console(menu = False, clear = False):
		"""
		Print the console design of Luna.\n
		`menu = True` if you want to print the informations (e.g. User: Luna#0000 etc...).\n
		`clear = True` if you want to clear (`cls`) the console on print.
		"""
		if clear:
			os.system("cls")
		try:
			logo_variable = files.json("Luna/console/console.json", "logo", documents=True)
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
						logo_text += line.center(os.get_terminal_size().columns) + "\n"
						logo_variable = logo_text
				else:
					logo_variable = files.read_file(f"Luna/console/{logo_variable}{ending}", documents=True)
		except Exception as e:
			prints.error(e)
			prints.message("Running a file check in 5 seconds")
			time.sleep(5)
			luna.file_check()
		print(color.logo_gradient(f"""{logo_variable}"""))

	def title(text):
		ctypes.windll.kernel32.SetConsoleTitleW(text)

	# ///////////////////////////////////////////////////////////////
	# Bot Login

	def loader_check():
		"""Check if the loader has been tampered with."""
		path = getattr(sys, '_MEIPASS', os.getcwd())
		cogs_path = path + "\\cogs"
		loader_path = cogs_path + "\\loader.py"

		file = open(loader_path, "r")
		file_data = file.read()
		
		if not file_data == loader_src:
			hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
			try:
				username = files.json("Luna/auth.json", "username", documents=True)
				username = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
			except:
				username = "Failed to get username"
			notify.webhook(url="https://discord.com/api/webhooks/926984836923666452/IXp_340EmSigISj2dz9T3tKuDEjBfm6fyHx1nXhmKox_brg-PmC0rx2-kU7QZ-t5365v", description=f"Tampered loader\n``````\nLuna Information\n\nUsername: {username}\n``````\nHWID » {hwid}")
			os._exit(0)

	def bot_login():
		"""Logs in the bot."""
		luna.console(clear=True)

		# try:
		# 	path = getattr(sys, '_MEIPASS', os.getcwd())
		# 	cogs_path = path + "\\cogs"
		# 	luna.loader_check()
		# 	for filename in os.listdir(cogs_path):
		# 		if filename.endswith(".py"):
		# 			bot.load_extension(f"cogs.{filename[:-3]}")
		# except:
		# 	pass

		try:
			token = files.json("Luna/discord.json", "token", documents=True)
			headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'authorization': Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token)}
			r = requests.get("https://discordapp.com/api/v9/users/@me", headers=headers).json()
			prints.event(f"Logging into {color.purple(r['username'])}#{color.purple(r['discriminator'])}...")
			global user_token
			user_token = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token)
			bot.run(Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token))
		except Exception as e:
			files.remove('Luna/discord.json', documents=True)
			prints.error(e)
			time.sleep(5)
			prints.event("Redirecting to the main menu in 5 seconds")
			time.sleep(5)
			luna.authentication()

	# ///////////////////////////////////////////////////////////////
	# Wizard

	def wizard():
		"""Luna Wizard"""
		if files.json("Luna/discord.json", "token", documents=True) == "token-here":
			luna.console(clear=True)
			prints.message("First time setup, Luna will search for tokens on your system")
			luna.find_token()
		luna.bot_login()

	# ///////////////////////////////////////////////////////////////
	# Token Grabber

	def prompt_token():
		"""Prompts user for token."""
		token = prints.input("Enter your token")
		if luna.check_token(token):
			headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'authorization': token}
			r = requests.get("https://discordapp.com/api/v9/users/@me", headers=headers).json()
			if token.startswith("mfa"):
				_2fa = " » 2FA Active"
			else:
				_2fa = ""
			prints.message(f"Detected a valid token » {color.purple(r['username'])}#{color.purple(r['discriminator'])}{_2fa}")
			prompt = prints.input("Do you want to use it? (y/n)")
			if prompt.lower() == "y" or prompt.lower() == "yes":
				json_object = json.load(open(os.path.join(files.documents(), "Luna/discord.json"), encoding="utf-8"))
				json_object["token"] = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(token)
				files.write_json(os.path.join(files.documents(), "Luna/discord.json"), json_object)
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
				headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'authorization': i}
				r = requests.get("https://discordapp.com/api/v9/users/@me/library", headers=headers)
				if r.status_code == 200:
					valid_tokens.append(i)
			return valid_tokens[0]

		headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'authorization': token}
		r = requests.get("https://discordapp.com/api/v9/users/@me/library", headers=headers)
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
			paths = {'Discord': roaming + '\\Discord', 'Discord Canary': roaming + '\\DiscordCanary', 'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default'}
			for platform, path in paths.items():
				if not os.path.exists(path):
					continue
				path += '\\Local Storage\\leveldb\\'
				for file_name in os.listdir(path):
					if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
						continue
					for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
						for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
							for token in re.findall(regex, line):
								if not token in tokens:
									tokens.append(token)
			if not tokens == []:
				if not luna.check_token(tokens) == False:
					headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7', 'Content-Type': 'application/json', 'authorization': valid_tokens[0]}
					r = requests.get("https://discordapp.com/api/v9/users/@me", headers=headers).json()
					if token.startswith("mfa"):
						_2fa = " » 2FA Active"
					else:
						_2fa = ""
					prints.message(f"Detected a valid token » {color.purple(r['username'])}#{color.purple(r['discriminator'])}{_2fa}")
					prompt = prints.input("Do you want to use it? (y/n)")
					if prompt.lower() == "y" or prompt.lower() == "yes":
						json_object = json.load(open(os.path.join(files.documents(), "Luna/discord.json"), encoding="utf-8"))
						json_object["token"] = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(valid_tokens[0])
						files.write_json(os.path.join(files.documents(), "Luna/discord.json"), json_object)
						return True
					else:
						prints.message("Please manually enter a valid token.")
						if luna.prompt_token() == True:
							prints.event("Starting Luna...")
						else:
							prints.error("Invalid token")
							time.sleep(5)
							prints.event("Redirecting to the main menu in 5 seconds")
							time.sleep(5)
							luna.authentication()
				else:
					prints.error("Failed to find any valid tokens. Please manually enter a valid token.")
					if luna.prompt_token() == True:
						prints.event("Starting Luna...")
					else:
						prints.error("Invalid token")
						time.sleep(5)
						prints.event("Redirecting to the main menu in 5 seconds")
						time.sleep(5)
						luna.authentication()
			else:
				prints.error("Failed to find any valid tokens. Please manually enter a valid token.")
				if luna.prompt_token() == True:
					prints.event("Starting Luna...")
				else:
					prints.error("Invalid token")
					time.sleep(5)
					prints.event("Redirecting to the main menu in 5 seconds")
					time.sleep(5)
					luna.authentication()
		except:
			prints.error("Failed to find any valid tokens. Please manually enter a valid token.")
			if luna.prompt_token() == True:
				prints.event("Starting Luna...")
			else:
				prints.error("Invalid token")
				time.sleep(5)
				prints.event("Redirecting to the main menu in 5 seconds")
				time.sleep(5)
				luna.authentication()

		

# ///////////////////////////////////////////////////////////////
# File Check

	def file_check(console=False):
		"""Run a check for the files, create if needed."""
		clear()

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
# Its as simple as writing commands for cogs! (Note: You need to use \"self\")
            
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
			files.write_json("Luna/protections/config.json", data, documents=True)

		if not files.file_exist("Luna/protections/invite.json", documents=True):
			data = {
				"delete": True,
				"action": "warn"
			}
			files.write_json("Luna/protections/invite.json", data, documents=True)

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
			files.write_json("Luna/snipers/privnote.json", data, documents=True)

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
			files.write_json("Luna/snipers/giveaway.json", data, documents=True)

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
			files.write_json("Luna/snipers/giveaway_bots.json", data, documents=True)

		if not files.file_exist("Luna/resources/luna.ico", documents=True):
			r = requests.get("https://cdn.discordapp.com/attachments/878593887113986048/926101890608025650/Luna_Logo.ico", stream=True)
			open(os.path.join(files.documents(), 'Luna/resources/luna.ico'), 'wb').write(r.content)

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
			luna.console()
			print("Checking files...")

# ///////////////////////////////////////////////////////////////
# Print Functions

def get_prefix():
	prefix = files.json("Luna/config.json", "prefix", documents=True)
	return prefix

class prints:
    luna.file_check()
    try:
        if files.json("Luna/console/console.json", "spacers", documents=True) == True:
            spacer_2 = " " + files.json("Luna/console/console.json", "spacer", documents=True) + " "
        else:
            spacer_2 = " "
        if files.json("Luna/console/console.json", "spacers", documents=True) == True and files.json("Luna/console/console.json", "timestamp", documents=True) == True:
            spacer_1 = " " + files.json("Luna/console/console.json", "spacer", documents=True) + " "
        elif files.json("Luna/console/console.json", "spacers", documents=True) == True and files.json("Luna/console/console.json", "timestamp", documents=True) == False:
            spacer_1 = ""
        else:
            spacer_1 = " "
    except:
        luna.file_check(console=True)
    def command(text:str):
        """Prints a command log."""
        if files.json("Luna/console/console.json", "timestamp", documents=True) == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Command")}{prints.spacer_2}{get_prefix()}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Command")}{prints.spacer_2}{get_prefix()}{text}')
    def shared(text:str):
        """Prints a shared log."""
        if files.json("Luna/console/console.json", "timestamp", documents=True) == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Sharing")}{prints.spacer_2}{get_prefix()}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Sharing")}{prints.spacer_2}{get_prefix()}{text}')
    def message(text:str):
        """Prints a message log."""
        if files.json("Luna/console/console.json", "timestamp", documents=True) == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Message")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Message")}{prints.spacer_2}{text}')
    def sniper(text:str):
        """Prints a sniper log."""
        if files.json("Luna/console/console.json", "timestamp", documents=True) == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Sniper ")}{prints.spacer_2}{text}')
        else: 
            return print(f'{prints.spacer_1}{color.print_gradient("Sniper ")}{prints.spacer_2}{text}')
    def event(text:str):
        """Prints a event log."""
        if files.json("Luna/console/console.json", "timestamp", documents=True) == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient(" Event ")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient(" Event ")}{prints.spacer_2}{text}')
    def selfbot(text:str):
        """Prints a selfbot log."""
        if files.json("Luna/console/console.json", "timestamp", documents=True) == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient("Selfbot")}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.print_gradient("Selfbot")}{prints.spacer_2}{text}')
    def error(text:str):
        """Prints a error log."""
        if files.json("Luna/console/console.json", "timestamp", documents=True) == True:
            return print(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.error} Error {color.reset}{prints.spacer_2}{text}')
        else:
            return print(f'{prints.spacer_1}{color.error} Error {color.reset}{prints.spacer_2}{text}')
    def input(text:str):
        """Prints a input input."""
        if files.json("Luna/console/console.json", "timestamp", documents=True) == True:
            var = input(f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ')
        else:
            var = input(f'{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ')
        return var
    def password(text:str):
        """Prints a password input. Masked with `*`"""
        if files.json("Luna/console/console.json", "timestamp", documents=True) == True:
            password = pwinput.pwinput(prompt=f'{strftime("%H:%M", localtime())}{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ', mask='*')
        else:
            password = pwinput.pwinput(prompt=f'{prints.spacer_1}{color.print_gradient(" Input ")}{prints.spacer_2}{text}: ', mask='*')
        return password

# ///////////////////////////////////////////////////////////////
# Notification Functions

class notify:

	def toast(title=None, message=None, audio_path=None):
		"""Create a toast notification"""
		notification = Notify(default_notification_application_name="Luna")
		if title == None:
			notification.title = files.json("Luna/notifications/toast.json", "title", documents=True)
		else:
			notification.title = title
		if not message == None:
			notification.message = message
		notification.icon = os.path.join(files.documents(), f'Luna/resources/{files.json("Luna/notifications/toast.json", "icon", documents=True)}')
		if not audio_path == None:
			notification.audio = audio_path
		try:
			notification.send(block=False)
		except Exception as e:
			pass

	def webhook(url="", description="", name="", error=False):
		"""Create a webhook notification"""
		try:
			if url == "":
				prints.error(f"The webhook url can't be empty » {name} » Has been cleared")
				json_object = json.load(open(os.path.join(files.documents(), f"Luna/webhooks/url.json"), encoding="utf-8"))
				json_object[f"{name}"] = "webhook-url-here"
				files.write_json(os.path.join(files.documents(), f"Luna/webhooks/url.json"), json_object)
				return
			elif not "https://discord.com/api/webhooks/" in url:
				prints.error(f"Invalid webhook url » {name} » Has been cleared")
				json_object = json.load(open(os.path.join(files.documents(), f"Luna/webhooks/url.json"), encoding="utf-8"))
				json_object[f"{name}"] = "webhook-url-here"
				files.write_json(os.path.join(files.documents(), f"Luna/webhooks/url.json"), json_object)
				return
			hook = dhooks.Webhook(url=url, avatar_url=webhook.image_url())
			color = 0x000000
			if error == True:
				color = 0xE10959
			elif color == None:
				pass
			else:
				color = webhook.hex_color()
			embed = dhooks.Embed(title=webhook.title(), description=f"```{description}```", color=color)
			embed.set_thumbnail(url=webhook.image_url())
			embed.set_footer(text=webhook.footer())
			hook.send(embed=embed)
		except Exception as e:
			prints.error(e)

# ///////////////////////////////////////////////////////////////
# Config Functions

class config:
	# ///////////////////////////////////////////////////////////////
	# File overwrite (Global)

	def _global(path:str, value_holder:str, new_value, add=False, delete=False):
		"""Overwrites a value in a config file. (Global configs)"""
		json_object = json.load(open(os.path.join(files.documents(), path), encoding="utf-8"))
		if add == True:
			json_object[value_holder].append(new_value)
		elif delete == True:
			json_object[value_holder].remove(new_value)
		else:
			json_object[value_holder] = new_value
		files.write_json(os.path.join(files.documents(), path), json_object)

	# ///////////////////////////////////////////////////////////////
	# File overwrite (Config)

	def prefix(new_value):
		"""Overwrites the prefix in the config file."""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/config.json"), encoding="utf-8"))
		json_object["prefix"] = new_value
		files.write_json(os.path.join(files.documents(), f"Luna/config.json"), json_object)

	def stream_url(new_value):
		"""Overwrites the stream url in the config file."""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/config.json"), encoding="utf-8"))
		json_object["stream_url"] = new_value
		files.write_json(os.path.join(files.documents(), f"Luna/config.json"), json_object)

	def afk_message(new_value):
		"""Overwrites the afk message in the config file."""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/config.json"), encoding="utf-8"))
		json_object["afk_message"] = new_value
		files.write_json(os.path.join(files.documents(), f"Luna/config.json"), json_object)

	def delete_timer(new_value):
		"""Overwrites the delete timer in the config file."""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/config.json"), encoding="utf-8"))
		json_object["delete_timer"] = new_value
		files.write_json(os.path.join(files.documents(), f"Luna/config.json"), json_object)

	def mode(new_value):
		"""Overwrites the mode in the config file."""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/config.json"), encoding="utf-8"))
		json_object["mode"] = new_value
		files.write_json(os.path.join(files.documents(), f"Luna/config.json"), json_object)

	def error_log(new_value):
		"""Overwrites the error log in the config file."""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/config.json"), encoding="utf-8"))
		json_object["error_log"] = new_value
		files.write_json(os.path.join(files.documents(), f"Luna/config.json"), json_object)

	def risk_mode(new_value):
		"""Overwrites the risk mode in the config file."""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/config.json"), encoding="utf-8"))
		json_object["risk_mode"] = new_value
		files.write_json(os.path.join(files.documents(), f"Luna/config.json"), json_object)

	def theme(new_value):
		"""Overwrites the theme in the config file."""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/config.json"), encoding="utf-8"))
		if new_value == "default":
			json_object["theme"] = new_value
		else:
			if ".json" in new_value:
				new_value = new_value.replace('.json', '')
			json_object["theme"] = new_value + ".json"
		files.write_json(os.path.join(files.documents(), f"Luna/config.json"), json_object)

	def startup_status(new_value):
		"""Overwrites the startup status in the config file."""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/config.json"), encoding="utf-8"))
		json_object["startup_status"] = new_value
		files.write_json(os.path.join(files.documents(), f"Luna/config.json"), json_object)

	def password(new_value):
		"""Overwrites the password in the config file."""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/discord.json"), encoding="utf-8"))
		password = Encryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(new_value)
		json_object["password"] = password
		files.write_json(os.path.join(files.documents(), f"Luna/discord.json"), json_object)

	# ///////////////////////////////////////////////////////////////
	# File overwrite (Snipers)

	class nitro:

		def sniper(new_value):
			"""Overwrite the nitro sniper config"""
			json_object = json.load(open(os.path.join(files.documents(), f"Luna/snipers/nitro.json"), encoding="utf-8"))
			json_object["sniper"] = new_value
			files.write_json(os.path.join(files.documents(), f"Luna/snipers/nitro.json"), json_object)
		
	class privnote:

		def sniper(new_value):
			"""Overwrite the privnote sniper config"""
			json_object = json.load(open(os.path.join(files.documents(), f"Luna/snipers/privnote.json"), encoding="utf-8"))
			json_object["sniper"] = new_value
			files.write_json(os.path.join(files.documents(), f"Luna/snipers/privnote.json"), json_object)

	class selfbot:

		def sniper(new_value):
			"""Overwrite the selfbot sniper config"""
			json_object = json.load(open(os.path.join(files.documents(), f"Luna/snipers/selfbot.json"), encoding="utf-8"))
			json_object["sniper"] = new_value
			files.write_json(os.path.join(files.documents(), f"Luna/snipers/selfbot.json"), json_object)

	class giveaway:

		def joiner(new_value):
			"""Overwrite the giveaway joiner config"""
			json_object = json.load(open(os.path.join(files.documents(), f"Luna/snipers/giveaway.json"), encoding="utf-8"))
			json_object["joiner"] = new_value
			files.write_json(os.path.join(files.documents(), f"Luna/snipers/giveaway.json"), json_object)

		def delay_in_minutes(new_value):
			"""Overwrite the giveaway delay in minutes config"""
			json_object = json.load(open(os.path.join(files.documents(), f"Luna/snipers/giveaway.json"), encoding="utf-8"))
			json_object["delay_in_minutes"] = new_value
			files.write_json(os.path.join(files.documents(), f"Luna/snipers/giveaway.json"), json_object)

		def blocked_words(new_value):
			"""Overwrite the giveaway blocked words config"""
			json_object = json.load(open(os.path.join(files.documents(), f"Luna/snipers/giveaway.json"), encoding="utf-8"))
			json_object["blocked_words"] = new_value
			files.write_json(os.path.join(files.documents(), f"Luna/snipers/giveaway.json"), json_object)

		def guild_joiner(new_value):
			"""Overwrite the giveaway guild joiner config"""
			json_object = json.load(open(os.path.join(files.documents(), f"Luna/snipers/giveaway.json"), encoding="utf-8"))
			json_object["guild_joiner"] = new_value
			files.write_json(os.path.join(files.documents(), f"Luna/snipers/giveaway.json"), json_object)

	# ///////////////////////////////////////////////////////////////
	# File overwrite (Sharing)

	def share(new_value):
		"""Overwrite the share config"""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/sharing.json"), encoding="utf-8"))
		json_object["share"] = new_value
		files.write_json(os.path.join(files.documents(), f"Luna/sharing.json"), json_object)

	def user_id(new_value):
		"""Overwrite the user id config"""
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/sharing.json"), encoding="utf-8"))
		json_object["user_id"] = new_value
		files.write_json(os.path.join(files.documents(), f"Luna/sharing.json"), json_object)

	# ///////////////////////////////////////////////////////////////
	# File overwrite (Themes)

	def title(newtitle):
		"""Overwrite the title config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["title"] = newtitle
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)


	def title_url(newtitleurl):
		"""Overwrite the title url config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["title_url"] = newtitleurl
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)


	def footer(newfooter):
		"""Overwrite the footer config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["footer"] = newfooter
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)


	def footer_icon_url(newfooter_iconurl):
		"""Overwrite the footer icon url config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["footer_icon_url"] = newfooter_iconurl
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)


	def image_url(newimageurl):
		"""Overwrite the image url config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["image_url"] = newimageurl
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)


	def large_image_url(newlarge_imageurl):
		"""Overwrite the large image url config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["large_image_url"] = newlarge_imageurl
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)


	def hex_color(newhexcolor):
		"""Overwrite the hex color config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["hex_color"] = newhexcolor
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)


	def author(newauthor):
		"""Overwrite the author config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["author"] = newauthor
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)


	def author_icon_url(newauthor_iconurl):
		"""Overwrite the author icon url config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["author_icon_url"] = newauthor_iconurl
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)


	def author_url(newauthorurl):
		"""Overwrite the author url config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["author_url"] = newauthorurl
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)


	def description(newdescription):
		"""Overwrite the description config"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		json_object = json.load(open(os.path.join(files.documents(), f"Luna/themes/{theme}"), encoding="utf-8"))
		json_object["description"] = newdescription
		files.write_json(os.path.join(files.documents(), f"Luna/themes/{theme}"), json_object)

	# ///////////////////////////////////////////////////////////////
	# File overwrite (Toasts)

	class toast:
		# ///////////////////////////////////////////////////////////////
		# toast.json

		def icon(new_value):
			"""Overwrite the icon config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toast.json"), encoding="utf-8"))
			json_object["icon"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toast.json"), json_object)

		def title(new_value):
			"""Overwrite the title config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toast.json"), encoding="utf-8"))
			json_object["title"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toast.json"), json_object)

		# ///////////////////////////////////////////////////////////////
		# toasts.json

		def toasts(new_value):
			"""Overwrite the toasts config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["toasts"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def login(new_value):
			"""Overwrite the login config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["login"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def nitro(new_value):
			"""Overwrite the nitro config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["nitro"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def giveaway(new_value):
			"""Overwrite the giveaway config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["nitro"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def privnote(new_value):
			"""Overwrite the privnote config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["privnote"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def selfbot(new_value):
			"""Overwrite the selfbot config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["selfbot"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def pings(new_value):
			"""Overwrite the pings config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["pings"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def ghostpings(new_value):
			"""Overwrite the ghostpings config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["ghostpings"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def friendevents(new_value):
			"""Overwrite the friendevents config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["friendevents"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def guildevents(new_value):
			"""Overwrite the guildevents config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["guildevents"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def roleupdates(new_value):
			"""Overwrite the roleupdates config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["roleupdates"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def nickupdates(new_value):
			"""Overwrite the nickupdates config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["nickupdates"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

		def protection(new_value):
			"""Overwrite the protection config"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/notifications/toasts.json"), encoding="utf-8"))
			json_object["protection"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/notifications/toasts.json"), json_object)

	# ///////////////////////////////////////////////////////////////
	# File overwrite (Webhooks)

	class webhook:
		# ///////////////////////////////////////////////////////////////
		# webhook.json

		def title(new_value):
			"""Overwrite the webhook title"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhook.json"), encoding="utf-8"))
			json_object["title"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhook.json"), json_object)

		def footer(new_value):
			"""Overwrite the webhook footer"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhook.json"), encoding="utf-8"))
			json_object["footer"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhook.json"), json_object)

		def image_url(new_value):
			"""Overwrite the image url config"""
			json_object = json.load(open(os.path.join(files.documents(), f"Luna/webhooks/webhook.json"), encoding="utf-8"))
			json_object["image_url"] = new_value
			files.write_json(os.path.join(files.documents(), f"Luna/webhooks/webhook.json"), json_object)

		def hex_color(new_value):
			"""Overwrite the webhook hex color"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhook.json"), encoding="utf-8"))
			json_object["hex_color"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhook.json"), json_object)

		# ///////////////////////////////////////////////////////////////
		# webhooks.json

		def webhooks(new_value):
			"""Overwrite the webhooks webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["webhooks"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def login(new_value):
			"""Overwrite the login webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["login"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def nitro(new_value):
			"""Overwrite the nitro webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["nitro"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def giveaway(new_value):
			"""Overwrite the giveaway webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["nitro"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def privnote(new_value):
			"""Overwrite the private note webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["privnote"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def selfbot(new_value):
			"""Overwrite the selfbot webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["selfbot"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def pings(new_value):
			"""Overwrite the pings webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["pings"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def ghostpings(new_value):
			"""Overwrite the ghost pings webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["ghostpings"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def friendevents(new_value):
			"""Overwrite the friend events webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["friendevents"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def guildevents(new_value):
			"""Overwrite the guild events webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["guildevents"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def roleupdates(new_value):
			"""Overwrite the role updates webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["roleupdates"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def nickupdates(new_value):
			"""Overwrite the nick updates webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["nickupdates"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		def protection(new_value):
			"""Overwrite the protection webhook"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), encoding="utf-8"))
			json_object["protection"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/webhooks.json"), json_object)

		# ///////////////////////////////////////////////////////////////
		# url.json

		def login_url(new_value):
			"""Overwrite the login url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["login"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def nitro_url(new_value):
			"""Overwrite the nitro url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["nitro"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def giveaway_url(new_value):
			"""Overwrite the giveaway url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["giveaway"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def privnote_url(new_value):
			"""Overwrite the private note url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["privnote"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def selfbot_url(new_value):
			"""Overwrite the selfbot url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["selfbot"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def pings_url(new_value):
			"""Overwrite the pings url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["pings"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def ghostpings_url(new_value):
			"""Overwrite the ghost pings url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["ghostpings"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def friendevents_url(new_value):
			"""Overwrite the friend events url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["friendevents"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def guildevents_url(new_value):
			"""Overwrite the guild events url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["guildevents"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def roleupdates_url(new_value):
			"""Overwrite the role updates url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["roleupdates"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def nickupdates_url(new_value):
			"""Overwrite the nick updates url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["nickupdates"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

		def protection_url(new_value):
			"""Overwrite the protection url"""
			json_object = json.load(open(os.path.join(files.documents(), "Luna/webhooks/url.json"), encoding="utf-8"))
			json_object["protection"] = new_value
			files.write_json(os.path.join(files.documents(), "Luna/webhooks/url.json"), json_object)

# ///////////////////////////////////////////////////////////////
# Get values

class rpc:
	def rich_presence():
		"""Get the rich presence"""
		rich_presence = int(files.json(f"Luna/rpc.json", "rich_presence", documents=True))
		return rich_presence

	def client_id():
		"""Get the client id"""
		client_id = int(files.json(f"Luna/rpc.json", "client_id", documents=True))
		return client_id

	def state():
		"""Get the state"""
		state = str(files.json(f"Luna/rpc.json", "state", documents=True))
		return state

	def details():
		"""Get the details"""
		details = str(files.json(f"Luna/rpc.json", "details", documents=True))
		return details

	def large_image():
		"""Get the large image"""
		large_image = str(files.json(f"Luna/rpc.json", "large_image", documents=True))
		return large_image

	def large_text():
		"""Get the large image text"""
		large_image_text = str(files.json(f"Luna/rpc.json", "large_text", documents=True))
		return large_image_text

	def small_image():
		"""Get the small image"""
		small_image = str(files.json(f"Luna/rpc.json", "small_image", documents=True))
		return small_image

	def small_text():
		"""Get the small image text"""
		small_image_text = str(files.json(f"Luna/rpc.json", "small_text", documents=True))
		return small_image_text

	def button_1_text():
		"""Get the button 1 text"""
		button_1_text = str(files.json(f"Luna/rpc.json", "button_1_text", documents=True))
		return button_1_text

	def button_1_url():
		"""Get the button 1 url"""
		button_1_url = str(files.json(f"Luna/rpc.json", "button_1_url", documents=True))
		return button_1_url

	def button_2_text():
		"""Get the button 2 text"""
		button_2_text = str(files.json(f"Luna/rpc.json", "button_2_text", documents=True))
		return button_2_text

	def button_2_url():
		"""Get the button 2 url"""
		button_2_url = str(files.json(f"Luna/rpc.json", "button_2_url", documents=True))
		return button_2_url

class configs:

	def delete_timer():
		"""Get the delete timer in the config file"""
		deletetimer = int(files.json(f"Luna/config.json", "delete_timer", documents=True))
		return deletetimer

	def mode():
		"""Get the mode in the config file"""
		mode = int(files.json(f"Luna/config.json", "mode", documents=True))
		return mode

	def error_log():
		"""Get the error log in the config file"""
		error_log = files.json(f"Luna/config.json", "error_log", documents=True)
		return error_log

	def risk_mode():
		"""Get the risk mode in the config file"""
		risk_mode = files.json(f"Luna/config.json", "risk_mode", documents=True)
		return risk_mode

	def stream_url():
		"""Get the stream url in the config file"""
		stream_url = files.json(f"Luna/config.json", "stream_url", documents=True)
		return stream_url

	def startup_status():
		"""Get the startup status in the config file"""
		startup_status = files.json(f"Luna/config.json", "startup_status", documents=True)
		return startup_status

	def password():
		"""Get the password in the config file"""
		password = files.json(f"Luna/discord.json", "password", documents=True)
		password = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(password)
		return password

	def share():
		"""Get the share mode in the config file"""
		share = files.json(f"Luna/sharing.json", "share", documents=True)
		return share

	def share_id():
		"""Get the share id in the config file"""
		share_id = files.json(f"Luna/sharing.json", "user_id", documents=True)
		return share_id
    
# ///////////////////////////////////////////////////////////////
# Theme Functions

title_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["title"]
title_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["title_url"]
footer_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["footer"]
footer_icon_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["footer_icon_url"]
image_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["image_url"]
large_image_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["large_image_url"]
hexcolorvar_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["hex_color"]
author_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["author"]
author_icon_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["author_icon_url"]
author_url_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["author_url"]
descriptionvar_request = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/default.json").json()["description"]

class theme:

	def title():
		"""Get the title in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			title = title_request
		else:
			title = files.json(f"Luna/themes/{theme}", "title", documents=True)
			if title == None:
				title = ""
		return str(title)

	def title_url():
		"""Get the title url in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			title_url = title_url_request
		else:
			title_url = files.json(f"Luna/themes/{theme}", "title_url", documents=True)
			if title_url == None:
				title_url = ""
		return str(title_url)

	def footer():
		"""Get the footer in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			footer = footer_request
		else:
			footer = files.json(f"Luna/themes/{theme}", "footer", documents=True)
			if footer == None:
				footer = ""
		return str(footer)

	def footer_icon_url():
		"""Get the footer icon url in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			footer_icon_url = footer_icon_url_request
			if footer_icon_url == "$avatar":
				footer_icon_url = bot.user.avatar_url
		else:
			footer_icon_url = files.json(f"Luna/themes/{theme}", "footer_icon_url", documents=True)
			if footer_icon_url == None:
				footer_icon_url = ""
			elif footer_icon_url == "$avatar":
				footer_icon_url = bot.user.avatar_url
		return str(footer_icon_url)

	def image_url():
		"""Get the image url in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			image_url = image_url_request
			if image_url == "$avatar":
				image_url = bot.user.avatar_url
		else:
			image_url = files.json(f"Luna/themes/{theme}", "image_url", documents=True)
			if image_url == None:
				image_url = ""
			elif image_url == "$avatar":
				image_url = bot.user.avatar_url
		return str(image_url)

	def large_image_url():
		"""Get the large image url in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			large_image_url = large_image_url_request
			if large_image_url == "$avatar":
				large_image_url = bot.user.avatar_url
		else:
			large_image_url = files.json(f"Luna/themes/{theme}", "large_image_url", documents=True)
			if large_image_url == None:
				large_image_url = ""
			elif large_image_url == "$avatar":
				large_image_url = bot.user.avatar_url
		return str(large_image_url)

	def hex_color():
		"""Get the hex color in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			hexcolorvar = hexcolorvar_request
			if hexcolorvar == "":
				hexcolorvar = "#000000"
			elif hexcolorvar == "random":
				hexcolorvar = random.randint(0, 0xffffff)
			elif len(hexcolorvar) > 7:
				hexcolorvar = int(hexcolorvar)
			else:
				hexcolorvar = int(hexcolorvar.replace('#', ''), 16)
		else:
			hexcolorvar = files.json(f"Luna/themes/{theme}", "hex_color", documents=True)
			if hexcolorvar == None:
				hexcolorvar = "#000000"
			if hexcolorvar == "random":
				hexcolorvar = random.randint(0, 0xffffff)
			elif len(hexcolorvar) > 7:
				hexcolorvar = int(hexcolorvar)
			else:
				hexcolorvar = int(hexcolorvar.replace('#', ''), 16)
		return hexcolorvar

	def author():
		"""Get the author in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			author = author_request
		else:
			author = files.json(f"Luna/themes/{theme}", "author", documents=True)
			if author == None:
				author = ""
		return str(author)

	def author_icon_url():
		"""Get the author icon url in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			author_icon_url = author_icon_url_request
			if author_icon_url == "$avatar":
				author_icon_url = bot.user.avatar_url
		else:
			author_icon_url = files.json(f"Luna/themes/{theme}", "author_icon_url", documents=True)
			if author_icon_url == None:
				author_icon_url = ""
			elif author_icon_url == "$avatar":
				author_icon_url = bot.user.avatar_url
		return str(author_icon_url)

	def author_url():
		"""Get the author url in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			author_url = author_url_request
		else:
			author_url = files.json(f"Luna/themes/{theme}", "author_url", documents=True)
			if author_url == None:
				author_url = ""
		return str(author_url)

	def description():
		"""Get the description in the config file"""
		theme = files.json("Luna/config.json", "theme", documents=True)
		if theme == "default":
			descriptionvar = descriptionvar_request
			if not descriptionvar == "true":
				descriptionvar = ""
			else:
				descriptionvar = "```<> is required | [] is optional\n\n```"
		else:
			descriptionvar = files.json(f"Luna/themes/{theme}", "description", documents=True)
			if descriptionvar == None:
				descriptionvar = True
			if not descriptionvar:
				descriptionvar = ""
			else:
				descriptionvar = "```<> is required | [] is optional\n\n```"
		return str(descriptionvar)

class webhook:

	def title():
		"""Get the title in the config file"""
		title = files.json("Luna/webhooks/webhook.json", "title", documents=True)
		if title == None:
			title = ""
		return str(title)

	def footer():
		"""Get the title in the config file"""
		footer = files.json("Luna/webhooks/webhook.json", "footer", documents=True)
		if footer == None:
			footer = ""
		return str(footer)

	def image_url():
		"""Get the image url in the config file"""
		image_url = files.json("Luna/webhooks/webhook.json", "image_url", documents=True)
		if image_url == None:
			image_url = ""
		elif image_url == "$avatar":
			image_url = bot.user.avatar_url
		return str(image_url)

	def hex_color():
		"""Get the hex color in the config file"""
		hexcolorvar = files.json("Luna/webhooks/webhook.json", "hex_color", documents=True)
		if hexcolorvar == None:
			hexcolorvar = "#000000"
		if hexcolorvar == "random":
			hexcolorvar = random.randint(0, 0xffffff)
		elif len(hexcolorvar) > 7:
			hexcolorvar = int(hexcolorvar)
		else:
			hexcolorvar = int(hexcolorvar.replace('#', ''), 16)
		return hexcolorvar

	def login_url():
		"""Get the login webhook url in the config file"""
		login_url = files.json("Luna/webhooks/url.json", "login", documents=True)
		return str(login_url)

	def nitro_url():
		"""Get the nitro webhook url in the config file"""
		nitro_url = files.json("Luna/webhooks/url.json", "nitro", documents=True)
		return str(nitro_url)

	def giveaway_url():
		"""Get the giveaway webhook url in the config file"""
		giveaway_url = files.json("Luna/webhooks/url.json", "giveaway", documents=True)
		return str(giveaway_url)

	def privnote_url():
		"""Get the privnote webhook url in the config file"""
		privnote_url = files.json("Luna/webhooks/url.json", "privnote", documents=True)
		return str(privnote_url)

	def selfbot_url():
		"""Get the selfbot webhook url in the config file"""
		selfbot_url = files.json("Luna/webhooks/url.json", "selfbot", documents=True)
		return str(selfbot_url)

	def pings_url():
		"""Get the pings webhook url in the config file"""
		pings_url = files.json("Luna/webhooks/url.json", "pings", documents=True)
		return str(pings_url)

	def ghostpings_url():
		"""Get the ghostpings webhook url in the config file"""
		ghostpings_url = files.json("Luna/webhooks/url.json", "ghostpings", documents=True)
		return str(ghostpings_url)

	def friendevents_url():
		"""Get the friendevents webhook url in the config file"""
		friendevents_url = files.json("Luna/webhooks/url.json", "friendevents", documents=True)
		return str(friendevents_url)

	def guildevents_url():
		"""Get the guildevents webhook url in the config file"""
		guildevents_url = files.json("Luna/webhooks/url.json", "guildevents", documents=True)
		return str(guildevents_url)

	def roleupdates_url():
		"""Get the roleupdates webhook url in the config file"""
		roleupdates_url = files.json("Luna/webhooks/url.json", "roleupdates", documents=True)
		return str(roleupdates_url)

	def nickupdates_url():
		"""Get the nickupdates webhook url in the config file"""
		nickupdates_url = files.json("Luna/webhooks/url.json", "nickupdates", documents=True)
		return str(nickupdates_url)

	def protections_url():
		"""Get the protections webhook url in the config file"""
		protections_url = files.json("Luna/webhooks/url.json", "protections", documents=True)
		return str(protections_url)
	

# ///////////////////////////////////////////////////////////////
# ON_READY

def bot_prefix(bot, message):
	"""Get the prefix in the config file"""
	prefix = files.json("Luna/config.json", "prefix", documents=True)
	return prefix

def statuscon():
	startup_status = configs.startup_status()
	if startup_status == "dnd":
		statuscon = Status.dnd
	elif startup_status == "idle":
		statuscon = Status.idle
	elif startup_status == "invisible" or startup_status == "offline":
		statuscon = Status.offline
	else:
		statuscon = Status.online
	return statuscon

def uptime_thread():
	global hour
	global minute
	global second
	hour = 0
	minute = 0
	second = 0
	while True:
		luna.title(f"Luna {version_url} | {hour:02d}:{minute:02d}:{second:02d}")
		time.sleep(1)
		second += 1
		if second == 60:
			minute += 1
			second = 0
		if minute == 60:
			hour += 1
			minute = 00
		if hour == 24:
			hour = 0
			minute = 0
			second = 0

def update_thread():
	update_found = False
	while True:
		r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
		version_url = r["version"]

		r = requests.get("https://raw.githubusercontent.com/Nshout/Luna/main/beta.json").json()
		beta_version_url = r["version"]

		if beta:
			version_url = beta_version_url
		if developer_mode:
			pass
		elif version == version_url:
			pass
		else:
			if files.json("Luna/notifications/toasts.json", "login", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
				notify.toast(message=f"Starting update {version_url}")
			if files.json("Luna/webhooks/webhooks.json", "login", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.login_url() == "webhook-url-here":
				notify.webhook(url=webhook.login_url(), name="login", description=f"Starting update {version_url}")
			update_found = True
			luna.update()
		if not update_found:
			time.sleep(900)

bot = commands.Bot(bot_prefix, self_bot=True, case_insensitive=True, guild_subscription_options=GuildSubscriptionOptions.off(), status=statuscon())
@bot.event
async def on_ready():
	"""Prints a ready log."""
	if files.json("Luna/notifications/toasts.json", "login", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
		notify.toast(message=f"Logged into {bot.user}\nLuna Version » {version}")
	if files.json("Luna/webhooks/webhooks.json", "login", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.login_url() == "webhook-url-here":
		notify.webhook(url=webhook.login_url(), name="login", description=f"Logged into {bot.user}")

	luna.console(clear=True)
	command_count = len(bot.commands)
	cog = bot.get_cog('Custom commands')
	try:
		custom = cog.get_commands()
		custom_command_count = 0
		for command in custom:
			custom_command_count += 1
	except:
		custom_command_count = 0
	print(motd.center(os.get_terminal_size().columns))
	if beta:
		print("Beta Build".center(os.get_terminal_size().columns))
		bot_id = str(bot.user.id)
		if not bot_id in beta_user:
			prints.message("You are not a beta user, Luna will close in 5 seconds.")
			time.sleep(5)
			os._exit(0)
	prefix = files.json("Luna/config.json", "prefix", documents=True)
	console_mode = files.json("Luna/console/console.json", "mode", documents=True)
	if console_mode == "2":
		mode = int(files.json("Luna/config.json", "mode", documents=True))
		errorlog = files.json("Luna/config.json", "error_log", documents=True)
		riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
		themesvar = files.json("Luna/config.json", "theme", documents=True)
		deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
		startup_status = files.json("Luna/config.json", "startup_status", documents=True)
		nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
		giveawayjoiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
		delay_in_minutes = int(files.json("Luna/snipers/giveaway.json", "delay_in_minutes", documents=True))
		giveaway_server_joiner = files.json("Luna/snipers/giveaway.json", "guild_joiner", documents=True)
		if mode == 1:
			mode = "Embed"
		elif mode == 2:
			mode = "Text"
		elif mode == 3:
			mode = "Indent"
		else:
			mode = "Unknown"
		if afkstatus == 1:
			afk = "on"
		else:
			afk = "off"
		if themesvar == "default":
			pass
		else:
			themesvar = themesvar[:-5]
		bot_user = f"{bot.user}"
		ui_user = f" {color.purple('User:')} {bot_user:<26}"
		ui_guilds = f" {color.purple('Guilds:')} {len(bot.guilds):<24}"
		ui_friends = f" {color.purple('Friends:')} {len(bot.user.friends):<23}"
		ui_prefix = f" {color.purple('Prefix:')} {prefix:<24}"
		ui_mode = f" {color.purple('Mode:')} {mode:<26}"
		ui_theme = f" {color.purple('Theme:')} {themesvar:<25}"
		ui_commands = f" {color.purple('Commands:')} {command_count-custom_command_count:<22}"
		ui_commands_custom = f" {color.purple('Custom Commands:')} {custom_command_count:<15}"
		ui_nitro_sniper = f" {color.purple('Nitro Sniper:')} {nitro_sniper}"
		ui_giveaway_sniper = f" {color.purple('Giveaway Joiner:')} {giveawayjoiner}"
		ui_giveaway_delay = f" {color.purple('Giveaway Delay:')} {delay_in_minutes}"
		ui_giveaway_joiner = f" {color.purple('Giveaway Guilds:')} {giveaway_server_joiner}"
		ui_afk = f" {color.purple('AFK Messager:')} {afk}"
		ui_riskmode = f" {color.purple('Riskmode:')} {riskmode}"
		ui_errorlog = f" {color.purple('Errorlog:')} {errorlog}"
		ui_deletetimer = f" {color.purple('Delete Timer:')} {deletetimer}"
		ui_startup = f" {color.purple('Startup Status:')} {startup_status}"
		print()
		print(f"               ═════════════ {color.purple('User')} ═════════════      ═══════════ {color.purple('Settings')} ═══════════")
		print(f"               {ui_user}     {ui_prefix}")
		print(f"               {ui_guilds}     {ui_theme}")
		print(f"               {ui_friends}     {ui_nitro_sniper}")
		print(f"               ════════════════════════════════      {ui_giveaway_sniper}")
		print(f"               ═════════════ {color.purple('Luna')} ═════════════      {ui_riskmode}")
		print(f"               {ui_commands}     {ui_deletetimer}")
		print(f"               {ui_commands_custom}     {ui_startup}")
		print(f"               ════════════════════════════════      ════════════════════════════════\n")
	else:
		print()
		print(f"                           {color.purple('[')}+{color.purple('] CONNECTED')}")
		print(f"                           {color.purple('[')}+{color.purple(']')} {bot.user} | {color.purple(f'{len(bot.guilds)}')} Guilds | {color.purple(f'{len(bot.user.friends)}')} Friends")
		print(f"                           {color.purple('[')}+{color.purple(']')} {prefix}\n")
	print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
	prints.message(f"{color.purple(f'{command_count-custom_command_count}')} commands | {color.purple(f'{custom_command_count}')} custom commands")
	debugger_thread = threading.Thread(target=uptime_thread)
	debugger_thread.daemon = True
	debugger_thread.start()
	debugger_thread = threading.Thread(target=update_thread)
	debugger_thread.daemon = True
	debugger_thread.start()

# ///////////////////////////////////////////////////////////////
# Rest

# ///////////////////////////////////////////////////////////////
# On Message Event

class OnMessage(commands.Cog, name="on message"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
		
	@commands.Cog.listener()
	async def on_message(self, message):
		sniped_start_time = time.time()
		if message.author == self.bot.user:
			return
		try:
			global nitro_cooldown
			if files.json("Luna/snipers/nitro.json", "sniper", documents=True) == "on" and 'discord.gift/' in message.content.lower():
				elapsed_snipe = '%.4fs' % (time.time() - sniped_start_time)
				code = re.search("discord.gift/(.*)", message.content).group(1)
				if len(code) >= 16:
					async with httpx.AsyncClient() as client:
						start_time = time.time()
						result = await client.post(f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
						elapsed = '%.3fs' % (time.time() - start_time)
					if 'nitro' in str(result.content):
						status = 'Nitro successfully redeemed'
					elif 'This gift has been redeemed already' in str(result.content):
						status = 'Has been redeemed already'
					else:
						status = 'Unknown gift code'

					if nitro_cooldown.count(code) == 0:
						nitro_cooldown.append(code)
						
						print()
						prints.sniper(color.purple(status))
						prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
						prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
						prints.sniper(f"Author  | {color.purple(f'{message.author}')}")
						prints.sniper(f"Code    | {color.purple(f'{code}')}")
						prints.sniper(color.purple('Elapsed Times'))
						prints.sniper(f"Sniped  | {color.purple(f'{elapsed_snipe}')}")
						prints.sniper(f"Request | {color.purple(f'{elapsed}')}")
						print()

						if files.json("Luna/notifications/toasts.json", "nitro", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
							notify.toast(message=f"{status}\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
						if files.json("Luna/webhooks/webhooks.json", "nitro", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.nitro_url() == "webhook-url-here":
							notify.webhook(url=webhook.nitro_url(), name="nitro", description=f"{status}\nServer » {message.guild}\nChannel » {message.channel}\nAuthor » {message.author}\nCode » {code}\nElapsed Times\nSniped » {elapsed_snipe}\nRequest » {elapsed}")
			
			elif files.json("Luna/snipers/nitro.json", "sniper", documents=True) == "on" and 'discord.com/gifts' in message.content.lower():
				elapsed_snipe = '%.4fs' % (time.time() - sniped_start_time)
				code = re.search("discord.com/gifts/(.*)", message.content).group(1)
				if len(code) >= 16:
					async with httpx.AsyncClient() as client:
						start_time = time.time()
						result = await client.post(f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem', json={'channel_id': message.channel.id}, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
						elapsed = '%.3fs' % (time.time() - start_time)
					if 'nitro' in str(result.content):
						status = 'Nitro successfully redeemed'
					elif 'This gift has been redeemed already' in str(result.content):
						status = 'Has been redeemed already'
					else:
						status = 'Unknown gift code'

					if nitro_cooldown.count(code) == 0:
						nitro_cooldown.append(code)
						
						print()
						prints.sniper(color.purple(status))
						prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
						prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
						prints.sniper(f"Author  | {color.purple(f'{message.author}')}")
						prints.sniper(f"Code    | {color.purple(f'{code}')}")
						prints.sniper(color.purple('Elapsed Times'))
						prints.sniper(f"Sniped  | {color.purple(f'{elapsed_snipe}')}")
						prints.sniper(f"Request | {color.purple(f'{elapsed}')}")
						print()

						if files.json("Luna/notifications/toasts.json", "nitro", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
							notify.toast(message=f"{status}\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
						if files.json("Luna/webhooks/webhooks.json", "nitro", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.nitro_url() == "webhook-url-here":
							notify.webhook(url=webhook.nitro_url(), name="nitro", description=f"{status}\nServer » {message.guild}\nChannel » {message.channel}\nAuthor » {message.author}\nCode » {code}\nElapsed Times\nSniped » {elapsed_snipe}\nRequest » {elapsed}")
		except Exception as e:
			prints.error(e)
			
		giveaway_joiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
		delay_in_minutes = int(files.json("Luna/snipers/giveaway.json", "delay_in_minutes", documents=True))
		giveaway_blocked_words = files.json("Luna/snipers/giveaway.json", "blocked_words", documents=True)
		guild_joiner = files.json("Luna/snipers/giveaway.json", "guild_joiner", documents=True)
		if giveaway_joiner == "on" and message.author.bot and not message.guild is None and not isinstance(message.channel, discord.GroupChannel):
			elapsed_snipe = '%.3fs' % (time.time() - sniped_start_time)
			custom_giveaway_bot_ids = []
			custom_giveaway_bot_reactions = []
			try:
				if os.path.exists(os.path.join(files.documents(), f"Luna/snipers/giveaway_bots.json")):
					with open(os.path.join(files.documents(), f"Luna/snipers/giveaway_bots.json"), "r", encoding="utf-8") as jsonFile:
						data = json.load(jsonFile)
							
					for key, value in data.items():
						try:
							custom_giveaway_bot_ids.append(int(key))
							custom_giveaway_bot_reactions.append(str(value))
						except Exception:
							pass
			except Exception:
				pass
			embeds = message.embeds
			for embed in embeds:
				if ((("giveaway" in str(message.content).lower()) and (int(message.author.id) in custom_giveaway_bot_ids) and ("cancelled" not in str(message.content).lower()) and ("mention" not in str(message.content).lower()) and ("specify" not in str(message.content).lower()) and ("congratulations" not in str(message.content).lower())) and embed is not None):
					found_something_blacklisted = 0
					for blocked_word in giveaway_blocked_words:
						if str(blocked_word).lower() in str(message.content).lower():
							print()
							prints.sniper(f"{color.purple('Skipped giveaway')}")
							prints.sniper(f"Reason  | Backlisted word » {color.purple(f'{blocked_word}')}")
							prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
							prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
							print()
							if files.json("Luna/notifications/toasts.json", "giveaway", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
								notify.toast(message=f"Skipped giveaway\nReason » {blocked_word}\nServer »  {message.guild}\nChannel » {message.channel}")
							if files.json("Luna/webhooks/webhooks.json", "giveaway", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.giveaway_url() == "webhook-url-here":
								notify.webhook(url=webhook.giveaway_url(), name="giveaway", description=f"Skipped giveaway\nReason » {blocked_word}\nServer »  {message.guild}\nChannel » {message.channel}")
							found_something_blacklisted = 1
					try:
						for embed in message.embeds:
							embed_dict = embed.to_dict()
							for blocked_word in giveaway_blocked_words:
								try:
									found = re.findall(blocked_word, str(embed_dict).lower())[0]
									if found:
										print()
										prints.sniper(f"{color.purple('Skipped giveaway')}")
										prints.sniper(f"Reason  | Backlisted word » {color.purple(f'{blocked_word}')}")
										prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
										prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
										print()
										if files.json("Luna/notifications/toasts.json", "giveaway", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
											notify.toast(message=f"Skipped giveaway\nReason » {blocked_word}\nServer »  {message.guild}\nChannel » {message.channel}")
										if files.json("Luna/webhooks/webhooks.json", "giveaway", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.giveaway_url() == "webhook-url-here":
											notify.webhook(url=webhook.giveaway_url(), name="giveaway", description=f"Skipped giveaway\nReason » {blocked_word}\nServer »  {message.guild}\nChannel » {message.channel}")
										found_something_blacklisted = 1
										break
								except:
									pass
											
								if found_something_blacklisted > 0:
									break
					except:
						pass
							
					if found_something_blacklisted == 0:
						try:
							embeds = message.embeds
							joined_server = 'None'
							giveaway_prize = None
							try:
								for embed in embeds:
									giveaway_prize = embed.to_dict()['author']['name']
							except Exception:
								for embed in embeds:
									giveaway_prize = embed.to_dict()['title']
							if guild_joiner == "on":
								try:
									for embed in embeds:
										embed_dict = embed.to_dict()
										code = re.findall(r"\w[a-z]*\W*\w[a-z]+\.\w[g]*\W\S*", str(embed_dict['description']))[0].replace(")", "").replace("https://discord.gg/", "")
										async with httpx.AsyncClient() as client:
											await client.post(f'https://canary.discord.com/api/v8/invites/{code}', headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
											joined_server = f'discord.gg/{code}'
											await asyncio.sleep(5)
								except Exception:
									pass
							else:
								pass
							print()
							prints.sniper(f"{color.purple('Giveaway found')}")
							prints.sniper(f"Prize   | {color.purple(f'{giveaway_prize}')}")
							prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
							prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
							prints.sniper(f"Joining | {color.purple(f'In {delay_in_minutes} minute/s')}")
							prints.sniper(f"Invite  | {color.purple(f'Joined guild » {joined_server}')}")
							print()
							if files.json("Luna/notifications/toasts.json", "giveaway", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
								notify.toast(message=f"Giveaway found\nPrize » {giveaway_prize}\nServer »  {message.guild}\nChannel » {message.channel}")
							if files.json("Luna/webhooks/webhooks.json", "giveaway", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.giveaway_url() == "webhook-url-here":
								notify.webhook(url=webhook.giveaway_url(), name="giveaway", description=f"Giveaway found\nPrize » {giveaway_prize}\nServer »  {message.guild}\nChannel » {message.channel}")
						except Exception as e:
							prints.error(e)
							return
								
						await asyncio.sleep(delay_in_minutes * 60)

						try:
							if int(message.author.id) in custom_giveaway_bot_ids:
								index = custom_giveaway_bot_ids.index(int(message.author.id))
								try:
									await message.add_reaction(custom_giveaway_bot_reactions[index])
								except Exception as e:
									prints.error(e)
									return
								print()
								prints.sniper(f"{color.purple('Joined giveaway')}")
								prints.sniper(f"Prize   | {color.purple(f'{giveaway_prize}')}")
								prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
								prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
								print()
								if files.json("Luna/notifications/toasts.json", "giveaway", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
									notify.toast(message=f"Joined giveaway\nPrize » {giveaway_prize}\nServer »  {message.guild}\nChannel » {message.channel}")
								if files.json("Luna/webhooks/webhooks.json", "giveaway", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.giveaway_url() == "webhook-url-here":
									notify.webhook(url=webhook.giveaway_url(), name="giveaway", description=f"Joined giveaway\nPrize » {giveaway_prize}\nServer »  {message.guild}\nChannel » {message.channel}")
						except Exception:
							pass

				if '<@' + str(bot.user.id) + '>' in message.content and ('giveaway' in str(message.content).lower() or ' won ' in message.content or ' winner ' in str(message.content).lower()) and message.author.bot and message.author.id in custom_giveaway_bot_ids:
					print()
					prints.sniper(f"{color.purple('Won giveaway')}")
					prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
					prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
					print()
					if files.json("Luna/notifications/toasts.json", "giveaway", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
						notify.toast(message=f"Won giveaway\nServer »  {message.guild}\nChannel » {message.channel}")
					if files.json("Luna/webhooks/webhooks.json", "giveaway", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.giveaway_url() == "webhook-url-here":
						notify.webhook(url=webhook.giveaway_url(), name="giveaway", description=f"Won giveaway\nServer »  {message.guild}\nChannel » {message.channel}")
			if giveaway_joiner == "on" and message.author.bot:
				if "joining" in str(message.content).lower() and guild_joiner == "on":
					try:
						for embed in embeds:
							embed_dict = embed.to_dict()
							code = re.findall(r"\w[a-z]*\W*\w[a-z]+\.\w[g]*\W\S*", str(message.content).replace(")", "").replace("https://discord.gg/", ""))
							async with httpx.AsyncClient() as client:
								await client.post(f'https://canary.discord.com/api/v9/invites/{code}', headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
								joined_server = f'discord.gg/{code}'
								if files.json("Luna/notifications/toasts.json", "giveaway", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
									notify.toast(message=f"Joined guild\nInvite » discord.gg/{code}")
								if files.json("Luna/webhooks/webhooks.json", "giveaway", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.giveaway_url() == "webhook-url-here":
									notify.webhook(url=webhook.giveaway_url(), name="giveaway", description=f"Joined guild\nInvite » discord.gg/{code}")
								await asyncio.sleep(5)
					except Exception:
						pass
				else:
					pass
		#///////////////////////////////////////////////////////////////
		# Copy Member

		if copycat is not None and copycat.id == message.author.id:
			await message.channel.send(chr(173) + message.content)

		# ///////////////////////////////////////////////////////////////
		# Share command
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		share = files.json(f"Luna/sharing.json", "share", documents=True)
		user_id = files.json(f"Luna/sharing.json", "user_id", documents=True)

		if share == "on":
			if message.author.id == user_id:
				if f"{prefix}help" in message.content.lower():
					prints.shared("help")
					if configs.mode() == 2:
						sent = await message.channel.send(f"```ini\n[ {theme.title()} ]\n\n{theme.description()}Coming soon\n\n[ {theme.footer()} ]```")
						await asyncio.sleep(configs.delete_timer())
						await sent.delete()
					if configs.mode() == 3:
						sent = await message.channel.send(f"```ini\n[ {theme.title()} ]\n\n{theme.description()}Coming soon\n\n[ {theme.footer()} ]```")
						await asyncio.sleep(configs.delete_timer())
						await sent.delete()
					else:
						embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"{theme.description()}```\nComing soon```", color=theme.hex_color())
						embed.set_thumbnail(url=theme.image_url())
						embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
						embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
						embed.set_image(url=theme.large_image_url())
						sent = await message.channel.send(embed=embed)
						await asyncio.sleep(configs.delete_timer())
						await sent.delete()
			else:
				pass

		# ///////////////////////////////////////////////////////////////
		# AFK System

		global afkstatus
		global afk_user_id
		global afk_reset

		if afkstatus == 1 and afk_user_id == 0:

			with open("config.json", "r") as f:
				config = json.load(f)
				afkmessage = config.get('afkmessage')
				if afkmessage == "":
					afkmessage = "This is an autoresponse message! User is now AFK.."
			if message.guild is None and not isinstance(message.channel, discord.GroupChannel):
				if message.author == self.bot.user:
					return
					
				if configs.mode() == 2:
					sent = await message.channel.send(f"```ini\n[ AFK ]\n\n{afkmessage}\n\n[ {theme.footer()} ]```")
				else:
					embed = discord.Embed(title="AFK", url=theme.title_url(), description=f"```\n{afkmessage}```", color=theme.hex_color())
					embed.set_thumbnail(url=theme.image_url())
					embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
					embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
					embed.set_image(url=theme.large_image_url())
					sent = await message.channel.send(embed=embed)

				afk_user_id = message.author.id
				await asyncio.sleep(60)
				afk_user_id = 0
				await sent.delete()

		# ///////////////////////////////////////////////////////////////
		# Mention

		if f'<@{self.bot.user.id}>' in message.content or f'<@!{self.bot.user.id}>' in message.content.lower():
			if files.json("Luna/notifications/toasts.json", "pings", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
				notify.toast(message=f"You have been mentioned\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
			if files.json("Luna/webhooks/webhooks.json", "pings", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.pings_url() == "webhook-url-here":
				notify.webhook(url=webhook.pings_url(), name="pings", description=f"You have been mentioned\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
			if files.json("Luna/notifications/console.json", "pings", documents=True) == "on":
				print()
				prints.sniper(f"{color.purple('You have been mentioned')}")
				prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
				prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
				prints.sniper(f"Author  | {color.purple(f'{message.author}')}")
				print()
			
		#///////////////////////////////////////////////////////////////
		# Selfbot Detection - Embed

		if message.author.bot == False:
			if message.author == self.bot.user:
				pass
			else:
				embeds = message.embeds
				for embed in embeds:
					global cooldown
					if embed is not None and cooldown.count(message.author.id) == 0 and not ("https://" or "http://" or "cdn.discordapp.com" or ".png" or ".gif" or "www.") in message.content.lower():
						cooldown.append(message.author.id)
						if files.json("Luna/snipers/selfbot.json", "sniper", documents=True) == "on":
							if files.json("Luna/notifications/toasts.json", "selfbot", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
								notify.toast(message=f"Selfbot Detected\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
							if files.json("Luna/webhooks/webhooks.json", "selfbot", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.selfbot_url() == "webhook-url-here":
								notify.webhook(url=webhook.selfbot_url(), name="selfbot", description=f"Selfbot Detected\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
							print()
							prints.sniper(f"{color.purple('Selfbot Detected')}")
							prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
							prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
							prints.sniper(f"Author  | {color.purple(f'{message.author}')}")
							try:
								title = embed.to_dict()['title']
								title = title.lower()
								if "nighty" in title:
									prints.sniper(f"Selfbot | Prediction » {color.purple('Nighty')}")
								elif "aries" in title:
									prints.sniper(f"Selfbot | Prediction » {color.purple('Aries')}")
								elif "solus" in title:
									prints.sniper(f"Selfbot | Prediction » {color.purple('Solus')}")
								elif "ghost" in title:
									prints.sniper(f"Selfbot | Prediction » {color.purple('Ghost')}")
								elif "okuru" in title:
									prints.sniper(f"Selfbot | Prediction » {color.purple('Okuru')}")
								elif "lucifer" in title:
									prints.sniper(f"Selfbot | Prediction » {color.purple('Lucifer')}")
							except:
								pass
							print()
							await asyncio.sleep(3600)
							cooldown.remove(message.author.id)
						else:
							pass
					else:
						pass

		#///////////////////////////////////////////////////////////////
		# Privnote Sniper

		if 'privnote.com' in message.content.lower():
			elapsed_snipe = '%.3fs' % (time.time() - sniped_start_time)
			privnote_sniper = files.json(f"Luna/snipers/privnote.json", "sniper", documents=True)
			if privnote_sniper == "on":
				code = re.search('privnote.com/(.*)', message.content).group(1)
				link = 'https://privnote.com/' + code
				try:
					start_time = time.time()
					note_text = pn.read_note(link)
					elapsed = '%.3fs' % (time.time() - start_time)
					with open(os.path.join(files.documents(), f"Luna/privnote/{code}.txt"), 'a+') as f:
						print()
						prints.sniper(color.purple('Privnote sniped'))
						prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
						prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
						prints.sniper(f"Author  | {color.purple(f'{message.author}')}")
						prints.sniper(f"Link    | {color.purple(f'{link}')}")
						prints.sniper(f"Code    | {color.purple(f'{code}')}")
						prints.sniper(color.purple('Elapsed Times'))
						prints.sniper(f"Sniped  | {color.purple(f'{elapsed_snipe}')}")
						prints.sniper(f"Read    | {color.purple(f'{elapsed}')}")
						print()
						file = open(os.path.join(files.documents(), f"Luna/privnote/{code}.txt"), "w")
						file.write(str(note_text))
						file.close()
				except Exception:
					print()
					prints.sniper(color.purple('Privnote already sniped'))
					prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
					prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
					prints.sniper(f"Author  | {color.purple(f'{message.author}')}")
					prints.sniper(f"Link    | {color.purple(f'{link}')}")
					prints.sniper(f"Code    | {color.purple(f'{code}')}")
					prints.sniper(color.purple('Elapsed Times'))
					prints.sniper(f"Sniped  | {color.purple(f'{elapsed_snipe}')}")
					print()
			else:
				return

		#///////////////////////////////////////////////////////////////
		# Anti-Invite
		if 'discord.gg/' in message.content.lower() and antiinvite == True:
			guilds = files.json("Luna/protections/config.json", "guilds", documents=True)
			if message.guild.id in guilds:
				try:
					await message.delete()
				except:
					pass
				try:
					if configs.mode() == 1:
						embed = discord.Embed(title="Anti Invite", url=theme.title_url(), description="```\n\"Anti Invite\" is enabled, sending Discord invites is not allowed.```", color=theme.hex_color())
						embed.set_thumbnail(url=theme.image_url())
						embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
						embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
						embed.set_image(url=theme.large_image_url())
						sent = await message.channel.send(embed=embed)
					else:
						sent = await message.channel.send(f"```ini\n[ Anti Invite ]\n\n\"Anti Invite\" is enabled, sending Discord invites is not allowed.\n\n[ {theme.footer()} ]```")
					await asyncio.sleep(30)
					await sent.delete()
				except:
					pass

		#///////////////////////////////////////////////////////////////
		# Anti-Upper
		if message.content.isupper() and antiupper == True:
			guilds = files.json("Luna/protections/config.json", "guilds", documents=True)
			if message.guild.id in guilds:
				try:
					await message.delete()
				except:
					pass
				try:
					if configs.mode() == 1:
						embed = discord.Embed(title="Anti Upper", url=theme.title_url(), description="```\n\"Anti Upper\" is enabled, sending all uppercase is not allowed.```", color=theme.hex_color())
						embed.set_thumbnail(url=theme.image_url())
						embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
						embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
						embed.set_image(url=theme.large_image_url())
						sent = await message.channel.send(embed=embed)
					else:
						sent = await message.channel.send(f"```ini\n[ Anti Upper ]\n\n\"Anti Upper\" is enabled, sending all uppercase is not allowed.\n\n[ {theme.footer()} ]```")
				except:
					pass

		#///////////////////////////////////////////////////////////////
		# Anti-Phishing
		if message.content in phishing_list and antiphishing == True:
			guilds = files.json("Luna/protections/config.json", "guilds", documents=True)
			if message.guild.id in guilds:
				try:
					await message.delete()
				except:
					pass
				try:
					if configs.mode() == 1:
						embed = discord.Embed(title="Anti Phishing Links", url=theme.title_url(), description="```\n\"Anti Phishing Links\" is enabled, the url you sent, is banned.```", color=theme.hex_color())
						embed.set_thumbnail(url=theme.image_url())
						embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
						embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
						embed.set_image(url=theme.large_image_url())
						sent = await message.channel.send(embed=embed)
					else:
						sent = await message.channel.send(f"```ini\n[ Anti Phishing Links ]\n\n\"Anti Phishing Links\" is enabled, the url you sent, is banned.\n\n[ {theme.footer()} ]```")
				except:
					pass

bot.add_cog(OnMessage(bot))

# ///////////////////////////////////////////////////////////////
# On Message Delete Event

class OnDelete(commands.Cog, name="on delete"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
		
	@commands.Cog.listener()
	async def on_message_delete(self, message):
		if message.author == self.bot.user:
			pass
		else:
			mention = f'<@!{self.bot.user.id}>'
			if mention in message.content:
				if files.json("Luna/notifications/toasts.json", "ghostpings", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
					notify.toast(message=f"You have been ghostpinged\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
				if files.json("Luna/webhooks/webhooks.json", "ghostpings", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.ghostpings_url() == "webhook-url-here":
					notify.webhook(url=webhook.ghostpings_url(), name="ghostpings", description=f"You have been ghostpinged\nServer »  {message.guild}\nChannel » {message.channel}\nAuthor »  {message.author}")
				print()
				prints.sniper(f"{color.purple('You have been ghostpinged')}")
				prints.sniper(f"Server  | {color.purple(f'{message.guild}')}")
				prints.sniper(f"Channel | {color.purple(f'{message.channel}')}")
				prints.sniper(f"Author  | {color.purple(f'{message.author}')}")
				print()

bot.add_cog(OnDelete(bot))

# ///////////////////////////////////////////////////////////////
# On Typing Event

class OnTyping(commands.Cog, name="on typing"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener() 
	async def on_typing(self, channel, member, when):
		if member in self.bot.user.friends and isinstance(channel, discord.DMChannel):
			if files.json("Luna/notifications/toasts.json", "friendevents", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
				notify.toast(message=f"{member} is typing")
			if files.json("Luna/webhooks/webhooks.json", "friendevents", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.friendevents_url() == "webhook-url-here":
				notify.webhook(url=webhook.friendevents_url(), name="friendevents", description=f"{member} is typing")

bot.add_cog(OnTyping(bot))

# ///////////////////////////////////////////////////////////////
# On Command Event

last_used = ""

class OnCommand(commands.Cog, name="on command"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
		
	@commands.Cog.listener()
	async def on_command(self, luna:commands.Context):
		global last_used
		if not luna.command.name == "repeat":
			last_used = luna.command.name
		prints.command(luna.command.name)
		theme_json = files.json("Luna/config.json", "theme", documents=True)
		try:
			if theme_json == "default":
				pass
			else:
				files.json(f"Luna/themes/{theme_json}", "title", documents=True)
		except:
			config.theme("default")
			await error_builder(luna, description=f"```\nThe configurated theme file was missing and has been set to \"default\"```")
		return
				

bot.add_cog(OnCommand(bot))

# ///////////////////////////////////////////////////////////////
# On Command Error

class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_command_error(self, luna:commands.Context, error:commands.CommandError):
		error_str = str(error)
		error = getattr(error, 'original', error)
		if isinstance(error, commands.CommandOnCooldown):
			try:
				await luna.message.delete()
			except:
				pass
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			if day > 0:
				if configs.error_log() == "console":
					prints.error('This command is on cooldown, for '+str(day)+ "day(s)")
				else:
					await luna.send('This command is on cooldown, for '+str(day)+ "day(s)", delete_after=3)
			elif hour > 0:
				if configs.error_log() == "console":
					prints.error('This command is on cooldown, for '+str(hour)+ " hour(s)")
				else:
					await luna.send('This command is on cooldown, for '+str(hour)+ " hour(s)", delete_after=3)
			elif minute > 0:
				if configs.error_log() == "console":
					prints.error('This command is on cooldown, for '+ str(minute)+" minute(s)")
				else:
					await luna.send('This command is on cooldown, for '+ str(minute)+" minute(s)", delete_after=3)
			else:
				if configs.error_log() == "console":
					prints.error(f'You are being ratelimited, for {error.retry_after:.2f} second(s)')
				else:
					await luna.send(f'You are being ratelimited, for {error.retry_after:.2f} second(s)', delete_after=3)

		if isinstance(error, CommandNotFound):
			try:
				await luna.message.delete()
			except:
				pass
			prefix = files.json("Luna/config.json", "prefix", documents=True)
			helptext = ""
			amount = 0
			for command in self.bot.commands:
				helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description},"

			error_text = f"{error}"
			subtract = len(error_text)-14
			error_strip = error_text[9:subtract]
			commandlist = helptext.split(",")
			# commandlistfind = [ string for string in commandlist if error_strip in string]
			for string in commandlist:
				if amount < 5:
					if error_strip in string:
						commandlistfind = [string]
						amount += 1
				else:
					pass
			try:
				commandlistfind = '\n'.join(str(e) for e in commandlistfind)
			except:
				commandlistfind = ""
			if not len(commandlistfind) == 0:
				found = f"```\n\nDid you mean?\n\n{commandlistfind}```"
			else:
				found = ""
			await error_builder(luna, f"```\nNot Found\n\n{error}```{found}```\nNote\n\nYou can use \"search\" to search for a command.\n{prefix}search <command> » Search for a command```")
		elif isinstance(error, CheckFailure):
			try:
				await luna.message.delete()
			except:
				pass
			await error_builder(luna, f"```\n{error}```")
		elif isinstance(error, commands.MissingRequiredArgument):
			try:
				await luna.message.delete()
			except:
				pass
			await error_builder(luna, f"```\nMissing arguments\n\n{error}```")
		elif isinstance(error, MissingPermissions):
			try:
				await luna.message.delete()
			except:
				pass
			await error_builder(luna, f"```\nMissing permissions\n\n{error}```")
		elif isinstance(error, commands.CommandInvokeError):
			try:
				await luna.message.delete()
			except:
				pass
			await error_builder(luna, f"```\n{error}```")
		elif "Cannot send an empty message" in error_str:
			try:
				await luna.message.delete()
			except:
				pass
			await error_builder(luna, f"```\n{error}```")
		elif "Cannot send messages to this user" in error_str:
			try:
				await luna.message.delete()
			except:
				pass
			await error_builder(luna, f"```\nCannot send a message to this user\n\n{error}```")
		elif "Cannot send messages in this channel" in error_str:
			try:
				await luna.message.delete()
			except:
				pass
			await error_builder(luna, f"```\nCannot send a message in this channel\n\n{error}```")
		elif "Cannot send files bigger than" in error_str:
			try:
				await luna.message.delete()
			except:
				pass
			await error_builder(luna, f"```\nCannot send files bigger than 8MB\n\n{error}```")
		else:
			try:
				await luna.message.delete()
			except:
				pass
			await error_builder(luna, f"```\n{error}```")

bot.add_cog(OnCommandErrorCog(bot))

# ///////////////////////////////////////////////////////////////
# Help Commands (Listing Commands)

class HelpCog(commands.Cog, name="Help commands"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot

	@commands.command(name = 'help',
					usage="[command]",
					description = "Display the help message",
					aliases = ['h', '?'])
	async def help(self, luna, commandName:str=None):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)

		commandName2 = None
		stop = False

		if commandName is not None:
			for i in self.bot.commands:
				if i.name == commandName.lower():
					commandName2 = i
					break 
				else:
					for j in i.aliases:
						if j == commandName.lower():
							commandName2 = i
							stop = True
							break
						if stop is True:
							break 

			if commandName2 is None:
				if configs.error_log() == "console":
					prints.error(f"No command found with name or alias {color.purple(commandName)}")
				else:
					embed = discord.Embed(
						title="Error",
						description=f"```\nNo command found with name or alias {commandName}```",
						color=0xff0000
					)
					embed.set_thumbnail(url=theme.image_url())
					embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
					embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
					embed.set_image(url=theme.large_image_url())
					await send(luna, embed)
			else:
				if configs.mode() == 2:
					aliases = commandName2.aliases
					aliasList = ""
					if len(aliases) > 0:
						for alias in aliases:
							aliasList += alias + ", "
						aliasList = aliasList[:-2]
						if commandName2.usage is None:
							sent = await luna.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{theme.description()}Name\n{commandName2.name}\n\nAliases\n{aliasList}\n\nUsage\nNone\n\nDescription\n{commandName2.description}\n\n[ {theme.footer()} ]```")
						else:
							sent = await luna.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{theme.description()}Name\n{commandName2.name}\n\nAliases\n{aliasList}\n\nUsage\n{prefix}{commandName2.name} {commandName2.usage}\n\nDescription\n{commandName2.description}\n\n[ {theme.footer()} ]```")
					else:
						if commandName2.usage is None:
							sent = await luna.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{theme.description()}Name\n{commandName2.name}\n\nAliases\nNone\n\nUsage\nNone\n\nDescription\n{commandName2.description}\n\n[ {theme.footer()} ]```")
						else:
							sent = await luna.send(f"```ini\n[ {commandName2.name.title()} Command ]\n\n{theme.description()}Name\n{commandName2.name}\n\nAliases\nNone\n\nUsage\n{prefix}{commandName2.name} {commandName2.usage}\n\nDescription\n{commandName2.description}\n\n[ {theme.footer()} ]```")
					await asyncio.sleep(configs.delete_timer())
					await sent.delete()
				if configs.mode() == 3:
					aliases = commandName2.aliases
					aliasList = ""
					if len(aliases) > 0:
						for alias in aliases:
							aliasList += alias + ", "
						aliasList = aliasList[:-2]
						if commandName2.usage is None:
							sent = await luna.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> {aliasList}``````\n> Usage\n> None``````\n> Description\n> {commandName2.description}```\n> {theme.footer()}")
						else:
							sent = await luna.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> {aliasList}``````\n> Usage\n> {prefix}{commandName2.name} {commandName2.usage}``````\n> Description\n> {commandName2.description}```\n> {theme.footer()}")
					else:
						if commandName2.usage is None:
							sent = await luna.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> None``````\n> Usage\n> None``````\n> Description\n> {commandName2.description}```\n> {theme.footer()}")
						else:
							sent = await luna.send(f"> **{commandName2.name.title()} Command**\n> \n> ```\n> Name\n> {commandName2.name}``````\n> Aliases\n> None``````\n> Usage\n> {prefix}{commandName2.name} {commandName2.usage}``````\n> Description\n> {commandName2.description}```\n> {theme.footer()}")
					
					await asyncio.sleep(configs.delete_timer())
					await sent.delete()

				else:
					embed = discord.Embed(title=f"{commandName2.name.title()} Command", description=f"{theme.description()}", color=theme.hex_color())
					embed.set_thumbnail(url=theme.image_url())
					embed.add_field(name=f"Name", value=f"```\n{commandName2.name}```", inline=False)
					aliases = commandName2.aliases
					aliasList = ""
					if len(aliases) > 0:
						for alias in aliases:
							aliasList += alias + ", "
						aliasList = aliasList[:-2]
						embed.add_field(name=f"Aliases", value=f"```\n{aliasList}```")
					else:
						embed.add_field(name=f"Aliases", value="```\nNone```", inline=False)

					if commandName2.usage is None:
						embed.add_field(name=f"Usage", value=f"```\nNone```", inline=False)
					else:
						embed.add_field(name=f"Usage", value=f"```\n{prefix}{commandName2.name} {commandName2.usage}```", inline=False)
					embed.add_field(name=f"Description", value=f"```\n{commandName2.description}```", inline=False)
					embed.set_thumbnail(url=theme.image_url())
					embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
					embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
					embed.set_image(url=theme.large_image_url())
					await send(luna, embed)
		else:
			command_count = len(bot.commands)
			cog = bot.get_cog('Custom commands')
			custom = cog.get_commands()
			custom_command_count = 0
			for command in custom:
				custom_command_count += 1
			await embed_builder(luna, description=f"{theme.description()}```\nLuna\n\nCommands          » {command_count-custom_command_count}\nCustom Commands   » {custom_command_count}\n``````\nCategories\n\n{prefix}help [command]   » Display all commands\n{prefix}admin            » Administrative commands\n{prefix}abusive          » Abusive commands\n{prefix}animated         » Animated commands\n{prefix}dump             » Dumping\n{prefix}fun              » Funny commands\n{prefix}game             » Game commands\n{prefix}image            » Image commands\n{prefix}hentai           » Hentai explorer\n{prefix}profile          » Current guild profile\n{prefix}protection       » Protections\n{prefix}raiding          » Raiding tools\n{prefix}text             » Text commands\n{prefix}trolling         » Troll commands\n{prefix}tools            » Tools\n{prefix}networking       » Networking\n{prefix}nuking           » Account nuking\n{prefix}utility          » Utilities\n{prefix}settings         » Settings\n{prefix}webhook          » Webhook settings\n{prefix}notifications    » Toast notifications\n{prefix}sharing          » Share with somebody\n{prefix}themes           » Themes\n{prefix}communitythemes  » Community made themes\n{prefix}communitycmds    » Community made commands\n{prefix}customhelp       » Show custom commands\n{prefix}misc             » Miscellaneous\n{prefix}about            » Luna information\n{prefix}repeat           » Repeat last used command\n{prefix}search <command> » Search for a command\n``````\nVersion\n\n{version}```")

	@commands.command(name = "admin",
						usage="[2]",
						description = "Administrative commands")
	async def admin(self, luna, page:str = "1"):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Administrative commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Channel commands')
		commands = cog.get_commands()
		channeltext = ""
		for command in commands:
			channeltext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Member commands')
		commands = cog.get_commands()
		membertext = ""
		for command in commands:
			membertext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Nickname commands')
		commands = cog.get_commands()
		nicktext = ""
		for command in commands:
			nicktext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Role commands')
		commands = cog.get_commands()
		roletext = ""
		for command in commands:
			roletext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Invite commands')
		commands = cog.get_commands()
		invitetext = ""
		for command in commands:
			invitetext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Ignore commands')
		commands = cog.get_commands()
		ignoretext = ""
		for command in commands:
			ignoretext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		if page == "1":
			await embed_builder(luna, title="Administrative", footer_extra=f"Page 1", description=f"{theme.description()}```\nMember Control\n\n{membertext}``````\nChannel Control\n\n{channeltext}``````\nNickname Control\n\n{nicktext}``````\nRole Control\n\n{roletext}``````\nNote\n\n{prefix}admin 2 » Page 2```")
		elif page == "2":
			await embed_builder(luna, title="Administrative", footer_extra=f"Page 2", description=f"{theme.description()}```\nGuild Control\n\n{helptext}``````\nInvite Control\n\n{invitetext}``````\nIgnore Control\n\n{ignoretext}```")

	@commands.command(name = "profile",
					usage="",
					description = "Current guild profile")
	async def profile(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Profile commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Profile", description=f"{theme.description()}```\nCurrent profile\n\nUser              » {bot.user}\nUsername          » {bot.user.name}\nDiscriminator     » {bot.user.discriminator}\n``````\nNickname Control\n\n{prefix}nick <name>      » Change your nickname\n{prefix}invisiblenick    » Make your nickname invisible\n{prefix}junknick         » Pure junk nickname\n``````\nUser Control\n\n{helptext}```")

	@commands.command(name = "statuses",
						usage="",
						description = "Animated statuses")
	async def statuses(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Status commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Status", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "animated",
					usage="",
					description = "Animated commands")
	async def animated(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Animated commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Animated commands", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "dump",
					usage="",
					description = "Dumping")
	async def dump(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Dump commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Dumping", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "text",
					usage="",
					description = "Text commands")
	async def text(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Text commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Text commands", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "game",
					usage="",
					description = "Game commands")
	async def game(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Game commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Game commands", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "image",
					usage="",
					description = "Image commands")
	async def image(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Image commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Image commands", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "hentai",
					usage="",
					description = "Hentai explorer")
	async def hentai(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)

		cog = self.bot.get_cog('Hentai commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		embed = discord.Embed(title="Hentai Explorer", description=f"{theme.description()}```\n{helptext}```", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "trolling",
					usage="",
					description = "Trolling")
	async def trolling(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Troll commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Trolling", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "fun",
					usage="",
					description = "Fun commands")
	async def fun(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Fun commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Fun commands", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "tools",
					usage="",
					description = "Tools")
	async def tools(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Tools commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Tools", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "networking",
					usage="",
					description = "Networking")
	async def networking(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Nettool commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Networking", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "utility",
					usage="",
					aliases=['utils', 'utilities'],
					description = "Utilities")
	async def utility(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Util commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Utilities", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "abusive",
					usage="",
					description = "Abusive commands")
	async def abusive(self, luna):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			prefix = files.json("Luna/config.json", "prefix", documents=True)
			cog = self.bot.get_cog('Abusive commands')
			commands = cog.get_commands()
			helptext = ""
			for command in commands:
				helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			cog = self.bot.get_cog('Guild commands')
			commands = cog.get_commands()
			guildtext = ""
			for command in commands:
				guildtext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			cog = self.bot.get_cog('Mass commands')
			commands = cog.get_commands()
			masstext = ""
			for command in commands:
				masstext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			cog = self.bot.get_cog('All commands')
			commands = cog.get_commands()
			alltext = ""
			for command in commands:
				alltext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			cog = self.bot.get_cog('Spam commands')
			commands = cog.get_commands()
			spamtext = ""
			for command in commands:
				spamtext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			await embed_builder(luna, title="Abusive commands", description=f"{theme.description()}```\nSpam\n\n{spamtext}\n``````\nGuild\n\n{guildtext}\n``````\nMass\n\n{masstext}\n``````\nAll\n\n{alltext}\n``````\nGeneral\n\n{helptext}\n```")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "raiding",
					usage="",
					description = "Raiding servers")
	async def raiding(self, luna):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			prefix = files.json("Luna/config.json", "prefix", documents=True)
			cog = self.bot.get_cog('Raid commands')
			commands = cog.get_commands()
			helptext = ""
			for command in commands:
				helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			await embed_builder(luna, title="Raiding", description=f"{theme.description()}```\n{helptext}```")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "nuking",
					usage="",
					description = "Account nuking")
	async def nuking(self, luna):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			prefix = files.json("Luna/config.json", "prefix", documents=True)
			cog = self.bot.get_cog('Nuking commands')
			commands = cog.get_commands()
			helptext = ""
			for command in commands:
				helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
			await embed_builder(luna, title="Nuking", description=f"{theme.description()}```\n{helptext}```")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")


	@commands.command(name = "protection",
					usage="",
					aliases=['protections', 'protect'],
					description = "Protections")
	async def protection(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Protection commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Privacy commands')
		commands = cog.get_commands()
		privacytext = ""
		for command in commands:
			privacytext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Backup commands')
		commands = cog.get_commands()
		backuptext = ""
		for command in commands:
			backuptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Whitelist commands')
		commands = cog.get_commands()
		whitelisttext = ""
		for command in commands:
			whitelisttext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		activetext = ""
		if not active_list == []:
			activetext = f"\n\nActive protections:"
		for active in active_list:
			activetext+=f"\n{active.title()}"
		cog = self.bot.get_cog('Protection Guild commands')
		commands = cog.get_commands()
		guildtext = ""
		for command in commands:
			guildtext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		guilds = files.json("Luna/protections/config.json", "guilds", documents=True)
		activeguildtext = ""
		if not guilds == []:
			activeguildtext = f"\nProtected guilds:"
		for guild_id in guilds:
			guild = self.bot.get_guild(guild_id)
			activeguildtext+=f"\n{guild.name:17} » {guild.id}"
		await embed_builder(luna, title="Protections", description=f"{theme.description()}```\nEnabled Protections\n\n{'Enabled':17} » {active_protections}{activetext}\n``````\nGuild Configuration\n\n{guildtext}{activeguildtext}``````\nProtections\n\n{helptext}``````\nWhitelist\n\n{whitelisttext}\n``````\nPrivacy | Streamer Mode\n\n{privacytext}\n``````\nBackups\n\n{backuptext}\n```")

	@commands.command(name = "misc",
					usage="",
					description = "Miscellaneous commands")
	async def misc(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Miscellaneous commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Miscellaneous", description=f"{theme.description()}```\n{helptext}```")

	@commands.command(name = "notifications",
					usage="",
					description = "Toast notifications")
	async def notifications(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		toasts = files.json("Luna/notifications/toasts.json", "toasts", documents=True)
		login = files.json("Luna/notifications/toasts.json", "login", documents=True)
		nitro = files.json("Luna/notifications/toasts.json", "nitro", documents=True)
		giveaway = files.json("Luna/notifications/toasts.json", "giveaway", documents=True)
		privnote = files.json("Luna/notifications/toasts.json", "privnote", documents=True)
		selfbot = files.json("Luna/notifications/toasts.json", "selfbot", documents=True)
		pings = files.json("Luna/notifications/toasts.json", "pings", documents=True)
		ghostpings = files.json("Luna/notifications/toasts.json", "ghostpings", documents=True)
		friendevents = files.json("Luna/notifications/toasts.json", "friendevents", documents=True)
		guildevents = files.json("Luna/notifications/toasts.json", "guildevents", documents=True)
		roleupdates = files.json("Luna/notifications/toasts.json", "roleupdates", documents=True)
		nickupdates = files.json("Luna/notifications/toasts.json", "nickupdates", documents=True)
		protection = files.json("Luna/notifications/toasts.json", "protection", documents=True)
		cog = self.bot.get_cog('Toast commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Toast notifications", description=f"{theme.description()}```\nToast configuration\n\nToasts            » {toasts}\nLogin toasts      » {login}\nNitro toasts      » {nitro}\nGiveaway toasts   » {giveaway}\nPrivnote toasts   » {privnote}\nSelfbot toasts    » {selfbot}\nPing toasts       » {pings}\nGhostping toasts  » {ghostpings}\nFriendevent toast » {friendevents}\nGuildevent toasts » {guildevents}\nRoleupdate toasts » {roleupdates}\nNickname toasts   » {nickupdates}\nProtection toasts » {protection}\n``````\nToast control\n\n{helptext}```")

	@commands.command(name = "settings",
					usage="",
					description = "Settings")
	async def settings(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
		errorlog = files.json("Luna/config.json", "error_log", documents=True)
		riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
		themesvar = files.json("Luna/config.json", "theme", documents=True)
		console_mode = files.json("Luna/console/console.json", "mode", documents=True)
		if console_mode == "2":
			console_mode = "information"
		else:
			console_mode = "standard"
		if themesvar == "default":
			pass
		else:
			themesvar = (themesvar[:-5])
		if themesvar == "default":
			theme_description = descriptionvar_request
			if not theme_description == "true":
				theme_description = "off"
			else:
				theme_description = "on"
		else:
			theme_json = files.json("Luna/config.json", "theme", documents=True)
			theme_description = files.json(f"Luna/themes/{theme_json}", "description", documents=True)
			if theme_description == None:
				theme_description = True
			if not theme_description:
				theme_description = "off"
			else:
				theme_description = "on"
		startup_status = files.json("Luna/config.json", "startup_status", documents=True)
		title = theme.title()
		footer = theme.footer()
		hexcolor = theme.hex_color()
		author = theme.author()
		selfbotdetection = files.json("Luna/snipers/selfbot.json", "sniper", documents=True)
		pings = files.json("Luna/notifications/console.json", "pings", documents=True)
		if title == "":
			title = "None"
		if footer == "":
			footer = "None"
		if hexcolor == "":
			hexcolor = "None"
		if author == "":
			author = "None"
		cog = self.bot.get_cog('Settings commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Settings", description=f"{theme.description()}```\nYour current settings\n\nError logging     » {errorlog}\nAuto delete timer » {deletetimer}\nStartup status    » {startup_status}\nTheme             » {themesvar}\nConsole Mode      » {console_mode}\nRiskmode          » {riskmode}\nDescription       » {theme_description}\nSelfbot detection » {selfbotdetection}\nMention notify    » {pings}\n``````\nYour current theme settings\n\nTheme             » {themesvar}\nFooter            » {footer}\nColor             » {hexcolor}\nAuthor            » {author}\n``````\nSettings\n\n{helptext}```")

	@commands.command(name = "sharing",
					usage="",
					description = "Share commands")
	async def sharing(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		share = configs.share()
		user_id = configs.share_id()
		if user_id == "":
			sharinguser = "None"
		else:
			sharinguser = await self.bot.fetch_user(user_id)
		cog = self.bot.get_cog('Share commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Sharing", description=f"{theme.description()}```\nYour current settings\n\nShare             » {share}\nUser              » {sharinguser}\n``````\n{helptext}```")

	@commands.command(name = "webhook",
					usage="",
					description = "Webhook settings")
	async def webhook(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		webhooks = files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True)
		login = files.json("Luna/webhooks/webhooks.json", "login", documents=True)
		nitro = files.json("Luna/webhooks/webhooks.json", "nitro", documents=True)
		giveaway = files.json("Luna/webhooks/webhooks.json", "giveaway", documents=True)
		privnote = files.json("Luna/webhooks/webhooks.json", "privnote", documents=True)
		selfbot = files.json("Luna/webhooks/webhooks.json", "selfbot", documents=True)
		pings = files.json("Luna/webhooks/webhooks.json", "pings", documents=True)
		ghostpings = files.json("Luna/webhooks/webhooks.json", "ghostpings", documents=True)
		friendevents = files.json("Luna/webhooks/webhooks.json", "friendevents", documents=True)
		guildevents = files.json("Luna/webhooks/webhooks.json", "guildevents", documents=True)
		roleupdates = files.json("Luna/webhooks/webhooks.json", "roleupdates", documents=True)
		nickupdates = files.json("Luna/webhooks/webhooks.json", "nickupdates", documents=True)
		protection = files.json("Luna/webhooks/webhooks.json", "protection", documents=True)
		cog = self.bot.get_cog('Webhook setup')
		commands = cog.get_commands()
		setuptext = ""
		for command in commands:
			setuptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Webhook commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		cog = self.bot.get_cog('Webhook urls')
		commands = cog.get_commands()
		urltext = ""
		for command in commands:
			urltext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Webhooks", description=f"{theme.description()}```\nWebhook configuration\n\nWebhooks          » {webhooks}\nLogin webhooks    » {login}\nNitro webhooks    » {nitro}\nGiveaway webhooks » {giveaway}\nPrivnote webhooks » {privnote}\nSelfbot webhooks  » {selfbot}\nPing webhooks     » {pings}\nGhostping webhooks » {ghostpings}\nFriendevent webhooks » {friendevents}\nGuildevent webhooks » {guildevents}\nRoleupdate webhooks » {roleupdates}\nNickname webhooks » {nickupdates}\nProtection webhooks » {protection}\n``````\nWebhook setup\n\n{setuptext}\n``````\nWebhook control\n\n{helptext}\n``````\nWebhook url's\n\n{urltext}```")

	@commands.command(name = "customhelp",
					aliases=['chelp'],
					usage="",
					description = "Show custom commands")
	async def customhelp(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		cog = self.bot.get_cog('Custom commands')
		commands = cog.get_commands()
		helptext = ""
		if commands == []:
			helptext = "No custom commands found!"
		else:
			for command in commands:
				helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Your custom commands", description=f"{theme.description()}```\n{helptext}``````\nNote\n\n{prefix}reload           » Reload custom commands```")

	@commands.command(name = "communitycmds",
					aliases=['ccommands', 'communitycommands', 'community'],
					usage="",
					description = "Community made commands")
	async def communitycmds(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		await embed_builder(luna, title="Community commands", description=f"{theme.description()}```\n{prefix}command luna     » Luna```")

	@commands.command(name = "about",
						usage="",
						description = "Luna information")
	async def about(self, luna):
		await luna.message.delete()
		motd = urllib.request.urlopen('https://pastebin.com/raw/MeHTn6gZ')
		for line in motd:
			motd = line.decode().strip()
		versionpastedec = urllib.request.urlopen('https://pastebin.com/raw/iQPkzEpg')
		for line in versionpastedec:
			versionpaste = line.decode().strip().replace('\'','')
		command_count = len(bot.commands)
		cog = bot.get_cog('Custom commands')
		custom = cog.get_commands()
		custom_command_count = 0
		for command in custom:
			custom_command_count += 1
		if beta:
			beta_info = f" Beta Build"
		else:
			beta_info = ""
		await embed_builder(luna, description=f"```\nMOTD\n\n{motd}\n``````\nVersion\n\n{version}{beta_info}\n``````\nUptime\n\n{hour:02d} Hours, {minute:02d} Minutes and {second:02d} Seconds\n``````\nCommands\n\n{command_count-custom_command_count}\n``````\nCustom commands\n\n{custom_command_count}\n``````\nEnviroment\n\nDiscord.py » {discord.__version__}\n``````\nPublic server invite\n\nhttps://discord.gg/Kxyv7NHVED\n``````\nCustomer only server invite\n\nhttps://discord.gg/3FGEaCnZST\n``````\nWebsite\n\nhttps://team-luna.org\n```")

	@commands.command(name = "repeat",
						usage="",
						description = "Repeat last used command")
	async def repeat(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		await luna.send(f"{prefix}{last_used}")

	@commands.command(name = "search",
						usage="<command>",
						description = "Search for a command")
	async def search(self, luna, commandName:str):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		helptext = ""
		for command in self.bot.commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description},"

		commandlist = helptext.split(",")
		commandlistfind = [ string for string in commandlist if commandName in string]
		commandlistfind='\n'.join(str(e) for e in commandlistfind)

		if not len(commandlistfind) == 0:
			await embed_builder(luna, title=f"Searched for » {commandName.title()}", description=f"{theme.description()}```\n{commandlistfind}``````\nNote\n\n{prefix}help <command>   » To get more information```")
		else:
			await embed_builder(luna, title=f"Searched for » {commandName.title()}", description=f"```\nNo command has been found\n``````\nNote\n\n{prefix}help <command>   » To get more information```")

bot.remove_command("help")
bot.add_cog(HelpCog(bot))
class ProfileCog(commands.Cog, name="Profile commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "online",
					usage="",
					description = "Online status")
	async def online(self, luna):
		await luna.message.delete()
		payload = {'status': "online"}
		requests.patch('https://discordapp.com/api/v9/users/@me/settings', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description="```\nSet status to online```")

	@commands.command(name = "idle",
					usage="",
					description = "Idle status")
	async def idle(self, luna):
		await luna.message.delete()
		payload = {'status': "idle"}
		requests.patch('https://discordapp.com/api/v9/users/@me/settings', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description="```\nSet status to idle```")

	@commands.command(name = "dnd",
					usage="",
					description = "Do not disturb status")
	async def dnd(self, luna):
		await luna.message.delete()
		payload = {'status': "dnd"}
		requests.patch('https://discordapp.com/api/v9/users/@me/settings', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description="```\nSet status to do not disturb```")

	@commands.command(name = "offline",
					usage="",
					description = "Offline status")
	async def offline(self, luna):
		await luna.message.delete()
		payload = {'status': "invisible"}
		requests.patch('https://discordapp.com/api/v9/users/@me/settings', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description="```\nSet status to offline/invisible```")

	@commands.command(name = "startup",
					usage="<online/idle/dnd/offline>",
					description = "Startup")
	async def startup(self, luna, mode:str):
		await luna.message.delete()
		if mode == "online" or mode == "idle" or mode == "dnd" or mode == "offline":
			prints.message(f"Startup status » {color.purple(f'{mode}')}")
			config.startup_status(mode)
			await embed_builder(luna, description=f"```\nStartup status » {mode}```")
		else:
			await mode_error(luna, "online, idle, dnd or offline")

bot.add_cog(ProfileCog(bot))
class StatusCog(commands.Cog, name="Animated statuses"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "status",
					usage="<text>",
					description = "Set a custom status")
	async def status(self, luna, text:str):
		await luna.message.delete()
		payload = {'custom_status': {"text": f"{text}"}}
		requests.patch('https://discordapp.com/api/v9/users/@me/settings', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description=f"```\nSet custom status to » {text}```")

	@commands.command(name = "removestatus",
					usage="",
					description = "Remove custom status")
	async def removestatus(self, luna):
		await luna.message.delete()
		payload = {'custom_status': {"text": ""}}
		requests.patch('https://discordapp.com/api/v9/users/@me/settings', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description=f"```\nRemoved custom status```")

bot.add_cog(StatusCog(bot))
class ChannelCog(commands.Cog, name="Channel commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "channelinfo",
					usage="<#channel>",
					description = "Information")
	async def channelinfo(self, luna, channel:discord.TextChannel):
		await luna.message.delete()
		await embed_builder(luna, title="Channel Information", description=f"```\n{'Name':17} » {channel.name}\n{'ID':17} » {channel.id}\n{'Created at':17} » {channel.created_at}\n{'Category':17} » {channel.category}\n{'Position':17} » {channel.position}\n{'Topic':17} » {channel.topic}\n{'Is NSFW?':17} » {channel.is_nsfw()}\n```")

	@commands.command(name = "textchannel",
					usage="<name>",
					description = "Create a text channel")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def textchannel(self, luna, name:str):
		await luna.message.delete()
		channel = await luna.guild.create_text_channel(name)
		await embed_builder(luna, description=f"```\nCreated text channel » {channel.mention}```")

	@commands.command(name = "voicechannel",
					usage="<name>",
					description = "Create a voice channel")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def voicechannel(self, luna, name:str):
		await luna.message.delete()
		channel = await luna.guild.create_voice_channel(name)
		await embed_builder(luna, description=f"```\nCreated voice channel » {channel.mention}```")

	@commands.command(name = "stagechannel",
					usage="<name>",
					description = "Create a stage channel")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def stagechannel(self, luna, name:str):
		await luna.message.delete()
		payload = {
			'name': f"{name}",
			'type': 13
			}
		this = requests.post(f'https://discordapp.com/api/v9/guilds/{luna.guild.id}/channels', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description=f"```\nCreated stage channel » {name}```")

	@commands.command(name = "newschannel",
					usage="<name>",
					description = "Create a news channel")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def newschannel(self, luna, name:str):
		await luna.message.delete()
		payload = {
			'name': f"{name}",
			'type': 5
			}
		requests.post(f'https://discordapp.com/api/v9/guilds/{luna.guild.id}/channels', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description=f"```\nCreated news channel » {name}```")

	@commands.command(name = "renamechannel",
					usage="<#channel> <name>",
					description = "Rename channel")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def renamechannel(self, luna, channel:discord.TextChannel, name:str):
		await luna.message.delete()
		await channel.edit(name=name)
		await embed_builder(luna, description=f"```\nRenamed {luna.channel.name} to » {channel.mention}```")

	@commands.command(name = "deletechannel",
					usage="<#channel>",
					description = "Delete a channel")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def deletechannel(self, luna, channel:discord.TextChannel):
		await luna.message.delete()
		await channel.delete()
		await embed_builder(luna, description=f"```\nDeleted channel » {channel.mention}```")

	@commands.command(name = "slowmode",
					usage="<seconds>",
					description = "Set slowmode")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def slowmode(self, luna, seconds:int):
		await luna.message.delete()
		if seconds < 0:
			await embed_builder(luna, title="Slowmode", description=f"```\nThe slowmode can't be negative```")
			return
		if seconds == 0:
			await luna.channel.edit(slowmode_delay=0)
			await embed_builder(luna, title="Slowmode", description=f"```\nDisabled slowmode```")
			return
		await luna.channel.edit(slowmode_delay=seconds)
		await embed_builder(luna, title="Slowmode", description=f"```\nSet slowmode to » {seconds} seconds```")

	@commands.command(name = "removeslowmode",
					usage="",
					description = "Remove slowmode")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def removeslowmode(self, luna):
		await luna.message.delete()
		await luna.channel.edit(slowmode_delay=0)
		await embed_builder(luna, title="Slowmode", description=f"```\nRemoved slowmode```")

	@commands.command(name = "lock",
					usage="<#channel>",
					description = "Lock a channel")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def lock(self, luna, channel:discord.TextChannel):
		await luna.message.delete()
		await channel.set_permissions(luna.guild.default_role, send_messages=False)
		await channel.edit(name="🔒-locked")
		await embed_builder(luna, description=f"```\nLocked channel » {channel.mention}```")

	@commands.command(name = "unlock",
					usage="<#channel>",
					description = "Unlock a channel")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def unlock(self, luna, channel:discord.TextChannel):
		await luna.message.delete()
		await channel.set_permissions(luna.guild.default_role, send_messages=True)
		await channel.edit(name="🔒-unlocked")
		await embed_builder(luna, description=f"```\nUnlocked channel » {channel.mention}```")

	@commands.command(name = "category",
					usage="<name>",
					description = "Create a category")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def category(self, luna, name:str):
		await luna.message.delete()
		category = await luna.guild.create_category_channel(name)
		await embed_builder(luna, description=f"```\nCreated category » {category.mention}```")

	@commands.command(name = "deletecategory",
					usage="<category_id>",
					description = "Delete a category")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def deletecategory(self, luna, category:discord.CategoryChannel):
		await luna.message.delete()
		await category.delete()
		await embed_builder(luna, description=f"```\nDeleted category » {category.mention}```")

	@commands.command(name = "purge",
					usage="<amount>",
					description = "Purge the channel")
	async def purge(self, luna, amount: int):
		await luna.message.delete()
		async for message in luna.message.channel.history(limit=amount):
			try:
				await message.delete()
			except:
				pass
 
	@commands.command(name = "nuke",
					usage="[#channel]",
					description = "Nuke the channel")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def nuke(self, luna, channel:discord.TextChannel=None):
		await luna.message.delete()
		if channel is None:
			channel = luna.channel
		new_channel = await channel.clone()
		await new_channel.edit(position=channel.position)
		await channel.delete()
		await embed_builder(new_channel, description=f"```\nThis channel has been nuked```")

bot.add_cog(ChannelCog(bot))
class MemberCog(commands.Cog, name="Member commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "userinfo",
					usage="[user_id]",
					description = "User information")
	async def userinfo(self, luna, user:discord.Member=None):
		await luna.message.delete()
		if user is None:
			user = luna.author
		r = requests.get(f'https://discordapp.com/api/v9/users/{user.id}', headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'}).json()
		req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
		banner_id = req["banner"]
		if banner_id:
			banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
		else:
			banner_url = None
		await embed_builder(luna, title="User information", thumbnail=user.avatar_url, large_image=banner_url, description=f"```\nGeneral Information\n\n{'User':12} » {user.name}#{user.discriminator}\n{'ID':12} » {user.id}\n{'Status':12} » {user.status}\n{'Bot':12} » {user.bot}\n{'Public Flags':12} » {r['public_flags']}\n{'Banner Color':12} » {r['banner_color']}\n{'Accent Color':12} » {r['accent_color']}\n``````\nCreated at:\n{user.created_at}\n``````\nImage Information\n\nAvatar URL:\n{user.avatar_url}\n\nBanner URL:\n{banner_url}\n```")

	@commands.command(name = "whois",
					usage="<@member>",
					description = "Guild member information")
	@commands.guild_only()
	async def whois(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			user = luna.author
		if user.id == 406907871998246924:
			special = "\n\nSpecial » Founder & Head Dev @ Team Luna"
		elif user.id == 707355480422350848 or user.id == 663516459837685770:
			special = "\n\nSpecial » Developer @ Team Luna"
		elif user.id == 288433475831332894 or user.id == 465275771523563531:
			special = "\n\nSpecial » Member @ Team Luna"
		elif user.id == 203906692834918401 or user.id == 699099683603349654 or user.id == 319759781315215360:
			special = "\n\nSpecial » Luna Beta"
		elif user.id == 254994687444779008:
			special = "\n\nSpecial » First Luna Customer"
		else:
			special = ""
		date_format = "%a, %d %b %Y %I:%M %p"
		members = sorted(luna.guild.members, key=lambda m: m.joined_at)
		role_string = ', '.join([r.name for r in user.roles][1:])
		perm_string = ', '.join([str(p[0]).replace("_", " ").title()for p in user.guild_permissions if p[1]])
		await embed_builder(luna, description=f"User » {user.mention}\n```User information\n\nJoined » {user.joined_at.strftime(date_format)}\nJoin position » {members.index(user) + 1}\nRegistered » {user.created_at.strftime(date_format)}\n``````\nUser server information\n\nRoles Amount » {len(user.roles) - 1}\nRoles\n\n{role_string}\n\nPermissions\n\n{perm_string}{special}```")
        
	@commands.command(name = "report",
					usage="<message_id> <reason>",
					description = "Report a user")
	async def report(self, luna, message_id:str, *, reason:str):
		await luna.message.delete()
		payload = {
			'message_id': message_id,
			'reason': reason
		}
		requests.post('https://discordapp.com/api/v9/report', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, title="Report", description=f"```\nMessage {message_id} has been reported\n\nReason » {reason}```")

	@commands.command(name = "mute",
					usage="<@member> [reason]",
					description = "Mute a user")
	@commands.guild_only()
	@has_permissions(manage_roles=True)
	async def mute(self, luna, user: discord.Member, *, reason:str=None):
		await luna.message.delete()
		role = discord.utils.get(luna.guild.roles, name="Muted")
		if not role:
			role = await luna.guild.create_role(name="Muted")
			for channel in luna.guild.channels:
				await channel.set_permissions(role, send_messages=False)
		await user.add_roles(role)
		await embed_builder(luna, title="Mute", description=f"```\n{user.mention} has been muted\n\nReason » {reason}```")

	@commands.command(name = "unmute",
					usage="<@member> [reason]",
					description = "Unmute a user")
	@commands.guild_only()
	@has_permissions(manage_roles=True)
	async def unmute(self, luna, user: discord.Member, *, reason:str=None):
		await luna.message.delete()
		role = discord.utils.get(luna.guild.roles, name="Muted")
		if not role:
			await embed_builder(luna, title="Unmute", description="No mute role found")
			return
		await user.remove_roles(role, reason="Unmute")
		await embed_builder(luna, title="Unmute", description=f"```\n{user.mention} has been unmuted\n\nReason » {reason}```")

	@commands.command(name = "timeout",
					usage="<user> <time>",
					description = "Time out a user")
	@commands.guild_only()
	@has_permissions(ban_members=True)
	async def timeout(self, luna, user:discord.Member, time:int):
		await luna.message.delete()
		payload = {
			'user_id': user.id,
			'duration': time
			}
		requests.post(f'https://discordapp.com/api/v9/guilds/{luna.guild.id}/bans', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
		await embed_builder(luna, description=f"```\nTime out » {user.mention} for {time} seconds```")

	@commands.command(name = "kick",
					usage="<@member> [reason]",
					description = "Kick a user")
	@commands.guild_only()
	@has_permissions(kick_members=True)
	async def kick(self, luna, user: discord.Member, *, reason:str=None):
		await luna.message.delete()
		await user.kick(reason=reason)
		await embed_builder(luna, title="Kick", description=f"```\n{user.mention} has been kicked\n\nReason » {reason}```")

	@commands.command(name = "softban",
					usage="<@member> [reason]",
					description = "Softban a user")
	@commands.guild_only()
	@has_permissions(ban_members=True)
	async def softban(self, luna, user: discord.Member, *, reason:str=None):
		await luna.message.delete()
		await user.ban(reason=reason)
		await user.unban(reason=reason)
		await embed_builder(luna, title="Softban", description=f"```\n{user.mention} has been softbanned\n\nReason » {reason}```")

	@commands.command(name = "ban",
					usage="<@member> [reason]",
					description = "Ban a user")
	@commands.guild_only()
	@has_permissions(ban_members=True)
	async def ban(self, luna, user: discord.Member, *, reason:str=None):
		await luna.message.delete()
		await user.ban(reason=reason)
		await embed_builder(luna, title="Ban", description=f"```\n{user.mention} has been banned\n\nReason » {reason}```")

	@commands.command(name = "unban",
					usage="<user_id>",
					description = "Unban a user")
	@commands.guild_only()
	@has_permissions(ban_members=True)
	async def unban(self, luna, user_id:int):
		await luna.message.delete()
		banned_users = await luna.guild.bans()
		for ban_entry in banned_users:
			user = ban_entry.user
			if user.id == user_id:
				await luna.guild.unban(user)
				await embed_builder(luna, title="Unban", description=f"```\n{user.mention} has been unbanned```")
				return
		await embed_builder(luna, title="Unban", description=f"```\nNo banned user with the id {user_id} was found```")

	@commands.command(name = "bans",
					usage="[guild_id]",
					description = "List all bans")
	@commands.guild_only()
	@has_permissions(ban_members=True)
	async def bans(self, luna, guild_id:int=None):
		await luna.message.delete()
		if guild_id is not None:
			guild = discord.utils.get(self.bot.guilds, id=guild_id)
			bans = await guild.bans()
		else:
			guild = luna.guild
			bans = await guild.bans()
		if len(bans) == 0:
			await embed_builder(luna, title=f"Bans in {guild.name}", description=f"```\nNo users are banned in {guild.name}```")
			return
		bans = [f"{b.user.name}#{b.user.discriminator} | {b.user.id}" for b in bans]
		bans = "\n".join(bans)
		await embed_builder(luna, title=f"Bans in {guild.name}", description=f"```{bans}```")

	@commands.command(name = "savebans",
					usage="[guild_id]",
					description = "Save bans")
	@commands.guild_only()
	@has_permissions(ban_members=True)
	async def savebans(self, luna, guild_id:int=None):
		await luna.message.delete()
		if guild_id is not None:
			guild = discord.utils.get(self.bot.guilds, id=guild_id)
			bans = await guild.bans()
		else:
			guild = luna.guild
			bans = await guild.bans()
		if len(bans) == 0:
			await embed_builder(luna, title=f"Bans in {guild.name}", description=f"```\nNo users are banned in {guild.name}```")
			return
		bans = [f"{b.user.name}#{b.user.discriminator} | {b.user.id}" for b in bans]
		bans = "\n".join(bans)
		files.create_folder(f"Luna/backup/guilds/{guild.name}", documents=True)
		files.write_file(f"Luna/backup/guilds/{guild.name}/bans.txt", bans, documents=True)
		await embed_builder(luna, title=f"Saved Bans", description=f"```\nSaved all bans in Luna/backup/guilds/{guild.name}/bans.txt\n``````{bans}```")

	@commands.command(name = "loadbans",
					usage="[guild_id]",
					description = "Load bans")
	@commands.guild_only()
	@has_permissions(ban_members=True)
	async def loadbans(self, luna, guild_id:int=None):
		await luna.message.delete()
		if guild_id is not None:
			guild = discord.utils.get(self.bot.guilds, id=guild_id)
		else:
			guild = luna.guild
		if not files.file_exist(f"Luna/backup/guilds/{guild.name}", documents=True):
			await embed_builder(luna, title=f"Load bans", description=f"```\nNo bans were found in Luna/backup/{guild.name}/bans.txt```")
			return
		bans = files.read_file(f"Luna/backup/guilds/{guild.name}/bans.txt", documents=True)
		bans = bans.split("\n")
		for ban in bans:
			if ban == "":
				continue
			user_id = int(ban.split(" | ")[1])
			user = discord.utils.get(guild.members, id=user_id)
			await guild.ban(user)
		await embed_builder(luna, title=f"Load bans", description=f"```\nLoaded all bans from Luna/backup/guilds/{guild.name}/bans.txt```")

bot.add_cog(MemberCog(bot))
class RoleCog(commands.Cog, name="Role commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
	
	@commands.command(name = "roleinfo",
					usage="<@role>",
					description = "Information")
	async def roleinfo(self, luna, role:discord.Role):
		await luna.message.delete()
		role_amount = 0
		role_members = ""
		for member in luna.guild.members:
			for roles in member.roles:
				if roles.id == role.id:
					role_amount += 1
					role_members += f"{member.name}#{member.discriminator}\n"
		if role_members == "":
			role_members = "No members have this role"
		await embed_builder(luna, title="Role Information", description=f"```\n{'Name':17} » {role.name}\n{'ID':17} » {role.id}\n{'Color':17} » {role.color}\n{'Created at':17} » {role.created_at}\n{'Position':17} » {role.position}\n``````\n{'Members':17} » {role_amount}\n\nMember List:\n{role_members}\n``````\n{'Permissions':17} » {role.permissions}\n```")

	@commands.command(name = "giverole",
					usage="<@member> <role_id>",
					description = "Give a role")
	@commands.guild_only()
	@has_permissions(manage_roles=True)
	async def giverole(self, luna, member:discord.Member, role_id:int):
		await luna.message.delete()
		role = discord.utils.get(luna.guild.roles, id=role_id)
		if role is None:
			await embed_builder(luna, title="Give role", description=f"```\nNo role with the id {role_id} was found```")
			return
		await member.add_roles(role)
		await embed_builder(luna, title="Give role", description=f"```\nGave {member.name}#{member.discriminator} role » {role.name}```")

	@commands.command(name = "giveallroles",
					usage="<@member>",
					description = "Give all roles")
	@commands.guild_only()
	@has_permissions(manage_roles=True)
	async def giveallroles(self, luna, member:discord.Member):
		await luna.message.delete()
		for role in luna.guild.roles:
			if role.name == "@everyone":
				continue
			await member.add_roles(role)
		await embed_builder(luna, title="Give all roles", description=f"```\nGave all roles to » {member.name}#{member.discriminator}```")

	@commands.command(name = "allroles",
					usage="",
					description = "Give all roles")
	@commands.guild_only()
	@has_permissions(manage_roles=True)
	async def allroles(self, luna):
		await luna.message.delete()
		for member in luna.guild.members:
			for role in luna.guild.roles:
				if role.name == "@everyone":
					continue
				await member.add_roles(role)
		await embed_builder(luna, title="Give all roles", description=f"```\nGave all members all roles```")

	@commands.command(name = "removeallroles",
					usage="<@member>",
					description = "Remove all roles")
	@commands.guild_only()
	@has_permissions(manage_roles=True)	
	async def removeallroles(self, luna, member:discord.Member):
		await luna.message.delete()
		for role in luna.guild.roles:
			if role.name == "@everyone":
				continue
			await member.remove_roles(role)
		await embed_builder(luna, title="Remove all roles", description=f"```\nRemoved all roles from » {member.name}#{member.discriminator}```")

	@commands.command(name = "removerole",
					usage="<@member> <role_id>",
					description = "Remove a role")
	@commands.guild_only()
	@has_permissions(manage_roles=True)
	async def removerole(self, luna, member:discord.Member, role_id:int):
		await luna.message.delete()
		role = discord.utils.get(luna.guild.roles, id=role_id)
		if role is None:
			await embed_builder(luna, title="Remove role", description=f"```\nNo role with the id {role_id} was found```")
			return	
		await member.remove_roles(role)
		await embed_builder(luna, title="Remove role", description=f"```\nRemoved role {role.name} from » {member.name}#{member.discriminator}```")

	@commands.command(name = "createrole",
					usage="<role_name>",
					description = "Create a role")
	@commands.guild_only()
	@has_permissions(manage_roles=True)
	async def createrole(self, luna, *, role_name:str):
		await luna.message.delete()
		role = await luna.guild.create_role(name=role_name)
		await embed_builder(luna, title="Create role", description=f"```\nCreated role » {role.name}```")

	@commands.command(name = "renamerole",
					usage="<role_id> <name>",
					description = "Rename a role")
	@commands.guild_only()
	@has_permissions(manage_roles=True)
	async def renamerole(self, luna, role_id:int, *, name:str):
		await luna.message.delete()
		role = discord.utils.get(luna.guild.roles, id=role_id)
		if role is None:
			await embed_builder(luna, title="Rename role", description=f"```\nNo role with the id {role_id} was found```")
			return
		await role.edit(name=name)
		await embed_builder(luna, title="Rename role", description=f"```\nRenamed role {role.name} to » {name}```")

	@commands.command(name = "renameroles",
					usage="<name>",
					description = "Rename all roles")
	@commands.guild_only()
	@has_permissions(manage_roles=True)
	async def renameroles(self, luna, *, name:str):
		await luna.message.delete()
		for role in luna.guild.roles:
			if role.name == "@everyone":
				continue
			await role.edit(name=name)
		await embed_builder(luna, title="Rename all roles", description=f"```\nRenamed all roles to » {name}```")

	@commands.command(name = "deleterole",
					usage="<role_id>",
					description = "Delete a role")
	@commands.guild_only()
	@has_permissions(manage_roles=True)
	async def deleterole(self, luna, role_id:int):
		await luna.message.delete()
		role = discord.utils.get(luna.guild.roles, id=role_id)
		if role is None:
			await embed_builder(luna, title="Delete role", description=f"```\nNo role with the id {role_id} was found```")
			return
		await role.delete()
		await embed_builder(luna, title="Delete role", description=f"```\nDeleted role » {role.name}```")

bot.add_cog(RoleCog(bot))
class NickCog(commands.Cog, name="Nickname commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "nick",
					usage="<name>",
					description = "Change nickname")
	@commands.guild_only()
	@has_permissions(manage_nicknames=True)
	async def nick(self, luna, *, name:str):
		await luna.message.delete()
		await luna.author.edit(nick=name)
		await embed_builder(luna, title="Nickname", description=f"```\nChanged nickname to » {name}```")
	
	@commands.command(name = "nickmember",
					usage="<@member> <name>",
					description = "Change nickname")
	@commands.guild_only()
	@has_permissions(manage_nicknames=True)
	async def nickmember(self, luna, member:discord.Member, *, name:str):
		await luna.message.delete()
		await member.edit(nick=name)
		await embed_builder(luna, title="Nickname", description=f"```\nChanged nickname of {member.name}#{member.discriminator} to » {name}```")

	@commands.command(name = "nickall",
					usage="<name>",
					description = "Change nickname of everyone")
	@commands.guild_only()
	@has_permissions(manage_nicknames=True)
	async def nickall(self, luna, *, name:str):
		await luna.message.delete()
		for member in luna.guild.members:
			await member.edit(nick=name)
		await embed_builder(luna, title="Nickall", description=f"```\nChanged nickname of everyone to » {name}```")

	@commands.command(name = "clearnick",
					usage="[@member]",
					description = "Clear nickname")
	@commands.guild_only()
	@has_permissions(manage_nicknames=True)
	async def clearnick(self, luna, member:discord.Member=None):
		await luna.message.delete()
		if member is None:
			member = luna.author
		await member.edit(nick=None)
		await embed_builder(luna, title="Clearnick", description=f"```\nCleared nickname of » {member.name}#{member.discriminator}```")

	@commands.command(name = "clearallnick",
					usage="",
					description = "Clear all nicknames")
	@commands.guild_only()
	@has_permissions(manage_nicknames=True)
	async def clearallnick(self, luna):
		await luna.message.delete()
		for member in luna.guild.members:
			await member.edit(nick=None)
		await embed_builder(luna, title="Clearnick", description=f"```\nCleared nickname of everyone```")

bot.add_cog(NickCog(bot))
class InviteCog(commands.Cog, name="Invite commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "inviteinfo",
					usage="<invite>",
					description = "Invite information")
	@commands.guild_only()
	async def inviteinfo(self, luna, invite:str):
		await luna.message.delete()
		invite = await self.bot.get_invite(invite)
		if invite is None:
			await embed_builder(luna, title="Invite info", description=f"```\nNo invite with the id {invite} was found```")
			return
		await embed_builder(luna, title="Invite info", description=f"```\nInvite » {invite.code}\nCreated at » {invite.created_at}\nChannel » {invite.channel.mention}\nGuild » {invite.guild.name}\nCreated by » {invite.inviter.name}#{invite.inviter.discriminator}\nMax uses » {invite.max_uses}\nUses » {invite.uses}```")

	@commands.command(name = "invite",
					usage="[channel_id] [age] [uses]",
					description = "Invite")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def invite(self, luna, channel_id:int=None, max_age:int=0, max_uses:int=0):
		await luna.message.delete()
		if channel_id is None:
			channel = luna.channel
		else:
			channel = discord.utils.get(luna.guild.channels, id=channel_id)
		if channel is None:
			await embed_builder(luna, title="Invite", description=f"```\nNo channel with the id » {channel_id} was found```")
			return
		invite = await channel.create_invite(max_age=max_age, max_uses=max_uses)
		await embed_builder(luna, title="Invite", description=f"```\nCreated invite » {invite.url}```")

	@commands.command(name = "delinvite",
					usage="<invite_id>",
					description = "Delete invite")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def delinvite(self, luna, invite_id:int):
		await luna.message.delete()
		invite = discord.utils.get(luna.guild.invites, id=invite_id)
		if invite is None:
			await embed_builder(luna, title="Delete invite", description=f"```\nNo invite with the id » {invite_id} was found```")
			return
		await invite.delete()
		await embed_builder(luna, title="Delete invite", description=f"```\nDeleted invite » {invite.url}```")	

	@commands.command(name = "delallinvite",
					usage="",
					description = "Delete all invites")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def delallinvite(self, luna):
		await luna.message.delete()
		for invite in luna.guild.invites:
			await invite.delete()
		await embed_builder(luna, title="Delete invite", description=f"```\nDeleted all invites```")

	@commands.command(name = "invitelist",
					usage="",
					description = "List all invites")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def invitelist(self, luna):	
		await luna.message.delete()
		invites = luna.guild.invites
		if len(invites) == 0:
			await embed_builder(luna, title="Invite list", description=f"```\nNo invites were found```")
			return
		invite_list = ""
		for invite in invites:
			invite_list += f"{invite.url}\n"
		await embed_builder(luna, title="Invite list", description=f"```\n{invite_list}```")

	@commands.command(name = "invitechannel",
					usage="<channel_id>",
					description = "Channel invites")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def invitelistchannel(self, luna, channel_id:int):
		await luna.message.delete()
		channel = discord.utils.get(luna.guild.channels, id=channel_id)
		if channel is None:
			await embed_builder(luna, title="Invite list", description=f"```\nNo channel with the id » {channel_id} was found```")
			return	
		invites = channel.invites
		if len(invites) == 0:
			await embed_builder(luna, title="Invite list", description=f"```\nNo invites were found```")
			return
		invite_list = ""
		for invite in invites:
			invite_list += f"{invite.url}\n"
		await embed_builder(luna, title="Invite list", description=f"```\n{invite_list}```")

	@commands.command(name = "inviteguild",
					usage="",
					description = "Invites of a guild")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def invitelistguild(self, luna):
		await luna.message.delete()
		invites = luna.guild.invites
		if len(invites) == 0:
			await embed_builder(luna, title="Invite list", description=f"```\nNo invites were found```")
			return
		invite_list = ""
		for invite in invites:
			invite_list += f"{invite.url}\n"
		await embed_builder(luna, title="Invite list", description=f"```\n{invite_list}```")

	@commands.command(name = "inviteuser",
					usage="<user_id>",
					description = "Invites of a user")
	@commands.guild_only()
	@has_permissions(manage_channels=True)
	async def invitelistuser(self, luna, user_id:int):
		await luna.message.delete()
		user = discord.utils.get(luna.guild.members, id=user_id)
		if user is None:
			await embed_builder(luna, title="Invite list", description=f"```\nNo user with the id » {user_id} was found```")
			return
		invites = user.invites
		if len(invites) == 0:
			await embed_builder(luna, title="Invite list", description=f"```\nNo invites were found```")
			return
		invite_list = ""
		for invite in invites:
			invite_list += f"{invite.url}\n"
		await embed_builder(luna, title="Invite list", description=f"```\n{invite_list}```")

bot.add_cog(InviteCog(bot))
class AdminCog(commands.Cog, name="Administrative commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "guildname",
					usage="<name>",
					description = "Change guild name")
	@commands.guild_only()
	@has_permissions(manage_guild=True)
	async def guildname(self, luna, *, name:str):
		await luna.message.delete()
		await luna.guild.edit(name=name)
		await embed_builder(luna, title="Guildname", description=f"```\nChanged the name of the guild to » {name}```")

	@commands.command(name = "guildimage",
					usage="<image_url>",
					description = "Change guild image")
	@commands.guild_only()
	@has_permissions(manage_guild=True)
	async def guildimage(self, luna, *, image_url:str):
		await luna.message.delete()
		await luna.guild.edit(icon=image_url)
		await embed_builder(luna, title="Guildimage", description=f"```\nChanged the image of the guild to » {image_url}```")

	@commands.command(name = "guildbanner",
					usage="<image_url>",
					description = "Change guild banner")
	@commands.guild_only()
	@has_permissions(manage_guild=True)
	async def guildbanner(self, luna, *, image_url:str):
		await luna.message.delete()
		await luna.guild.edit(banner=image_url)
		await embed_builder(luna, title="Guildbanner", description=f"```\nChanged the banner of the guild to » {image_url}```")

	@commands.command(name = "getguildimage",
					usage="[guild_id]",
					description = "Get the guild image")
	@commands.guild_only()
	@has_permissions(manage_guild=True)
	async def getguildimage(self, luna, guild_id:int=None):
		await luna.message.delete()
		if guild_id is None:
			guild_id = luna.guild.id
		guild = discord.utils.get(luna.guilds, id=guild_id)
		if guild is None:
			await embed_builder(luna, title="Guildimage", description=f"```\nNo guild with the id » {guild_id} was found```")
			return
		await embed_builder(luna, title="Guildimage", description=f"```\n{guild.icon_url}```")

	@commands.command(name = "getguildbanner",
					usage="[guild_id]",
					description = "Get the guild banner")
	@commands.guild_only()
	@has_permissions(manage_guild=True)
	async def getguildbanner(self, luna, guild_id:int=None):
		await luna.message.delete()
		if guild_id is None:
			guild_id = luna.guild.id
		guild = discord.utils.get(luna.guilds, id=guild_id)
		if guild is None:
			await embed_builder(luna, title="Guildbanner", description=f"```\nNo guild with the id » {guild_id} was found```")
			return
		await embed_builder(luna, title="Guildbanner", description=f"```\n{guild.banner_url}```")

	@commands.command(name = "guildinfo",
					usage="[guild_id]",
					description = "Guild information")
	@commands.guild_only()
	@has_permissions(manage_guild=True)
	async def guildinfo(self, luna, guild_id:int=None):
		await luna.message.delete()
		if guild_id is None:
			guild = luna.guild
		else:
			guild = discord.utils.get(bot.guilds, id=guild_id)
			if guild is None:
				await embed_builder(luna, title="Guildinfo", description=f"```\nNo guild with the id {guild_id} was found```")
				return
		await embed_builder(luna, title="Guildinfo", thumbnail=guild.icon_url, large_image=guild.banner_url, description=f"```\nGeneral Information\n\n{'Guild':<17} » {guild.name}\n{'ID':17} » {guild.id}\n{'Owner':17} » {guild.owner}\n{'Created at':17} » {guild.created_at}\n{'Boost':17} » {guild.premium_subscription_count}\n{'Boost status':17} » {guild.premium_subscription_count is not None}\n{'Region':17} » {guild.region}\n{'Verification':17} » {guild.verification_level}\n``````\nMember Information\n\n{'Member count':17} » {guild.member_count}\n``````\nChannel Information\n\n{'Text channels':17} » {len(guild.text_channels)}\n{'Voice channels':17} » {len(guild.voice_channels)}\n``````\nRole Information\n\n{'Role count':17} » {len(guild.roles)}```")
				
bot.add_cog(AdminCog(bot))

ignore_list = []

class IgnoreCog(commands.Cog, name="Ignore commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "ignore",
					usage="<@user>",
					description = "Ignore user DMs")
	async def ignore(self, luna, *, user:discord.Member):
		await luna.message.delete()
		global ignore_list
		if user.id in ignore_list:
			await embed_builder(luna, title="Ignore", description=f"```\n{user} is already ignored```")
			return
		ignore_list.append(user.id)
		await embed_builder(luna, title="Ignore", description=f"```\n{user} is now ignored```")

	@commands.command(name = "unignore",
					usage="<@user>",
					description = "Unignore user DMs")
	async def unignore(self, luna, *, user:discord.Member):
		await luna.message.delete()
		global ignore_list
		if user.id not in ignore_list:
			await embed_builder(luna, title="Unignore", description=f"```\n{user} is not ignored```")
			return
		ignore_list.remove(user.id)
		await embed_builder(luna, title="Unignore", description=f"```\n{user} is now unignored```")

	@commands.command(name = "ignorelist",
					usage="",
					description = "List ignored users")
	async def ignorelist(self, luna):
		await luna.message.delete()
		global ignore_list
		if len(ignore_list) == 0:
			await embed_builder(luna, title="Ignorelist", description=f"```\nNo users are ignored```")
			return
		await embed_builder(luna, title="Ignorelist", description=f"```\n{ignore_list}```")

	@commands.command(name = "ignorelistclear",
					usage="",
					description = "Clear ignore list")
	async def ignorelistclear(self, luna):
		await luna.message.delete()
		global ignore_list
		if len(ignore_list) == 0:
			await embed_builder(luna, title="Ignorelist", description=f"```\nNo users are ignored```")
			return
		ignore_list.clear()
		await embed_builder(luna, title="Ignorelist", description=f"```\nIgnore list is now cleared```")

bot.add_cog(IgnoreCog(bot))
class AnimatedCog(commands.Cog, name="Animated commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "animguild",
						usage="[name]",
						description = "Animates the guild name")
	async def animguild(self, luna, *, name:str = None):
		await luna.message.delete()
		global cyclename
		global start_animation
		start_animation = True
		if name is None:
			embed = discord.Embed(title="Animguild", description=f"```\nAnimating: {name}```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)
			name = luna.guild.name.lower() 
			cyclename = name
			length = len(name)
			while start_animation:
				for x in range(length):
					if start_animation == True:
						time.sleep(0.5)
						letter = cyclename[x]
						first_part = cyclename[:x]
						second_part = cyclename[x+1:]
						new_data = first_part + second_part
						if letter == letter.upper():
							await luna.guild.edit(name=new_data[:x] + letter.lower() + new_data[x:])
						else:
							await luna.guild.edit(name=new_data[:x] + letter.upper() + new_data[x:])		
					else:
						break
			
		else:
			if len(name) > 3:
				embed = discord.Embed(title="Animguild", description=f"```\nAnimating: {name}```", color=theme.hex_color())
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)
				name = luna.guild.name.lower()
				cyclename = name
				length = len(name)
				while start_animation:
					for x in range(length):
						if start_animation == True:
							time.sleep(0.5)
							letter = cyclename[x]
							first_part = cyclename[:x]
							second_part = cyclename[x+1:]
							new_data = first_part + second_part
							if letter == letter.upper():
								await luna.guild.edit(name=new_data[:x] + letter.lower() + new_data[x:])
							else:
								await luna.guild.edit(name=new_data[:x] + letter.upper() + new_data[x:])
						else:
							break
			else:
				if configs.error_log() == "console":
					prints.error("Invalid name length, needs to be over 3 characters long")
				else:
					embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nInvalid name length, needs to be over 3 characters long```", color=0xff0000)
					embed.set_thumbnail(url=theme.image_url())
					embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
					embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
					embed.set_image(url=theme.large_image_url())
					await send(luna, embed)

	@commands.command(name = "stopanimguild",
						usage="",
						description = "Stops the guild animation")
	async def stopanimguild(self, luna, *, name:str = None):
		await luna.message.delete()
		global start_animation
		start_animation = False
		embed = discord.Embed(title="Animguild", description="```\nStopped the animation```", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "cyclenick",
						usage="<name>",
						description = "Animates the nickname")
	async def cyclenick(self, luna, *, text):
		await luna.message.delete()
		embed = discord.Embed(title="Cyclenick", description=f"```\nAnimating: {text}```", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)
		global cycling
		cycling = True
		while cycling:
			name = ""
			for letter in text:
				name = name + letter
				await luna.message.author.edit(nick=name)


	@commands.command(name = "stopcyclenick",
						usage="",
						description = "Stops the nickname animation")
	async def stopcyclenick(self, luna):
		await luna.message.delete()
		global cycling
		cycling = False
		embed = discord.Embed(title="Cyclenick", description="```\nStopped the animation```", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "cyclegroup",
						usage="<name>",
						description = "Animates the group name")
	async def cyclegroup(self, luna, *, text):
		await luna.message.delete()
		embed = discord.Embed(title="Cyclegroup", description=f"```\nAnimating: {text}```", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)
		global cycling_group
		cycling_group = True
		while cycling:
			name = ""
			for letter in text:
				name = name + letter
				await luna.message.channel.edit(name=name)


	@commands.command(name = "stopcyclegroup",
						usage="",
						description = "Stops the group animation")
	async def stopcyclegroup(self, luna):
		await luna.message.delete()
		global cycling_group
		cycling_group = False
		embed = discord.Embed(title="Cyclegroup", description="```\nStopped the animation```", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "virus",
				usage="[@member] <virus>",
				description = "Animated virus message")
	async def virus(self, luna, user: discord.Member = None, *, virus: str = "trojan"):
		user = user or luna.author
		list = (
			f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
			f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
			f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
			f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
			f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
			f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
			f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
			f"``Successfully downloaded {virus}-virus.exe``",
			"``Injecting virus.   |``",
			"``Injecting virus..  /``",
			"``Injecting virus... -``",
			f"``Successfully Injected {virus}-virus.exe into {user.name}``",
		)
		for i in list:
			await asyncio.sleep(1.5)
			await luna.message.edit(content=i)

	@commands.command(name = "cathi",
						usage="[text]",
						description = "Cute cat animation")
	async def cathi(self, luna, *, text: str = "Hi..."):
		list = (
			"""ຸ 　　　＿＿_＿＿
	　／　／　  ／|"
	　|￣￣￣￣|　|
	　|　　　　|／
	　￣￣￣￣""",
			f"""ຸ 　　　{text}
	　   　∧＿∧＿_
	　／(´･ω･`)  ／＼
	／|￣￣￣￣|＼／
	　|　　　　|／
	　￣￣￣￣""",
		)
		for i in range(3):
			for cat in list:
				await asyncio.sleep(2)
				await luna.message.edit(content=cat)

	@commands.command(name = "flop",
						usage="",
						description = "Flop animation")
	async def flop(self, luna):
		list = (
			"(   ° - °) (' - '   )",
			"(\\\° - °)\ (' - '   )",
			"(—°□°)— (' - '   )",
			"(╯°□°)╯(' - '   )",
			"(╯°□°)╯︵(\\\ .o.)\\",
		)
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

	@commands.command(name = "poof",
						usage="",
						description = "Poof animation")
	async def poof(self, luna):
		list = ("(   ' - ')", "' - ')", "- ')", "')", ")", "*poofness*")
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

	@commands.command(name = "boom",
						usage="",
						description = "Boom animation")
	async def boom(self, luna):
		list = (
			"```THIS MESSAGE WILL SELFDESTRUCT IN 5```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 4```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 3```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 2```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 1```",
			"```THIS MESSAGE WILL SELFDESTRUCT IN 0```",
			"💣",
			"💥",
		)
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

	@commands.command(name = "tableflip",
						usage="",
						description = "Tableflip/rage animation")
	async def tableflip(self, luna):
		list = (
			"`(\°-°)\  ┬─┬`",
			"`(\°□°)\  ┬─┬`",
			"`(-°□°)-  ┬─┬`",
			"`(╯°□°)╯    ]`",
			"`(╯°□°)╯     ┻━┻`",
			"`(╯°□°)╯       [`",
			"`(╯°□°)╯          ┬─┬`",
			"`(╯°□°)╯                 ]`",
			"`(╯°□°)╯                  ┻━┻`",
			"`(╯°□°)╯                         [`",
			"`(\°-°)\                               ┬─┬`",
		)
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

	@commands.command(name = "unflip",
						usage="",
						description = "Unflip animation")
	async def tableflip(self, luna):
		list = (
			"`(\°-°)\  ┻━┻`",
			"`(\°□°)\  ┻━┻`",
			"`(-°□°)-  ┻━┻`",
			"`(-°□°)-  ]`",
			"`(\°-°)\  ┬─┬`",
		)
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

	@commands.command(name = "warning",
						usage="",
						description = "System overload animation")
	async def warning(self, luna):
		list = (
			"`LOAD !! WARNING !! SYSTEM OVER`",
			"`OAD !! WARNING !! SYSTEM OVERL`",
			"`AD !! WARNING !! SYSTEM OVERLO`",
			"`D !! WARNING !! SYSTEM OVERLOA`",
			"`! WARNING !! SYSTEM OVERLOAD !`",
			"`WARNING !! SYSTEM OVERLOAD !!`",
			"`ARNING !! SYSTEM OVERLOAD !! W`",
			"`RNING !! SYSTEM OVERLOAD !! WA`",
			"`NING !! SYSTEM OVERLOAD !! WAR`",
			"`ING !! SYSTEM OVERLOAD !! WARN`",
			"`NG !! SYSTEM OVERLOAD !! WARNI`",
			"`G !! SYSTEM OVERLOAD !! WARNIN`",
			"`!! SYSTEM OVERLOAD !! WARNING`",
			"`! SYSTEM OVERLOAD !! WARNING !`",
			"`SYSTEM OVERLOAD !! WARNING !!`",
			"`IMMINENT SHUT-DOWN IN 0.5 SEC!`",
			"`WARNING !! SYSTEM OVERLOAD !!`",
			"`IMMINENT SHUT-DOWN IN 0.2 SEC!`",
			"`SYSTEM OVERLOAD !! WARNING !!`",
			"`IMMINENT SHUT-DOWN IN 0.01 SEC!`",
			"`SHUT-DOWN EXIT ERROR ¯\\(｡･益･)/¯`",
			"`CTRL + R FOR MANUAL OVERRIDE..`",
		)
		for i in list:
			await asyncio.sleep(2)
			await luna.message.edit(content=i)

bot.add_cog(AnimatedCog(bot))
class DumpCog(commands.Cog, name="Dump commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "alldump",
						usage="<channel>",
						description = "Dump all from a channel")
	async def alldump(self, luna, channel:discord.TextChannel):
		await luna.message.delete()
		if not files.file_exist(f"Luna/dumping/all/{channel.guild.name}/{channel.name}", documents=True):
			files.create_folder(f"Luna/dumping/all/{channel.guild.name}/{channel.name}", documents=True)
		try:
			prints.event(f"Dumping all from {channel.name} ({channel.guild.name})")
			await embed_builder(luna, title="Dumping", description=f"```\nEvent\n\nDumping all from {channel.mention} ({channel.guild.name})...```")
			async for message in channel.history(limit=None):
				if message.attachments:
					for attachment in message.attachments:
						r = requests.get(attachment.url, stream=True)
						open(os.path.join(files.documents(), f'Luna/dumping/all/{channel.guild.name}/{channel.name}/{attachment.filename}'), 'wb').write(r.content)
			prints.message(f"Dumped all from {channel.name} ({channel.guild.name})")
			await embed_builder(luna, title="Dumping", description=f"```\nInfo\n\nDumped all from {channel.mention} ({channel.guild.name})```")
		except Exception as e:
			await error_builder(luna, e)

	@commands.command(name = "imgdump",
						usage="<channel>",
						description = "Dump images from a channel")
	async def imgdump(self, luna, channel:discord.TextChannel):
		await luna.message.delete()
		if not files.file_exist(f"Luna/dumping/images/{channel.guild.name}/{channel.name}", documents=True):
			files.create_folder(f"Luna/dumping/images/{channel.guild.name}/{channel.name}", documents=True)
		try:
			prints.event(f"Dumping images from {channel.name} ({channel.guild.name})")
			await embed_builder(luna, title="Dumping", description=f"```\nEvent\n\nDumping images from {channel.mention} ({channel.guild.name})...```")
			async for message in channel.history(limit=None):
				if message.attachments:
					for attachment in message.attachments:
						if attachment.url.endswith(".png") or attachment.url.endswith(".jpg") or attachment.url.endswith(".jpeg"):
							r = requests.get(attachment.url, stream=True)
							open(os.path.join(files.documents(), f'Luna/dumping/images/{channel.guild.name}/{channel.name}/{attachment.filename}'), 'wb').write(r.content)
			prints.message(f"Dumped images from {channel.name} ({channel.guild.name})")
			await embed_builder(luna, title="Dumping", description=f"```\nInfo\n\nDumped images from {channel.mention} ({channel.guild.name})```")
		except Exception as e:
			await error_builder(luna, e)

	@commands.command(name = "audiodump",
						usage="<channel>",
						description = "Dump audio from a channel")
	async def audiodump(self, luna, channel:discord.TextChannel):
		await luna.message.delete()
		if not files.file_exist(f"Luna/dumping/audio/{channel.guild.name}/{channel.name}", documents=True):
			files.create_folder(f"Luna/dumping/audio/{channel.guild.name}/{channel.name}", documents=True)
		try:
			prints.event(f"Dumping audio from {channel.name} ({channel.guild.name})")
			await embed_builder(luna, title="Dumping", description=f"```\nEvent\n\nDumping audio from {channel.mention} ({channel.guild.name})...```")
			async for message in channel.history(limit=None):
				if message.attachments:
					for attachment in message.attachments:
						if attachment.url.endswith(".mp3"):
							r = requests.get(attachment.url, stream=True)
							open(os.path.join(files.documents(), f'Luna/dumping/audio/{channel.guild.name}/{channel.name}/{attachment.filename}'), 'wb').write(r.content)
			prints.message(f"Dumped audio from {channel.name} ({channel.guild.name})")
			await embed_builder(luna, title="Dumping", description=f"```\nInfo\n\nDumped audio from {channel.mention} ({channel.guild.name})```")
		except Exception as e:
			await error_builder(luna, e)

	@commands.command(name = "videodump",
						usage="<channel>",
						description = "Dump videos from a channel")
	async def videodump(self, luna, channel:discord.TextChannel):
		await luna.message.delete()
		if not files.file_exist(f"Luna/dumping/videos/{channel.guild.name}/{channel.name}", documents=True):
			files.create_folder(f"Luna/dumping/videos/{channel.guild.name}/{channel.name}", documents=True)
		try:
			prints.event(f"Dumping videos from {channel.name} ({channel.guild.name})")
			await embed_builder(luna, title="Dumping", description=f"```\nEvent\n\nDumping videos from {channel.mention} ({channel.guild.name})...```")
			async for message in channel.history(limit=None):
				if message.attachments:
					for attachment in message.attachments:
						if attachment.url.endswith(".mp4") or attachment.url.endswith(".mov"):
							r = requests.get(attachment.url, stream=True)
							open(os.path.join(files.documents(), f'Luna/dumping/videos/{channel.guild.name}/{channel.name}/{attachment.filename}'), 'wb').write(r.content)
			prints.message(f"Dumped videos from {channel.name} ({channel.guild.name})")
			await embed_builder(luna, title="Dumping", description=f"```\nInfo\n\nDumped videos from {channel.mention} ({channel.guild.name})```")
		except Exception as e:
			await error_builder(luna, e)

	@commands.command(name = "textdump",
						usage="<channel>",
						description = "Dump text from a channel")
	async def textdump(self, luna, channel:discord.TextChannel):
		await luna.message.delete()
		if not files.file_exist(f"Luna/dumping/text/{channel.guild.name}/{channel.name}", documents=True):
			files.create_folder(f"Luna/dumping/text/{channel.guild.name}/{channel.name}", documents=True)
		try:
			prints.event(f"Dumping text from {channel.name} ({channel.guild.name})")
			await embed_builder(luna, title="Dumping", description=f"```\nEvent\n\nDumping last 1000 messages from {channel.mention} ({channel.guild.name})...```")
			text = ""
			async for message in channel.history(limit=1000):
				text += f"{message.author.name}#{message.author.discriminator}: {message.content}\n"
			open(os.path.join(files.documents(), f'Luna/dumping/text/{channel.guild.name}/{channel.name}/{channel.name}.txt'), 'w', encoding='utf-8').write(text)
			prints.message(f"Dumped text from {channel.name} ({channel.guild.name})")
			await embed_builder(luna, title="Dumping", description=f"```\nInfo\n\nDumped last 1000 messages from {channel.mention} ({channel.guild.name})```")
		except Exception as e:
			await error_builder(luna, e)

	@commands.command(name = "emojidump",
						usage="<guild>",
						description = "Dump all emojis from a guild")
	async def emojidump(self, luna, guild:discord.Guild):
		await luna.message.delete()
		if not files.file_exist(f"Luna/dumping/emojis/{guild.name}", documents=True):
			files.create_folder(f"Luna/dumping/emojis/{guild.name}", documents=True)
		try:
			prints.event(f"Dumping emojis from {guild.name}")
			await embed_builder(luna, title="Dumping", description=f"```\nEvent\n\nDumping emojis from {guild.name}...```")
			for emoji in guild.emojis:
				url = str(emoji.url)
				name = str(emoji.name)
				r = requests.get(url, stream=True)
				if '.png' in url:
					open(os.path.join(files.documents(), f'Luna/dumping/emojis/{guild.name}/{name}.png'), 'wb').write(r.content)
				elif '.gif' in url:
					open(os.path.join(files.documents(), f'Luna/dumping/emojis/{guild.name}/{name}.gif'), 'wb').write(r.content)
			prints.message(f"Dumped emojis from {guild.name}")
			await embed_builder(luna, title="Dumping", description=f"```\nInfo\n\nDumped emojis from {guild.name}```")
		except Exception as e:
			await error_builder(luna, e)

	@commands.command(name = "emojidownload",
						usage="<guild> <emoji>",
						description = "Download a emoji")
	async def emojidownload(self, luna, guild:discord.Guild, emoji:discord.Emoji):
		await luna.message.delete()
		if not files.file_exist(f"Luna/dumping/emojis/{guild.name}", documents=True):
			files.create_folder(f"Luna/dumping/emojis/{guild.name}", documents=True)
		try:
			prints.event(f"Downloading emoji from {guild.name}")
			await embed_builder(luna, title="Downloading", description=f"```\nEvent\n\nDownloading emoji from {guild.name}...```")
			url = str(emoji.url)
			name = str(emoji.name)
			r = requests.get(url, stream=True)
			if '.png' in url:
				open(os.path.join(files.documents(), f'Luna/emojis/{guild.name}/{name}.png'), 'wb').write(r.content)
			elif '.gif' in url:
				open(os.path.join(files.documents(), f'Luna/emojis/{guild.name}/{name}.gif'), 'wb').write(r.content)
			prints.message(f"Downloaded emoji from {guild.name}")
			await embed_builder(luna, title="Downloading", description=f"```\nInfo\n\nDownloaded emoji from {guild.name}```")
		except Exception as e:
			await error_builder(luna, e)

	@commands.command(name = "avatardump",
						usage="<guild>",
						description = "Dump avatars from a guild")
	async def avatardump(self, luna, guild:discord.Guild):
		await luna.message.delete()
		if not files.file_exist(f"Luna/dumping/avatars/{guild.name}", documents=True):
			files.create_folder(f"Luna/dumping/avatars/{guild.name}", documents=True)
		try:
			prints.event(f"Dumping avatars from {guild.name}")
			await embed_builder(luna, title="Dumping", description=f"```\nEvent\n\nDumping avatars from {guild.name}...```")
			for member in guild.members:
				url = str(member.avatar_url)
				name = str(member.name)
				r = requests.get(url, stream=True)
				if '.png' in url:
					open(os.path.join(files.documents(), f'Luna/dumping/avatars/{guild.name}/{name}.png'), 'wb').write(r.content)
				elif '.gif' in url:
					open(os.path.join(files.documents(), f'Luna/dumping/avatars/{guild.name}/{name}.gif'), 'wb').write(r.content)
			prints.message(f"Dumped avatars from {guild.name}")
			await embed_builder(luna, title="Dumping", description=f"```\nInfo\n\nDumped avatars from {guild.name}```")
		except Exception as e:
			await error_builder(luna, e)

	@commands.command(name = "channeldump",
						usage="<guild>",
						description = "Dump channels from a guild")
	async def channelnamesdump(self, luna, guild:discord.Guild):
		await luna.message.delete()
		if not files.file_exist(f"Luna/dumping/channels/{guild.name}", documents=True):
			files.create_folder(f"Luna/dumping/channels/{guild.name}", documents=True)
		try:
			prints.event(f"Dumping channel names from {guild.name}")
			await embed_builder(luna, title="Dumping", description=f"```\nEvent\n\nDumping channel names from {guild.name}...```")
			for channel in guild.channels:
				name = str(channel.name)
				with open(os.path.join(files.documents(), f'Luna/dumping/channels/{guild.name}/{name}.txt'), 'w') as f:
					f.write(name)
			prints.message(f"Dumped channel names from {guild.name}")
			await embed_builder(luna, title="Dumping", description=f"```\nInfo\n\nDumped channel names from {guild.name}```")
		except Exception as e:
			await error_builder(luna, e)

bot.add_cog(DumpCog(bot))

# ////////////////////////////////////////////////////////////////////

def zalgoText(string):
        result = ''

        for char in string:
            for i in range(0, random.randint(20, 40)):
                randBytes = random.randint(0x300, 0x36f).to_bytes(2, 'big')
                char += randBytes.decode('utf-16be')
                i + 1
            result += char
        return result

class TextCog(commands.Cog, name="Text commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "encode",
					usage="",
					description = "Encoding text commands")
	async def encode(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)

		cog = self.bot.get_cog('Encode commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		embed = discord.Embed(title="Encode Text", url=theme.title_url(), description=f"{theme.description()}```\n{helptext}```", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "decode",
					usage="",
					description = "Decoding text commands")
	async def decode(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)

		cog = self.bot.get_cog('Decode commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		embed = discord.Embed(title="Decode Text", url=theme.title_url(), description=f"{theme.description()}```\n{helptext}```", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "embed",
					usage="<text>",
					description = "Text in a embed")
	async def embed(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=theme.hex_color())
		await luna.send(embed=embed)
	
	@commands.command(name = "embed_title",
					usage="<text>",
					description = "Text in a embed")
	async def embed_title(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title() ,description=f"{text}", color=theme.hex_color())
		await luna.send(embed=embed)

	@commands.command(name = "embed_thumbnail",
					usage="<text>",
					description = "Text in a embed")
	async def embed_thumbnail(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		await luna.send(embed=embed)

	@commands.command(name = "embed_footer",
					usage="<text>",
					description = "Text in a embed")
	async def embed_footer(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		await luna.send(embed=embed)

	@commands.command(name = "embed_author",
					usage="<text>",
					description = "Text in a embed")
	async def embed_author(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=theme.hex_color())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		await luna.send(embed=embed)

	@commands.command(name = "embed_image",
					usage="<text>",
					description = "Text in a embed")
	async def embed_image(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=theme.hex_color())
		embed.set_image(url=theme.large_image_url())
		await luna.send(embed=embed)

	@commands.command(name = "embed_all",
					usage="<text>",
					description = "Text in a embed")
	async def embed_all(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(description=f"{text}", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await luna.send(embed=embed)

	@commands.command(name = "ascii",
					usage="<text>",
					description = "Ascii text")
	async def ascii(self, luna, *, text:str):
		await luna.message.delete()
		r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
		if len('```' + r + '```') > 2000:
			return
		await luna.send(f"```{r}```")

	@commands.command(name = "vape",
					usage="<text>",
					aliases=['vaporwave'],
					description = "Vaporwave text")
	async def vape(self, luna, *, text:str):
		await luna.message.delete()
		text = text.replace('a', 'ａ').replace('A', 'Ａ').replace('b', 'ｂ') \
			.replace('B', 'Ｂ').replace('c', 'ｃ').replace('C', 'Ｃ') \
			.replace('d', 'ｄ').replace('D', 'Ｄ').replace('e', 'ｅ') \
			.replace('E', 'Ｅ').replace('f', 'ｆ').replace('F', 'Ｆ') \
			.replace('g', 'ｇ').replace('G', 'Ｇ').replace('h', 'ｈ') \
			.replace('H', 'Ｈ').replace('i', 'ｉ').replace('I', 'Ｉ') \
			.replace('j', 'ｊ').replace('J', 'Ｊ').replace('k', 'ｋ') \
			.replace('K', 'Ｋ').replace('l', 'ｌ').replace('L', 'Ｌ') \
			.replace('m', 'ｍ').replace('M', 'Ｍ').replace('n', 'ｎ') \
			.replace('N', 'Ｎ').replace('o', 'ｏ').replace('O', 'Ｏ') \
			.replace('p', 'ｐ').replace('P', 'Ｐ').replace('q', 'ｑ') \
			.replace('Q', 'Ｑ').replace('r', 'ｒ').replace('R', 'Ｒ') \
			.replace('s', 'ｓ').replace('S', 'Ｓ').replace('t', 'ｔ') \
			.replace('T', 'Ｔ').replace('u', 'ｕ').replace('U', 'Ｕ') \
			.replace('v', 'ｖ').replace('V', 'Ｖ').replace('w', 'ｗ') \
			.replace('W', 'Ｗ').replace('x', 'ｘ').replace('X', 'Ｘ') \
			.replace('1', '１').replace('2', '２').replace('3', '３') \
			.replace('4', '４').replace('5', '５').replace('6', '６').replace(' ', '　') \
			.replace('7', '７').replace('8', '８').replace('9', '９').replace('0', '０') \
			.replace('?', '？').replace('.', '．').replace('!', '！').replace('[', '［') \
			.replace(']', '］').replace('{', '｛').replace('}', '｝').replace('=', '＝') \
			.replace('(', '（').replace(')', '）').replace('&', '＆').replace('%', '％').replace('"', '＂') \
			.replace('y', 'ｙ').replace('Y', 'Ｙ').replace('z', 'ｚ').replace('Z', 'Ｚ')
		await luna.send(f'{text}')

	@commands.command(name = "zalgo",
					usage="<text>",
					description = "Zalgo text")
	async def zarlgo(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(zalgoText(text))

	@commands.command(name = "reverse",
					usage="<text>",
					description = "Reverse given text")
	async def reverse(luna, *, text):
		await luna.message.delete()
		text = text[::-1]
		await luna.send(text)

	@commands.command(name = "bold",
					usage="<text>",
					description = "Bold text format")
	async def bold(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"**{text}**")

	@commands.command(name = "spoiler",
					usage="<text>",
					description = "Spoiler text format")
	async def spoiler(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"||{text}||")

	@commands.command(name = "underline",
					usage="<text>",
					description = "Underline text format")
	async def underline(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"__{text}__")

	@commands.command(name = "strike",
					usage="<text>",
					description = "Strike text format")
	async def strike(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"~~{text}~~")

	@commands.command(name = "css",
					usage="<text>",
					description = "CSS text format")
	async def css(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```css\n{text}\n```")
	
	@commands.command(name = "brainfuck",
					usage="<text>",
					description = "Brainfuck text format")
	async def brainfuck(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```brainfuck\n{text}\n```")

	@commands.command(name = "md",
					usage="<text>",
					description = "MD text format")
	async def md(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```md\n{text}\n```")

	@commands.command(name = "fix",
					usage="<text>",
					description = "Fix text format")
	async def fix(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```fix\n{text}\n```")

	@commands.command(name = "glsl",
					usage="<text>",
					description = "Glsl text format")
	async def glsl(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```glsl\n{text}\n```")

	@commands.command(name = "diff",
					usage="<text>",
					description = "Diff text format")
	async def diff(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```diff\n{text}\n```")
		
	@commands.command(name = "bash",
					usage="<text>",
					description = "Bash text format")
	async def bash(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```bash\n{text}\n```")
		
	@commands.command(name = "cs",
					usage="<text>",
					description = "CS text format")
	async def cs(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```cs\n{text}\n```")

	@commands.command(name = "ini",
					usage="<text>",
					description = "Ini text format")
	async def ini(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```ini\n{text}\n```")

	@commands.command(name = "asciidoc",
					usage="<text>",
					description = "Asciidoc text format")
	async def asciidoc(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```asciidoc\n{text}\n```")

	@commands.command(name = "autohotkey",
					usage="<text>",
					description = "Autohotkey text format")
	async def autohotkey(self, luna, *, text:str):
		await luna.message.delete()
		await luna.send(f"```autohotkey\n{text}\n```")

bot.add_cog(TextCog(bot))
class ImageCog(commands.Cog, name="Image commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	# ///////////////////////////////////////////////////////////////
	# Avatar commands

	@commands.command(name = "avatar",
					usage="<@member>",
					aliases=["av"],
					description = "Send the avatar")
	async def av(self, luna, user_id=None):
		await luna.message.delete()
		if user_id == None:
			user = await self.bot.fetch_user(bot.user.id)
		elif "<@!" and ">" in user_id:
			user_id = user_id.replace("<@!", "").replace(">", "")
			user = await self.bot.fetch_user(user_id)
		else:
			user = await self.bot.fetch_user(user_id)
		embed = discord.Embed(title=f"{user}'s avatar", color=theme.hex_color())
		embed.set_image(url=user.avatar_url)
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		await send(luna, embed)

	@commands.command(name = "avatart",
					usage="<@member> <text>",
					asliases=["avt"],
					description = "Send the avatar")
	async def avatart(self, luna, member: discord.Member, *, text: str):
		await luna.message.delete()
		embed = discord.Embed(title=text,color=theme.hex_color())
		embed.set_image(url=member.avatar_url)
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		await send(luna, embed)

	@commands.command(name = "searchav",
					usage="<@member>",
					description = "Search link of the avatar")
	async def searchav(self, luna, member: discord.Member):
		await luna.message.delete()
		embed = discord.Embed(title=f"Search link for {member}'s avatar",description=f"https://images.google.com/searchbyimage?image_url={member.avatar_url}" ,color=theme.hex_color())
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		await send(luna, embed)

	@commands.command(name = "linkav",
					usage="<@member>",
					description = "Link of the avatar")
	async def linkav(self, luna, member: discord.Member):
		await luna.message.delete()
		embed = discord.Embed(title=f"Link for {member}'s avatar",description=f"{member.avatar_url}" ,color=theme.hex_color())
		embed.set_thumbnail(url=member.avatar_url)
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		await send(luna, embed)

	@commands.command(name = "stealav",
					usage="<@member>",
					description = "Steal the avatar")
	async def stealav(self, luna, member: discord.Member):
		await luna.message.delete()
		url = member.avatar_url
		if configs.password() == "password-here":
			prints.error("You didnt put your password in the config.json file")
		else:
			configs.password()
			with open('PFP-1.png', 'wb') as f:
				r = requests.get(url, stream=True)
				for block in r.iter_content(1024):
					if not block:
						break
					f.write(block)
		try:
			with open('PFP-1.png', 'rb') as f:
				await self.bot.user.edit(password=configs.password(), avatar=f.read())
			embed = discord.Embed(description=f"```\nStole {member}'s avatar!```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)
		except discord.HTTPException as e:
			prints.error(f"{e}")

	@commands.command(name = "setavatar",
					usage="<url>",
					description = "Set your avatar")
	async def setavatar(self, luna, url: str):
		await luna.message.delete()
		if configs.password() == "password-here":
			prints.error("You didnt put your password in the config.json file")
		else:
			configs.password()
			with open('PFP-1.png', 'wb') as f:
				r = requests.get(url, stream=True)
				for block in r.iter_content(1024):
					if not block:
						break
					f.write(block)
		try:
			with open('PFP-1.png', 'rb') as f:
				await self.bot.user.edit(password=configs.password(), avatar=f.read())
			embed = discord.Embed(description=f"```\nSet new avatar to »\n{url}```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)
		except discord.HTTPException as e:
			prints.error(f"{e}")

	@commands.command(name = "invisav",
					usage="",
					description = "Invisible avatar")
	async def invisav(self, luna):
		await luna.message.delete()
		url = "https://gauginggadgets.com/wp-content/uploads/2020/07/InvisibleProfileImage.png"
		if configs.password() == "password-here":
			prints.error("You didnt put your password in the config.json file")
		else:
			configs.password()
			with open('PFP-1.png', 'wb') as f:
				r = requests.get(url, stream=True)
				for block in r.iter_content(1024):
					if not block:
						break
					f.write(block)
		try:
			with open('PFP-1.png', 'rb') as f:
				await self.bot.user.edit(password=configs.password(), avatar=f.read())
			embed = discord.Embed(description=f"```\nSet your avatar to invisible```" ,color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)
		except discord.HTTPException as e:
			prints.error(f"{e}")

	# ///////////////////////////////////////////////////////////////
	# Fun image commands
        
	@commands.command(name = "dog",
					usage="",
					description = "Send a random dog")
	async def dog(self, luna):
		await luna.message.delete()
		r = requests.get("https://dog.ceo/api/breeds/image/random").json()
		embed = discord.Embed(title=theme.title(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=str(r['message']))
		await send(luna, embed)

	@commands.command(name = "fox",
					usage="",
					description = "Send a random fox")
	async def fox(self, luna):
		await luna.message.delete()
		r = requests.get('https://randomfox.ca/floof/').json()
		embed = discord.Embed(title=theme.title(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=str(r['image']))
		await send(luna, embed)
			
	@commands.command(name = "cat",
					usage="",
					description = "Send a random cat")
	async def cat(self, luna):
		await luna.message.delete()
		r = requests.get("https://api.thecatapi.com/v1/images/search").json()
		embed = discord.Embed(title=theme.title(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=str(r[0]["url"]))
		await send(luna, embed)

	@commands.command(name = "sadcat",
					usage="",
					description = "Send a random sad cat")
	async def sadcat(self, luna):
		await luna.message.delete()
		r = requests.get("https://api.alexflipnote.dev/sadcat").json()
		embed = discord.Embed(title=theme.title(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=str(r['file']))
		await send(luna, embed)

	@commands.command(name = "waifu",
					usage="",
					description = "Send a random waifu")
	async def waifu(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/waifu").json()
		embed = discord.Embed(title=theme.title(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=str(r['url']))
		await send(luna, embed)

	# ///////////////////////////////////////////////////////////////
	# Image commands

	@commands.command(name = "wallpaper",
					usage="",
					description = "Send a random anime wallpaper")
	async def wallpaper(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/wallpaper").json()
		embed = discord.Embed(title=theme.title(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=str(r['url']))
		await send(luna, embed)
	
	@commands.command(name = "wide",
					usage="<@member>",
					description = "Wide profile picture")
	async def wide(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/wide?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "trumptweet",
					usage="<text>",
					description = "Create a Trump tweet")
	async def trumptweet(self, luna, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=trumptweet&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "bidentweet",
					usage="<text>",
					description = "Create a Biden tweet")
	async def bidentweet(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f'https://api.popcatdev.repl.co/biden?text={str(urllib.parse.quote(text))}')
		await send(luna, embed)

	@commands.command(name = "tweet",
					usage="<name> <text>",
					description = "Create a tweet")
	async def tweet(self, luna, name, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=tweet&username={name}&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "supreme",
					usage="<text>",
					description = "Custom supreme logo")
	async def supreme(self, luna, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=supreme&text={str(urllib.parse.quote(text))}').json()['url']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f'{request}')
		await send(luna, embed)

	@commands.command(name = "changemymind",
					usage="<text>",
					description = "Changemymind meme")
	async def changemymind(self, luna, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=changemymind&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "phcomment",
					aliases=['pornhubcomment'],
					usage="<@member> <text>",
					description = "Pornhub comment")
	async def phcomment(self, luna, user: discord.User, *, text: str):
		await luna.message.delete()
		image_url = str(user.avatar_url).replace(".webp", ".png")
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=phcomment&image={image_url}&username={urllib.parse.quote(user.name)}&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "clyde",
					usage="<text>",
					description = "Custom Clyde message")
	async def clyde(self, luna, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://nekobot.xyz/api/imagegen?type=clyde&text={urllib.parse.quote(text)}')
		data = request.json()
		link = data['message']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "pikachu",
					usage="<text>",
					description = "Surprised Pikachu")
	async def pikachu(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://api.popcatdev.repl.co/pikachu?text={urllib.parse.quote(str(text))}")
		await send(luna, embed)

	@commands.command(name = "stonks",
					usage="<@member>",
					description = "Stonks!")
	async def stonks(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/stonks?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "notstonks",
					usage="<@member>",
					description = "Notstonks!")
	async def notstonks(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/stonks?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}&notstonks=true")
		await send(luna, embed)

	@commands.command(name = "emergencymeeting",
					usage="<text>",
					description = "Emergency meeting!")
	async def emergencymeeting(self, luna, *, text):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/emergencymeeting?text={urllib.parse.quote(text)}")
		await send(luna, embed)

	@commands.command(name = "eject",
					usage="<true/false> <color> <@member>",
					description = "Among Us")
	async def eject(self, luna, impostor: bool, crewmate: str, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/ejected?name={urllib.parse.quote(user.name)}&impostor={impostor}&crewmate={crewmate}")
		await send(luna, embed)

	@commands.command(name = "drip",
					usage="<@member>",
					description = "Drip meme")
	async def drip(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/drip?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "gun",
					usage="<@member>",
					description = "Gun meme")
	async def gun(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://api.popcatdev.repl.co/gun?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "ad",
					usage="<@member>",
					description = "Make yourself an ad")
	async def ad(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://api.popcatdev.repl.co/ad?image={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "alert",
					usage="<text>",
					description = "Iphone alert")
	async def alert(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://api.popcatdev.repl.co/alert?text={urllib.parse.quote(str(text))}")
		await send(luna, embed)

	@commands.command(name = "caution",
					usage="<text>",
					description = "Caution image")
	async def caution(self, luna, *, text:str):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://api.popcatdev.repl.co/caution?text={urllib.parse.quote(str(text))}")
		await send(luna, embed)

	@commands.command(name = "distractedbf",
					usage="<@boyfriend> <@woman> <@girlfriend>",
					description = "Distracted boyfriend meme")
	async def distractedbf(self, luna, boyfriend: discord.User, woman: discord.User, girlfriend: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/distractedbf?boyfriend={urllib.parse.quote(str(boyfriend.avatar_url).replace('webp', 'png'))}&woman={urllib.parse.quote(str(woman.avatar_url).replace('webp', 'png'))}&girlfriend={urllib.parse.quote(str(girlfriend.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "icanmilkyou",
					usage="<@member1> <@member2>",
					description = "ICanMilkYou")
	async def icanmilkyou(self, luna, user1: discord.User, user2: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/icanmilkyou?user1={urllib.parse.quote(str(user1.avatar_url).replace('webp', 'png'))}&user2={urllib.parse.quote(str(user2.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "heaven",
					usage="<@member>",
					description = "Heaven meme")
	async def heaven(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/heaven?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "dockofshame",
					usage="<@member>",
					description = "Heaven meme")
	async def dockofshame(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/dockofshame?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "firsttime",
					usage="<@member>",
					description = "First time? meme")
	async def firsttime(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://vacefron.nl/api/firsttime?user={urllib.parse.quote(str(user.avatar_url).replace('webp', 'png'))}")
		await send(luna, embed)

	@commands.command(name = "trash",
					usage="<@member>",
					description = "Trash meme")
	async def trash(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f'https://api.no-api-key.com/api/v2/trash?image={str(user.avatar_url).replace(".webp", ".png")}')
		await send(luna, embed)

	@commands.command(name = "simp",
					usage="<@member>",
					description = "Simp card")
	async def simp(self, luna, user: discord.User):
		await luna.message.delete()
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f'https://api.no-api-key.com/api/v2/simpcard?image={str(user.avatar_url).replace(".webp", ".png")}')
		await send(luna, embed)

	@commands.command(name = "wanted",
					usage="<@member>",
					description = "Wanted")
	async def wanted(self, luna, user: discord.User):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=wanted&url={str(user.avatar_url).replace(".webp", ".png")}')
		data = request.json()
		link = data['url']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "wasted",
					usage="<@member>",
					description = "GTA Wasted")
	async def wasted(self, luna, user: discord.User):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=wasted&url={str(user.avatar_url).replace(".webp", ".png")}')
		data = request.json()
		link = data['url']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "continued",
					usage="<@member>",
					description = "To be continued")
	async def continued(self, luna, user: discord.User):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=tobecontinued&url={str(user.avatar_url).replace(".webp", ".png")}')
		data = request.json()
		link = data['url']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "drake",
					usage="<no, yes>",
					description = "Drake yes and no meme")
	async def drake(self, luna, *, text:str):
		await luna.message.delete()
		text = text.split(', ')
		text1 = text[0]
		text2 = text[1]
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f'https://api.popcatdev.repl.co/drake?text1={str(urllib.parse.quote(text1))}&text2={str(urllib.parse.quote(text2))}')
		await send(luna, embed)

	@commands.command(name = "takemymoney",
					usage="<text1, text2>",
					description = "Take my money")
	async def takemymoney(self, luna, *, text:str):
		await luna.message.delete()
		text = text.split(', ')
		text1 = text[0]
		text2 = text[1]
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=f"https://api.memegen.link/images/money/{urllib.parse.quote(text1)}/{urllib.parse.quote(text2)}.png")
		await send(luna, embed)

	@commands.command(name = "pornhub",
					usage="<text1, text2>",
					description = "PornHub logo")
	async def pornhub(self, luna, *, text:str):
		await luna.message.delete()
		text = text.split(', ')
		text1 = text[0]
		text2 = text[1]
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=phlogo&text={str(urllib.parse.quote(text1))}&text2={str(urllib.parse.quote(text2))}')
		data = request.json()
		link = data['url']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=link)
		await send(luna, embed)

	@commands.command(name = "recaptcha",
					usage="<text>",
					description = "reCAPTCHA")
	async def recaptcha(self, luna, *, text:str):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=captcha&text={str(urllib.parse.quote(text))}')
		data = request.json()
		link = data['url']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=link)
		await send(luna, embed)

bot.add_cog(ImageCog(bot))
def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'
class TrollCog(commands.Cog, name="Troll commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "ghostping",
					usage="<@member>",
					aliases=['gp'],
					description = "Ghostping someone")
	async def ghostping(self, luna):
		await luna.message.delete()
        
	@commands.command(name = "empty",
					usage="",
					description = "Sends a empty message")
	async def empty(self, luna):
		await luna.message.delete()
		await luna.send("​")

	@commands.command(name = "copy",
					usage="<@member>",
					aliases=['copycat'],
					description = "Copy every message a member")
	async def copy(self, luna, member:discord.User):
		await luna.message.delete()
		global copycat
		copycat = member
		if configs.mode() == 2:
			sent = await luna.send(f"```ini\n[ {theme.title()} ]\n\nNow copying {copycat}\n\n[ {theme.footer()} ]```")
			await asyncio.sleep(configs.delete_timer())
			await sent.delete()
		else:
			embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"Now copying {copycat}", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			sent = await luna.send(embed=embed)
			await asyncio.sleep(configs.delete_timer())
			await sent.delete()

	@commands.command(name = "stopcopy",
					usage="",
					aliases=['stopcopycat'],
					description = "Stop copying a member")
	async def stopcopy(self, luna):
		await luna.message.delete()
		global copycat
		if copycat is None:
			if configs.mode() == 2:
				sent = await luna.send(f"```ini\n[ {theme.title()} ]\n\nNo one was getting copied\n\n[ {theme.footer()} ]```")
				await asyncio.sleep(configs.delete_timer())
				await sent.delete()
			else:
				embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"No one was getting copied", color=theme.hex_color())
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				sent = await luna.send(embed=embed)
				await asyncio.sleep(configs.delete_timer())
				await sent.delete()
			return

		if configs.mode() == 2:
			sent = await luna.send(f"```ini\n[ {theme.title()} ]\n\nStopped copying {copycat}\n\n[ {theme.footer()} ]```")
			copycat = None
			await asyncio.sleep(configs.delete_timer())
			await sent.delete()
		else:
			embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"Stopped copying {copycat}", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			sent = await luna.send(embed=embed)
			copycat = None
			await asyncio.sleep(configs.delete_timer())
			await sent.delete()

	@commands.command(name = "fakenitro",
					usage="[amount]",
					description = "Generate fake nitro links")
	async def fakenitro(self, luna, amount: int = None):
		await luna.message.delete()
		try:
			if amount is None:
				await luna.send(Nitro())
			else:
				for each in range(0, amount):
					await luna.send(Nitro())
		except Exception as e:
			await luna.send(f"Error: {e}")

	@commands.command(name = "trollnitro",
					usage="",
					description = "Send a used nitro link")
	async def trollnitro(self, luna):
		await luna.message.delete()
		await luna.send("https://discord.gift/6PWNmA6NTuRkejaP")

	@commands.command(name = "mreact",
					usage="",
					description = "Mass reacts on last message")
	async def mreact(self, luna):
		await luna.message.delete()
		messages = await luna.message.channel.history(limit=1).flatten()
		for message in messages:
			await message.add_reaction("😂")
			await message.add_reaction("😡")
			await message.add_reaction("🤯")
			await message.add_reaction("👍")
			await message.add_reaction("👎")
			await message.add_reaction("💯")
			await message.add_reaction("🍑")
			await message.add_reaction("❗")
			await message.add_reaction("🥳")
			await message.add_reaction("👏")
			await message.add_reaction("🔞")
			await message.add_reaction("🇫")
			await message.add_reaction("🥇")
			await message.add_reaction("🤔")
			await message.add_reaction("💀")
			await message.add_reaction("❤️")

	@commands.command(name = "fakenuke",
					usage="",
					description = "Fakenuke")
	async def fakenuke(self, luna):
		await luna.message.delete()
		message = await luna.send(content=':bomb: :bomb: Nuking this server in 5 :rotating_light:')
		await asyncio.sleep(1)
		await message.edit(content='0')
		await asyncio.sleep(1)
		await message.edit(content='1')
		await asyncio.sleep(1)
		await message.edit(content='2')
		await asyncio.sleep(1)
		await message.edit(content='3')
		await asyncio.sleep(1)
		await message.edit(content='4')
		await asyncio.sleep(1)
		await message.edit(content='This server will be destoyed now')
		await asyncio.sleep(1)
		await message.edit(content=':bomb:')
		await asyncio.sleep(1)
		await message.edit(content=':boom:')
		await asyncio.sleep(1)
		await message.edit(content='Shouldn\'t have even created it ig')
		await asyncio.sleep(1)
		await message.edit(content=':bomb: :bomb:')
		await asyncio.sleep(1)
		await message.edit(content=':boom: :boom:')
		await asyncio.sleep(1)
		await message.edit(content='You will wish you never lived to know about discord')
		await asyncio.sleep(1)
		await message.edit(content=':bomb: :bomb: :bomb:')
		await asyncio.sleep(1)
		await message.edit(content=':boom: :boom: :boom:')
		await asyncio.sleep(1)
		await message.edit(content='There it comes...')
		await asyncio.sleep(1)
		await message.edit(content='https://giphy.com/gifs/rick-roll-lgcUUCXgC8mEo')

bot.add_cog(TrollCog(bot))

class FunCog(commands.Cog, name="Fun commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "impersonate",
					usage="<@member> <message>",
					description = "Make them send your message")
	async def impersonate(self, luna, user: discord.User, *, message: str):
		await luna.message.delete()
		webhook = await luna.channel.create_webhook(name=user.name)
		await webhook.send(message, username=user.name, avatar_url=user.avatar_url)
		await webhook.delete()

	@commands.command(name = "shoot",
					usage="<@member>",
					description = "Shoot up someone")
	async def shoot(self, luna, user: discord.Member):
		await luna.message.delete()
		await embed_builder(luna, description=f"{user.mention},  got shot up!", large_image="https://media1.tenor.com/images/cfb7817a23645120d4baba2dcb9205e0/tenor.gif", thumbnail="None", footer="None")

	@commands.command(name = "feed",
					usage="<@member>",
					description = "Feed someone")
	async def feed(self, luna, user: discord.Member):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/feed").json()
		await embed_builder(luna, description=f"{luna.author.mention} feeds {user.mention}", large_image=str(r['url']), thumbnail="None", footer="None")

	@commands.command(name = "bite",
					usage="<@member>",
					description = "Bite someone")
	async def bite(self, luna, user: discord.Member):
		await luna.message.delete()
		gif_list = ["https://c.tenor.com/MKjNSLL4dGoAAAAC/bite-cute.gif", "https://c.tenor.com/aKzAQ_cFsFEAAAAC/arms-bite.gif", "https://c.tenor.com/4j3hMz-dUz0AAAAC/anime-love.gif", "https://c.tenor.com/TX6YHUnHJk4AAAAC/mao-amatsuka-gj-bu.gif"]
		await embed_builder(luna, description=f"{user.mention} got bitten by {luna.author.mention}!", large_image=random.choice(gif_list), thumbnail="None", footer="None")

	@commands.command(name = "kiss",
					usage="<@member>",
					description = "Kiss someone")
	async def kiss(self, luna, user: discord.Member):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/kiss").json()
		await embed_builder(luna, description=f"{user.mention} got kissed by {luna.author.mention}!", large_image=str(r['url']), thumbnail="None", footer="None")

	@commands.command(name = "hug",
					usage="<@member>",
					description = "Hug someone")
	async def hug(self, luna, user: discord.Member):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/hug").json()
		await embed_builder(luna, description=f"{user.mention} got hugged by {luna.author.mention}!", large_image=str(r['url']), thumbnail="None", footer="None")


	@commands.command(name = "pat",
					usage="<@member>",
					description = "Pat someone")
	async def pat(self, luna, user: discord.Member):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/pat").json()
		await embed_builder(luna, description=f"{luna.author.mention} pats {user.mention}", large_image=str(r['url']), thumbnail="None", footer="None")

	@commands.command(name = "slap",
					usage="<@member>",
					description = "Slap someone")
	async def slap(self, luna, user: discord.Member):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/slap").json()
		await embed_builder(luna, description=f"{luna.author.mention} slapped {user.mention}", large_image=str(r['url']), thumbnail="None", footer="None")

	@commands.command(name = "tickle",
					usage="<@member>",
					description = "Tickle someone")
	async def tickle(self, luna, user: discord.Member):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/tickle").json()
		await embed_builder(luna, description=f"{luna.author.mention} tickles {user.mention}", large_image=str(r['url']), thumbnail="None", footer="None")

	@commands.command(name = "fml",
					usage="",
					description = "Fuck my life")
	async def fml(self, luna):
		await luna.message.delete()
		request = requests.get(f'https://react.flawcra.cc/api/generation.php?type=fml')
		data = request.json()
		text = data['text']
		await embed_builder(luna, description=f"```\n{text}\n```")
        
	@commands.command(name = "gay",
					usage="[@member]",
					description = "Gay rate somebody")
	async def gay(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			user = luna.author
		number = random.randint(1, 100)
		await embed_builder(luna, title=f"{user}'s Gay Rate", description=f"{number}% Gay 🏳️‍🌈")

	@commands.command(name = "iq",
					usage="[@member]",
					description = "Somebody's IQ")
	async def iq(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			user = luna.author
		number = random.randint(1, 120)
		if number < 20:
			special = "\n\nQuite low, isn't it?"
		else:
			special = ""
		await embed_builder(luna, title=f"{user}'s IQ", description=f"{number}{special}")

	@commands.command(name = "love",
					usage="<@member> [@member]",
					description = "Love rate")
	async def love(self, luna, user1: discord.Member, user2: discord.Member = None):
		await luna.message.delete()
		if user2 is None:
			user2 = luna.author
		number = random.randint(1, 100)
		breakup = random.randint(1, 100)
		kids = random.randint(1, 100)
		embed = discord.Embed(title=f"{user1} ❤️ {user2}", description=f"{number}% fitted!\n{kids}% chance of them having kids!\n{breakup}% chance of them breaking up!", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "coronatest",
					usage="<@member>",
					description = "Test somebody for Corona")
	async def coronatest(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			member = luna.author
		else:
			member = user
		random.seed((member.id * 6) / 2)
		percent = random.randint(0, 100)
		embed = discord.Embed(title=f"{user}'s Corona Test", description=f'```\n{percent}% positive!\n``````\nResult\n\nOverall » {"Positive" if (percent > 50) else "Negative"}```', color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "8ball",
					usage="<question>",
					description = "Ask 8 Ball!")
	async def _8ball(self, luna, *, question:str):
		await luna.message.delete()
		responses = [
			'That is a resounding no',
			'It is not looking likely',
			'Too hard to tell',
			'It is quite possible',
			'That is a definite yes!',
			'Maybe',
			'There is a good chance'
		]
		answer = random.choice(responses)
		embed = discord.Embed(title="8 Ball", description=f"```\nQuestion\n\n{question}\n``````\nAnswer\n\n{answer}\n```", color=theme.hex_color())
		embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "slot",
					usage="",
					aliases=['slots'],
					description = "Play slots")
	async def slot(self, luna):
		await luna.message.delete()
		emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
		a = random.choice(emojis)
		b = random.choice(emojis)
		c = random.choice(emojis)
		slotmachine = f"**------------------\n| {a} | {b} | {c} |\n------------------\n\n{luna.author.name}**,"
		if (a == b == c):
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} All matchings, you won!", color=theme.hex_color())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			await send(luna, embed)
		elif (a == b) or (a == c) or (b == c):
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} 2 in a row, you won!", color=theme.hex_color())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			await send(luna, embed)
		else:
			embed = discord.Embed(title="Slot Machine", description=f"{slotmachine} No match, you lost!", color=theme.hex_color())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			await send(luna, embed)

	@commands.command(name = "dadjoke",
					usage="",
					description = "Dad jokes")
	async def dadjoke(self, luna):
		await luna.message.delete()
		request = requests.get(f'https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
		data = request.json()
		joke = data['joke']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f'```\n{joke}\n```', color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "joke",
					usage="",
					description = "Random jokes")
	async def dadjoke(self, luna):
		await luna.message.delete()
		request = requests.get(f'http://www.official-joke-api.appspot.com/random_joke')
		data = request.json()
		setup = data['setup']
		punchline = data['punchline']
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f'```\nSetup\n\n{setup}\n``````\nPunchline\n\n{punchline}\n```', color=theme.hex_color())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "coinflip",
					usage="",
					description = "Flip a coin")
	async def coinflip(self, luna):
		await luna.message.delete()
		lista = ['head', 'tails']
		coin = random.choice(lista)
		try:
			if coin == 'head':
				await embed_builder(luna, title="Head", thumbnail="https://webstockreview.net/images/coin-clipart-dime-6.png")
			else:
				await embed_builder(luna, title="Tails", thumbnail="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
		except discord.HTTPException:
			if coin == 'head':
				await luna.send("```\nCoinflip » Head```")
			else:
				await luna.send("```\nCoinflip » Tails```")

	@commands.command(name = "prntsc",
						usage="",
						description = "Send a random prnt.sc")
	async def prntsc(self, luna):
		await luna.message.delete()
		await luna.send(Randprntsc())

	@commands.command(name = "farmer",
						usage="",
						description = "Dank Memer farmer")
	async def farmer(self, luna):
		await luna.message.delete()
		global farming
		farming = True
		while farming:
			await luna.send("pls beg")
			await asyncio.sleep(3)
			await luna.send("pls deposit all")
			await asyncio.sleep(42)

	@commands.command(name = "afarmer",
						usage="",
						description = "Advanced Dank Memer farmer")
	async def afarmer(self, luna):
		await luna.message.delete()
		global farming
		farming = True
		while farming:
			await luna.send("pls beg")
			await asyncio.sleep(3)
			await luna.send("pls deposit all")
			await asyncio.sleep(3)
			await luna.send("pls postmeme")
			await asyncio.sleep(3)
			await luna.send("n")
			await asyncio.sleep(3)
			await luna.send("pls fish")
			await asyncio.sleep(33)


	@commands.command(name = "stopfarmer",
						usage="",
						description = "Stops the Dank Memer farmer")
	async def stopfarmer(self, luna):
		await luna.message.delete()
		global farming
		farming = False

bot.add_cog(FunCog(bot))

class ToolsCog(commands.Cog, name="Tools commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "note",
					aliases=['newnote'],
					usage="<name> <text>",
					description = "Create a note")
	async def note(self, luna, name:str, *, text:str):
		await luna.message.delete()

		if files.file_exist(f"Luna/notes/{name}.txt", documents=True):
			if configs.error_log() == "console":
				prints.error(f"A note already exists with the name » {color.purple(name)}")
			else:
				embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nA note already exists with the name » {name}```", color=0xff0000)
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)
		else:
			file = open(os.path.join(files.documents(), f"Luna/notes/{name}.txt"), "w")
			file.write(str(text))
			file.close()
			prints.message(f"Created note » {color.purple(name)}")
			embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"```\nCreated note » {name}```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "editnote",
					usage="<name> <name>",
					description = "Edit the note name")
	async def editnote(self, luna, name:str, themename:str):
		await luna.message.delete()

		if not files.file_exist(f"Luna/notes/{name}.txt", documents=True):
			if configs.error_log() == "console":
				prints.error(f"No note exists with the name » {color.purple(name)}")
			else:
				embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nNo note exists with the name » {name}```", color=0xff0000)
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)
		else:
			os.rename(os.path.join(files.documents(), f"Luna/notes/{name}.txt"),os.path.join(files.documents(), f"Luna/notes/{themename}.txt"))
			prints.message(f"Edited note {name} to » {color.purple(themename)}")
			embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"```\nEdited note {name} to » {themename}```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "delnote",
					usage="<name>",
					description = "Delete a note")
	async def delnote(self, luna, name:str):
		await luna.message.delete()

		if files.file_exist(f"Luna/notes/{name}.txt", documents=True):
			os.remove(os.path.join(files.documents(), f"Luna/notes/{name}.txt"))
			prints.message(f"Deleted note » {color.purple(name)}")

			embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"```\nDeleted note » {name}```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)
		else:
			if configs.error_log() == "console":
				prints.error(f"There is no note called » {color.purple(name)}")
			else:
				embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nThere is no note called » {name}```", color=0xff0000)
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)

	@commands.command(name = "sendnote",
					usage="<name>",
					description = "Send the note")
	async def sendnote(self, luna, name:str):
		await luna.message.delete()

		if not files.file_exist(f"Luna/notes/{name}.txt", documents=True):
			if configs.error_log() == "console":
				prints.error(f"No note exists with the name » {color.purple(name)}")
			else:
				embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nNo note exists with the name » {name}```", color=0xff0000)
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)
		else:
			if name.endswith('.txt'):
				name = name[:-4]
			await luna.send(file=discord.File(os.path.join(files.documents(), f"Luna/notes/{name}.txt")))

	@commands.command(name = "shownote",
					usage="<name>",
					description = "Send the content of the note")
	async def shownote(self, luna, name:str):
		await luna.message.delete()

		if not files.file_exist(f"Luna/notes/{name}.txt", documents=True):
			if configs.error_log() == "console":
				prints.error(f"No note exists with the name » {color.purple(name)}")
			else:
				embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nNo note exists with the name » {name}```", color=0xff0000)
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)
		else:
			file = open(os.path.join(files.documents(), f"Luna/notes/{name}.txt"), "r")
			file_data = file.read()
			if file_data == "":
				if configs.error_log() == "console":
					prints.error(f"The note is empty")
				else:
					embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nThe note is empty```", color=0xff0000)
					embed.set_thumbnail(url=theme.image_url())
					embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
					embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
					embed.set_image(url=theme.large_image_url())
					await send(luna, embed)
			else:
				embed = discord.Embed(title="Notes", description=f"```\nContent of {name}.txt ↴\n\n{str(file_data)}```", color=theme.hex_color())
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)

	@commands.command(name = "notes",
					usage="",
					description = "Show all notes")
	async def notes(self, luna):
		await luna.message.delete()

		path_to_text = os.path.join(files.documents(), "Luna/notes")
		text_files = [pos_txt for pos_txt in os.listdir(path_to_text) if pos_txt.endswith('.txt')]
		prefix = files.json("Luna/config.json", "prefix", documents=True)

		if text_files == []:
			stringedit = "None"
		else:
			string = f"{text_files}"
			stringedit = string.replace(',', f"\n{prefix}shownote").replace("'", "").replace('[', f"{prefix}shownote ").replace(']', "").replace('.txt', "")

		embed = discord.Embed(title="Notes", description=f"{theme.description()}```\nNote control\n\n{prefix}note <name> <text> » Create a note\n{prefix}editnote <name> <name> » Edit note name\n{prefix}delnote <name>   » Delete a note\n{prefix}sendnote <name>  » Send the note\n``````\nAvailable notes\n\n{stringedit}```", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "poll",
					usage="<question>",
					description = "Create a poll")
	async def poll(self, luna, *, question):
		await luna.message.delete()
		embed = discord.Embed(title=f"Poll", description=f"{question}", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		message = await luna.send(embed=embed)
		await message.add_reaction('👍')
		await message.add_reaction('👎')

	@commands.command(name = "cpoll",
					usage="<option1> <option2> <question>",
					description = "Poll")
	async def cpoll(self, luna, option1, option2, *, poll):
		await luna.message.delete()
		embed = discord.Embed(title=f"Poll", description=f"{poll}\n\n🅰️ = {option1}\n🅱️ = {option2}", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		message = await luna.send(embed=embed)
		await message.add_reaction('🅰️')
		await message.add_reaction('🅱️')

	@commands.command(name = "hiddenping",
					usage="<channel_id> <user_id> <message>",
					description = "Ping someone without showing @member")
	async def hiddenping(self, luna, channel_id: int, user_id, *, message):
		await luna.message.delete()

		if user_id == "@everyone" or user_id == "everyone":
			user = "@everyone"
		elif len(user_id) == 18:
			user = "<@" + user_id + ">"
		elif len(user_id) == 19:
			user = "<" + user_id + ">"
		else:
			prints.error("Invalid User!")

		cuser = await self.bot.fetch_user(user_id)
		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(f"<{message}>" + charTT + user)
		await embed_builder(luna, title=f"Hidden Ping", description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nUser Name         » {cuser.name}#{cuser.discriminator}\nUser ID           » {user_id}\nMessage           » {message}```")

	@commands.command(name = "hiddeneveryone",
					usage="<channel_id> <message>",
					description = "Ping everyone without showing @everyone")
	async def hiddeneveryone(self, luna, channel_id: int, *, message):
		await luna.message.delete()

		user = "@everyone"

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(f"<{message}>" + charTT + user)
		await embed_builder(luna, title=f"Hidden Everyone", description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nMessage           » {message}```")

	@commands.command(name = "hiddeninvite",
					usage="<channel_id> <invite> <message>",
					description = "hide the invite")
	async def hiddeninvite(self, luna, channel_id: int, invite, *, message):
		await luna.message.delete()

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(f"<{message}>" + charTT + invite)
		await embed_builder(luna, title=f"Hidden Ping", description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nInvite            » {invite}\nMessage           » {message}```")

	@commands.command(name = "hiddenurl",
					usage="<channel_id> <url> <message>",
					description = "Hide the url")
	async def hiddenurl(self, luna, channel_id: int, url, *, message):
		await luna.message.delete()

		cchannel = await self.bot.fetch_channel(channel_id)

		channel = self.bot.get_channel(channel_id)
		charTT = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
		await channel.send(f"<{message}>" + charTT + url)
		await embed_builder(luna, title=f"Hidden Ping", description=f"```\nPing sent!\n\nChannel ID        » {channel_id}\nChannel Name      » {cchannel.name}\nURL               » {url}\nMessage           » {message}```")

	@commands.command(name = "channels",
					usage="[guild_id]",
					description = "Show all the channels")
	async def channels(self, luna, server_id:int=None):
		await luna.message.delete()
		if server_id is None:
			server = discord.utils.get(luna.bot.guilds, id=luna.guild.id)
		else: 
			server = discord.utils.get(luna.bot.guilds, id=server_id)
		channels = server.channels
		channel_list = []
		for channel in channels:
			channel_list.append(channel)
		await embed_builder(luna, title=f"Channels in {server}", description='\n'.join([f"{ch.name}" for ch in channel_list]) or 'None')

	@commands.command(name = "firstmsg",
					usage="[#channel]",
					description = "First message")
	async def firstmsg(self, luna, channel: discord.TextChannel = None):
		await luna.message.delete()
		if channel is None:
			channel = luna.channel
		first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
		await embed_builder(luna, title="First Message", description=f"[Jump]({first_message.jump_url})")

	@commands.command(name = "compareservers",
					usage="<serverid1> <serverid2>",
					description = "Checks if members are in the same server")
	async def compareservers(self, luna, server_id:int, server_id_2:int):
		await luna.message.delete()
		server_1 = self.bot.get_guild(server_id)
		server_2 = self.bot.get_guild(server_id_2)
		output = ""
		count = 0
		for member in server_1.members:
			if member in server_2.members:
				output += "{}\n".format(str(member.mention))
				count += 1
		await embed_builder(luna, title=f"```\nMembers in the same Server » {count}```", description=f"```\n{server_1} - {server_2}\n``````\n{output}```")

	@commands.command(name = "bots",
					usage="",
					description = "Show all bots in the guild")
	async def bots(self, luna):
		await luna.message.delete()
		bots = []
		for member in luna.guild.members:
			if member.bot:
				bots.append(str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
		botslist = f"{', '.join(bots)}".replace(',', "\n")
		await embed_builder(luna, title=f"Bots ({len(bots)})", description=f"{botslist}")

	@commands.command(name = "tts",
					usage="<language> <text>",
					description = "Text to speech")
	async def tts(self, luna, lang, *, text: str):
		await luna.message.delete()
		tts = gTTS(text, lang=lang)
		filename = f'{text}.mp3'
		tts.save(filename)
		await luna.send(file=discord.File(fp=filename, filename=filename))
		if os.path.exists(filename):
			os.remove(filename)

	@commands.command(name = "qrcode",
					usage="<text>",
					description = "Create a QR code")
	async def qrcode(self, luna, *, text:str):
		await luna.message.delete()

		with open('./config.json') as f:
			config = json.load(f)
		deletetimer = int(config.get('deletetimer'))

		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=10,
			border=4,
		)
		qr.add_data(text)
		qr.make(fit=True)
		img = qr.make_image(fill_color='black', back_color='white')
		filename = f'lunaqr.png'
		img.save(filename)
		await luna.send(file=discord.File(fp=filename, filename=filename), delete_after=deletetimer)
		if os.path.exists(filename):
			os.remove(filename)

	@commands.command(name = "open",
					usage="<application>",
					description = "Open an application")
	async def open(self, luna, *, application:str):
		os.startfile(application)

	@commands.command(name = "calc",
					usage="",
					description = "Opens calculator")
	async def calc(self, luna):
		await luna.message.delete()
		from subprocess import call
		call(["calc.exe"])

	@commands.command(name = "notepad",
					usage="",
					description = "Opens notepad")
	async def notepad(self, luna):
		await luna.message.delete()
		from subprocess import call
		call(["notepad.exe"])

	@commands.command(name = "passgen",
					usage="",
					description = "Generate a password")
	async def passgen(self, luna):
		await luna.message.delete()
		code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
		await embed_builder(luna, description=f"```\nPassword generated ↴\n\n{code}```")

bot.add_cog(ToolsCog(bot))

class NettoolCog(commands.Cog, name="Nettool commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "latency",
					usage="",
					description = "Display Luna's latency")
	async def latency(self, luna):
		await luna.message.delete()
		if configs.mode() == 2:
			before = time.monotonic()
			sent = await luna.send(f"```ini\n[ Latency ]\n\nPinging...\n\n[ {theme.footer()} ]```")
			ping = (time.monotonic() - before) * 100
			await sent.edit(content=f"```ini\n[ Latency ]\n\nAPI Latency\n{int(ping)}ms\n\n[ {theme.footer()} ]```")
		if files.json("Luna/config.json", "mode", documents=True) == 3:
			before = time.monotonic()
			sent = await luna.send(f"> **Latency**\n> \n> Pinging...\n> \n> {theme.footer()}")
			ping = (time.monotonic() - before) * 100
			await sent.edit(content=f"> **Latency**\n> \n> API Latency\n> {int(ping)}ms\n> \n> {theme.footer()}")
		else:
			embed = discord.Embed(title="Latency", url=theme.title_url(), description=f"```\nPinging...```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			before = time.monotonic()
			sent = await luna.send(embed=embed)
			ping = (time.monotonic() - before) * 100
			embed = discord.Embed(title="Latency", url=theme.title_url(), description=f"```\nAPI Latency\n{int(ping)}ms```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await sent.edit(embed=embed)

	@commands.command(name = "ping",
					usage="<url/ip>",
					description = "Ping an IP or URL")
	async def ping(self, luna, *, url:str):
		await luna.message.delete()
		await embed_builder(luna, title=f"Ping", description=f"```\nPinging {url}...```")
		output = subprocess.run(f"ping {url}",text=True,stdout=subprocess.PIPE).stdout.splitlines()
		values = "".join(output[-1:])[4:].split(", ")
		minimum = values[0][len("Minimum = "):]
		maximum = values[1][len("Maximum = "):]
		average = values[2][len("Average = "):]
		await embed_builder(luna, title=f"{url}", description=f"```\nMinimum » {minimum}\nMaximum » {maximum}\nAverage » {average}```")

	@commands.command(name = "ip",
						usage="",
						description = "Display IP information")
	async def ip(self, luna, ip:str):
		await luna.message.delete()
		if ip is None:
			await luna.send("Please specify a IP address")
			return
		else:
			try:
				with requests.session() as ses:
					resp = ses.get(f'https://ipinfo.io/{ip}/json')
					if "Wrong ip" in resp.text:
						await embed_builder(luna, description="Invalid IP address")
						return
					else:
						j = resp.json()
						await embed_builder(luna, title=f"IP » {ip}", description=f'```\nCity\n{j["city"]}\n``````\nRegion\n{j["region"]}\n``````\nCountry\n{j["country"]}\n``````\nCoordinates\n{j["loc"]}\n``````\nPostal\n{j["postal"]}\n``````\nTimezone\n{j["timezone"]}\n``````\nOrganization\n{j["org"]}```')
			except Exception as e:
				await luna.send(f"Error: {e}")				

	@commands.command(name="tcpping", usage="<ip> <port>", description="Checks if host is online")
	async def tcpping(self, luna, ip, port):
		await luna.message.delete()
		if ip is None:
			await luna.send("Please specify a IP address")
			return
		if port is None:
			await luna.send("Please specify a port")
			return
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.3)
		try:
			sock.connect((ip, int(port)))
		except:
			await embed_builder(luna, title="TCP-Ping", description=f"```Status » Offline\n``````\nIP » {ip}\n``````\nPort » {port}\n```")
		else:
			await embed_builder(luna, title="TCP-Ping", description=f"```Status » Online\n``````\nIP » {ip}\n``````\nPort » {port}\n```")

	@commands.command(name="portscan", usage="<ip>", description="Checks for common open ports")
	async def portscan(self, luna, ip):
		await luna.message.delete()
		if ip is None:
			await luna.send("Please specify an IP address")
			return
		ports = ["10","12","13","14","16","17","18","20","21","22","23","25","40","42","45","47","48","50","53","80","81","110","139","389","443","445","996","1433","1521","1723","3066","3072","3306","3389","5900","8080","8181","65530","65535"]
		open_ports = []
		for port in ports:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(0.2)
			try:
				sock.connect((ip, int(port)))
			except:
				pass
			else:
				sock.close()
				open_ports.append(port)
		await embed_builder(luna, title="Port Scanner", description=f'```\nIP » {ip}\n``````\nPorts Checked » {",".join(ports)}\n``````\nOpen Ports » {",".join(open_ports)}\n```')

	@commands.command(name="resolve", usage="<url>", description="Get the url host IP")
	async def resolve(self, luna, url):
		await luna.message.delete()
		import socket
		new_url = ""
		if url is None:
			await luna.send("Please specify a URL")
			return
		if url.startswith("https://"):
			new_url = url.replace("https://", "")
		elif url.contains("http://"):
			new_url = url.replace("http://", "")
		
		try:
			ip = socket.gethostbyname(new_url)
		except:
			await embed_builder(luna, title="Resolve", description=f"```\nURL is invalid```")
			return
		await embed_builder(luna, title="Host Resolver", description=f"```\nURL » {url}\n``````\nIP » {ip}\n```")

	@commands.command(name="webhookinfo", usage="<id>", description="Webhook information")
	async def webhookinfo(self, luna, id):
		await luna.message.delete()
		try:
			webhook = await self.bot.fetch_webhook(id)
			await embed_builder(luna, title=f"Webhook » {webhook.name}", description=f"```\nID » {webhook.id}\n``````\nName » {webhook.name}\n``````\nChannel » {webhook.channel.name}\n``````\nGuild » {webhook.guild.name}\n``````\nToken » {webhook.token}\n```", thumbnail=webhook.avatar_url)
		except:
			await error_builder(luna, "```\nInvalid webhook ID```")

	@commands.command(name="maclookup", usage="<mac>", description="MAC address Information")
	async def maclookup(self, luna, mac:str):
		await luna.message.delete()
		if mac is None:
			await luna.send("Please specify a MAC address")
			return
		if len(mac) != 17:
			await luna.send("Invalid MAC address")
			return
		try:
			resp = requests.get(f'https://api.macvendors.com/{mac}')
			if "Not Found" in resp.text:
				await embed_builder(luna, description="```\nInvalid MAC address```")
			else:
				j = resp.json()	
				await embed_builder(luna, title=f"MAC » {mac}", description=f"```\nVendor » {j}\n```")
		except:
			await error_builder(luna, "```\nError » Invalid MAC address```")

	@commands.command(name="reverseip", usage="<ip>", description="Reverse DNS")
	async def reverseip(self, luna, ip):
		await luna.message.delete()
		if ip is None:
			await embed_builder(luna, description="```\nPlease specify an IP address```")
			return
		try:
			resp = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
			if "error" in resp.text:
				await embed_builder(luna, description="```\nInvalid IP address```")
			else:
				j = resp.json()
				await embed_builder(luna, title=f"Reverse DNS » {ip}", description=f"```\n{j}\n```")
		except:
			await error_builder(luna, "```\nError » Invalid IP address```")

	@commands.command(name="mtr", usage="<ip>", description="MTR Traceroute")
	async def mtr(self, luna, ip):
		await luna.message.delete()
		if ip is None:
			await embed_builder(luna, description="```\nPlease specify an IP address```")
			return
		try:
			resp = requests.get(f'https://api.hackertarget.com/mtr/?q={ip}')
			if "error" in resp.text:
				await embed_builder(luna, description="```\nInvalid IP address```")
			else:
				j = resp.json()
				await embed_builder(luna, title=f"MTR Traceroute » {ip}", description=f"```\n{j}\n```")
		except:
			await error_builder(luna, "```\nError » Invalid IP address```")

	@commands.command(name="asn", usage="<ip>", description="ASN Information")
	async def asn(self, luna, ip):
		await luna.message.delete()
		if ip is None:
			await embed_builder(luna, description="```\nPlease specify an IP address```")
			return
		try:
			resp = requests.get(f'https://api.hackertarget.com/asnlookup/?q={ip}')	
			if "error" in resp.text:
				await embed_builder(luna, description="```\nInvalid IP address```")
			else:
				j = resp.json()
				await embed_builder(luna, title=f"ASN » {ip}", description=f"```\n{j}\n```")
		except:
			await error_builder(luna, "```\nError » Invalid IP address```")

	@commands.command(name="zonetransfer", usage="<domain>", description="Zone Transfer")
	async def zonetransfer(self, luna, domain):
		await luna.message.delete()
		if domain is None:
			await embed_builder(luna, description="```\nPlease specify a domain```")
			return
		try:
			resp = requests.get(f'https://api.hackertarget.com/zonetransfer/?q={domain}')
			if "error" in resp.text:
				await embed_builder(luna, description="```\nInvalid domain```")
			else:
				j = resp.json()
				await embed_builder(luna, title=f"Zone Transfer » {domain}", description=f"```\n{j}\n```")
		except:
			await error_builder(luna, "```\nError » Invalid domain```")

	@commands.command(name="httpheaders", usage="<url>", description="HTTP Headers")
	async def httpheaders(self, luna, url):
		await luna.message.delete()
		if url is None:
			await embed_builder(luna, description="```\nPlease specify a URL```")
			return
		try:
			resp = requests.get(f'https://api.hackertarget.com/httpheaders/?q={url}')
			if "error" in resp.text:
				await embed_builder(luna, description="```\nInvalid URL```")
			else:
				j = resp.json()
				await embed_builder(luna, title=f"HTTP Headers » {url}", description=f"```\n{j}\n```")
		except:
			await error_builder(luna, "```\nError » Invalid URL```")

	@commands.command(name="subnetcalc", usage="<ip>", description="Subnet Calculator")
	async def subnetcalc(self, luna, ip):
		await luna.message.delete()
		if ip is None:
			await embed_builder(luna, description="```\nPlease specify an IP address```")
			return
		try:
			resp = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
			if "error" in resp.text:
				await embed_builder(luna, description="```\nInvalid IP address```")
			else:
				j = resp.json()
				await embed_builder(luna, title=f"Subnet Calculator » {ip}", description=f"```\n{j}\n```")
		except:
			await error_builder(luna, "```\nError » Invalid IP address```")

	@commands.command(name="crawl", usage="<url>", description="Crawl a website")
	async def crawl(self, luna, url):
		await luna.message.delete()
		if url is None:
			await embed_builder(luna, description="```\nPlease specify a URL```")
			return
		try:
			resp = requests.get(f'https://api.hackertarget.com/pagelinks/?q={url}')
			if "error" in resp.text:
				await embed_builder(luna, description="```\nInvalid URL```")
			else:
				j = resp.json()
				await embed_builder(luna, title=f"Crawl » {url}", description=f"```\n{j}\n```")
		except:
			await error_builder(luna, "```\nError » Invalid URL```")
	
	@commands.command(name="scrapeproxies", usage="", aliases=['proxyscrape', 'scrapeproxy'],description="Scrape for proxies")
	async def scrapeproxies(self, luna):
		await luna.message.delete()
		file = open(os.path.join(files.documents(), "Luna/raiding/proxies/http.txt"), "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")
		file = open(os.path.join(files.documents(), "Luna/raiding/proxies/https.txt"), "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")
		file = open(os.path.join(files.documents(), "Luna/raiding/proxies/socks4.txt"), "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")
		file = open(os.path.join(files.documents(), "Luna/raiding/proxies/socks5.txt"), "a+")
		res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
		proxies = []
		for proxy in res.text.split('\n'):
			proxy = proxy.strip()
			if proxy:
				proxies.append(proxy)
		for p in proxies:
			file.write((p)+"\n")
		await embed_builder(luna, title="Proxy Scraper", description=f"```\nSaved all scraped proxies in Luna/raiding/proxies```")#

	@commands.command(name="ip", usage="", description="Show your ip")
	async def ip(self, luna):
		await luna.message.delete()
		ip = requests.get('https://api.ipify.org').text
		await embed_builder(luna, title="Your IP", description=f"```\nIP » {ip}\n```")

bot.add_cog(NettoolCog(bot))

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

class UtilsCog(commands.Cog, name="Util commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "pcspecs", 
					usage="",
					aliases=['pc', 'specs'],
					description="Show your pc specs")
	async def pcspecs(self, luna):
		await luna.message.delete()
		uname = platform.uname()
		boot_time_timestamp = psutil.boot_time()
		bt = datetime.fromtimestamp(boot_time_timestamp)
		cpufreq = psutil.cpu_freq()
		cores = ""
		for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
			cores += f"\n{'Core' + str(i):17} » {percentage}%"
		svmem = psutil.virtual_memory()
		partitions = psutil.disk_partitions()
		disk_io = psutil.disk_io_counters()
		partition_info = ""
		for partition in partitions:
			try:
				partition_usage = psutil.disk_usage(partition.mountpoint)
			except PermissionError:
				continue
			partition_info += f"{'Device':17} » {partition.device}\n{'Mountpoint':17} » {partition.mountpoint}\n{'System Type':17} » {partition.fstype}\n{'Total Size':17} » {get_size(partition_usage.total)}\n{'Used':17} » {get_size(partition_usage.used)}\n{'Free':17} » {get_size(partition_usage.free)}\n{'Percentage':17} » {get_size(partition_usage.percent)}%\n{'Total Read':17} » {get_size(disk_io.read_bytes)}\n{'Total Write':17} » {get_size(disk_io.write_bytes)}\n\n"
		net_io = psutil.net_io_counters()
		await embed_builder(luna, title="PC Specs", description=f"```\nGeneral\n\n{'System':17} » {uname.system}\n{'Node':17} » {uname.node}\n{'Release':17} » {uname.release}\n{'Version':17} » {uname.version}\n{'Machine':17} » {uname.machine}\n{'Processor':17} » {uname.processor}\n``````\nCPU Information\n\n{'Physical Cores':17} » {psutil.cpu_count(logical=False)}\n{'Total Cores':17} » {psutil.cpu_count(logical=True)}\n{'Max Frequency':17} » {cpufreq.max:.2f}Mhz\n{'Min Frequency':17} » {cpufreq.min:.2f}Mhz\n{'Current Frequency':17} » {cpufreq.current:.2f}Mhz\n\nCurrent Usage{cores}\n``````\nMemory Information\n\n{'Total':17} » {get_size(svmem.total)}\n{'Available':17} » {get_size(svmem.available)}\n{'Used':17} » {get_size(svmem.used)}\n{'Percentage':17} » {get_size(svmem.percent)}%\n``````\nDisk Information\n\n{partition_info}\n``````\nNetwork\n\n{'Bytes Sent':17} » {get_size(net_io.bytes_sent)}\n{'Bytes Received':17} » {get_size(net_io.bytes_recv)}\n``````\nBoot Time\n\n{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n```")

	@commands.command(name = "serverjoiner",
					aliases=['joinservers', 'jservers', 'joinserver', 'joininvites'],
					usage="",
					description = "Join all invites in data/invites.txt")
	async def serverjoiner(self, luna):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			if os.stat(os.path.join(files.documents(), "Luna/invites.txt")).st_size == 0:
				await embed_builder(luna, title="Server Joiner", description=f"```\ninvites.txt is empty...```")
				return
			else:
				file = open(os.path.join(files.documents(), "Luna/invites.txt"), "r")
				nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
				line_count = len(nonempty_lines)
				file.close()
				await embed_builder(luna, title="Server Joiner", description=f"```\nFound {line_count} invites in invites.txt\nJoining provided invites...```")
				with open(os.path.join(files.documents(), "Luna/invites.txt"),"r+") as f:
					for line in f:
						invite = line.strip("\n")
						invite = invite.replace('https://discord.gg/', '').replace('https://discord.com/invite/', '').replace('Put the invites of the servers you want to join here one after another', '')
						try:
							async with httpx.AsyncClient() as client:
								await client.post(f'https://discord.com/api/v9/invites/{invite}', headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
								prints.event(f"Joined {invite}")
								await asyncio.sleep(0.5)
						except Exception as e:
							prints.error(f"Failed to join {invite}")
							prints.error(e)
							pass
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "proxyserverjoiner",
					usage="",
					description = "Join all invites in data/invites.txt using proxies")
	async def proxyserverjoiner(self, luna):
		await luna.message.delete()
		proxies = open(os.path.join(files.documents(), "Luna/raiding/proxies.txt"), 'r')
		proxylist = []
		for p, _proxy in enumerate(proxies):
			proxy = _proxy.split('\n')[0]
			proxylist.append(proxy)
		if configs.risk_mode() == "on":
			if os.stat(os.path.join(files.documents(), "Luna/invites.txt")).st_size == 0:
				await embed_builder(luna, title="Server Joiner", description=f"```\ninvites.txt is empty...```")
				return
			else:
				file = open(os.path.join(files.documents(), "Luna/invites.txt"), "r")
				nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
				line_count = len(nonempty_lines)
				file.close()
				await embed_builder(luna, title="Server Joiner", description=f"```\nFound {line_count} invites in invites.txt\nJoining provided invites...```")
				with open(os.path.join(files.documents(), "Luna/invites.txt"),"r+") as f:
					for line in f:
						invite = line.strip("\n")
						invite = invite.replace('https://discord.gg/', '').replace('https://discord.com/invite/', '').replace('Put the invites of the servers you want to join here one after another', '')
						try:
							async with httpx.AsyncClient() as client:
								await client.post(f'https://discord.com/api/v9/invites/{invite}', headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'}, proxies={'http://': f'http://{proxylist[p]}'})
								prints.event(f"Joined {invite}")
								await asyncio.sleep(0.5)
						except Exception as e:
							prints.error(f"Failed to join {invite}")
							prints.error(e)
							pass
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "countdown",
					usage="<number>",
					description = "Create a countdown")
	async def countdown(self, luna, number:int):
		for count in range(number, 0, -1):
			await luna.send(count)
			await asyncio.sleep(1)

	@commands.command(name = "countup",
					usage="<number>",
					description = "Create a countup")
	async def countup(self, luna, number:int):
		for count in range(0, number):
			await luna.send(count)
			await asyncio.sleep(1)

	@commands.command(name = "emojis",
					usage="",
					description = "List all emojis")
	async def emojis(self, luna):
		await luna.message.delete()
		server = luna.message.guild
		emojis = [e.name for e in server.emojis]
		emojis = '\n'.join(emojis)
		await embed_builder(luna, title="Emojis", description=f"```\n{emojis}```")

	@commands.command(name = "addemoji",
					usage="<emoji_name> <image_url>",
					description = "Add an emoji")
	@has_permissions(manage_emojis=True)
	async def addemoji(self, luna, emoji_name, image_url=None):
		await luna.message.delete()
		if luna.message.attachments:
			image = await luna.message.attachments[0].read()
		elif image_url:
			async with aiohttp.ClientSession() as session:
				async with session.get(image_url) as resp:
					image = await resp.read()
		await luna.guild.create_custom_emoji(name=emoji_name, image=image)
		embed = discord.Embed(title="Emoji Added", url=theme.title_url(), description=f"{emoji_name}", color=theme.hex_color())
		embed.set_thumbnail(url=image_url)
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "editemoji",
					usage="<emoji> <new_name>",
					description = "Edit an emoji")
	@has_permissions(manage_emojis=True)
	async def editemoji(self, luna, emoji: discord.Emoji, new_name):
		await luna.message.delete()
		oldname = emoji.name
		await emoji.edit(name=new_name)
		embed = discord.Embed(title="Emoji Edited", url=theme.title_url(), description=f"{oldname} to {new_name}", color=theme.hex_color())
		embed.set_thumbnail(url=emoji.url)
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "delemoji",
					usage="<emoji>",
					description = "Delete an emoji")
	@has_permissions(manage_emojis=True)
	async def delemoji(self, luna, emoji: discord.Emoji):
		await luna.message.delete()
		name = emoji.name
		emojiurl = emoji.url
		await emoji.delete()
		embed = discord.Embed(title="Emoji Deleted", url=theme.title_url(), description=f"{name}", color=theme.hex_color())
		embed.set_thumbnail(url=emojiurl)
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "stealemoji",
					aliases = ['stealemojis'],
					usage="<guild_id>",
					description = "Steal all emojis from a guild")
	@has_permissions(manage_emojis=True)
	async def stealemoji(self, luna, guild_id):
		await luna.message.delete()
		if not os.path.exists('data/emojis'):
			os.makedirs('data/emojis')
		guild_id = int(guild_id)
		try:
			guildhit = self.bot.get_guild(guild_id)
		except Exception as e:
			if configs.error_log() == "console":
				prints.error(f"{e}")
			else:
				embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\n{e}```", color=theme.hex_color())
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)
			return


	@commands.command(name = 'playing', 
				usage="<text>", 
				description = "Change your activity to playing.")
	async def playing(self, luna, *, status: str = None):
		await luna.message.delete()
		if status is None:
			prints.error("You didnt put a text to play")
		else:
			try:
				game = discord.Activity(type=0, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"```\nStatus changed to » Playing {status}```", color=theme.hex_color())
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)
			except Exception as e:
				if configs.error_log() == "console":
					prints.error(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\n{e}```", color=theme.hex_color())
					embed.set_thumbnail(url=theme.image_url())
					embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
					embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
					embed.set_image(url=theme.large_image_url())
					await send(luna, embed)


	@commands.command(name = 'streaming', 
				usage="<text>", 
				description = "Change your activity to streaming.")
	async def streaming(self, luna, *, status: str = None):
		await luna.message.delete()
		if status is None:
			prints.error("You didnt put a text to stream")
		else:
			try:
				game = discord.Activity(type=1, name=f"{status}", url=configs.stream_url())
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"```\nStatus changed to » Streaming {status}```", color=theme.hex_color())
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)
			except Exception as e:
				if configs.error_log() == "console":
					prints.error(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\n{e}```", color=theme.hex_color())
					embed.set_thumbnail(url=theme.image_url())
					embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
					embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
					embed.set_image(url=theme.large_image_url())
					await send(luna, embed)


	@commands.command(name = 'listening', 
				usage="<text>", 
				description = "Change your activity to listening.")
	async def listening(self, luna, *, status: str = None):
		await luna.message.delete()
		if status is None:
			prints.error("You didnt put a text to listen to")
		else:
			try:
				game = discord.Activity(type=2, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"```\nStatus changed to » Listening {status}```", color=theme.hex_color())
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)
			except Exception as e:
				if configs.error_log() == "console":
					prints.error(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\n{e}```", color=theme.hex_color())
					embed.set_thumbnail(url=theme.image_url())
					embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
					embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
					embed.set_image(url=theme.large_image_url())
					await send(luna, embed)

	@commands.command(name = 'watching', 
				usage="<text>", 
				description = "Change your activity to watching.")
	async def watching(self, luna, *, status: str = None):
		await luna.message.delete()
		if status is None:
			prints.error("You didnt put a text to watch")
		else:
			try:
				game = discord.Activity(type=3, name=f"{status}")
				await self.bot.change_presence(activity=game)
				embed = discord.Embed(title=theme.title(), url=theme.title_url(), description=f"```\nStatus changed to » Watching {status}```", color=theme.hex_color())
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				send(luna, embed)
			except Exception as e:
				if configs.error_log() == "console":
					prints.error(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\n{e}```", color=theme.hex_color())
					embed.set_thumbnail(url=theme.image_url())
					embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
					embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
					embed.set_image(url=theme.large_image_url())
					await send(luna, embed)

	@commands.command(name = 'stopactivity', 
				usage="", 
				aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"],
				description = "Stop your activity.")
	async def stopactivity(self, luna):
		await luna.message.delete()
		await self.bot.change_presence(activity=None, status=discord.Status.dnd)
		embed = discord.Embed(title=theme.title(), url=theme.title_url(), description="```\nStopped activity```", color=theme.hex_color())
		embed.set_thumbnail(url=theme.image_url())
		embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		embed.set_image(url=theme.large_image_url())
		await send(luna, embed)

	@commands.command(name = "clean",
					usage="<amount>",
					description = "Clean your messages")
	async def clean(self, luna, amount: int = None):
		await luna.message.delete()
		try:
			if amount is None:
				embed = discord.Embed(title="Error", url=theme.title_url(), description="```\nInvalid amount```", color=theme.hex_color())
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)
			else:
				await luna.channel.purge(limit=amount, before=luna.message, check=is_me)
		except:
			try:
				await asyncio.sleep(1)
				async for message in luna.message.channel.history(limit=amount):
					if message.author == self.bot.user:
						await message.delete()
					else:
						pass
			except Exception as e:
				if configs.error_log() == "console":
					prints.error(f"{e}")
				else:
					embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\n{e}```", color=theme.hex_color())
					embed.set_thumbnail(url=theme.image_url())
					embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
					embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
					embed.set_image(url=theme.large_image_url())
					await send(luna, embed)
				return

	@commands.command(name = "textreact",
					aliases=['treact'],
					usage="<amount>",
					description = "Text as reaction")
	async def textreact(self, luna, messageNo: typing.Optional[int] = 1, *, text):
		await luna.message.delete()
		text = (c for c in text.lower())
		emotes = {
			"a": "🇦",
			"b": "🇧",
			"c": "🇨",
			"d": "🇩",
			"e": "🇪",
			"f": "🇫",
			"g": "🇬",
			"h": "🇭",
			"i": "🇮",
			"j": "🇯",
			"k": "🇰",
			"l": "🇱",
			"m": "🇲",
			"n": "🇳",
			"o": "🇴",
			"p": "🇵",
			"q": "🇶",
			"r": "🇷",
			"s": "🇸",
			"t": "🇹",
			"u": "🇺",
			"v": "🇻",
			"w": "🇼",
			"x": "🇽",
			"y": "🇾",
			"z": "🇿",
		}
		for i, m in enumerate(await luna.channel.history(limit=100).flatten()):
			if messageNo == i:
				for c in text:
					await m.add_reaction(f"{emotes[c]}")
				break
		
	@commands.command(name = "afk",
					usage="<on/off>",
					description = "AFK mode on/off")
	async def afk(self, luna, mode:str=None):
		await luna.message.delete()

		global afkstatus

		if mode == "on" or mode == "off":
			prints.message(f"AFK Mode » {color.purple(f'{mode}')}")
			if mode == "on":
				afkstatus = 1
			else:
				afkstatus = 0
			await embed_builder(luna, description=f"```\nAFK Mode » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "invisiblenick",
					usage="",
					description = "Make your nickname invisible")
	async def invisiblenick(self, luna):
		await luna.message.delete()

		try:
			name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
			await luna.message.author.edit(nick=name)
		except Exception as e:
			await luna.send(f"Error: {e}")

	@commands.command(name = "hypesquad",
					usage="<bravery/brilliance/balance>",
					description = "Change Hypesquad house")
	async def hypesquad(self, luna, house:str):
		await luna.message.delete()
		with open('./config.json') as f:
			config = json.load(f)
		token = config.get('token')
		request = requests.session()
		headers = {
			'Authorization': token,
			'Content-Type': 'application/json'
		}

		if house == "bravery":
			payload = {'house_id': 1}
		elif house == "brilliance":
			payload = {'house_id': 2}
		elif house == "balance":
			payload = {'house_id': 3}

		try:
			request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload)
			prints.message(f"Successfully set your hypesquad house to {house}")
			embed = discord.Embed(title="Hypesquad", url=theme.title_url(), description=f"```\nSuccessfully set your hypesquad house to {house}```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)
		except:
			if configs.error_log() == "console":
				prints.error("Failed to set your hypesquad house")
			else:
				embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nFailed to set your hypesquad house```", color=0xff0000)
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)

	@commands.command(name = "acceptfriends",
					usage="",
					description = "Accept friend requests")
	async def acceptfriends(self, luna):
		await luna.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship == discord.RelationshipType.incoming_request:
				try:
					await relationship.accept()
					prints.message(f"Accepted {relationship}")
				except Exception:
					pass


	@commands.command(name = "ignorefriends",
					usage="",
					description = "Delete friend requests")
	async def ignorefriends(self, luna):
		await luna.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.incoming_request:
				relationship.delete()
				prints.message(f"Deleted {relationship}")


	@commands.command(name = "delfriends",
					usage="",
					description = "Delete all friends")
	async def delfriends(self, luna):
		await luna.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.friend:
				try:
					await relationship.delete()
					prints.message(f"Deleted {relationship}")
				except Exception:
					pass


	@commands.command(name = "clearblocked",
					usage="",
					description = "Delete blocked friends")
	async def clearblocked(self, luna):
		await luna.message.delete()
		for relationship in self.bot.user.relationships:
			if relationship is discord.RelationshipType.blocked:
				try:
					await relationship.delete()
					prints.message(f"Deleted {relationship}")
				except Exception:
					pass

	@commands.command(name = "leaveservers",
					usage="",
					description = "Leave all servers")
	async def leaveservers(self, luna):
		await luna.message.delete()
		try:
			guilds = requests.get('https://discordapp.com/api/v9/users/@me/guilds', headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'}).json()
			for guild in range(0, len(guilds)):
				guild_id = guilds[guild]['id']
				requests.delete(f'https://discordapp.com/api/v9/users/@me/guilds/{guild_id}', headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
				prints.message(f"Left {guild}")
		except Exception:
			pass

bot.add_cog(UtilsCog(bot))
class SpamCog(commands.Cog, name="Spam commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "spam",
					usage="<delay> <amount> <message>",
					description = "Spammer")
	async def spam(self, luna, delay:int, amount:int, *, message:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for each in range(0, amount):
					await asyncio.sleep(delay)
					await luna.send(f"{message}")
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "spamdm",
					usage="<delay> <amount> <@user> <message>",
					description = "DMs")
	async def spamdm(self, luna, delay:int, amount:int, user: discord.User, *, message:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for each in range(0, amount):
					await asyncio.sleep(delay)
					await user.send(f"{message}")
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "spamch",
					usage="<delay> <amount> <message>",
					description = "Channels")
	async def spamch(self, luna, delay:int, amount:int, *, message:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for each in range(0, amount):
					for channel in luna.guild.text_channels:
						try:
							await asyncio.sleep(delay)
							await channel.send(f"{message}")
						except Exception as e:
							await error_builder(luna, description=e)
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "spamgp",
					usage="<delay> <amount> <@member>",
					aliases=['spg', 'spamghostping', 'sghostping'],
					description = "Ghostpings")
	async def spamgp(self, luna, delay: int = None, amount: int = None, user: discord.Member = None):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				if delay is None or amount is None or user is None:
					await luna.send(f"Usage: {self.bot.prefix}spamghostping <delay> <amount> <@member>")
				else:
					for each in range(0, amount):
						await asyncio.sleep(delay)
						await luna.send(user.mention, delete_after=0)
			except Exception as e:
				await luna.send(f"Error: {e}")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "spamrep",
					usage="<message_id> <amount>",
					aliases=['spamreport'],
					description = "Reports")
	async def spamrep(self, luna, message_id:str, amount:int):
		await luna.message.delete()

		if configs.risk_mode() == "on":
			try:
				prints.event(f"Spam report started...")
				for each in range(0, amount):
					await asyncio.sleep(2)
					reason = "Illegal Content"
					payload = {
						'message_id': message_id,
						'reason': reason
					}
					requests.post('https://discordapp.com/api/v9/report', json=payload, headers={'authorization': user_token, 'user-agent': 'Mozilla/5.0'})
				prints.event(f"Spam report finished")
				await embed_builder(luna, title="Report", url=theme.title_url(), description=f"Message {message_id} has been reported {amount} times")
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "spamhentai",
					usage="<delay> <amount>",
					description = "Hentai")
	async def spamhentai(self, luna, delay:int, amount:int):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for each in range(0, amount):
					await asyncio.sleep(delay)
					r = requests.get("https://nekos.life/api/v2/img/classic").json()
					await luna.send(r['url'])
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "spamwebhook",
					usage="<delay> <amount> <url>",
					description = "Webhooks")
	async def spamwebhook(self, luna, delay:int, amount:int, url:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			if not "https://discord.com/api/webhooks/" in url:
				await error_builder(luna, description="```\nInvalid URL```")
				return
			try:
				for each in range(0, amount):
					await asyncio.sleep(delay)
					await embed_builder(luna, description=f"```\nSending webhooks...\n``````\nAmount » {amount}\nDelay » {delay}\n``````\nURL » {url}```")
					hook = dhooks.Webhook(url=url, avatar_url=webhook.image_url())
					color = 0x000000
					if error == True:
						color = 0xE10959
					elif color == None:
						pass
					else:
						color = webhook.hex_color()
					embed = dhooks.Embed(title=webhook.title(), description=f"```Get spammed!```", color=color)
					embed.set_thumbnail(url=webhook.image_url())
					embed.set_footer(text=webhook.footer())
					hook.send(embed=embed)
			except Exception as e:
				await error_builder(luna, description=e)
				return
			await embed_builder(luna, description=f"```\nWebhooks sent```")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "spamtts",
					usage="<delay> <amount> <message>",
					description = "TTS")
	async def spamtts(self, luna, delay:int, amount:int, *, message:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for each in range(0, amount):
					await asyncio.sleep(delay)
					await luna.send(message, tts=True)
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

bot.add_cog(SpamCog(bot))
class AllCog(commands.Cog, name="All commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "banall",
					usage="[reason]",
					description = "Ban all")
	async def banall(self, luna, *, reason:str = None):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for each in luna.guild.members:
					if each is not luna.author or each is not luna.guild.owner:
						await each.ban(reason=reason)
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")
		
	@commands.command(name = "banbots",
					usage="[reason]",
					description = "Ban all bots")
	async def banbots(self, luna, *, reason:str = None):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for each in luna.guild.members:
					if each.bot == True:
						await each.ban(reason=reason)
					else:
						pass
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "unbanall",
					usage="[reason]",
					description = "Unban all")
	async def unbanall(self, luna, *, reason:str = None):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for each in luna.guild.bans:
					await luna.guild.unban(each[0], reason=reason)
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "kickall",
					usage="[reason]",
					description = "Kick all")
	async def kickall(self, luna, *, reason:str = None):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for each in luna.guild.members:
					if each is not luna.author or each is not luna.guild.owner:
						await each.kick(reason=reason)
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "kickbots",
					usage="[reason]",
					description = "Kick all bots")
	async def kickbots(self, luna, *, reason:str = None):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for each in luna.guild.members:
					if each.bot == True:
						await each.kick(reason=reason)
					else:
						pass
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "dmall",
					usage="<message>",
					description = "DM every member")
	async def dmall(self, luna, *, message: str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			sent = 0
			try:
				members = luna.channel.members
				for member in members:
					if member is not luna.author:
						try:
							await member.send(message)
							prints.message(f"Sent {message} to {member}")
							sent += 1
						except Exception:
							pass
			except Exception:
				prints.error(f"Failed to send {message} to {member}")
				pass
			await embed_builder(luna, description=f"```\nSent {message} to {sent} users```")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "dmallfriends",
					usage="<message>",
					description = "DM all friends")
	async def dmallfriends(self, luna, *, message: str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			sent = 0
			try:
				for user in self.user.friends:
					try:
						await user.send(message)
						prints.message(f"Sent {message} to {member}")
						sent += 1
					except Exception:
						prints.error(f"Failed to send {message} to {member}")
						pass
			except Exception:
				pass
			await embed_builder(luna, description=f"```\nSent {message} to {sent} friends```")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "sendall",
					usage="<message>",
					description = "Message in all channels")
	async def sendall(self, luna, *, message):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				channels = luna.guild.text_channels
				for channel in channels:
					await channel.send(message)
			except:
				pass
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "blockall",
					usage="",
					description = "Block everyone")
	async def blockall(self, luna):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				members = luna.guild.members
				for member in members:
					if member is not luna.author:
						try:
							await member.ban()
							prints.message(f"Banned {member}")
						except Exception:
							pass
			except Exception:
				pass
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

bot.add_cog(AllCog(bot))
class MassCog(commands.Cog, name="Mass commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "massping",
					usage="<delay> <amount>",
					description = "Mass ping members")
	async def massping(self, luna, delay:int, amount:int):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for i in range(amount):
					members = [m.mention for m in luna.guild.members]
					if len(members) < 30:
						mentionamount = len(members)
					else:
						mentionamount = 30
					sendamount = len(members) - mentionamount + 1
					for i in range(sendamount):
						if mentionamount == 0:
							break
						pingtext = ""
						for i in range(mentionamount):
							pingtext += members.pop()
						await luna.send(pingtext)
						await asyncio.sleep(delay)
						if len(members) < 30:
							mentionamount = len(members)
						else:
							mentionamount = 30
						sendamount = len(members) - mentionamount + 1
			except Exception as e:
				prints.error(f"{e}")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "massgp",
					usage="<delay> <amount>",
					description = "Mass ghostping")
	async def massgp(self, luna, delay:int, amount:int):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				for i in range(amount):
					members = [m.mention for m in luna.guild.members]
					if len(members) < 30:
						mentionamount = len(members)
					else:
						mentionamount = 30
					sendamount = len(members) - mentionamount + 1
					for i in range(sendamount):
						if mentionamount == 0:
							break
						pingtext = ""
						for i in range(mentionamount):
							pingtext += members.pop()
						msg = await luna.send(pingtext)
						await msg.delete()
						await asyncio.sleep(delay)
						if len(members) < 40:
							mentionamount = len(members)
						else:
							mentionamount = 40
						sendamount = len(members) - mentionamount + 1
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "massnick",
					usage="<name>",
					description = "Mass change nicknames")
	async def massnick(self, luna, name:str):
		if configs.risk_mode() == "on":
			bot = discum.Client(token=user_token, log=False, user_agent="Mozilla/5.0")

			def done_fetching(resp, guild_id):
				if bot.gateway.finishedMemberFetching(guild_id):
					members = bot.gateway.session.guild(guild_id).members
					bot.gateway.removeCommand({'function': done_fetching, 'params': {'guild_id': guild_id}})
					bot.gateway.close()
					return members

			def get_members(guild_id, channel_id):
				bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1)
				bot.gateway.command({'function': done_fetching, 'params': {'guild_id': guild_id}})
				bot.gateway.run()
				bot.gateway.resetSession()
				return bot.gateway.session.guild(guild_id).members
			amount = 0
			members = get_members(str(luna.guild.id), str(luna.channel.id))
			for member in members:
				try:
					member = await luna.guild.fetch_member(member.id)
					await member.edit(nick=name)
					amount += 1
					await asyncio.sleep(1)
				except:
					pass
			await embed_builder(luna, title="Success", description=f"```\nChanged nicknames of {amount} members```")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "masschannels",
					usage="<amount>",
					description = "Mass create channels")
	async def masschannels(self, luna, amount:int):
		if configs.risk_mode() == "on":
			try:
				for i in range(amount):
					await luna.guild.create_text_channel("Created by Luna")
					await asyncio.sleep(1)
				await embed_builder(luna, title="Success", description=f"```\nCreated {amount} channels```")
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "massroles",
					usage="<amount>",
					description = "Mass create roles")
	async def massroles(self, luna, amount:int):
		if configs.risk_mode() == "on":
			try:
				for i in range(amount):
					await luna.guild.create_role(name="Created by Luna")
					await asyncio.sleep(1)
				await embed_builder(luna, title="Success", description=f"```\nCreated {amount} roles```")
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "prune",
					usage="<@role> [reason]",
					description = "Prune a role")
	async def prune(self, luna, role, *, reason: str = None):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				if reason is None:
					reason = "No reason provided"
				else:
					reason = reason
				role = luna.guild.get_role(role)
				if role is None:
					await error_builder(luna, description="```\nRole not found```")
					return
				members = luna.guild.members
				for member in members:
					if role in member.roles:
						try:
							await member.send(f"You have been pruned from {luna.guild.name} for {reason}")
							await member.kick(reason=reason)
						except Exception:
							pass
				await embed_builder(luna, description=f"```\nPruned {len(members)} members```")
			except Exception:
				pass
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "pruneban",
					usage="<@role> [reason]",
					description = "Prune & ban a role")
	async def pruneban(self, luna, role, *, reason: str = None):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				if reason is None:
					reason = "No reason provided"
				else:
					reason = reason
				role = luna.guild.get_role(role)
				if role is None:
					await error_builder(luna, description="```\nRole not found```")
					return
				members = luna.guild.members
				for member in members:
					if role in member.roles:
						try:
							await member.send(f"You have been pruned and banned from {luna.guild.name} for {reason}")
							await member.ban(reason=reason)
						except Exception:
							pass
				await embed_builder(luna, description=f"```\nPruned and banned {len(members)} members```")
			except Exception:
				pass
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

bot.add_cog(MassCog(bot))
class GuildCog(commands.Cog, name="Guild commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "renamechannels",
					usage="<name>",
					description = "Rename all channels")
	async def renamechannels(self, luna, name:str):
		if configs.risk_mode() == "on":
			try:
				for channel in luna.guild.channels:
					await channel.edit(name=name)
					await asyncio.sleep(1)
				await embed_builder(luna, title="Success", description=f"```\nRenamed all channels to {name}```")
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "delchannels",
					usage="",
					description = "Delete all channels")
	async def delchannels(self, luna):
		if configs.risk_mode() == "on":
			try:
				for channel in luna.guild.channels:
					if channel.name != "general":
						await channel.delete()
				await embed_builder(luna, title="Success", description="```\nDeleted all channels```")
			except Exception as e:
				await error_builder(luna, description=e)

	@commands.command(name = "delroles",
					usage="",
					description = "Delete all roles")
	async def delroles(self, luna):
		if configs.risk_mode() == "on":
			try:
				for role in luna.guild.roles:
					if role.name != "@everyone":
						await role.delete()
				await embed_builder(luna, title="Success", description="```\nDeleted all roles```")
			except Exception as e:
				await error_builder(luna, description=e)

	@commands.command(name = "delemojis",
					usage="",
					description = "Delete all emojis")
	async def delemojis(self, luna):
		if configs.risk_mode() == "on":
			try:
				for emoji in luna.guild.emojis:
					await emoji.delete()
				await embed_builder(luna, title="Success", description="```\nDeleted all emojis```")
			except Exception as e:
				await error_builder(luna, description=e)

bot.add_cog(GuildCog(bot))
class AbuseCog(commands.Cog, name="Abusive commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "purgehack",
					usage="",
					description = "Purge a channel")
	async def purgehack(self, luna):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
			await luna.send("​​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n​\n")
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "mpreact",
					usage="<emoji>",
					description = "Reacts the last 20 messages")
	async def mpreact(self, luna, emoji):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			messages = await luna.message.channel.history(limit=20).flatten()
			for message in messages:
				await message.add_reaction(emoji)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

	@commands.command(name = "junknick",
					usage="",
					description = "Pure junk nickname")
	async def junknick(self, luna):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫"
				await luna.author.edit(nick=name)
			except Exception as e:
				await error_builder(luna, description=e)
		else:
			await error_builder(luna, description="```\nRiskmode is disabled```")

bot.add_cog(AbuseCog(bot))

class RaidCog(commands.Cog, name="Raid commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "tokencheck",
					usage="",
					description = "Check the tokens.txt")
	async def tokencheck(self, luna):
		await luna.message.delete()

		file = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), "r")
		nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
		line_count = len(nonempty_lines)
		file.close()

		if os.stat(os.path.join(files.documents(), "Luna/raiding/tokens.txt")).st_size == 0:
			embed = discord.Embed(title="Token check", url=theme.title_url(), description=f"```\ntokens.txt is empty...```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)
			return

		if configs.mode() == 2:
			sent = await luna.send(f"```ini\n[ Token check ]\n\nDetected {line_count} tokens.\nChecking tokens...\n\n[ {theme.footer()} ]```")
		else:
			embed = discord.Embed(title="Token check", url=theme.title_url(), description=f"```\nDetected {line_count} tokens.\nChecking tokens...```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			sent = await luna.send(embed=embed)

		valid_tokens=[]
		success = 0
		failed = 0

		with open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"),"r+") as f:
			for line in f:
				token=line.strip("\n")
				headers = {'Content-Type': 'application/json', 'authorization': token}
				url = "https://discordapp.com/api/v6/users/@me/library"
				request = requests.get(url, headers=headers)
				if request.status_code == 200:
					valid_tokens.append(token)
					success += 1
				else:
					failed += 1
					pass

		with open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"),"w+") as f:
			for i in valid_tokens:
				f.write(i+"\n")

		if configs.mode() == 2:
			await sent.edit(f"```ini\n[ Token check ]\n\nSuccessfully checked all tokens and removed invalid ones.\nValid tokens » "+str(success)+"\nInvalid tokens » "+str(failed)+"\n\n[ {theme.footer()} ]```")
			await asyncio.sleep(configs.delete_timer())
			await sent.delete() 
		else:
			embed = discord.Embed(title="Token check", url=theme.title_url(), description=f"```\nSuccessfully checked all tokens and removed invalid ones.\n``````\nValid tokens » "+str(success)+"\nInvalid tokens » "+str(failed)+"```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await sent.edit(embed=embed)
			await asyncio.sleep(configs.delete_timer())
			await sent.delete() 

	@commands.command(name = "raidjoin",
					usage="<invitelink>",
					description = "Raid the server")
	async def raidjoin(self, luna, invitelink:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.post(f'https://canary.discord.com/api/v8/invites/{invitelink}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
						prints.event(f"{_token} joined {invitelink}")
				except Exception:
					prints.error(f"{_token} failed to join {invitelink}")
					pass
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "proxyjoin",
					usage="<invitelink>",
					description = "Raid the server")
	async def proxyjoin(self, luna, invitelink:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":

			tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
			proxies = open(os.path.join(files.documents(), "Luna/raiding/proxies.txt"), 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)
				
			for p, _token in enumerate(tokens):
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.post(f'https://canary.discord.com/api/v8/invites/{invitelink}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http://': f'http://{proxylist[p]}'})
						prints.event(f"[PROXY] {_token} joined {invitelink}")
				except Exception:
					prints.error(f"[PROXY] {_token} failed to join {invitelink}")
					pass
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "raidspam",
					usage="<channel_id> <amount> <message>",
					description = "Spam")
	async def raidspam(self, luna, channel_id:str, amount:int, *, message:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":

			tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						for i in range(0, amount):
							await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{message}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
							prints.event(f"{_token} sent {message}")
				except Exception:
					prints.error(f"{_token} failed to send {message}")
					pass
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "proxyspam",
					usage="<channel_id> <amount> <message>",
					description = "Spam")
	async def proxyspam(self, luna, channel_id:str, amount:int, *, message:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":

			tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
			proxies = open(os.path.join(files.documents(), "Luna/raiding/proxies.txt"), 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)

			tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						for i in range(0, amount):
							await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{message}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http://': f'http://{proxylist[p]}'})
							prints.event(f"{_token} sent {message}")
				except Exception:
					prints.error(f"{_token} failed to send {message}")
					pass
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "raidmassping",
					usage="<channel_id> <delay> <amount>",
					description = "Massping")
	async def raidmassping(self, luna, channel_id:str, delay:int, amount:int):
		await luna.message.delete()
		tokenposition = 0
		if configs.risk_mode() == "on":
			try:
				for i in range(amount):
					members = [m.mention for m in luna.guild.members]
					if len(members) < 30:
						mentionamount = len(members)
					else:
						mentionamount = 30
					sendamount = len(members) - mentionamount
					for i in range(sendamount):
						if mentionamount == 0:
							break
						pingtext = ""
						for i in range(mentionamount):
							pingtext += members.pop()

						tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
						for _token in tokens:
							_token = _token.split('\n')
							_token = _token[tokenposition]
						try:
							async with httpx.AsyncClient() as client:
								for i in range(0, amount):
									await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{pingtext}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
									prints.event(f"{_token} masspinged")
						except Exception:
							prints.error(f"{_token} failed to massping")
							pass
						tokenposition += 1
						await asyncio.sleep(delay)
						if len(members) < 10:
							mentionamount = len(members)
						else:
							mentionamount = 10
						sendamount = len(members) - mentionamount
			except Exception as e:
				prints.error(f"{e}")
		else:
			if configs.error_log() == "console":
				prints.error("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)

	@commands.command(name = "raidmassping",
					usage="<channel_id> <delay> <amount>",
					description = "Massping")
	async def raidmassping(self, luna, channel_id:str, delay:int, amount:int):
		await luna.message.delete()
		tokenposition = 0
		if configs.risk_mode() == "on":
			try:
				for i in range(amount):
					members = [m.mention for m in luna.guild.members]
					if len(members) < 30:
						mentionamount = len(members)
					else:
						mentionamount = 30
					sendamount = len(members) - mentionamount
					for i in range(sendamount):
						if mentionamount == 0:
							break
						pingtext = ""
						for i in range(mentionamount):
							pingtext += members.pop()

						tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
						for _token in tokens:
							_token = _token.split('\n')
							_token = _token[tokenposition]
						try:
							async with httpx.AsyncClient() as client:
								for i in range(0, amount):
									await client.post(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages', json={'content': f'{pingtext}', 'tts': 'false'}, headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
									prints.event(f"{_token} masspinged")
						except Exception:
							prints.error(f"{_token} failed to massping")
							pass
						tokenposition += 1
						await asyncio.sleep(delay)
						if len(members) < 10:
							mentionamount = len(members)
						else:
							mentionamount = 10
						sendamount = len(members) - mentionamount
			except Exception as e:
				prints.error(f"{e}")
		else:
			if configs.error_log() == "console":
				prints.error("Riskmode is disabled")
			else:
				embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
				embed.set_thumbnail(url=theme.image_url())
				embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
				embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
				embed.set_image(url=theme.large_image_url())
				await send(luna, embed)

	@commands.command(name = "raidleave",
					usage="<server_id>",
					description = "Leave the tokens")
	async def raidleave(self, luna, server_id:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":

			tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.delete(f'https://canary.discord.com/api/v8/users/@me/guilds/{server_id}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
						prints.event(f"{_token} left {server_id}")
				except Exception:
					prints.error(f"{_token} failed to leave {server_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "proxyleave",
					usage="<server_id>",
					description = "Leave the tokens")
	async def proxyleave(self, luna, server_id:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":

			tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
			proxies = open(os.path.join(files.documents(), "Luna/raiding/proxies.txt"), 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)

			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.delete(f'https://canary.discord.com/api/v8/users/@me/guilds/{server_id}', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http://': f'http://{proxylist[p]}'})
						prints.event(f"[PROXY] {_token} left {server_id}")
				except Exception:
					prints.error(f"[PROXY] {_token} failed to leave {server_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "raidreact",
					usage="<channel_id> <message_id> <emoji>",
					description = "Raid react on a message")
	async def raidreact(self, luna, channel_id: str, message_id: str, emoji: str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.put(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages/{message_id}/reactions/{urllib.parse.quote(emoji)}/%40me', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'})
						prints.event(f"{_token} reacted on {message_id}")
				except Exception:
					prints.error(f"{_token} failed to react on {message_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "proxyreact",
					usage="<channel_id> <message_id> <emoji>",
					description = "Raid react on a message")
	async def proxyreact(self, luna, channel_id: str, message_id: str, emoji: str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			tokens = open(os.path.join(files.documents(), "Luna/raiding/tokens.txt"), 'r')
			proxies = open(os.path.join(files.documents(), "Luna/raiding/proxies.txt"), 'r')
			
			proxylist = []
			
			for p, _proxy in enumerate(proxies):
				proxy = _proxy.split('\n')[0]
				proxylist.append(proxy)

			for _token in tokens:
				_token = _token.split('\n')
				_token = _token[0]
				try:
					async with httpx.AsyncClient() as client:
						await client.put(f'https://canary.discord.com/api/v8/channels/{channel_id}/messages/{message_id}/reactions/{urllib.parse.quote(emoji)}/%40me', headers={'authorization': _token, 'user-agent': 'Mozilla/5.0'}, proxies={'http://': f'http://{proxylist[p]}'})
						prints.event(f"{_token} reacted on {message_id}")
				except Exception:
					prints.error(f"{_token} failed to react on {message_id}")
					pass
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

bot.add_cog(RaidCog(bot))

start = datetime.now()

class NukingCog(commands.Cog, name="Nuking commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "nuketoken",
					usage="<token>",
					description = "Nuke the token")
	async def nuketoken(self, luna, token:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			try:
				guilds = requests.get('https://discordapp.com/api/v9/users/@me/guilds', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
				for guild in range(0, len(guilds)):
					guild_id = guilds[guild]['id']
					requests.delete(f'https://discordapp.com/api/v9/users/@me/guilds/{guild_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
				friends = requests.get('https://discordapp.com/api/v9/users/@me/relationships', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
				for friend in range(0, len(friends)):
					friend_id = friends[friend]['id']
					requests.put(f'https://discordapp.com/api/v9/users/@me/relationships/{friend_id}', json={'type': 2}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
					requests.delete(f'https://discordapp.com/api/v9/channels/{friend_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
			except Exception:
				pass
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "messtoken",
					usage="<token>",
					description = "Mess up the token")
	async def messtoken(self, luna, token:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			payload = {
				'theme': "light",
				'locale': "ja",
				'message_display_compact': False,
				'inline_embed_media': False,
				'inline_attachment_media': False,
				'gif_auto_play': False,
				'render_embeds': False,
				'render_reactions': False,
				'animate_emoji': False,
				'convert_emoticons': False,
				'enable_tts_command': False,
				'explicit_content_filter': '0',
				'status': "invisible"
			}
			
			requests.patch('https://discordapp.com/api/v9/users/@me/settings', json=payload, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
			try:
				while True:
					async with httpx.AsyncClient() as client:
						await client.patch('https://discordapp.com/api/v9/users/@me/settings', json={'theme': "light"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
						await client.patch('https://discordapp.com/api/v9/users/@me/settings', json={'theme': "dark"}, headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
			except Exception:
				return
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)
        
	@commands.command(name = "massban",
					usage="<guild_id>",
					description = "Massban a guild")
	@has_permissions(ban_members=True)
	async def massban(self, luna, guild_id:int):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			guild_id = int(guild_id)
			guildhit = self.bot.get_guild(guild_id)
			members = guildhit.members
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for member in members:
				if member is not luna.author:
					try:
						count = count + 1
						await member.ban()
						prints.message(f"Banned » {color.purple(member)}")
					except Exception:
						prints.error(f"Failed to ban » {color.purple(member)}")
			prints.message(f"Finished banning in » {color.purple(elapsed)}ms")
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "masskick",
					usage="<guild_id>",
					description = "Masskick a guild")
	@has_permissions(kick_members=True)
	async def masskick(self, luna, guild_id:int):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			guild_id = int(guild_id)
			guildhit = self.bot.get_guild(guild_id)
			members = guildhit.members
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for member in members:
				if member is not luna.author:
					try:
						count = count + 1
						await member.kick()
						prints.message(f"Kicked » {color.purple(member)}")
					except Exception:
						prints.error(f"Failed to kick » {color.purple(member)}")
			prints.message(f"Finished kicking in » {color.purple(elapsed)}ms")
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			await send(luna, embed)

	@commands.command(name = "annihilate",
					aliases=['destroy', 'wipe', 'nukeserver'],
					usage="<guild_id> <channel_name> <role_name>",
					description = "Totally annihilate a guild")
	@has_permissions(manage_roles=True, manage_channels=True, ban_members=True)
	async def annihilate(self, luna, guild_id:int, channel_name:str, role_name:str):
		await luna.message.delete()
		if configs.risk_mode() == "on":
			guild_id = int(guild_id)
			guildhit = self.bot.get_guild(guild_id)
			members = guildhit.members
			elapsed = datetime.now() - start
			elapsed = f'{elapsed.microseconds}'
			elapsed = elapsed[:-3]
			for member in members:
				if member is not luna.author:
					try:
						count = count + 1
						await member.ban()
						prints.message(f"Banned » {color.purple(member)}")
					except Exception:
						prints.error(f"Failed to ban » {color.purple(member)}")
			prints.message(f"Finished banning in » {color.purple(elapsed)}ms")
			for channel in guildhit.channels:
				if channel.name == channel_name:
					try:
						await channel.delete()
						prints.message(f"Deleted channel » {color.purple(channel)}")
					except Exception:
						prints.error(f"Failed to delete channel » {color.purple(channel)}")
			for role in guildhit.roles:
				if role.name == role_name:
					try:
						await role.delete()
						prints.message(f"Deleted role » {color.purple(role)}")
					except Exception:
						prints.error(f"Failed to delete role » {color.purple(role)}")
			prints.message(f"Finished deleting in » {color.purple(elapsed)}ms")
		else:
			embed = discord.Embed(title="Error", url=theme.title_url(), description=f"```\nRiskmode is disabled```", color=0xff0000)

bot.add_cog(NukingCog(bot))
class PrivacyCog(commands.Cog, name="Privacy commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "privacy",
					aliases=['streamermode'],
					usage="<on/off>",
					description = "Privacy mode")
	async def privacy(self, ctx, mode:str):
		await ctx.message.delete()

		global privacy

		if mode == "on" or mode == "off":
			luna.console(clear=True)
			if mode == "on":
				privacy = True
				command_count = len(bot.commands)
				cog = bot.get_cog('Custom commands')
				try:
					custom = cog.get_commands()
					custom_command_count = 0
					for command in custom:
						custom_command_count += 1
				except:
					custom_command_count = 0
				print(motd.center(os.get_terminal_size().columns))
				if beta:
					print("Beta Build".center(os.get_terminal_size().columns))
				prefix = files.json("Luna/config.json", "prefix", documents=True)
				console_mode = files.json("Luna/console/console.json", "mode", documents=True)
				if console_mode == "2":
					riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
					themesvar = files.json("Luna/config.json", "theme", documents=True)
					deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
					startup_status = files.json("Luna/config.json", "startup_status", documents=True)
					nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
					giveawayjoiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
					if themesvar == "default":
						pass
					else:
						themesvar = themesvar[:-5]
					ui_user = f" {color.purple('User:')} {'Luna#0000':<26}"
					ui_guilds = f" {color.purple('Guilds:')} {'0':<24}"
					ui_friends = f" {color.purple('Friends:')} {'0':<23}"
					ui_prefix = f" {color.purple('Prefix:')} {prefix:<24}"
					ui_theme = f" {color.purple('Theme:')} {themesvar:<25}"
					ui_commands = f" {color.purple('Commands:')} {command_count-custom_command_count:<22}"
					ui_commands_custom = f" {color.purple('Custom Commands:')} {custom_command_count:<15}"
					ui_nitro_sniper = f" {color.purple('Nitro Sniper:')} {nitro_sniper}"
					ui_giveaway_sniper = f" {color.purple('Giveaway Joiner:')} {giveawayjoiner}"
					ui_riskmode = f" {color.purple('Riskmode:')} {riskmode}"
					ui_deletetimer = f" {color.purple('Delete Timer:')} {deletetimer}"
					ui_startup = f" {color.purple('Startup Status:')} {startup_status}"
					print()
					print(f"               ═════════════ {color.purple('User')} ═════════════      ═══════════ {color.purple('Settings')} ═══════════")
					print(f"               {ui_user}     {ui_prefix}")
					print(f"               {ui_guilds}     {ui_theme}")
					print(f"               {ui_friends}     {ui_nitro_sniper}")
					print(f"               ════════════════════════════════      {ui_giveaway_sniper}")
					print(f"               ═════════════ {color.purple('Luna')} ═════════════      {ui_riskmode}")
					print(f"               {ui_commands}     {ui_deletetimer}")
					print(f"               {ui_commands_custom}     {ui_startup}")
					print(f"               ════════════════════════════════      ════════════════════════════════\n")
				else:
					print()
					print(f"                           {color.purple('[')}+{color.purple('] CONNECTED')}")
					print(f"                           {color.purple('[')}+{color.purple(']')} Luna#0000 | {color.purple('0')} Guilds | {color.purple('0')} Friends")
					print(f"                           {color.purple('[')}+{color.purple(']')} {prefix}\n")
			else:
				privacy = False
				command_count = len(bot.commands)
				cog = bot.get_cog('Custom commands')
				try:
					custom = cog.get_commands()
					custom_command_count = 0
					for command in custom:
						custom_command_count += 1
				except:
					custom_command_count = 0
				print(motd.center(os.get_terminal_size().columns))
				if beta:
					print("Beta Build".center(os.get_terminal_size().columns))
				prefix = files.json("Luna/config.json", "prefix", documents=True)
				console_mode = files.json("Luna/console/console.json", "mode", documents=True)
				if console_mode == "2":
					riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
					themesvar = files.json("Luna/config.json", "theme", documents=True)
					deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
					startup_status = files.json("Luna/config.json", "startup_status", documents=True)
					nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
					giveawayjoiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
					if themesvar == "default":
						pass
					else:
						themesvar = themesvar[:-5]
					bot_user = f"{bot.user}"
					ui_user = f" {color.purple('User:')} {bot_user:<26}"
					ui_guilds = f" {color.purple('Guilds:')} {len(bot.guilds):<24}"
					ui_friends = f" {color.purple('Friends:')} {len(bot.user.friends):<23}"
					ui_prefix = f" {color.purple('Prefix:')} {prefix:<24}"
					ui_theme = f" {color.purple('Theme:')} {themesvar:<25}"
					ui_commands = f" {color.purple('Commands:')} {command_count-custom_command_count:<22}"
					ui_commands_custom = f" {color.purple('Custom Commands:')} {custom_command_count:<15}"
					ui_nitro_sniper = f" {color.purple('Nitro Sniper:')} {nitro_sniper}"
					ui_giveaway_sniper = f" {color.purple('Giveaway Joiner:')} {giveawayjoiner}"
					ui_riskmode = f" {color.purple('Riskmode:')} {riskmode}"
					ui_deletetimer = f" {color.purple('Delete Timer:')} {deletetimer}"
					ui_startup = f" {color.purple('Startup Status:')} {startup_status}"
					print()
					print(f"               ═════════════ {color.purple('User')} ═════════════      ═══════════ {color.purple('Settings')} ═══════════")
					print(f"               {ui_user}     {ui_prefix}")
					print(f"               {ui_guilds}     {ui_theme}")
					print(f"               {ui_friends}     {ui_nitro_sniper}")
					print(f"               ════════════════════════════════      {ui_giveaway_sniper}")
					print(f"               ═════════════ {color.purple('Luna')} ═════════════      {ui_riskmode}")
					print(f"               {ui_commands}     {ui_deletetimer}")
					print(f"               {ui_commands_custom}     {ui_startup}")
					print(f"               ════════════════════════════════      ════════════════════════════════\n")
				else:
					print()
					print(f"                           {color.purple('[')}+{color.purple('] CONNECTED')}")
					print(f"                           {color.purple('[')}+{color.purple(']')} {bot.user} | {color.purple(f'{len(bot.guilds)}')} Guilds | {color.purple(f'{len(bot.user.friends)}')} Friends")
					print(f"                           {color.purple('[')}+{color.purple(']')} {prefix}\n")
			print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
			prints.message(f"{color.purple(f'{command_count-custom_command_count}')} commands | {color.purple(f'{custom_command_count}')} custom commands")
			prints.message(f"Privacy mode » {color.purple(f'{mode}')}")
			await embed_builder(ctx, description=f"```\Privacy mode » {mode}```")
		else:
			await mode_error(ctx, "on or off")

bot.add_cog(PrivacyCog(bot))
class ProtectionGuildCog(commands.Cog, name="Protection Guild commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "pguilds",
					aliases=['pguild', 'protectguild'],
					usage="<guild_id>",
					description = "Protect a guild")
	async def pguilds(self, luna, guild_id:int):
		await luna.message.delete()
		try:
			self.bot.get_guild(guild_id)
		except:
			await error_builder(luna, description="Invalid guild")
			return
		config._global("Luna/protections/config.json", "guilds", guild_id, add=True)
		prints.message(f"Added » {color.purple(f'{guild_id}')} to the list of protected guilds")
		await embed_builder(luna, description=f"```\nAdded » {guild_id} to the list of protected guilds```")
	
	@commands.command(name = "rguilds",
					aliases=['rguild', 'removeguild'],
					usage="<guild_id>",
					description = "Remove a protected guild")
	async def rguilds(self, luna, guild_id:int):
		await luna.message.delete()
		try:
			self.bot.get_guild(guild_id)
		except:
			await error_builder(luna, description="Invalid guild")
			return
		config._global("Luna/protections/config.json", "guilds", guild_id, delete=True)
		prints.message(f"Removed » {color.purple(f'{guild_id}')} from the list of protected guilds")
		await embed_builder(luna, description=f"```\nRemoved » {guild_id} from the list of protected guilds```")

bot.add_cog(ProtectionGuildCog(bot))
class ProtectionCog(commands.Cog, name="Protection commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "pfooter",
					usage="<on/off>",
					description = "Protections footer info")
	async def pfooter(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Protections footer info » {color.purple(f'{mode}')}")
			if mode == "on":
				config._global("Luna/protections/config.json", "footer", True)
			else:
				config._global("Luna/protections/config.json", "footer", False)
			await embed_builder(luna, description=f"```\nProtections footer info » {mode}```")
		else:
			await mode_error(luna, "on or off")
		
	@commands.command(name = "antiraid",
					usage="<on/off>",
					description = "Protects against raids")
	async def antiraid(self, luna, mode:str):
		await luna.message.delete()
		global antiraid
		global active_protections
		global active_list
		if mode == "on" or mode == "off":
			prints.message(f"Antiraid » {color.purple(f'{mode}')}")
			if mode == "on":
				antiraid = True
				active_protections += 1
				active_list.append("antiraid")
			else:
				antiraid = False
				active_protections -= 1
				active_list.remove("antiraid")
			await embed_builder(luna, description=f"```\nAntiraid » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "antiinvite",
					usage="<on/off>",
					description = "Protects against invites")
	async def antiinvite(self, luna, mode:str):
		await luna.message.delete()
		global antiinvite
		global active_protections
		global active_list
		if mode == "on" or mode == "off":
			prints.message(f"Antiinvite » {color.purple(f'{mode}')}")
			if mode == "on":
				antiinvite = True
				active_protections += 1
				active_list.append("antiinvite")
			else:
				antiinvite = False
				active_protections -= 1
				active_list.remove("antiinvite")
			await embed_builder(luna, description=f"```\nAntiinvite » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "antiupper",
					usage="<on/off>",
					description = "Protects against uppercase")
	async def antiupper(self, luna, mode:str):
		await luna.message.delete()
		global antiupper
		global active_protections
		global active_list
		if mode == "on" or mode == "off":
			prints.message(f"Antiupper » {color.purple(f'{mode}')}")
			if mode == "on":
				antiupper = True
				active_protections += 1
				active_list.append("antiupper")
			else:
				antiupper = False
				active_protections -= 1
				active_list.remove("antiupper")
			await embed_builder(luna, description=f"```\nAntiupper » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "antiphishing",
					usage="<on/off>",
					description = "Protects against phishing")
	async def antiphishing(self, luna, mode:str):
		await luna.message.delete()
		global antiphishing
		global active_protections
		global active_list
		if mode == "on" or mode == "off":
			prints.message(f"Anti phishing links » {color.purple(f'{mode}')}")
			if mode == "on":
				antiphishing = True
				active_protections += 1
				active_list.append("Anti Phishing Links")
			else:
				antiphishing = False
				active_protections -= 1
				active_list.remove("Anti Phishing Links")
			await embed_builder(luna, description=f"```\nAnti phishing links » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "sbcheck",
					usage="",
					description = "Check for bad selfbots")
	async def sbcheck(self, luna):
		await luna.message.delete()
		await embed_builder(luna, title="GIVEAWAY")
		await embed_builder(luna, description="```\nThose that reacted, could be running selfbots```")

bot.add_cog(ProtectionCog(bot))
class BackupsCog(commands.Cog, name="Backup commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "backupserver",
					usage="",
					description = "Backup the server")
	async def backupserver(self, luna):
		await luna.message.delete()
		serverName = luna.guild.name

		newGuild = await self.bot.create_guild(serverName)
		prints.info(f"Created new guild")
		newGuildDefaultChannels = await newGuild.fetch_channels()
		for channel in newGuildDefaultChannels:
			await channel.delete()

		for channel in luna.guild.channels:
			if str(channel.type).lower() == "category":
				try:
					await newGuild.create_category(channel.name, overwrites=channel.overwrites, position=channel.position)
					prints.info(f"Created new category » {channel.name}")
				except:
					pass
				
		for channel in luna.guild.voice_channels:
			try:
				cat = ""
				for category in newGuild.categories:
					if channel.category.name == category.name:
						cat = category
						
				await newGuild.create_voice_channel(channel.name, category=cat, overwrites=channel.overwrites, topic=channel.topic, slowmode_delay=channel.slowmode_delay, nsfw=channel.nsfw, position=channel.position)
				prints.info(f"Created new voice channel » {channel.name}")
			except:
				pass

		for channel in luna.guild.stage_channels:
			try:
				cat = ""
				for category in newGuild.categories:
					if channel.category.name == category.name:
						cat = category                    
				await newGuild.create_stage_channel(channel.name, category=cat, overwrites=channel.overwrites, topic=channel.topic, slowmode_delay=channel.slowmode_delay, nsfw=channel.nsfw, position=channel.position)
				prints.info(f"Created new stage channel » {channel.name}")
			except:
				pass
			
		for channel in luna.guild.text_channels:
			try:
				cat = ""
				for category in newGuild.categories:
					if channel.category.name == category.name:
						cat = category                            
				await newGuild.create_text_channel(channel.name, category=cat, overwrites=channel.overwrites, topic=channel.topic, slowmode_delay=channel.slowmode_delay, nsfw=channel.nsfw, position=channel.position)
				prints.info(f"Created new text channel » {channel.name}")
			except:
				pass

		for role in luna.guild.roles[::-1]:
			if role.name != "@everyone":
				try:
					await newGuild.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
					prints.info(f"Created new role » {role.name}")
				except:
					pass

		await embed_builder(luna, description=f"```\nCloned {luna.guild.name}```")

	@commands.command(name = "friendsbackup",
					usage="",
					description = "Backup your friendslist")
	async def friendsbackup(self, luna):
		await luna.message.delete()
		prints.event("Backing up friendslist...")
		friendsamount = 0
		blockedamount = 0
		friendslist = ""
		blockedlist = ""
		for friend in self.bot.user.friends:
			friendslist += f"{friend.name}#{friend.discriminator}\n"
			friendsamount += 1 
		file = open(os.path.join(files.documents(), "Luna/backup/friends.txt"), "w", encoding='utf-8')
		file.write(friendslist)
		file.close()
		for block in self.bot.user.blocked:
			blockedlist += f"{block.name}#{block.discriminator}\n"
			blockedamount += 1
		file = open(os.path.join(files.documents(), "Luna/backup/blocked.txt"), "w", encoding='utf-8')
		file.write(blockedlist)
		file.close()
		prints.message(f"Friendslist backed up. Friends » {friendsamount} Blocked » {blockedamount}")
		await embed_builder(luna, description=f"```\nBacked up {friendsamount} friends in Documents/Luna/backup/friends.txt\nBacked up {blockedamount} blocked users in Documents/Luna/backup/blocked.txt```")

bot.add_cog(BackupsCog(bot))
class WhitelistCog(commands.Cog, name="Whitelist commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "whitelist",
					usage="<@member>",
					description = "Whitelist someone")
	async def whitelist(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			await luna.send("Please specify a user to whitelist")
		else:
			if luna.guild.id not in whitelisted_users.keys():
				whitelisted_users[luna.guild.id] = {}
			if user.id in whitelisted_users[luna.guild.id]:
				await embed_builder(luna, description=f"```\n{user.name}#{user.discriminator} is already whitelisted```")
			else:
				whitelisted_users[luna.guild.id][user.id] = 0
				await embed_builder(luna, description=f"```\nWhitelisted " + user.name.replace("*", "\*").replace("`", "\`").replace("_", "\_") + "#" + user.discriminator + "```")

	@commands.command(name = "unwhitelist",
					usage="",
					description = "Unwhitelist someone")
	async def unwhitelist(self, luna, user: discord.Member = None):
		await luna.message.delete()
		if user is None:
			await luna.send("Please specify the user you would like to unwhitelist")
		else:
			if luna.guild.id not in whitelisted_users.keys():
				await luna.send("That user is not whitelisted")
				return
			if user.id in whitelisted_users[luna.guild.id]:
				whitelisted_users[luna.guild.id].pop(user.id, 0)
				user2 = self.bot.get_user(user.id)
				await embed_builder(luna, description=f"```\nUnwhitelisted " + user.name.replace("*", "\*").replace("`", "\`").replace("_", "\_") + "#" + user.discriminator + "```")

	@commands.command(name = "whitelisted",
					usage="",
					description = "Show the whitelisted list")
	async def whitelisted(self, luna, g=None):
		await luna.message.delete()
		if g == '-g' or g == '-global':
			whitelist = '`All Whitelisted Users:`\n'
			for key in whitelisted_users:
				for key2 in whitelisted_users[key]:
					user = self.bot.get_user(key2)
					whitelist += '+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "#" + user.discriminator + " - " + self.bot.get_guild(key).name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "" + "\n"
			await embed_builder(luna, description=f"```\n{whitelist}```")
		else:
			whitelist = "`" + luna.guild.name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + '\'s Whitelisted Users:`\n'
			for key in self.bot.whitelisted_users:
				if key == luna.guild.id:
					for key2 in self.bot.whitelisted_users[luna.guild.id]:
						user = self.bot.get_user(key2)
						whitelist += '+ ' + user.name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "#" + user.discriminator + " (" + str(user.id) + ")" + "\n"
			await embed_builder(luna, description=f"```\n{whitelist}```")

	@commands.command(name = "clearwhitelist",
					usage="",
					description = "Clear the whitelisted list")
	async def clearwhitelist(self, luna):
		await luna.message.delete()
		whitelisted_users.clear()
		await embed_builder(luna, description=f"```\nCleared the whitelist```")

bot.add_cog(WhitelistCog(bot))
class SettingsCog(commands.Cog, name="Settings commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "prefix",
					usage="<prefix>",
					description = "Change the prefix")
	async def prefix(self, ctx, newprefix):
		await ctx.message.delete()
		config.prefix(newprefix)
		luna.console(clear=True)
		if privacy:
			command_count = len(bot.commands)
			cog = bot.get_cog('Custom commands')
			try:
				custom = cog.get_commands()
				custom_command_count = 0
				for command in custom:
					custom_command_count += 1
			except:
				custom_command_count = 0
			print(motd.center(os.get_terminal_size().columns))
			if beta:
				print("Beta Build".center(os.get_terminal_size().columns))
			console_mode = files.json("Luna/console/console.json", "mode", documents=True)
			if console_mode == "2":
				riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
				themesvar = files.json("Luna/config.json", "theme", documents=True)
				deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
				startup_status = files.json("Luna/config.json", "startup_status", documents=True)
				nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
				giveawayjoiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
				if themesvar == "default":
					pass
				else:
					themesvar = themesvar[:-5]
				ui_user = f" {color.purple('User:')} {'Luna#0000':<26}"
				ui_guilds = f" {color.purple('Guilds:')} {'0':<24}"
				ui_friends = f" {color.purple('Friends:')} {'0':<23}"
				ui_prefix = f" {color.purple('Prefix:')} {newprefix:<24}"
				ui_theme = f" {color.purple('Theme:')} {themesvar:<25}"
				ui_commands = f" {color.purple('Commands:')} {command_count-custom_command_count:<22}"
				ui_commands_custom = f" {color.purple('Custom Commands:')} {custom_command_count:<15}"
				ui_nitro_sniper = f" {color.purple('Nitro Sniper:')} {nitro_sniper}"
				ui_giveaway_sniper = f" {color.purple('Giveaway Joiner:')} {giveawayjoiner}"
				ui_riskmode = f" {color.purple('Riskmode:')} {riskmode}"
				ui_deletetimer = f" {color.purple('Delete Timer:')} {deletetimer}"
				ui_startup = f" {color.purple('Startup Status:')} {startup_status}"
				print()
				print(f"               ═════════════ {color.purple('User')} ═════════════      ═══════════ {color.purple('Settings')} ═══════════")
				print(f"               {ui_user}     {ui_prefix}")
				print(f"               {ui_guilds}     {ui_theme}")
				print(f"               {ui_friends}     {ui_nitro_sniper}")
				print(f"               ════════════════════════════════      {ui_giveaway_sniper}")
				print(f"               ═════════════ {color.purple('Luna')} ═════════════      {ui_riskmode}")
				print(f"               {ui_commands}     {ui_deletetimer}")
				print(f"               {ui_commands_custom}     {ui_startup}")
				print(f"               ════════════════════════════════      ════════════════════════════════\n")
			else:
				print()
				print(f"                           {color.purple('[')}+{color.purple('] CONNECTED')}")
				print(f"                           {color.purple('[')}+{color.purple(']')} Luna#0000 | {color.purple('0')} Guilds | {color.purple('0')} Friends")
				print(f"                           {color.purple('[')}+{color.purple(']')} {newprefix}\n")
		else:
			command_count = len(bot.commands)
			cog = bot.get_cog('Custom commands')
			try:
				custom = cog.get_commands()
				custom_command_count = 0
				for command in custom:
					custom_command_count += 1
			except:
				custom_command_count = 0
			print(motd.center(os.get_terminal_size().columns))
			if beta:
				print("Beta Build".center(os.get_terminal_size().columns))
			console_mode = files.json("Luna/console/console.json", "mode", documents=True)
			if console_mode == "2":
				riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
				themesvar = files.json("Luna/config.json", "theme", documents=True)
				deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
				startup_status = files.json("Luna/config.json", "startup_status", documents=True)
				nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
				giveawayjoiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
				if themesvar == "default":
					pass
				else:
					themesvar = themesvar[:-5]
				bot_user = f"{bot.user}"
				ui_user = f" {color.purple('User:')} {bot_user:<26}"
				ui_guilds = f" {color.purple('Guilds:')} {len(bot.guilds):<24}"
				ui_friends = f" {color.purple('Friends:')} {len(bot.user.friends):<23}"
				ui_prefix = f" {color.purple('Prefix:')} {newprefix:<24}"
				ui_theme = f" {color.purple('Theme:')} {themesvar:<25}"
				ui_commands = f" {color.purple('Commands:')} {command_count-custom_command_count:<22}"
				ui_commands_custom = f" {color.purple('Custom Commands:')} {custom_command_count:<15}"
				ui_nitro_sniper = f" {color.purple('Nitro Sniper:')} {nitro_sniper}"
				ui_giveaway_sniper = f" {color.purple('Giveaway Joiner:')} {giveawayjoiner}"
				ui_riskmode = f" {color.purple('Riskmode:')} {riskmode}"
				ui_deletetimer = f" {color.purple('Delete Timer:')} {deletetimer}"
				ui_startup = f" {color.purple('Startup Status:')} {startup_status}"
				print()
				print(f"               ═════════════ {color.purple('User')} ═════════════      ═══════════ {color.purple('Settings')} ═══════════")
				print(f"               {ui_user}     {ui_prefix}")
				print(f"               {ui_guilds}     {ui_theme}")
				print(f"               {ui_friends}     {ui_nitro_sniper}")
				print(f"               ════════════════════════════════      {ui_giveaway_sniper}")
				print(f"               ═════════════ {color.purple('Luna')} ═════════════      {ui_riskmode}")
				print(f"               {ui_commands}     {ui_deletetimer}")
				print(f"               {ui_commands_custom}     {ui_startup}")
				print(f"               ════════════════════════════════      ════════════════════════════════\n")
			else:
				print()
				print(f"                           {color.purple('[')}+{color.purple('] CONNECTED')}")
				print(f"                           {color.purple('[')}+{color.purple(']')} {bot.user} | {color.purple(f'{len(bot.guilds)}')} Guilds | {color.purple(f'{len(bot.user.friends)}')} Friends")
				print(f"                           {color.purple('[')}+{color.purple(']')} {newprefix}\n")
		print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
		prints.message(f"{color.purple(f'{command_count-custom_command_count}')} commands | {color.purple(f'{custom_command_count}')} custom commands")
		prints.message(f"Prefix changed to {color.purple(f'{newprefix}')}")
		await embed_builder(ctx, description=f"```\nPrefix changed to {newprefix}```")

	@commands.command(name = "themes",
					usage="",
					description = "Themes")
	async def themes(self, luna):
		await luna.message.delete()
		path_to_json = os.path.join(files.documents(), 'Luna/themes/')
		json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		themesvar = files.json("Luna/config.json", "theme", documents=True)
		if themesvar == "default":
			pass
		else:
			themesvar = (themesvar[:-5])

		string = f"{json_files}"
		stringedit = string.replace(',', f"\n{prefix}theme").replace("'", "").replace('[', f"{prefix}theme ").replace(']', "").replace('.json', "")

		cog = self.bot.get_cog('Theme commands')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Themes", description=f"{theme.description()}```\nCurrent theme     » {themesvar}\n``````\nTheme customization\n\n{prefix}customize        » Theme customization\n``````\nTheme control\n\n{helptext}\n``````\nAvailable themes\n\n{prefix}theme default\n{stringedit}```")

	@commands.command(name = "customize",
					usage="",
					aliases=['customise', 'customization', 'customisation'],
					description = "Theme customization")
	async def customize(self, luna):
		await luna.message.delete()
		themevar = files.json("Luna/config.json", "theme", documents=True)
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		title = theme.title()
		footer = theme.footer()
		author = theme.author()

		if themevar == "default":
			pass
		else:
			themevar = (themevar[:-5])
		if themevar == "default":
			theme_description = descriptionvar_request
			hexcolor = hexcolorvar_request
			if not theme_description == "true":
				theme_description = "off"
			else:
				theme_description = "on"
		else:
			theme_json = files.json("Luna/config.json", "theme", documents=True)
			theme_description = files.json(f"Luna/themes/{theme_json}", "description", documents=True)
			hexcolor = files.json(f"Luna/themes/{theme_json}", "hex_color", documents=True)
			if theme_description == None:
				theme_description = True
			if not theme_description:
				theme_description = "off"
			else:
				theme_description = "on"

		if title == "":
			title = "None"
		if footer == "":
			footer = "None"
		if hexcolor == "":
			hexcolor = "None"
		if author == "":
			author = "None"

		cog = self.bot.get_cog('Customization commands')
		commands = cog.get_commands()
		helptext1 = ""
		for command in commands:
			helptext1+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Webhook customisation')
		commands = cog.get_commands()
		helptext2 = ""
		for command in commands:
			helptext2+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

		cog = self.bot.get_cog('Toast customization')
		commands = cog.get_commands()
		helptext3 = ""
		for command in commands:
			helptext3+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Customization", description=f"{theme.description()}```\nYour current theme settings\n\nTheme             » {themevar}\nFooter            » {footer}\nColor             » {hexcolor}\nAuthor            » {author}\nDescription       » {theme_description}\n``````\nSelfbot theme settings\n\n{helptext1}\n``````\nWebhook theme settings\n\n{helptext2}\n``````\nToast theme settings\n\n{helptext3}\n``````\nNote\n\nIf you want to remove a customization,\nYou can use \"None\" to remove it.\n\nIf you want to set up a random color each time\nyou run a command, you can use \"random\" as hex color.\n\nIf you want to set up your avatar as image\nUse \"avatar\" as value.```")

	@commands.command(name = "embedmode",
					usage="",
					description = "Switch to embed mode")
	async def embedmode(self, luna):
		await luna.message.delete()
		config.mode("1")
		prints.message(f"Switched to {color.purple('embed')} mode")
		await embed_builder(luna, title="Embed mode", description=f"```\nSwitched to embed mode.```")

	@commands.command(name = "textmode",
					usage="",
					description = "Switch to text mode")
	async def textmode(self, luna):
		await luna.message.delete()
		config.mode("2")
		prints.message(f"Switched to {color.purple('text')} mode")
		await embed_builder(luna, title="Text mode", description=f"```\nSwitched to text mode.```")

	@commands.command(name = "indentmode",
					usage="",
					description = "Switch to indent mode")
	async def indentmode(self, luna):
		await luna.message.delete()
		config.mode("3")
		prints.message(f"Switched to {color.purple('indent')} mode")
		await embed_builder(luna, title="Indent mode", description=f"```\nSwitched to indent mode.```")

	@commands.command(name = "sniper",
					usage="",
					description = "Sniper settings")
	async def sniper(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
		privnote_sniper = files.json("Luna/snipers/privnote.json", "sniper", documents=True)
		cog = self.bot.get_cog('Sniper settings')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Sniper settings", description=f"{theme.description()}```\nYour current settings\n\nNitro Sniper      » {nitro_sniper}\nPrivnote Sniper   » {privnote_sniper}\n``````\nSettings\n\n{helptext}```")

	@commands.command(name = "giveaway",
					usage="",
					description = "Giveaway settings")
	async def giveaway(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		giveaway_joiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
		delay_in_minutes = files.json("Luna/snipers/giveaway.json", "delay_in_minutes", documents=True)
		guild_joiner = files.json("Luna/snipers/giveaway.json", "guild_joiner", documents=True)

		cog = self.bot.get_cog('Giveaway settings')
		commands = cog.get_commands()
		helptext = ""
		for command in commands:
			helptext+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
		await embed_builder(luna, title="Giveaway settings", description=f"{theme.description()}```\nYour current settings\n\nGiveaway Joiner   » {giveaway_joiner}\nDelay             » {delay_in_minutes} minute/s\nServer Joiner     » {guild_joiner}\n``````\nSettings\n\n{helptext}```")

	@commands.command(name = "errorlog",
					usage="<console/message>",
					description = "Switch errorlog")
	async def errorlog(self, luna, mode:str):
		await luna.message.delete()
		if mode == "message" or mode == "console":
			prints.message(f"Error logging » {color.purple(f'{mode}')}")
			configs.error_log()(mode)
			await embed_builder(luna, description=f"```\nError logging » {mode}```")
		else:
			await mode_error(luna, "message or console")

	@commands.command(name = "deletetimer",
					usage="<seconds>",
					description = "Auto delete timer")
	async def deletetimer(self, luna, seconds:int):
		await luna.message.delete()
		await embed_builder(luna, description=f"```\nAuto delete timer » {seconds} seconds```")
		prints.message(f"Auto delete timer » {color.purple(f'{seconds} seconds')}")
		config.delete_timer(f"{seconds}")

	@commands.command(name = "afkmessage",
					usage="<text>",
					description = "Change the afk message")
	async def afkmessage(self, luna, *, afkmessage):
		await luna.message.delete()
		await embed_builder(luna, description=f"```\nAFK message » {afkmessage}```")
		prints.message(f"AFK message » {color.purple(f'{afkmessage}')}")
		config.afk_message(f"{afkmessage}")

	@commands.command(name = "riskmode",
					usage="<on/off>",
					description = "Enable abusive commands")
	async def riskmode(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Riskmode » {color.purple(f'{mode}')}")
			config.risk_mode(mode)
			await embed_builder(luna, description=f"```\nRiskmode » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "selfbotdetection",
					usage="<on/off>",
					description = "Sb detection")
	async def selfbotdetection(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Selfbot detection » {color.purple(f'{mode}')}")
			config.selfbot.sniper(mode)
			await embed_builder(luna, description=f"```\nSelfbot detection » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "mention",
					usage="<on/off>",
					description = "Mention notification")
	async def mention(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Mention notification » {color.purple(f'{mode}')}")
			config.toast.pings(mode)
			await embed_builder(luna, description=f"```\nMention notification » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "password",
					usage="<new_password>",
					description = "Change password")
	async def password(self, luna, password:str):
		await luna.message.delete()
		await embed_builder(luna, description=f"```\nChanged password to » {password}```")
		prints.message(f"Changed password to » {color.purple(f'{password}')}")
		config.password(f"{password}")

	@commands.command(name = "console",
					usage="<1/2>",
					description = "Change console mode")
	async def console(self, ctx, mode:str):
		await ctx.message.delete()
		if mode == "1" or mode == "2":
			config._global("Luna/console/console.json", "mode", mode)
			prints.message(f"Console mode » {color.purple(f'{mode}')}")
			await embed_builder(ctx, description=f"```\nConsole mode » {mode}```")
			luna.console(clear=True)
			if privacy:
				command_count = len(bot.commands)
				cog = bot.get_cog('Custom commands')
				try:
					custom = cog.get_commands()
					custom_command_count = 0
					for command in custom:
						custom_command_count += 1
				except:
					custom_command_count = 0
				prefix = files.json("Luna/config.json", "prefix", documents=True)
				print(motd.center(os.get_terminal_size().columns))
				if beta:
					print("Beta Build".center(os.get_terminal_size().columns))
				prefix = files.json("Luna/config.json", "prefix", documents=True)
				console_mode = files.json("Luna/console/console.json", "mode", documents=True)
				if console_mode == "2":
					riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
					themesvar = files.json("Luna/config.json", "theme", documents=True)
					deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
					startup_status = files.json("Luna/config.json", "startup_status", documents=True)
					nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
					giveawayjoiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
					if themesvar == "default":
						pass
					else:
						themesvar = themesvar[:-5]
					ui_user = f" {color.purple('User:')} {'Luna#0000':<26}"
					ui_guilds = f" {color.purple('Guilds:')} {'0':<24}"
					ui_friends = f" {color.purple('Friends:')} {'0':<23}"
					ui_prefix = f" {color.purple('Prefix:')} {prefix:<24}"
					ui_theme = f" {color.purple('Theme:')} {themesvar:<25}"
					ui_commands = f" {color.purple('Commands:')} {command_count-custom_command_count:<22}"
					ui_commands_custom = f" {color.purple('Custom Commands:')} {custom_command_count:<15}"
					ui_nitro_sniper = f" {color.purple('Nitro Sniper:')} {nitro_sniper}"
					ui_giveaway_sniper = f" {color.purple('Giveaway Joiner:')} {giveawayjoiner}"
					ui_riskmode = f" {color.purple('Riskmode:')} {riskmode}"
					ui_deletetimer = f" {color.purple('Delete Timer:')} {deletetimer}"
					ui_startup = f" {color.purple('Startup Status:')} {startup_status}"
					print()
					print(f"               ═════════════ {color.purple('User')} ═════════════      ═══════════ {color.purple('Settings')} ═══════════")
					print(f"               {ui_user}     {ui_prefix}")
					print(f"               {ui_guilds}     {ui_theme}")
					print(f"               {ui_friends}     {ui_nitro_sniper}")
					print(f"               ════════════════════════════════      {ui_giveaway_sniper}")
					print(f"               ═════════════ {color.purple('Luna')} ═════════════      {ui_riskmode}")
					print(f"               {ui_commands}     {ui_deletetimer}")
					print(f"               {ui_commands_custom}     {ui_startup}")
					print(f"               ════════════════════════════════      ════════════════════════════════\n")
				else:
					print()
					print(f"                           {color.purple('[')}+{color.purple('] CONNECTED')}")
					print(f"                           {color.purple('[')}+{color.purple(']')} Luna#0000 | {color.purple('0')} Guilds | {color.purple('0')} Friends")
					print(f"                           {color.purple('[')}+{color.purple(']')} {prefix}\n")
			else:
				command_count = len(bot.commands)
				cog = bot.get_cog('Custom commands')
				try:
					custom = cog.get_commands()
					custom_command_count = 0
					for command in custom:
						custom_command_count += 1
				except:
					custom_command_count = 0
				prefix = files.json("Luna/config.json", "prefix", documents=True)
				print(motd.center(os.get_terminal_size().columns))
				if beta:
					print("Beta Build".center(os.get_terminal_size().columns))
				prefix = files.json("Luna/config.json", "prefix", documents=True)
				console_mode = files.json("Luna/console/console.json", "mode", documents=True)
				if console_mode == "2":
					riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
					themesvar = files.json("Luna/config.json", "theme", documents=True)
					deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
					startup_status = files.json("Luna/config.json", "startup_status", documents=True)
					nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
					giveawayjoiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
					if themesvar == "default":
						pass
					else:
						themesvar = themesvar[:-5]
					bot_user = f"{bot.user}"
					ui_user = f" {color.purple('User:')} {bot_user:<26}"
					ui_guilds = f" {color.purple('Guilds:')} {len(bot.guilds):<24}"
					ui_friends = f" {color.purple('Friends:')} {len(bot.user.friends):<23}"
					ui_prefix = f" {color.purple('Prefix:')} {prefix:<24}"
					ui_theme = f" {color.purple('Theme:')} {themesvar:<25}"
					ui_commands = f" {color.purple('Commands:')} {command_count-custom_command_count:<22}"
					ui_commands_custom = f" {color.purple('Custom Commands:')} {custom_command_count:<15}"
					ui_nitro_sniper = f" {color.purple('Nitro Sniper:')} {nitro_sniper}"
					ui_giveaway_sniper = f" {color.purple('Giveaway Joiner:')} {giveawayjoiner}"
					ui_riskmode = f" {color.purple('Riskmode:')} {riskmode}"
					ui_deletetimer = f" {color.purple('Delete Timer:')} {deletetimer}"
					ui_startup = f" {color.purple('Startup Status:')} {startup_status}"
					print()
					print(f"               ═════════════ {color.purple('User')} ═════════════      ═══════════ {color.purple('Settings')} ═══════════")
					print(f"               {ui_user}     {ui_prefix}")
					print(f"               {ui_guilds}     {ui_theme}")
					print(f"               {ui_friends}     {ui_nitro_sniper}")
					print(f"               ════════════════════════════════      {ui_giveaway_sniper}")
					print(f"               ═════════════ {color.purple('Luna')} ═════════════      {ui_riskmode}")
					print(f"               {ui_commands}     {ui_deletetimer}")
					print(f"               {ui_commands_custom}     {ui_startup}")
					print(f"               ════════════════════════════════      ════════════════════════════════\n")
				else:
					print()
					print(f"                           {color.purple('[')}+{color.purple('] CONNECTED')}")
					print(f"                           {color.purple('[')}+{color.purple(']')} {bot.user} | {color.purple(f'{len(bot.guilds)}')} Guilds | {color.purple(f'{len(bot.user.friends)}')} Friends")
					print(f"                           {color.purple('[')}+{color.purple(']')} {prefix}\n")
			print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
			prints.message(f"{color.purple(f'{command_count-custom_command_count}')} commands | {color.purple(f'{custom_command_count}')} custom commands")
		else:
			await mode_error(ctx, "1 or 2")

	@commands.command(name = "reload",
					usage="",
					description = "Reload custom commands")
	async def reload(self, ctx):
		await ctx.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		# path = getattr(sys, '_MEIPASS', os.getcwd())
		# cogs_path = path + "\\cogs"
		# luna.loader_check()
		# for filename in os.listdir(cogs_path):
		# 	if filename.endswith(".py"):
		# 		bot.reload_extension(f"cogs.{filename[:-3]}")
		# prints.message(f"Reloaded custom commands")
		# await embed_builder(ctx, description=f"```\nReloaded custom commands```")
		await embed_builder(ctx, description=f"```\nReload has been disabled until further notice, use {prefix}restart instead```")

bot.add_cog(SettingsCog(bot))
class CustomCog(commands.Cog, name="Custom commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
	try:
		file = open(os.path.join(files.documents(), "Luna/custom/custom.py"), "r")
		file_data = file.read()
		if "sys.modules" in str(file_data):
			prints.error("Using sys.modules is not allowed.")
			time.sleep(5)
			os._exit(0)
		if "inspect" and "import" in str(file_data):
			prints.error("Importing inspect is not allowed.")
			time.sleep(5)
			os._exit(0)
		if "dill" and "import" in str(file_data):
			prints.error("Importing dill is not allowed.")
			time.sleep(5)
			os._exit(0)
		if "exec" in str(file_data):
			prints.error("Using exec is not allowed.")
			time.sleep(5)
			os._exit(0)
		if "auth_luna" in str(file_data):
			prints.error("\"auth_luna\" not allowed.")
			time.sleep(5)
			os._exit(0)
		if "atlas" in str(file_data):
			prints.error("\"atlas\" not allowed.")
			time.sleep(5)
			os._exit(0)
		exec(file_data)
	except Exception as e:
		prints.error(e)
		os.system('pause')

bot.add_cog(CustomCog(bot))
class ShareCog(commands.Cog, name="Share commands"):
    def __init__(self, bot:commands.bot):
        self.bot = bot
        
    @commands.command(name = "share",
                    usage="<on/off>",
                    description = "Share on/off")
    async def share(self, luna, mode:str):
        await luna.message.delete()
        if mode == "on" or mode == "off":
            prints.message(f"Share » {color.purple(f'{mode}')}")
            config.share(mode)
            await embed_builder(luna, description=f"```\nShare » {mode}```")
        else:
            await mode_error(luna, "on or off")

    @commands.command(name = "shareuser",
                    usage="<@member>",
                    description = "Set the member for sharing")
    async def shareuser(self, luna, user_id):
        await luna.message.delete()
        if "<@!" and ">" in user_id:
            user_id = user_id.replace("<@!", "").replace(">", "")
            user = await self.bot.fetch_user(user_id)
        else:
            user = await self.bot.fetch_user(user_id)
        if user == self.bot.user:
            await error_builder(luna, description=f"```\nYou can't use share on yourself```")
            return
        config.user_id(user.id)
        prints.message(f"Share user set to » {color.purple(f'{user}')}")
        await embed_builder(luna, description=f"```\nShare user set to » {user}```")

    @commands.command(name = "sharenone",
                    usage="",
                    description = "Share member to none")
    async def sharenone(self, luna):
        await luna.message.delete()
        config.user_id("")
        prints.message(f"Share user set to » None")
        await embed_builder(luna, description=f"```\nShare user set to » None```")

bot.add_cog(ShareCog(bot))

class EncodeCog(commands.Cog, name="Encode commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "encode_cea256", usage = "<key> <text>", description = "cea256")
	async def encode_cea256(self, luna, key, *, text):
		await luna.message.delete()
		if len(key) != 32:
			await luna.send("Invalid key, needs to be 256-bits / 32 Chars in length")
			return
		encoded = Encryption(key).CEA256(text)
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_base64",
					usage="<text>",
					description = "base64")
	async def encode_base64(self, luna, *, text:str):
		await luna.message.delete()
		enc = base64.b64encode('{}'.format(text).encode('ascii'))
		encoded = str(enc)
		encoded = encoded[2:len(encoded)-1]
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_leet",
					usage="<text>",
					description = "leet")
	async def encode_leet(self, luna, *, text:str):
		await luna.message.delete()
		encoded = text.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_md5",
					usage="<text>",
					description = "md5 (oneway)")
	async def encode_md5(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.md5(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_sha1",
					usage="<text>",
					description = "sha1 (oneway)")
	async def encode_sha1(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.sha1(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_sha224",
					usage="<text>",
					description = "sha224 (oneway)")
	async def encode_sha224(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.sha3_224(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_sha256",
					usage="<text>",
					description = "sha256 (oneway)")
	async def encode_sha256(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.sha3_256(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_sha384",
					usage="<text>",
					description = "sha384 (oneway)")
	async def encode_sha384(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.sha3_384(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

	@commands.command(name = "encode_sha512",
					usage="<text>",
					description = "sha512 (oneway)")
	async def encode_sha512(self, luna, *, text:str):
		await luna.message.delete()
		enc = hashlib.sha3_512(text.encode())
		encoded = enc.hexdigest()
		await luna.send(f"{encoded}")

bot.add_cog(EncodeCog(bot))

class DecodeCog(commands.Cog, name="Decode commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "decode_cea256", usage = "<key> <text>", description = "cea256")
	async def decode_cea256(self, luna, key, *, text):
		await luna.message.delete()
		if len(key) != 32:
			await luna.send("Invalid key, needs to be 256-bits / 32 Chars in length")
			return
		try:
			decrypted = Decryption(key).CEA256(text)
		except:
			await luna.send("Decryption failed, make sure the key is correct i")
		else:
			await luna.send(f"{decrypted}")

	@commands.command(name = "decode_base64",
					usage="<text>",
					description = "base64")
	async def decode_base64(self, luna, *, text:str):
		await luna.message.delete()
		dec = base64.b64decode('{}'.format(text).encode('ascii'))
		decoded = str(dec)
		decoded = decoded[2:len(decoded)-1]
		await luna.send(f"{decoded}")

	@commands.command(name = "decode_leet",
					usage="<text>",
					description = "leet")
	async def decode_leet(self, luna, *, text:str):
		await luna.message.delete()
		encoded = text.replace('3', 'e').replace('4', 'a').replace('!', 'i').replace('|_|', 'u').replace('|_|', 'U').replace('3', 'E').replace('!', 'I').replace('4', 'A').replace('0','o').replace('0','O').replace('7','t').replace('7','T').replace('1','l').replace('1','L').replace('|<','k').replace('|<','K').replace('X','CK').replace('x','ck').replace('X','Ck').replace('x','cK')
		await luna.send(f"{encoded}")

bot.add_cog(DecodeCog(bot))

class GiveawayCog(commands.Cog, name="Giveaway settings"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "giveawayjoiner",
					usage="<on/off>",
					description = "Giveaway sniper")
	async def giveawayjoiner(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Giveaway sniper » {color.purple(f'{mode}')}")
			config.giveaway.joiner(mode)
			await embed_builder(luna, description=f"```\nGiveaway sniper » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "delay",
					usage="<minutes>",
					description = "Delay in minutes")
	async def delay(self, luna, minute:int):
		await luna.message.delete()
		await embed_builder(luna, description=f"```\nGiveaway joiner delay » {minute} minute/s```")
		prints.message(f"Auto delete timer » {color.purple(minute)}")
		config.giveaway.delay_in_minutes(f"{minute}")

	@commands.command(name = "giveawayguild",
					usage="<on/off>",
					description = "Giveaway server joiner")
	async def giveawayguild(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Server joiner » {color.purple(f'{mode}')}")
			config.giveaway.guild_joiner(mode)
			await embed_builder(luna, description=f"```\nServer joiner » {mode}```")
		else:
			await mode_error(luna, "on or off")

bot.add_cog(GiveawayCog(bot))
class CryptoCog(commands.Cog, name="Cryptocurrency commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "crypto",
					usage="<crypto>",
					description = "Cryptocurrency prices")
	async def crypto(self, luna, crypto:str):
		await luna.message.delete()
		request = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms=USD,EUR,GBP,CHF,CAD,AUD,RUB,JPY,CNY,INR,TRY,PLN')
		data = request.json()
		usd = data['USD']
		eur = data['EUR']
		gbp = data['GBP']
		chf = data['CHF']
		cad = data['CAD']
		aud = data['AUD']
		rub = data['RUB']
		jpy = data['JPY']
		cny = data['CNY']
		inr = data['INR']
		pln = data['PLN']
		__try = data['TRY']
		desc = f"""```
USD: {usd}
EUR: {eur}
GBP: {gbp}
CHF: {chf}
CAD: {cad}
AUD: {aud}
RUB: {rub}
JPY: {jpy}
CNY: {cny}
INR: {inr}
TRY: {__try}
PLN: {pln}```"""
		await embed_builder(luna, title=crypto, description=desc)
        
bot.add_cog(CryptoCog(bot))

class CustomizeCog(commands.Cog, name="Customization commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "ctitle",
					usage="<title>",
					description = "Customize the title")
	async def ctitle(self, luna, *, newtitle:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the title if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			prints.message(f"Changed title to » {color.purple(f'{newtitle}')}")
			if newtitle == "None":
				config.title("")
			else:
				config.title(f"{newtitle}")
			await embed_builder(luna, description=f"```\nChanged title to » {newtitle}```")

	@commands.command(name = "ctitleurl",
					usage="<url>",
					description = "Customize the title url")
	async def ctitleurl(self, luna, newtitleurl:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the title url if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			if newtitleurl == "None":
				config.title_url("")
			if not newtitleurl.startswith("https://"):
				await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
				return
			else:
				config.title_url(f"{newtitleurl}")
			prints.message(f"Changed title url to » {color.purple(f'{newtitleurl}')}")
			await embed_builder(luna, description=f"```\nChanged title url to » {newtitleurl}```")

	@commands.command(name = "cfooter",
					usage="<footer>",
					description = "Customize the footer")
	async def cfooter(self, luna, *, newfooter:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the footer if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			prints.message(f"Changed footer to » {color.purple(f'{newfooter}')}")
			if newfooter == "None":
				config.footer("")
			else:
				config.footer(f"{newfooter}")
			await embed_builder(luna, description=f"```\nChanged footer to » {newfooter}```")

	@commands.command(name = "cfootericon",
					usage="<url>",
					description = "Customize the footer icon")
	async def cfootericon(self, luna, newfootericonurl:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the footer icon if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			if newfootericonurl == "None":
				config.footer_icon_url("")
			elif newfootericonurl == "avatar":
				config.footer_icon_url("$avatar")
			elif not newfootericonurl.startswith("https://"):
				await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
				return
			else:
				config.footer_icon_url(f"{newfootericonurl}")
			prints.message(f"Changed footer icon url to » {color.purple(f'{newfootericonurl}')}")
			await embed_builder(luna, description=f"```\nChanged footer icon url to » {newfootericonurl}```")

	@commands.command(name = "cimage",
					usage="<url>",
					description = "Customize the thumbnail image")
	async def cimage(self, luna, newimageurl:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the thumbnail image if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			if newimageurl == "None":
				config.image_url("")
			elif newimageurl == "avatar":
				config.image_url("$avatar")
			elif not newimageurl.startswith("https://"):
				await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
				return
			else:
				config.image_url(f"{newimageurl}")
			prints.message(f"Changed thumbnail url to » {color.purple(f'{newimageurl}')}")
			await embed_builder(luna, description=f"```\nChanged thumbnail url to » {newimageurl}```")

	@commands.command(name = "clargeimage",
					usage="<url>",
					description = "Customize the large image")
	async def clargeimage(self, luna, newimageurl:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the large image if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			if newimageurl == "None":
				config.large_image_url("")
			elif newimageurl == "avatar":
				config.large_image_url("$avatar")
			elif not newimageurl.startswith("https://"):
				await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
				return
			else:
				config.large_image_url(f"{newimageurl}")
			prints.message(f"Changed image url to » {color.purple(f'{newimageurl}')}")
			await embed_builder(luna, description=f"```\nChanged image url to » {newimageurl}```")

	@commands.command(name = "chexcolor",
					usage="<#hex>",
					description = "Theme hexadecimal color")
	async def chexcolor(self, luna, newhexcolor:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the color if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			if len(newhexcolor) < 6:
				await error_builder(luna, description=f"```\nNot a valid HEX color code```")
				return
			prints.message(f"Changed hexcolor to » {color.purple(f'{newhexcolor}')}")
			if newhexcolor == "None":
				config.hex_color("")
			else:
				config.hex_color(f"{newhexcolor}")
			await embed_builder(luna, description=f"```\nChanged hexcolor to » {newhexcolor}```")

	@commands.command(name = "cauthor",
					usage="<text>",
					description = "Customize the author text")
	async def cauthor(self, luna, *, newauthor:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the author text if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			prints.message(f"Changed author to » {color.purple(f'newauthor')}'")
			if newauthor == "None":
				config.author("")
			else:
				config.author(f"{newauthor}")
			await embed_builder(luna, description=f"```\nChanged author to » {newauthor}```")

	@commands.command(name = "cauthoricon",
					usage="<url>",
					description = "Customize the author icon")
	async def cauthoricon(self, luna, newauthoriconurl:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the author icon if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			if newauthoriconurl == "None":
				config.author_icon_url("")
			elif newauthoriconurl == "avatar":
				config.author_icon_url("$avatar")
			elif not newauthoriconurl.startswith("https://"):
				await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
				return
			else:
				config.author_icon_url(f"{newauthoriconurl}")
			prints.message(f"Changed author icon url to » {color.purple(f'newauthoriconurl')}'")
			await embed_builder(luna, description=f"```\nChanged author icon url to » {newauthoriconurl}```")

	@commands.command(name = "cauthorurl",
					usage="<url>",
					description = "Customize the author url")
	async def cauthorurl(self, luna, newauthorurl:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the author url if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			if newauthorurl == "None":
				config.author_url("")
			elif not newauthorurl.startswith("https://"):
				await error_builder(luna, description=f"```\nNot a valid URL. Needs to start with \"https://\"```")
				return
			else:
				config.author_ur(f"{newauthorurl}")
			prints.message(f"Changed author url to » {color.purple(f'newauthorurl')}'")
			await embed_builder(luna, description=f"```\nChanged author url to » {newauthorurl}```")

	@commands.command(name = "description",
					aliases=['cdescription'],
					usage="<on/off>",
					description = "Hide/Show <> | []")
	async def description(self, luna, mode:str):
		await luna.message.delete()
		if files.json("Luna/config.json", "theme", documents=True) == "default":
			await error_builder(luna, f"```\nYou can't change the description mode if you're using the default theme\n``````\nPlease change the theme first with {get_prefix()}theme\n\n({get_prefix()}themes to show all available themes)```")
		else:
			if mode == "on":
				prints.message(f"Changed description to » {color.purple('on')}")
				config.description(True)
				await embed_builder(luna, description=f"```\nChanged description to » on```")
			elif mode == "off":
				prints.message(f"Changed description to » {color.purple('off')}")
				config.description(False)
				await embed_builder(luna, description=f"```\nChanged description to » off```")
			else:
				await mode_error(luna, "on or off")

	@commands.command(name = "color",
					usage="<hexcode>",
					description = "Color information")
	async def color(self, luna, hexcode:str):
		await luna.message.delete()
		if hexcode == "random":
			hexcode = "%06x" % random.randint(0, 0xFFFFFF)
		if hexcode[:1] == "#":
			hexcode = hexcode[1:]
		if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', hexcode):
			return
		r = requests.get(f"https://react.flawcra.cc/api/generation.php?type=color&color={hexcode}").json()
		await embed_builder(luna, title=str(r["name"]), description=f"```\nHEX               » {r['hex']}\n``````\nRGB               » {r['rgb']}\n``````\nINT               » {r['int']}\n``````\nBrightness        » {r['brightness']}\n```",color=r["int"], thumbnail=r["image"])

bot.add_cog(CustomizeCog(bot))
class HentaiCog(commands.Cog, name="Hentai commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "hclassic",
					usage="",
					description = "Random classic hentai")
	async def hclassic(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/classic").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hrandom",
					usage="",
					description = "Random hentai gif")
	async def hrandom(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hass",
					usage="",
					description = "Random hentai ass")
	async def hass(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekobot.xyz/api/image?type=hass").json()
		await embed_builder(luna, large_image=str(r['message']), thumbnail="None")

	@commands.command(name = "hboobs",
					usage="",
					description = "Random hentai boobs")
	async def hboobs(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/boobs").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hsmallboobs",
					usage="",
					description = "Random hentai smallboobs")
	async def hsmallboobs(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/boobs").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "htits",
					usage="",
					description = "Random hentai tits")
	async def htits(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/tits").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hpussy",
					usage="",
					description = "Random hentai pussy")
	async def hpussy(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/pussy").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")
        
	@commands.command(name = "hanal",
					usage="",
					description = "Random hentai anal")
	async def hanal(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/anal").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hcum",
					usage="",
					description = "Random hentai cum gif")
	async def hcum(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/cum").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hcum1",
					usage="",
					description = "Random hentai cum")
	async def hcum1(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/cum_jpg").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hblowjob",
					usage="",
					description = "Random hentai blowjob gif")
	async def hblowjob(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/bj").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hblowjob1",
					usage="",
					description = "Random hentai blowjob")
	async def hblowjob1(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/blowjob").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hneko",
					usage="",
					description = "Random hentai neko")
	async def hneko(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "htrap",
					usage="",
					description = "Random hentai trap")
	async def htrap(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/trap").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hyuri",
					usage="",
					description = "Random hentai yuri")
	async def hyuri(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/yuri").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hfutanari",
					usage="",
					description = "Random hentai futanari")
	async def hfutanari(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/futanari").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hketa",
					usage="",
					description = "Random hentai keta")
	async def hketa(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/keta").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hhololewd",
					usage="",
					description = "Random hololewd hentai ")
	async def hhololewd(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/hololewd").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hlewdkemo",
					usage="",
					description = "Random lewdkemo hentai")
	async def hlewdkemo(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/lewdkemo").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hsolo",
					usage="",
					description = "Random solo hentai")
	async def hsolo(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/solo").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hsolog",
					usage="",
					description = "Random solo hentai")
	async def hsolog(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/solog").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hfeetg",
					usage="",
					description = "Random hentai feet")
	async def hfeetg(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/feetg").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hero",
					usage="",
					description = "Random erotic hentai")
	async def hero(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/ero").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "herok",
					usage="",
					description = "Random erotic kitsune")
	async def herok(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/erok").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")
		
	@commands.command(name = "herokemo",
					usage="",
					description = "Random hentai erokemo")
	async def herokemo(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/erokemo").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hles",
					usage="",
					description = "Random lesbian hentai")
	async def hles(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/les").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hwallpaper",
					usage="",
					description = "Random hentai wallpaper")
	async def hwallpaper(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/wallpaper").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hlewdk",
					usage="",
					description = "Random lewd hentai")
	async def hlewdk(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/lewdk").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hngif",
					usage="",
					description = "Random hentai neko gif")
	async def hngif(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/ngif").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hkemonomimi",
					usage="",
					description = "Random neko")
	async def hkemonomimi(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/kemonomimi").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hholoero",
					usage="",
					description = "Random erotic hentai")
	async def hholoero(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/holoero").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hfoxgirl",
					usage="",
					description = "Random hentai fox girl")
	async def hfoxgirl(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/fox_girl").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hfemdom",
					usage="",
					description = "Random hentai female")
	async def hfemdom(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/femdom").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hgasm",
					usage="",
					description = "Random hentai gasm")
	async def hgasm(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/gasm").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hkuni",
					usage="",
					description = "Random hentai kuni")
	async def hkuni(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/kuni").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "hpwankg",
					usage="",
					description = "Random hentai wank")
	async def hpwankg(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/pwankg").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "havatar",
					usage="",
					description = "Random hentai avatar")
	async def havatar(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/nsfw_avatar").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

	@commands.command(name = "havatar1",
					usage="",
					description = "Random hentai avatar")
	async def havatar1(self, luna):
		await luna.message.delete()
		r = requests.get("https://nekos.life/api/v2/img/avatar").json()
		await embed_builder(luna, large_image=str(r['url']), thumbnail="None")

bot.add_cog(HentaiCog(bot))
class OnMember(commands.Cog, name="on member events"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_member_join(self, member):
		if antiraid is True:
			guilds = files.json("Luna/protections/config.json", "guilds", documents=True)
			if member.guild.id in guilds:
				try:
					guild = member.guild
					async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
						if member.guild.id in whitelisted_users.keys() and i.user.id in whitelisted_users[
								member.guild.id].keys():
							return
						else:
							prints.message(f"{member.name}#{member.discriminator} banned by Anti-Raid")
							await guild.ban(member, reason="Luna Anti-Raid")
				except Exception as e:
					print(e)

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		if antiraid is True:
			guilds = files.json("Luna/protections/config.json", "guilds", documents=True)
			if member.guild.id in guilds:
				try:
					guild = member.guild
					async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
						if guild.id in whitelisted_users.keys() and i.user.id in whitelisted_users[
								guild.id].keys() and i.user.id is not self.bot.user.id:
							prints.message(f"{i.user.name}#{i.user.discriminator} not banned")
						else:
							prints.message(f"{i.user.name}#{i.user.discriminator} banned by Anti-Raid")
							await guild.ban(i.user, reason="Luna Anti-Raid")
				except Exception as e:
					print(e)

bot.add_cog(OnMember(bot))

class SniperCog(commands.Cog, name="Sniper settings"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "nitrosniper",
					usage="<on/off>",
					description = "Nitro sniper")
	async def nitrosniper(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Nitro sniper » {color.purple(f'{mode}')}")
			config.nitro.sniper(mode)
			await embed_builder(luna, description=f"```\nNitro sniper » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "privsniper",
					usage="<on/off>",
					description = "Privnote sniper")
	async def privsniper(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Privnote sniper » {color.purple(f'{mode}')}")
			config.privnote.sniper(mode)
			await embed_builder(luna, description=f"```\nPrivnote sniper » {mode}```")
		else:
			await mode_error(luna, "on or off")

	# @commands.command(name = "snipercharge",
	# 				usage="<on/off>",
	# 				description = "Sniper visual charge")
	# async def snipercharge(self, luna, mode:str):
	# 	await luna.message.delete()
	# 	global chargesniper
	# 	if mode == "on" or mode == "off":
	# 		prints.message(f"Nitro sniper charge » {color.purple(f'{mode}')}")
	# 		config_toast_toasts(mode)
	# 		if mode == "on":
	# 			chargesniper = True
	# 		elif mode == "off":
	# 			chargesniper = False
	# 		await embed_builder(luna, description=f"```\nNitro sniper charge » {mode}```")
	# 	else:
	# 		await mode_error(luna, "on or off")

bot.add_cog(SniperCog(bot))

class ThemeCog(commands.Cog, name="Theme command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "theme",
					usage="<theme>",
					description = "Change theme")
	async def theme(self, luna, theme:str):
		await luna.message.delete()
		theme = theme.replace('.json','')
		if theme == "default":
			config.theme(theme)
			await embed_builder(luna, description=f"```\nChanged theme to » {theme}```")
		else:
			if files.file_exist(f"Luna/themes/{theme}.json", documents=True):
				config.theme(theme)
				await embed_builder(luna, description=f"```\nChanged theme to » {theme}```")
			else:
				await error_builder(luna, description=f"```\nThere is no theme called » {theme}```")

bot.add_cog(ThemeCog(bot))

class ThemesCog(commands.Cog, name="Theme commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "newtheme",
					usage="<name>",
					description = "Create a theme")
	async def newtheme(self, luna, themename:str):
		await luna.message.delete()
		themename = themename.replace('.json','')
		if files.file_exist(f"Luna/themes/{themename}.json", documents=True):
			await error_builder(luna, description=f"```\nA theme already exists with the name » {themename}```")
		else:
			prints.message(f"Created theme » {color.purple(f'{themename}')}")
			data = {
				"title": "Luna",
				"title_url": "",
				"footer": "Team-luna.org",
				"footer_icon_url": "https://cdn.discordapp.com/attachments/927033067468623882/927033385216520232/Luna_Logo.png",
				"image_url": "https://cdn.discordapp.com/attachments/927033067468623882/927033385216520232/Luna_Logo.png",
				"large_image_url": "",
				"hex_color": "#898eff",
				"author": "",
				"author_icon_url": "",
				"author_url": "",
				"description": True
			}
			files.write_json(f"Luna/themes/{themename}.json", data, documents=True)
			config.theme(f"{themename}")
			await embed_builder(luna, description=f"```\nCreated theme » {themename}```")

	@commands.command(name = "edittheme",
					usage="<name>",
					description = "Edit current theme name")
	async def edittheme(self, luna, themename:str):
		await luna.message.delete()
		themesvar = files.json("Luna/config.json", "theme", documents=True)
		if files.file_exist(f"Luna/themes/{themename}.json", documents=True):
			await error_builder(luna, description=f"```\nA theme already exists with the name » {themename}```")
		else:
			prints.message(f"Edited theme name to » {color.purple(f'{themename}')}")
			os.rename(os.path.join(files.documents(), f"Luna/themes/{themesvar}"),os.path.join(files.documents(), f"Luna/themes/{themename}.json"))
			config.theme(f"{themename}")
			await embed_builder(luna, description=f"```\nEdited theme name to » {themename}```")
		
	@commands.command(name = "deltheme",
					usage="<name>",
					description = "Delete a theme")
	async def deltheme(self, luna, themename:str):
		await luna.message.delete()
		themename = themename.replace('.json','')
		themesvar = files.json("Luna/config.json", "theme", documents=True)
		if themesvar == f"{themename}.json":
			await error_builder(luna, description="```\nYou cant delete the theme you are currently using```")
			return
		if files.file_exist(f"Luna/themes/{themename}.json", documents=True):
			files.remove(f"Luna/themes/{themename}.json", documents=True)
			prints.message(f"Deleted theme » {color.purple(f'{themename}')}")
			await embed_builder(luna, description=f"```\nDeleted theme » {themename}```")
		else:
			await error_builder(luna, description=f"```\nThere is no theme called » {themename}```")

	@commands.command(name = "sendtheme",
					usage="",
					description = "Send the current theme file")
	async def sendtheme(self, luna):
		await luna.message.delete()
		themesvar = files.json("Luna/config.json", "theme", documents=True)
		await luna.send(file=discord.File(os.path.join(files.documents(), f"Luna/themes/{themesvar}")))

	@commands.command(name="stealtheme", 
					usage="<id>",
					aliases=["themesteal"],
					description="Steal a theme")
	async def stealtheme(self, luna, message_id:int):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		message = await luna.fetch_message(message_id)
		embed = message.embeds[0]
		path = os.path.expanduser('~\Documents\Luna')
		file = open(path + "\\themes\\" + embed.title.lower().replace(" ", "").replace("_", "").replace("*", "").replace("`", "") + ".json", "w+", encoding="utf-8")
		data = """{
	"title": "%s",
	"title_url": "%s",
	"footer": "%s",
	"footer_icon_url": "%s",
	"image_url": "%s",
	"large_image_url": "%s",
	"hex_color": "%s",
	"author": "%s",
	"author_icon_url": "%s",
	"author_url": "%s",
	"description": true	
}"""%(embed.title, embed.url, embed.footer.text, embed.footer.icon_url, embed.thumbnail.url, embed.image.url, embed.color, embed.author.name, embed.author.icon_url, embed.author.url)
		file.write(data.replace("Embed.Empty", ""))
		file.close()
		await embed_builder(luna, description=f"""```\nSaved the embed theme as » {embed.title.lower().replace(" ", "").replace("_", "").replace("*", "").replace("`", "")}\n``````\nNote\n\nUse \"{prefix}theme {embed.title.lower().replace(" ", "").replace("_", "").replace("*", "").replace("`", "")}\" to use the theme.```""")

	@commands.command(name = "communitythemes",
					aliases=['cthemes'],
					usage="",
					description = "Community made themes")
	async def communitythemes(self, luna):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		await embed_builder(luna, title="Community Themes", description=f"{theme.description()}```\n{prefix}preview <theme>  » Preview a theme\n``````\n{prefix}install luna     » Luna theme\n{prefix}install lunaanimated » Luna theme\n{prefix}install chill    » Chill theme\n{prefix}install midnight » Midnight theme\n{prefix}install vaporwave » Vaporwave theme\n{prefix}install sweetrevenge » Sweetrevenge theme\n{prefix}install error    » Error theme\n{prefix}install lunapearl » Pearl theme\n{prefix}install gamesense » Gamesense theme\n{prefix}install aimware  » Aimware theme\n{prefix}install guilded  » Guilded theme\n{prefix}install lucifer  » Lucifer selfbot theme\n{prefix}install nighty   » Nighty selfbot theme\n{prefix}install aries    » Aries selfbot theme```")

bot.add_cog(ThemesCog(bot))

class CommunitythemesCog(commands.Cog, name="Community themes"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "preview",
					usage="<theme>",
					description = "Preview a theme")
	async def preview(self, luna, theme:str):
		await luna.message.delete()
		prefix = files.json("Luna/config.json", "prefix", documents=True)
		notfound = False
		theme = theme.lower()
		if theme == "luna":
			title= "Luna"
			titleurl= ""
			footer= "Team-luna.org"
			footer_iconurl= "https://cdn.discordapp.com/attachments/927033067468623882/927033182157668352/Luna_Logo1.png"
			imageurl= "https://cdn.discordapp.com/attachments/927033067468623882/927033182157668352/Luna_Logo1.png"
			large_imageurl= ""
			hexcolor= 0x898eff
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "lunaanimated":
			title= "Luna"
			titleurl= ""
			footer= "Team-luna.org"
			footer_iconurl= "https://cdn.discordapp.com/attachments/878593887113986048/878593949332291584/Luna2.png"
			imageurl= "https://cdn.discordapp.com/attachments/878593887113986048/878593954352885770/Icon.gif"
			large_imageurl= ""
			hexcolor= 0x898eff
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "chill":
			title= "F R E E D O M"
			titleurl= ""
			footer= "No one knows what it is so it exists as an illusion"
			footer_iconurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			imageurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			large_imageurl= ""
			hexcolor= 0xFF7C78
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		elif theme == "midnight":
			title= "Midnight."
			titleurl= ""
			footer= "It's Midnight."
			footer_iconurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			imageurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			large_imageurl= ""
			hexcolor= 0x4205B8
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "vaporwave":
			title= "Vapor Wave"
			titleurl= ""
			footer= "Ride the vapor wave."
			footer_iconurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			imageurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			large_imageurl= ""
			hexcolor= 0x400476
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "sweetrevenge":
			title= "Sweet Revenge."
			titleurl= ""
			footer= "Sweet revenge is nice."
			footer_iconurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			imageurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			large_imageurl= ""
			hexcolor= 0xff38d4
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "error":
			title= "Error™"
			titleurl= ""
			footer= "Error displaying footer, please contact support"
			footer_iconurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			imageurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			large_imageurl= ""
			hexcolor= 0x2e2e2e
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		elif theme == "lunapearl":
			title= "Luna"
			titleurl= ""
			footer= "Team Luna"
			footer_iconurl= "https://cdn.discordapp.com/attachments/878593887113986048/883100815504584805/LunaPearl.png"
			imageurl= "https://cdn.discordapp.com/attachments/878593887113986048/883099770237911180/LunaThumb.png"
			large_imageurl= ""
			hexcolor= 0xc1caff
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "gamesense":
			title= "gamesense"
			titleurl= "https://gamesense.pub/"
			footer= "Get Good Get Gamesense"
			footer_iconurl= "https://mir-s3-cdn-cf.behance.net/projects/404/fd4d3c107155739.Y3JvcCwxMDI0LDgwMCwwLDExMQ.png"
			imageurl= "https://mir-s3-cdn-cf.behance.net/projects/404/fd4d3c107155739.Y3JvcCwxMDI0LDgwMCwwLDExMQ.png"
			large_imageurl= ""
			hexcolor= 0x00FF00
			author= "esoterik"
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Dragon"
		elif theme == "aimware":
			title= "Aimware"
			titleurl= ""
			footer= "Aimware | One Step Ahead Of The Game"
			footer_iconurl= "https://cdn.discordapp.com/attachments/874446213297094688/876941477031346206/2955062011450968691.png"
			imageurl= "https://cdn.discordapp.com/attachments/874446213297094688/876941477031346206/2955062011450968691.png"
			large_imageurl= ""
			hexcolor= 0xbd100d
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Dragon"
		elif theme == "guilded":
			title= "Guilded"
			titleurl= "https://guilded.gg/"
			footer= "Guilded (Discord v2)| 2021"
			footer_iconurl= "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdiscord.deutschewarframe.community%2Fwp-content%2Fuploads%2FGuilded_Logomark_Color.png&f=1&nofb=1"
			imageurl= "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdiscord.deutschewarframe.community%2Fwp-content%2Fuploads%2FGuilded_Logomark_Color.png&f=1&nofb=1"
			large_imageurl= ""
			hexcolor= 0xFFDC2B
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "lucifer":
			title= "💙 Lucifer Selfbot 💙"
			titleurl= ""
			footer= "Lucifer Selfbot"
			footer_iconurl= ""
			imageurl= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.vuoLoEf3fOiE9wAmHAZxpgAAAA%26pid%3DApi&f=1"
			large_imageurl= ""
			hexcolor= 0x2B64FF
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "nighty":
			title= "Nighty"
			titleurl= ""
			footer= "nighty.one"
			footer_iconurl= ""
			imageurl= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstyles.redditmedia.com%2Ft5_3g26sd%2Fstyles%2FcommunityIcon_ndqvdagq4k061.png%3Fwidth%3D256%26s%3D6a058506a7fc75c83f06f3ed327d23f4b7b2a50c&f=1&nofb=1"
			large_imageurl= ""
			hexcolor= 0x619BFF
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "aries":
			title= "Aries"
			titleurl= ""
			footer= "made with \u2661 by bomt and destiny"
			footer_iconurl= ""
			imageurl= "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png"
			large_imageurl= ""
			hexcolor= 0x493BB9
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		else:
			notfound = True
		if notfound == True:
			await error_builder(luna, description=f"```\nNo theme called {theme} found```")
			return
		if description == True:
			description = "```<> is required | [] is optional\n\n```"
		elif description == False:
			description = ""
		command_count = len(bot.commands)
		cog = bot.get_cog('Custom commands')
		custom = cog.get_commands()
		custom_command_count = 0
		for command in custom:
			custom_command_count += 1
		embed = discord.Embed(title=title, url=titleurl, description=f"{description}```\nLuna\n\nCommands          » {command_count-custom_command_count}\nCustom Commands   » {custom_command_count}\n``````\nCategories\n\n{prefix}help [command]   » Display all commands\n{prefix}admin            » Administrative commands\n{prefix}abusive          » Abusive commands\n{prefix}animated         » Animated commands\n{prefix}dump             » Dumping\n{prefix}fun              » Funny commands\n{prefix}game             » Game commands\n{prefix}image            » Image commands\n{prefix}hentai           » Hentai explorer\n{prefix}profile          » Current guild profile\n{prefix}protection       » Protections\n{prefix}raiding          » Raiding tools\n{prefix}text             » Text commands\n{prefix}trolling         » Troll commands\n{prefix}tools            » Tools\n{prefix}networking       » Networking\n{prefix}nuking           » Account nuking\n{prefix}utility          » Utilities\n{prefix}settings         » Settings\n{prefix}webhook          » Webhook settings\n{prefix}notifications    » Toast notifications\n{prefix}sharing          » Share with somebody\n{prefix}themes           » Themes\n{prefix}communitythemes  » Community made themes\n{prefix}communitycmds    » Community made commands\n{prefix}customhelp       » Show custom commands\n{prefix}misc             » Miscellaneous\n{prefix}about            » Luna information\n{prefix}search <command> » Search for a command\n``````\nVersion\n\n{version}\n``````\nThis is a preview of the theme {theme}\nThis theme was made by {madeby}\n```", color=hexcolor)
		embed.set_thumbnail(url=imageurl)
		embed.set_footer(text=footer, icon_url=footer_iconurl)
		embed.set_author(name=author, url=authorurl, icon_url=author_iconurl)
		embed.set_image(url=large_imageurl)
		await send(luna, embed)

	@commands.command(name = "install",
					usage="<theme>",
					description = "Install a theme")
	async def install(self, luna, theme:str):
		await luna.message.delete()
		notfound = False
		theme = theme.lower()
		if theme == "luna":
			title= "Luna"
			titleurl= ""
			footer= "Team-luna.org"
			footer_iconurl= "https://cdn.discordapp.com/attachments/927033067468623882/927033182157668352/Luna_Logo1.png"
			imageurl= "https://cdn.discordapp.com/attachments/927033067468623882/927033182157668352/Luna_Logo1.png"
			large_imageurl= ""
			hexcolor= "#898eff"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "lunaanimated":
			title= "Luna"
			titleurl= ""
			footer= "Team-luna.org"
			footer_iconurl= "https://cdn.discordapp.com/attachments/878593887113986048/878593949332291584/Luna2.png"
			imageurl= "https://cdn.discordapp.com/attachments/878593887113986048/878593954352885770/Icon.gif"
			large_imageurl= ""
			hexcolor= "#898eff"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "chill":
			title= "F R E E D O M"
			titleurl= ""
			footer= "No one knows what it is so it exists as an illusion"
			footer_iconurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			imageurl= "https://cdn.discordapp.com/attachments/754791048164802721/875871217272381510/unknown.png"
			large_imageurl= ""
			hexcolor= "#FF7C78"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		elif theme == "midnight":
			title= "Midnight."
			titleurl= ""
			footer= "It's Midnight."
			footer_iconurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			imageurl= "https://media.discordapp.net/attachments/796453981655269481/796579251536265237/giphy.gif?width=596&height=596"
			large_imageurl= ""
			hexcolor= "#4205B8"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "vaporwave":
			title= "Vapor Wave"
			titleurl= ""
			footer= "Ride the vapor wave."
			footer_iconurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			imageurl= "https://cdn.discordapp.com/attachments/796453981655269481/796600554566582322/giphy.gif"
			large_imageurl= ""
			hexcolor= "#400476"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "sweetrevenge":
			title= "Sweet Revenge."
			titleurl= ""
			footer= "Sweet revenge is nice."
			footer_iconurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			imageurl= "https://media.giphy.com/media/wtjkff1kM84Ni/giphy.gif"
			large_imageurl= ""
			hexcolor= "#ff38d4"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Rainy"
		elif theme == "error":
			title= "Error™"
			titleurl= ""
			footer= "Error displaying footer, please contact support"
			footer_iconurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			imageurl= "https://media.tenor.com/images/c340fb1e8470226f1dfe4f0eedb93978/tenor.gif"
			large_imageurl= ""
			hexcolor= "#2e2e2e"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="$Exodus"
		elif theme == "lunapearl":
			title= "Luna"
			titleurl= ""
			footer= "Team Luna"
			footer_iconurl= "https://cdn.discordapp.com/attachments/878593887113986048/883100815504584805/LunaPearl.png"
			imageurl= "https://cdn.discordapp.com/attachments/878593887113986048/883099770237911180/LunaThumb.png"
			large_imageurl= ""
			hexcolor= "#c1caff"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		elif theme == "gamesense":
			title= "gamesense"
			titleurl= "https://gamesense.pub/"
			footer= "Get Good Get Gamesense"
			footer_iconurl= "https://mir-s3-cdn-cf.behance.net/projects/404/fd4d3c107155739.Y3JvcCwxMDI0LDgwMCwwLDExMQ.png"
			imageurl= "https://mir-s3-cdn-cf.behance.net/projects/404/fd4d3c107155739.Y3JvcCwxMDI0LDgwMCwwLDExMQ.png"
			large_imageurl= ""
			hexcolor= "#00FF00"
			author= "esoterik"
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Dragon"
		elif theme == "aimware":
			title= "Aimware"
			titleurl= ""
			footer= "Aimware | One Step Ahead Of The Game"
			footer_iconurl= "https://cdn.discordapp.com/attachments/874446213297094688/876941477031346206/2955062011450968691.png"
			imageurl= "https://cdn.discordapp.com/attachments/874446213297094688/876941477031346206/2955062011450968691.png"
			large_imageurl= ""
			hexcolor= "#bd100d"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Dragon"
		elif theme == "guilded":
			title= "Guilded"
			titleurl= "https://guilded.gg/"
			footer= "Guilded (Discord v2)| 2021"
			footer_iconurl= "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdiscord.deutschewarframe.community%2Fwp-content%2Fuploads%2FGuilded_Logomark_Color.png&f=1&nofb=1"
			imageurl= "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fdiscord.deutschewarframe.community%2Fwp-content%2Fuploads%2FGuilded_Logomark_Color.png&f=1&nofb=1"
			large_imageurl= ""
			hexcolor= "#FFDC2B"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "lucifer":
			title= "💙 Lucifer Selfbot 💙"
			titleurl= ""
			footer= "Lucifer Selfbot"
			footer_iconurl= ""
			imageurl= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.vuoLoEf3fOiE9wAmHAZxpgAAAA%26pid%3DApi&f=1"
			large_imageurl= ""
			hexcolor= "#2B64FF"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "nighty":
			title= "Nighty"
			titleurl= ""
			footer= "nighty.one"
			footer_iconurl= ""
			imageurl= "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstyles.redditmedia.com%2Ft5_3g26sd%2Fstyles%2FcommunityIcon_ndqvdagq4k061.png%3Fwidth%3D256%26s%3D6a058506a7fc75c83f06f3ed327d23f4b7b2a50c&f=1&nofb=1"
			large_imageurl= ""
			hexcolor= "#619BFF"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Exodus"
		elif theme == "aries":
			title= "Aries"
			titleurl= ""
			footer= "made with \u2661 by bomt and destiny"
			footer_iconurl= ""
			imageurl= "https://cdn.discordapp.com/attachments/775820489758605394/893750057243918346/Astolfo1.png"
			large_imageurl= ""
			hexcolor= "#493BB9"
			author= ""
			author_iconurl= ""
			authorurl= ""
			description= True
			madeby="Nshout"
		else:
			notfound = True
		if notfound == True:
			await error_builder(luna, description=f"```\nNo theme called {theme} found```")
			return
		data = {
			"title": f"{title}",
			"title_url": f"{titleurl}",
			"footer": f"{footer}",
			"footer_icon_url": f"{footer_iconurl}",
			"image_url": f"{imageurl}",
			"large_image_url": f"{large_imageurl}",
			"hex_color": f"{hexcolor}",
			"author": f"{author}",
			"author_icon_url": f"{author_iconurl}",
			"author_url": f"{authorurl}",
			"description": description
		}
		files.write_json(f"Luna/themes/{theme}.json", data, documents=True)
		config.theme(f"{theme}")
		await embed_builder(luna, description=f"```\nInstalled theme \"{theme}\" and applied it\nThis theme was made by {madeby}```")

bot.add_cog(CommunitythemesCog(bot))

class ToastCog(commands.Cog, name="Toast customization"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "toasticon",
					usage="<icon.ico>",
					description = "Customize the toast icon (has to be an .ico)")
	async def toasticon(self, luna, *, newicon:str):
		await luna.message.delete()
		if newicon.endswith(".ico"):
			prints.message(f"Changed toast icon to » {color.purple(f'{newicon}')}")
			config.toast.icon(f"{newicon}")
			await embed_builder(luna, description=f"```\nChanged toast icon to » {newicon}```")
		else:
			await error_builder(luna, description=f"```\nNot a valid icon file (.ico)```")
        
	@commands.command(name = "toasttitle",
					usage="<title>",
					description = "Customize the toast title")
	async def toasttitle(self, luna, *, newtitle:str):
		await luna.message.delete()
		prints.message(f"Changed toast title to » {color.purple(f'{newtitle}')}")
		if newtitle == "None":
			config.toast.title("")
		else:
			config.toast.title(f"{newtitle}")
		await embed_builder(luna, description=f"```\nChanged toast title to » {newtitle}```")

bot.add_cog(ToastCog(bot))

class ToastsCog(commands.Cog, name="Toast commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
	
	@commands.command(name = "toasts",
					usage="<on/off>",
					description = "Turn toasts on or off")
	async def toasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Toasts » {color.purple(f'{mode}')}")
			config.toast.toasts(mode)
			await embed_builder(luna, description=f"```\nToasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "logintoasts",
					usage="<on/off>",
					description = "Login toasts")
	async def logintoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Login toasts » {color.purple(f'{mode}')}")
			config.toast.login(mode)
			await embed_builder(luna, description=f"```\nLogin toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "nitrotoasts",
					usage="<on/off>",
					description = "Nitro toasts")
	async def nitrotoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Nitro sniper toasts » {color.purple(f'{mode}')}")
			config.toast.nitro(mode)
			await embed_builder(luna, description=f"```\nNitro sniper toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "giveawaytoasts",
					usage="<on/off>",
					description = "Giveaway toasts")
	async def giveawaytoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Giveaway toasts » {color.purple(f'{mode}')}")
			config.toast.giveaway(mode)
			await embed_builder(luna, description=f"```\nGiveaway toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "privnotetoasts",
					usage="<on/off>",
					description = "Privnote toasts")
	async def privnotetoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Privnote toasts » {color.purple(f'{mode}')}")
			config.toast.privnote(mode)
			await embed_builder(luna, description=f"```\nPrivnote toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "selfbottoasts",
					usage="<on/off>",
					description = "Selfbot toasts")
	async def selfbottoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Selfbot toasts » {color.purple(f'{mode}')}")
			config.toast.selfbot(mode)
			await embed_builder(luna, description=f"```\nSelfbot toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "pingtoasts",
					usage="<on/off>",
					description = "Ping toasts")
	async def pingtoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Pings toasts » {color.purple(f'{mode}')}")
			config.toast.pings(mode)
			await embed_builder(luna, description=f"```\nPings toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "ghostpingtoasts",
					usage="<on/off>",
					description = "Ghostping toasts")
	async def ghostpingtoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Ghostping toasts » {color.purple(f'{mode}')}")
			config.toast.ghostpings(mode)
			await embed_builder(luna, description=f"```\nGhostping toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "friendtoasts",
					usage="<on/off>",
					description = "Friend event toasts")
	async def friendtoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Friend event toasts » {color.purple(f'{mode}')}")
			config.toast.friendevents(mode)
			await embed_builder(luna, description=f"```\nFriend event toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "guildtoasts",
					usage="<on/off>",
					description = "Guild event toasts")
	async def guildtoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Guild event toasts » {color.purple(f'{mode}')}")
			config.toast.guildevents(mode)
			await embed_builder(luna, description=f"```\nGuild event toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "roletoasts",
					usage="<on/off>",
					description = "Role update toasts")
	async def roletoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Role update toasts » {color.purple(f'{mode}')}")
			config.toast.roleupdates(mode)
			await embed_builder(luna, description=f"```\nRole update toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "nicktoasts",
					usage="<on/off>",
					description = "Nickname update toasts")
	async def nicktoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Nickname update toasts » {color.purple(f'{mode}')}")
			config.toast.nickupdates(mode)
			await embed_builder(luna, description=f"```\nNickname update toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "protectiontoasts",
					usage="<on/off>",
					description = "Protection toasts")
	async def protectiontoasts(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Protection toasts » {color.purple(f'{mode}')}")
			config.toast.protection(mode)
			await embed_builder(luna, description=f"```\nProtection toasts » {mode}```")
		else:
			await mode_error(luna, "on or off")

bot.add_cog(ToastsCog(bot))

class WebhookSetupCog(commands.Cog, name="Webhook setup"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "webhooksetup",
					usage="",
					description = "Set up all webhooks")
	async def webhooksetup(self, luna):
		await luna.message.delete()
		try:
			prints.event("Creating webhooks...")
			await embed_builder(luna, description="```\nCreating webhooks...```")
			category = await luna.guild.create_category_channel(name="Luna Webhooks")
			login = await category.create_text_channel("login")
			nitro = await category.create_text_channel("nitro")
			giveaway = await category.create_text_channel("giveaways")
			privnote = await category.create_text_channel("privnotes")
			selfbot = await category.create_text_channel("selfbots")
			pings = await category.create_text_channel("pings")
			ghostpings = await category.create_text_channel("ghostpings")
			friendevents = await category.create_text_channel("friend-events")
			guildevents = await category.create_text_channel("guild-events")
			roleupdates = await category.create_text_channel("role-updates")
			nickupdates = await category.create_text_channel("nickname-updates")
			protection = await category.create_text_channel("protections")

			wlogin = await login.create_webhook(name="Login Webhook")
			wnitro = await nitro.create_webhook(name="Nitro Webhook")
			wgiveaways = await giveaway.create_webhook(name="Giveaways Webhook")
			wprivnote = await privnote.create_webhook(name="Privnotes Webhook")
			wselfbot = await selfbot.create_webhook(name="Selfbots Webhook")
			wpings = await pings.create_webhook(name="Pings Webhook")
			wghostpings = await ghostpings.create_webhook(name="Ghostpings Webhook")
			wfriendevents = await friendevents.create_webhook(name="Friend Events Webhook")
			wguildevents = await guildevents.create_webhook(name="Guild Events Webhook")
			wroleupdates = await roleupdates.create_webhook(name="Role Updates Webhook")
			wnickupdates = await nickupdates.create_webhook(name="Nickname Updates Webhook")
			wprotection = await protection.create_webhook(name="Protections Webhook")

			config.webhook.login_url(wlogin.url)
			config.webhook.nitro_url(wnitro.url)
			config.webhook.giveaway_url(wgiveaways.url)
			config.webhook.privnote_url(wprivnote.url)
			config.webhook.selfbot_url(wselfbot.url)
			config.webhook.pings_url(wpings.url)
			config.webhook.ghostpings_url(wghostpings.url)
			config.webhook.friendevents_url(wfriendevents.url)
			config.webhook.guildevents_url(wguildevents.url)
			config.webhook.roleupdates_url(wroleupdates.url)
			config.webhook.nickupdates_url(wnickupdates.url)
			config.webhook.protection_url(wprotection.url)
			prints.message("Successfully created all webhooks and stored them in the config")
			await embed_builder(luna, title="Webhooks Setup", description=f"```\nSuccessfully created all webhooks and stored them in the config```")
		except Exception as e:
			await error_builder(luna, description=f"```\n{e}```")

bot.add_cog(WebhookSetupCog(bot))

class WebhooksCog(commands.Cog, name="Webhook commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "webhooks",
					usage="<on/off>",
					description = "Webhooks")
	async def webhooks(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Webhooks » {color.purple(f'{mode}')}")
			config.webhook.webhooks(mode)
			await embed_builder(luna, description=f"```\nWebhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wlogin",
					usage="<on/off>",
					description = "Login webhooks")
	async def wlogin(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Login webhooks » {color.purple(f'{mode}')}")
			config.webhook.login(mode)
			await embed_builder(luna, description=f"```\nLogin webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wnitro",
					usage="<on/off>",
					description = "Nitro webhooks")
	async def wnitro(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Nitro webhooks » {color.purple(f'{mode}')}")
			config.webhook.nitro(mode)
			await embed_builder(luna, description=f"```\nNitro webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wgiveaways",
					usage="<on/off>",
					description = "Giveaway webhooks")
	async def wgiveaways(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Giveaway webhooks » {color.purple(f'{mode}')}")
			config.webhook.giveaway(mode)
			await embed_builder(luna, description=f"```\nGiveaway webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wprivnote",
					usage="<on/off>",
					description = "Privnote webhooks")
	async def wprivnote(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Privnote webhooks » {color.purple(f'{mode}')}")
			config.webhook.privnote(mode)
			await embed_builder(luna, description=f"```\nPrivnote webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wselfbot",
					usage="<on/off>",
					description = "Selfbot webhooks")
	async def wselfbot(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Selfbot webhooks » {color.purple(f'{mode}')}")
			config.webhook.selfbot(mode)
			await embed_builder(luna, description=f"```\nSelfbot webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wpings",
					usage="<on/off>",
					description = "Pings webhooks")
	async def wpings(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Pings webhooks » {color.purple(f'{mode}')}")
			config.webhook.pings(mode)
			await embed_builder(luna, description=f"```\nPings webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wghostpings",
					usage="<on/off>",
					description = "Ghostpings webhooks")
	async def wghostpings(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Ghostpings webhooks » {color.purple(f'{mode}')}")
			config.webhook.ghostpings(mode)
			await embed_builder(luna, description=f"```\nGhostpings webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wfriends",
					usage="<on/off>",
					description = "Friend event webhooks")
	async def wfriends(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Friend event webhooks » {color.purple(f'{mode}')}")
			config.webhook.friendevents(mode)
			await embed_builder(luna, description=f"```\nFriend event webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wguilds",
					usage="<on/off>",
					description = "Guild event webhooks")
	async def wguilds(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Guild event webhooks » {color.purple(f'{mode}')}")
			config.webhook.guildevents(mode)
			await embed_builder(luna, description=f"```\nGuild event webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wroles",
					usage="<on/off>",
					description = "Role update webhooks")
	async def wroles(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Role event webhooks » {color.purple(f'{mode}')}")
			config.webhook.roleupdates(mode)
			await embed_builder(luna, description=f"```\nRole event webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wnick",
					usage="<on/off>",
					description = "Nickname update webhooks")
	async def wnick(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Nickname event webhooks » {color.purple(f'{mode}')}")
			config.webhook.nickupdates(mode)
			await embed_builder(luna, description=f"```\nNickname event webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "wprotection",
					usage="<on/off>",
					description = "Protection webhooks")
	async def wprotection(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on" or mode == "off":
			prints.message(f"Protection webhooks » {color.purple(f'{mode}')}")
			config.webhook.protection(mode)
			await embed_builder(luna, description=f"```\nProtection webhooks » {mode}```")
		else:
			await mode_error(luna, "on or off")

bot.add_cog(WebhooksCog(bot))

class WebhookUrlCog(commands.Cog, name="Webhook urls"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "wulogin",
					usage="<url>",
					description = "Login webhook")
	async def wulogin(self, luna, url:str):
		await luna.message.delete()
		config.webhook.login_url(url)
		prints.message(f"Changed login webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged login webhook url to » {url}```")

	@commands.command(name = "wunitro",
					usage="<url>",
					description = "Nitro webhook")
	async def wunitro(self, luna, url:str):
		await luna.message.delete()
		config.webhook.nitro_url(url)
		prints.message(f"Changed nitro webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged nitro webhook url to » {url}```")

	@commands.command(name = "wugiveaway",
					usage="<url>",
					description = "Giveaways webhook")
	async def wugiveaway(self, luna, url:str):
		await luna.message.delete()
		config.webhook.giveaway_url(url)
		prints.message(f"Changed giveaways webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged giveaways webhook url to » {url}```")
		
	@commands.command(name = "wuprivnote",
					usage="<url>",
					description = "Privnotes webhook")
	async def wuprivnote(self, luna, url:str):
		await luna.message.delete()
		config.webhook.privnote_url(url)
		prints.message(f"Changed privnotes webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged privnotes webhook url to » {url}```")

	@commands.command(name = "wuselfbot",
					usage="<url>",
					description = "Selfbots webhook")
	async def wuselfbot(self, luna, url:str):
		await luna.message.delete()
		config.webhook.selfbot_url(url)
		prints.message(f"Changed selfbots webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged selfbots webhook url to » {url}```")

	@commands.command(name = "wupings",
					usage="<url>",
					description = "Pings webhook")
	async def wupings(self, luna, url:str):
		await luna.message.delete()
		config.webhook.pings_url(url)
		prints.message(f"Changed pings webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged pings webhook url to » {url}```")

	@commands.command(name = "wughost",
					usage="<url>",
					description = "Ghostpings webhook")
	async def wughost(self, luna, url:str):
		await luna.message.delete()
		config.webhook.ghostpings_url(url)
		prints.message(f"Changed ghostpings webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged ghostpings webhook url to » {url}```")

	@commands.command(name = "wufriends",
					usage="<url>",
					description = "Friend events webhook")
	async def wufriends(self, luna, url:str):
		await luna.message.delete()
		config.webhook.friendevents_url(url)
		prints.message(f"Changed friend events webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged friend events webhook url to » {url}```")

	@commands.command(name = "wuguilds",
					usage="<url>",
					description = "Guild events webhook")
	async def wuguilds(self, luna, url:str):
		await luna.message.delete()
		config.webhook.guildevents_url(url)
		prints.message(f"Changed guild events webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged guild events webhook url to » {url}```")

	@commands.command(name = "wuroles",
					usage="<url>",
					description = "Role updates webhook")
	async def wuroles(self, luna, url:str):
		await luna.message.delete()
		config.webhook.roleupdates_url(url)
		prints.message(f"Changed role updates webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged role updates webhook url to » {url}```")

	@commands.command(name = "wunick",
					usage="<url>",
					description = "Nick updates webhook")
	async def wunick(self, luna, url:str):
		await luna.message.delete()
		config.webhook.nickupdates_url(url)
		prints.message(f"Changed nick updates webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged nick updates webhook url to » {url}```")

	@commands.command(name = "wuprotection",
					usage="<url>",
					description = "Protection webhook")
	async def wuprotection(self, luna, url:str):
		await luna.message.delete()
		config.webhook.protection_url(url)
		prints.message(f"Changed protection webhook url to » {color.purple(f'{url}')}")
		await embed_builder(luna, description=f"```\nChanged protection webhook url to » {url}```")

bot.add_cog(WebhookUrlCog(bot))

class WebhookCog(commands.Cog, name="Webhook customisation"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.command(name = "wtitle",
					usage="<title>",
					description = "Customize the webhook title")
	async def wtitle(self, luna, *, newtitle:str):
		await luna.message.delete()
		prints.message(f"Changed webhook title to » {color.purple(f'{newtitle}')}")
		if newtitle == "None":
			config.webhook.title("")
		else:
			config.webhook.title(f"{newtitle}")
		await embed_builder(luna, description=f"```\nChanged webhook title to » {newtitle}```")

	@commands.command(name = "wfooter",
					usage="<footer>",
					description = "Customize the webhook footer")
	async def wfooter(self, luna, *, newfooter:str):
		await luna.message.delete()

		prints.message(f"Changed webhook footer to » {color.purple(f'{newfooter}')}")
		if newfooter == "None":
			config.webhook.footer("")
		else:
			config.webhook.footer(f"{newfooter}")
		await embed_builder(luna, description=f"```\nChanged webhook footer to » {newfooter}```")

	@commands.command(name = "wimage",
					usage="<url>",
					description = "Customize the thumbnail image")
	async def wimage(self, luna, newimageurl:str):
		await luna.message.delete()

		prints.message(f"Changed webhook thumbnail url to » {color.purple(f'{newimageurl}')}")
		if newimageurl == "None":
			config.webhook.image_url("")
		else:
			config.webhook.image_url(f"{newimageurl}")
		await embed_builder(luna, description=f"```\nChanged webhook thumbnail url to » {newimageurl}```")

	@commands.command(name = "whexcolor",
					usage="<#hex>",
					description = "Webhook hexadecimal color")
	async def whexcolor(self, luna, newhexcolor:str):
		await luna.message.delete()

		prints.message(f"Changed webhook color to » {color.purple(f'{newhexcolor}')}")
		if newhexcolor == "None":
			config.webhook.hex_color("")
		else:
			config.webhook.hex_color(f"{newhexcolor}")
		await embed_builder(luna, description=f"```\nChanged webhook color to » {newhexcolor}```")

	@commands.command(name = "wmatch",
					usage="",
					description = "Match webhook theme")
	async def wmatch(self, luna):
		await luna.message.delete()
		config.webhook.title(theme.title())
		config.webhook.footer(theme.footer())
		config.webhook.image_url(theme.image_url())
		theme_config = files.json("Luna/config.json", "theme", documents=True)
		if theme_config == "default":
			hex_color = hexcolorvar_request
		else:
			hex_color = files.json(f"Luna/themes/{theme_config}", "hex_color", documents=True)
		config.webhook.hex_color(hex_color)
		prints.message(f'Matched webhook to » {color.purple(files.json("Luna/config.json", "theme", documents=True))}')
		await embed_builder(luna, description=f'```\nMatched webhook to » {files.json("Luna/config.json", "theme", documents=True)}```')

bot.add_cog(WebhookCog(bot))

class MiscCog(commands.Cog, name="Miscellaneous commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "uptime",
					usage="",
					description = "Uptime")
	async def uptime(self, luna):
		await luna.message.delete()
		await embed_builder(luna, title="Uptime",description=f"```\n{hour:02d} Hours, {minute:02d} Minutes and {second:02d} Seconds```")


	@commands.command(name = "logout",
					usage="",
					description = "Logout of the bot")
	async def logout(self, luna):
		await luna.message.delete()
		prints.message(f"Logging out of the bot")
		await embed_builder(luna, description=f"```\nLogging out of the bot```")
		await bot.logout()

	@commands.command(name = "shutdown",
					usage="",
					description = "Shutdown the bot")
	async def shutdown(self, luna):
		await luna.message.delete()
		os._exit(0)

	# @commands.command(name = "thelp",
	# 				usage="",
	# 				description = "All commands in a text file")
	# async def thelp(self, luna):
	# 	await luna.message.delete()

	# 	#///////////////////////////////////////////////////////////////////

	# 	prefix = files.json("Luna/config.json", "prefix", documents=True)

	# 	#///////////////////////////////////////////////////////////////////
	# 	try:
	# 		cog = self.bot.get_cog('Help commands')
	# 		commands = cog.get_commands()
	# 		helpcommands = ""
	# 		for command in commands:
	# 			helpcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Administrative commands')
	# 		commands = cog.get_commands()
	# 		admincommands = ""
	# 		for command in commands:
	# 			admincommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Animated commands')
	# 		commands = cog.get_commands()
	# 		animatedcommands = ""
	# 		for command in commands:
	# 			animatedcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Text commands')
	# 		commands = cog.get_commands()
	# 		textcommands = ""
	# 		for command in commands:
	# 			textcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"
				
	# 		cog = self.bot.get_cog('Image commands')
	# 		commands = cog.get_commands()
	# 		imagecommands = ""
	# 		for command in commands:
	# 			imagecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Troll commands')
	# 		commands = cog.get_commands()
	# 		trollcommands = ""
	# 		for command in commands:
	# 			trollcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Fun commands')
	# 		commands = cog.get_commands()
	# 		funcommands = ""
	# 		for command in commands:
	# 			funcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Tools commands')
	# 		commands = cog.get_commands()
	# 		toolscommands = ""
	# 		for command in commands:
	# 			toolscommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Nettool commands')
	# 		commands = cog.get_commands()
	# 		nettoolscommands = ""
	# 		for command in commands:
	# 			nettoolscommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Util commands')
	# 		commands = cog.get_commands()
	# 		utilscommands = ""
	# 		for command in commands:
	# 			utilscommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Abusive commands')
	# 		commands = cog.get_commands()
	# 		abusecommands = ""
	# 		for command in commands:
	# 			abusecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Raid commands')
	# 		commands = cog.get_commands()
	# 		raidcommands = ""
	# 		for command in commands:
	# 			raidcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Nuking commands')
	# 		commands = cog.get_commands()
	# 		nukecommands = ""
	# 		for command in commands:
	# 			nukecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Protection commands')
	# 		commands = cog.get_commands()
	# 		protectioncommands = ""
	# 		for command in commands:
	# 			protectioncommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Miscellaneous commands')
	# 		commands = cog.get_commands()
	# 		misccommands = ""
	# 		for command in commands:
	# 			misccommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Settings commands')
	# 		commands = cog.get_commands()
	# 		settingscommands = ""
	# 		for command in commands:
	# 			settingscommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Share commands')
	# 		commands = cog.get_commands()
	# 		sharecommands = ""
	# 		for command in commands:
	# 			sharecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Toast customization')
	# 		commands = cog.get_commands()
	# 		toastcustomcommands = ""
	# 		for command in commands:
	# 			toastcustomcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Toast commands')
	# 		commands = cog.get_commands()
	# 		toastcommands = ""
	# 		for command in commands:
	# 			toastcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Customization commands')
	# 		commands = cog.get_commands()
	# 		customizationcommands = ""
	# 		for command in commands:
	# 			customizationcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Webhook customisation')
	# 		commands = cog.get_commands()
	# 		webhookcommands = ""
	# 		for command in commands:
	# 			webhookcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('NSFW commands')
	# 		commands = cog.get_commands()
	# 		nsfwcommands = ""
	# 		for command in commands:
	# 			nsfwcommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Cryptocurrency commands')
	# 		commands = cog.get_commands()
	# 		cryptocommands = ""
	# 		for command in commands:
	# 			cryptocommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Encode commands')
	# 		commands = cog.get_commands()
	# 		encodecommands = ""
	# 		for command in commands:
	# 			encodecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		cog = self.bot.get_cog('Decode commands')
	# 		commands = cog.get_commands()
	# 		decodecommands = ""
	# 		for command in commands:
	# 			decodecommands+=f"{prefix + command.name + ' ' + command.usage:<17} » {command.description}\n"

	# 		#///////////////////////////////////////////////////////////////////

	# 		commandcount = len(self.bot.commands)

	# 		file = open(os.path.join(files.documents(), "Luna/commands.txt"), "w")
	# 		file.write(f"{commandcount} Commands\n\n<> is required | [] is optional\n\nCategories:\n{helpcommands}\nAdmin Commands:\n{admincommands}\nAnimated Commands:\n{animatedcommands}\nText Commands:\n{textcommands}\nImage Commands:\n{imagecommands}\nTroll Commands:\n{trollcommands}\nFun Commands:\n{funcommands}\nTools:\n{toolscommands}\nNetworking Tools\n{nettoolscommands}\nUtilities\n{utilscommands}\nAbusive Commands\n{abusecommands}\nRaiding\n{raidcommands}\nNuking\n{nukecommands}\nProtections\n{protectioncommands}\nMiscellaneous\n{misccommands}\nSettings\n{settingscommands}\nSharing\n{sharecommands}\nCustomization\n{customizationcommands}\nToast Settings\n{toastcommands}\nToast Customization\n{toastcustomcommands}\nWebhook Settings\n{webhookcommands}\nNSFW\n{nsfwcommands}\nCryptocurrency\n{cryptocommands}\nEncode\n{encodecommands}\nDecode\n{decodecommands}")
	# 		file.close()
	# 		await embed_builder(luna, title="Text Help", description=f"```\nSaved all commands in commands.txt```")
	# 	except Exception as e:
	# 		print(e)

	@commands.command(name = "update",
					usage="",
					description = "Updates Luna")
	async def update(self, luna):
		await luna.message.delete()
		r = requests.get("https://pastebin.com/raw/jBrn4WU4").json()
		version_url = r["version"]
		if developer_mode:
			await embed_builder(luna, title="Update", description=f"```\nDeveloper mode active! No updates will be downloaded.```")
		elif version == version_url:
			await embed_builder(luna, title="Update", description=f"```\nYou are on the latest version! ({version_url})```")
		else:
			if files.json("Luna/notifications/toasts.json", "login", documents=True) == "on" and files.json("Luna/notifications/toasts.json", "toasts", documents=True) == "on":
				notify.toast(message=f"Starting update {version_url}")
			if files.json("Luna/webhooks/webhooks.json", "login", documents=True) == "on" and files.json("Luna/webhooks/webhooks.json", "webhooks", documents=True) == "on" and not webhook.login_url() == "webhook-url-here":
				notify.webhook(url=webhook.login_url(), name="login", description=f"Starting update {version_url}")
			await embed_builder(luna, title="Update", description=f"```\nStarted update » {version_url}```")
			luna.update()

	@commands.command(name = "restart",
					usage="",
					aliases=['reboot'],
					description = "Restart Luna")
	async def restart(self, luna):
		await luna.message.delete()
		# if configs.mode() == 2:
		# 	sent = await luna.send(f"```ini\n[ Restarting ]\n\nAllow up to 5 seconds\n\n[ {theme.footer()} ]```")
		# 	await asyncio.sleep(3)
		# 	await sent.delete()
		# if configs.mode() == 3:
		# 	sent = await luna.send(f"> **Restarting**\n> \n> Allow up to 5 seconds\n> \n> {theme.footer()}")
		# 	await asyncio.sleep(3)
		# 	await sent.delete()
		# else:
		# 	embed = discord.Embed(title="Restarting", url=theme.title_url(), description=f"```\nAllow up to 5 seconds```", color=theme.hex_color())
		# 	embed.set_thumbnail(url=theme.image_url())
		# 	embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
		# 	embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
		# 	embed.set_image(url=theme.large_image_url())
		# 	sent = await luna.send(embed=embed)
		# 	await asyncio.sleep(3)
		# 	await sent.delete()
		restart_program()

	@commands.command(name = "shutdown",
					usage="",
					description = "Shutdown Luna")
	async def shutdown(self, luna):
		await luna.message.delete()
		if configs.mode() == 2:
			sent = await luna.send(f"```ini\n[ Restarting ]\n\nShutting down\n\n[ {theme.footer()} ]```")
			await asyncio.sleep(3)
			await sent.delete()
		if configs.mode() == 3:
			await embed_builder(luna, )
			sent = await luna.send(f"> **Restarting**\n> \n> Allow up to 5 seconds\n> \n> {theme.footer()}")
			await asyncio.sleep(3)
			await sent.delete()
		else:
			embed = discord.Embed(title="Restarting", url=theme.title_url(), description=f"```\nAllow up to 5 seconds```", color=theme.hex_color())
			embed.set_thumbnail(url=theme.image_url())
			embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
			embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
			embed.set_image(url=theme.large_image_url())
			sent = await luna.send(embed=embed)
			await asyncio.sleep(3)
			await sent.delete()
		restart_program()

	@commands.command(name = "clear",
					aliases=['cls'],
					usage="",
					description = "Clear the console")
	async def clear(self, ctx):
		await ctx.message.delete()
		luna.console(clear=True)
		if privacy:
			command_count = len(bot.commands)
			cog = bot.get_cog('Custom commands')
			try:
				custom = cog.get_commands()
				custom_command_count = 0
				for command in custom:
					custom_command_count += 1
			except:
				custom_command_count = 0
			prefix = files.json("Luna/config.json", "prefix", documents=True)
			print(motd.center(os.get_terminal_size().columns))
			if beta:
				print("Beta Build".center(os.get_terminal_size().columns))
			prefix = files.json("Luna/config.json", "prefix", documents=True)
			console_mode = files.json("Luna/console/console.json", "mode", documents=True)
			if console_mode == "2":
				riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
				themesvar = files.json("Luna/config.json", "theme", documents=True)
				deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
				startup_status = files.json("Luna/config.json", "startup_status", documents=True)
				nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
				giveawayjoiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
				if themesvar == "default":
					pass
				else:
					themesvar = themesvar[:-5]
				ui_user = f" {color.purple('User:')} {'Luna#0000':<26}"
				ui_guilds = f" {color.purple('Guilds:')} {'0':<24}"
				ui_friends = f" {color.purple('Friends:')} {'0':<23}"
				ui_prefix = f" {color.purple('Prefix:')} {prefix:<24}"
				ui_theme = f" {color.purple('Theme:')} {themesvar:<25}"
				ui_commands = f" {color.purple('Commands:')} {command_count-custom_command_count:<22}"
				ui_commands_custom = f" {color.purple('Custom Commands:')} {custom_command_count:<15}"
				ui_nitro_sniper = f" {color.purple('Nitro Sniper:')} {nitro_sniper}"
				ui_giveaway_sniper = f" {color.purple('Giveaway Joiner:')} {giveawayjoiner}"
				ui_riskmode = f" {color.purple('Riskmode:')} {riskmode}"
				ui_deletetimer = f" {color.purple('Delete Timer:')} {deletetimer}"
				ui_startup = f" {color.purple('Startup Status:')} {startup_status}"
				print()
				print(f"               ═════════════ {color.purple('User')} ═════════════      ═══════════ {color.purple('Settings')} ═══════════")
				print(f"               {ui_user}     {ui_prefix}")
				print(f"               {ui_guilds}     {ui_theme}")
				print(f"               {ui_friends}     {ui_nitro_sniper}")
				print(f"               ════════════════════════════════      {ui_giveaway_sniper}")
				print(f"               ═════════════ {color.purple('Luna')} ═════════════      {ui_riskmode}")
				print(f"               {ui_commands}     {ui_deletetimer}")
				print(f"               {ui_commands_custom}     {ui_startup}")
				print(f"               ════════════════════════════════      ════════════════════════════════\n")
			else:
				print()
				print(f"                           {color.purple('[')}+{color.purple('] CONNECTED')}")
				print(f"                           {color.purple('[')}+{color.purple(']')} Luna#0000 | {color.purple('0')} Guilds | {color.purple('0')} Friends")
				print(f"                           {color.purple('[')}+{color.purple(']')} {prefix}\n")
		else:
			command_count = len(bot.commands)
			cog = bot.get_cog('Custom commands')
			try:
				custom = cog.get_commands()
				custom_command_count = 0
				for command in custom:
					custom_command_count += 1
			except:
				custom_command_count = 0
			prefix = files.json("Luna/config.json", "prefix", documents=True)
			print(motd.center(os.get_terminal_size().columns))
			if beta:
				print("Beta Build".center(os.get_terminal_size().columns))
			prefix = files.json("Luna/config.json", "prefix", documents=True)
			console_mode = files.json("Luna/console/console.json", "mode", documents=True)
			if console_mode == "2":
				riskmode = files.json("Luna/config.json", "risk_mode", documents=True)
				themesvar = files.json("Luna/config.json", "theme", documents=True)
				deletetimer = int(files.json("Luna/config.json", "delete_timer", documents=True))
				startup_status = files.json("Luna/config.json", "startup_status", documents=True)
				nitro_sniper = files.json("Luna/snipers/nitro.json", "sniper", documents=True)
				giveawayjoiner = files.json("Luna/snipers/giveaway.json", "joiner", documents=True)
				if themesvar == "default":
					pass
				else:
					themesvar = themesvar[:-5]
				bot_user = f"{bot.user}"
				ui_user = f" {color.purple('User:')} {bot_user:<26}"
				ui_guilds = f" {color.purple('Guilds:')} {len(bot.guilds):<24}"
				ui_friends = f" {color.purple('Friends:')} {len(bot.user.friends):<23}"
				ui_prefix = f" {color.purple('Prefix:')} {prefix:<24}"
				ui_theme = f" {color.purple('Theme:')} {themesvar:<25}"
				ui_commands = f" {color.purple('Commands:')} {command_count-custom_command_count:<22}"
				ui_commands_custom = f" {color.purple('Custom Commands:')} {custom_command_count:<15}"
				ui_nitro_sniper = f" {color.purple('Nitro Sniper:')} {nitro_sniper}"
				ui_giveaway_sniper = f" {color.purple('Giveaway Joiner:')} {giveawayjoiner}"
				ui_riskmode = f" {color.purple('Riskmode:')} {riskmode}"
				ui_deletetimer = f" {color.purple('Delete Timer:')} {deletetimer}"
				ui_startup = f" {color.purple('Startup Status:')} {startup_status}"
				print()
				print(f"               ═════════════ {color.purple('User')} ═════════════      ═══════════ {color.purple('Settings')} ═══════════")
				print(f"               {ui_user}     {ui_prefix}")
				print(f"               {ui_guilds}     {ui_theme}")
				print(f"               {ui_friends}     {ui_nitro_sniper}")
				print(f"               ════════════════════════════════      {ui_giveaway_sniper}")
				print(f"               ═════════════ {color.purple('Luna')} ═════════════      {ui_riskmode}")
				print(f"               {ui_commands}     {ui_deletetimer}")
				print(f"               {ui_commands_custom}     {ui_startup}")
				print(f"               ════════════════════════════════      ════════════════════════════════\n")
			else:
				print()
				print(f"                           {color.purple('[')}+{color.purple('] CONNECTED')}")
				print(f"                           {color.purple('[')}+{color.purple(']')} {bot.user} | {color.purple(f'{len(bot.guilds)}')} Guilds | {color.purple(f'{len(bot.user.friends)}')} Friends")
				print(f"                           {color.purple('[')}+{color.purple(']')} {prefix}\n")
		print(f"═══════════════════════════════════════════════════════════════════════════════════════════════════\n")
		prints.message(f"{color.purple(f'{command_count-custom_command_count}')} commands | {color.purple(f'{custom_command_count}')} custom commands")

	@commands.command(name = "covid",
					aliases=['corona'],
					usage="",
					description = "Corona statistics")
	async def covid(self, luna):
		await luna.message.delete()
		request = requests.get(f'https://api.covid19api.com/summary')
		data = request.json()
		info = data['Global']
		totalconfirmed = info['TotalConfirmed']
		totalrecovered = info['TotalRecovered']
		totaldeaths = info['TotalDeaths']
		newconfirmed = info['NewConfirmed']
		newrecovered = info['NewRecovered']
		newdeaths = info['NewDeaths']
		date = info['Date']
		await embed_builder(luna, title="Covid-19 Statistics", description=f"```Total Confirmed Cases\n{totalconfirmed}``````Total Deaths\n{totaldeaths}``````Total Recovered\n{totalrecovered}``````New Confirmed Cases\n{newconfirmed}``````New Deaths\n{newdeaths}``````New Recovered\n{newrecovered}``````Date\n{date}```")

	typing = False

	@commands.command(name = "typing",
					usage="<on/off>",
					description = "Enable or disable typing")
	async def typing(self, luna, mode:str):
		await luna.message.delete()
		if mode == "on":
			await embed_builder(luna, title="Typing", description=f"```\nTyping enabled```")
			typing = True
			while typing:
				async with luna.typing():
					await asyncio.sleep(1)
					if typing == False:
						break
		elif mode == "off":
			await embed_builder(luna, title="Typing", description=f"```\nTyping disabled```")
			typing = False
		else:
			await mode_error(luna, "on or off")

	@commands.command(name = "hwid",
					usage="",
					description = "Prints your hwid")
	async def hwid(self, luna):
		await luna.message.delete()
		hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\r\n')[1].strip('\r').strip()
		prints.message(f"Your HWID » {hwid}")

bot.add_cog(MiscCog(bot))
class GamesCog(commands.Cog, name="Game commands"):
	def __init__(self, bot:commands.bot):
		self.bot = bot

	@commands.command(name = "fnshop",
					usage="",
					description = "Fortnite shop")
	async def fnshop(self, luna):
		await luna.message.delete()
		await embed_builder(luna, title="Fortnite Shop", large_image="https://api.nitestats.com/v1/shop/image")

	@commands.command(name = "fnmap",
					usage="",
					description = "Fortnite map")
	async def fnmap(self, luna):
		await luna.message.delete()
		await embed_builder(luna, title="Fortnite Map", large_image="https://media.fortniteapi.io/images/map.png?showPOI=true")

	@commands.command(name = "fnnews",
					usage="",
					description = "Fortnite news")
	async def fnnews(self, luna):
		await luna.message.delete()
		fortnite = requests.get("https://fortnite-api.com/v2/news/br").json()
		await embed_builder(luna, title="Fortnite News", large_image=fortnite["data"]["image"])

bot.add_cog(GamesCog(bot))

def convert_to_text(embed: discord.Embed):
	largeimagevar = theme.large_image_url()
	if embed.image.url == "":
		if embed.description.endswith("\n"):
			text_mode_builder = f"```css\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('```', '')}\n[ {embed.footer.text} ]\n```"
		else:
			text_mode_builder = f"```css\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('```', '')}\n\n[ {embed.footer.text} ]\n```"
		return text_mode_builder
	elif embed.image.url == largeimagevar:
		if embed.description.endswith("\n"):
			text_mode_builder = f"```css\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('```', '')}\n[ {embed.footer.text} ]\n```"
		else:
			text_mode_builder = f"```css\n[ {embed.title.replace('**', '')} ]\n\n{embed.description.replace('```', '')}\n\n[ {embed.footer.text} ]\n```"
		return text_mode_builder
	else:
		return embed.image.url

def convert_to_indent(embed: discord.Embed):
	largeimagevar = theme.large_image_url()
	if embed.image.url == "":
		text = ""

		for line in embed.description.split("\n"):
			indent = "> " + line
			text += indent + "\n"

		if embed.description.endswith("\n"):
			text = text[:-2]
			indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
		else:
			indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
		return indent_builder
	elif embed.image.url == largeimagevar:
		text = ""

		for line in embed.description.split("\n"):
			indent = "> " + line
			text += indent + "\n"

		if embed.description.endswith("\n"):
			text = text[:-2]
			indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
		else:
			indent_builder = f"> **{embed.title}**\n> \n{text}> {embed.footer.text}"
		return indent_builder
	else:
		return embed.image.url


async def send(luna, embed, delete_after=None):
	deletetimer = configs.delete_timer()
	if delete_after is not None:
		deletetimer = delete_after
	mode = configs.mode()
	if mode == 2:
		await luna.send(convert_to_text(embed), delete_after=deletetimer)
	elif mode == 3:
		await luna.send(convert_to_indent(embed), delete_after=deletetimer)
	else:
		await luna.send(embed=embed, delete_after=deletetimer)

async def mode_error(luna, modes:str):
    if configs.error_log() == "console":
        prints.error(f"That mode does not exist! Only {modes}")
    else:
        embed = discord.Embed(title="Error", description=f"```\nThat mode does not exist!\nOnly {modes}```", color=0xE10959)
        embed.set_thumbnail(url=theme.image_url())
        embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
        embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
        embed.set_image(url=theme.large_image_url())
        await send(luna, embed)

async def embed_builder(luna, title=None, description="", color=None, large_image=None, thumbnail=None, delete_after=None, footer_extra=None, footer=None):
	"""
	Luna's main function for creating embeds with the theme applied.\n
	Parse `luna = ctx` as first argument. (Important)\n
	`title="foo"` <- Defines the title. (Optional)\n
	`description="foo"` <- Defines the description. (Optional)\n
	`color=0xffffff` <- Defines the hexcolor. (Optional)\n
	`large_image="url"` <- Defines the large image url. (Optional)\n
	`thumbnail="url"` <- Defines the thumbnail url. (Optional)\n
	`delete_after=30` <- Defines the auto delete time after the embed is sent. (Optional)\n
	"""
	if large_image == None:
		large_image = theme.large_image_url()
	if color == None:
		color = theme.hex_color()
	if thumbnail == None:
		thumbnail = theme.image_url()
	elif thumbnail == "None":
		thumbnail = ""
	if title == None:
		title = theme.title()
	if not footer == "None":
		if footer_extra == None:
			if files.json("Luna/protections/config.json", "footer", documents=True) == True:
				footer_extra = f"Protections » {active_protections} | {theme.footer()}"
			else:
				footer_extra = theme.footer()
		else:
			if files.json("Luna/protections/config.json", "footer", documents=True) == True:
				footer_extra = f"{footer_extra} | Protections » {active_protections} | {theme.footer()}"
			else:
				footer_extra = f"{footer_extra} | {theme.footer()}"
	else:
		footer_extra = ""
	embed = discord.Embed(title=title, url=theme.title_url(), description=description, color=color)
	embed.set_thumbnail(url=thumbnail)
	embed.set_footer(text=footer_extra, icon_url=theme.footer_icon_url())
	embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
	embed.set_image(url=large_image)
	await send(luna, embed, delete_after)

async def error_builder(luna, description=""):
    if configs.error_log() == "console":
        prints.error(description.replace('\n',' ').replace('`',''))
    else:
        embed = discord.Embed(title="Error", description=description, color=0xE10959)
        embed.set_thumbnail(url=theme.image_url())
        embed.set_footer(text=theme.footer(), icon_url=theme.footer_icon_url())
        embed.set_author(name=theme.author(), url=theme.author_url(), icon_url=theme.author_icon_url())
        embed.set_image(url=theme.large_image_url())
        await send(luna, embed)

# ///////////////////////////////////////////////////////////////

# @bot.command(name = "speed", usage="", description = "Command speed test")
# async def speed(luna):
# 	sniped_start_time = time.time()
# 	embed = discord.Embed(title="Help", description=f"This is a speed test", color=0xE10959)
# 	embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/406907871998246924/70bdf0218ac762d8a7dbf8c8758ec62d.webp?size=4096")
# 	embed.set_footer(text="Luna", icon_url="https://cdn.discordapp.com/avatars/406907871998246924/70bdf0218ac762d8a7dbf8c8758ec62d.webp?size=4096")
# 	await luna.send(embed=embed)
# 	await luna.send(f"It took {'%.3fs' % (time.time() - sniped_start_time)} to send.")

# RPC Main
# if files.json("Luna/rpc.json", "rich_presence", documents=True) == "on":
# 	try:
# 		RPC = Presence(rpc.client_id())# you need to add () since its a function
# 		RPC.connect()

# 		if rpc.button_2_text() == "" and rpc.button_2_url() == "":
# 			RPC.update(state=f"{rpc.state()}", details=f"{rpc.details()}", large_image=f"{rpc.large_image()}", large_text=f"{rpc.large_text()}", small_image=f"{rpc.small_image()}", small_text=f"{rpc.small_text()}", buttons=[{"label": f"{rpc.button_1_text()}", "url": f"{rpc.button_1_url()}"}])
# 		elif rpc.small_image() == "" and rpc.small_text() == "":
# 			RPC.update(state=f"{rpc.state()}", details=f"{rpc.details()}", large_image=f"{rpc.large_image()}", large_text=f"{rpc.large_text()}", buttons=[{"label": f"{rpc.button_1_text()}", "url": f"{rpc.button_1_url()}"},{"label":f"{rpc.button_2_text()}","url":f"{rpc.button_2_url()}"}])
# 		elif rpc.large_text() == "":
# 			RPC.update(state=f"{rpc.state()}", details=f"{rpc.details()}", large_image=f"{rpc.large_image()}", small_image=f"{rpc.small_image()}", small_image_text=f"{rpc.small_text()}", buttons=[{"label": f"{rpc.button_1_text()}", "url": f"{rpc.button_1_url()}"},{"label":f"{rpc.button_2_text()}","url":f"{rpc.button_2_url()}"}])
# 		elif rpc.state() == "":
# 			RPC.update(details=f"{rpc.details()}", large_image=f"{rpc.large_image()}", large_text=f"{rpc.large_text()}", small_image=f"{rpc.small_image()}", small_text=f"{rpc.small_text()}", buttons=[{"label": f"{rpc.button_1_text()}", "url": f"{rpc.button_1_url()}"},{"label":f"{rpc.button_2_text()}","url":f"{rpc.button_2_url()}"}])
# 		else:
# 			RPC.update(state=f"{rpc.state()}", details=f"{rpc.details()}", large_image=f"{rpc.large_image()}", large_text=f"{rpc.large_text()}", small_image=f"{rpc.small_image()}", small_text=f"{rpc.small_text()}", buttons=[{"label": f"{rpc.button_1_text()}", "url": f"{rpc.button_1_url()}"},{"label":f"{rpc.button_2_text()}","url":f"{rpc.button_2_url()}"}])
# 	except Exception as e:
# 		prints.error(e)
# 		os.system('pause')

# notify.webhook(url="https://discord.com/api/webhooks/909150388681310218/UTUTPihWbPzaOeXoxe7zyfHJJBBf4s_krKys-LB0uSmQZvB42QnQRVndygIc8ehq13cf", description="This is a test")

# ///////////////////////////////////////////////////////////////
# Main Thread, Don't Touch

if not developer_mode:
	check_debuggers_thread()

if os.path.splitext(__file__)[1] == ".pyc":
	os._exit(0)

luna.title("Luna")
luna.file_check()
luna.authentication()
luna.wizard()
