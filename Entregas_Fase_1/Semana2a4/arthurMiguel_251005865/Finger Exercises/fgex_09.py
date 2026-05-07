tA = ()
tB = ()

tamanho = int(input("Qual o tamanho das tuplas?: "))

for c in range(tamanho):
    numA = int(input("Digite um número a ser adicionado: "))
    tA = tA + (numA,)

for i in range(tamanho):
    numB = int(input("Digite um número a ser adicionado: "))
    tB = tB + (numB,)

soma = sum(tA + tB)

print(len(tA))
print(soma)
