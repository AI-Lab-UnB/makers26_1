
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
        if letter not in letters_guessed:
            return False
        return
    
def get_word_progress(secret_word, letters_guessed):
    progress = ''
    for letter in secret_word:
        if letter in letters_guessed:
            progress += letter
        else:
            progress += '*'
    return progress
    

def get_available_letters(letters_guessed):
    available = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available += letter
    return available

def hangman(secret_word, with_help):
    print(f'Estou pensando em uma palavra que tem {len(secret_word)} letras')
    tentativas = 10
    vogais = 'aeiou'
    letters_guessed = []
    while not has_player_won(secret_word, letters_guessed) and tentativas >0: 
        print(f'Você ainda tem {tentativas} tentativas')
        print(f'As letras ainda disponiveis são: {get_available_letters(letters_guessed)}')
        chute = str(input("Chute uma letra ou digite ! se quiser ajuda: ")).lower()
        if chute == '!' and with_help:
            if tentativas >=3:
                tentativas -=3
                choose_from = ''
                for letter in secret_word:
                    if letter in get_available_letters(letters_guessed):
                        choose_from+= letter
                new = random.randint(0, len(choose_from)-1)
                revealed_letter = choose_from[new]
                letters_guessed.append(revealed_letter)
                print(get_word_progress(secret_word, letters_guessed))
            else:
                print("Você não possui tentativas suficientes")
        elif chute not in string.ascii_lowercase:
            print("Chute invalido! Lembre-se você deve chutar apenas letras")
        elif chute in letters_guessed:
            print("Opa, você já chutou essa letra")
        elif chute in vogais and chute not in secret_word :
            tentativas -=2
            letters_guessed.append(chute)
            print(get_word_progress(secret_word, letters_guessed))
        elif chute not in vogais and chute not in secret_word:
            tentativas -=1
            letters_guessed.append(chute)
            print(get_word_progress(secret_word, letters_guessed))
        else:
            letters_guessed.append(chute)
            print(get_word_progress(secret_word, letters_guessed))
    if has_player_won(secret_word, letters_guessed):
        score = (tentativas +4 * len(set(secret_word))) + (3 * len(secret_word))
        print(f"Parabéns você venceu!\n Sua pontuação foi: {score}")
    else:
        print(f"Infelizmente você ficou sem mais tentantivas.\n A palavra era {secret_word}")



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
    
