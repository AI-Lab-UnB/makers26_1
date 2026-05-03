N = int(input("Digite um número inteiro positivo: "))

guess = 0

while guess**3 < N:
    guess += 1

if guess**3 == N:
    print("Cube root of", N, "is", guess)
else:
    print("Error")