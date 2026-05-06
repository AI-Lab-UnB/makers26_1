yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
amount_saved = 0
r = 0.05
monthly_salary = yearly_salary / 12
months = 0
down = cost_of_dream_home * portion_down_payment

while down > amount_saved:
    monthly_return = amount_saved * (r/12)
    montly_save = monthly_salary * portion_saved
    amount_saved += monthly_return + montly_save

    months += 1

print(f"Number of months: {months}")