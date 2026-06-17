def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which the quadratic equation will be evaluated.
    Returns the value of the quadratic equation ax² + bx + c.
    """
    return a * x**2 + b * x + c

# Examples:
print(eval_quadratic(1, 1, 1, 1))  # prints 3