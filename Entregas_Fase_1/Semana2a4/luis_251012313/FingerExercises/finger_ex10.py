def all_true(n, lf):
    for i in range(n):
        if not lf(i):
            return False
    return True;

def f1 (n):
    return True if n > 0 else False;
def f2 (n):
    return True if n % 2 == 0 else False;

lf = lambda x: f1(x) and f2(x);

print(all_true(3, lf)); # print False, porque 0 é par, mas não é maior que 0.
print(all_true(2, lf)); # print True, porque 2 é par e é maior que 0.
print(all_true(-4, lf));# print False, porque -4 é par, mas não é maior que 0.