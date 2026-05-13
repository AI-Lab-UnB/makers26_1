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

    for letter in secret_word:
        
        if letter in letters_guessed:
          pass
        
        else:
          return False
        
    return True



def get_word_progress(secret_word, letters_guessed):

    string_aux = ""

    

    for letter in secret_word:
        
        if letter in letters_guessed:
            string_aux += letter

        else:
            string_aux += "*"

    return string_aux



def get_available_letters(letters_guessed):

    string_aux = ""

    alfabeto = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z']


    for i in range(len(alfabeto)) :
        
        if alfabeto[i] not in letters_guessed:
            string_aux += alfabeto[i]

    return string_aux



def help(secret_word, letters_guessed):
    
    while True :

      new = random.randint(0, len(secret_word) - 1)
      
      if secret_word[new] not in letters_guessed:
          
          print(f"Letter revealed: {secret_word[new]}")

          letters_guessed.append(secret_word[new])

          print(f"{get_word_progress(secret_word, letters_guessed)}")

          return letters_guessed




def calculate_points(count_gusses_left, secret_word):

    unique_letters = []

    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)

    num_unique = len(unique_letters)

    total_score = (count_gusses_left + 4 * num_unique) + (3 * len(secret_word))

    return total_score



def hangman(secret_word, with_help):

    count_guesses_left = 10
    letters_guessed = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    consoantes = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


    print(f"Welcome to Hangman!\n I am thinking of a word that is {len(secret_word)} letters long.")

    while(True):

    
        
      print("--------------")
      print(f"You have {count_guesses_left} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      letter = input("Please guess a letter: ")
      letter.lower()

      skip = False

      if letter == "!" and with_help:
          letters_guessed = help(secret_word, letters_guessed)
          skip = True
          count_guesses_left -= 3


      elif letter in letters_guessed:
          print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
          continue
      
      elif letter.isalpha() == False:
          print("invalid enter!")
          continue
      
      else :
          letters_guessed.append(letter)



      if not skip:

        flag = False
        for i in range(len(secret_word)):

          if secret_word[i] == letter:
              
              print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
              flag = True
              

        if not flag:
            
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")

            if letter in vogais:
                count_guesses_left-= 2

            elif letter in consoantes:
                count_guesses_left-=1

      
      check_won = has_player_won(secret_word, letters_guessed)

      if check_won:
          print("------")
          print("Congratulations, you won!")
          print(f"Your total score for this game is: {calculate_points(count_guesses_left, secret_word)}\n")
          break
      
      if count_guesses_left <= 0:
          print("------")
          print("Sorry, you ran out of guesses. The word was else.")
          print(f"The correct word was : {secret_word}\n")
          break






if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman(secret_word, True)
    


