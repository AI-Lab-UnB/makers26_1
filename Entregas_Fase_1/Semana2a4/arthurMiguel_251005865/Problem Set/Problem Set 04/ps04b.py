import random

class Message(object):
    def __init__(self, input_text):
        self.message_text = input_text

    def get_text(self):
        return self.message_text

    def shift_char(self, char, shift):
        ascii_val = ord(char)
        if 32 <= ascii_val <= 126:
            return chr(((ascii_val - 32 + shift) % 95) + 32)
        return char

    def apply_pad(self, pad):
        result = ""
        for i in range(len(self.message_text)):
            result += self.shift_char(self.message_text[i], pad[i])
        return result

class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        super().__init__(input_text)
        if pad is None:
            self.pad = self.generate_pad()
        else:
            self.pad = pad.copy()

    def generate_pad(self):
        return [random.randint(0, 109) for _ in range(len(self.message_text))]

    def get_pad(self):
        return self.pad.copy()

    def get_ciphertext(self):
        return self.apply_pad(self.pad)

    def change_pad(self, new_pad):
        self.pad = new_pad.copy()

class EncryptedMessage(Message):
    def __init__(self, input_text):
        super().__init__(input_text)

    def decrypt_message(self, pad):
        decrypted_pad = [-p for p in pad]
        return self.apply_pad(decrypted_pad)