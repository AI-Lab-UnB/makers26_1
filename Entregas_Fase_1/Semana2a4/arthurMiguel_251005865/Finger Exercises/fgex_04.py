i = 1
N = int(input("Escolha um número: "))
while i**3 < N:
    i += 1   
    if i**3 == N:
        print(i)
    else:
        print('erro')