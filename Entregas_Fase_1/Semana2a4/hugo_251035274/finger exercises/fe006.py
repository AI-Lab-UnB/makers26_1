n = int(input("Write a number between 0 e 1000: "))

count = 0
low = 0
high = 1001
guess = (high + low) // 2

while guess != n:
    if guess < n:
        low = guess
    else:
        high = guess

    guess = (high + low) // 2
    count += 1

print("count:",count)
print("answer:",guess)
