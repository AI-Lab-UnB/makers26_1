# Problem Set 2, hangman.py
# Name: Júlia Campos
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "1_ps2/words.txt"

def count_guess(count_turn_guess,letter_guess,before_guess,after_guess):

    vowel = ['a','e','i','o','u']
    
    if before_guess!=after_guess:
        return count_turn_guess

    else:
        if letter_guess in vowel:
            return count_turn_guess-2
        else:
            return count_turn_guess-1


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

    for i in secret_word:
        if i not in letters_guessed:
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
    count_word = len(secret_word)

    word = ['*'] * count_word
    count = 0

    for i in range(count_word):
      if i in secret_word:
          word[count] = i
          count += 1
      else:
          count += 1

    result = "".join(word)
    return result



def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    
    avaliable_letters = list(string.ascii_lowercase)

    for i in letters_guessed:
        if i in avaliable_letters:
            avaliable_letters.remove(i)
      

    result = "".join(avaliable_letters)
    return result



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #Implementar a função with helpp

    guesses_remaining = 10
    letters_guessed = []
    
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    
    while guesses_remaining > 0 and not has_player_won(secret_word, letters_guessed):
        print("--------------")
        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        
        guess = input("Please guess a letter: ").lower()
        
        # Lógica de Ajuda (Help)
        if with_help and guess == '!':
            if guesses_remaining < 3:
                print(f"Ops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
            else:
                guesses_remaining -= 3
                available = get_available_letters(letters_guessed)
                choose_from = [c for c in secret_word if c in available]
                if choose_from:
                    revealed_letter = random.choice(choose_from)
                    letters_guessed.append(revealed_letter)
                    print(f"Letter revealed: {revealed_letter}")
                    print(get_word_progress(secret_word, letters_guessed))
            continue
            
        # Tratamento de input inválido
        if not guess.isalpha() or len(guess) != 1:
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
            continue
            
        # Letra já utilizada
        if guess in letters_guessed:
            print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
            continue
            
        letters_guessed.append(guess)
        
        # Verificação do acerto ou erro
        if guess in secret_word:
            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
        else:
            if guess in ['a', 'e', 'i', 'o', 'u']:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")

    print("--------------")
    if has_player_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        unique_letters = len(set(secret_word))
        score = (guesses_remaining + 4 * unique_letters) + (3 * len(secret_word))
        print(f"Your total score for this game is: {score}")
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

