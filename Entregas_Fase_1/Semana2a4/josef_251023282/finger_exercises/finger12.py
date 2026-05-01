def count_sqrts(nums_list):
    cont = 0

    for i in range(len(nums_list)):
        num = nums_list[i]
        for j in range(len(nums_list)):
            n = nums_list[j]
            
            if n**2 == num:
                cont += 1
                break 

    return cont

print(count_sqrts([3, 4, 2, 1, 9, 25])) 