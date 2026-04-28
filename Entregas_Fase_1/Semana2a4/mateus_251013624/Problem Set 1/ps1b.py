salario = float(input("Digite o salario anual: "))
porcentagem_salva = float(input("Digite a parte do salário a ser salva: "))
custo = float(input("Digite o custo da casa: "))
aumento = float(input("Digite o aumento semi-anual: "))
pagamento_inicial = custo /4
salario_mensal = (salario*porcentagem_salva)/12
salvo = 0
meses = 0
while salvo < pagamento_inicial:
    salvo += salario_mensal + salvo * (0.05/12)
    meses += 1
    if meses % 6 == 0:
        salario += salario*aumento
        salario_mensal = (salario * porcentagem_salva) / 12
print("Número de meses para realizar o pagamento inicial: ", meses)