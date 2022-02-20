from Functions.functions import *
from variables import *
import time

def uptime_thread():
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
            title(f"Luna {version_url} | {day} Days, {hour:02d} Hours, {minute:02d} Minutes, {second:02d} Seconds")
        else:
            title(f"Luna {version_url} | {hour:02d}:{minute:02d}:{second:02d}")
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