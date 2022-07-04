# pyarmor options: no-spp-mode

# ///////////////////////////////////////////////////////////////
# Changed CEA256

import random
import string
import base64

class Misc:
    def GenerateKey():
        """
        Generate a random string of 32 characters
        :return: a string of 32 random characters from the string.ascii_letters and string.digits.
        """
        characters = string.ascii_letters + string.digits
        generate_string = "".join(random.sample(characters, 32))
        return generate_string

    def XOR(ptext, key):
        """
        XOR the given plaintext with the given key, character by character

        :param ptext: The text to be encrypted
        :param key: The key is the same length as the plaintext message, and it is used to encrypt the plaintext
        :return: The XOR'd string.
        """
        xored = []
        for x in range(len(ptext)):
            xored.append(chr(ord(ptext[x]) ^ ord(key[x % len(key)])))

        return "".join(xored)

    def CipherEncode(plaintext):
        """
        It takes a string as input, and returns a string as output

        :param plaintext: The text you want to encode
        :return: a string of the encoded text.
        """
        normal_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        normal_low = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "u",
            "v",
            "x",
            "y",
            "z"]
        normal_caps = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "U",
            "V",
            "X",
            "Y",
            "Z"]
        ciphered_low = [
            "c",
            "e",
            "a",
            "b",
            "i",
            "f",
            "d",
            "h",
            "g",
            "n",
            "l",
            "k",
            "q",
            "j",
            "r",
            "p",
            "o",
            "m",
            "u",
            "s",
            "y",
            "x",
            "v",
            "z"]
        ciphered_caps = [
            "C",
            "E",
            "A",
            "B",
            "I",
            "F",
            "D",
            "H",
            "G",
            "N",
            "L",
            "K",
            "Q",
            "J",
            "R",
            "P",
            "O",
            "M",
            "U",
            "S",
            "Y",
            "X",
            "V",
            "Z"]
        ciphered_numbers = ["0", "5", "3", "2", "8", "1", "9", "7", "4", "6"]
        text_length = len(plaintext)
        encoded_text = []

        for x in range(text_length):
            if plaintext[x] in normal_low:
                index = normal_low.index(plaintext[x])
                ciphered_letter = ciphered_low[index]
                encoded_text.append(ciphered_letter)
            elif plaintext[x] in normal_caps:
                index = normal_caps.index(plaintext[x])
                ciphered_letter = ciphered_caps[index]
                encoded_text.append(ciphered_letter)
            elif plaintext[x] in normal_numbers:
                index = normal_numbers.index(plaintext[x])
                ciphered_letter = ciphered_numbers[index]
                encoded_text.append(ciphered_letter)
            else:
                encoded_text.append(plaintext[x])

        return "".join(encoded_text)

    def CipherDecode(encodedtext):
        normal_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        normal_low = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "u",
            "v",
            "x",
            "y",
            "z"]
        normal_caps = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "U",
            "V",
            "X",
            "Y",
            "Z"]
        ciphered_low = [
            "c",
            "e",
            "a",
            "b",
            "i",
            "f",
            "d",
            "h",
            "g",
            "n",
            "l",
            "k",
            "q",
            "j",
            "r",
            "p",
            "o",
            "m",
            "u",
            "s",
            "y",
            "x",
            "v",
            "z"]
        ciphered_caps = [
            "C",
            "E",
            "A",
            "B",
            "I",
            "F",
            "D",
            "H",
            "G",
            "N",
            "L",
            "K",
            "Q",
            "J",
            "R",
            "P",
            "O",
            "M",
            "U",
            "S",
            "Y",
            "X",
            "V",
            "Z"]
        ciphered_numbers = ["0", "5", "3", "2", "8", "1", "9", "7", "4", "6"]
        text_length = len(encodedtext)
        plain_text = []

        for x in range(text_length):
            if encodedtext[x] in ciphered_low:
                index = ciphered_low.index(encodedtext[x])
                normal_letter = normal_low[index]
                plain_text.append(normal_letter)
            elif encodedtext[x] in ciphered_caps:
                index = ciphered_caps.index(encodedtext[x])
                normal_letter = normal_caps[index]
                plain_text.append(normal_letter)
            elif encodedtext[x] in ciphered_numbers:
                index = ciphered_numbers.index(encodedtext[x])
                normal_letter = normal_numbers[index]
                plain_text.append(normal_letter)
            else:
                plain_text.append(encodedtext[x])

        return "".join(plain_text)


