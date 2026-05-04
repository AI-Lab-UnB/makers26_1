
num = int(input())

cont = False

i = 1
while cont is False:
    if i**3 == num:
        cont = True
        print("Perfect cube")
    elif i**3 > num:
        cont = True
        print("error")
    else:
        i+=1