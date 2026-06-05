def dot_product(tA, tB):
    length = len(tA)
    total = 0
    for i in range(length):
        total += tA[i] * tB[i]
    return (length, total)

tA = (1, 2, 3)
tB = (4, 5, 6)
print(dot_product(tA, tB))  # prints (3, 32)