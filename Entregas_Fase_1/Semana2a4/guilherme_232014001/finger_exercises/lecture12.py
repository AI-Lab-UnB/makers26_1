def count_sqrts(nums_list):
    count = 0
    for num in nums_list:
        if num ** 0.5 in nums_list:
            count += 1
    return count

print(count_sqrts([3, 4, 2, 1, 9, 25]))  # prints 3