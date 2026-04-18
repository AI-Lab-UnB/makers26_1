def dot_product(t1, t2):
    soma = 0
    for i in range(len(t1)):
        soma += t1[i] * t2[i]
    return [len(t1), soma]

tA = (1, 2, 3)
tB = (4, 5, 6)
print(dot_product(tA, tB)) # prints (3,32)