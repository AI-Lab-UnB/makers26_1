def all_positive(d):
    """
    d: a dictionary that maps int:list
    Assume that an element of d is a key k mapping to a value v (non-empty list).
    Return the sorted list of all k whose elements in v sum to a positive value.
    """

    result = []
    for k, v in d.items():
        if sum(v) > 0:
            result.append(k)
        result.sort()
    return result

# Examples:
d = {5: [2, -4], 2: [1, 2, 3], 1: [2]}
print(all_positive(d))  # prints [1, 2]