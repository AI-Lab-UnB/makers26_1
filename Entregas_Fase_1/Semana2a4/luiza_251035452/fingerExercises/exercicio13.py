def sum_str_lengths(L):
    total = 0  
    
    for elem in L:  
        
        if type(elem) == str:  
            total += len(elem)
        
        elif type(elem) == list:  
            for sub in elem:  
                
                if type(sub) == str:  
                    total += len(sub)
                else:
                    raise ValueError  # elemento inválido na sublista
        
        else:
            raise ValueError  # elemento inválido na lista principal
    
    return total


# examples
print(sum_str_lengths(["abcd", ["e", "fg"]]))  
print(sum_str_lengths([12, ["e", "fg"]]))      
