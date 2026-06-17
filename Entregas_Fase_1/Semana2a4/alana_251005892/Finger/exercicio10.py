def all_true(n, Lf):
    for i in Lf:
        if i(n) == False:
            return False
    return True
def positivo(k):
    resul = k>0
    return resul
def par(l):
    resul = (l%2)==0
    return resul
n = int(input("digite o numero a ser testado nas funções "))
Lf = [positivo, par]
print(all_true(n,Lf))