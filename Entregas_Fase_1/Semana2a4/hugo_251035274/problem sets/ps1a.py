yearly_salary = float(input("Qual seu salário anual? "))
portion_saved = float(input("Qual a porção do seu salário que você poupa? "))
coast_of_dream_home = float(input("Qual o custo da casa dos seus sonhos? "))

portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0
down_payment = coast_of_dream_home * portion_down_payment

while amount_saved < down_payment:
    month_saved = (yearly_salary / 12) * portion_saved
    month_return = amount_saved * (r / 12)
    
    amount_saved += month_saved + month_return
    months += 1

print("Número de meses: " + str(months))