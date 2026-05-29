def soma_lista(lista):
    total = 0
    for i in lista:
        total += i
    return total

lista = [1, 2, 3, 4, 5]
print(soma_lista(lista))