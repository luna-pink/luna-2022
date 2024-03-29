import os
import json

keys = []
backup_paths = []


def clear_keys():
    keys.clear()
    return keys


def load_keys(folder: list):
    """
    It takes a list of folders, and for each folder, it looks for a file ending in .json, and if it finds one, it loads it into a list called keys

    :param folder: list - a list of folders to search for keys in
    :type folder: list
    :return: A list of dictionaries.
    """
    clear_keys()
    for i in folder:
        for file in os.listdir(i):
            if file.endswith('.json'):
                with open(f'{i}/{file}') as f:
                    keys.append(json.load(f))
                    keys[-1]['file'] = f'{i}/{file}'
    return keys


def backup_path(folder: list):
    backup_paths.append(folder)
    return backup_paths


def load_backup():
    clear_keys()
    for i in backup_paths:
        for file in os.listdir(i):
            if file.endswith('.json'):
                with open(f'{i}/{file}') as f:
                    keys.append(json.load(f))
                    keys[-1]['file'] = f'{i}/{file}'
    return keys
