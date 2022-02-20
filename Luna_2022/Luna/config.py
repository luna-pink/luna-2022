from FileHandling.filehandler import *
from CEA256 import *

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