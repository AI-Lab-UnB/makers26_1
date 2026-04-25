import string

def has_player_won(secret_word, letters_guessed):

    for char in secret_word:
        if char not in letters_guessed:
            return False;

    return True;

def get_word_progress(secret_word,letters_guessed):

    result = ""

    for char in secret_word:
        if char not in letters_guessed:
            result+='*'
        else:
            result+=char

    return result


def get_available_letters(secret_word,letters_guessed):
    
    alphabet = string.ascii_lowercase
    avilable_letters=""

    for char in alphabet:
        if char not in letters_guessed:
            avilable_letters+=char

    return avilable_letters