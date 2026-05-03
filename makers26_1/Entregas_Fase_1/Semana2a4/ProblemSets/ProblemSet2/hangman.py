# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

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
    for char in secret_word:
        if char not in letters_guessed:
            return False;

    return True;


def get_word_progress(secret_word, letters_guessed):
    
    result = ""

    for char in secret_word:
        if char not in letters_guessed:
            result+='*'
        else:
            result+=char

    return result


def get_available_letters(letters_guessed):
    alphabet = string.ascii_lowercase
    avilable_letters=""

    for char in alphabet:
        if char not in letters_guessed:
            avilable_letters+=char

    return avilable_letters



def hangman(secret_word, with_help):
    
    print("Welcome to Hangman")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    guesses_left=10
    letters_guessed=[]

    while guesses_left>0 and not has_player_won(secret_word,letters_guessed):

      print(f"{guesses_left}")
        
      guess = input("Please guess a letter: ").lower()

      if with_help and guess=='!':
        if guesses_left<=3:
          print("Oops you don't have enough guesses anymore")
        else:
          guesses_left-=3
          for char in secret_word:
            if char not in letters_guessed:
              letters_guessed.append(char)
              print(f"Help revealed the letter '{char}'")
              print(f"Word progress: {get_word_progress(secret_word, letters_guessed)}")
              break 
        continue
      
      if not guess.isalpha() or len(guess)!=1:
          print("Invalid Input")
          continue
      
      if guess in letters_guessed:
        print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")        

      elif guess in secret_word:
        letters_guessed.append(guess)
        print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")

      else:
        letters_guessed.append(guess)
        if guess in "aeiou":
            guesses_left -= 2
        else:
            guesses_left -= 1
        print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")

    if has_player_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
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

