def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    # Your code here

    for char in s1:
        
        if char not in s2:
            return False
        
        else:
            for char2 in s2:
                
                if char2 not in s1:
                    return False
                
                else:
                    return True
            
    

 
# Examples:
print(same_chars("abc", "cab")) # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa")) # prints False
print(same_chars("abcabc", "cabz")) # prints False