
def all_true(n, Lf):

    for func in Lf :

        if not func(n):
            return False
        
    return True


print(all_true())