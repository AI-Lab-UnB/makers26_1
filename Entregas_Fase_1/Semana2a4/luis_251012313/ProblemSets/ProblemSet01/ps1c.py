## 6.100A PSet 1: Part C
## Name: Luis
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################

initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

down_payment_goal = 800000 * 0.25
months = 36

high = 1.0
low = 0.0
r = (high + low) / 2
steps = 0

e = 100

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

while (True):
	steps += 1

	amount_saved = initial_deposit * (1 + r / 12) ** months

	if (abs(amount_saved - down_payment_goal) <= e): break

	if (amount_saved < down_payment_goal): low = r
	else: high = r

	r = (high + low) / 2

	if (r >= 0.999): r = None; break

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")
