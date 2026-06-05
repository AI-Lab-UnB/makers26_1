def sum_str_lengths(L):
    total = 0
    for element in L:
        if type(element) == str:
            total += len(element)
        elif type(element) == list:
            for item in element:
                if type(item) != str:
                    raise ValueError
                total += len(item)
        else:
            raise ValueError
    return total

print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError