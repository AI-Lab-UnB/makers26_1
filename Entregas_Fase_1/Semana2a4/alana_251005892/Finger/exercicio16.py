def flatten (L):
    lista_achatada = []
    for sublista in L:
        lista_achatada.extend(sublista)
    lista_unica = list(set(lista_achatada))
    return lista_unica
num = int(input("A seguir digite o tamanho da lista: "))
el=[]
for i in range(num):
    el.append(list(input(f"Digite os itens da sublista {i+1} sem espaço ")))
print(flatten(el))