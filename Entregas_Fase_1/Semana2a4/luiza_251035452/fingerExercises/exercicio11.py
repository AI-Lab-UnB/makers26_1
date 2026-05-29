def remove_and_sort(Lin, k):
    # remove os k primeiros elementos
    del Lin[:k]
    
    # ordena o restante
    Lin.sort()


# examples
L = [1, 6, 3]
k = 1
remove_and_sort(L, k)
print(L)   