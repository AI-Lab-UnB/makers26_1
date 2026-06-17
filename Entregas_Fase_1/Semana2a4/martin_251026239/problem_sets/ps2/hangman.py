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
    """s
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
    
  for letters in (secret_word):
    if letters not in letters_guessed:
      return False
  return True


def get_word_progress(secret_word, letters_guessed):
    
    progress = ""

    for letters in (secret_word):
      if letters in letters_guessed:
        progress += letters
      else:
        progress += "*"
    return progress


def get_available_letters(letters_guessed):
    
    available_letters = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letters in (alphabet):
       if letters not in letters_guessed:
          available_letters += letters
    return available_letters


def hangman(secret_word, with_help):
    
    guesses_remaining = 10
    letters_guessed = []
    length = len(secret_word)

    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {length} letters long.")

    while guesses_remaining > 0 and not has_player_won(secret_word, letters_guessed):
        print("--------------")
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")

        guess = input("Please guess a letter: ").lower()

        if guess == "!" and with_help:
            if guesses_remaining < 3:
              print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 3

                missing_letters = []
                for letter in secret_word:
                    if letter not in letters_guessed and letter not in missing_letters:
                        missing_letters.append(letter)

                revealed_letter = random.choice(missing_letters)
                letters_guessed.append(revealed_letter)
                print(f"Letter revealed: {revealed_letter}")
                print(get_word_progress(secret_word, letters_guessed))

        elif not guess.isalpha() or len(guess) != 1:
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
        elif guess in letters_guessed:
            print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
            
        else:
            letters_guessed.append(guess)
            
            if guess in secret_word:
                print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
                
            else:
                print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
                
                vowels = ['a', 'e', 'i', 'o', 'u']
                if guess in vowels:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1

    print("--------------")

    if has_player_won(secret_word, letters_guessed):
        unique_letters = len(set(secret_word)) 
        
        total_score = (guesses_remaining + 4 * unique_letters) + (3 * length)
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {total_score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

