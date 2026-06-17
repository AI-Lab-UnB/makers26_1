# Finger Exercise - Lecture 6
# Name: Arthur Carvalho Leite
# Matrícula: 222037595

# N já vem definido, entre 0 e 1000
# busca binária pra adivinhar N
low = 0
high = 1001
chute = (high + low) // 2
count = 1

while chute != N:
    if chute < N:
        low = chute
    else:
        high = chute
    chute = (high + low) // 2
    count += 1

print("count:", count)
print("answer:", chute)
