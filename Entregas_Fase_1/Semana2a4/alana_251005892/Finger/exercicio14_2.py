def all_positive(d):
    los = []
    for i,k in d.items():
        soma = sum(k)
        if soma >0:
            los.append(i)
    new = sorted(los)
    return new
d = {5:[2, -5], 3:[4,2], 9:[4, 7, 1], 1:[-4, 3]}
print(all_positive(d))