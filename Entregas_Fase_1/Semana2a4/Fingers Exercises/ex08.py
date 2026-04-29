# Finger Exercise - Lecture 8
# Name: Arthur Carvalho Leite
# Matrícula: 222037595

def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    # checa se todo char de s1 ta em s2
    for c in s1:
        if c not in s2:
            return False
    # checa o contrario tambem
    for c in s2:
        if c not in s1:
            return False
    return True
