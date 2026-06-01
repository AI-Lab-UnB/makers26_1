def sum_str_lengths(l):
    soma = 0
    for i in l:
        if type(i) == str:
            soma += len(i)
        elif type(i) == list:
            for j in i:
                if type(j) == str:
                    soma += len(j)
                else:
                    raise ValueError
        else:
            raise ValueError

    return soma
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]]))    # raises ValueError