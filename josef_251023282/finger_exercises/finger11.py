def remove_and_sort(Lin, k):
    
    if k >= len(Lin):
        Lin.clear()
        return 
    else:
        Lin[:] = Lin[k:]

    
    n = len(Lin)
    for i in range(n):
        for c in range(0, n - i - 1):
            if Lin[c] > Lin[c + 1]:
                temp = Lin[c]
                Lin[c] = Lin[c + 1]
                Lin[c + 1] = temp

L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)