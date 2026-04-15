def same_chars(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    for j in s2:
        if j not in s1:
            return False
    return True
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False