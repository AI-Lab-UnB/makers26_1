def remove_and_sort(Lin, k):
    """
    Lin is a list of integers
    k is an integer >= 0
    Modifies Lin by removing the first k elements and
    then sorts the remaining elements in ascending order.
    If there are not enough elements to remove, Lin is modified to an empty list.
    Returns nothing.
    """

    del Lin[:k]
    Lin.sort()


# Examples:
L = [1, 6, 3]
k = 1
remove_and_sort(L, k)
print(L)  # prints [3, 6]