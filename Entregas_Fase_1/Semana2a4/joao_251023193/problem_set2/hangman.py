# Problem Set 2, hangman.py
# Name: João Vítor Sauma de Faria
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = __file__[:-len('hangman.py')] + 'words.txt'

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
  
def help_reveal_letter(secret_word, available_letters, with_help, attempts_remaining):
  
  if with_help == True:
    
    words_to_reveal = []
    
    if attempts_remaining > 3:
      
      for char in available_letters:
        
        if char in secret_word:
          words_to_reveal.append(char)
          
    else:
      return print(f"Oops ! Not enough guesses left")
        
  
    if not words_to_reveal:
      return None
        
    return random.choice(words_to_reveal)
  else:
    print("To use '!', activate the help before start the game ")

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
  
  hidden_secret_word = ""
  
  for char in secret_word:
    if char in letters_guessed:
      hidden_secret_word += char
    else:
      hidden_secret_word += "*"
  
  
  return hidden_secret_word


def get_available_letters(letters_guessed):
  
  available_letters = string.ascii_lowercase
    
  for char in available_letters:
    if char in letters_guessed:
      available_letters = available_letters.replace(char, "")
    
  return available_letters


def hangman(secret_word, with_help):
  
  #inicio do jogo
  
  print(f"""
        Welcome to the Hangman game!\n\n
        I am thinking of a word that is {len(secret_word)} letters long.\n\n
        Rules:\n
        1 - Only 1 letter per attempt\n
        2 - Digit "!" for help (if with_help = True)\n
        Good Luck!\n""")
  
  
  attempts_remaining = 10
  letters_guessed = []
  
  #fluxo do jogo
  
  while has_player_won(secret_word, letters_guessed) != True and attempts_remaining > 0:
    print("--------------")
    print(f"You have {attempts_remaining} guesses left")
    print(f"Available letters: {get_available_letters(letters_guessed)}")
    
    attempt = input("Please guess a letter: ")
    attempt = attempt.lower()
    
    #caminhos do input
    
    if attempt == "!":
      
      letter_revealed = help_reveal_letter(secret_word, get_available_letters(letters_guessed), with_help, attempts_remaining)

      
      if letter_revealed == None:
        None
        
      else:
        letters_guessed.append(letter_revealed)
        attempts_remaining -= 3
        print(f"Letter revealed: {letter_revealed}")
        print(get_word_progress(secret_word, letters_guessed))
    
    elif attempt.isalpha() != True or len(attempt) != 1:
      print(f"\nOops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
      
    elif attempt in letters_guessed:
      print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
      
    elif attempt in secret_word:
      letters_guessed.append(attempt)
      print(f"\nGood guess: {get_word_progress(secret_word, letters_guessed)}")
      
    elif attempt in ["a", "e", "i", 'o', "u"] and attempt not in secret_word:
      letters_guessed.append(attempt)
      attempts_remaining -= 2
      print(f"\nOops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
      
    else:
      letters_guessed.append(attempt)
      attempts_remaining -= 1
      print(f"\nOops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
 
      
    if has_player_won(secret_word, letters_guessed):
      unique_letters = len(set(secret_word))
      total_score = (attempts_remaining + 4 * unique_letters) + (3 * len(secret_word))
      print("--------------")
      print(f"\nCongratulations, you won!")
      print(f"Your total score for this game is: {total_score}\n")
      break

 
    
    if attempts_remaining <= 0:
      print("--------------")
      print(f"Sorry, you ran out of guesses. The word was {secret_word}.\n")
      
    

if __name__ == "__main__":

  secret_word = choose_word(wordlist)
  with_help = True
  hangman(secret_word, with_help)




