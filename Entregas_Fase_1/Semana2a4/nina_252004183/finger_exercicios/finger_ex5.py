my_str = input("Digite uma string: ")

result = ""

for i in range(0, len(my_str), 2):
    result += my_str[i]

print(result)