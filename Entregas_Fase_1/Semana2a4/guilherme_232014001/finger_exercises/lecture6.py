x = 4

guess = int(input('Guess the number: '))

while x != guess:
    if guess > x:
        print('Too High')
        guess = int(input('Guess the number: '))
        
    elif guess < x:
        print('Too Low')
        guess = int(input('Guess the number: '))
        
print('Correct')