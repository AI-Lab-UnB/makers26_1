yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0
down = cost_of_dream_home * portion_down_payment

while (down > amount_saved):
    monthly_salary = yearly_salary / 12
    monthly_return = amount_saved * (r/12)
    montly_save = monthly_salary * portion_saved
    amount_saved += monthly_return + montly_save

    months += 1

    if (months % 6 == 0):
        yearly_salary += yearly_salary * semi_annual_raise

print(f"Number of months: {months}")