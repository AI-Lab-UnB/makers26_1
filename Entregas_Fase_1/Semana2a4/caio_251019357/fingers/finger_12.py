
def count_sqrts(nums_list) :

    count = 0

    for num_i in nums_list:

        for num_j in nums_list:

            if num_j ** 2 == num_i:

                count += 1

                break

    return count


# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3
