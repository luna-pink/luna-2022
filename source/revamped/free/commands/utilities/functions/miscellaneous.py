import random
import string


def zalgoText(string):
    result = ''

    for char in string:
        for _ in range(random.randint(20, 40)):
            rand_bytes = random.randint(0x300, 0x36f).to_bytes(2, 'big')
            char += rand_bytes.decode('utf-16be')
        result += char
    return result


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def Randprntsc():
    """
    Random print screen.
    """
    letterprn = ''.join(random.choices(string.ascii_lowercase, k=4))
    numberprn = random.randint(10, 99)
    return f'https://prnt.sc/{numberprn}{letterprn}'


def get_size(_bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if _bytes < factor:
            return f"{_bytes:.2f}{unit}{suffix}"
        _bytes /= factor
