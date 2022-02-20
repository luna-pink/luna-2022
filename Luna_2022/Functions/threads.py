from Functions.functions import *
from variables import *
import time
from CEA256 import *

def uptime_thread():
    username = JsonHandler("auth.json", "data").read_value("username")
    username = Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(username)
    global hour
    global minute
    global second
    global day
    hour = 0
    minute = 0
    second = 0
    day = 0
    while True:
        if not day == 0:
            title(f"Luna - {username} | {day} Days, {hour:02d} Hours, {minute:02d} Minutes, {second:02d} Seconds")
        else:
            title(f"Luna - {username} | {hour:02d}:{minute:02d}:{second:02d}")
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
            day += 1