def all_true(n, Lf):
    """ n is an int
    Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called
    with n as a parameter. Otherwise returns False.
    """

    flag = True
    for f in Lf:
        if not f(n):
            flag = False
            break
        return flag


 # Your code here
# Examples:
all_true() # prints 6