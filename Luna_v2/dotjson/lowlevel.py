import json

from .loader import *


def get_list():
    """
    It returns the list of keys

    :return: The list of keys
    """
    return keys


def get_key(key):
    """
    It returns the value of the key in the dictionary, if the key is in the dictionary, otherwise it raises a KeyError

    :param key: The key to search for
    :return: The value of the key in the dictionary.
    """
    for i in keys:
        if key in i:
            return i[key]
    load_backup()
    for i in keys:
        if key in i:
            return i[key]
    raise KeyError('Key not found')


def write_key(key, value):
    """
    It takes a key and a value, and then it writes the value to the key in the file

    :param key: The key you want to change
    :param value: The value to write to the key
    :return: The value of the key
    """
    for i in keys:
        if key in i:
            i[key] = value
            with open(i['file'], 'w') as f:
                file = i['file']
                del i['file']
                json.dump(i, f, indent=4)
                keys[keys.index(i)]['file'] = file
            return
    load_backup()
    for i in keys:
        if key in i:
            i[key] = value
            with open(i['file'], 'w') as f:
                file = i['file']
                del i['file']
                json.dump(i, f, indent=4)
                keys[keys.index(i)]['file'] = file
            return
    raise KeyError('Key not found')


def write_new(key, value, file):
    """
    It takes a key, value, and file name, and writes the key and value to the file

    :param key: The key you want to add to the json file
    :param value: The value you want to write to the file
    :param file: The file you want to write to
    :return: The value of the key in the file.
    """
    for i in keys:
        if file in i['file']:
            i[key] = value
            with open(i['file'], 'w') as f:
                file = i['file']
                del i['file']
                json.dump(i, f, indent=4)
                keys[keys.index(i)]['file'] = file
            return
    load_backup()
    for i in keys:
        if file in i['file']:
            i[key] = value
            with open(i['file'], 'w') as f:
                file = i['file']
                del i['file']
                json.dump(i, f, indent=4)
                keys[keys.index(i)]['file'] = file
            return
    with open(f'{file}', 'w') as f:
        json.dump({key: value}, f, indent=4)
    keys.append({key: value, 'file': f'{file}'})


def remove_key(key):
    """
    It takes a key and removes it from the dictionary

    :param key: The key you want to remove
    :return: The value of the key in the dictionary.
    """
    for i in keys:
        if key in i:
            value = i[key]
            del i[key]
            with open(i['file'], 'w') as f:
                file = i['file']
                del i['file']
                json.dump(i, f, indent=4)
                keys[keys.index(i)]['file'] = file
                print(keys)
            return value
    load_backup()
    for i in keys:
        if key in i:
            value = i[key]
            del i[key]
            with open(i['file'], 'w') as f:
                file = i['file']
                del i['file']
                json.dump(i, f, indent=4)
                keys[keys.index(i)]['file'] = file
                print(keys)
            return value
    raise KeyError('Key not found')
