def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns True if every character in s1 is also in s2, and vice versa.
    If a character exists in only one of the strings, returns False.
    """
    
    set1 = set(s1)
    set2 = set(s2)
    return set1 == set2

# Examples:
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False