n = int(input("Digite um número: "))
baixo = 0
alto = 1000
contador = 0
chute = (baixo + alto) // 2
while chute != n:
    if chute > n:
        alto = chute
    elif chute < n:
        baixo = chute
    chute = (baixo + alto) // 2
    contador += 1
print("Número de tentativas: ", contador)
print("Respota:", n )