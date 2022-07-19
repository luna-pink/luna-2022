from dotjson import load_keys, get_key, write_key, write_new, remove_key


def load_luna():
    load_keys(['data', 'data/sniper'])
    get_key('test2')
    write_key('test2', 'This is test2')
    write_new('test4', 'I am a new value', 'test.json')
    remove_key('test4')


if __name__ == '__main__':
    load_luna()
