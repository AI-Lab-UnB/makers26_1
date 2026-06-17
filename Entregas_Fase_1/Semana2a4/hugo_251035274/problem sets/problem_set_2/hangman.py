# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

WORDLIST_FILENAME = "Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_2/words.txt"

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
    
    list_secret_word = list(secret_word)
    for letter in list_secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    
    list_secret_word = list(secret_word)
    progress = ""
    for letter in list_secret_word:
      if letter in letters_guessed:
        progress += letter
      else:
        progress += "*"
    return progress


def get_available_letters(letters_guessed):
    
    string_available_letters = string.ascii_lowercase
    for letter in letters_guessed:
        string_available_letters = string_available_letters.replace(letter, "")
    return string_available_letters
    

def letter_selector(secret_word, available_letters):
  choose_from = ""
  for letter in secret_word:
    if letter in available_letters:
      choose_from += letter

  revealed_letter = random.choice(choose_from)
  return revealed_letter
  



def hangman(secret_word, with_help):
    print("Welcome to the Hangman game!")
    length_word = len(secret_word)
    print(f"I am thinking of a word that is {length_word} letters long.")
    print("--------------")
    
    guesses = 10
    letters_guessed = ""
    while True:
      print(f"You have {guesses} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      letter = str(input("Please guess a letter: "))
      letter_lower = letter.lower()
      caractere = list(secret_word)
      
      if letter_lower == "!" and with_help == True:
        if guesses > 3:
          revealed_letter = letter_selector(secret_word, get_available_letters(letters_guessed))
          print(f"Letter revealed: {revealed_letter}")
          letters_guessed += revealed_letter
          print(get_word_progress(secret_word, letters_guessed))
          guesses -= 3
          print("--------------")
        else:
          print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
          print("--------------")
      elif letter_lower in letters_guessed:
        print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
        print("--------------")
      elif letter_lower in caractere:
        letters_guessed += letter
        print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
        print("--------------")
      elif len(letter) > 1 or not letter.isalpha() :
        print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
        print("--------------")
      else:
        letters_guessed += letter
        print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
        guesses -= 1
        print("--------------")
      
      game_status = has_player_won(secret_word, letters_guessed)
      if game_status == True:
        print("Congratulations, you won!")
        unique_word = len(set(secret_word))
        total_score = (guesses + 4 * unique_word) + (3 * len(secret_word))
        print(f"Your total score for this game is: {total_score}")
        break
      elif guesses == 0:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
        break
      else:
        continue
        
      


if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)



