s1 = str(input("Digite uma string: "))
s2 = str(input("Digite outra string: "))

def same_chars(s1,s2):
    for c in s1:
        if c in s2:
            return True
            break
        else:
            return False

print(same_chars(s1,s2))