class Encryption:
    def __init__(self, key=Misc.GenerateKey(), encoding=1):
        """
        The constructor for the class

        :param key: The key used to encrypt the message
        :param encoding: 1 = ASCII, 2 = Unicode, defaults to 1 (optional)
        """
        self.key = key
        self.encoding = encoding

    def CEA256(self, plain_text):
        """
        The function takes in a plain text and a key and encrypts the plain text using the key

        :param plain_text: The text you want to encrypt
        :return: The cipher text.
        """

        # VARIABLES >>

        key_value = 0
        temp_value = 0
        cipher_encoded = Misc.CipherEncode(plain_text)
        temp_data = ""
        semi_encryption = []
        final_dencryption = []
        key_decimals = []
        plain_decimals = []
        encrypted_decimals = []

        # FUNCTIONS >>

        if len(self.key) != 32:
            return "InvalidKeyLength"

        for x in range(len(cipher_encoded)):  # Plain Text Conversion
            letter = cipher_encoded[x]
            plain_decimals.append(ord(letter))

        for x in range(len(self.key)):  # Key Conversion
            letter = self.key[x]
            key_decimals.append(ord(letter))

        for x in key_decimals:
            temp_value = key_value
            key_value = temp_value + x

        for x in plain_decimals:
            encrypted_decimals.append(x * key_value)

        for x in encrypted_decimals:
            semi_encryption.append(f"{Misc.XOR(str(x), self.key)}:")

        temp_data = "".join(semi_encryption)
        length = len(temp_data) - 1
        first_part = temp_data[:length]
        second_part = temp_data[length + 1:]
        temp_data = first_part + second_part

        return base64.b64encode(f"{temp_data}".encode()).decode()


class Decryption:
    def __init__(self, key, encoding=1):
        """
        The __init__ function is called when an instance of the class is created.

        :param key: The key is the key that will be used to encrypt and decrypt the message
        :param encoding: 1 = ASCII, 2 = Unicode, defaults to 1 (optional)
        """
        self.key = key
        self.encoding = encoding

    def CEA256(self, encoded_text):
        """
        The function takes in a string, splits it into a list, and then decrypts it

        :param encoded_text: The text to be decrypted
        :return: The decrypted data.
        """

        # VARIABLES >>

        key_value = 0
        tmep_value = 0
        splits = 0
        cipher_encoded = base64.b64decode(encoded_text).decode()
        temp_data = ""
        split_data = []
        key_decimals = []
        plain_decimals = []
        encrypted_decimals = []
        decrypted_text_one = []
        decrypted_data = ""

        # FUNCTIONS >>

        for x in range(len(cipher_encoded)):
            character = cipher_encoded[x]
            if character == ":":
                splits += 1
            else:
                pass

        splits += 1

        for x in range(splits):
            split_data.append(
                int(f"{Misc.XOR(cipher_encoded.split(':')[x], self.key)}"))

        for x in range(len(self.key)):
            key_decimals.append(ord(self.key[x]))

        for x in key_decimals:
            temp_value = key_value
            key_value = temp_value + x

        for x in split_data:
            plain_decimals.append(int(x / key_value))

        for x in plain_decimals:
            decrypted_text_one.append(chr(x))

        decrypted_data = Misc.CipherDecode("".join(decrypted_text_one))

        return decrypted_data