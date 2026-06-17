# Finger Exercise - Lecture 5
# Name: Arthur Carvalho Leite
# Matrícula: 222037595

# my_str já vem definido
# pega os caracteres nos indices pares (0, 2, 4...)
resultado = ''
for i in range(0, len(my_str), 2):
    resultado += my_str[i]
print(resultado)
