def sum_str_lengths(L):
    sum = 0
    for s in L:
        if isinstance(s, list):
            sum += sum_str_lengths(s)
        elif isinstance(s, str):
            sum += len(s)
        else:
            raise ValueError
    return sum 

print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError