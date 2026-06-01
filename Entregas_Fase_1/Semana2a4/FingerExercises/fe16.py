def flatten(L):
    flat_list = []
    for x in L:
        if isinstance(x, list):
            flat_list.extend(flatten(x))
        else:
            flat_list.append(x)
    return flat_list

    
# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]