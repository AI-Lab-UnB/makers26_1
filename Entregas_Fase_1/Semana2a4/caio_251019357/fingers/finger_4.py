n = 27

i = 1

flag = False

while i < n/2 :

    if i**3 == n:
        print(i)
        flag = True
        break

    else:
        i += 1

if not flag:
    print("error")



    