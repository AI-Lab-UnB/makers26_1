# Assume you are given an integer 0 <= N <= 1000. Write a piece of Python code that uses bisection search to
# guess N. The code prints two lines: count: with how many guesses it took to find N, and answer: with the
# value of N. Hints: If the halfway value is exactly in between two integers, choose the smaller one

low = 0
high = 1000
guess = (low + high) / 2
count = 1
N = int

while guess != N:
    
    if guess < N or abs(low - guess) == abs(high - guess):
        low = guess
        
    elif guess > N:
        high = guess
        
    else:
        print(f"{count} iterations")
        print(f"N = {N}")
    count += 1
