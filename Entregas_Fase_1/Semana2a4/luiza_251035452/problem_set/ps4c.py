import ps4b
import os
import ast


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORDLIST_FILENAME = os.path.join(BASE_DIR, 'words.txt')

def load_words(file_name):
    print(f"Carregando lista de palavras do arquivo {file_name}...")
    with open(file_name, 'r') as f:
        words = f.read().split()
    print(f"  {len(words)} palavras carregadas.")
    return words

def is_word(wordlist, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordlist

def get_story_string():
    with open(os.path.join(BASE_DIR, "story.txt"), 'r') as f:
        return f.read().strip()

def get_story_pads():
    with open(os.path.join(BASE_DIR, "pads.txt"), 'r') as f:
        conteudo = f.read()
    return ast.literal_eval(conteudo)

wordlist = load_words(WORDLIST_FILENAME)


class EncryptedMessage(ps4b.EncryptedMessage):
    def decrypt_message_try_pads(self, pads):
        melhor_pad = None
        maior_contagem = -1
        tamanho_texto = len(self.get_text())

        for pad in pads:
            if len(pad) != tamanho_texto:
                continue

            texto_decifrado = self.decrypt_message(pad)
            palavras = texto_decifrado.split()
            contagem = sum(1 for p in palavras if is_word(wordlist, p))

            if contagem >= maior_contagem:
                maior_contagem = contagem
                melhor_pad = pad

        if melhor_pad is None:
            return None

        texto_final = self.decrypt_message(melhor_pad)
        return ps4b.PlaintextMessage(texto_final, melhor_pad)


def decode_story():
    ciphertext = get_story_string()
    pads = get_story_pads()
    
    print(f"Tamanho do texto: {len(ciphertext)}")
    print(f"Total de pads: {len(pads)}")
    print(f"Tamanhos dos primeiros 5 pads: {[len(p) for p in pads[:5]]}")
    
    mensagem = EncryptedMessage(ciphertext)
    return mensagem.decrypt_message_try_pads(pads)

if __name__ == "__main__":
    mensagem = EncryptedMessage("Monoo#")
    pads = [[5, 10, 2, 3, 0, 2], [1, 2, 3, 4, 5, 6]]
    resultado = mensagem.decrypt_message_try_pads(pads)
    print(resultado.get_text())
    print(resultado.get_pad())

    historia = decode_story()
    if historia is None:
        print("Nenhum pad compatível encontrado")
    else:
        print(historia.get_text())