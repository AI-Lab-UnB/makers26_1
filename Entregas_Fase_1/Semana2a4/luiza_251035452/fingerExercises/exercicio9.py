def dot_product(tA, tB):
    tamanho = len(tA)  
    
    soma = 0
    for i in range(tamanho):
        soma += tA[i] * tB[i] 
    
    return (tamanho, soma)


# examples
tA = (1, 2, 3)
tB = (4, 5, 6)
print(dot_product(tA, tB))  # (3, 32)