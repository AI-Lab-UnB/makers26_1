
def remove_and_sort(Lin, k):

    if k == 0:
        pass
    else :
        
        del Lin[0:k]

    Lin.sort()


# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]     