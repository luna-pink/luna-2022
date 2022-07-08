# pyarmor options: no-spp-mode

##################################################################
#                                                                #
#     CEA-256 Is A Fully Custom Encryption Made By $Exodus       #
#        IF ANY CHANGES ARE MADE MAKE SURE TO CREDIT ME          #
#                                                                #
##################################################################
#
# Discord: $Exodus#4667
# Github: N/A
# Website: https://astro.rest/Encryption
#
##################################################################

################### IMPORTS >>

import os
from queue import Empty
import time
import random
import string
import base64
import binascii
from enum import Enum

################### Data >>

CipherAlphabet = {
    "a": "ü", "ü": "a", "A": "┌", "┌": "A",
    "b": "é", "é": "b", "B": "█", "█": "B",
    "c": "â", "â": "c", "C": "▄", "▄": "C",
    "d": "ä", "ä": "d", "D": "¦", "¦": "D",
    "e": "å", "å": "e", "E": "Ì", "Ì": "E",
    "f": "ç", "ç": "f", "F": "▀", "▀": "F",
    "g": "ê", "ê": "g", "G": "Ó", "Ó": "G",
    "h": "ì", "ì": "h", "H": "ß", "ß": "H",
    "i": "É", "É": "i", "I": "Ô", "Ô": "I",
    "j": "Æ", "Æ": "j", "J": "Ò", "Ò": "J",
    "k": "ö", "ö": "k", "K": "õ", "õ": "K",
    "l": "û", "û": "l", "L": "Õ", "Õ": "L",
    "m": "ò", "ò": "m", "M": "µ", "µ": "M",
    "n": "Ö", "Ö": "n", "N": "þ", "þ": "N",
    "o": "ø", "ø": "o", "O": "Þ", "Þ": "O",
    "p": "×", "×": "p", "P": "È", "È": "P",
    "q": "á", "á": "q", "Q": "ú", "ú": "Q",
    "r": "ƒ", "ƒ": "r", "R": "Ù", "Ù": "R",
    "s": "๏", "๏": "s", "S": "ý", "ý": "S",
    "t": "Ñ", "Ñ": "t", "T": "Ç", "Ç": "T",
    "u": "º", "º": "u", "U": "气", "气": "U",
    "v": "ó", "ó": "v", "V": "Ú", "Ú": "V",
    "w": "ÿ", "ÿ": "w", "W": "๔", "๔": "W",
    "x": "æ", "æ": "x", "X": "¸", "¸": "X",
    "y": "Ä", "Ä": "y", "Y": "©", "©": "Y",
    "z": "ï", "ï": "z", "Z": "÷", "÷": "Z",

    "0": "♤", "♤": "0",  
    "1": "♥", "♥": "1",  
    "2": "♧", "♧": "2",  
    "3": "♛", "♛": "3",  
    "4": "♘", "♘": "4",  
    "5": "♖", "♖": "5",  
    "6": "♟", "♟": "6",  
    "7": "♙", "♙": "7",  
    "8": "♢", "♢": "8",  
    "9": "♗", "♗": "9"
}


################### Classes >>
class Internal:
    def keyconvert(key: str):
        """
        Converts a key to the correct format for the encryption.
        """
        return sum(ord(letter) for letter in key)

    def xor(key: str, data: str):
        """
        XORs a string with a key using specialised algorithm.
        """
        xored_value = [
            chr(ord(data[i]) ^ ord(key[i % len(key)])) for i in range(len(data))
        ]

        return "".join(xored_value)

    def keygen(length: int):
        """
        Generates a key of a given length.
        """
        return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    def letterswap(data: str, cipher: dict):
        """
        Uses the unique cipher alphabet table to swap letters.
        """
        newData = ""
        for letter in data:
            if letter in cipher:
                newData += cipher[letter]
            else:
                newData += letter
        return newData

    def saltgen(length: int, prefix: str):
        """
        Generates a salt of a given length with a prefix.
        """
        return prefix + "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

    def CipherGen(seed: int):
        CipherAlphabetNew = {}
        for letter in string.ascii_uppercase:
            CipherAlphabetNew[letter] = chr(int(ord(letter) + seed * 100))
        for letter in string.ascii_lowercase:
            CipherAlphabetNew[letter] = chr(int(ord(letter) + seed * 100))
        for number in string.digits:
            CipherAlphabetNew[number] = chr(int(ord(number) + seed * 100))
        TempCipher = CipherAlphabetNew.copy()
        for letter in TempCipher.keys():
            CipherAlphabetNew[chr(int(ord(letter) + seed * 100))] = letter
       # print(CipherAlphabetNew)
        return CipherAlphabetNew
        

        

class Mode(Enum):
    """
    Enum for the different Mode of encryption/decryption.
    """
    CDA = 0
    """
    CEA Default Alogrithm
    \nDefault algorithm for CEA.
    """
    CBR = 1
    """
    CEA Block Repeat
    \nRepeats a set block in the algorithm nth amount of times to strengthen the encryption.
    """
    CCS = 2
    """
    CEA Cipher Seed
    \nUses a set seed to create a custom cipher table for the algorithm.
    """
    CCBR = 3
    """
    CEA Cipher Block Repeat
    \nRepeats a set block in the algorithm nth amount of times to strengthen the encryption and uses a set seed to create a custom cipher table for the algorithm.
    """

class Format(Enum):
    """
    Enum for the different format Mode
    """
    BASE64 = 1,
    RAW = 2,

class Cea:
    def __init__(self, key: str, mode: Mode, format: Format, lengthCheck: bool = True, useSalt: bool = False, saltPrefix: str = "$", blockRepeat: int = 1, cipherSeed: int = 1):
        """
        Initialises the class with a key and mode.
        :param key: The key to use for encryption/decryption
        :param mode: The mode to use for encryption/decryption
        :param lengthCheck: Whether or not to check the length of the key (Optional)
        :param prefix: The prefix to use for the salt (Optional)
        :param salt: The salt to use for the salt (Optional)
        :param blockRepeat: The number of times to repeat the block (Optional)
        """
        self.key = key
        self.length = 32
        self.salt = ""
        self.lengthCheck = lengthCheck
        self.saltUsage = useSalt
        self.saltPrefix = saltPrefix
        if self.saltUsage:
            self.salt = Internal.saltgen(length=10, prefix=saltPrefix)
        self.blockRepeat = blockRepeat
        self.cipherSeed = cipherSeed
        self.mode = mode
        self.encrypt = Empty
        self.decrypt = Empty
        self.cipherSpec = Empty
        self.formatEncrypt = Empty
        self.formatDecrypt = Empty
        if format == Format.BASE64:
            self.formatEncrypt = lambda x: base64.b64encode(x.encode())
            self.formatDecrypt = lambda x: base64.b64decode(x).decode()
        if format == Format.RAW:
            self.formatEncrypt = lambda x: x
            self.formatDecrypt = lambda x: x
        match mode:
            case Mode.CBR:
                self.encrypt = self.__cbr_encrypt
                self.decrypt = self.__cbr_decrypt
                pass
            case Mode.CCS:
                self.cipherSpec = Internal.CipherGen(self.cipherSeed)
                self.encrypt = self.__ccs_encrypt
                self.decrypt = self.__ccs_decrypt
            case Mode.CCBR:
                #self.encrypt = self.__ccbr_encrypt
                pass
            case Mode.CDA:
                self.encrypt = self.__cda_encrypt
                self.decrypt = self.__cda_decrypt

