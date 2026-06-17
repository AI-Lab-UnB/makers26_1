input_str = input("Enter a number")
N = int(input_str)
minimo = N+1
maximo = N-1

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
