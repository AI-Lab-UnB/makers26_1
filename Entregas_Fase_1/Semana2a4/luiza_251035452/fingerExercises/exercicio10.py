def all_true(n, Lf):
    for f in Lf:
        if not f(n):
            return False
    return True

# funções de teste
def maior_que_zero(x):
    return x > 0

def par(x):
    return x % 2 == 0

Lf = [maior_que_zero, par]

# examples
print(all_true(4, Lf))  
print(all_true(5, Lf))  
