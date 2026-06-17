def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """

    result = []
    
    for item in L:
        if isinstance(item, list):
            result.extend(flatten(item))  # achata recursivamente
        else:
            result.append(item)
    
    return result

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]
