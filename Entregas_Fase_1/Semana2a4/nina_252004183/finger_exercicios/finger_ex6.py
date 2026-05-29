N = int(input("Digite um número entre 0 e 1000: "))

low = 0
high = 1000
count = 0

while True:
    guess = (low + high) // 2
    count += 1

    if guess == N:
        print("count:", count)
        print("answer:", guess)
        break
    elif guess < N:
        low = guess + 1
    else:
        high = guess - 1