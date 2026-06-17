def recur_power(base, exp):
    if exp == 0:
        return 1

    base = base * (recur_power(base, (exp - 1)))
    
    return base

print(recur_power(2,5)) # 32
print(recur_power(2, 10)) # 1024