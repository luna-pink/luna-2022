import variables
import os

# def get_prefix():
#     prefix = variables.default_prefix
#     return prefix


"""
Create a Class that has functions for handling files and folders, such as reading a value, overwriting a file, creating a file or folder as well as deleting.

run a check in the __init__ if the file exists, if not, create it before writing to it.
run a check if the folder exists, if not, create it.
"""


class FileHandler:

    def __init__(self, file_name: str, file_path: str = "./"):
        """
        Initialize the FileHandler class.
        Does a check if the file exists, if not creates it, before writing to it.

        Args:
            file_name: The name of the file.
            file_path: The path to the file.
        """
        if "Luna" in file_path:
            file_path = os.path.expanduser("~/Documents/Luna")
        self.file_name = file_name
        self.file_path = file_path
        self.file_path_full = file_path + file_name
        self.file_path_full_read = file_path + file_name

    def check_file_exists(self):
        """
        Checks if the file exists.

        Returns:
            True if the file exists, False if not.
        """
        if os.path.isfile(self.file_path_full):
            return True
        else:
            return False

    def check_folder_exists(self):
        """
        Checks if the folder exists.

        Returns:
            True if the folder exists, False if not.
        """
        if os.path.isdir(self.file_path):
            return True
        else:
            return False

    def create_file(self):
        """
        Creates a file.

        Returns:
            True if the file was created, False if not.
        """
        if not self.check_file_exists():
            with open(self.file_path_full, 'w+') as f:
                f.write('')
                f.close()
                return True
        else:
            return False

    def create_folder(self):
        """
        Creates a folder.

        Returns:
            True if the folder was created, False if not.
        """
        if not self.check_folder_exists():
            os.mkdir(self.file_path)
            return True
        else:
            return False

    def read_file(self):
        """
        Reads the file.

        Returns:
            The data in the file.
        """
        if self.check_file_exists():
            with open(self.file_path_full_read, 'r') as f:
                return f.read()
        else:
            return False

    def write_file(self, data):
        """
        Writes to the file.

        Args:
            data: The data to write to the file.

        Returns:
            True if the file was written, False if not.
        """
        if self.check_file_exists():
            with open(self.file_path_full, 'w') as f:
                f.write(data)
                f.close()
                return True
        else:
            return False

    def delete_file(self):
        """
        Deletes the file.

        Returns:
            True if the file was deleted, False if not.
        """
        if self.check_file_exists():
            os.remove(self.file_path_full)
            return True
        else:
            return False

    def delete_folder(self):
        """
        Deletes the folder.

        Returns:
            True if the folder was deleted, False if not.
        """
        if self.check_folder_exists():
            os.rmdir(self.file_path)
            return True
        else:
            return False
