def keys_with_value(aDict, target):
    resp = []
    
    for ele in aDict:
        if aDict[ele] == target:
            resp.append(ele)
    resp.sort()
    
    return resp

def all_positive(d):
    resp = []
    
    for ele, li in d.items():
        if sum(li) > 0:
            resp.append(ele)
    resp.sort()
    
    return resp


aDict = {1:2, 2:4, 5:2}
target = 2   
print(keys_with_value(aDict, target)) # prints the list [1,5]

d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]
