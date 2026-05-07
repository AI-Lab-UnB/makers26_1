class EncryptedMessageDecoder(EncryptedMessage):
    def __init__(self, input_text):
        super().__init__(input_text)

    def decrypt_message_try_pads(self, pads, wordlist):
        best_plaintext = ""
        max_valid_words = -1
        
        for pad in pads:
            decrypted_text = self.decrypt_message(pad)
            words = decrypted_text.split(' ')
            
            valid_words = 0
            for word in words:
                if is_word(wordlist, word):
                    valid_words += 1
                    
            if valid_words >= max_valid_words:
                max_valid_words = valid_words
                best_plaintext = decrypted_text
                
        return best_plaintext

def decode_story(wordlist):
    ciphertext = get_story_string()
    pads = get_story_pads()
    
    decoder = EncryptedMessageDecoder(ciphertext)
    return decoder.decrypt_message_try_pads(pads, wordlist)