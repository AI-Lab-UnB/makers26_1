def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that the keys and values of aDict are integers or strings.
    Return a sorted list of the keys of aDict whose value is equal to target.
    If aDict does not contain the value target, return an empty list.
    """
    list_of_keys = []
    for key, value in aDict.items():
        if value == target:
            list_of_keys.append(key)
    list_of_keys.sort()
    return list_of_keys

# Examples:
aDict = {1: 2, 2: 4, 5: 2}
target = 2
print(keys_with_value(aDict, target))  # prints [1, 5]