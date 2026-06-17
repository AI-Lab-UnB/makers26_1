def tricky_f(L, L2):
    inL = False
    for e1 in L:
        if e1 in L2:
            inL = True

    inL2 = False
    for e2 in L2:
        if e2 in L:
            inL2 = True

    return inL and inL2