initial_deposit = float(input("Valor do deposito incial: "))
custo_casa = 800000
entrada = 0.25 * 800000
prazo = 36
low = 0.0
high = 1.0
steps = 0
if initial_deposit >= 199900:
    r=0.0
    steps = 0
elif initial_deposit * (1 + 1.0/12)**36 < 199900:
    r = None
    steps = 0
else: 
    while True:
        r = (low + high) /2
        amount_saved = initial_deposit* (1 + r/12)**36
        if abs(amount_saved - entrada) <= 100:
            break
        elif amount_saved < entrada:
            low = r
        else:
            high = r
        steps +=1
print(steps)
print(r)

