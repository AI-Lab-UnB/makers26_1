my_str = input("Write a word: ")

new_str = ''
for i in range(0, len(my_str)):
    if (i % 2 == 0):
        new_str += my_str[i]

print(new_str)
