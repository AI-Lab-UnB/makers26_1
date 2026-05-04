def dot_product(tA, tB):

    sum = 0
    for i in range(len(tA)):
        sum += (tA[i]*tB[i])

    return (len(tA), sum)    
tA = (1, 2, 3) 
tB = (4, 5, 6) 
print(dot_product(tA, tB)) # prints (3,32) 

