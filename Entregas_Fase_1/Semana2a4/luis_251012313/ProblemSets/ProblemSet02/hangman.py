# Problem Set 2, hangman.py
# Name: Luis
# Collaborators:
# Time spent:

import os
import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------
base_dir = os.path.dirname(__file__) # ajuste para funcionar em qualquer computador, sem se importar com o sistema operacional
WORDLIST_FILENAME = os.path.join(base_dir, "words.txt")

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True

def get_word_progress(secret_word, letters_guessed):
    progress = ""
    
    for char in secret_word:
        if char in letters_guessed:
            progress += char
        else:
            progress += "*"
    
    return progress	 


def get_available_letters(letters_guessed):
    available = ""
    
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available += char
    
    return available
   

def hangman(secret_word, with_help):
    x = 10
    letters_guessed = []
    vowels = "aeiou"

    print("Welcome to the Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    while x > 0 and not has_player_won(secret_word, letters_guessed):
        available_letters = get_available_letters(letters_guessed)

        print("-------------")
        print(f"You have {x} guesses left.")
        print(f"Available Letters: {available_letters}")

        word_guessed = input("Please guess a letter: ").lower()

        if with_help and word_guessed == '!':
            if x < 3:
                print("Sorry, you don't have enough guesses for help")
            else:
                missing_letters = []

                for letter in secret_word:
                    if letter not in letters_guessed:
                        missing_letters.append(letter)

                revealed = random.choice(missing_letters)
                letters_guessed.append(revealed)

                x -= 3

                print(f"Letter revealed: {revealed}")
                print(get_word_progress(secret_word, letters_guessed))

            continue

        if len(word_guessed) != 1 or word_guessed not in string.ascii_lowercase:
            print("Oops! That word is not valid")
            continue

        if word_guessed in letters_guessed:
            print(f"Oops! You've already guessed that letter. {get_word_progress(secret_word, letters_guessed)}")
            continue

        letters_guessed.append(word_guessed)

        if word_guessed in secret_word:
            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
        else:
            if word_guessed in vowels:
                x -= 2
            else:
                x -= 1

            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")

    print("--------------")

    if has_player_won(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        total_score = x + (4 * unique_letters) + (3 * len(secret_word))

        print("Congratulations, you won!")
        print(f"Your total score for this game is: {total_score}")
    else:
        print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
        print(f"The word was: {secret_word}")


if __name__ == "__main__":
    # To test your game, uncomment the following three lines.
    
    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    pass