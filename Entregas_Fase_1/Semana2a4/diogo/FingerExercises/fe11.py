def remove_and_sort(Lin : list, k):
    while len(Lin) != 0 and k != 0:
        Lin.pop(0)
        k -= 1
        
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]