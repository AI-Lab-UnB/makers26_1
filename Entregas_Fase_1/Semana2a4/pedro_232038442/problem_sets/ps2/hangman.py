# Problem Set 2, hangman.py
# Name: Pedro Henrique
# Collaborators: none
# Time spent: 2h00

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

# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for char in secret_word:
        if char not in letters_guessed:
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
    result = ""
    for char in secret_word:
        if char in letters_guessed:
            result += char
        else:
            result += "*"
    return result


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
    guessed so far

    returns: string, comprised of letters that represents which
    letters have not yet been guessed. The letters should be returned in
    alphabetical order
    """
    available = ""
    for char in string.ascii_lowercase:
        if char not in letters_guessed:
            available += char
    return available


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.
    """
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    guesses_left = 10
    letters_guessed = []
    
    while guesses_left > 0:
        print("-------------")
        if has_player_won(secret_word, letters_guessed):
            break
            
        print(f"You have {guesses_left} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        guess = input("Please guess a letter: ")
        
        if with_help and guess == '!':
            if guesses_left < 3:
                print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
                continue
            else:
                guesses_left -= 3
                choose_from = []
                for c in secret_word:
                    if c not in letters_guessed and c not in choose_from:
                        choose_from.append(c)
                
                if len(choose_from) > 0:
                    revealed = random.choice(choose_from)
                    letters_guessed.append(revealed)
                    print(f"Letter revealed: {revealed}")
                    print(get_word_progress(secret_word, letters_guessed))
                
                if has_player_won(secret_word, letters_guessed):
                    break
                continue

        if len(guess) != 1 or not guess.isalpha():
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
            continue
            
        guess = guess.lower()
        
        if guess in letters_guessed:
            print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
            continue
            
        letters_guessed.append(guess)
        
        if guess in secret_word:
            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
        else:
            if guess in ['a', 'e', 'i', 'o', 'u']:
                guesses_left -= 2
            else:
                guesses_left -= 1
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
            
        if has_player_won(secret_word, letters_guessed):
            break

    print("-------------")
    if has_player_won(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        score = (guesses_left + 4 * unique_letters) + (3 * len(secret_word))
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)
