def flatten(L):
    resp = []
    for ele in L:
        if type(ele) == list:
            resp.extend(flatten(ele))
        else:
            resp.append(ele)
    return resp


L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]