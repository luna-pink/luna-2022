import string
import random
import base64

###
# CEAShim LTS (Long Term Support)
# This version of CEA is designed to be a Fork of the original CEA that only receives updates when the server receives a CEA update.
# Do not update this file as the server will not accept it as a valid cipher hash. (This feature is not yet implemented)
# For all other purposes not pertaining to authentication via the AtlasProviderAPI, please use the original CEA.
###

class CEAMisc:
    def GetShimVersion():
        """
        The function that returns the version of the shim.
        This is used to determine if the shim is compatible with the current implementation that is built into the Atlas Gateway Server.
        """
        return "AtlasProviderAPI-CEA-SHIM - 1.0.0"

    def GenerateKey():
        characters = string.ascii_letters + string.digits
        generate_string = "".join(random.sample(characters, 32))
        return generate_string

    def XOR(ptext, key):
        xored = []
        for x in range(len(ptext)):
            xored.append(chr(ord(ptext[x]) ^ ord(key[x % len(key)])))

        return "".join(xored)

    def CipherEncode(plaintext):
        normal_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        normal_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "u", "v", "x", "y", "z"]
        normal_caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                       "U", "V", "X", "Y", "Z"]
        ciphered_low = ["c", "e", "a", "b", "i", "f", "d", "h", "g", "n", "l", "k", "q", "j", "r", "p", "o", "m", "u",
                        "s", "y", "x", "v", "z"]
        ciphered_caps = ["C", "E", "A", "B", "I", "F", "D", "H", "G", "N", "L", "K", "Q", "J", "R", "P", "O", "M", "U",
                         "S", "Y", "X", "V", "Z"]
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
        normal_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "u", "v", "x", "y", "z"]
        normal_caps = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                       "U", "V", "X", "Y", "Z"]
        ciphered_low = ["c", "e", "a", "b", "i", "f", "d", "h", "g", "n", "l", "k", "q", "j", "r", "p", "o", "m", "u",
                        "s", "y", "x", "v", "z"]
        ciphered_caps = ["C", "E", "A", "B", "I", "F", "D", "H", "G", "N", "L", "K", "Q", "J", "R", "P", "O", "M", "U",
                         "S", "Y", "X", "V", "Z"]
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


class CEAEncrypt:
    def __init__(self, key=CEAMisc.GenerateKey(), encoding=1):
        self.key = key
        self.encoding = encoding

    def CEA256(self, plain_text):

        # VARIABLES >>

        key_value = 0
        temp_value = 0
        cipher_encoded = CEAMisc.CipherEncode(plain_text)
        temp_data = ""
        semi_encryption = []
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
            semi_encryption.append(f"{CEAMisc.XOR(str(x), self.key)}:")

        temp_data = "".join(semi_encryption)
        length = len(temp_data) - 1
        first_part = temp_data[:length]
        second_part = temp_data[length + 1:]
        temp_data = first_part + second_part

        return base64.b64encode(f"{temp_data}".encode()).decode()


class CEADecrypt:
    def __init__(self, key, encoding=1):
        self.key = key
        self.encoding = encoding

    def CEA256(self, encoded_text):

        # VARIABLES >>

        key_value = 0
        splits = 0
        cipher_encoded = base64.b64decode(encoded_text).decode()
        split_data = []
        key_decimals = []
        plain_decimals = []
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
                int(f"{CEAMisc.XOR(cipher_encoded.split(':')[x], self.key)}"))

        for x in range(len(self.key)):
            key_decimals.append(ord(self.key[x]))

        for x in key_decimals:
            temp_value = key_value
            key_value = temp_value + x

        for x in split_data:
            plain_decimals.append(int(x / key_value))

        for x in plain_decimals:
            decrypted_text_one.append(chr(x))

        decrypted_data = CEAMisc.CipherDecode("".join(decrypted_text_one))

        return decrypted_data