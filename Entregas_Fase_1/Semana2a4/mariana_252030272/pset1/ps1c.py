initial_deposit = float(input())
cost_dreamhouse = 800000*0.25
r = 1.0
months = 36
loop_counts = 0
a = True

if ((initial_deposit * (1+ 1/12)**months) <= cost_dreamhouse + 100):
    a = False
    r = None

    
r_passado = 0
r_proximo = 1
while(a):
    
    amount_saved = (initial_deposit * (1+ r/12)**months)
    r_proximo 
    if (cost_dreamhouse + 100 >= amount_saved >= cost_dreamhouse - 100):
        break
    elif (cost_dreamhouse - 100 >= amount_saved ):
        r_passado = r
        r = (r_passado+r_proximo)/2

    elif (cost_dreamhouse + 100 <= amount_saved ):
        r_proximo = r
        r = (r_passado+r_proximo)/2
    else:
        break
    loop_counts += 1
    
    print(r)

print("Best savings rate: ", r)
print("Steps in bisection search: ", loop_counts)