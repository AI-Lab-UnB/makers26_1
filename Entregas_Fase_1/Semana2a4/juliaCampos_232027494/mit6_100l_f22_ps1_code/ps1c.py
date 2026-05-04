## 6.100A PSet 1: Part C
## Name: Júlia Campos
## Time Spent:
## Collaborators:
import math

def amount_cal(initial_deposit,r):
    a= (1+(r/12))**36
    return initial_deposit*a

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
high = 1.0
low = 0.0
margin= 100
nd_value = 200000
r = (high+low)/2
amount_saved = amount_cal(initial_deposit,r)
steps = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
    
while abs(amount_saved - nd_value) > margin:
    if amount_saved > nd_value:
        high = r
        r = (high+low)/2
        amount_saved = amount_cal(initial_deposit,r)
    else:
        low = r
        r = (high+low)/2
        amount_saved = amount_cal(initial_deposit,r)
    steps+=1

print(f'Best savings rate: {r} [or very close to this number]')
print(f'Steps in bisection search: {steps} [May vary based on how you implemented your bisection search]')