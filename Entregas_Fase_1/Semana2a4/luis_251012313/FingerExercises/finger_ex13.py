def sum_str_lengths(L):
    total = 0;
    for i in L:
        if type(i) == str:
            total += len(i);
        elif type(i) == list:
            for e in i:
                if type(e) == str:
                    total += len(e);
                else:
                    raise ValueError;
        else:
            raise ValueError;
    return total;

print(sum_str_lengths(["abcd", ["e", "fg"]]));
print(sum_str_lengths([12, ["e", "fg"]]));
print(sum_str_lengths(["abcd", [3, "fg"]]));