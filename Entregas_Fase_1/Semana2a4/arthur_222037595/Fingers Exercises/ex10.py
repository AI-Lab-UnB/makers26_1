# Finger Exercise - Lecture 10
# Name: Arthur Carvalho Leite
# Matrícula: 222037595

def all_true(n, Lf):
    """ n is an int
    Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True
    with n as a parameter. Otherwise returns False.
    """
    # passa n pra cada funcao da lista, se alguma retornar False ja para
    for f in Lf:
        if not f(n):
            return False
    return True
