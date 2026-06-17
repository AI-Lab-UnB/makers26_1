def keys_with_value(aDict, target):
    result = []
    for key in aDict:
        if aDict[key] == target:
            result.append(key)
    return sorted(result)

aDict = {1:2, 2:4, 5:2}
target = 2
print(keys_with_value(aDict, target))  # prints [1, 5]

def all_positive(d):
    result = []
    for key in d:
        if sum(d[key]) > 0:
            result.append(key)
    return sorted(result)

d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))  # prints [1, 2]