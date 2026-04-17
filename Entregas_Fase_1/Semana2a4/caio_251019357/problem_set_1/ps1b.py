## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter semi anual raise: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################


valor_entrada = cost_of_dream_home * 0.25

valor_guardado = 0

investimento_mensal = yearly_salary / 12 * portion_saved

meses = 0


###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################


while valor_guardado < valor_entrada :

    valor_guardado = valor_guardado * (1 + 0.05/12) + investimento_mensal

    meses += 1

    if meses % 6 == 0 :

        yearly_salary += yearly_salary * semi_annual_raise
        investimento_mensal = yearly_salary / 12 * portion_saved

print(meses)