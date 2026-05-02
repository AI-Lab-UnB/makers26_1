def eval_quadratic(a, b, c, x):
    
    resultado = a * (x**2) + b * x + c
    
    return resultado

print(eval_quadratic(1, 1, 1, 1)) 

def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):

    resultado1 = (a1 * x1**2) + (b1 * x1) + c1
    
    resultado2 = (a2 * x2**2) + (b2 * x2) + c2
    
    print(resultado1 + resultado2)

two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)

print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1))