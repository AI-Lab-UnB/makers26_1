import math
contador = 0
def count_sqerts (num_list):
    cont = 0
    for i in num_list:
        if i <0:
            continue
        sqrt = math.sqrt(i)
        if sqrt in num_list:
            cont +=1
    return cont
num_list = []
num = int(input("DIgite a quantidade de elementos da lista, a seguir: "))
for i in range(num):
    num_list.append(int(input(f"Digite o elemento {i+1}: ")))
print(count_sqerts(num_list))