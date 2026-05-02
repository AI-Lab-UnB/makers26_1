
def flatten(L):

    copy_L = []

    for num in L :

        if type(num) == list:

            copy_L.extend(flatten(num))
    
        else:

            copy_L.append(num)


    return copy_L


# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]