N = 700

low = 0
high = 1001
count = 0
guess = 0

while True:
    count += 1
    
    guess = (low + high) // 2
    
    if guess == N:
        break
    elif guess < N:
        low = guess + 1
    else:
        high = guess - 1

print(f"count: {count}")
print(f"answer: {guess}")