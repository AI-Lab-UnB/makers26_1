import random
import string
import os
WORDLIST_FILENAME = os.path.join(os.path.dirname(__file__), "words.txt")

def load_words():
    print("Carregando lista de palavras do arquivo...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "palavras carregadas.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_word_progress(secret_word, letters_guessed):
    progress = ""
    for letter in secret_word:
        if letter in letters_guessed:
            progress += letter
        else:
            progress += "*"
    return progress

def get_available_letters(letters_guessed):
    available = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter
    return available

def get_help_letter(secret_word, available_letters):
    choose_from = ""
    for letter in secret_word:
        if letter in available_letters and letter not in choose_from:
            choose_from += letter
    new = random.randint(0, len(choose_from) - 1)
    return choose_from[new]

def hangman(secret_word, with_help):
    guesses_remaining = 10
    letters_guessed = []
    vowels = "aeiou"

    print("Bem-vindo ao Hangman!")
    print(f"Estou pensando em uma palavra com {len(secret_word)} letras.")

    while not has_player_won(secret_word, letters_guessed) and guesses_remaining > 0:
        print("-------------")
        print(f"Você tem {guesses_remaining} tentativas restantes.")
        print(f"Letras disponíveis: {get_available_letters(letters_guessed)}")

        guess = input("Por favor, adivinhe uma letra: ").lower()

        # input de ajuda
        if with_help and guess == "!":
            if guesses_remaining < 3:
                print(f"Oops! Tentativas insuficientes: {get_word_progress(secret_word, letters_guessed)}")
            else:
                revealed = get_help_letter(secret_word, get_available_letters(letters_guessed))
                letters_guessed.append(revealed)
                guesses_remaining -= 3
                print(f"Letra revelada: {revealed}")
                print(get_word_progress(secret_word, letters_guessed))
            continue

        # input inválido
        if not guess.isalpha() or len(guess) != 1:
            print(f"Oops! Isso não é uma letra válida. Por favor, insira uma letra do alfabeto: {get_word_progress(secret_word, letters_guessed)}")
            continue

        # letra já chutada
        if guess in letters_guessed:
            print(f"Oops! Você já tentou essa letra: {get_word_progress(secret_word, letters_guessed)}")
            continue

        # letra válida e nova
        letters_guessed.append(guess)

        if guess in secret_word:
            print(f"Boa tentativa: {get_word_progress(secret_word, letters_guessed)}")
        else:
            print(f"Oops! Essa letra não está na palavra: {get_word_progress(secret_word, letters_guessed)}")
            if guess in vowels:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1

    # fim do jogo
    if has_player_won(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        total_score = (guesses_remaining + 4 * unique_letters) + (3 * len(secret_word))
        print("-------------")
        print("Parabéns, você ganhou!")
        print(f"Sua pontuação final foi: {total_score}")
    else:
        print("-------------")
        print(f"Que pena, você ficou sem tentativas. A palavra era: {secret_word}.")


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)