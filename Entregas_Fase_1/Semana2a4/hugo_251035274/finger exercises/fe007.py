def eval_quadratic(a, b, c, x):
    result = (a * x ** 2) + b * x + c
    return result

def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    result1 = eval_quadratic(a1, b1, c1, x1)
    result2 = eval_quadratic(a2, b2, c2, x2)
    
    sum = result1 + result2
    
    print(sum) 


print(eval_quadratic(1, 1, 1, 1)) # 3
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) # 6