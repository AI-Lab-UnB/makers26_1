#finger 1
"""
total (a + b) * c
print(total)
"""
#finger 2
"""
number = 2
if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
"""
#finger 3
"""
for i in range(int(input())):
    print("hello world")
"""
#finger 4
"""
N = 8
perfect_cubes = 0
i = 0
while(perfect_cubes < N):
    perfect_cubes = i*i*i
    if perfect_cubes == N:
        print("perfect cube")
        break
    i+=1
else:
    print("error")
"""
#finger 5
"""
my_str = "abcdefg"
print("".join(my_str[x] for x in range(0, len(my_str), 2)))
"""
#finger 6
"""
max = 1001
min = 0
integer = 1
count = 1
answer = None
while(True):
    if (max+min)//2 == integer:
        answer = (max+min)//2
        break 
    if (max+min)//2 > integer:
        max = (max+min)//2
    else:
        min = (max+min)//2
    count +=1
print ("count: ", count)
print("answer: ", answer)
"""


#finger 7
"""
def eval_quadratic(a, b, c, x):
    
    # a, b, c: numerical values for the coefficients of a quadratic equation
    # x: numerical value at which to evaluate the quadratic.
    # Returns the value of the quadratic a×x² + b×x + c.
    
    return a*x**2 + b*x + c

# Examples:    
print(eval_quadratic(1, 1, 1, 1)) # prints 3
def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    
    # a1, b1, c1: one set of coefficients of a quadratic equation
    # a2, b2, c2: another set of coefficients of a quadratic equation
    # x1, x2: values at which to evaluate the quadratics
    # Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    # Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    # Prints the sum of the two evaluations. Does not return anything.

    print(eval_quadratic(a1, b1, c1, x1) + eval_quadratic(a2, b2, c2, x2))

# Examples:    
#two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) # prints 6
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6 then None
"""
#finger 8
