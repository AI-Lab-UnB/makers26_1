def counting_squares(nums_list):
    contador = 0
    for i in nums_list:
        for j in range(len(nums_list)):
            if i ** 2 == j:
                contador += 1
    if contador > 0:
        contador += 1
        print(contador)
    else:
        print(0)
counting_squares([3,4,2,1,9,25])