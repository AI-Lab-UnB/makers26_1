# Problem Set 1C
# Name: Matheus Eiki
# Collaborators: Claude (não consegui fazer sozinho)
# Time Spent: 0:25

initial_deposit = float(input("Enter the initial deposit: "))

cost_of_dream_home = 800000
portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment  
months = 36
epsilon = 100

if initial_deposit >= down_payment - epsilon:
    r = 0.0
    steps = 0

elif initial_deposit * (1 + 1.0/12) ** months < down_payment - epsilon:
    r = None
    steps = 0

else:
    low = 0.0
    high = 1.0
    r = (low + high) / 2
    steps = 0

    amount_saved = initial_deposit * (1 + r/12) ** months

    while abs(amount_saved - down_payment) >= epsilon:
        if amount_saved < down_payment:
            low = r
        else:
            high = r

        r = (low + high) / 2
        steps += 1
        amount_saved = initial_deposit * (1 + r/12) ** months

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")