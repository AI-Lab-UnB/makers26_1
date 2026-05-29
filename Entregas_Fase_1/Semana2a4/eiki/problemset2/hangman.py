# Problem Set 2, hangman.py
# Name: Matheus
# Collaborators:
# Time spent: 1:30

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

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
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    result = ''
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += '*'
    return result


def get_available_letters(letters_guessed):
    available = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter
    return available



def hangman(secret_word, with_help):
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    guesses = 10
    letters_guessed = []
    vowels = 'aeiou'

    while guesses > 0 and not has_player_won(secret_word, letters_guessed):
        print("--------------")
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        guess = input("Please guess a letter: ").lower()

        # Caso especial: pediu ajuda
        if guess == '!' and with_help:
            if guesses < 3:
                print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
            else:
                revealed = get_help_letter(secret_word, get_available_letters(letters_guessed))
                letters_guessed.append(revealed)
                guesses -= 3
                print(f"Letter revealed: {revealed}")
                print(get_word_progress(secret_word, letters_guessed))

        # Input inválido
        elif not guess.isalpha() or len(guess) != 1:
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")

        # Letra já tentada
        elif guess in letters_guessed:
            print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")

        # Letra correta
        elif guess in secret_word:
            letters_guessed.append(guess)
            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")

        # Letra errada
        else:
            letters_guessed.append(guess)
            if guess in vowels:
                guesses -= 2  # vogal errada custa 2
            else:
                guesses -= 1  # consoante errada custa 1
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")

    # Fim do jogo
    print("--------------")
    if has_player_won(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        score = (guesses + 4 * unique_letters) + (3 * len(secret_word))
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# Função auxiliar para o modo com ajuda
def get_help_letter(secret_word, available_letters):
    choose_from = ''
    for letter in secret_word:
        if letter in available_letters and letter not in choose_from:
            choose_from += letter
    new = random.randint(0, len(choose_from) - 1)
    return choose_from[new]


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

