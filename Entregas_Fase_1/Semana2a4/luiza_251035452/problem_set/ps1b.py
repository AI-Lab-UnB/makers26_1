yearly_salary = float(input("Digite seu salário anual inicial: "))
portion_saved = float(input("Digite a porcentagem do salário a poupar (em decimal): "))
cost_of_dream_home = float(input("Digite o custo da sua casa dos sonhos: "))
semi_annual_raise = float(input("Digite o aumento semestral, em decimal: "))

portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0

down_payment = cost_of_dream_home * portion_down_payment

while amount_saved < down_payment:
    amount_saved += amount_saved * (r / 12) + (yearly_salary / 12) * portion_saved
    months += 1
    if months % 6 == 0:
        yearly_salary *= (1 + semi_annual_raise)

print("Número de meses:", months)