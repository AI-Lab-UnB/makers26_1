def all_positive(d):
    L = []
    for i,j in d.items():
        if sum(j) > 0:
            L.append(i)
    return sorted(L)