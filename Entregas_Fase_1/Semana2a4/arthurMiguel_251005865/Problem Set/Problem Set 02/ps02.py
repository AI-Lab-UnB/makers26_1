import string
def has_player_won(secret_word, letters_guessed):
    contador = 0
    for i in secret_word:
        for j in letters_guessed:
            if i == j:
                contador += 1
    if contador == len(secret_word):
        return True
    
def guess_letter(secret_word):
    progresso = ""

    for i in secret_word:
        if i in secret_word:
            progresso += i
        else:
            progresso += "*"
    return progresso

def get_available_letters(letters_guessed):
    alfabeto = string.ascii_letters
    temp=""
    for c in alfabeto:
        if c not in alfabeto:
            temp += c
    return temp

def hangman(secret_word,with_help):
    print("Bem Vindo ao jogo da forca!")
