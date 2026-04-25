initial_deposit = float(input("Enter the initial deposit: "))

target_down_payment = 800000 * 0.25
months = 36
epsilon = 100  

low = 0.0
high = 1.0
steps = 0
r = (high + low) / 2.0

if initial_deposit >= target_down_payment - epsilon:
    r = 0.0
    steps = 0
else:
    if initial_deposit * (1 + 1.0/12)**months < target_down_payment - epsilon:
        r = None
        steps = 0
    else:
        while True:
            steps += 1
            current_savings = initial_deposit * (1 + r/12)**months
            
            if abs(current_savings - target_down_payment) < epsilon:
                break
            
            if current_savings > target_down_payment:
                high = r
            else:
                low = r
                
            r = (high + low) / 2.0
            
            if steps > 100:
                break

print("Best savings rate:", r)
print("Steps in bisection search:", steps)