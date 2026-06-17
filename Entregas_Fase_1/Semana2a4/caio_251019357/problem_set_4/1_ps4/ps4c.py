# Problem Set 4C
# Name:
# Collaborators:

import json
import ps4b # Importing your work from Part B

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
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    list_words = load_words(WORDLIST_FILENAME)

    count_correct_words_max = 0
    best_pad = []
    plaintext_true = ""
    


    for pad in pads:

        count_correct_words = 0

        # object = ps4b.EncryptedMessage(ciphertext)

        object_plaintext = ciphertext.decrypt_message(pad)

        plaintext = object_plaintext.input_text

        list_plaintext = plaintext.split()

        for word in list_plaintext:

            verification_word = is_word( list_words , word)

            if verification_word:
                count_correct_words += 1
  
        if count_correct_words >= count_correct_words_max:

            count_correct_words_max = count_correct_words
            best_pad = pad
            plaintext_true = plaintext

        

    plaintext_object = ps4b.PlaintextMessage(plaintext_true, best_pad)
    # print(plaintext_object.input_text)
    # print(plaintext_object.pad)
    return plaintext_object
        
        
       




def decode_story():
    '''
    Write your code here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''

    story = get_story_string()
    pads_initial = get_story_pads()

    encrypted_object = ps4b.EncryptedMessage(story)
    plaintext_object = decrypt_message_try_pads(encrypted_object, pads_initial)

    return plaintext_object.input_text



if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
    story = decode_story()
    print("Decoded story: ", story)

    # decrypt_message_try_pads("8fxvr6/C'9 _^[G4uXCN", [[51, 32, 46, 74, 57, 81, 50, 58, 12, 78, 24, 76, 34, 66, 50, 60, 77, 5, 86, 75], [69, 37, 11, 94, 53, 18, 61, 72, 7, 45, 69, 88, 5, 58, 31, 56, 31, 44, 67, 41], [27, 35, 38, 26, 2, 84, 86, 85, 77, 40, 89, 80, 41, 78, 86, 5, 39, 50, 18, 43], [30, 12, 35, 7, 86, 43, 81, 87, 43, 57,
    #             10, 26, 8, 31, 83, 56, 94, 83, 94, 33], [68, 85, 19, 19, 9, 52, 34, 35, 67, 48, 30, 76, 74, 33, 40, 24, 87, 38, 26, 46], [56, 34, 14, 73, 67, 35, 15, 17, 1, 16, 51, 7, 28, 31, 46, 26, 68, 84, 21, 91]])
    
    
    # decrypt_message_try_pads('05<Nvv`\\.8_0qvh?b?', [[42, 27, 38, 56, 8, 70, 7, 45, 17, 54, 51, 53, 69, 50, 40, 86, 67, 73], [59, 44, 50, 90, 86, 13, 13, 60, 64, 46, 70, 74, 45, 86, 5, 93, 15, 57], [43, 94, 13, 15, 33, 72, 27, 94, 28, 20, 54, 74, 67, 54, 7, 86, 70, 57], [25, 28, 94, 37, 58, 10, 52, 63, 30,
    #             92, 72, 43, 34, 4, 3, 56, 73, 22], [72, 54, 52, 43, 47, 36, 67, 93, 16, 8, 25, 23, 22, 28, 59, 10, 2, 54], [89, 81, 94, 89, 23, 26, 53, 44, 31, 78, 50, 45, 71, 82, 79, 76, 22, 8]])
    
    # decrypt_message_try_pads('ThiS iS MixED cASe', [59, 44, 50, 90, 86, 13, 13, 60, 64, 46, 70, 74, 45, 86, 5, 93, 15, 57])
    # pass

