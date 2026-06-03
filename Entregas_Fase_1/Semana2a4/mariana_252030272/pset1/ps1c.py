initial_deposit = float(input("Enter your yearly salary: "))
cost_dreamhouse = 800000*0.25

months = 36
loop_counts = 0
a = True

if ((initial_deposit * (1+ 1/12)**months) <= cost_dreamhouse + 100):
    a = False
    r = None

r_passado = 0
r_proximo = 1
r =  (r_passado + r_proximo)/2

while(a):
    
    amount_saved = (initial_deposit * (1+ r/12)**months) 
    if (cost_dreamhouse + 100 >= amount_saved >= cost_dreamhouse - 100):
        break
    elif (amount_saved < cost_dreamhouse - 100):
        r_passado = r
        r = (r_passado + r_proximo)/2
    elif (amount_saved > cost_dreamhouse + 100):
        r_proximo = r
        r = (r_passado + r_proximo)/2
    else:
        break
    loop_counts += 1

print("Best savings rate: ", r)
print("Steps in bisection search: ", loop_counts)