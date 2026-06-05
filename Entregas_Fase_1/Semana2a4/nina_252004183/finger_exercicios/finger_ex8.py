def same_chars(s1, s2):
    return set(s1) == set(s2)


print(same_chars("abc", "cab"))      
print(same_chars("abccc", "caaab"))  
print(same_chars("abcd", "cabaa"))   
print(same_chars("abcabc", "cabz"))  