
def same_chars(text_1, text_2):

    for char in text_1:

        if char in text_2:
            pass

        else:
            return False
        

    for char in text_2:

        if char in text_1:
            pass

        else:
            return False
        
        
    return True

# Examples:
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False