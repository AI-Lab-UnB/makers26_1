def all_true(n, Lf):
    """
    n is an integer
    Lf is a list of functions that each take an integer and return a boolean
    Returns True if each function in Lf returns True when called
    with n as a parameter. Otherwise, returns False.
    """
    
    return all(f(n) for f in Lf)

# Examples:
print(all_true(10, [lambda x: x % 2 == 0]))  # prints True
