# # # # # # # # # # # #
#       questao 1     #
# # # # # # # # # # # #
def keys_with_value(aDict, target):
    resultado = []

    for chave in aDict:
        atual = aDict[chave]
        
        if atual == target:
            resultado.append(chave)
            
    n = len(resultado)
    for i in range(n):
        for j in range(0, n - i - 1):
            if resultado[j] > resultado[j + 1]:
                # Swap manual estilo C
                temp = resultado[j]
                resultado[j] = resultado[j + 1]
                resultado[j + 1] = temp
                
    return resultado

# # # # # # # # # # # #
#       questao 2     #
# # # # # # # # # # # #
def all_positive(d):
    chaves_positivas = []
    
    for k in d:
        v = d[k]
        
        soma_total = 0
        for num in v:
            soma_total += num
            
        if soma_total > 0:
            chaves_positivas.append(k)
            
    n = len(chaves_positivas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if chaves_positivas[j] > chaves_positivas[j + 1]:
                # Swap manual
                temp = chaves_positivas[j]
                chaves_positivas[j] = chaves_positivas[j + 1]
                chaves_positivas[j + 1] = temp
                
    return chaves_positivas
