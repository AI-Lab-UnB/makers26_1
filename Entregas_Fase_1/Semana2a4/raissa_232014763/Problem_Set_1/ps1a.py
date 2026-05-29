## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your annual salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
savings = 0
months = 0
portion_of_payment = 0.25
down_payment = portion_of_payment * cost_of_dream_home

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while savings < down_payment:
    savings += savings * (0.05 / 12) + (yearly_salary / 12) * portion_saved
    months += 1

print("Number of months:", months)