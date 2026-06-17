def flatten(lista):
    for i in lista:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i
L = [[1,4,[6],2],[[[3]],2],4,5]

print(list(flatten(L))) # prints the list [1,4,6,2,3,2,4,5]