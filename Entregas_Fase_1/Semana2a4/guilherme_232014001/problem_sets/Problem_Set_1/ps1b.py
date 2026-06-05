## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter your percent of your annual salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise (e.g. 0.03 for 3%): "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
savings = 0
months = 0
portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment
annual_return = 0.05


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while savings < down_payment:
    savings += savings * (annual_return / 12) + (yearly_salary / 12) * portion_saved
    months += 1
    if months % 6 == 0:
        yearly_salary *= (1 + semi_annual_raise)

print("Number of months:", months)
