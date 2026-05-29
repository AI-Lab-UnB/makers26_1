import random

# CLASSE BASE: Message

class Message:
    def __init__(self, input_text):
        self.message_text = input_text

    def get_text(self):
        return self.message_text

    def shift_char(self, char, shift):
        ascii_val = ord(char)
        shifted = (ascii_val - 32 + shift) % 95 + 32
        return chr(shifted)

    def apply_pad(self, pad):
        result = ""
        for i, char in enumerate(self.message_text):
            result += self.shift_char(char, pad[i])
        return result

    def __repr__(self):
        return f"Message('{self.message_text}')"


# CLASSE FILHA

class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        super().__init__(input_text)
        if pad is None:
            self.pad = self.generate_pad()
        else:
            self.pad = pad[:]  

    def generate_pad(self):
        # gera um pad aleatório com valores entre 0 e 109
        return [random.randint(0, 109) for _ in self.message_text]

    def get_pad(self):
        return self.pad[:] 

    def get_ciphertext(self):
        return self.apply_pad(self.pad)

    def change_pad(self, new_pad):
        self.pad = new_pad[:]
        
    def __repr__(self):
        return f"PlaintextMessage('{self.message_text}', pad={self.pad})"


# CLASSE FILHA: 

class EncryptedMessage(Message):
    def __init__(self, input_text):
        super().__init__(input_text)

    def decrypt_message(self, pad):
        negative_pad = [-shift for shift in pad]
        return self.apply_pad(negative_pad)

    def __repr__(self):
        return f"EncryptedMessage('{self.message_text}')"


msg = Message("hello")
print(msg.shift_char('A', 5))   # F
print(msg.shift_char('a', 10))  # k
print(msg.shift_char(' ', -1))  # ~

# teste apply_pad
msg2 = Message("hello")
print(msg2.apply_pad([3, 0, 10, 11, 4]))  # kevws

# teste PlaintextMessage
p = PlaintextMessage("Hello!", [5, 10, 2, 3, 0, 2])
print(p.get_ciphertext())  # Monoo#

# teste EncryptedMessage
e = EncryptedMessage("Monoo#")
print(e.decrypt_message([5, 10, 2, 3, 0, 2]))  # Hello!