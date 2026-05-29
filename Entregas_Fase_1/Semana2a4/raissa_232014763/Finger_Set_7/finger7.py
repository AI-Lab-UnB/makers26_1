def eval_quadratic(a, b, c, x):
    return a * x**2 + b * x + c

print(eval_quadratic(1, 1, 1, 1))  # prints 3


def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    return eval_quadratic(a1, b1, c1, x1) + eval_quadratic(a2, b2, c2, x2)

print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1))  # prints 6