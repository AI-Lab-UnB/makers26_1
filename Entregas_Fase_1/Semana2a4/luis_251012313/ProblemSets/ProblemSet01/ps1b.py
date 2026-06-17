## 6.100A PSet 1: Part B
## Name: Luis
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################

yearly_salary = float(input("Enter yout starting yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment
amount_saved = 0
months = 0
r = 0.05

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while (amount_saved < down_payment):

	monthly_return = amount_saved * (r / 12)

	monthly_deposit = (yearly_salary / 12) * portion_saved

	amount_saved += monthly_return + monthly_deposit

	months += 1
	if (months % 6 == 0): yearly_salary *= (1 + semi_annual_raise)

print(f"Number of months: {months}")