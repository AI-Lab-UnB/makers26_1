minimo = 0
maximo = 1001

count = 0
answer = (minimo+maximo)//2

while answer != N:
    if answer < N:
        minimo = answer
    elif answer > N:
        maximo = answer
    answer = (minimo+maximo)//2
    count +=1

print(f'count: {count}')
print(f'answer: {answer}')
