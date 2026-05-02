def dot_product(tA, tB):
    soma = 0
    for i in range(len(tA)):
        soma += tA[i] * tB[i]
        
    return (len(tA), soma)

numeros = list(map(int, input().split()))
metade = len(numeros)//2
tA = tuple(numeros[:metade])
tB = tuple(numeros[metade:])
print(dot_product(tA, tB))
