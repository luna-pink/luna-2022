
from Authentication.atlas import *
from Functions import *
from variables import *
from Encryption import *
from Encryption.CEAShim256 import *
import subprocess
import os

username_value = "Nshout"
password_value = "luna"
key_value = "IP9UY-WA8J3-J3YM2-2T34U-6IS7I"

auth_luna = Atlas(
    "45.41.240.7", 9696,
    "41014302915357696839", "SqpozXfd6dbv5KdNLvtefJjudikBkbbp"
)

def auth_connect(username):
    print("Connecting to Atlas...")
    try:
        auth_luna.connect()
    except BaseException:
        print("Failed to connect to Atlas")
    auth_luna.Identify(username)

def auth_validate():
    hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(
        '\\r\\n'
    )[1].strip('\\r').strip()
    auth_luna.ValidateUserHWID(hwid)
    auth_luna.ValidateEntitlement("LunaSB")

def login():
    auth_connect(username_value)
    print("Connected to Atlas")
    auth_luna.Login(username_value, password_value)
    print("Logged in")
    auth_validate()
    print("Validated")
    print("USER ID")
    auth_luna.GetUserUID()
    auth_luna.disconnect()
    print("Disconnected from server")
    print("LOGGED IN")
    os.system("pause")

def register():
    try:
        hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(
            '\\r\\n'
        )[1].strip('\\r').strip()
        try:
            print("Connecting to server...")
            auth_luna.connect()
        except BaseException:
            auth_luna.disconnect()
            print("Disconnected from server")
            print("Connection failed, try again later")
            return
        try:
            auth_luna.CheckLicenseKeyValidity(key_value)
        except BaseException:
            auth_luna.disconnect()
            print("Disconnected from server")
            print("CODE 1")
            return
        try:
            auth_luna.Register(username_value, password_value)
            auth_luna.Identify(username_value)
            auth_luna.Login(username_value, password_value)
            auth_luna.InitAppUser(hwid)
            auth_luna.RedeemEntitlement(key_value, "LunaSB")
            auth_luna.disconnect()
            print("Disconnected from server")
            print("CODE 2")
        except Exception as e:
            auth_luna.disconnect()
            print("Disconnected from server")
            print(e)
    except Exception as e:
        auth_luna.disconnect()
        print(e)
    os.system("pause")


login()