baixo = 0
alto = 1001
chute = (baixo+alto)//2
counter = 0
N = 531

while chute != N:
    if chute < N:
        baixo = N
    else:
        alto = chute
    chute = (baixo+alto)//2
    counter += 1
    
print(f'count: {counter}')
print(f'answer: {chute}')
    