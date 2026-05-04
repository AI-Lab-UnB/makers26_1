
entrada = int(input())

achou = False
N = 500
i = 0
while achou is False:
    i+=1
    if entrada == N:
        achou = True
    elif entrada > N:
        N += N//2
    else:
        N -= N//2

print('Passos',i)
