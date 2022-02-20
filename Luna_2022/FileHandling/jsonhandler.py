import json
import os
from discord import *

# /////////////////////////////////////////////////////////////////////////////

from variables import *

# /////////////////////////////////////////////////////////////////////////////


class JsonHandler:
    """
    This class handles the json files.
    """
    def __init__(self, file_name: str, file_path: str = "./"):
        """
        Initialize the JsonHandler class.
        Does a check if the file exists, if not creates it, before writing to it.
        (Default: "./", if "Luna" in the file_path, the path is changed to "Documents/Luna/")

        Args:
            file_name: The name of the file.
            file_path: The path of the file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if file_path.title().startswith("Luna"):
            file_path = os.path.expanduser(f"~/Documents/{file_path}")
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        self.file_path = file_path
        if not file_name.endswith(".json"):
            file_name += ".json"
        self.file_name = file_name
        self.file_path_name = os.path.join(self.file_path, self.file_name)
        if not os.path.exists(self.file_path_name):
            with open(self.file_path_name, "w+", encoding="utf-8") as file:
                file.write("{}")

    def read_value(self, key: str) -> str:
        """
        Read a value from a Json file.

        Args:
            key: The key of the value to read.

        Returns:
            The value of the key.

        Raises:
            KeyError: If the key is not in the Json file.
        """
        with open(self.file_path_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        try:
            return data[key]
        except KeyError:
            return "Key not found"

    def write_value(self, key: str, value: str):
        """
        Write a value to a Json file.

        Args:
            key: The key of the value to write.
            value: The value to write.
        """
        with open(self.file_path_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        data[key] = value
        with open(self.file_path_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def write_new_file(self, data: dict):
        """
        Write a new Json file.

        Args:
            data: The data to write.
        """
        with open(self.file_path_name, "w") as file:
            json.dump(data, file, indent=4)

    def delete_value(self, key: str):
        """
        Delete a value from a Json file.

        Args:
            key: The key of the value to delete.
        """
        with open(self.file_path_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        del data[key]
        with open(self.file_path_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

# /////////////////////////////////////////////////////////////////////////////
# Special Config Functions

def get_prefix():
    return JsonHandler("config.json").read_value("prefix")

def statuscon():
    startup_status = JsonHandler("config.json").read_value("startup_status")
    if startup_status == "dnd":
        statuscon = Status.dnd
    elif startup_status == "idle":
        statuscon = Status.idle
    elif startup_status == "invisible" or startup_status == "offline":
        statuscon = Status.offline
    else:
        statuscon = Status.online
    return statuscon

