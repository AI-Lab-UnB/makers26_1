# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
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

def reveal_letter(secret_word, available_letters):
    choose_from = ''
    for letter in secret_word:
        if letter in available_letters and letter not in choose_from:
            choose_from += letter
    new = random.randint(0, len(choose_from) - 1)
    return choose_from[new]

def hangman(secret_word, with_help):
    guesses = 10
    letters_guessed = []
    vowels = 'aeiou'

    print("Welcome to Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    while not has_player_won(secret_word, letters_guessed) and guesses > 0:
        print("--------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()

        if with_help and guess == '!':
            if guesses < 3:
                print("Oops! Not enough guesses left:", get_word_progress(secret_word, letters_guessed))
            else:
                revealed = reveal_letter(secret_word, get_available_letters(letters_guessed))
                letters_guessed.append(revealed)
                guesses -= 3
                print("Letter revealed:", revealed)
                print(get_word_progress(secret_word, letters_guessed))
        elif not guess.isalpha() or len(guess) != 1:
            print("Oops! That is not a valid letter. Please input a letter from the alphabet:", get_word_progress(secret_word, letters_guessed))
        elif guess in letters_guessed:
            print("Oops! You've already guessed that letter:", get_word_progress(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Good guess:", get_word_progress(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))
                if guess in vowels:
                    guesses -= 2
                else:
                    guesses -= 1

    if has_player_won(secret_word, letters_guessed):
        print("--------------")
        unique_letters = len(set(secret_word))
        score = (guesses + 4 * unique_letters) + (3 * len(secret_word))
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    else:
        print("--------------")
        print("Sorry, you ran out of guesses. The word was", secret_word)

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)