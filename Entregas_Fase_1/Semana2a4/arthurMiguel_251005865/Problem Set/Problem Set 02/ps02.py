import string

def has_player_won(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True

def get_word_progress(secret_word, letters_guessed):
    progresso = ""
    for i in secret_word:
        if i in letters_guessed:
            progresso += i
        else:
            progresso += "*"
    return progresso

def get_available_letters(letters_guessed):
    alfabeto = string.ascii_lowercase
    temp = ""
    for c in alfabeto:
        if c not in letters_guessed:
            temp += c
    return temp

def hangman(secret_word, with_help):
    tentativas_restantes = 10
    letters_guessed = []

    print("Bem vindo ao jogo da forca!")
    print(f"A palavra que eu estou pensando tem {len(secret_word)} letras.")

    while tentativas_restantes > 0 and not has_player_won(secret_word, letters_guessed):
        print("-------------")
        print(f" Você tem {tentativas_restantes} tentativas.")
        print(f"Letras disponíveis: {get_available_letters(letters_guessed)}")

        chute = input("Tentativa: ").lower()

        if not chute.isalpha() or len(chute) != 1:
            print("Isso não é uma letra válida.")
        elif chute in letters_guessed:
            print("Você já tentou essa letra! ")
        else:
            letters_guessed.append(chute)
            if chute in secret_word:
                print("Bom chute!")
            else:
                print("Essa letra não está na palavra.")
                tentativas_restantes -= 1

        print(get_word_progress(secret_word, letters_guessed))

    print("-------------")
    if has_player_won(secret_word, letters_guessed):
        print("Parabéns! Você venceu! ")
    else:
        print(f"Desculpe, você perdeu =(. A palavra era: {secret_word}")