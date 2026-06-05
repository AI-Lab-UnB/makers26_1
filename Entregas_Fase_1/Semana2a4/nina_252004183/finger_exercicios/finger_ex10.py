def all_true(n, lf):
    return all(func(n) for func in lf)