

def sum_str_lengths(L):

    copy_L = []

    for num in L :

        if type(num) == list:

            copy_L.extend(sum_str_lengths(num))
    
        else:

            if type(num) != str:

                raise ValueError("Nao é permitido entrada diferente de string")

            copy_L.append(num)
            
    return copy_L







# Examples:
L = ["abcd", ["e", "fg"]]
copy_L = sum_str_lengths(L) # prints the list [1,4,6,2,3,2,4,5]



count = 0

for elem in copy_L:

    tam_elem = len(elem)
    count += tam_elem

print(count)