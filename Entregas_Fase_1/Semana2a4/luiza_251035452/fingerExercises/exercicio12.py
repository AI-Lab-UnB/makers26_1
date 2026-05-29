def count_sqrts(nums_list):
    contador = 0  
    
    for num in nums_list:  
        quadrado = num * num  
        
        if quadrado in nums_list: 
            contador += 1
    
    return contador


# examples
print(count_sqrts([3, 4, 2, 1, 9, 25])) 