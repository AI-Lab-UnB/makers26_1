my_str = "abcdefg"
new_str = ""

for i in range(len(my_str)):
    if i % 2 == 0:
        new_str =new_str + my_str[i]

print(new_str)