def all_true(n, Lf):
    for func in Lf:
        if not func(n):
            return False
    return True

# Examples:
print(all_true(4, [lambda x: x > 0, lambda x: x % 2 == 0]))  # prints True
print(all_true(3, [lambda x: x > 0, lambda x: x % 2 == 0]))  # prints False