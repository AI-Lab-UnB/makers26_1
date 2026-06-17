initial_deposit = float(input())

down_payment = 800000.0 * 0.25
months = 36
tolerance = 100

if initial_deposit >= down_payment - tolerance:
    print("Best savings rate:", 0.0)
    print("Steps in bisection search:", 0)
else:
    max_savings = initial_deposit * (1 + 1.0/12) ** 36


    if max_savings < down_payment - tolerance:
        print("Best savings rate:", None)
        print("Steps in bisection search:", 0)
    else:
        low = 0.0
        high = 1.0
        steps = 0
        r = 0.0
    
    while True:
        r = (low + high) / 2
        steps += 1

        current_savings = initial_deposit * (1 + r/12) ** 36

        if abs(current_savings - down_payment) <= tolerance:
            break
        elif current_savings < down_payment:
            low = r
        else:
            high = r

    print("Best savings rate:", r)
    print("Steps in bisection search:", steps)