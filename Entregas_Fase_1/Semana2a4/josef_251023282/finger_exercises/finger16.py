def flatten(L):
    resultado = []
    
    for item in L:
        if isinstance(item, list):
            sublista_achatada = flatten(item)
            
            for elemento in sublista_achatada:
                resultado.append(elemento)
        else:
            resultado.append(item)
            
    return resultado

L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L))