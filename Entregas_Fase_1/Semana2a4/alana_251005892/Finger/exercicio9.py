def dot_product(tA, tB):
    soma = sum(a*b for a, b in zip(tA, tB))
    return (len(tA), soma)
n= int(input("qual o tamanho desejado da tupla 1? "))
tA= tuple(int(input(f'digite o numero {i+1} da tupla 1: ')) for i in range(n))
tB= tuple(int(input(f'digite o numero {i+1} de {len(tA)} da tupla2: ')) for i in range(len(tA)))
print(dot_product(tA,tB))