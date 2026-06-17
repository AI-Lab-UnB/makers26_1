

a = int(input("Digite o primeiro coeficiente: "))
b = int(input("Digite o segundo coeficiente: "))
c = int(input("Digite o terceiro coeficiente: "))

d = int(input("Digite o quarto coeficiente: "))
e = int(input("Digite o quinto coeficiente: "))
f = int(input("Digite o sexto coeficiente: "))


def delta(a,b,c):
    delta_result = b**2 - 4 * a * c
    return delta_result
    if delta_result < 0:
        print("Delta não pertence aos reais")

def bhaskara_pos(a,b,c):
    bhaskara_result_p = (-b + (delta(a,b,c)**1/2)) / 2*a
    return bhaskara_result_p

def bhaskara_neg(a,b,c):
    bhaskara_result_n = (-b - (delta(a,b,c)**1/2)) / 2*a
    return bhaskara_result_n

delta(a,b,c)
bhaskara_pos(a,b,c)
bhaskara_neg(a,b,c)

delta(d,e,f)
bhaskara_pos(d,e,f)
bhaskara_neg(d,e,f)

total = bhaskara_pos(a,b,c) + bhaskara_pos(d,e,f) + bhaskara_neg(a,b,c) + bhaskara_neg(d,e,f)

print(f"A soma das raízes das duas equações quadráticas é: {total}")