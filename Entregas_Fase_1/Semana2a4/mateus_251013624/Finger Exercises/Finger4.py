n = int(input("Figite o número que você queira achar a raiz cúbica: "))
i = 1
while i**3 < n:
    i+= 1
if i**3 == n:
    print(f"A raiz cúbica de {n} é {i}")
else:
    print(f"Erro {n} não tem raiz cúbica ")
