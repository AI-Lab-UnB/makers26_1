# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = 'makers26_1\Entregas_Fase_1\Semana2a4\mariana_252030272\pset2\palavras.txt'
ALFABETO = "abcdefghijklmnopqrstuvwxyz"

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
    string_retornada = ""
    for i in range(len(secret_word)):
      if secret_word[i] in letters_guessed:
        o = secret_word[i]
      else:
        o = "*"
      string_retornada += o
      
    return string_retornada
            
        

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    string_retornada = ""
    for i in range(len(ALFABETO)):
      if(ALFABETO[i] not in letters_guessed):
        string_retornada += ALFABETO[i] 
    return string_retornada



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    guesses = 10
    chutes = []
    palavra = get_word_progress(secret_word, chutes)
    char_unicos = set(secret_word)

    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    while(not has_player_won(secret_word, palavra) and guesses != 0):
      print("--------------")
      guesses_reduced = 1
      print(f"You currently have {guesses} guesses left")
      letras_faltantes = get_available_letters(chutes)
      print("Available letters: ", letras_faltantes) 
      letter_guessed = input("Please guess a letter: ").lower()
      if letter_guessed in ALFABETO and letter_guessed not in chutes:
        chutes.append(letter_guessed)
        if letter_guessed in "aeiou":
           guesses_reduced = 2
        if letter_guessed in secret_word:
          print("Good guess: ", end="")
        else:
          print("Oops! That letter is not in my word: ", end="")
          guesses -= guesses_reduced
      elif letter_guessed == "!" and with_help == True:
        for i in range(len(letras_faltantes)):
           if letras_faltantes[i] in secret_word:
              chutes.append(letras_faltantes[i])
      elif(letter_guessed in chutes):
        print("Oops! You've already guessed that letter: ", end="")
      else:
        print("Oops! That is not a valid letter. Please input a letter from the alphabet: ")

         

      palavra = get_word_progress(secret_word, chutes)
      print(palavra)
    if guesses == 0:
      print("Sorry, you ran out of guesses. The word was {secret_word}.")
    else:
       print("Congratulations, you won!")
       print(f"Your total score for this game is: {guesses + 4 * len(char_unicos) + 3 * len(secret_word)}")

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

