def all_true(n, Lf):

    for funcao in Lf:
        if funcao(n) == False:
            return False

    return True

def par(x): return x % 2 == 0
def maior_que_cinco(x): return x > 5

testes = [par, maior_que_cinco]

print(all_true(6, testes)) 
print(all_true(4, testes))  