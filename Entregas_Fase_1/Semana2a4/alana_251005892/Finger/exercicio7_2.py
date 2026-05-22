import math
def two_quadratics (a1,b1,c1,x1,a2,b2,c2,x2):
   equação1 =  (a1*pow(x1,2)) + (b1*x1) + c1
   equação2 = (a2*pow(x2,2)) + (b2*x2) + c2
   total = equação1 + equação2
   print(total)
A1=int(input("insira o 'a' da primeira equação "))
A2=int(input("insira o 'a' da segunda equação "))
B1=int(input("insira o 'b' da primeira equação "))
B2=int(input("insira o 'b' da segunda equação "))
C1=int(input("insira o 'c' da primeira equação "))
C2=int(input("insira o 'c' da segunda equação "))
X1=int(input("insira o valor de x da primeira equação "))
X2=int(input("insira o valor de x da segunda equação "))
two_quadratics(A1, B1, C1, X1,A2, B2,C2,X2)