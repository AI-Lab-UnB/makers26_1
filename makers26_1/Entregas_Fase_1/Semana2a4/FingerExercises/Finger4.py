N = int(input())
i=0
Truth = False

while i<=N:
    if i**3==N:
        print(i)
        Truth=True
    i+=1
if not Truth:
    print("Erro")