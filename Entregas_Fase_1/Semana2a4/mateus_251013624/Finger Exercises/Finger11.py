def remove_and_sort(l, k):
    if k >= len(l):
        l.clear()
        return
    del(l[:k])
    l .sort()
# Exemplo caso k seja menor que o tamanho da lista
l = [1, 6, 3]
k = 1
remove_and_sort(l, k)
print(l)   # prints the list [3, 6]

# Exemplo caso k seja maior que o tamanho da lista
l = [1, 6, 3]
k = 4
remove_and_sort(l, k)
print(l)   # printa lista vazia