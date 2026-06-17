semi_annual_raise = float(input("Porcentagem de aumento salarial a cada 6 meses em decimal: "))
yearly_salary = int(input("Salario anual: "))
portion_saved = float(input("Porcentagem do salario a salvar em decimal: "))
cost_of_dream_house = int(input("Custo da casa dos sonhos: "))
portion_down_payment = 0.25 * cost_of_dream_house
meses = 0
amount_saved = 0.0
r = 0.05
while amount_saved < portion_down_payment :
    meses +=1
    amount_saved+= amount_saved * (r/12)
    amount_saved+= portion_saved * (yearly_salary/12)
    if meses %6 == 0:
        yearly_salary += yearly_salary * semi_annual_raise
        
print(meses)