####### Encryptions >>
    def __cda_encrypt(self, plainText: str):
        """
        Encrypts a plain text string.
        :param plainText: The plain text to encrypt
        :return: The encrypted text
        """
        if not plainText:
            return "Error: No data provided"
        if self.lengthCheck and len(self.key) != self.length:
            return "Error: Key is not the correct length"

        key_value = Internal.keyconvert(self.key)
        encrypted_text = "".join(
            chr(int((ord(letter) + (key_value % 2560))))
            for letter in Internal.letterswap(plainText, CipherAlphabet)
        )
        encrypted_text = Internal.xor(self.key, Internal.letterswap(encrypted_text[:round(len(encrypted_text) / 2)] + self.salt + encrypted_text[round(len(encrypted_text) / 2):], CipherAlphabet))
        return self.formatEncrypt(encrypted_text)

    def __ccs_encrypt(self, plainText: str):
        """
        Encrypts a plain text string.
        :param plainText: The plain text to encrypt
        :return: The encrypted text
        """
        if not plainText:
            return "Error: No data provided"
        if self.lengthCheck and len(self.key) != self.length:
            return "Error: Key is not the correct length"

        key_value = Internal.keyconvert(self.key)
        encrypted_text = "".join(
            chr(int((ord(letter) + (key_value % 2560))))
            for letter in Internal.letterswap(plainText, self.cipherSpec)
        )
        encrypted_text = Internal.xor(self.key, Internal.letterswap(encrypted_text[:round(len(encrypted_text) / 2)] + self.salt + encrypted_text[round(len(encrypted_text) / 2):], self.cipherSpec))
        return self.formatEncrypt(encrypted_text)

    def __cbr_encrypt(self, plainText: str):
        """
        Encrypts a plain text string.
        :param plainText: The plain text to encrypt
        :return: The encrypted text
        """
        if not plainText:
            return "Error: No data provided"
        if self.lengthCheck and len(self.key) != self.length:
            return "Error: Key is not the correct length"

        key_value = Internal.keyconvert(self.key)
        encrypted_text = [
            chr(int((ord(letter) + (key_value % 2560))))
            for letter in Internal.letterswap(plainText, CipherAlphabet)
        ]
        
        for i in range(self.blockRepeat):
            for i in range(len(encrypted_text)):
                encrypted_text[i] = chr(int((ord(str(encrypted_text[i])) + (key_value % 2560))))
        encrypted_text = "".join(encrypted_text)   

        encrypted_text = Internal.xor(self.key, Internal.letterswap(encrypted_text[:round(len(encrypted_text) / 2)] + self.salt + encrypted_text[round(len(encrypted_text) / 2):], CipherAlphabet))
        return self.formatEncrypt(encrypted_text)
####### End of Encryptions >>
####### Decryptions >>
    def SaltClean(self, data: str):
        """
        Cleans the salt from the data.
        :param data: The data to clean
        :return: The cleaned data
        """
        try:
            salt = data.split(self.saltPrefix)[1][:10]
            return data.replace(self.saltPrefix + salt, "")
        except:
            return data
        
    def __cda_decrypt(self, encrypted_text: str):
        """
        Decrypts an encrypted text string.
        :param encrypted_text: The encrypted text to decrypt
        :return: The decrypted text
        """
        if not encrypted_text:
            return "Error: No data provided"
        if self.lengthCheck and len(self.key) != self.length:
            return "Error: Key is not the correct length"

        key_value = Internal.keyconvert(self.key)
        encrypted_text = self.SaltClean(Internal.xor(self.key, self.formatDecrypt(encrypted_text)))

        decrypted_text = "".join(
            chr(int((ord(letter) - (key_value % 2560)))) for letter in encrypted_text
        )
        decrypted_text = Internal.letterswap(decrypted_text, CipherAlphabet)
        return decrypted_text

    def __ccs_decrypt(self, encrypted_text: str):
        """
        Decrypts an encrypted text string.
        :param encrypted_text: The encrypted text to decrypt
        :return: The decrypted text
        """
        if not encrypted_text:
            return "Error: No data provided"
        if self.lengthCheck and len(self.key) != self.length:
            return "Error: Key is not the correct length"

        key_value = Internal.keyconvert(self.key)
        encrypted_text = self.SaltClean(Internal.xor(self.key, self.formatDecrypt(encrypted_text)))

        decrypted_text = "".join(
            chr(int((ord(letter) - (key_value % 2560)))) for letter in encrypted_text
        )
        decrypted_text = Internal.letterswap(decrypted_text, self.cipherSpec)
        return decrypted_text

    def __cbr_decrypt(self, encrypted_text: str):
        """
        Decrypts an encrypted text string.
        :param encrypted_text: The encrypted text to decrypt
        :return: The decrypted text
        """
        if not encrypted_text:
            return "Error: No data provided"
        if self.lengthCheck and len(self.key) != self.length:
            return "Error: Key is not the correct length"

        key_value = Internal.keyconvert(self.key)
        encrypted_text_temp = self.SaltClean(Internal.xor(self.key, self.formatDecrypt(encrypted_text)))
        encrypted_text = []
        encrypted_text[:0] = encrypted_text_temp
        for i in range(self.blockRepeat):
            for i in range(len(encrypted_text)):
                #print(encrypted_text[i])
                encrypted_text[i] = chr(int((ord(str(encrypted_text[i])) - (key_value % 2560))))

        decrypted_text = "".join(
            chr(int((ord(letter) - (key_value % 2560)))) for letter in encrypted_text
        )
        decrypted_text = Internal.letterswap(decrypted_text, CipherAlphabet)
        return decrypted_text

####### End of Decryptions >>

if __name__ == "__main__":
    pass

