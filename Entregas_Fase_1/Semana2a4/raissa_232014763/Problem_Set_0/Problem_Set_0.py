import math

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
x = float(input("Digite um número para calcular o logaritmo natural: "))

resultado = a ** b
resultado_log = math.log(x)

print(f"O resultado de {a} elevado a {b} é: {resultado}")
print(f"O logaritmo natural de {x} é: {resultado_log}")
