import math
def eq_quadratica (a,b,c,x):
    primeiroTermo = a*pow(x,2)
    segundoTermo = b*x
    total = primeiroTermo + segundoTermo + c
    print(total)
A = int(input("Insira o coeficiente do primeiro termo: "))
B= int(input("Insira o coeficiente do segundo termo: "))
C =int(input("Insira o terceiro termo: "))
X = int(input("Insira o valor de x: "))
eq_quadratica(A,B,C,X)