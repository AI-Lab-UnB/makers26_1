import math
def count_sqrts(nums_list):
    counter = 0
    for num in nums_list:
        if math.sqrt(num) in nums_list:
            counter += 1
    return counter

print(count_sqrts([3,4,2,1,9,25])) # prints 3