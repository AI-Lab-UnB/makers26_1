depositoInicial = float(input("Digite o deposito inicial: "))
alto = 1
baixo = 0
r = (alto+ baixo) /2
contador = 1
valor = depositoInicial * (1 + (r/12))**36
while not(abs(valor - 200000) < 100):
    contador += 1
    if valor < 200000:
        baixo = r
    elif valor > 200000:
        alto = r
    r = (alto+ baixo) /2
    if r >= 0.99:
        r = None
        break
    valor = abs(depositoInicial * (1 + (r / 12)) ** 36)

print(f"Melhor índice de deposito: {r}")
print(f"Número de passos: {contador}")