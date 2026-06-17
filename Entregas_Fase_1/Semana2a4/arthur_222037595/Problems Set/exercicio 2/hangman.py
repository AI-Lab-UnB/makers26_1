# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for letra in secret_word:
        if letra not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    resultado = ""
    for letra in secret_word:
        if letra in letters_guessed:
            resultado += letra
        else:
            resultado += "*"
    return resultado


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    disponiveis = ""
    for letra in string.ascii_lowercase:
        if letra not in letters_guessed:
            disponiveis += letra
    return disponiveis


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.
    """
    vogais = "aeiou"
    guesses_remaining = 10
    letters_guessed = []

    print("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    while guesses_remaining > 0 and not has_player_won(secret_word, letters_guessed):
        print("-" * 13)
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        chute = input("Please guess a letter: ").lower()

        # trata o caractere de ajuda
        if with_help and chute == "!":
            if guesses_remaining < 3:
                print("Oops! Not enough guesses left:", get_word_progress(secret_word, letters_guessed))
            else:
                # escolhe uma letra da palavra que ainda nao foi chutada
                opcoes = [c for c in secret_word if c not in letters_guessed]
                revelada = random.choice(opcoes)
                letters_guessed.append(revelada)
                guesses_remaining -= 3
                print("Letter revealed:", revelada)
                print(get_word_progress(secret_word, letters_guessed))
            continue

        # valida entrada: tem que ser uma unica letra
        if len(chute) != 1 or not chute.isalpha():
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:",
                  get_word_progress(secret_word, letters_guessed))
            continue

        if chute in letters_guessed:
            print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
            continue

        letters_guessed.append(chute)

        if chute in secret_word:
            print("Good guess:", get_word_progress(secret_word, letters_guessed))
        else:
            # vogal errada custa 2, consoante errada custa 1
            if chute in vogais:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))

    print("-" * 13)
    if has_player_won(secret_word, letters_guessed):
        score = (guesses_remaining + 4 * len(set(secret_word))) + (3 * len(secret_word))
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)
