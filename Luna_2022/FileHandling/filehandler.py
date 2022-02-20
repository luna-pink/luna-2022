import os
import json

class FileHandler:
    """
    This class handles the file operations.
    """
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
        
# /////////////////////////////////////////////////////////////////////////////
# Deprecated
# TODO: Must change all of luna's functions to the new FileHandler and JsonHandler by mid 2022.

class files:
    def documents():
        return os.path.expanduser("~/Documents")

    def file_exist(file_name: str, documents=False):
        """Checks if a file exists"""
        if documents:
            return os.path.exists(os.path.join(files.documents(), file_name))
        else:
            return os.path.exists(file_name)

    def write_file(path: str, content, documents=False, byte=False):
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

    def write_json(path: str, content, documents=False):
        """Writes a json file"""
        if documents:
            with open(os.path.join(files.documents(), path), "w") as f:
                f.write(json.dumps(content, indent=4))
        else:
            with open(path, "w") as f:
                f.write(json.dumps(content, indent=4))

    def read_file(path: str, documents=False):
        """Reads a file"""
        if documents:
            with open(os.path.join(files.documents(), path), 'r', encoding="utf-8") as f:
                return f.read()
        else:
            with open(path, 'r', encoding="utf-8") as f:
                return f.read()

    def append_file(path: str, content):
        """Appends to a file"""
        with open(path, 'a') as f:
            f.write(content)

    def delete_file(path: str, documents=False):
        """Deletes a file"""
        if documents:
            os.remove(os.path.join(files.documents(), path))
        else:
            os.remove(path)

    def create_folder(path: str, documents=False):
        """Creates a folder"""
        if documents:
            if not os.path.exists(os.path.join(files.documents(), path)):
                os.makedirs(os.path.join(files.documents(), path))
        else:
            if not os.path.exists(path):
                os.makedirs(path)

    def json(file_name: str, value: str, documents=False):
        """Reads a json file"""
        if documents:
            return json.load(open(os.path.join(files.documents(), file_name), encoding="utf-8"))[value]
        else:
            return json.load(open(file_name, encoding="utf-8"))[value]

    def remove(path: str, documents=False):
        """Removes a file"""
        if documents:
            if os.path.exists(os.path.join(files.documents(), path)):
                os.remove(os.path.join(files.documents(), path))
        else:
            if os.path.exists(path):
                os.remove(path)