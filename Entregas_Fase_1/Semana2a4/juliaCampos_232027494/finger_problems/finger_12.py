def count_sqrts(nums_list):
    """
    nums_list: a list
    Assumes that nums_list only contains positive numbers and that there are no duplicates.
    Returns how many elements in nums_list are exact squares of elements in the same list, including itself.
    """
    q_squares = 0

    for i in nums_list:
        j = 0
        while j**2 < i:
            j+=1

        if (j**2 == i) and (j in nums_list):
            q_squares+=1

    return q_squares
# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3