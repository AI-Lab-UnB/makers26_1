N = (int(input("Digite um númeoro a ser advinhado: ")))

H = 1001
L = 0
def adivinhar(H,L):
    ((H + L)/2)
contar = 0

while(adivinhar != N):
    adivinhar(H,L)
    if adivinhar < N:
        L = N
    if adivinhar > N:
        H = N
    adivinhar(H, L)
    contar += 1

print(contar)
print(adivinhar)
