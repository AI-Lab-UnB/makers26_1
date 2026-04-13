initial_deposit = float(input("Qual o valor do depósito inicial? "))

cost_of_dream_home = 800000
portion_down_payment = 0.25
months = 36
down_payment = cost_of_dream_home * portion_down_payment

low = 0
high = 1
r = (low + high) / 2
steps = 0


while True:
    amount_saved = initial_deposit * (1 + r / 12) ** months
    if abs(amount_saved - down_payment) <= 100:
        break
     
    if amount_saved < down_payment:
        low = r
    else:
        high = r
    
    if steps > 100:
        r = None
        steps = 0
        break
    
    r = (low + high) / 2    
    steps += 1
    

print("Porção a ser poupada: " + str(r))
print("Quantidade de passos na bisseção: " + str(steps))