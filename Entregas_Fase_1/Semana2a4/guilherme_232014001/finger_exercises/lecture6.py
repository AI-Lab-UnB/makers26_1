 N = 742

low = 0
high = 1000
count = 0

while True:
    guess = (low + high) // 2
    count += 1
    
    if guess == N:
        break
    elif guess < N:
        low = guess + 1
    else:
        high = guess - 1

print("count:", count)
print("answer:", guess)