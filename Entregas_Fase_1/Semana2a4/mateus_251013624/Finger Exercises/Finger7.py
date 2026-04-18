#Questão 1
def eval_quadratic(a, b, c, x):
    return a*x*x + b*x + c
print("Questão 1:\n")
print(eval_quadratic(1,2,3,4)) # printa 27

#Questão 2
def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    print((a1*x1*x1 + b1*x1 + c1) + (a2*x2*x2 + b2*x2 + c2))
print("\nQuestão 2:\n")
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) # printa 6
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) #printa 6 e então None
