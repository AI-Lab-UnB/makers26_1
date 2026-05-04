import math
N = int(input("insira um numero inteiro: "))
raiz = math.cbrt(N)
contador = 0
while ((contador** 3) < N):
    contador = contador + 1
    if ((contador**3) == N):
        print(raiz)
    elif ((contador**3)<N):
        contador = contador + 1
    else:
        print("error")