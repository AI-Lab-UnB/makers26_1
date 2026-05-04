# Problem Set 1A
# Name: [Thomaz]
# Collaborators: 
# Time spent: 

yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
r = 0.05
monthly_salary = yearly_salary / 12
monthly_saved = monthly_salary * portion_saved
down_payment = cost_of_dream_home * portion_down_payment

amount_saved = 0.0
months = 0

while amount_saved < down_payment:
    amount_saved += amount_saved * (r / 12)
    amount_saved += monthly_saved
    months += 1

print(f"Number of months: {months}")