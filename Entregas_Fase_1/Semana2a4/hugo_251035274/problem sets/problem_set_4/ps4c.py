import json
import ps4b 

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_4/story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_4/pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'Entregas_Fase_1/Semana2a4/hugo_251035274/problem sets/problem_set_4/words.txt'
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext, pads):
    word_list = load_words(WORDLIST_FILENAME)
    best_pad = None
    max_words = -1
    best_msg = None
    
    for pad in pads:
        decrypted_msg = ciphertext.decrypt_message(pad)
        
        text_msg = decrypted_msg.get_text()
        words = text_msg.split(" ")
        count = 0
        
        for word in words:
            if is_word(word_list, word):
                count += 1
        
        if count >= max_words:
            max_words = count
            best_pad = pad
            best_msg = decrypted_msg
    
    return best_msg
    


def decode_story():
    cipher_string = get_story_string()
    possible_pads = get_story_pads()
    
    encrypted = ps4b.EncryptedMessage(cipher_string)
    
    decrypted = decrypt_message_try_pads(encrypted, possible_pads)
    
    return decrypted.get_text()



if __name__ == '__main__':
    story = decode_story()
    print("Decoded story: ", story)