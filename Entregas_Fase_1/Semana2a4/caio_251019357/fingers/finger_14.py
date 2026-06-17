
def keys_with_value(aDict, target):

    list_aux = []

    for key in aDict :

        if aDict[key] == target:

            list_aux.append(key)

    return list_aux


# Examples:
aDict = {1:2, 2:4, 5:2}
target = 2   
print(keys_with_value(aDict, target)) # prints the list [1,5]



    
def all_positive(d):

    list_aux = []

    for key in d:

        sum = 0

        for num in d[key] :

            sum += num

        if sum > 0:

            list_aux.append(key)

    sort_list = sorted(list_aux)

    return sort_list




# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]