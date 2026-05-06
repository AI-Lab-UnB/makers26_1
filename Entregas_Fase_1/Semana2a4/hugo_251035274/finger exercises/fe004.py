n = int(input("Write a number: "))

i = 1
while i ** 3 < n:
    i += 1

if i**3 == n:
    print(f"The cube root of {n} is {i}!")
else:
    print("error")