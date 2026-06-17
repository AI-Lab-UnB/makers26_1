n = 50

count = 0
answer = 0
menor = 0
maior = n

while answer != n:
    count += 1
    answer = (menor + maior) // 2

    if answer < n:
        menor = answer + 1
    elif answer > n:
        maior = answer - 1
    else: 
        break

print("count: ",count)
print("answer: ", answer)
