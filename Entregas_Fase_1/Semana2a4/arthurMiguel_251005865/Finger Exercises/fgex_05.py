my_str = str(input("Digite uma palavra: "))
i = 1

for c in my_str:
    if i % 2 != 0:
        print (c,end="")
    i += 1
