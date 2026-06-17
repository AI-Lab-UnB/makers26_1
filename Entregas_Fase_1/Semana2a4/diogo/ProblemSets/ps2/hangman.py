# Problem Set 2, hangman.py
# Name: Diogo Oliveira
# Collaborators: Diogo Oliveira
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid_vowels words. Words are strings of lowercase letters.

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
word_choosen = choose_word(wordlist=wordlist)

alphabet_set = set(string.ascii_lowercase)
valid_vowels = {"a", "e", "i", "o", "u"}

choosen_word_letters = set()

for letter in word_choosen:
  choosen_word_letters.add(letter)

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """

    counter = 0
    
    for letter in letters_guessed:
      if letter in choosen_word_letters:
        counter += 1
      else:
        return False
    
    if(counter == len(choosen_word_letters)):
      return True
      


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    
    guessed_letters = []
    
    for letter in secret_word:
      if letter in letters_guessed:
        guessed_letters.append(letter)
      else:
        guessed_letters.append("*")
    guessed_letters = "".join(guessed_letters)
    
    return guessed_letters

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    
    avaliable_letters = []
    
    for letter in alphabet_set:
      if letter not in letters_guessed:
        avaliable_letters += letter
        
    avaliable_letters.sort()
    sorted_avaliable_letters = "".join(avaliable_letters)
    
    return sorted_avaliable_letters



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
    letters_guessed = set()
    
    while(not(has_player_won(secret_word=word_choosen, letters_guessed=letters_guessed)) and guesses != 0 ):
      
      avaliable_letters = get_available_letters(letters_guessed=letters_guessed)
    
      print("=" * 50)
    
      # Prints iniciais
      print(f" --- The secret word has {len(word_choosen)} letters \n")
      print(f"You have {guesses} guesses remaining \n")
      print(f"You CAN use a HINT for the COST of 3 guesses \n Use '!' for a HINT \n")
      print("If you miss inserting a character you LOSE 1 guess \n")
      print("If you miss inserting a VOWEL you LOSE 2 guesses \n")
      
      print(" --- You have not guessed these letters: \n")
      print(avaliable_letters)
      print("\n")
      
      # PALAVRA
      print(f" --- The word guessed so far: \n")
      print(get_word_progress(secret_word=word_choosen, letters_guessed=letters_guessed))
      
      # Entrada do Usuário
      while True:
        invalid = False
        user_input = input("Insert a letter in LOWERCASE to guess the secret word \n\n")
        if(len(user_input) != 1):
          print("Insert only one character \n")
          invalid = True
          
        if(user_input == "!"):
          if(not(with_help)):
            print("The help function is not avaliable: \n")
            invalid = True
          else:
            break  
        
        elif(user_input not in alphabet_set):
          print("Insert a valid character \n Valid characters: \n")
          print(avaliable_letters)
          print("\n")
          invalid = True
          
        if(not(invalid)):
          break
      
      # Processar Chute
      if(user_input in letters_guessed):
        print(f"The letter '{user_input}' was already guessed: \n")
      
      # Uso da DICA
      if(user_input == "!"):
        if(guesses > 3):
          guesses -= 3
          print(f"You spent 3 guesses for the hint \n Current Guesses: {guesses} \n")        
          for letter in choosen_word_letters:
            if (letter not in letters_guessed):
              letters_guessed.add(letter)
              print(f"The hint is the letter: '{letter}'")
              break
        else:
          print("Not enough guesses for the hint \n")
      
      # Chute de Letra
      elif(user_input not in letters_guessed):
        guesses -= 1
        letters_guessed.add(user_input)
        
        # Chute INCORRETO
        if(user_input not in choosen_word_letters):
          
          if(user_input in valid_vowels):
            guesses -= 1 # Vowel --> -2
            print("You lost 2 guesses for missing with a Vowel \n")
          print(f"The letter '{user_input}' is NOT in the word: \n")
          
        # Chute CORRETO
        else:
          print(f"The letter '{user_input}' IS in the word: \n")
        
    if(guesses == 0 and not(has_player_won(secret_word=word_choosen, letters_guessed=letters_guessed))):
      print("\n YOU LOST! \n You ran out of guesses \n")
    else:
      print("\n YOU WON \n Congratulations!!! \n")
      
    print(f"The secret word was {word_choosen}")

        

# When you've completed your hangman function, scroll down to the bottom
# of the file \nand uncomment the lines to test

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