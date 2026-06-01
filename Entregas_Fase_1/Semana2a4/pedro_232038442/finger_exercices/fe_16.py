def flatten(L):
    """
    L: a list
    Returns a copy of L completely "flattened" (without nested lists)
    """
    result = []
    for element in L:
        if isinstance(element, list):
            for subelement in element:
                if isinstance(subelement, list):
                    result.extend(flatten(subelement))
                else:
                    result.append(subelement)
        else:
            result.append(element)
    return result


# Examples:
L = [[1, 4, [6], 2], [[[3]], 2], 4, 5]
print(flatten(L))  # prints [1, 4, 6, 2, 3, 2, 4, 5]