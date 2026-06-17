def keys_with_value(dicionario, target):
    chaves = []
    for i in dicionario.keys():
        if dicionario[i] == target:
            chaves.append(i)
    chaves.sort()
    return chaves 