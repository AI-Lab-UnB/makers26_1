def dot_product(tA, tB):
    tA_length = len(tA)
    sum = 0
    
    for i in range(tA_length):
        sum += tA[i] * tB[i]
    
    new_tuple = (tA_length, sum)
    return new_tuple


tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)