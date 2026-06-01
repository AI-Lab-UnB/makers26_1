def flatten(L):
    result = []
    for element in L:
        if type(element) == list:
            result += flatten(element)
        else:
            result.append(element)
    return result

L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L))  # prints [1, 4, 6, 2, 3, 2, 4, 5]