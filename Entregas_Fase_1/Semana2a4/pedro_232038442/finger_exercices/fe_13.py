def sum_str_lengths(L):
    """
    L is a non-empty list containing:
    * elements of type string, or
    * non-empty sublists of elements of type string
    Return the sum of the lengths of all strings in L and
    the lengths of the strings in the sublists of L.
    If L contains an element that is not a string or list, or if the sublists
    of L contain an element that is not a string, raise a ValueError.
    """

    total_length = 0
    for element in L:
        if isinstance(element, str):
            total_length += len(element)
        elif isinstance(element, list):
            for sub_element in element:
                if isinstance(sub_element, str):
                    total_length += len(sub_element)
                else:
                    raise ValueError()
        else:
            raise ValueError()
    return total_length

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))       # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))           # throws ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))         # throws ValueError