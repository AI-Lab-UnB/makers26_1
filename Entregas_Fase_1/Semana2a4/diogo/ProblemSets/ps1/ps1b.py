## 6.100A PSet 1: Part B
## Name: Diogo Oliveira
## Time Spent: 10m
## Collaborators: Diogo Oliveira

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################


yearly_salary = int(input("Insert your 'yearly_salary' \n"))
portion_saved = float(input("Insert your 'portion_saved' percentage (0 - 1.0) \n"))
cost_of_dream_home = int(input("Insert your 'cost_of_dream_home' \n"))
semi_annual_raise = float(input("Insert your 'semi_annual_raise' (0 - 1.0) \n"))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

portion_down_payment = 0.25
amount_saved = 0.0
annual_rate = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

while(amount_saved < portion_down_payment * cost_of_dream_home):
    if(months % 6 == 0 and months > 1):
        yearly_salary += yearly_salary * semi_annual_raise
        
    amount_saved += amount_saved * annual_rate / 12
    amount_saved += portion_saved * yearly_salary / 12
    months += 1
    
print(f'Number of months: {months}')