yearly_salary = float(input("Salary:"))
portion_saved = float(input("Portion to be saved:"))
cost_of_dream_home = float(input("Cost of the house you want:"))

portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment
amount_saved = 0.0
r = 0.05  
months = 0
monthly_salary = yearly_salary / 12

while amount_saved < down_payment:
    monthly_return = amount_saved * (r / 12)
    monthly_deposit = monthly_salary * portion_saved
    amount_saved += monthly_deposit + monthly_return
    months += 1

print("Number of months:", months)