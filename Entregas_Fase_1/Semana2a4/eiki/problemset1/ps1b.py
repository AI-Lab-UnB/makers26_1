# Problem Set 1B
# Name: Matheus Eiki
# Collaborators: None
# Time Spent: 0:10

yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0

down_payment = cost_of_dream_home * portion_down_payment

while amount_saved < down_payment:
    amount_saved += amount_saved * (r / 12)           
    amount_saved += (yearly_salary / 12) * portion_saved
    months += 1

    if months % 6 == 0:                               # a cada 6 meses
        yearly_salary *= (1 + semi_annual_raise)      # aumenta o salário

print(f"Number of months: {months}")