import math
def recur_power(base, exp):
    if exp==0:
        return 1
    return base * recur_power(base, exp - 1)
base = float(input("Base: "))
exp = int(input("Expoente: "))
print(recur_power(base, exp))