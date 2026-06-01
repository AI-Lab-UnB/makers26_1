# Part 1

def keys_with_value(aDict, target):
    lista = []
    for key, value in aDict.items():
        if value == target:
            lista.append(key)
    return sorted(lista)



aDict = {1:2, 2:4, 5:2}
target = 2   
print(keys_with_value(aDict, target)) # prints the list [1,5]]

# Part 2

def all_positive(d):
    lista = []
    for key, listaDict in d.items():
        if(sum(listaDict) > 0):
            lista.append(key)
    return sorted(lista)

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]