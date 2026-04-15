def lf(x):
    lf1(x)
    lf2(x)
    lf3(x)

    print(lf1)

def lf1(x):
    if x.is_integer():
        return True
    else:
        return False
def lf2(x):
    if x.is_integer():
        return True
    else:
        return False

def lf3(x):
    if x.is_integer():
        return True
    else:
        return False


def all_true(n):
    n = int(input("Verifique se é um número"))
    lf(n)

n = int(input("Verifique se é um número"))

all_true(n)
