def sum_str_lengths(L):
    total = 0
    for item in L:
        if isinstance(item, str):
            total += len(item)
        elif isinstance(item, list):
            for subitem in item:
                if isinstance(subitem, str):
                    total += len(subitem)
                else:
                    raise ValueError("Elemento dentro da sublista não é uma string")
        else:
            raise ValueError("Elemento da lista principal não é string nem lista")
            
    return total

print(sum_str_lengths(["abcd", ["e", "fg"]])) 