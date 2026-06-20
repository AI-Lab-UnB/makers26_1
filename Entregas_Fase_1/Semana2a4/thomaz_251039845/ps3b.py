import random
import string



class Message:
  

    def __init__(self, input_text: str):
        self.message = input_text

    def get_text(self) -> str:
        return self.message

    def shift_char(self, char: str, shift: int) -> str:
      
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    def apply_pad(self, pad: list) -> str:

        result = []
        for i, ch in enumerate(self.message):
            shift = pad[i % len(pad)]
            result.append(self.shift_char(ch, shift))
        return ''.join(result)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.message}')"

class PlaintextMessage(Message):

    def __init__(self, input_text: str, pad: list = None):
        super().__init__(input_text)
        if pad is None:
            pad = [random.randint(0, 25) for _ in range(len(input_text))]
        self.pad = pad

    def get_pad(self) -> list:
        return self.pad

    def change_pad(self, new_pad: list):
        self.pad = new_pad

    def generate_pad(self, n: int) -> list:
        return [random.randint(0, 25) for _ in range(n)]

    def get_pad_text(self) -> str:
        return self.apply_pad(self.pad)

    def encrypt_message(self) -> 'EncryptedMessage':
        ciphertext = self.get_pad_text()
        return EncryptedMessage(ciphertext)

    def copy(self) -> 'PlaintextMessage':
        return PlaintextMessage(self.message, list(self.pad))

    def __repr__(self):
        return f"PlaintextMessage('{self.message}', pad={self.pad})"
class EncryptedMessage(Message):
    def __init__(self, input_text: str):
        super().__init__(input_text)

    def decrypt_message(self, pad: list) -> PlaintextMessage:
        inverse_pad = [(-v) % 26 for v in pad]
        original = self.message
        plaintext = self.apply_pad(inverse_pad)
        return PlaintextMessage(plaintext, pad)

    def __repr__(self):
        return f"EncryptedMessage('{self.message}')"
def load_words(file_path: str = 'words.txt') -> list:
    try:
        with open(file_path) as f:
            return [w.strip().lower() for w in f if w.strip()]
    except FileNotFoundError:
        return [
            'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'it',
            'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this',
            'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or',
            'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what',
            'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me',
        ]


def is_word(word: str, word_list: list) -> bool:
    cleaned = word.lower().strip(string.punctuation)
    return cleaned in word_list


def decrypt_message_try_pads(enc_message: EncryptedMessage,
                              pads: list,
                              word_list: list = None) -> PlaintextMessage:
    if word_list is None:
        word_list = load_words()

    best_plaintext = None
    best_score = -1

    for pad in pads:
        candidate: PlaintextMessage = enc_message.decrypt_message(pad)
        tokens = candidate.get_text().split()
        score = sum(1 for t in tokens if is_word(t, word_list))

        if score > best_score:
            best_score = score
            best_plaintext = candidate

    return best_plaintext

if __name__ == '__main__':
    print("=== Part B – One Time Pad Encryption ===\n")

    original = "Hello World"
    pad = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]   
    pm = PlaintextMessage(original, pad)
    print(f"Original : {pm.get_text()}")
    print(f"Pad      : {pm.get_pad()}")

    enc = pm.encrypt_message()
    print(f"Encrypted: {enc.get_text()}")

    dec = enc.decrypt_message(pad)
    print(f"Decrypted: {dec.get_text()}")
    assert dec.get_text() == original, "Round-trip failed!"
    print("Round-trip OK\n")

    secret = "meet me at noon"
    correct_pad = [random.randint(0, 25) for _ in range(len(secret))]
    pm2 = PlaintextMessage(secret, correct_pad)
    enc2 = pm2.encrypt_message()

    fake_pads = [[random.randint(0, 25) for _ in range(len(secret))]
                 for _ in range(19)]
    candidate_pads = fake_pads + [correct_pad]
    random.shuffle(candidate_pads)

    result = decrypt_message_try_pads(enc2, candidate_pads)
    print(f"Secret message : '{secret}'")
    print(f"Best decryption: '{result.get_text()}'")