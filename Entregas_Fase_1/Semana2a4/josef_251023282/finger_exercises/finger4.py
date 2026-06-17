x = int(input(""))
cont = 0

while cont**3 < x:
    cont = cont + 1

if cont**3 == x:
    print(cont)

else:
    print("error") 

