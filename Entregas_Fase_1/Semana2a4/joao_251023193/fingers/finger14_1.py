def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    # Your code here
    
    sorted_list = []
    for i in aDict.keys():
        if aDict[i] == target:
            sorted_list.append(i)
    
    sorted_list.sort()
    return sorted_list
    
    
# Examples:
aDict = {1:2, 2:4, 5:2}
target = 2
print(keys_with_value(aDict, target)) # prints the list [1,5]