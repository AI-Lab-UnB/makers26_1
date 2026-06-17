def dot_product(tA, tB):
        soma = 0

        for i in range(len(tA)):
            produto = tA[i] * tB[i]
            soma += produto

        return(len(tA), soma)


tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB))