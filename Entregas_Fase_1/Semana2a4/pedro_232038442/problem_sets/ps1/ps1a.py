## PSet 1: Part A
## Name: Pedro Henrique
## Time Spent: 10:00
## Collaborators: None

# Get user input for yearly_salary, portion_saved and cost_of_dream_home below
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

# Initialize other variables you need (if any) for your program below
portion_down_payment = 0.25
current_savings = 0.0
r = 0.05
monthly_salary = yearly_salary / 12
months = 0

# Determine how many months it would take to get the down payment for your dream home below
while current_savings < cost_of_dream_home * portion_down_payment:
    current_savings += current_savings * r / 12 + portion_saved * monthly_salary
    months += 1

print("Number of months:", months)
