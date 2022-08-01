from .functions import *


def get_prefix():
    return files.json("data/config.json", "prefix", documents=False)


class configs:

    def delete_timer():
        """Get to delete timer in the config file"""
        return int(files.json("data/config.json", "delete_timer", documents=False))

    def mode():
        """Get the mode in the config file"""
        return int(files.json("data/config.json", "mode", documents=False))

    def error_log():
        """Get the error log in the config file"""
        return files.json("data/config.json", "error_log", documents=False)

    def risk_mode():
        """Get the risk mode in the config file"""
        return files.json("data/config.json", "risk_mode", documents=False)

    def stream_url():
        """Get the stream url in the config file"""
        return files.json("data/config.json", "stream_url", documents=False)

    def startup_status():
        """Get the startup status in the config file"""
        return files.json("data/config.json", "startup_status", documents=False)

    def password():
        """
        It takes the password from the json file, and decrypts it
        :return: A string.
        """
        return Decryption('5QXapyTDbrRwW4ZBnUgPGAs9CeVSdiLk').CEA256(files.json("data/discord.luna", "password", documents=False))

    def share():
        """Get the share mode in the config file"""
        return files.json("data/sharing.json", "share", documents=False)

    def share_id():
        """Get the share id in the config file"""
        return files.json("data/sharing.json", "user_id", documents=False)
