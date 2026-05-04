def remove_and_sort(lin, k):
    for i in range(k):
        del lin[0]
    lin.sort()
    ordenada=lin
    return ordenada
k=int(input("Insira o numero de elementos a serem removidos da lista "))
lin = []
tam = int(input("qual o tamanho da lista? "))
for i in range(tam):
    lin.append(int(input(f"insira o elemento {i+1} da lista ")))
print(remove_and_sort(lin,k))