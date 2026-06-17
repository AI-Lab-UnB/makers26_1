
def recur_power(base, exp):

    if exp < 0:

        return base 

    return base * base**(exp-1)



# Examples:
print(recur_power(2,5))  # prints 32