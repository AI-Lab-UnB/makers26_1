# Problem Set 0
# Name: Pedro Henrique
# Collaborators: 
# Time Spent: 1:00

import numpy

a = int(input("Enter an integer number: "))
b = int(input("Enter another integer number: "))

z = a ** b

a = numpy.log2(z)

print(f"Value of z: {z}")
print(f"Value of a (log2 of z): {a}")