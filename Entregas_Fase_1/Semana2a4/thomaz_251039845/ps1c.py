
# Problem Set 1C
# Name: [Thomaz]
# Collaborators: 
# Time spent: 

initial_deposit = float(input("Enter the initial deposit: "))

cost_of_dream_home = 800000
portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment
months = 36

if initial_deposit >= down_payment - 100:
    r = 0.0
    steps = 0
    print(f"Best savings rate: {r}")
    print(f"Steps in bisection search: {steps}")
    exit()
max_r = 1.0
amount_saved_max = initial_deposit * (1 + max_r/12) ** months
if amount_saved_max < down_payment - 100:
    r = None
    steps = 0
    print(f"Best savings rate: {r}")
    print(f"Steps in bisection search: {steps}")
    exit()
low = 0.0
high = 1.0
steps = 0
r = None

while steps < 100: 
    steps += 1
    r = (low + high) / 2
    amount_saved = initial_deposit * (1 + r/12) ** months
    
    if abs(amount_saved - down_payment) <= 100:
        break
    elif amount_saved < down_payment:
        low = r
    else:
        high = r
    if high - low < 1e-10:
        break

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")