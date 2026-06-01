def same_chars(s1, s2):
    hashmapS1 = {}
    hashmapS2 = {}
    for char in s1:
        hashmapS1[char] = 0
    for char in s2:
        hashmapS2[char] = 0
        
    merge = hashmapS1 | hashmapS2
    
    if(len(hashmapS1) != len(merge) or len(hashmapS2) != len(merge) ):
        return False
    return True

print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False