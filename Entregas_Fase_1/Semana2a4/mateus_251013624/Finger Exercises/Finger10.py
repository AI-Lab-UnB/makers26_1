def all_true(n,lf):
    v = True
    for i in lf:
        if not i(n):
            v = False
            break
    return v
def f1(n):
    return True if n> 0 else False
def f2(n):
    return True if n %2 == 0 else False
lf = [f1, f2]

print(all_true(3, lf)) # False
print(all_true(2, lf)) #True
print(all_true(-2, lf))  #False
