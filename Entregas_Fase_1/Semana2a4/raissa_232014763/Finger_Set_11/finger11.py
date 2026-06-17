def remove_and_sort(Lin, k):
    del Lin[:k]
    Lin.sort()

# Examples:
L = [1, 6, 3]
k = 1
remove_and_sort(L, k)
print(L)  # prints [3, 6]