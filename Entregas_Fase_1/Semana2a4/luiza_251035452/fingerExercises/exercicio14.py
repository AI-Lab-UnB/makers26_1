def keys_with_value(aDict, target):
    resultado = []  
    
    for chave in aDict:  
        if aDict[chave] == target:  
            resultado.append(chave)  
    
    resultado.sort()  
    
    return resultado  


# questão 2
aDict = {1: 2, 2: 4, 5: 2}
target = 2
print(keys_with_value(aDict, target))  

def all_positive(d):
    resultado = []  
    
    for chave in d: 
        soma = sum(d[chave])  
        
        if soma > 0:  
            resultado.append(chave)  
    
    resultado.sort()  
    
    return resultado 


# example
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))  