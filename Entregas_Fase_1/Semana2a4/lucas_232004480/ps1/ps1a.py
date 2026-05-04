yearly_salary = float(input('Enter your yearly salary: '))
portion_saved  = float(input('Enter the percent of your salary to save, as a decimal:'))
cost_of_dream_home = float(input('Enter the cost of your dream home: '))

mounthly_salary = yearly_salary / 12    # Salário mensal

r = .05                         # annual rate of return

portion_down_payment = .25      # Down payment = Pagamento da Entrada
down_payment = portion_down_payment * cost_of_dream_home

amount_saved = 0
amount_saved += mounthly_salary * portion_saved
amount_saved = amount_saved *(r/12) + mounthly_salary * portion_saved



number_of_months = (down_payment) /  amount_saved

# Imprimindo na tela
# print('Custo da Entrada:', down_payment)
# print('Total acumulado:',amount_saved)
print('number of months:', int(number_of_months))