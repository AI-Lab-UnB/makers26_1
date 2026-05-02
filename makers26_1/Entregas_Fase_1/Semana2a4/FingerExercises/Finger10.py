def all_true(n,Lf):
    booleanFlag = True
    for f in Lf:
        if not f(n):
            booleanFlag=False
    return booleanFlag

