## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
# salario_mensal = yearly_salary / 12

valor_entrada = cost_of_dream_home * 0.25

valor_guardado = 0

# bonificacao = 0.05 / 12

investimento_mensal = yearly_salary / 12 * portion_saved

meses = 0

# print(f"Valor da entrada : {valor_entrada}")

while valor_guardado < valor_entrada :

    valor_guardado = valor_guardado * (1 + 0.05/12) + investimento_mensal

    # print(valor_guardado)

    meses += 1


print(meses)
    

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
