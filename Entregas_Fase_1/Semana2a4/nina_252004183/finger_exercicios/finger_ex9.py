def dot_product(tA, tB):
    soma = 0

    for i in range(len(tA)):
        soma += tA[i] * tB[i]

    return (len(tA), soma)


tA = (1, 2, 3)
tB = (4, 5, 6)

print(dot_product(tA, tB))  