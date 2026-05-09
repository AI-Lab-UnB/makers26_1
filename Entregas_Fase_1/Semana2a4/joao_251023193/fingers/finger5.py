# Assume you are given a string variable named my_str. Write a piece of Python code that prints out a new
# string containing the even indexed characters of my_str. For example, if my_str = "abcdefg" then your
# code should print out aceg.

my_str = "abcdefg"
new_str = ""
number = 0

for i in my_str:
    number += 1
    if number % 2 == 1:
        new_str += i
    else:
        continue
print(new_str)