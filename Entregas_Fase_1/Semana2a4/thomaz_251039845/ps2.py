import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as f:
        wordlist = f.read().split()
    print(f"{len(wordlist)} words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)
def has_player_won(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
def get_word_progress(secret_word, letters_guessed):
    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "*"
    return result
def get_available_letters(letters_guessed):
    available = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter
    return available

def hangman(secret_word, with_help=False):
    guesses = 10
    letters_guessed = []

    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    while guesses > 0:
        print("-" * 20)
        print(f"You have {guesses} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            if with_help and guess == "!":
                # SISTEMA DE AJUDA
                possible = [c for c in set(secret_word) if c not in letters_guessed]
                if possible:
                    revealed = random.choice(possible)
                    letters_guessed.append(revealed)
                    guesses -= 3
                    print(f"Letter revealed: {revealed}")
                else:
                    print("No letters to reveal.")
                print(get_word_progress(secret_word, letters_guessed))
                continue

            print("Oops! That is not a valid letter.")
            print(get_word_progress(secret_word, letters_guessed))
            continue
        if guess in letters_guessed:
            print("Oops! You've already guessed that letter:")
            print(get_word_progress(secret_word, letters_guessed))
            continue

        letters_guessed.append(guess)
        if guess in secret_word:
            print("Good guess:", get_word_progress(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:",
                  get_word_progress(secret_word, letters_guessed))
            if guess in "aeiou":
                guesses -= 2
            else:
                guesses -= 1
        if has_player_won(secret_word, letters_guessed):
            print("-" * 20)
            print("Congratulations, you won!")
            return
    print("-" * 20)
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman(secret_word, with_help=True)