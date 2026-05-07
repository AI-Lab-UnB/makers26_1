def sum_str_lengths(L):
    temp = 0
    for i in L:
        if type(i) == int or type(i) == float:
            raise ValueError
        elif type(i) == list:
            for j in i:
                for k in j:
                    temp += 1
        else:
           for p in i:
            temp += 1
    print(temp)

L = ["abcd", ["e", "fg"]]
K = [12, ["e", "fg"]]

sum_str_lengths(L)
sum_str_lengths(K)
            