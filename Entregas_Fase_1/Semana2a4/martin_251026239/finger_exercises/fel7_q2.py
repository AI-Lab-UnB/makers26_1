def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    resp1 = a1 * pow(x1, 2) + b1 * x1 + c1
    resp2 = a2 * pow(x2, 2) + b2 * x2 + c2

    print(resp1 + resp2)

two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) # prints 6
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6 then None