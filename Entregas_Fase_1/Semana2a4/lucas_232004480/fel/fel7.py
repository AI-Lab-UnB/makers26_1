

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))
x = int(input("Valor de x: "))

def eval_quadratic(a, b, c, x):
    return a*x**2 + b*x + c

print(eval_quadratic(a, b, c, x)) # prints 3 