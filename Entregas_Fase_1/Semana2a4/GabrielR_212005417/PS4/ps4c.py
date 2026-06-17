# Problem Set 4C, ps4c.py
# Name: Gabriel
# Collaborators: None
# Time Spent:

'''
LINHA DE PENSAMENTO:
- PARTE 1: tentar varios pads e contar palavras validas em ingles
- PARTE 2: usar o melhor pad para descriptografar a historia do Bob
'''

import ps4b
import string

WORDLIST_FILENAME = 'words.txt'

# FUNCAO FORNECIDA - carrega lista de palavras
def load_words(filename):
    with open(filename, 'r') as f:
        conteudo = f.read()
    return conteudo.split()

# FUNCAO FORNECIDA - verifica se uma string e uma palavra valida
def is_word(wordlist, word):
    word = word.lower()
    word = word.strip(string.punctuation + string.whitespace)
    return word in wordlist

# FUNCAO FORNECIDA - carrega o texto cifrado da historia
def get_story_string():
    with open('story.txt', 'r') as f:
        story = f.read().strip()
    return story

# FUNCAO FORNECIDA - carrega os pads possiveis
def get_story_pads():
    import ast
    with open('pads.txt', 'r') as f:
        conteudo = f.read()
    pads = ast.literal_eval(conteudo)
    return pads

# PARTE 1 - TENTAR VARIOS PADS
# tenta descriptografar com cada pad e retorna PlaintextMessage com mais palavras validas
# em caso de empate retorna o ultimo pad com mais palavras validas
def decrypt_message_try_pads(mensagem_cifrada, pads):
    lista_palavras = load_words(WORDLIST_FILENAME)
    melhor_mensagem = None
    maior_contagem = -1

    for pad in pads:
        # descriptografa com o pad atual
        texto_decifrado = mensagem_cifrada.decrypt_message(pad)

        # conta quantas palavras validas existem no texto decifrado
        palavras = texto_decifrado.split()
        contagem = 0
        for palavra in palavras:
            palavra_limpa = palavra.strip(string.punctuation + string.whitespace).lower()
            if palavra_limpa in lista_palavras:
                contagem += 1

        # atualiza o melhor resultado se encontrou igual ou maior contagem
        if contagem >= maior_contagem:
            maior_contagem = contagem
            melhor_mensagem = ps4b.PlaintextMessage(texto_decifrado, pad)

    return melhor_mensagem

# PARTE 2 - DECODIFICAR A HISTORIA DO BOB
# usa decrypt_message_try_pads para encontrar o pad correto da historia
def decode_story():
    texto_cifrado = get_story_string()
    pads = get_story_pads()

    # cria objeto EncryptedMessage com o texto cifrado
    mensagem = ps4b.EncryptedMessage(texto_cifrado)

    # encontra o melhor pad e retorna o texto decifrado
    melhor_plaintext = decrypt_message_try_pads(mensagem, pads)
    return melhor_plaintext.get_text()

if __name__ == '__main__':
    print(decode_story())