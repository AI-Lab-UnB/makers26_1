def count_sqrts(nums_list):
    """
    nums_list: a list
    Assume that nums_list contains only positive numbers and without duplicates.
    Return how many elements of nums_list are exact squares of other
    elements of the same list, including itself.
    """

    count = 0
    for i in range(len(nums_list)):
        for j in range(len(nums_list)):
            if nums_list[i] == nums_list[j] ** 2:
                count += 1
    return count

# Examples:
print(count_sqrts([3, 4, 2, 1, 9, 25]))  # prints 3