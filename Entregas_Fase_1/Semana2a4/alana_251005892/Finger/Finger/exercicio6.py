N = int(input("insira um numero pertencente ao intervalo [0,1000] "))
low = 0
high = 1000
guess = (low + high)//2
contador = 0
while (guess != N):
    if(guess<N):
        low += 1
    else:
        high -=1
    guess = (low + high)//2
    contador = contador +1
print(f'count: {contador}')
print(f'answer: {guess}')
