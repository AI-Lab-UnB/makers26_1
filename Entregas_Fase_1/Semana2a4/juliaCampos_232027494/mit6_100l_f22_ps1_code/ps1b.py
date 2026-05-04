## 6.100A PSet 1: Part B
## Name: Júlia Campos
## Time Spent:
## Collaborators:

def new_annual_salary(year_salary,semi_annual_raise):
    year_salary += year_salary*semi_annual_raise
    return year_salary

def month_add_calc(portion_saved,month_salary):
    add = portion_saved * month_salary
    return add

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
year_salary = float(input("Enter your year salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your  dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as  a decimal: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0.0
r = 0.05
months = 0
needed_value = cost_of_dream_home*portion_down_payment
month_salary = year_salary/12
month_add = month_add_calc(portion_saved,month_salary)


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < needed_value:
    amount_saved += amount_saved * (r/12)
    amount_saved += month_add
    months +=1
    if months%6 == 0:
        year_salary = new_annual_salary(year_salary,semi_annual_raise)
        month_salary = year_salary/12
        month_add = month_add_calc(portion_saved,month_salary)

print(f'Number of months: {months}')
