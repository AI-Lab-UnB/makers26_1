def recur_power(base, exp):
    if exp == 0:
        return 1
    return base * recur_power(base, exp-1)

print(recur_power(2,5)) # prints 32
print(recur_power(8459498984598549845984985489895454895489892,0)) #prints 1