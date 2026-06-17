def flatten(L):
    result = [];
    for i in L:
        if type(i) == list:
            result.extend(flatten(i));
        else:
            result.append(i);
    return result;

L = [[1, 4, [6], 2], [[[3]], 2], 4, 5];
print(flatten(L)); 