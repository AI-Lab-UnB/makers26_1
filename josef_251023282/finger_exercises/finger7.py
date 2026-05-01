# question 1:
def eval_quadratic(a, b, c, x):
    return a*x**2 + b*x + c

print(eval_quadratic(1,1,1,1))

# question 2:

def two_quadratics(a1,b1,c1,x1,a2,b2,c2,x2):
    soma = (a1*x1**2 + b1*x1 + c1) + (a2*x2**2 + b2*x2 + c2)

    print(soma)

two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) 
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1))