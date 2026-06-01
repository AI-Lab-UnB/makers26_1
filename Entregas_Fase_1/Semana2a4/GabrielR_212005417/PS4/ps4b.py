
'''
LINHA DE PENSAMENTO:
- PARTE 1: classe Message com metodos de deslocamento de caracteres
- PARTE 2: classe PlaintextMessage para criptografar mensagens com pad
- PARTE 3: classe EncryptedMessage para descriptografar mensagens
'''

import random

# CONSTANTES - intervalo de caracteres ASCII permitidos
ASCII_MIN = 32
ASCII_MAX = 126
TOTAL_CHARS = 95  # total de caracteres no intervalo (126 - 32 + 1)

# CLASSE MAE - MESSAGE
# contem metodos compartilhados entre mensagem plaintext e criptografada
class Message:
    def __init__(self, texto_entrada):
        # armazena o texto da mensagem
        self.texto_mensagem = texto_entrada

    def get_text(self):
        # retorna o texto da mensagem
        return self.texto_mensagem

    def shift_char(self, char, deslocamento):
        # desloca um caractere pelo valor do deslocamento usando ASCII
        # usa modulo para garantir que fica no intervalo 32-126
        valor_ascii = ord(char)
        novo_valor = (valor_ascii - ASCII_MIN + deslocamento) % TOTAL_CHARS + ASCII_MIN
        return chr(novo_valor)

    def apply_pad(self, pad):
        # aplica o pad a cada caractere do texto e retorna o texto cifrado
        texto_cifrado = ''
        for i, char in enumerate(self.texto_mensagem):
            texto_cifrado += self.shift_char(char, pad[i])
        return texto_cifrado

    def __repr__(self):
        return f'Message: {self.texto_mensagem}'

# CLASSE FILHA - PLAINTEXTMESSAGE
# representa uma mensagem em texto plano que pode ser criptografada
class PlaintextMessage(Message):
    def __init__(self, texto_entrada, pad=None):
        # chama o construtor da classe mae
        super().__init__(texto_entrada)

        # gera pad aleatorio se nao for fornecido
        if pad is None:
            self.pad = self.generate_pad()
        else:
            # salva uma copia do pad para evitar mutacao
            self.pad = pad[:]

    def generate_pad(self):
        # gera um pad aleatorio com inteiros no intervalo [0, 110)
        # cada posicao do texto recebe um valor aleatorio
        pad_aleatorio = []
        for _ in self.texto_mensagem:
            pad_aleatorio.append(random.randint(0, 109))
        return pad_aleatorio

    def get_pad(self):
        # retorna uma copia do pad para evitar mutacao do original
        return self.pad[:]

    def get_ciphertext(self):
        # retorna o texto criptografado usando o pad atual
        return self.apply_pad(self.pad)

    def change_pad(self, novo_pad):
        # atualiza o pad e recalcula o texto cifrado
        self.pad = novo_pad[:]

    def __repr__(self):
        return f'PlaintextMessage: {self.texto_mensagem}, Pad: {self.pad}'

# CLASSE FILHA - ENCRYPTEDMESSAGE
# representa uma mensagem criptografada que pode ser descriptografada
class EncryptedMessage(Message):
    def __init__(self, texto_entrada):
        # chama o construtor da classe mae
        super().__init__(texto_entrada)

    def decrypt_message(self, pad):
        # descriptografa aplicando o pad invertido (valores negativos)
        pad_invertido = [-valor for valor in pad]
        return self.apply_pad(pad_invertido)

    def __repr__(self):
        return f'EncryptedMessage: {self.texto_mensagem}'
if __name__ == '__main__':
    # testando Message
    m = Message('Hello!')
    print('Texto:', m.get_text())
    print('Shift A por 5:', m.shift_char('A', 5))

    # testando PlaintextMessage
    pt = PlaintextMessage('Hello!', [5, 10, 2, 3, 0, 2])
    print('Pad:', pt.get_pad())
    print('Cifrado:', pt.get_ciphertext())

    # testando EncryptedMessage
    enc = EncryptedMessage(pt.get_ciphertext())
    print('Decifrado:', enc.decrypt_message(pt.get_pad()))