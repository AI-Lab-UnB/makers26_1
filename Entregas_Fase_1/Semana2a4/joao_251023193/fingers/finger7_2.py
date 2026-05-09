def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    Prints the sum of the two evaluations. Does not return anything.
    """
    # Your code here

    q1 = ((a1*x1**2) + (b1*x1) + (c1))
    q2 = ((a2*x2**2) + (b2*x2) + (c2))
    print(q1 + q2)
 
# Examples:
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) # prints 6
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6 then None