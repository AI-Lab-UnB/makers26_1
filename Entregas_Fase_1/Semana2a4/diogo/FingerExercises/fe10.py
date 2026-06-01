def all_true(n, Lf):
    result = True
    for func in Lf:
        if(not func(n)):
            result = False
            break
    return result
