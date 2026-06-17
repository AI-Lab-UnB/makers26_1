## 6.100A PSet 1: Part C
## Name: Diogo Oliveira
## Time Spent: 1h
## Collaborators: Diogo Oliveira

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input("Insert the initial_deposit: \n"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

r = 0.5 # Começa em 50% - Bisection Search
amount_saved = initial_deposit

required_down_payment = 800000 * 0.25
min_required_down_payment = required_down_payment - 100
max_required_down_payment = required_down_payment + 100

steps = 0
lim_menor = 0.0
lim_maior = 1.0
##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

if(amount_saved >= min_required_down_payment):
    r = None
elif( not(amount_saved * pow((1 + 1 / 12), 36)) >= min_required_down_payment ):
    r = None
else:
    
    test_amount_saved = 0
    
    while( not(test_amount_saved >= min_required_down_payment and test_amount_saved <= max_required_down_payment) ):
        
        r = (lim_maior + lim_menor) / 2
        steps += 1
        test_amount_saved = amount_saved * pow((1 + r / 12), 36)
        
        if(test_amount_saved > max_required_down_payment):
            lim_maior = r
        elif(test_amount_saved < min_required_down_payment):
            lim_menor = r
        else: break
            


print(f'Best savings rate: {r}')
print(f'Steps in bisection search: {steps}')
            