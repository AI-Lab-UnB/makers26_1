my_str = input()
s = ""

for i in range(len(my_str)):
    if i % 2 == 0:
        s += my_str[i]

print(s)
