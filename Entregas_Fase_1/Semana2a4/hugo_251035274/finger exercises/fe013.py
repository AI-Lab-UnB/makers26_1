def sum_str_lengths(L):
    total = 0
    for ele in L:
        if type(ele) == str:
            total += len(ele)
        elif type(ele) == list:
            for i in ele:
                if type(i) == str:
                    total += len(i)
                else:
                    raise ValueError
        else:
            raise ValueError
        
    return total


print(sum_str_lengths(["abcd", ["e", "fg"]])) # prints 7
print(sum_str_lengths([12, ["e", "fg"]])) # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]])) # raises ValueError 