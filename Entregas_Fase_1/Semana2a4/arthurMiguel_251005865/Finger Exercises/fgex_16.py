def flatten(L):
    temp = []
    for i in L:
        if type(i) == list:
            temp.extend(flatten(i))
        else:
            temp.append(i)
    return temp

L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L))