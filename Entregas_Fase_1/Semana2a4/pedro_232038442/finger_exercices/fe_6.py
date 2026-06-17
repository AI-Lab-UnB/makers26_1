N = int(input("Enter a number between 0 and 1000: "))

low = 0
high = 1000
count = 0

while low <= high:
    ans = (low + high) // 2
    count += 1
    if ans == N:
        break
    elif ans < N:
        low = ans + 1
    else:
        high = ans - 1

print(f"Count: {count}")
print(f"Answer: {ans}")
