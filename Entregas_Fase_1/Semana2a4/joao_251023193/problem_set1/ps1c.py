## 6.100A PSet 1: Part C
## Name: João Vítor Sauma de Faria
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = int(input("Enter the initial deposit here: $"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_dream_house = 800000
down_payment = 200000 #0.25 * cost_of_dream_house
r1 = 0.00
r2 = 1.00
steps = 0
amount_saved = 0
max_amount = initial_deposit * (1 + (1.0/12))**36

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

if max_amount < 200000:
    
    print(f"Best savings rate: {None}")
    print(f"Steps in bisection search: 0 [May vary based on how you implemented your bisection search]")
    
else:

    while True:
        steps += 1
        r = (r1+r2)/2
        amount_saved = initial_deposit * (1 + (r/12))**36
        
        if abs(amount_saved - 200000) < 100:
            print(f"Best savings rate: {r} [or very close to this number]")
            print(f"Steps in bisection search: {steps} [or very close to this number]")
            break
        elif amount_saved > 200000 + 100:
            r2 = r  
        else:
            r1 = r