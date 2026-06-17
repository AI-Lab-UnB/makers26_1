
def dot_product(ta, tb):

    list_aux = []

    for i in range(len(ta)):

        new_element = ta[i] * tb[i]

        list_aux.append(new_element)

    sum_final = sum(list_aux)

    return (len(ta) ,sum_final)


# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)