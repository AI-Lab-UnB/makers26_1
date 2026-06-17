def flatten(L):
    """
    L: a list
    Returns a copy of L, which is a flattened version of L
    """
    # Your code here
 
    new_list = []
    for i in L:
        if type(i) == list:
            new_list.extend(flatten(i))
        
        else:
            new_list.append(i)
    return new_list

 
# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]