i = 0

while i**3 < N:
    i+=1

if i**3 == N:
    print(N**(1/3))
else:
    print('error')