def same_chars(s1, s2):
    return set(s1) == set(s2);

print(same_chars("hello", "oellh")); # print True
print(same_chars("abcc", "bacc"));   # print True
print(same_chars("abc", "def"));     # print False
print(same_chars("abcabc", "cabz")); # print False