def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: a set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which the quadratic equations will be evaluated
    Evaluates one quadratic equation with coefficients a1, b1, c1, at x1.
    Evaluates another quadratic equation with coefficients a2, b2, c2, at x2.
    Prints the sum of the two evaluations. Returns nothing.
    """
    
    result1 = a1 * x1**2 + b1 * x1 + c1
    result2 = a2 * x2**2 + b2 * x2 + c2
    print(result1 + result2)
    return None

# Examples:
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)        # prints 6
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6 and then None