def flatten(L):
    resultado = []  
    
    for elem in L:  
        
        if type(elem) == list: 
            resultado += flatten(elem)  
        else:
            resultado.append(elem)  
    
    return resultado


# example
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L))  #prints the list [1,4,6,2,3,2,4,5]