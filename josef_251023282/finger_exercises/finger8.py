def same_chars(s1, s2):
    for i in range(len(s1)):
        letra = s1[i]

        if letra not in s2:
            return False
        
    for j in range(len(s2)):
        if s2[j] not in s1:
            return False
    
    return True

print(same_chars("abc", "cab"))     
print(same_chars("abccc", "caaab")) 
print(same_chars("abcd", "cabaa"))  
print(same_chars("abcabc", "cabz"))

