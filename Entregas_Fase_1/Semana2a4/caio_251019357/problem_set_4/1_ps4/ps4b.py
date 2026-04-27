# Problem Set 4B
# Name:
# Collaborators:

import random
import copy


class Message(object):
    def __init__(self, input_text):
        
        self.input_text = input_text
    

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''Message('{self.get_text()}')'''
    


    def get_text(self):
        
        return self.input_text
    
    

    def shift_char(self, char, shift):
        '''
        Used to shift a character as described in the pset handout

        char (string): the single character to shift.
                    ASCII value in the range: 32<=ord(char)<=126
        shift (int): the amount to shift char by

        Returns: (string) the shifted character with ASCII value in the range [32, 126]
        '''
        ascii_char = ord(char)

        char_encryption = chr((ascii_char - 32 + shift) % 95 + 32)


        return char_encryption




    def apply_pad(self, pad):
        '''
        Used to calculate the ciphertext produced by applying a one time pad to the message text.
        For each character in the text at index i shift that character by
            the amount specified by pad[i]

        pad (list of ints): a list of integers used to encrypt the message text
                        len(pad) == len(the message text)

        Returns: (string) The ciphertext produced using the one time pad
        '''

        ciphertext = ""

        for i , letter in enumerate(self.input_text):

            char_encryption = self.shift_char(letter, pad[i])

            ciphertext += char_encryption

        return ciphertext




class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        pad (list of ints OR None): the pad to encrypt the input_text or None if left empty
            if pad is not None then len(pad) == len(self.input_text)

        A PlaintextMessage object inherits from Message. It has three attributes:
            the message text
            the pad (list of integers, determined by pad
                or generated randomly using self.generate_pad() if pad is None)
            the ciphertext (string, input_text encrypted using the pad)
        '''
        super().__init__(input_text)

        if pad is None :
            
            self.pad = self.generate_pad()

        else :

            self.pad = copy.deepcopy(pad)



    def __repr__(self):
    
        return f'''PlaintextMessage('{self.get_text()}', {self.get_pad()})'''




    def generate_pad(self):
        
        new_pad = []

        for i in range(len(self.input_text)):

            n = random.randint(0, 110)

            new_pad.append(n)

        return new_pad





    def get_pad(self):
        
        return copy.deepcopy(self.pad)



    def get_ciphertext(self):
        '''
        Used to access the ciphertext produced by applying pad to the message text

        Returns: (string) the ciphertext
        '''
        
        pad = self.get_pad()

        ciphertext = self.apply_pad(pad)

        return ciphertext



    def change_pad(self, new_pad):
        '''
        Changes the pad used to encrypt the message text and updates any other
        attributes that are determined by the pad.

        new_pad (list of ints): the new one time pad that should be associated with this message.
            len(new_pad) == len(the message text)

        Returns: nothing
        '''
        
        self.pad = copy.deepcopy(new_pad)

        self.get_ciphertext()


class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the ciphertext of the message

        an EncryptedMessage object inherits from Message. It has one attribute:
            the message text (ciphertext)
        '''
        super().__init__(input_text)


    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''EncryptedMessage('{self.get_text()}')'''

    def decrypt_message(self, pad):
        '''
        Decrypts the message text that was encrypted with pad as described in the writeup

        pad (list of ints): the new one time pad used to encrypt the message.
            len(pad) == len(the message text)

        Returns: (PlaintextMessage) the decrypted message (containing the pad)
        '''
        pad_descryp = []

        for i in range(len(pad)):

            new_pad = pad[i] * -1

            pad_descryp.append(new_pad)

        plaintext = self.apply_pad(pad_descryp)

        return PlaintextMessage(plaintext, pad)


    

text1 = 'testing message'
msg1 = Message(text1)

print(msg1.get_text())