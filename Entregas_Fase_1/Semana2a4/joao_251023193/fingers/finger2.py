# Assume you are given a variable named number (has a numerical value). Write a piece of Python code that
# prints out one of the folowing strings:

# positive if the variable number is positive
# negative if the variable number is negative
# zero if the variable number is equal to zero

number = 9

if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")