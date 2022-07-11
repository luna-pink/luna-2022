# pyarmor options: no-spp-mode

import contextlib
import os
import json


# ///////////////////////////////////////////////////////////////
# File Functions

class files:
    def documents():
        """
        It returns the path to the Documents' folder in the user's home directory
        :return: The path to the Documents' folder in the user's home directory.
        """
        return os.path.expanduser("~/Documents")

    def file_exist(self, documents=False):
        """
        It checks if a file exists in the documents folder or not

        :param documents: If True, the file will be searched for in the documents' folder, defaults to False (optional)
        :return: The file_exist method is being returned.
        """
        if documents:
            return os.path.exists(os.path.join(files.documents(), self))
        else:
            return os.path.exists(self)

    def write_file(self, content, documents=False, byte=False, append=False):
        """
        It writes a file.

        :param content: The content to write to the file
        :param documents: If True, the file will be written to the documents' folder, defaults to False (optional)
        :param byte: If the file is a byte file, set this to True, defaults to False (optional)
        :param append: If you want to append to the file, set this to True, defaults to False (optional)
        """
        if documents and byte:
            with open(os.path.join(files.documents(), self), "wb") as f:
                f.write(content)
        elif documents:
            mode = "a" if append else "w"
            with open(os.path.join(files.documents(), self), mode) as f:
                f.write(content)
        elif byte:
            with open(self, 'wb') as f:
                f.write(content)
        else:
            with open(self, 'w') as f:
                f.write(content)

    def write_json(self, content, documents=False):
        """
        It writes a json file to the documents folder

        :param content: The content to write to the file
        :param documents: If True, the file will be saved in the documents' folder, defaults to False (optional)
        """
        if documents:
            with open(os.path.join(files.documents(), self), "w") as f:
                f.write(json.dumps(content, indent=4))
        else:
            with open(self, "w") as f:
                f.write(json.dumps(content, indent=4))

    def read_file(self, documents=False):
        """
        It opens a file, reads it, and returns the contents of the file

        :param documents: If True, the file will be read from the documents' folder, defaults to False (optional)
        :return: The read() method returns the specified number of bytes from the file.
        """
        if documents:
            with open(os.path.join(files.documents(), self), 'r', encoding="utf-8") as f:
                return f.read()
        else:
            with open(self, 'r', encoding="utf-8") as f:
                return f.read()

    def append_file(self, content):
        """
        Append the content to the file.

        :param content: The content to be written to the file
        """
        with open(self, 'a') as f:
            f.write(content)

    def delete_file(self, documents=False):
        """
        It deletes a file

        :param documents: If True, the file will be deleted from the documents' folder. If False, the file will be deleted from the current directory, defaults to False (optional)
        """
        if documents:
            os.remove(os.path.join(files.documents(), self))
        else:
            os.remove(self)

    def create_folder(self, documents=False):
        """
        If the folder doesn't exist, create it

        :param documents: If True, the folder will be created in the documents' folder, defaults to False (optional)
        """
        if documents:
            if not os.path.exists(os.path.join(files.documents(), self)):
                os.makedirs(os.path.join(files.documents(), self))
        elif not os.path.exists(self):
            os.makedirs(self)

    def json(self, value: str, documents=False):
        """
        It returns a value from a JSON file

        :param value: The value you want to get from the json file
        :type value: str
        :param documents: If you want to get a value from a json file in the documents' folder, set this to True, defaults to False (optional)
        :return: The value of the key in the json file.
        """
        if documents:
            return json.load(open(os.path.join(files.documents(), self), encoding="utf-8"))[value]

        else:
            return json.load(open(self, encoding="utf-8"))[value]

    def remove(self, documents=False):
        """
        It removes a file

        :param documents: If True, the file will be removed from the documents' folder, defaults to False (optional)
        """
        with contextlib.suppress(BaseException):
            if documents:
                if os.path.exists(os.path.join(files.documents(), self)):
                    os.remove(os.path.join(files.documents(), self))
            elif os.path.exists(self):
                os.remove(self)
