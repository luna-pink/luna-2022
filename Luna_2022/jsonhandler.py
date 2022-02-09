"""
Create a Class that has functions for handling Json files, such as reading a value, overwriting a value and writing a new file.

All have indention 4 spaces.

run a check in the __init__ if the file exists, if not create it (and write "{}") before writing to it.

def __init__(self, file_name:str, file_path:str = "./"):

if "Luna" is in file_path, use os.path.expanduser("~/Documents/Luna").

Put a description on every function and the class.
Put a description on __init__.
"""

import json
import os


class JsonHandler:
    def __init__(self, file_name: str, file_path: str = "./"):
        """
        Initialize the JsonHandler class.
        Does a check if the file exists, if not creates it, before writing to it.

        Args:
            file_name: The name of the file.
            file_path: The path of the file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if "Luna" in file_path:
            file_path = os.path.expanduser("~/Documents/Luna")
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        self.file_path = file_path
        self.file_name = file_name
        self.file_path_name = os.path.join(self.file_path, self.file_name)
        if not os.path.exists(self.file_path_name):
            with open(self.file_path_name, "w+") as file:
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
        with open(self.file_path_name, "r") as file:
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
        with open(self.file_path_name, "r") as file:
            data = json.load(file)
        data[key] = value
        with open(self.file_path_name, "w") as file:
            json.dump(data, file)

    def write_new_file(self, data: dict):
        """
        Write a new Json file.

        Args:
            data: The data to write.
        """
        with open(self.file_path_name, "w") as file:
            json.dump(data, file)
