n = int(input())
low=0
high=1000
guess=(high+low)/2
count=0

while guess!=n:
    count+=1
    if guess<n:
        low=guess
    elif guess>n:
        high=guess
    guess=(high+low)/2

print(f"{count}\n{guess}")
