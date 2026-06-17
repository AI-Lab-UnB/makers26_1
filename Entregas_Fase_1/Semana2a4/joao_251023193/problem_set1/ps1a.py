## 6.100A PSet 1: Part A
## Name: João Vítor Sauma de Faria
## Time Spent:
## Collaborators: 

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = int(input("Enter your yearly salary: $"))
portion_saved = float(input("Enter the portion saved, as a decimal: "))
cost_of_dream_home = int(input("Enter the cost of the dream home: $"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

monthly_salary = yearly_salary / 12
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0
down_payment = portion_down_payment * cost_of_dream_home


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while amount_saved < down_payment:
    amount_saved += (monthly_salary * portion_saved) + (amount_saved * (r/12))
    months +=1
print(f"Number of months: {months}")