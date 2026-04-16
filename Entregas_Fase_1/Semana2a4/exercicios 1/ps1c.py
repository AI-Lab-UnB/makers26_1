## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

# casa custa 800k, down payment eh 25%
down_payment = 800000 * 0.25
months = 36
epsilon = 100

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

# se o deposito inicial ja cobre (com margem), taxa eh zero
if initial_deposit >= down_payment - epsilon:
    r = 0.0
    steps = 0
else:
    # testa se eh possivel chegar com taxa maxima de 100%
    if initial_deposit * ((1 + 1.0 / 12) ** months) < down_payment - epsilon:
        r = None
        steps = 0
    else:
        low = 0.0
        high = 1.0
        steps = 0

        while True:
            r = (low + high) / 2
            total = initial_deposit * ((1 + r / 12) ** months)
            steps += 1

            if abs(total - down_payment) <= epsilon:
                break
            elif total < down_payment:
                low = r
            else:
                high = r

print("Best savings rate:", r)
print("Steps in bisection search:", steps)
