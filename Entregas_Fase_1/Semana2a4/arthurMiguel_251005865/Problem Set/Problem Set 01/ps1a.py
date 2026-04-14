## 6.100A PSet 1: Part A
## Name: Arthur Miguel Silva Rocha
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

yearly_salary = float(input("Digite seu salário: "))
portion_saved = float(input("Digite a porção a ser salva (em decimal): "))
cost_of_dream_home = float(input("Digite o custo da sua casa dos sonhos: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

cost_of_down_payment = cost_of_dream_home * 0.25
amount_saved = 0
amount_saved += amount_saved * (0.05 / 12)
monthly_deposit = (yearly_salary / 12) * portion_saved
savings = amount_saved + monthly_deposit 

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

months = 1
while(savings < cost_of_down_payment):
    monthly_rate = savings * (0.05 / 12)
    savings = savings + amount_saved + monthly_deposit + monthly_rate
    months += 1
print(months)
