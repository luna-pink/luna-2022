import os
import json

# ///////////////////////////////////////////////////////////////
# File Functions

class files:
    def documents():
        return os.path.expanduser("~/Documents")

    def file_exist(file_name: str, documents=False):
        """Checks if a file exists"""
        if documents:
            return os.path.exists(os.path.join(files.documents(), file_name))
        else:
            return os.path.exists(file_name)

    def write_file(path: str, content, documents=False, byte=False, append=False):
        """Writes a file"""
        if documents and byte:
            with open(os.path.join(files.documents(), path), "wb") as f:
                f.write(content)
        elif documents:
            mode = "a" if append else "w"
            with open(os.path.join(files.documents(), path), mode) as f:
                f.write(content)
        else:
            with open(path, 'wb') as f:
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
        elif not os.path.exists(path):
            os.makedirs(path)

    def json(file_name: str, value: str, documents=False):
        """Reads a json file"""
        if documents:
            return json.load(
                open(
                    os.path.join(
                        files.documents(),
                        file_name),
                    encoding="utf-8"))[value]
        else:
            return json.load(open(file_name, encoding="utf-8"))[value]

    def remove(path: str, documents=False):
        """Removes a file"""
        try:
            if documents:
                if os.path.exists(os.path.join(files.documents(), path)):
                    os.remove(os.path.join(files.documents(), path))
            elif os.path.exists(path):
                os.remove(path)
        except BaseException:
            pass