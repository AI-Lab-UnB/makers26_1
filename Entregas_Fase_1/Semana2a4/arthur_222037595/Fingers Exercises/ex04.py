# Finger Exercise - Lecture 4
# Name: Arthur Carvalho Leite
# Matrícula: 222037595

# N já vem definido
# vai incrementando i ate i^3 >= N, depois checa se bateu exato
i = 1
while i**3 < N:
    i += 1

if i**3 == N:
    print(i)
else:
    print('error')
