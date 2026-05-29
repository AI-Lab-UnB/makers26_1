## 6.100A PSet 1: Part A
## Name: Júlia Campos
## Time Spent:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
year_salary = float(input("Enter your year salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your  dream home: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0.0
r = 0.05
months = 0
needed_value = cost_of_dream_home*portion_down_payment
month_salary = year_salary/12
month_add = portion_saved * month_salary


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < needed_value:
    amount_saved += amount_saved * (r/12)
    amount_saved += month_add
    months +=1

print(f'Number of months: {months}')