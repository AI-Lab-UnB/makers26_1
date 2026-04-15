def keys_with_value(aDict, target):
    resp = []
    
    for ele in aDict:
        if aDict[ele] == target:
            resp.append(ele)

    return resp


aDict = {1:2, 2:4, 5:2}
target = 2   
print(keys_with_value(aDict, target)) # prints the list [1,5]
