def sum_str_lengths(L):
    total = 0
    for i in L:
        if type(i)== str:
            total+=len(i)
        elif type(i)== list:
            for u in i:
                total+=len(u)
        else:
            raise ValueError
    return total
num = int(input("Digite a quantidade de elementos pesentes na lista, a seguir: "))
elementos = []
for i in range(num):
    elementos.append(str(input(f"A seguir digite o elemento {i+1}: ")))
print(sum_str_lengths(elementos))