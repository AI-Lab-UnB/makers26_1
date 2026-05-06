def all_true(n, Lf):
    resp = True
    for f in Lf:
        if not f(n):
            resp = False
            break
    return resp


is_even = lambda x: x % 2 == 0
is_positive = lambda x: x > 0

print(all_true(6, [is_even, is_positive])) # True
print(all_true(-2, [is_even, is_positive])) # False
    