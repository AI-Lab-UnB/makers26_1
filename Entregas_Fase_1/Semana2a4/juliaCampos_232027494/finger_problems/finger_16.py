def flatten(L):
    """ 
    L: a list 
    Returns a copy of L, which is a flattened version of L 
    """
    final_list = []
    for i in L:
        if isinstance(i,list):
            final_list.extend(flatten(i))
        else:
            final_list.append(i)
    
    return final_list

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]