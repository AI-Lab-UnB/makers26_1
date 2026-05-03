import random


class Message(object):
    def __init__(self, input_text):
        self.text = input_text

    def __repr__(self):
        return f'''Message('{self.get_text()}')'''

    def get_text(self):
        return self.text 

    def shift_char(self, char, shift):
        original_pos = ord(char)
        
        pos_zero = original_pos - 32
        
        new_pos = (pos_zero + shift) % 95
        return chr(new_pos + 32)

    def apply_pad(self, pad):
        chiper_list = []
        for i in range(len(self.text)):
            chiper_list.append(self.shift_char(self.text[i], pad[i]))
        return "".join(chiper_list)


class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        super().__init__(input_text)
        
        if pad is None:
            self.pad = self.generate_pad()
        else:
            self.pad = pad
        
        self.ciphertext = self.apply_pad(self.pad)
    
    def __repr__(self):
        return f'''PlaintextMessage('{self.get_text()}', {self.get_pad()})'''

    def generate_pad(self):
        lista = []
        for i in range(len(self.text)):
            lista.append(random.randint(0, 109))
        return lista

    def get_pad(self):
        return self.pad[:]

    def get_ciphertext(self):
        return self.ciphertext

    def change_pad(self, new_pad):
        self.pad = new_pad
        self.ciphertext = self.apply_pad(self.pad)


class EncryptedMessage(Message):
    def __init__(self, input_text):
        super().__init__(input_text)

    def __repr__(self):
        return f'''EncryptedMessage('{self.get_text()}')'''

    def decrypt_message(self, pad):
        neg_pad = [-s for s in pad]
        decrypted_text = self.apply_pad(neg_pad)
        return PlaintextMessage(decrypted_text, pad)

if __name__ == '__main__':
    msg_original = PlaintextMessage("Ola Mundo!")
    print(f"Original: {msg_original.get_text()}")
    print(f"Criptografado: {msg_original.get_ciphertext()}")

    cipher_text = msg_original.get_ciphertext()
    pad_usado = msg_original.get_pad()

    msg_travada = EncryptedMessage(cipher_text)

    msg_revelada = msg_travada.decrypt_message(pad_usado)
    print(f"Revelado: {msg_revelada.get_text()}")
