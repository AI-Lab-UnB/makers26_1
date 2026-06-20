# Problem Set 1B
# Name: [Thomaz]
# Collaborators: 
# Time spent: 


yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
r = 0.05
down_payment = cost_of_dream_home * portion_down_payment

amount_saved = 0.0
months = 0
monthly_salary = yearly_salary / 12

while amount_saved < down_payment:
    amount_saved += amount_saved * (r / 12)
    amount_saved += monthly_salary * portion_saved
    months += 1
    
    if months % 6 == 0:
        yearly_salary += yearly_salary * semi_annual_raise
        monthly_salary = yearly_salary / 12

print(f"Number of months: {months}")